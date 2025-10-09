from flask import Flask, render_template, abort
import pandas as pd
import os

app = Flask(__name__)

DATA_PATH = os.path.join("data", "compliance_trend.csv")

def load_data():
    """Safely load the compliance trend CSV."""
    try:
        df = pd.read_csv(DATA_PATH)
        required_cols = ["Date", "Compliance", "ResidualRisk", "AuditFindings", "ControlEffectiveness"]
        for col in required_cols:
            if col not in df.columns:
                raise KeyError(f"Missing required column: {col}")
        df["Date"] = pd.to_datetime(df["Date"])
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        abort(500)

@app.route("/")
def dashboard():
    """Default dashboard (original version)."""
    df = load_data()
    latest = df.iloc[-1]
    context = {
        "date": latest["Date"].strftime("%Y-%m-%d"),
        "compliance": round(latest["Compliance"], 2),
        "risk": round(latest["ResidualRisk"], 2),
        "findings": int(latest["AuditFindings"]),
        "effectiveness": round(latest["ControlEffectiveness"] * 100, 1),
        "data_points": len(df),
    }
    return render_template("dashboard.html", **context)

@app.route("/powerbi")
def dashboard_powerbi():
    """Power BI–style enhanced dashboard."""
    df = load_data()
    latest = df.iloc[-1]
    context = {
        "date": latest["Date"].strftime("%Y-%m-%d"),
        "compliance": round(latest["Compliance"], 2),
        "risk": round(latest["ResidualRisk"], 2),
        "findings": int(latest["AuditFindings"]),
        "effectiveness": round(latest["ControlEffectiveness"] * 100, 1),
        "data_points": len(df),
    }
    return render_template("dashboard_powerbi.html", **context)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
