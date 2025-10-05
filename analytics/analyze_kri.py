#!/usr/bin/env python3
import pandas as pd, matplotlib.pyplot as plt, datetime, os

df = pd.read_csv("data/compliance_trend.csv")

# ---- New KPIs ----
df["CEI"] = 100 - (df["ResidualRisk"] * 10)  # Control Effectiveness Index
df["PolicyDrift"] = df["Compliance"].diff().fillna(0)

summary = {
    "Last_Run": datetime.datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
    "Avg_Compliance": round(df["Compliance"].mean(), 2),
    "Avg_ResidualRisk": round(df["ResidualRisk"].mean(), 2),
    "CEI_Trend": round(df["CEI"].iloc[-1], 2),
}

# ---- Charts ----
plt.figure(figsize=(8,4))
plt.plot(df["Date"], df["Compliance"], label="Compliance %", color="green")
plt.plot(df["Date"], df["ResidualRisk"], label="Residual Risk", color="red")
plt.title("Compliance vs Risk Trend")
plt.legend()
plt.tight_layout()
os.makedirs("dashboards", exist_ok=True)
plt.savefig("dashboards/insight_trend.png")

# ---- HTML Report ----
html = f"""
<h2>GRC Analytics & Insight Report</h2>
<p><b>Last Run:</b> {summary['Last_Run']}</p>
<p><b>Average Compliance:</b> {summary['Avg_Compliance']}%</p>
<p><b>Average Residual Risk:</b> {summary['Avg_ResidualRisk']}</p>
<p><b>Current CEI:</b> {summary['CEI_Trend']}</p>
<img src='insight_trend.png' width='600'>
"""
open("dashboards/insight_report.html", "w").write(html)
print("✅ Insight dashboard generated successfully.")
