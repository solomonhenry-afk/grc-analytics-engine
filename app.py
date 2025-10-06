from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

app = Flask(__name__)

def load_data():
    df = pd.read_csv("data/compliance_trend.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

@app.route("/")
def dashboard():
    df = load_data()

    # KPIs
    latest = df.iloc[-1]
    compliance = round(latest["Compliance"], 2)
    risk = round(latest["ResidualRisk"], 2)
    avg_compliance = round(df["Compliance"].mean(), 2)
    avg_risk = round(df["ResidualRisk"].mean(), 2)

    # KPI Gauges
    fig_compliance = go.Figure(go.Indicator(
        mode="gauge+number",
        value=compliance,
        title={"text": "Compliance %"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "green" if compliance > 80 else "orange"}}
    ))

    fig_risk = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk,
        title={"text": "Residual Risk"},
        gauge={"axis": {"range": [0, 10]}, "bar": {"color": "red" if risk > 5 else "yellow"}}
    ))

    # Trend Chart
    trend_fig = px.line(df, x="Date", y=["Compliance", "ResidualRisk"],
                        title="📈 Compliance & Risk Trend Over Time",
                        markers=True)

    # Compliance Distribution Bar
    df["Week"] = df["Date"].dt.isocalendar().week
    bar_fig = px.bar(df, x="Week", y="Compliance",
                     title="Weekly Compliance Overview", color="Compliance",
                     color_continuous_scale="Blues")

    # Convert to HTML
    gauges_html = fig_compliance.to_html(full_html=False, include_plotlyjs=False) + \
                  fig_risk.to_html(full_html=False, include_plotlyjs=False)
    trend_html = trend_fig.to_html(full_html=False, include_plotlyjs=False)
    bar_html = bar_fig.to_html(full_html=False, include_plotlyjs=False)

    return render_template("dashboard.html",
                           compliance=compliance,
                           risk=risk,
                           avg_compliance=avg_compliance,
                           avg_risk=avg_risk,
                           gauges_html=gauges_html,
                           trend_html=trend_html,
                           bar_html=bar_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
