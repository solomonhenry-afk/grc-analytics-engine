#!/usr/bin/env python3
# app.py — Flask + Plotly dashboard for GRC Analytics Engine
from flask import Flask, render_template, abort
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
import json
from pathlib import Path
from datetime import datetime

app = Flask(__name__, template_folder="templates")

DATA_PATH = Path("data/compliance_trend.csv")

def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"{DATA_PATH} not found")
    df = pd.read_csv(DATA_PATH)
    # Ensure Date column
    if "Date" not in df.columns:
        # try to detect
        for c in df.columns:
            if "date" in c.lower() or "time" in c.lower():
                df.rename(columns={c: "Date"}, inplace=True)
                break
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    return df

def make_figures(df):
    # Time series: Compliance & ResidualRisk
    fig_ts = go.Figure()
    fig_ts.add_trace(go.Scatter(
        x=df["Date"], y=df["Compliance"], mode="lines+markers", name="Compliance %",
        line=dict(color="#2b8cff", width=3)
    ))
    fig_ts.add_trace(go.Scatter(
        x=df["Date"], y=df["ResidualRisk"], mode="lines+markers", name="Residual Risk",
        yaxis="y2", line=dict(color="#ff7f50", width=3, dash="dash")
    ))
    fig_ts.update_layout(
        title="Compliance vs Residual Risk",
        xaxis=dict(title="Date"),
        yaxis=dict(title="Compliance (%)", range=[0, 100]),
        yaxis2=dict(title="Residual Risk (score)", overlaying="y", side="right"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(t=60, r=60, l=40, b=40)
    )

    # Audit findings bar
    fig_findings = go.Figure()
    fig_findings.add_trace(go.Bar(
        x=df["Date"], y=df["AuditFindings"], marker_color="#f39c12", name="Open Findings"
    ))
    fig_findings.update_layout(title="Open Audit Findings Over Time", xaxis=dict(title="Date"), yaxis=dict(title="Findings"))

    # Control Effectiveness gauge using latest value
    latest = df.iloc[-1]
    gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=round(latest.get("ControlEffectiveness", 0) * 100, 1),
        delta={'reference': round(df["ControlEffectiveness"].iloc[-2] * 100, 1) if len(df) > 1 else 0},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': '#2b8cff'},
               'steps': [{'range': [0, 50], 'color': '#ff4d4f'}, {'range': [50, 80], 'color': '#ffd666'}, {'range': [80, 100], 'color': '#73d13d'}]},
        title={'text': "Control Effectiveness (%)"}
    ))

    # Trend sparkline for compliance (small)
    spark = go.Figure()
    spark.add_trace(go.Scatter(x=df["Date"], y=df["Compliance"], mode="lines", line=dict(color="#2b8cff")))
    spark.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=80, xaxis=dict(visible=False), yaxis=dict(visible=False))

    # Serialize to JSON for frontend
    figs = {
        "ts": pio.to_json(fig_ts),
        "findings": pio.to_json(fig_findings),
        "gauge": pio.to_json(gauge),
        "spark": pio.to_json(spark)
    }
    return figs, latest

@app.route("/")
def dashboard():
    try:
        df = load_data()
    except Exception as e:
        return abort(500, description=f"Data error: {e}")

    figs, latest = make_figures(df)

    # KPIs
    total_points = len(df)
    latest_date = pd.to_datetime(latest["Date"]).strftime("%Y-%m-%d")
    compliance = float(latest["Compliance"])
    residual = float(latest["ResidualRisk"])
    findings = int(latest.get("AuditFindings", 0))
    control_eff = float(latest.get("ControlEffectiveness", 0))

    # week-over-week or last delta
    prev = df["Compliance"].iloc[-2] if total_points > 1 else compliance
    delta = compliance - prev

    context = {
        "generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "total_points": total_points,
        "latest_date": latest_date,
        "compliance": round(compliance, 2),
        "delta": round(delta, 2),
        "residual": round(residual, 3),
        "findings": findings,
        "control_eff_pct": round(control_eff * 100, 1),
        "figs_json": figs
    }
    return render_template("dashboard.html", **context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
