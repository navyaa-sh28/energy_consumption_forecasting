import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Electricity Load Forecasting", layout="wide")

MODELS = {
    "baseline": "Baseline (same hour last week)",
    "xgb_no_weather": "XGBoost (no weather)",
    "xgb_weather": "XGBoost (with weather)",
}


@st.cache_data
def load_predictions():
    df = pd.read_csv("predictions.csv", index_col=0, parse_dates=True).sort_index()
    return df


@st.cache_data
def load_metrics():
    return pd.read_csv("metrics.csv", index_col=0)


def metrics(actual, pred):
    err = actual - pred
    return {
        "MAE (MW)": float(np.mean(np.abs(err))),
        "RMSE (MW)": float(np.sqrt(np.mean(err ** 2))),
        "MAPE (%)": float(np.mean(np.abs(err / actual)) * 100),
    }


try:
    preds = load_predictions()
    saved_metrics = load_metrics()
except FileNotFoundError as e:
    st.error(f"Missing data file: {e.filename}. Make sure predictions.csv and metrics.csv are in the same folder as app.py.")
    st.stop()

available = {k: v for k, v in MODELS.items() if k in preds.columns}

# ---------------- Header ----------------
st.title("Electricity Load Forecasting")
st.caption("Hourly grid load (MW) forecast with time series ML: baseline vs XGBoost, with and without weather.")
st.info(
    f"**Backtest mode.** This app shows predictions on a held-out test period "
    f"({preds.index.min().date()} to {preds.index.max().date()}) that the models never saw during training. "
    "The data is historical (PJM dataset, ends around 2018), so this is a demonstration of forecast quality, not a live forecast. "
    "Scope: electricity demand only."
)

# ---------------- Sidebar ----------------
st.sidebar.header("Controls")
min_d, max_d = preds.index.min().date(), preds.index.max().date()
start_date = st.sidebar.date_input("Start date", value=min_d, min_value=min_d, max_value=max_d)
window_label = st.sidebar.radio("Window", ["24 hours", "7 days", "30 days"], index=1)
window_hours = {"24 hours": 24, "7 days": 24 * 7, "30 days": 24 * 30}[window_label]
chosen = st.sidebar.multiselect(
    "Models to show",
    options=list(available.keys()),
    default=list(available.keys()),
    format_func=lambda k: available[k],
)

start = pd.Timestamp(start_date)
end = start + pd.Timedelta(hours=window_hours)
win = preds[(preds.index >= start) & (preds.index < end)]

tab1, tab2, tab3 = st.tabs(["Forecast", "Model comparison", "About"])

# ---------------- Forecast tab ----------------
with tab1:
    if win.empty:
        st.warning("No data in this window. Choose an earlier start date.")
    elif not chosen:
        st.warning("Select at least one model in the sidebar.")
    else:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=win.index, y=win["load"], name="Actual", line=dict(width=3, color="#F59E0B")))
        for k in chosen:
            fig.add_trace(go.Scatter(x=win.index, y=win[k], name=available[k], line=dict(width=2, dash="dot")))
        fig.update_layout(
            height=460, margin=dict(l=10, r=10, t=30, b=10),
            yaxis_title="Load (MW)", xaxis_title="Time", hovermode="x unified",
            legend=dict(orientation="h", y=1.08),
        )
        st.plotly_chart(fig, width="stretch")

        st.subheader("Error metrics")
        rows = []
        for k in chosen:
            m_win = metrics(win["load"], win[k])
            m_all = metrics(preds["load"], preds[k])
            rows.append({
                "Model": available[k],
                "MAE window": m_win["MAE (MW)"], "RMSE window": m_win["RMSE (MW)"], "MAPE window (%)": m_win["MAPE (%)"],
                "MAE full test": m_all["MAE (MW)"], "RMSE full test": m_all["RMSE (MW)"], "MAPE full test (%)": m_all["MAPE (%)"],
            })
        st.dataframe(pd.DataFrame(rows).set_index("Model").round(2), width="stretch")
        st.caption("Lower is better. \"Window\" covers the selected dates; \"full test\" covers the entire held-out period.")

        st.download_button("Download this window as CSV", win.to_csv().encode("utf-8"),
                           file_name="forecast_window.csv", mime="text/csv")

# ---------------- Comparison tab ----------------
with tab2:
    st.subheader("Full test-set results from the notebook")
    st.dataframe(saved_metrics.round(2), width="stretch")
    numeric_cols = saved_metrics.select_dtypes("number").columns.tolist()
    if numeric_cols:
        metric_choice = st.selectbox("Chart metric", numeric_cols, index=len(numeric_cols) - 1)
        bar = go.Figure(go.Bar(x=saved_metrics[metric_choice], y=saved_metrics.index, orientation="h"))
        bar.update_layout(height=320, margin=dict(l=10, r=10, t=30, b=10), xaxis_title=f"{metric_choice} (lower is better)")
        st.plotly_chart(bar, width="stretch")
    st.caption("If SARIMA is listed, it was scored on a shorter window than the other models, so it is a reference rather than a direct ranking.")

# ---------------- About tab ----------------
with tab3:
    st.markdown(
        """
**Problem.** Forecast hourly electricity demand from past load and calendar (and optionally weather) information.

**Data.** Kaggle "Hourly Energy Consumption" (PJM Interconnection), one regional file, in MW. Hourly temperature comes from the Open-Meteo historical API.

**Method.**
1. Clean the series: remove duplicate timestamps, force a strict hourly frequency, fill gaps.
2. Build features: hour, day of week, month, weekend, holiday, load 24 hours ago, load 1 week ago, 24-hour rolling mean, and temperature.
3. Split by time: train on earlier years, test on the later period. No random shuffling, so the model never sees the future.
4. Compare a naive baseline (same hour last week) with XGBoost, with and without temperature.
5. Score with MAE, RMSE and MAPE.

**Limitations.**
- The dataset ends around 2018, so results may not reflect current usage.
- Temperature used is observed historical weather; a real deployment would rely on weather forecasts.
- Electricity only, and one region.

Built with Python, pandas, XGBoost, Plotly and Streamlit.
"""
    )
