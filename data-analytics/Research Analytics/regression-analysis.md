---
title: Regression Analysis Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, machine-learning, research, statistics, template]
use_cases:
  - Conducting comprehensive regression analysis to model relationships between variables, make predictions, and quantify variable associations using linear and logistic regression methods.
  - Predictive modeling
  - Relationship analysis
related_templates:
  - statistical-analysis-overview.md
  - hypothesis-testing.md
  - multivariate-analysis.md
last_updated: 2025-11-09
---

# Regression Analysis Template

## Purpose
Conduct comprehensive regression analysis to model relationships between variables, make predictions, and quantify variable associations using linear and logistic regression methods with proper diagnostics.

## Template

```
You are a regression analysis expert. Build a regression model to predict [OUTCOME_VARIABLE] using [PREDICTOR_VARIABLES] on [DATA_SOURCE] with [MODEL_TYPE] regression and validate using [VALIDATION_METHOD].

REGRESSION FRAMEWORK:
Model Context:
- Outcome variable: [OUTCOME_VARIABLE]
- Predictor variables: [PREDICTOR_VARIABLES]
- Model type: [MODEL_TYPE] (Linear/Logistic/Poisson/Cox)
- Sample size: [SAMPLE_SIZE]
- Categorical predictors: [CATEGORICAL_VARIABLES]
- Continuous predictors: [CONTINUOUS_VARIABLES]
- Interaction terms: [INTERACTION_TERMS]
- Expected R²: [EXPECTED_R_SQUARED]

### MULTIPLE LINEAR REGRESSION

### Regression Model Building
```python
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from statsmodels.stats.diagnostic import het_breuschpagan, het_white
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson

# Multiple Linear Regression
def multiple_regression(data, outcome_var, predictor_vars, categorical_vars=None):
    """Comprehensive multiple regression analysis"""

    # Prepare formula
    predictors = ' + '.join(predictor_vars)
    if categorical_vars:
        cat_terms = [f'C({var})' for var in categorical_vars if var in predictor_vars]
        cont_terms = [var for var in predictor_vars if var not in categorical_vars]
        predictors = ' + '.join(cont_terms + cat_terms)

    formula = f'{outcome_var} ~ {predictors}'

    # Fit model
    model = smf.ols(formula, data=data).fit()

    # Model diagnostics
    residuals = model.resid
    fitted_values = model.fittedvalues

    # Heteroscedasticity tests
    bp_stat, bp_p, _, _ = het_breuschpagan(residuals, model.model.exog)
    white_stat, white_p, _, _ = het_white(residuals, model.model.exog)

    # Durbin-Watson test for autocorrelation
    dw_stat = durbin_watson(residuals)

    # Multicollinearity (VIF)
    vif_data = pd.DataFrame()
    vif_data["Variable"] = model.model.exog_names[1:]  # Exclude intercept
    vif_data["VIF"] = [variance_inflation_factor(model.model.exog, i)
                       for i in range(1, model.model.exog.shape[1])]

    # Confidence intervals
    conf_int = model.conf_int()

    # Standardized coefficients (beta weights)
    X = data[predictor_vars]
    y = data[outcome_var]
    X_std = (X - X.mean()) / X.std()
    y_std = (y - y.mean()) / y.std()
    model_std = sm.OLS(y_std, sm.add_constant(X_std)).fit()

    return {
        'model': model,
        'summary': model.summary(),
        'r_squared': model.rsquared,
        'adj_r_squared': model.rsquared_adj,
        'f_statistic': model.fvalue,
        'f_pvalue': model.f_pvalue,
        'aic': model.aic,
        'bic': model.bic,
        'coefficients': model.params,
        'p_values': model.pvalues,
        'confidence_intervals': conf_int,
        'standardized_coefficients': model_std.params[1:],
        'vif_data': vif_data,
        'breusch_pagan_p': bp_p,
        'white_test_p': white_p,
        'durbin_watson': dw_stat,
        'residuals': residuals,
        'fitted_values': fitted_values
    }
```

### LOGISTIC REGRESSION

### Binary Outcome Modeling
```python
# Logistic Regression
def logistic_regression(data, outcome_var, predictor_vars):
    """Logistic regression analysis"""
    # Prepare formula
    predictors = ' + '.join(predictor_vars)
    formula = f'{outcome_var} ~ {predictors}'

    # Fit model
    model = smf.logit(formula, data=data).fit()

    # Odds ratios
    odds_ratios = np.exp(model.params)

    # Classification metrics
    probabilities = model.predict()
    predictions = (probabilities > 0.5).astype(int)

    from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

    cm = confusion_matrix(data[outcome_var], predictions)
    roc_auc = roc_auc_score(data[outcome_var], probabilities)

    return {
        'model': model,
        'summary': model.summary(),
        'pseudo_r_squared': model.prsquared,
        'log_likelihood': model.llf,
        'aic': model.aic,
        'bic': model.bic,
        'coefficients': model.params,
        'p_values': model.pvalues,
        'odds_ratios': odds_ratios,
        'confusion_matrix': cm,
        'roc_auc': roc_auc,
        'probabilities': probabilities,
        'predictions': predictions
    }
```

### MODEL DIAGNOSTICS

### Diagnostic Plots and Tests
```python
import matplotlib.pyplot as plt
import seaborn as sns

def regression_diagnostics(model_results, data):
    """Create comprehensive diagnostic plots"""

    residuals = model_results['residuals']
    fitted = model_results['fitted_values']

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Residuals vs Fitted
    axes[0, 0].scatter(fitted, residuals, alpha=0.5)
    axes[0, 0].axhline(y=0, color='r', linestyle='--')
    axes[0, 0].set_xlabel('Fitted Values')
    axes[0, 0].set_ylabel('Residuals')
    axes[0, 0].set_title('Residuals vs Fitted')

    # Q-Q Plot
    from scipy import stats
    stats.probplot(residuals, dist="norm", plot=axes[0, 1])
    axes[0, 1].set_title('Normal Q-Q Plot')

    # Scale-Location
    standardized_residuals = residuals / np.std(residuals)
    axes[1, 0].scatter(fitted, np.sqrt(np.abs(standardized_residuals)), alpha=0.5)
    axes[1, 0].set_xlabel('Fitted Values')
    axes[1, 0].set_ylabel('√|Standardized Residuals|')
    axes[1, 0].set_title('Scale-Location')

    # Residuals Histogram
    axes[1, 1].hist(residuals, bins=30, edgecolor='black')
    axes[1, 1].set_xlabel('Residuals')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].set_title('Residuals Distribution')

    plt.tight_layout()
    return fig
```

### MODEL VALIDATION

### Cross-Validation and Performance
```python
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def validate_regression_model(data, outcome_var, predictor_vars, cv_folds=5):
    """Perform k-fold cross-validation"""

    X = data[predictor_vars]
    y = data[outcome_var]

    # Initialize model
    model = LinearRegression()

    # K-fold cross-validation
    kfold = KFold(n_splits=cv_folds, shuffle=True, random_state=42)

    # Calculate cross-validated scores
    cv_r2 = cross_val_score(model, X, y, cv=kfold, scoring='r2')
    cv_mse = -cross_val_score(model, X, y, cv=kfold, scoring='neg_mean_squared_error')
    cv_mae = -cross_val_score(model, X, y, cv=kfold, scoring='neg_mean_absolute_error')

    return {
        'cv_r2_mean': cv_r2.mean(),
        'cv_r2_std': cv_r2.std(),
        'cv_mse_mean': cv_mse.mean(),
        'cv_mse_std': cv_mse.std(),
        'cv_mae_mean': cv_mae.mean(),
        'cv_mae_std': cv_mae.std(),
        'cv_scores_detail': {
            'r2_scores': cv_r2,
            'mse_scores': cv_mse,
            'mae_scores': cv_mae
        }
    }
```

OUTPUT REQUIREMENTS:
Deliver comprehensive regression analysis including:

1. **Model Summary**
   - Regression coefficients with standard errors
   - Statistical significance of predictors
   - Confidence intervals for coefficients
   - R-squared and adjusted R-squared

2. **Model Diagnostics**
   - Residual plots and normality assessment
   - Heteroscedasticity tests
   - Multicollinearity assessment (VIF)
   - Influence diagnostics

3. **Model Performance**
   - Goodness of fit measures
   - Prediction accuracy metrics
   - Cross-validation results
   - Model comparison statistics

4. **Interpretation**
   - Standardized coefficients
   - Odds ratios (for logistic regression)
   - Practical significance of effects
   - Model assumptions assessment

5. **Predictions**
   - Predicted values with confidence intervals
   - Prediction intervals
   - Classification metrics (for logistic)
```

## Variables

- `[OUTCOME_VARIABLE]` - Dependent variable to predict
- `[PREDICTOR_VARIABLES]` - Independent variables in model
- `[DATA_SOURCE]` - Source of data for modeling
- `[MODEL_TYPE]` - Type of regression model
- `[VALIDATION_METHOD]` - Method for model validation
- `[SAMPLE_SIZE]` - Total sample size
- `[CATEGORICAL_VARIABLES]` - Categorical predictor variables
- `[CONTINUOUS_VARIABLES]` - Continuous predictor variables
- `[INTERACTION_TERMS]` - Interaction terms to include
- `[EXPECTED_R_SQUARED]` - Expected model R-squared

## Usage Examples

### Example 1: House Price Prediction
```
OUTCOME_VARIABLE: "sale_price"
PREDICTOR_VARIABLES: "square_feet, bedrooms, bathrooms, age, location"
MODEL_TYPE: "Multiple linear regression"
CATEGORICAL_VARIABLES: "location"
CONTINUOUS_VARIABLES: "square_feet, age"
EXPECTED_R_SQUARED: "0.75"
```

### Example 2: Customer Churn
```
OUTCOME_VARIABLE: "churned (binary)"
PREDICTOR_VARIABLES: "tenure, monthly_charges, total_charges, contract_type"
MODEL_TYPE: "Logistic regression"
VALIDATION_METHOD: "5-fold cross-validation"
```

## Best Practices

1. **Check assumptions** - Linearity, independence, homoscedasticity, normality
2. **Assess multicollinearity** - Use VIF to detect correlated predictors
3. **Examine residuals** - Look for patterns indicating model violations
4. **Report standardized coefficients** - For comparing predictor importance
5. **Use robust standard errors** - When heteroscedasticity is present
6. **Validate the model** - Use cross-validation or holdout sample
7. **Check for influential points** - Use Cook's distance and leverage
8. **Interpret coefficients carefully** - Consider units and scaling
