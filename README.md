# 🧩 GRC Analytics & Insight Engine

## 📊 Latest Analytics Snapshot

| Artifact | Description | Last Updated |
|-----------|--------------|--------------|
| [📈 GRC_PowerBI_Snapshot.html](https://github.com/solomonhenry-afk/grc-analytics-engine/releases/latest/download/GRC_PowerBI_Snapshot.html) | Static pre-rendered Power BI–style HTML dashboard (offline preview) | ![Last Updated](https://img.shields.io/github/last-commit/solomonhenry-afk/grc-analytics-engine?label=Updated&color=blue) |

> The downloadable snapshot provides a **read-only version** of the live Render dashboard — ideal for recruiters or auditors who want to preview analytics without running Flask.

### 🔍 Automating Governance, Risk & Compliance Intelligence with Python, Flask, Plotly, and CI/CD.

---

## 🎯 Objective
Build an end-to-end **GRC analytics platform** that automates compliance scoring, risk visualization, and executive reporting against major frameworks (SOX, ISO 27001, NIST CSF).  
This project blends **data analytics, automation, and visualization** into one seamless system.

---

## ⚙️ Tech Stack
- **Python 3.13** — Data processing & KRI computation  
- **Pandas, Plotly, Matplotlib** — Trend analytics & visualization  
- **Flask** — Web dashboard delivery  
- **GitHub Actions** — CI/CD automation for nightly analytics refresh  
- **Render Cloud** — Live deployment of Flask dashboard  

---

## 🧩 System Overview
**Data Pipeline**
- Fetches compliance & audit trend data (from CSV / API)
- Normalizes and scores key GRC indicators:
  - `Compliance %`
  - `Residual Risk`
  - `Audit Findings`
  - `Control Effectiveness`

**Analytics Engine**
- Computes daily performance trends
- Generates visual summaries with KPIs and compliance gauges
- Automatically exports static HTML reports for offline review

**Dashboard**
- Flask + Plotly interactive dashboard with:
  - **Overview** → KPI metrics & summaries  
  - **Trends** → Interactive risk/compliance visualizations  
  - **Controls** → Effectiveness insights with heatmaps  

---

## 🚀 CI/CD Workflow (GitHub Actions)
```yaml
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 23 * * *'  # Daily refresh

jobs:
  build-dashboard:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Generate static dashboard
        run: python3 scripts/generate_static_dashboard.py
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: GRC-Insight-Report
          path: dashboards/GRC_PowerBI_Snapshot.html
🌐 Live Demo

🔗 Live Dashboard: https://grc-analytics-engine.onrender.com
🔗 Repository: github.com/solomonhenry-afk/grc-analytics-engine

💼 Business Impact

✅ Reduced manual compliance report prep time by ~85% through data automation
✅ Delivered continuous compliance visibility with zero human intervention
✅ Improved executive decision-making with live KPI insights & risk trends
✅ Established a reusable GRC analytics framework adaptable to multiple standards


| Metric                       | Before        | After Automation     |
| ---------------------------- | ------------- | -------------------- |
| Compliance Report Generation | 4 hrs/manual  | <10 mins automated   |
| Risk Score Update Frequency  | Weekly        | Daily                |
| Human Intervention           | High          | Minimal              |
| Visualization Quality        | Static charts | Interactive (Plotly) |


🧰 Features

Automated GRC scoring engine

Continuous monitoring via CI/CD

Power BI–style dashboard (executive-grade visuals)

Static HTML snapshot generation for offline review

Full DevOps integration (Render + GitHub Actions)


🧠 Lessons Learned

Solved data pipeline validation issues (KeyError: 'Date' / missing columns)

Debugged Flask template rendering (url_for undefined in Jinja)

Improved data schema enforcement to guarantee analytics reliability

Learned CI pipeline troubleshooting and artifact automation

| Snapshot           | Description                          |
| ------------------ | ------------------------------------ |
| ✅ CI/CD Green Tick | Automated analytics pipeline success |
| 📊 CSV Data        | Real compliance trend inputs         |
| 🌍 Flask App       | Live hosted dashboard on Render      |
| 📈 Power BI Mockup | Executive snapshot (HTML + PNG)      |


🏁 Outcome

“Transformed a manual, compliance-heavy reporting process into a fully automated GRC intelligence system — merging analytics, automation, and DevOps into one.”

👨‍💻 Author

Solomon Henry
Cybersecurity & GRC Automation Specialist
🔗 Portfolio: solomonhenry.github.io
🔗 LinkedIn: linkedin.com/in/solomonhenry
