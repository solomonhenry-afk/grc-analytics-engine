#!/usr/bin/env python3
"""
Generate a static HTML snapshot of the GRC Analytics Dashboard
to publish as an artifact in CI.
"""
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from pathlib import Path
from datetime import datetime

data_path = Path("data/compliance_trend.csv")
output_dir = Path("dashboards")
output_dir.mkdir(parents=True, exist_ok=True)
output_html = output_dir / "insight_report.html"

df = pd.read_csv(data_path)
df["Date"] = pd.to_datetime(df["Date"])

latest = df.iloc[-1]

# --- Figures ---
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df["Date"], y=df["Compliance"], mode="lines+markers", name="Compliance %", line=dict(color="#2b8cff", width=3)
))
fig.add_trace(go.Scatter(
    x=df["Date"], y=df["ResidualRisk"], mode="lines+markers", name="Residual Risk", yaxis="y2",
    line=dict(color="#ff7f50", width=3, dash="dash")
))
fig.update_layout(
    title=f"GRC Analytics Report — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
    xaxis=dict(title="Date"),
    yaxis=dict(title="Compliance (%)", range=[0, 100]),
    yaxis2=dict(title="Residual Risk", overlaying="y", side="right"),
    legend=dict(orientation="h", y=1.05, x=0.5, xanchor="center"),
)

pio.write_html(fig, file=str(output_html), include_plotlyjs="cdn", auto_open=False)

print(f"[INFO] Dashboard snapshot saved to {output_html}")
