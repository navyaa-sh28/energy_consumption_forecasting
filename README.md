# Electricity Load Forecasting (Time Series ML)

Streamlit app that shows hourly electricity load forecasts on a held-out test period,
comparing a naive baseline with XGBoost (with and without weather).

**Live app:** _add your Streamlit link here after deploying_

## Files
- `app.py` - the Streamlit app
- `predictions.csv` - actual load and each model's predictions on the test period (from the Colab notebook)
- `metrics.csv` - full test-set MAE, RMSE, MAPE for every model
- `xgb_model.json`, `features.json` - the trained model and its feature list (not needed to run the app)
- `requirements.txt` - dependencies

## Run locally
```
pip install -r requirements.txt
streamlit run app.py
```

## Deploy
Push this folder to a public GitHub repository, then create a new app at share.streamlit.io,
choose the repository, branch and `app.py`.

## Notes
Backtest on historical PJM data (ends around 2018). Not a live forecast. Electricity demand only.
Data source: Kaggle "Hourly Energy Consumption" (check its licence before redistributing data).
