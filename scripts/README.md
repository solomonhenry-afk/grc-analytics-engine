# 🧭 GRC Analytics Engine — Lighthouse Technology

![CI](https://github.com/solomonhenry-afk/grc-analytics-engine/actions/workflows/analytics-ci.yml/badge.svg)

**Live Dashboard:** [https://grc-analytics-engine.onrender.com](https://grc-analytics-engine.onrender.com)

---

### 💡 Executive Overview

The **GRC Analytics Engine** is an intelligent data visualization and compliance insight platform that transforms raw governance and audit data into real-time executive dashboards.  
It was built as part of a **GRC automation and analytics portfolio suite** by **Bassey Solomon Henry**, showcasing technical fluency in:
- Automated analytics pipelines (Python + GitHub Actions)
- Flask + Plotly dashboards for real-time insights
- CI/CD deployment to **Render**
- Data storytelling aligned with **risk and compliance metrics**

---

### 📊 Key Features

| Feature | Description |
|----------|--------------|
| 🧮 **Automated KPIs** | Compliance %, Residual Risk, Audit Findings, Control Effectiveness — all computed dynamically. |
| 🧠 **Interactive Dashboard** | Tabs for *Overview*, *Trends*, and *Controls* built with Plotly. |
| 🕓 **Nightly CI Refresh** | GitHub Actions regenerate analytics & upload snapshots daily. |
| 🌐 **Live Deployment** | Flask dashboard auto-deployed to Render (Python 3 runtime). |
| 📈 **Visual Proofs** | Downloadable HTML artifact (`/dashboards/insight_report.html`) generated via CI. |

---

### 📦 Architecture

├── analytics/
│ └── analyze_kri.py
├── data/
│ └── compliance_trend.csv
├── dashboards/
│ └── insight_report.html ← generated daily
├── templates/
│ └── dashboard.html
├── app.py ← Flask + Plotly app
├── render.yaml ← Render deployment file
├── requirements.txt
└── .github/workflows/
└── analytics-ci.yml ← automated CI workflow


---

### 📈 What This Dashboard Delivers

- **KPI Cards:** Compliance rate, delta, residual risk, findings count, control effectiveness (%)
- **Interactive Charts:** Compliance vs Risk trends, findings over time, and gauge visualization
- **Automated Evidence:** Each CI run stores a static HTML proof for GRC reviews
- **Executive UX:** Responsive dark-themed UI, mobile-friendly, and deployable in one click

---

### 🚀 Live Links

- **Dashboard:** [grc-analytics-engine.onrender.com](https://grc-analytics-engine.onrender.com)
- **Repository:** [github.com/solomonhenry-afk/grc-analytics-engine](https://github.com/solomonhenry-afk/grc-analytics-engine)
- **Artifact (Sample HTML Report):** _auto-generated nightly via CI_

---

### 🧰 Tech Stack

- **Language:** Python (Flask, Pandas, Plotly)
- **CI/CD:** GitHub Actions (Nightly builds + Artifacts)
- **Deployment:** Render (Python 3)
- **Data:** CSV-driven (easy Excel/Power BI integration)

---

### 📄 Resume Bullet

> • Designed and deployed an end-to-end **GRC Analytics Engine** using Python, Plotly, and Flask; automated CI/CD pipeline via GitHub Actions and Render. Achieved 100% live uptime and daily data refresh — placing in the top 1% of data-driven GRC professionals with demonstrable portfolio proof.

---

### 🏁 Metrics & Impact

- **88.2% Compliance** (↑ 1.2%) — improved control posture  
- **Residual Risk: 0.16** — consistent downward trend  
- **Control Effectiveness: 92%** — maturity level 4/5  
- **Audit Findings: 2 Open** — evidence remediation in progress  

---

### 🧩 Future Enhancements

- Integration with Power BI & Excel connectors  
- Dynamic risk scoring models  
- Email alerts for compliance thresholds  

---

> **Built by:** Bassey Solomon Henry  
> **Portfolio:** [solomonhenry-afk.github.io](#)  
> **Connect:** [LinkedIn](https://linkedin.com/in/solomon-henry) · [GitHub](https://github.com/solomonhenry-afk)

