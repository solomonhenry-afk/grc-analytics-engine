import pandas as pd
import plotly.express as px
from pathlib import Path

# Load dataset
df_path = Path("data/compliance_trend.csv")
df = pd.read_csv(df_path)

# Normalize column names
df.columns = [c.strip().capitalize() for c in df.columns]

required_cols = ["Date", "Compliance", "Residualrisk", "Auditfindings", "Controleffectiveness"]
for col in required_cols:
    if col not in df.columns:
        print(f"⚠️ Warning: Missing expected column '{col}', skipping this metric.")
        df[col] = None

# Convert date
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Create basic Plotly chart
fig = px.line(df, x="Date", y="Compliance", title="Compliance Trend Over Time", markers=True)
fig.update_layout(template="plotly_white")

# Save static HTML snapshot
Path("dashboards").mkdir(exist_ok=True)
output_path = Path("dashboards/insight_report.html")
fig.write_html(output_path, include_plotlyjs="cdn")

print(f"✅ Static dashboard generated: {output_path.resolve()}")
