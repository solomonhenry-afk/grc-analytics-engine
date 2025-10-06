import os
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Ensure dashboards/ directory exists
os.makedirs("dashboards", exist_ok=True)

# Load dataset
data_path = "data/compliance_trend.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ CSV file not found: {data_path}")

df = pd.read_csv(data_path)

# Validate required columns
required_cols = ["Date", "Compliance", "ResidualRisk", "AuditFindings", "ControlEffectiveness"]
for col in required_cols:
    if col not in df.columns:
        raise KeyError(f"❌ Missing required column: {col}")

# Create Plotly figure
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["Date"], y=df["Compliance"],
    mode="lines+markers", name="Compliance (%)",
    line=dict(color="green", width=3)
))
fig.add_trace(go.Scatter(
    x=df["Date"], y=df["ResidualRisk"],
    mode="lines+markers", name="Residual Risk",
    yaxis="y2", line=dict(color="red", width=3)
))

fig.update_layout(
    title="GRC Analytics — Compliance vs Risk Trend",
    xaxis_title="Date",
    yaxis=dict(title="Compliance (%)", color="green"),
    yaxis2=dict(title="Residual Risk", overlaying="y", side="right", color="red"),
    legend=dict(x=0.01, y=0.99, bordercolor="gray", borderwidth=1),
    template="plotly_white",
    height=600
)

# Save static HTML snapshot
output_path = "dashboards/insight_report.html"
fig.write_html(output_path, include_plotlyjs="cdn")

print(f"[INFO] ✅ Dashboard generated successfully: {output_path}")
print(f"[INFO] Snapshot timestamp: {datetime.utcnow()} UTC")
