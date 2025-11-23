---
title: Time Series Analysis & Forecasting Framework
category: data-analytics
tags:
- data-analytics
- ai-ml
- framework
- research
use_cases:
- Creating comprehensive framework for time series analysis, forecasting, anomaly
  detection, and pattern recognition including statistical methods, machine learning
  approaches, and real-time streaming analytics.
- Project planning and execution
- Strategy development
related_templates:
- data-analytics/dashboard-design-patterns.md
- data-analytics/data-governance-framework.md
- data-analytics/predictive-modeling-framework.md
last_updated: 2025-11-09
industries:
- finance
- manufacturing
- retail
- technology
type: template
difficulty: intermediate
slug: time-series-analysis
---

# Time Series Analysis & Forecasting Framework

## Purpose
Comprehensive framework for time series analysis, forecasting, anomaly detection, and pattern recognition including statistical methods, machine learning approaches, and real-time streaming analytics.

## Quick Start

Launch your time series analysis in 4 steps:

1. **Characterize Your Data**: Define your time series (e.g., "sales forecasting analyzing 5 metrics with daily frequency, 3 years historical data, forecasting 30 days ahead with 95% accuracy").

2. **Analyze Patterns**: Perform decomposition (trend, seasonal, residual), test for stationarity (ADF test), identify autocorrelation (ACF/PACF plots), and detect seasonality patterns.

3. **Select Forecasting Model**: Choose ARIMA (simple patterns), Prophet (multiple seasonality), LSTM (complex non-linear), XGBoost (feature-rich), or Ensemble (best accuracy) based on data characteristics and accuracy requirements.

4. **Validate and Deploy**: Split data chronologically, perform walk-forward validation, evaluate metrics (RMSE, MAE, MAPE), implement real-time streaming (if needed), and set up anomaly detection alerts.

## Template

Develop time series analysis solution for [DOMAIN] analyzing [METRIC_COUNT] metrics with [DATA_FREQUENCY] frequency, [HISTORY_LENGTH] historical data, forecasting [HORIZON] periods ahead with [ACCURACY_TARGET]% accuracy.

### 1. Time Series Data Characterization

| **Metric** | **Frequency** | **History** | **Seasonality** | **Trend** | **Stationarity** | **Missing Data** |
|-----------|--------------|------------|----------------|----------|-----------------|-----------------|
| [METRIC_1] | [FREQ_1] | [HIST_1] | [SEASON_1] | [TREND_1] | [STATION_1] | [MISSING_1]% |
| [METRIC_2] | [FREQ_2] | [HIST_2] | [SEASON_2] | [TREND_2] | [STATION_2] | [MISSING_2]% |
| [METRIC_3] | [FREQ_3] | [HIST_3] | [SEASON_3] | [TREND_3] | [STATION_3] | [MISSING_3]% |
| [METRIC_4] | [FREQ_4] | [HIST_4] | [SEASON_4] | [TREND_4] | [STATION_4] | [MISSING_4]% |
| [METRIC_5] | [FREQ_5] | [HIST_5] | [SEASON_5] | [TREND_5] | [STATION_5] | [MISSING_5]% |

### 2. Statistical Analysis & Decomposition

**Time Series Components:**
```
Decomposition Analysis:
- Method: [DECOMP_METHOD] (Additive/Multiplicative)
- Trend Component: [TREND_COMP]
- Seasonal Component: [SEASONAL_COMP]
- Residual Component: [RESIDUAL_COMP]

Statistical Tests:
- ADF Test (Stationarity): [ADF_RESULT] (p-value: [ADF_P])
- KPSS Test: [KPSS_RESULT] (p-value: [KPSS_P])
- Ljung-Box (Autocorrelation): [LB_RESULT] (p-value: [LB_P])
- Jarque-Bera (Normality): [JB_RESULT] (p-value: [JB_P])

### Correlation Analysis
- Autocorrelation (ACF): [ACF_LAGS] significant lags
- Partial Autocorrelation (PACF): [PACF_LAGS] significant lags
- Cross-correlation: [CROSS_CORR]
- Granger Causality: [GRANGER_RESULT]
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[DOMAIN]` | Specify the domain | "Retail sales forecasting", "Financial market analysis", "Energy demand prediction", "Supply chain optimization" |
| `[METRIC_COUNT]` | Specify the metric count | "5", "10", "20", "50" |
| `[DATA_FREQUENCY]` | Specify the data frequency | "Daily", "Hourly", "Weekly", "Monthly", "15-minute intervals" |
| `[HISTORY_LENGTH]` | Specify the history length | "3 years", "5 years", "18 months", "10 years" |
| `[HORIZON]` | Specify the horizon | "30 days", "12 months", "7 days", "52 weeks" |
| `[ACCURACY_TARGET]` | Target or intended accuracy | "95 (MAPE < 5%)", "90 (MAPE < 10%)", "98 (critical forecasts)" |
| `[METRIC_1]` | Specify the metric 1 | "Daily sales revenue", "Stock closing price", "Energy consumption (kWh)", "Website traffic" |
| `[FREQ_1]` | Specify the freq 1 | "Daily", "Hourly", "15-min", "Weekly" |
| `[HIST_1]` | Specify the hist 1 | "3 years", "5 years", "2 years", "10 years" |
| `[SEASON_1]` | Specify the season 1 | "Weekly + Yearly", "Daily + Weekly", "Monthly", "None detected" |
| `[TREND_1]` | Specify the trend 1 | "Upward (+5% YoY)", "Downward (-2%)", "Flat", "Non-linear growth" |
| `[STATION_1]` | Specify the station 1 | "Stationary (ADF p<0.05)", "Non-stationary (d=1)", "Trend-stationary" |
| `[MISSING_1]` | Specify the missing 1 | "0.5", "2.3", "0.1", "5.0" |
| `[METRIC_2]` | Specify the metric 2 | "Transaction count", "Trading volume", "Temperature readings", "Page views" |
| `[FREQ_2]` | Specify the freq 2 | "Daily", "Hourly", "5-min", "Weekly" |
| `[HIST_2]` | Specify the hist 2 | "3 years", "2 years", "5 years", "18 months" |
| `[SEASON_2]` | Specify the season 2 | "Weekly", "Daily", "Annual", "Multi-seasonal" |
| `[TREND_2]` | Specify the trend 2 | "Upward", "Stable", "Declining", "Cyclical" |
| `[STATION_2]` | Specify the station 2 | "Stationary", "Unit root (needs differencing)", "Seasonal unit root" |
| `[MISSING_2]` | Specify the missing 2 | "1.2", "0.8", "3.5", "0.2" |
| `[METRIC_3]` | Specify the metric 3 | "Average order value", "Bid-ask spread", "Humidity levels", "Bounce rate" |
| `[FREQ_3]` | Specify the freq 3 | "Daily", "Tick-level", "Hourly", "Weekly" |
| `[HIST_3]` | Specify the hist 3 | "2 years", "3 years", "5 years", "1 year" |
| `[SEASON_3]` | Specify the season 3 | "Monthly", "None", "Diurnal", "Quarterly" |
| `[TREND_3]` | Specify the trend 3 | "Slight upward", "No trend", "Structural break in 2020", "Exponential growth" |
| `[STATION_3]` | Specify the station 3 | "Stationary", "I(1) process", "Cointegrated with metric 1" |
| `[MISSING_3]` | Specify the missing 3 | "0.3", "1.5", "0.0", "2.1" |
| `[METRIC_4]` | Specify the metric 4 | "Customer count", "Volatility index", "Wind speed", "Session duration" |
| `[FREQ_4]` | Specify the freq 4 | "Daily", "Daily close", "10-min", "Daily" |
| `[HIST_4]` | Specify the hist 4 | "4 years", "10 years", "3 years", "2 years" |
| `[SEASON_4]` | Specify the season 4 | "Weekly + Holiday effects", "Low in summer", "Diurnal + seasonal", "Weekly" |
| `[TREND_4]` | Specify the trend 4 | "Growing steadily", "Mean-reverting", "Climate trend", "Declining" |
| `[STATION_4]` | Specify the station 4 | "Non-stationary", "Stationary", "Requires seasonal differencing" |
| `[MISSING_4]` | Specify the missing 4 | "0.8", "0.0", "4.2", "1.0" |
| `[METRIC_5]` | Specify the metric 5 | "Inventory levels", "Market sentiment score", "Solar irradiance", "Conversion rate" |
| `[FREQ_5]` | Specify the freq 5 | "Daily", "Daily", "Hourly", "Daily" |
| `[HIST_5]` | Specify the hist 5 | "3 years", "5 years", "2 years", "3 years" |
| `[SEASON_5]` | Specify the season 5 | "Quarterly", "Weekly sentiment cycles", "Strong annual", "Weekly" |
| `[TREND_5]` | Specify the trend 5 | "Inventory optimization trend", "No clear trend", "Climate-driven", "Improving" |
| `[STATION_5]` | Specify the station 5 | "Stationary after detrending", "I(0)", "Seasonal unit root", "Stationary" |
| `[MISSING_5]` | Specify the missing 5 | "1.5", "0.5", "2.0", "0.7" |
| `[DECOMP_METHOD]` | Specify the decomp method | "STL (Seasonal-Trend Decomposition using LOESS)", "Classical additive", "MSTL (multiple seasonal)", "X-13ARIMA-SEATS" |
| `[TREND_COMP]` | Specify the trend comp | "Linear growth +2.5% annually", "Polynomial degree 2", "Piecewise linear with 3 breakpoints" |
| `[SEASONAL_COMP]` | Specify the seasonal comp | "Weekly (amplitude 15%) + Yearly (amplitude 30%)", "Single 7-day period", "12-month cycle" |
| `[RESIDUAL_COMP]` | Specify the residual comp | "White noise (mean=0, std=120)", "Slight autocorrelation at lag 1", "Heteroscedastic" |
| `[ADF_RESULT]` | Specify the adf result | "Stationary (reject null)", "Non-stationary (fail to reject)", "Stationary after d=1" |
| `[ADF_P]` | Specify the adf p | "0.001", "0.32", "0.048", "0.15" |
| `[KPSS_RESULT]` | Specify the kpss result | "Stationary (fail to reject)", "Non-stationary (reject)", "Trend-stationary" |
| `[KPSS_P]` | Specify the kpss p | "0.10", "0.01", "0.05", "0.15" |
| `[LB_RESULT]` | Specify the lb result | "No autocorrelation (fail to reject)", "Significant autocorrelation", "Borderline" |
| `[LB_P]` | Specify the lb p | "0.45", "0.001", "0.08", "0.23" |
| `[JB_RESULT]` | Specify the jb result | "Normally distributed", "Non-normal (heavy tails)", "Slight skewness" |
| `[JB_P]` | Specify the jb p | "0.12", "0.001", "0.04", "0.35" |
| `[ACF_LAGS]` | Specify the acf lags | "7, 14, 21 (weekly pattern)", "1, 2, 3 (short memory)", "12, 24, 36 (monthly)" |
| `[PACF_LAGS]` | Specify the pacf lags | "1, 2 (AR(2) suggested)", "1, 7 (AR + seasonal)", "1 (AR(1) process)" |
| `[CROSS_CORR]` | Specify the cross corr | "0.72 with marketing spend (lag -7)", "0.85 with temperature", "0.65 with competitor pricing" |
| `[GRANGER_RESULT]` | Specify the granger result | "Marketing Granger-causes sales (p=0.002)", "Temperature causes demand", "Bidirectional causality" |
| `[ARIMA_RMSE]` | Specify the arima rmse | "450", "1250", "85", "2100" |
| `[ARIMA_MAE]` | Specify the arima mae | "320", "890", "62", "1580" |
| `[ARIMA_MAPE]` | Specify the arima mape | "4.5", "6.2", "3.1", "8.5" |
| `[ARIMA_TIME]` | Specify the arima time | "5 sec", "15 sec", "2 sec", "30 sec" |
| `[ARIMA_COMPLEX]` | Specify the arima complex | "Low (interpretable)", "Medium", "Low", "Low" |
| `[ARIMA_SEL]` | Specify the arima sel | "Yes (baseline)", "No", "Yes", "No" |
| `[PROPHET_RMSE]` | Specify the prophet rmse | "420", "1180", "78", "1950" |
| `[PROPHET_MAE]` | Specify the prophet mae | "295", "840", "55", "1420" |
| `[PROPHET_MAPE]` | Specify the prophet mape | "4.1", "5.8", "2.8", "7.8" |
| `[PROPHET_TIME]` | Specify the prophet time | "30 sec", "1 min", "20 sec", "2 min" |
| `[PROPHET_COMPLEX]` | Specify the prophet complex | "Medium (tunable)", "Medium", "Low", "Medium" |
| `[PROPHET_SEL]` | Specify the prophet sel | "Yes (holidays)", "Yes", "No", "Yes" |
| `[LSTM_RMSE]` | Specify the lstm rmse | "380", "1050", "70", "1750" |
| `[LSTM_MAE]` | Specify the lstm mae | "265", "750", "48", "1280" |
| `[LSTM_MAPE]` | Specify the lstm mape | "3.5", "5.2", "2.4", "6.8" |
| `[LSTM_TIME]` | Specify the lstm time | "15 min", "45 min", "10 min", "1 hour" |
| `[LSTM_COMPLEX]` | Specify the lstm complex | "High (GPU needed)", "High", "High", "Very High" |
| `[LSTM_SEL]` | Specify the lstm sel | "Yes (best)", "No", "No", "Yes" |
| `[XGB_RMSE]` | Specify the xgb rmse | "395", "1100", "72", "1820" |
| `[XGB_MAE]` | Specify the xgb mae | "275", "780", "50", "1320" |
| `[XGB_MAPE]` | Specify the xgb mape | "3.8", "5.5", "2.5", "7.2" |
| `[XGB_TIME]` | Specify the xgb time | "2 min", "5 min", "1 min", "8 min" |
| `[XGB_COMPLEX]` | Specify the xgb complex | "Medium (feature eng)", "Medium", "Medium", "Medium" |
| `[XGB_SEL]` | Specify the xgb sel | "Yes", "Yes", "Yes (production)", "No" |
| `[ENS_RMSE]` | Specify the ens rmse | "355", "980", "65", "1650" |
| `[ENS_MAE]` | Specify the ens mae | "248", "695", "45", "1180" |
| `[ENS_MAPE]` | Specify the ens mape | "3.2", "4.8", "2.2", "6.2" |
| `[ENS_TIME]` | Specify the ens time | "20 min", "1 hour", "15 min", "1.5 hours" |
| `[ENS_COMPLEX]` | Specify the ens complex | "Very High (multiple models)", "Very High", "High", "Very High" |
| `[ENS_SEL]` | Specify the ens sel | "Yes (final)", "Yes (final)", "No", "Yes (final)" |
| `[SS_RMSE]` | Specify the ss rmse | "440", "1220", "82", "2050" |
| `[SS_MAE]` | Specify the ss mae | "310", "870", "60", "1520" |
| `[SS_MAPE]` | Specify the ss mape | "4.3", "6.0", "3.0", "8.2" |
| `[SS_TIME]` | Specify the ss time | "10 sec", "25 sec", "5 sec", "45 sec" |
| `[SS_COMPLEX]` | Specify the ss complex | "Medium (Bayesian)", "Medium", "Medium", "Medium" |
| `[SS_SEL]` | Specify the ss sel | "No", "No", "Yes (uncertainty)", "No" |
| `[LAG_COUNT]` | Specify the lag count | "7", "14", "30", "52" |
| `[LAG_EXAMPLES]` | Specify the lag examples | "t-1, t-7, t-14, t-28 (daily)", "t-1, t-24, t-168 (hourly)", "t-1, t-52 (weekly)" |
| `[LAG_IMP]` | Specify the lag imp | "High (0.85 correlation)", "Medium (0.65)", "Critical for AR component" |
| `[LAG_CORR]` | Specify the lag corr | "t-1: 0.92, t-7: 0.78, t-14: 0.65", "Decaying pattern", "Seasonal peaks at 7, 14, 21" |
| `[LAG_PROC]` | Specify the lag proc | "Auto-generated with statsmodels", "Manual selection via PACF", "Recursive feature elimination" |
| `[ROLL_COUNT]` | Specify the roll count | "8", "12", "6", "15" |
| `[ROLL_EXAMPLES]` | Specify the roll examples | "7-day mean, 30-day mean, 7-day std", "24h rolling max/min", "52-week moving average" |
| `[ROLL_IMP]` | Specify the roll imp | "High for trend capture", "Medium for volatility", "Essential for smoothing noise" |
| `[ROLL_CORR]` | Specify the roll corr | "Rolling mean: 0.82, Rolling std: 0.45", "Strong trend correlation", "Moderate predictive power" |
| `[ROLL_PROC]` | Specify the roll proc | "Pandas rolling window", "Exponential weighted moving average", "Custom window functions" |
| `[DATE_COUNT]` | Specify the date count | "2025-01-15" |
| `[DATE_EXAMPLES]` | Specify the date examples | "2025-01-15" |
| `[DATE_IMP]` | Specify the date imp | "2025-01-15" |
| `[DATE_CORR]` | Specify the date corr | "2025-01-15" |
| `[DATE_PROC]` | Specify the date proc | "2025-01-15" |
| `[EXT_COUNT]` | Specify the ext count | "5", "10", "15", "20" |
| `[EXT_EXAMPLES]` | Specify the ext examples | "Weather (temp, precip), Holidays, Marketing spend, Competitor prices", "Economic indicators (GDP, CPI)" |
| `[EXT_IMP]` | Specify the ext imp | "High (explains 25% variance)", "Medium (seasonal adjustment)", "Low (minor improvement)" |
| `[EXT_CORR]` | Specify the ext corr | "Temperature: 0.72, Holiday: 0.55, Marketing: 0.48", "Lagged correlations identified" |
| `[EXT_PROC]` | Specify the ext proc | "API integration for weather", "Manual holiday calendar", "Feature store integration" |
| `[FOUR_COUNT]` | Specify the four count | "4", "6", "10", "12" |
| `[FOUR_EXAMPLES]` | Specify the four examples | "sin/cos pairs for weekly (k=1,2,3)", "Annual harmonics (k=1..6)", "Multi-seasonal Fourier terms" |
| `[FOUR_IMP]` | Specify the four imp | "Critical for seasonal modeling", "High for complex seasonality", "Medium for simple patterns" |
| `[FOUR_CORR]` | Specify the four corr | "Weekly harmonics: 0.75 combined", "Annual: 0.68", "Interaction terms: 0.42" |
| `[FOUR_PROC]` | Specify the four proc | "Prophet auto-generation", "Manual calculation via NumPy", "Statsmodels seasonal components" |
| `[INT_COUNT]` | Specify the int count | "6", "10", "15", "20" |
| `[INT_EXAMPLES]` | Specify the int examples | "Lag1 x DayOfWeek, Temperature x Season, Holiday x Weekend", "Promo x Price interaction" |
| `[INT_IMP]` | Specify the int imp | "Medium (captures non-additive effects)", "High for promo analysis", "Low for simple models" |
| `[INT_CORR]` | Specify the int corr | "Holiday x Weekend: 0.35 incremental", "Temp x Season: 0.28", "Cross-validated importance" |
| `[INT_PROC]` | Specify the int proc | "PolynomialFeatures (sklearn)", "Manual domain-driven creation", "Automatic interaction search" |
| `[ZSCORE_THRESH]` | Specify the zscore thresh | "3.0", "2.5", "3.5", "2.0" |
| `[ZSCORE_ANOM]` | Specify the zscore anom | "45 points (0.5% of data)", "120 anomalies detected", "28 confirmed outliers" |
| `[ZSCORE_FPR]` | Specify the zscore fpr | "2.5", "5.0", "1.5", "8.0" |
| `[ISO_CONTAM]` | Specify the iso contam | "0.01", "0.02", "0.005", "0.05" |
| `[ISO_ANOM]` | Specify the iso anom | "52 anomalies (isolation score > 0.6)", "85 points flagged", "35 confirmed" |
| `[ISO_PREC]` | Specify the iso prec | "85", "78", "92", "70" |
| `[LSTM_THRESH]` | Specify the lstm thresh | "95th percentile reconstruction error", "MAE > 3x baseline", "Dynamic threshold" |
| `[LSTM_ANOM]` | Specify the lstm anom | "38 anomalies detected", "62 sequence anomalies", "25 point anomalies" |
| `[LSTM_RECALL]` | Specify the lstm recall | "92", "88", "95", "85" |
| `[SEASONAL_ANOM]` | Specify the seasonal anom | "15 seasonal outliers (residual > 3 std)", "Holiday-driven anomalies excluded", "8 unexplained" |
| `[CHANGE_POINTS]` | Specify the change points | "3 detected (2020-03, 2021-06, 2023-01)", "COVID structural break", "Policy change point" |
| `[OUTLIER_CLUSTERS]` | Specify the outlier clusters | "2 clusters: system errors (n=12), external events (n=23)", "Spatial clustering of anomalies" |
| `[WINDOW_SIZE]` | Specify the window size | "24 hours", "7 days", "1 hour", "30 minutes" |
| `[UPDATE_FREQ]` | Specify the update freq | "2025-01-15" |
| `[ALERT_LATENCY]` | Specify the alert latency | "50", "100", "500", "1000" |
| `[SEVERITY_LEVELS]` | Specify the severity levels | "Critical, High, Medium, Low", "P1/P2/P3/P4", "Red/Yellow/Green" |
| `[VAR_SET_1]` | Specify the var set 1 | "Sales, Marketing spend, Price", "Revenue, Traffic, Conversion" |
| `[CORR_1]` | Specify the corr 1 | "Sales-Marketing: 0.72, Sales-Price: -0.45", "Strong positive multicollinearity" |
| `[CAUSE_1]` | Specify the cause 1 | "Marketing -> Sales (lag 7d)", "Bidirectional between traffic and revenue" |
| `[LAG_1]` | Specify the lag 1 | "7 days optimal lag", "0-14 day range tested", "Instantaneous for some pairs" |
| `[MODEL_1]` | Specify the model 1 | "VAR(3)", "VARMAX with exogenous", "Vector Error Correction Model" |
| `[PERF_1]` | Specify the perf 1 | "MAPE: 4.2%, RMSE: 450", "Impulse response validated", "Forecast horizon: 30 days" |
| `[VAR_SET_2]` | Specify the var set 2 | "Demand, Inventory, Lead time", "Orders, Shipments, Returns" |
| `[CORR_2]` | Specify the corr 2 | "Demand-Inventory: -0.55", "Orders-Shipments: 0.92 (lagged)" |
| `[CAUSE_2]` | Specify the cause 2 | "Demand drives inventory decisions", "Shipments follow orders with 2-day lag" |
| `[LAG_2]` | Specify the lag 2 | "2-5 days for supply chain", "Lead time varies by product" |
| `[MODEL_2]` | Specify the model 2 | "Structural VAR", "Dynamic factor model", "Bayesian VAR" |
| `[PERF_2]` | Specify the perf 2 | "MAPE: 5.5%, Good for planning", "Captures bullwhip effect" |
| `[VAR_SET_3]` | Specify the var set 3 | "Temperature, Energy demand, Price", "Weather features cluster" |
| `[CORR_3]` | Specify the corr 3 | "Temp-Demand: 0.85 (non-linear)", "Heating/cooling thresholds" |
| `[CAUSE_3]` | Specify the cause 3 | "Weather exogenous driver", "Price responds to demand" |
| `[LAG_3]` | Specify the lag 3 | "0-1 day for weather impact", "Price lags demand by 1 day" |
| `[MODEL_3]` | Specify the model 3 | "ARIMAX with weather", "Neural network with external", "Gradient boosting" |
| `[PERF_3]` | Specify the perf 3 | "MAPE: 3.8% with weather", "20% improvement over baseline" |
| `[VAR_SET_4]` | Specify the var set 4 | "Stock price, Volume, Volatility", "Returns, Sentiment, News" |
| `[CORR_4]` | Specify the corr 4 | "Price-Volume: 0.35", "Volatility clustering (GARCH)" |
| `[CAUSE_4]` | Specify the cause 4 | "News -> Sentiment -> Returns", "Volume predicts volatility" |
| `[LAG_4]` | Specify the lag 4 | "Intraday lags", "Sentiment leads by 1-4 hours" |
| `[MODEL_4]` | Specify the model 4 | "GARCH family", "Multivariate GARCH (DCC)", "HAR-RV model" |
| `[PERF_4]` | Specify the perf 4 | "VaR backtesting passed", "Volatility forecast: 15% MAPE" |
| `[VAR_SET_5]` | Specify the var set 5 | "Customer metrics: LTV, Churn, Engagement", "Product metrics cluster" |
| `[CORR_5]` | Specify the corr 5 | "Engagement-Churn: -0.65", "LTV-Engagement: 0.72" |
| `[CAUSE_5]` | Specify the cause 5 | "Engagement predicts churn", "Product quality -> NPS -> LTV" |
| `[LAG_5]` | Specify the lag 5 | "30-90 day lagged effects", "Quarterly business cycles" |
| `[MODEL_5]` | Specify the model 5 | "Panel VAR", "Hierarchical time series", "Mixed-effects model" |
| `[PERF_5]` | Specify the perf 5 | "Churn prediction AUC: 0.82", "LTV forecast: 12% MAPE" |
| `[TSCV_WINDOW]` | Specify the tscv window | "365 days training", "52 weeks", "90 days", "2 years" |
| `[TSCV_STEP]` | Specify the tscv step | "30 days", "7 days", "1 month", "1 week" |
| `[TSCV_ITER]` | Specify the tscv iter | "12", "24", "52", "36" |
| `[TSCV_ERROR]` | Specify the tscv error | "MAPE: 4.2% +/- 0.8%", "RMSE: 450 +/- 50", "Consistent across folds" |
| `[TSCV_STABLE]` | Specify the tscv stable | "High (std < 10% of mean)", "Medium (some seasonal variation)", "Stable" |
| `[WF_WINDOW]` | Specify the wf window | "180 days initial", "365 days", "90 days rolling", "2 years" |
| `[WF_STEP]` | Specify the wf step | "1 day (daily update)", "7 days", "30 days", "1 week" |
| `[WF_ITER]` | Specify the wf iter | "365", "52", "12", "24" |
| `[WF_ERROR]` | Specify the wf error | "Mean MAPE: 4.5%", "Degradation at horizon +14d", "Stable within 5%" |
| `[WF_STABLE]` | Specify the wf stable | "High (production-ready)", "Good stability", "Minor drift detected" |
| `[BLOCK_WINDOW]` | Specify the block window | "90-day blocks", "Quarterly blocks", "Monthly blocks" |
| `[BLOCK_STEP]` | Specify the block step | "30 days gap", "No gap", "7-day gap" |
| `[BLOCK_ITER]` | Specify the block iter | "8", "12", "24", "4" |
| `[BLOCK_ERROR]` | Specify the block error | "MAPE: 4.8%", "Higher variance than TSCV", "Robust to regime changes" |
| `[BLOCK_STABLE]` | Specify the block stable | "Medium (block-dependent)", "Tests temporal independence", "Useful for regime changes" |
| `[EXP_WINDOW]` | Specify the exp window | "Starting 1 year, expanding", "Minimum 90 days", "Full history" |
| `[EXP_STEP]` | Specify the exp step | "Monthly expansion", "Weekly", "Daily" |
| `[EXP_ITER]` | Specify the exp iter | "24", "36", "52", "12" |
| `[EXP_ERROR]` | Specify the exp error | "Improving trend (more data)", "MAPE: 5.2% -> 3.8%", "Learning curve visible" |
| `[EXP_STABLE]` | Specify the exp stable | "Improving with data", "Shows learning effect", "Good for growth assessment" |
| `[OOS_WINDOW]` | Specify the oos window | "Last 90 days holdout", "Last 6 months", "Last year" |
| `[OOS_ITER]` | Specify the oos iter | "1 (final test)", "3 (multiple horizons)", "12 (monthly)" |
| `[OOS_ERROR]` | Specify the oos error | "MAPE: 4.5% (matches CV)", "Slight degradation expected", "Within tolerance" |
| `[OOS_STABLE]` | Specify the oos stable | "Validated (no overfitting)", "Production-ready", "Matches CV performance" |
| `[INGESTION_RATE]` | Specify the ingestion rate | "10,000", "100,000", "1,000,000", "50,000" |
| `[STREAM_ENGINE]` | Specify the stream engine | "Apache Kafka + Flink", "AWS Kinesis", "Google Pub/Sub + Dataflow", "Apache Spark Streaming" |
| `[WINDOW_TYPES]` | Type or category of window s | "Standard" |
| `[STATE_MGMT]` | Specify the state mgmt | "RocksDB state backend", "In-memory with checkpoints", "Redis for shared state" |
| `[CHECKPOINT_FREQ]` | Specify the checkpoint freq | "Every 1 minute", "Every 5 minutes", "Event-driven", "Every 10,000 records" |
| `[BATCH_SIZE]` | Specify the batch size | "1000 events", "100 events", "5000 events", "Time-based (1 second)" |
| `[PROC_LATENCY]` | Specify the proc latency | "50", "100", "200", "500" |
| `[WATERMARK]` | Specify the watermark | "Event time - 5 seconds", "Processing time", "10-second allowed lateness" |
| `[LATE_DATA]` | Specify the late data | "Side output for late events", "Drop after 1 minute", "Update previous windows" |
| `[JOIN_OPS]` | Specify the join ops | "Stream-stream 30s window join", "Stream-table enrichment", "Temporal join with versioning" |
| `[PRED_FREQ]` | Specify the pred freq | "Every minute", "Every 5 minutes", "Every hour", "On event trigger" |
| `[ALERT_MECH]` | Specify the alert mech | "PagerDuty integration", "Slack webhook", "Email + SMS", "Custom alert service" |
| `[STORAGE_SINKS]` | Specify the storage sinks | "InfluxDB (time series)", "Elasticsearch (search)", "S3 (archive)", "PostgreSQL (structured)" |
| `[DASH_UPDATE]` | Specify the dash update | "2025-01-15" |
| `[API_ENDPOINTS]` | Specify the api endpoints | "/forecast/realtime, /anomaly/detect, /model/retrain", "REST + WebSocket for streaming" |
| `[BEST_PARAMS]` | Specify the best params | "Strong economy, no disruptions, favorable weather", "High demand, low competition" |
| `[BEST_PROB]` | Specify the best prob | "15", "20", "10", "25" |
| `[BEST_RANGE]` | Specify the best range | "+15% to +25% vs baseline", "+20% revenue uplift", "Upper confidence bound" |
| `[BEST_ADJUST]` | Specify the best adjust | "+18", "+22", "+12", "+25" |
| `[BEST_CONF]` | Specify the best conf | "75", "80", "70", "85" |
| `[BASE_PARAMS]` | Specify the base params | "Current trends continue, moderate growth", "Normal seasonality, stable market" |
| `[BASE_PROB]` | Specify the base prob | "60", "55", "65", "50" |
| `[BASE_RANGE]` | Specify the base range | "+3% to +8% growth", "Baseline forecast range", "Mean prediction" |
| `[BASE_ADJUST]` | Specify the base adjust | "+5", "0", "+3", "+7" |
| `[BASE_CONF]` | Specify the base conf | "90", "85", "92", "88" |
| `[WORST_PARAMS]` | Specify the worst params | "Economic downturn, supply chain disruption", "Competitive pressure, regulatory change" |
| `[WORST_PROB]` | Specify the worst prob | "20", "15", "25", "18" |
| `[WORST_RANGE]` | Specify the worst range | "-10% to -20% vs baseline", "Revenue decline scenario", "Lower confidence bound" |
| `[WORST_ADJUST]` | Specify the worst adjust | "-15", "-12", "-20", "-10" |
| `[WORST_CONF]` | Specify the worst conf | "75", "70", "80", "72" |
| `[STRESS_PARAMS]` | Specify the stress params | "Black swan event, pandemic-level disruption", "Major competitor entry, market crash" |
| `[STRESS_PROB]` | Specify the stress prob | "5", "3", "8", "2" |
| `[STRESS_RANGE]` | Specify the stress range | "-30% to -50% extreme", "Tail risk scenario", "VaR 99% level" |
| `[STRESS_ADJUST]` | Specify the stress adjust | "-40", "-35", "-50", "-30" |
| `[STRESS_CONF]` | Specify the stress conf | "60", "55", "65", "50" |
| `[MC_PARAMS]` | Specify the mc params | "10,000 simulations, historical volatility", "Bootstrap residuals, copula for dependencies" |
| `[MC_RANGE]` | Specify the mc range | "5th-95th percentile: -12% to +18%", "Full distribution available", "Quantile forecasts" |
| `[MC_ADJUST]` | Specify the mc adjust | "Mean: +3%, Median: +2%", "Mode at baseline", "Skewed distribution" |
| `[MC_CONF]` | Specify the mc conf | "95", "90", "99", "80" |
| `[ACC_TARGET]` | Target or intended acc | "95 (MAPE < 5%)", "90", "98", "92" |
| `[ACC_CURRENT]` | Specify the acc current | "94.2", "91.5", "96.8", "93.1" |
| `[ACC_1W]` | Specify the acc 1w | "94.5", "92.0", "97.1", "93.5" |
| `[ACC_1M]` | Specify the acc 1m | "94.0", "91.2", "96.5", "92.8" |
| `[ACC_TRIGGER]` | Specify the acc trigger | "If < 90% for 3 consecutive days", "< 88% triggers retrain", "Manual review at < 92%" |
| `[BIAS_TARGET]` | Target or intended bias | "2 (±2%)", "1", "3", "2.5" |
| `[BIAS_CURRENT]` | Specify the bias current | "1.2", "-0.8", "2.1", "0.5" |
| `[BIAS_1W]` | Specify the bias 1w | "0.8", "-1.2", "1.8", "0.3" |
| `[BIAS_1M]` | Specify the bias 1m | "1.5", "-0.5", "2.5", "0.8" |
| `[BIAS_TRIGGER]` | Specify the bias trigger | "If |bias| > 5% for 1 week", "Sustained bias > 3%", "Cumulative bias check" |
| `[DRIFT_TARGET]` | Target or intended drift | "PSI < 0.1", "No significant drift", "KS < 0.05" |
| `[DRIFT_CURRENT]` | Specify the drift current | "PSI: 0.08", "No drift detected", "Minor input drift" |
| `[DRIFT_1W]` | Specify the drift 1w | "PSI: 0.06", "Stable", "0.04" |
| `[DRIFT_1M]` | Specify the drift 1m | "PSI: 0.12", "Slight increase", "0.09" |
| `[DRIFT_TRIGGER]` | Specify the drift trigger | "PSI > 0.2 triggers investigation", "KS test p < 0.01", "ADWIN alert" |
| `[STAB_TARGET]` | Target or intended stab | "CV < 10%", "Std/Mean < 0.1", "Consistent performance" |
| `[STAB_CURRENT]` | Specify the stab current | "CV: 8%", "Stable", "0.07" |
| `[STAB_1W]` | Specify the stab 1w | "CV: 7%", "Very stable", "0.06" |
| `[STAB_1M]` | Specify the stab 1m | "CV: 9%", "Good stability", "0.08" |
| `[STAB_TRIGGER]` | Specify the stab trigger | "CV > 15% triggers review", "Volatility spike detection", "Rolling variance check" |
| `[TIME_TARGET]` | Target or intended time | "60 (1 minute)", "30", "120", "300" |
| `[TIME_CURRENT]` | Specify the time current | "45", "28", "95", "180" |
| `[TIME_1W]` | Specify the time 1w | "42", "25", "88", "165" |
| `[TIME_1M]` | Specify the time 1m | "48", "30", "102", "195" |
| `[TIME_TRIGGER]` | Specify the time trigger | "If > 120s, scale up infrastructure", "SLA breach at 60s", "Auto-scaling at 80%" |

### 3. Forecasting Model Selection

| **Model Type** | **RMSE** | **MAE** | **MAPE** | **Training Time** | **Complexity** | **Selected** |
|---------------|---------|--------|---------|------------------|---------------|-------------|
| ARIMA | [ARIMA_RMSE] | [ARIMA_MAE] | [ARIMA_MAPE]% | [ARIMA_TIME] | [ARIMA_COMPLEX] | [ARIMA_SEL] |
| Prophet | [PROPHET_RMSE] | [PROPHET_MAE] | [PROPHET_MAPE]% | [PROPHET_TIME] | [PROPHET_COMPLEX] | [PROPHET_SEL] |
| LSTM | [LSTM_RMSE] | [LSTM_MAE] | [LSTM_MAPE]% | [LSTM_TIME] | [LSTM_COMPLEX] | [LSTM_SEL] |
| XGBoost | [XGB_RMSE] | [XGB_MAE] | [XGB_MAPE]% | [XGB_TIME] | [XGB_COMPLEX] | [XGB_SEL] |
| Ensemble | [ENS_RMSE] | [ENS_MAE] | [ENS_MAPE]% | [ENS_TIME] | [ENS_COMPLEX] | [ENS_SEL] |
| State Space | [SS_RMSE] | [SS_MAE] | [SS_MAPE]% | [SS_TIME] | [SS_COMPLEX] | [SS_SEL] |

### 4. Feature Engineering

**Feature Categories:**
| **Feature Type** | **Count** | **Examples** | **Importance** | **Correlation** | **Processing** |
|-----------------|----------|-------------|---------------|----------------|---------------|
| Lag Features | [LAG_COUNT] | [LAG_EXAMPLES] | [LAG_IMP] | [LAG_CORR] | [LAG_PROC] |
| Rolling Statistics | [ROLL_COUNT] | [ROLL_EXAMPLES] | [ROLL_IMP] | [ROLL_CORR] | [ROLL_PROC] |
| Date/Time Features | [DATE_COUNT] | [DATE_EXAMPLES] | [DATE_IMP] | [DATE_CORR] | [DATE_PROC] |
| External Variables | [EXT_COUNT] | [EXT_EXAMPLES] | [EXT_IMP] | [EXT_CORR] | [EXT_PROC] |
| Fourier Terms | [FOUR_COUNT] | [FOUR_EXAMPLES] | [FOUR_IMP] | [FOUR_CORR] | [FOUR_PROC] |
| Interaction Terms | [INT_COUNT] | [INT_EXAMPLES] | [INT_IMP] | [INT_CORR] | [INT_PROC] |

### 5. Anomaly Detection

**Anomaly Detection Methods:**
```
Statistical Methods:
- Z-Score: Threshold = [ZSCORE_THRESH]
  Anomalies Detected: [ZSCORE_ANOM]
  False Positive Rate: [ZSCORE_FPR]%

- Isolation Forest: Contamination = [ISO_CONTAM]
  Anomalies Detected: [ISO_ANOM]
  Precision: [ISO_PREC]%

- LSTM Autoencoder: Threshold = [LSTM_THRESH]
  Anomalies Detected: [LSTM_ANOM]
  Recall: [LSTM_RECALL]%

Pattern-Based:
- Seasonal Decomposition: [SEASONAL_ANOM]
- Change Point Detection: [CHANGE_POINTS]
- Outlier Clustering: [OUTLIER_CLUSTERS]

Real-time Detection:
- Sliding Window: [WINDOW_SIZE]
- Update Frequency: [UPDATE_FREQ]
- Alert Latency: [ALERT_LATENCY]ms
- Severity Levels: [SEVERITY_LEVELS]
```

### 6. Multi-variate Analysis

| **Variable Set** | **Correlation Matrix** | **Causality** | **Lead/Lag** | **Model Type** | **Performance** |
|-----------------|----------------------|--------------|-------------|---------------|----------------|
| [VAR_SET_1] | [CORR_1] | [CAUSE_1] | [LAG_1] | [MODEL_1] | [PERF_1] |
| [VAR_SET_2] | [CORR_2] | [CAUSE_2] | [LAG_2] | [MODEL_2] | [PERF_2] |
| [VAR_SET_3] | [CORR_3] | [CAUSE_3] | [LAG_3] | [MODEL_3] | [PERF_3] |
| [VAR_SET_4] | [CORR_4] | [CAUSE_4] | [LAG_4] | [MODEL_4] | [PERF_4] |
| [VAR_SET_5] | [CORR_5] | [CAUSE_5] | [LAG_5] | [MODEL_5] | [PERF_5] |

### 7. Forecast Validation & Backtesting

**Validation Strategy:**
| **Method** | **Window Size** | **Step Size** | **Iterations** | **Avg Error** | **Stability** |
|-----------|----------------|--------------|---------------|--------------|--------------|
| Time Series CV | [TSCV_WINDOW] | [TSCV_STEP] | [TSCV_ITER] | [TSCV_ERROR] | [TSCV_STABLE] |
| Walk-Forward | [WF_WINDOW] | [WF_STEP] | [WF_ITER] | [WF_ERROR] | [WF_STABLE] |
| Blocked CV | [BLOCK_WINDOW] | [BLOCK_STEP] | [BLOCK_ITER] | [BLOCK_ERROR] | [BLOCK_STABLE] |
| Expanding Window | [EXP_WINDOW] | [EXP_STEP] | [EXP_ITER] | [EXP_ERROR] | [EXP_STABLE] |
| Out-of-Sample | [OOS_WINDOW] | N/A | [OOS_ITER] | [OOS_ERROR] | [OOS_STABLE] |

### 8. Real-time Streaming Analytics

```
Streaming Infrastructure:
- Data Ingestion: [INGESTION_RATE] events/sec
- Processing Engine: [STREAM_ENGINE]
- Window Types: [WINDOW_TYPES]
- State Management: [STATE_MGMT]
- Checkpointing: [CHECKPOINT_FREQ]

Stream Processing:
- Micro-batch Size: [BATCH_SIZE]
- Processing Latency: [PROC_LATENCY]ms
- Watermarking: [WATERMARK]
- Late Data Handling: [LATE_DATA]
- Join Operations: [JOIN_OPS]

### Output & Actions
- Prediction Frequency: [PRED_FREQ]
- Alert Mechanisms: [ALERT_MECH]
- Storage Sinks: [STORAGE_SINKS]
- Dashboard Update: [DASH_UPDATE]
- API Endpoints: [API_ENDPOINTS]
```

### 9. Scenario Analysis & Simulation

| **Scenario** | **Parameters** | **Probability** | **Impact Range** | **Forecast Adjustment** | **Confidence** |
|-------------|---------------|----------------|-----------------|----------------------|---------------|
| Best Case | [BEST_PARAMS] | [BEST_PROB]% | [BEST_RANGE] | [BEST_ADJUST]% | [BEST_CONF]% |
| Base Case | [BASE_PARAMS] | [BASE_PROB]% | [BASE_RANGE] | [BASE_ADJUST]% | [BASE_CONF]% |
| Worst Case | [WORST_PARAMS] | [WORST_PROB]% | [WORST_RANGE] | [WORST_ADJUST]% | [WORST_CONF]% |
| Stress Test | [STRESS_PARAMS] | [STRESS_PROB]% | [STRESS_RANGE] | [STRESS_ADJUST]% | [STRESS_CONF]% |
| Monte Carlo | [MC_PARAMS] | N/A | [MC_RANGE] | [MC_ADJUST]% | [MC_CONF]% |

### 10. Performance Monitoring & Optimization

**Model Performance Tracking:**
| **Metric** | **Target** | **Current** | **1-Week Avg** | **1-Month Avg** | **Action Trigger** |
|-----------|-----------|------------|---------------|----------------|-------------------|
| Forecast Accuracy | [ACC_TARGET]% | [ACC_CURRENT]% | [ACC_1W]% | [ACC_1M]% | [ACC_TRIGGER] |
| Bias | <[BIAS_TARGET]% | [BIAS_CURRENT]% | [BIAS_1W]% | [BIAS_1M]% | [BIAS_TRIGGER] |
| Drift Detection | [DRIFT_TARGET] | [DRIFT_CURRENT] | [DRIFT_1W] | [DRIFT_1M] | [DRIFT_TRIGGER] |
| Model Stability | [STAB_TARGET] | [STAB_CURRENT] | [STAB_1W] | [STAB_1M] | [STAB_TRIGGER] |
| Computation Time | <[TIME_TARGET]s | [TIME_CURRENT]s | [TIME_1W]s | [TIME_1M]s | [TIME_TRIGGER] |

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: Financial Market Forecasting
```
Domain: Stock Price Prediction
Frequency: 1-minute bars
History: 5 years
Models: LSTM + ARIMA ensemble
Features: 150+ technical indicators
Accuracy: MAPE < 2%
Latency: <10ms predictions
```

### Example 2: Demand Forecasting
```
Domain: Retail Sales
Frequency: Daily
History: 3 years
Seasonality: Weekly, Monthly, Yearly
Models: Prophet + XGBoost
External: Weather, holidays, promotions
Accuracy: MAPE < 8%
```

### Example 3: IoT Sensor Analytics
```
Domain: Manufacturing Equipment
Frequency: 1-second readings
Metrics: Temperature, Vibration, Pressure
Analysis: Anomaly detection, failure prediction
Method: LSTM Autoencoder
Alert Latency: <100ms
False Positive Rate: <1%
```

## Customization Options

### 1. Data Frequency
- High-frequency (seconds/minutes)
- Hourly
- Daily
- Weekly/Monthly
- Irregular/Event-based

### 2. Forecast Horizon
- Ultra-short (minutes-hours)
- Short-term (days)
- Medium-term (weeks-months)
- Long-term (months-years)
- Mixed horizons

### 3. Analysis Focus
- Point forecasting
- Interval forecasting
- Probabilistic forecasting
- Anomaly detection
- Causal analysis

### 4. Industry Domain
- Finance/Trading
- Retail/E-commerce
- Manufacturing
- Energy/Utilities
- Healthcare

### 5. Deployment Mode
- Batch processing
- Real-time streaming
- Near real-time
- On-demand
- Hybrid batch-stream