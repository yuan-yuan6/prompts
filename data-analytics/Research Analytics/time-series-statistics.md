---
title: Time Series Statistics Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, forecasting, research, statistics, time-series, template]
use_cases:
  - Conducting time series statistical analysis including trend analysis, seasonality detection, autocorrelation assessment, and temporal pattern identification for longitudinal data.
  - Temporal data analysis
  - Trend analysis
related_templates:
  - statistical-analysis-overview.md
  - regression-analysis.md
  - descriptive-statistics.md
last_updated: 2025-11-09
---

# Time Series Statistics Template

## Purpose
Conduct time series statistical analysis including trend analysis, seasonality detection, autocorrelation assessment, and temporal pattern identification for longitudinal and sequential data.

## Template

```
You are a time series statistics expert. Analyze temporal patterns in [TIME_SERIES_DATA] to identify [TEMPORAL_PATTERNS] using [TIME_SERIES_METHODS] with [TEMPORAL_RESOLUTION] resolution.

TIME SERIES FRAMEWORK:
Analysis Context:
- Time series data: [TIME_SERIES_DATA]
- Temporal patterns: [TEMPORAL_PATTERNS]
- Time series methods: [TIME_SERIES_METHODS]
- Temporal resolution: [TEMPORAL_RESOLUTION]
- Analysis period: [ANALYSIS_PERIOD]
- Frequency: [DATA_FREQUENCY]
- Missing data handling: [MISSING_DATA_METHOD]
- Stationarity requirement: [STATIONARITY_REQUIREMENT]

### TEMPORAL PATTERN ANALYSIS

### Trend and Seasonality Detection
```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, acf, pacf

# Time series decomposition
def decompose_time_series(data, period=12, model='additive'):
    """Decompose time series into trend, seasonal, and residual components"""
    
    decomposition = seasonal_decompose(data, model=model, period=period)
    
    return {
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.resid,
        'observed': decomposition.observed
    }

# Trend analysis
def analyze_trend(data, time_index):
    """Analyze trend in time series"""
    
    from scipy.stats import linregress
    
    # Linear trend
    slope, intercept, r_value, p_value, std_err = linregress(
        range(len(data)), data
    )
    
    # Mann-Kendall test for monotonic trend
    from scipy.stats import kendalltau
    tau, mk_p_value = kendalltau(range(len(data)), data)
    
    return {
        'linear_slope': slope,
        'linear_r_squared': r_value**2,
        'linear_p_value': p_value,
        'mann_kendall_tau': tau,
        'mann_kendall_p': mk_p_value,
        'trend_direction': 'increasing' if slope > 0 else 'decreasing',
        'trend_strength': abs(r_value)
    }
```

### AUTOCORRELATION ANALYSIS

```python
# Autocorrelation analysis
def analyze_autocorrelation(data, nlags=40):
    """Analyze autocorrelation structure"""
    
    # Autocorrelation function
    acf_values = acf(data, nlags=nlags)
    
    # Partial autocorrelation function
    pacf_values = pacf(data, nlags=nlags)
    
    # Ljung-Box test for autocorrelation
    from statsmodels.stats.diagnostic import acorr_ljungbox
    lb_test = acorr_ljungbox(data, lags=nlags)
    
    return {
        'acf': acf_values,
        'pacf': pacf_values,
        'ljung_box_stats': lb_test['lb_stat'].values,
        'ljung_box_pvalues': lb_test['lb_pvalue'].values,
        'significant_lags': np.where(lb_test['lb_pvalue'] < 0.05)[0]
    }
```

### STATIONARITY TESTING

```python
# Stationarity tests
def test_stationarity(data):
    """Test time series stationarity"""
    
    # Augmented Dickey-Fuller test
    adf_result = adfuller(data)
    
    # KPSS test
    from statsmodels.tsa.stattools import kpss
    kpss_result = kpss(data, regression='c')
    
    return {
        'adf_statistic': adf_result[0],
        'adf_pvalue': adf_result[1],
        'adf_critical_values': adf_result[4],
        'is_stationary_adf': adf_result[1] < 0.05,
        'kpss_statistic': kpss_result[0],
        'kpss_pvalue': kpss_result[1],
        'kpss_critical_values': kpss_result[3],
        'is_stationary_kpss': kpss_result[1] > 0.05
    }
```

### TEMPORAL VISUALIZATION

```python
# Time series visualization
def plot_time_series_analysis(data, decomposition=None):
    """Create comprehensive time series plots"""
    
    fig, axes = plt.subplots(4, 1, figsize=(12, 12))
    
    # Original series
    axes[0].plot(data)
    axes[0].set_title('Original Time Series')
    axes[0].set_xlabel('Time')
    axes[0].set_ylabel('Value')
    
    if decomposition:
        # Trend
        axes[1].plot(decomposition['trend'])
        axes[1].set_title('Trend Component')
        
        # Seasonal
        axes[2].plot(decomposition['seasonal'])
        axes[2].set_title('Seasonal Component')
        
        # Residual
        axes[3].plot(decomposition['residual'])
        axes[3].set_title('Residual Component')
    
    plt.tight_layout()
    return fig
```

OUTPUT REQUIREMENTS:
1. **Temporal Patterns** - Trend, seasonality, cycles
2. **Autocorrelation** - ACF, PACF plots and statistics
3. **Stationarity** - ADF and KPSS test results
4. **Decomposition** - Trend, seasonal, residual components
5. **Change Points** - Structural breaks and regime changes
```

## Variables

- [TIME_SERIES_DATA] - Time series data identifier
- [TEMPORAL_PATTERNS] - Patterns to identify (trend/seasonal/cyclical)
- [TIME_SERIES_METHODS] - Methods for analysis
- [TEMPORAL_RESOLUTION] - Time resolution (daily/weekly/monthly)
- [ANALYSIS_PERIOD] - Period of analysis
- [DATA_FREQUENCY] - Data collection frequency
- [MISSING_DATA_METHOD] - Method for handling missing values
- [STATIONARITY_REQUIREMENT] - Whether stationarity required

## Usage Examples

### Example 1: Sales Trend Analysis
```
TIME_SERIES_DATA: "Monthly sales data 2020-2024"
TEMPORAL_PATTERNS: "Trend and seasonality"
TIME_SERIES_METHODS: "Seasonal decomposition, trend testing"
TEMPORAL_RESOLUTION: "Monthly"
DATA_FREQUENCY: "Monthly"
```

### Example 2: Stock Price Analysis
```
TIME_SERIES_DATA: "Daily stock prices"
TEMPORAL_PATTERNS: "Volatility and autocorrelation"
TEMPORAL_RESOLUTION: "Daily"
STATIONARITY_REQUIREMENT: "Yes - required for modeling"
```

## Best Practices

1. **Check for stationarity** - Before applying many models
2. **Handle missing data appropriately** - Use interpolation or forward/backward fill
3. **Test for autocorrelation** - Important for modeling decisions
4. **Visualize temporal patterns** - Always plot time series
5. **Consider multiple decomposition methods** - Additive vs. multiplicative
6. **Test for structural breaks** - Check for change points
