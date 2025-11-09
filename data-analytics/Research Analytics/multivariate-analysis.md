---
title: Multivariate and Bayesian Analysis Template
category: data-analytics/Research Analytics
tags: [bayesian, data-analytics, data-science, machine-learning, research, statistics, template]
use_cases:
  - Conducting advanced multivariate and Bayesian statistical analysis including Bayesian inference, hierarchical models, and advanced statistical methods for complex research questions.
  - Bayesian inference
  - Advanced statistical modeling
related_templates:
  - statistical-analysis-overview.md
  - regression-analysis.md
  - hypothesis-testing.md
last_updated: 2025-11-09
---

# Multivariate and Bayesian Analysis Template

## Purpose
Conduct advanced multivariate and Bayesian statistical analysis including Bayesian inference, hierarchical models, multiple testing correction, and confidence interval estimation for complex research questions.

## Template

```
You are a Bayesian and multivariate statistics expert. Conduct [ANALYSIS_TYPE] on [DATA_SOURCE] using [BAYESIAN_METHOD] with [PRIOR_SPECIFICATION] priors and [MCMC_METHOD] sampling.

BAYESIAN FRAMEWORK:
Analysis Context:
- Analysis type: [ANALYSIS_TYPE]
- Data source: [DATA_SOURCE]
- Bayesian method: [BAYESIAN_METHOD]
- Prior specification: [PRIOR_SPECIFICATION]
- MCMC method: [MCMC_METHOD]
- Number of iterations: [MCMC_ITERATIONS]
- Burn-in period: [BURN_IN_SAMPLES]
- Credible interval level: [CREDIBLE_INTERVAL_LEVEL]

### BAYESIAN INFERENCE

### Bayesian T-Test
```python
import pymc3 as pm
import arviz as az
import numpy as np

# Bayesian t-test
def bayesian_ttest(group1, group2):
    """Bayesian independent samples t-test"""
    
    # Combine data
    y = np.concatenate([group1, group2])
    group_idx = np.concatenate([np.zeros(len(group1)), np.ones(len(group2))])
    
    with pm.Model() as model:
        # Priors
        mu = pm.Normal('mu', mu=0, sigma=10, shape=2)  # Group means
        sigma = pm.HalfNormal('sigma', sigma=10, shape=2)  # Group stds
        
        # Likelihood
        y_obs = pm.Normal('y_obs', mu=mu[group_idx.astype(int)], 
                         sigma=sigma[group_idx.astype(int)], observed=y)
        
        # Derived quantities
        diff_means = pm.Deterministic('diff_means', mu[0] - mu[1])
        effect_size = pm.Deterministic('effect_size', 
                                     diff_means / pm.math.sqrt((sigma[0]**2 + sigma[1]**2) / 2))
        
        # Sample posterior
        trace = pm.sample(2000, tune=1000, target_accept=0.95, return_inferencedata=True)
    
    # Posterior summary
    summary = az.summary(trace, var_names=['mu', 'sigma', 'diff_means', 'effect_size'])
    
    # Probability that difference > 0
    prob_positive = (trace.posterior.diff_means > 0).mean().values
    
    # Credible intervals
    hdi = az.hdi(trace, credible_interval=0.95)
    
    return {
        'trace': trace,
        'summary': summary,
        'prob_diff_positive': prob_positive,
        'credible_intervals': hdi,
        'model': model
    }
```

### Bayesian Regression
```python
# Bayesian regression
def bayesian_regression(data, outcome_var, predictor_vars):
    """Bayesian linear regression"""
    
    # Prepare data
    X = data[predictor_vars].values
    y = data[outcome_var].values
    
    # Standardize predictors
    X_mean = X.mean(axis=0)
    X_std = X.std(axis=0)
    X_centered = (X - X_mean) / X_std
    
    with pm.Model() as model:
        # Priors
        alpha = pm.Normal('alpha', mu=0, sigma=10)
        beta = pm.Normal('beta', mu=0, sigma=10, shape=X_centered.shape[1])
        sigma = pm.HalfNormal('sigma', sigma=10)
        
        # Linear model
        mu = alpha + pm.math.dot(X_centered, beta)
        
        # Likelihood
        y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y)
        
        # R-squared
        y_mean = y.mean()
        ss_res = pm.math.sum((y - mu)**2)
        ss_tot = pm.math.sum((y - y_mean)**2)
        r_squared = pm.Deterministic('r_squared', 1 - ss_res / ss_tot)
        
        # Sample posterior
        trace = pm.sample(2000, tune=1000, target_accept=0.95, return_inferencedata=True)
    
    return {
        'trace': trace,
        'summary': az.summary(trace),
        'model': model,
        'X_mean': X_mean,
        'X_std': X_std
    }
```

### MULTIPLE TESTING CORRECTION

```python
from statsmodels.stats.multitest import multipletests

# Multiple testing corrections
def multiple_testing_correction(p_values, method='fdr_bh', alpha=0.05):
    """Apply multiple testing corrections"""
    
    methods = ['bonferroni', 'sidak', 'holm-sidak', 'holm', 'simes-hochberg', 
               'hommel', 'fdr_bh', 'fdr_by']
    
    results = {}
    
    for method_name in methods:
        rejected, p_corrected, alpha_sidak, alpha_bonf = multipletests(
            p_values, alpha=alpha, method=method_name
        )
        
        results[method_name] = {
            'rejected': rejected,
            'p_corrected': p_corrected,
            'alpha_corrected': alpha_bonf if method_name == 'bonferroni' else alpha_sidak,
            'num_significant': np.sum(rejected)
        }
    
    return results

# False Discovery Rate Control
def fdr_control(p_values, q_value=0.05):
    """Benjamini-Hochberg FDR control"""
    from statsmodels.stats.multitest import fdrcorrection
    
    rejected, p_corrected = fdrcorrection(p_values, alpha=q_value)
    
    return {
        'rejected': rejected,
        'q_values': p_corrected,
        'num_discoveries': np.sum(rejected),
        'fdr_level': q_value
    }
```

### BOOTSTRAP CONFIDENCE INTERVALS

```python
from scipy import stats
from arch.bootstrap import IIDBootstrap

# Bootstrap confidence intervals
def bootstrap_ci(data, statistic, n_bootstrap=10000, confidence=0.95, method='percentile'):
    """Bootstrap confidence intervals"""
    
    bootstrap_stats = []
    n = len(data)
    
    for _ in range(n_bootstrap):
        sample = np.random.choice(data, size=n, replace=True)
        bootstrap_stats.append(statistic(sample))
    
    bootstrap_stats = np.array(bootstrap_stats)
    
    alpha = 1 - confidence
    
    if method == 'percentile':
        ci_lower = np.percentile(bootstrap_stats, 100 * alpha/2)
        ci_upper = np.percentile(bootstrap_stats, 100 * (1 - alpha/2))
    
    return {
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'bootstrap_distribution': bootstrap_stats,
        'method': method,
        'confidence_level': confidence
    }
```

OUTPUT REQUIREMENTS:
1. **Bayesian Results** - Posterior distributions, credible intervals
2. **MCMC Diagnostics** - Trace plots, R-hat statistics, effective sample size
3. **Multiple Testing** - Corrected p-values, FDR control
4. **Bootstrap Results** - Confidence intervals, distributions
5. **Model Comparison** - Bayes factors, DIC, WAIC
```

## Variables

- [ANALYSIS_TYPE] - Type of analysis to conduct
- [DATA_SOURCE] - Source of data
- [BAYESIAN_METHOD] - Bayesian method to use
- [PRIOR_SPECIFICATION] - Prior distribution specification
- [MCMC_METHOD] - MCMC sampling method
- [MCMC_ITERATIONS] - Number of MCMC iterations
- [BURN_IN_SAMPLES] - Burn-in period
- [CREDIBLE_INTERVAL_LEVEL] - Credible interval level (e.g., 0.95)

## Usage Examples

### Example 1: Bayesian A/B Test
```
ANALYSIS_TYPE: "Bayesian comparison of conversion rates"
BAYESIAN_METHOD: "Bayesian beta-binomial model"
PRIOR_SPECIFICATION: "Weakly informative priors"
MCMC_METHOD: "NUTS sampler"
CREDIBLE_INTERVAL_LEVEL: "0.95"
```

## Best Practices

1. **Choose appropriate priors** - Weakly informative when possible
2. **Check MCMC convergence** - Use R-hat and trace plots
3. **Report credible intervals** - Not just point estimates
4. **Use Bayes factors carefully** - Sensitive to priors
5. **Correct for multiple testing** - When conducting multiple tests
6. **Bootstrap for robustness** - When distributional assumptions uncertain
