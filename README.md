# Electricity Load Forecasting — Energy Consumption Forecasting

[![Streamlit](https://img.shields.io/badge/Streamlit-App-orange)](https://energyconsumptionforecasting-3abkbqypyaj6zna7ltvq5s.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Repo Size](https://img.shields.io/github/repo-size/navyaa-sh28/energy_consumption_forecasting)](https://github.com/navyaa-sh28/energy_consumption_forecasting)


A polished, production-friendly repository for hourly electricity load forecasting. This project demonstrates data ingestion, exploratory analysis, feature engineering, model training (baseline and ML models), evaluation, and a simple Streamlit demo.

---

Hero demo

> Live interactive demo: https://energyconsumptionforecasting-3abkbqypyaj6zna7ltvq5s.streamlit.app/

![Demo placeholder](docs/images/hero_demo.gif)

---

Why this project

- Real-world hourly electricity load forecasting (PJM dataset)
- Reproducible notebooks and scripts for model training and evaluation
- Clear experiments: baseline vs. XGBoost (with/without weather)
- Lightweight Streamlit app to explore forecasts and model comparisons

---

Quick links

- app: `app.py` (Streamlit demo)
- data: `predictions.csv`, original dataset link
- notebooks: Colab / Jupyter notebooks for EDA and experiments

---

Table of contents

- [Quickstart](#quickstart)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Architecture](#architecture)
- [Visualizations](#visualizations)
- [Project structure](#project-structure)
- [Contributing](#contributing)
- [License & Contact](#license--contact)

---

Quickstart

1. Clone the repo:

```bash
git clone https://github.com/navyaa-sh28/energy_consumption_forecasting.git
cd energy_consumption_forecasting
```

2. Install dependencies and run the Streamlit demo:

```bash
pip install -r requirements.txt
streamlit run app.py
```

3. Open the demo link above or visit the hosted app to explore forecasts and model comparisons.

---

Installation

Create and activate a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

If you need the main dependencies quickly:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost lightgbm prophet streamlit
```

---

Data

This project uses the "Hourly Energy Consumption" dataset by Rob Mulla (Kaggle):
https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption

- The repository includes `predictions.csv` (actuals + model outputs) used in the demo.
- Expected schema: timestamp, load (MW), optional weather features (temperature, humidity).

---

Architecture

High-level pipeline:

```mermaid
flowchart LR
  A[Raw data (CSV / API)] --> B[Ingestion & validation]
  B --> C[Preprocessing & feature engineering]
  C --> D[Train / validation split]
  D --> E[Model training (XGBoost / Baseline)]
  E --> F[Evaluation & visualizations]
  F --> G[Export artifacts (predictions, metrics, model files)]
  G --> H[Streamlit demo / Reports]
  style E fill:#ffd07a,stroke:#333,stroke-width:1px
  style H fill:#c3f0ff,stroke:#333,stroke-width:1px
```

This simple diagram shows the flow from raw data to demo and reporting. Add further details in `notebooks/`.

---

Visualizations & Results

Examples included or easily produced with the notebooks and demo:

- Actual vs Predicted time series (hourly)
- Residuals over time and error distribution (MAE / RMSE / MAPE)
- Feature importance (for XGBoost)
- Model comparison table and metrics CSV

Example plot snippet (notebook):

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('predictions.csv', parse_dates=['timestamp']).set_index('timestamp')
plt.figure(figsize=(14,5))
plt.plot(df['load'], label='Actual', alpha=0.8)
plt.plot(df['xgb_pred'], label='XGBoost', alpha=0.9)
plt.legend()
plt.title('Actual vs XGBoost Prediction — Hourly Load')
plt.show()
```

Add your own `docs/images/` screenshots or export figures from notebooks and replace the placeholders in this README to make it more attractive.

---

Project structure

```
energy_consumption_forecasting/
├─ app.py                 # Streamlit demo
├─ notebooks/             # EDA and modeling notebooks (Colab / Jupyter)
├─ predictions.csv        # actuals and model outputs used in demo
├─ xgb_model.json         # trained XGBoost model (optional)
├─ features.json          # feature list used by model
├─ requirements.txt       # dependencies
├─ README.md              # this file
└─ docs/
   └─ images/             # screenshots, gifs, diagrams (placeholders)
```

---

How to improve this README (suggested next steps)

- Add a short GIF or 3–4 screenshots in docs/images showing the Streamlit app and a few plots.
- Include a small example notebook link (Colab) that runs end-to-end on a subset of the data.
- Add badges for CI, code coverage, and license (if available) to build trust.

---

Contributing

Contributions welcome! Please:

1. Fork the repo
2. Create a topic branch: `git checkout -b feat/your-feature`
3. Open a PR with a clear description and tests / demo

---

License & Contact

MIT © Navyaa Sh
Project: https://github.com/navyaa-sh28/energy_consumption_forecasting
