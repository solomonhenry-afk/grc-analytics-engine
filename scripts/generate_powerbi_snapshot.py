"""
Generate static Power BI–style dashboard snapshot for GRC Analytics.
Outputs: dashboards/GRC_PowerBI_Snapshot.html
"""

import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader

# ---- Paths ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE_DIR)
DATA_PATH = os.path.join(ROOT, "data", "compliance_trend.csv")
TEMPLATE_PATH = os.path.join(ROOT, "templates")
OUTPUT_DIR = os.path.join(ROOT, "dashboards")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "GRC_PowerBI_Snapshot.html")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---- Load Data ----
df = pd.read_csv(DATA_PATH)
required_cols = ["Date", "Compliance", "ResidualRisk", "AuditFindings", "ControlEffectiveness"]
for col in required_cols:
    if col not in df.columns:
        raise KeyError(f"❌ Missing required column: {col}")

df["Date"] = pd.to_datetime(df["Date"])
latest = df.iloc[-1]

context = {
    "date": latest["Date"].strftime("%Y-%m-%d"),
    "compliance": round(latest["Compliance"], 2),
    "risk": round(latest["ResidualRisk"], 2),
    "findings": int(latest["AuditFindings"]),
    "effectiveness": round(latest["ControlEffectiveness"] * 100, 1),
    "data_points": len(df),
}

# ---- Render Template ----
env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
template = env.get_template("dashboard_powerbi.html")
html_output = template.render(**context)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"✅ Static Power BI snapshot created: {OUTPUT_FILE}")
