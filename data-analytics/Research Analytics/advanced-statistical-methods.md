---
title: Advanced Statistical Methods
category: data-analytics/Research Analytics
tags: ['statistics', 'bayesian', 'non-parametric', 'advanced']
use_cases:
  - Apply advanced statistical methods including Bayesian analysis, non-parametric tests, multiple testing corrections, and specialized statistical techniques.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Advanced Statistical Methods

## Purpose
Apply advanced statistical methods including Bayesian analysis, non-parametric tests, multiple testing corrections, and specialized statistical techniques.

## Quick Start

### For Researchers & Statisticians

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific needs for apply
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine based on results

**Common Use Cases:**
- Apply advanced statistical methods including Bayesian analysis, non-parametric tests, multiple testing corrections, and specialized statistical techniques.
- Project-specific implementations
- Practical applications and deployments



## Template

---
title: Statistical Analysis and Inference Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, design, machine-learning, research, template]
use_cases:
  - Creating conduct comprehensive statistical analysis and inference to test hypotheses, estimate parameters, make predictions, and draw valid conclusions from data using advanced statistical methods and frameworks.

  - Project planning and execution
  - Strategy development
related_templates:
  - dashboard-design-patterns.md
  - data-governance-framework.md
  - predictive-modeling-framework.md
last_updated: 2025-11-09
---


## Purpose
Conduct comprehensive statistical analysis and inference to test hypotheses, estimate parameters, make predictions, and draw valid conclusions from data using advanced statistical methods and frameworks.


Non-Parametric Inference:

BAYESIAN INFERENCE:

Bayesian Analysis Framework:
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

MULTIPLE TESTING CORRECTION:
```python
from statsmodels.stats.multitest import multipletests


# Multiple testing corrections
def multiple_testing_correction(p_values, method='fdr_bh', alpha=0.05):
    """Apply multiple testing corrections"""

    methods = ['bonferroni', 'sidak', 'holm-sidak', 'holm', 'simes-hochberg',
               'hommel', 'fdr_bh', 'fdr_by', 'fdr_tsbh', 'fdr_tsbky']

    results = {}

    for method_name in methods:
        if method_name in ['fdr_tsbh', 'fdr_tsbky']:
            continue  # Skip methods requiring additional parameters

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

Advanced CI Methods:
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
    elif method == 'bias_corrected':
        # Bias-corrected and accelerated (BCa) bootstrap
        observed_stat = statistic(data)
        bias_correction = stats.norm.ppf((bootstrap_stats < observed_stat).mean())

        # Acceleration constant (simplified)
        acceleration = 0  # Would need jackknife estimation for full BCa

        z_alpha_2 = stats.norm.ppf(alpha/2)
        z_1_alpha_2 = stats.norm.ppf(1 - alpha/2)

        alpha_1 = stats.norm.cdf(bias_correction +
                                 (bias_correction + z_alpha_2)/(1 - acceleration * (bias_correction + z_alpha_2)))
        alpha_2 = stats.norm.cdf(bias_correction +
                                 (bias_correction + z_1_alpha_2)/(1 - acceleration * (bias_correction + z_1_alpha_2)))

        ci_lower = np.percentile(bootstrap_stats, 100 * alpha_1)
        ci_upper = np.percentile(bootstrap_stats, 100 * alpha_2)

    return {
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'bootstrap_distribution': bootstrap_stats,
        'method': method,
        'confidence_level': confidence
    }


# Robust confidence intervals
def robust_ci(data, confidence=0.95, method='trimmed_mean'):
    """Robust confidence intervals"""

    if method == 'trimmed_mean':
        # Trimmed mean CI
        trim_prop = 0.1
        from scipy.stats.mstats import trimmed_mean_ci
        ci_lower, ci_upper = trimmed_mean_ci(data, limits=(trim_prop, trim_prop),
                                           alpha=1-confidence)
    elif method == 'median':
        # Median CI using bootstrap
        ci_lower, ci_upper = bootstrap_ci(data, np.median, confidence=confidence)

    return {
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'method': method,
        'confidence_level': confidence
    }

5. **Multiple Testing Correction**

7. **Bayesian Analysis** (if applicable)

### Test Parameters
- [TEST_TYPE] - Type of statistical test
- [ALTERNATIVE] - Alternative hypothesis direction
- [DEGREES_OF_FREEDOM] - Degrees of freedom
- [EQUAL_VAR_ASSUMED] - Whether equal variance assumed
- [CONFIDENCE_LEVEL] - Confidence level (e.g., 0.95)
- [BOOTSTRAP_SAMPLES] - Number of bootstrap samples
- [MCMC_SAMPLES] - Number of MCMC samples
- [MCMC_CHAINS] - Number of MCMC chains
- [BURN_IN] - Burn-in samples for MCMC


### Confidence Intervals
- [CI_LOWER] - Confidence interval lower bound
- [CI_UPPER] - Confidence interval upper bound
- [CI_WIDTH] - Confidence interval width
- [MARGIN_ERROR] - Margin of error
- [BOOTSTRAP_CI_LOWER] - Bootstrap CI lower bound
- [BOOTSTRAP_CI_UPPER] - Bootstrap CI upper bound
- [BAYESIAN_CI_LOWER] - Bayesian credible interval lower
- [BAYESIAN_CI_UPPER] - Bayesian credible interval upper
- [ROBUST_CI_LOWER] - Robust CI lower bound
- [ROBUST_CI_UPPER] - Robust CI upper bound


### Multiple Testing
- [BONFERRONI_ALPHA] - Bonferroni corrected alpha
- [HOLM_ALPHA] - Holm corrected alpha
- [FDR_Q_VALUE] - False discovery rate q-value
- [BENJAMINI_HOCHBERG_P] - B-H corrected p-values
- [SIDAK_ALPHA] - Šidák corrected alpha
- [NUM_COMPARISONS] - Number of comparisons
- [FAMILY_WISE_ERROR] - Family-wise error rate
- [FALSE_DISCOVERY_RATE] - False discovery rate
- [NUM_REJECTED] - Number of rejected hypotheses


### Regression Variables
- [REGRESSION_FORMULA] - Regression model formula
- [PREDICTOR_VARIABLES] - List of predictor variables
- [INTERCEPT] - Regression intercept
- [SLOPE_COEFFICIENT] - Slope coefficient
- [REGRESSION_COEFFICIENTS] - All regression coefficients
- [STANDARD_ERRORS] - Standard errors of coefficients
- [T_VALUES] - T-values for coefficients
- [COEFFICIENT_P_VALUES] - P-values for coefficients
- [VIF_VALUES] - Variance inflation factors
- [RESIDUALS] - Model residuals
- [FITTED_VALUES] - Fitted values
- [STANDARDIZED_RESIDUALS] - Standardized residuals
- [COOK_DISTANCES] - Cook's distances
- [LEVERAGE_VALUES] - Leverage values
- [DFBETAS] - DFBETAS values
- [MODEL_AIC] - Akaike Information Criterion
- [MODEL_BIC] - Bayesian Information Criterion
- [LOG_LIKELIHOOD] - Log-likelihood
- [PSEUDO_R_SQUARED] - Pseudo R-squared (logistic)


### Bayesian Analysis
- [PRIOR_DISTRIBUTION] - Prior distribution specification
- [POSTERIOR_DISTRIBUTION] - Posterior distribution
- [POSTERIOR_MEAN] - Posterior mean
- [POSTERIOR_MEDIAN] - Posterior median
- [POSTERIOR_MODE] - Posterior mode
- [POSTERIOR_SD] - Posterior standard deviation
- [CREDIBLE_INTERVAL_LOWER] - Credible interval lower bound
- [CREDIBLE_INTERVAL_UPPER] - Credible interval upper bound
- [BAYES_FACTOR] - Bayes factor
- [POSTERIOR_PROBABILITY] - Posterior probability
- [PRIOR_ODDS] - Prior odds
- [POSTERIOR_ODDS] - Posterior odds
- [EVIDENCE] - Model evidence
- [DIC] - Deviance Information Criterion
- [WAIC] - Watanabe-Akaike Information Criterion
- [RHAT] - R-hat convergence diagnostic
- [EFFECTIVE_SAMPLE_SIZE] - Effective sample size
- [MCMC_DIAGNOSTICS] - MCMC diagnostics summary


### Non-parametric Tests
- [MANN_WHITNEY_U] - Mann-Whitney U statistic
- [WILCOXON_W] - Wilcoxon W statistic
- [KRUSKAL_WALLIS_H] - Kruskal-Wallis H statistic
- [FRIEDMAN_STATISTIC] - Friedman test statistic
- [SIGN_TEST_STATISTIC] - Sign test statistic
- [RUNS_TEST_STATISTIC] - Runs test statistic
- [MEDIAN_TEST_STATISTIC] - Median test statistic
- [EPSILON_SQUARED] - Epsilon-squared effect size
- [RANK_SUM_1] - Rank sum for group 1
- [RANK_SUM_2] - Rank sum for group 2
- [TIED_RANKS] - Number of tied ranks
- [CONTINUITY_CORRECTION] - Continuity correction applied


### Sensitivity Analysis
- [SENSITIVITY_METHODS] - Sensitivity analysis methods
- [ROBUST_RESULTS] - Robust analysis results
- [ALTERNATIVE_TESTS] - Alternative test results
- [BOOTSTRAP_RESULTS] - Bootstrap analysis results
- [JACKKNIFE_RESULTS] - Jackknife analysis results
- [LEAVE_ONE_OUT] - Leave-one-out analysis
- [INFLUENCE_MEASURES] - Influence measures
- [STABILITY_CHECK] - Stability check results


MULTIPLE_TESTING: "Bonferroni correction for multiple metrics"
```


SPHERICITY_CHECK: "Mauchly's test with Greenhouse-Geisser correction"
```


## Customization Options

1. **Statistical Approach**
   - Frequentist inference
   - Bayesian inference
   - Nonparametric methods
   - Robust statistics
   - Bootstrap procedures

2. **Study Design**
   - Experimental designs
   - Observational studies
   - Longitudinal studies
   - Cross-sectional studies
   - Case-control studies

3. **Analysis Complexity**
   - Simple comparisons
   - Multivariable analysis
   - Multilevel modeling
   - Structural equation modeling
   - Machine learning integration

4. **Field Application**
   - Clinical research
   - Social sciences
   - Business analytics
   - Educational research
   - Public health
   - Engineering studies

5. **Output Format**
   - Academic publication
   - Technical report
   - Executive summary
   - Regulatory submission
   - Conference presentation

## Variables

- Primary outcome: [PRIMARY_OUTCOME]
- Secondary outcomes: [SECONDARY_OUTCOMES]
- Primary predictor: [PRIMARY_PREDICTOR]
- Covariates: [COVARIATES]
- Confounding variables: [CONFOUNDERS]
- Mediating variables: [MEDIATORS]
- Moderating variables: [MODERATORS]
- Stratification variables: [STRATIFICATION_VARS]

## Usage Examples

### Example 3: A/B Testing
```
RESEARCH_OBJECTIVE: "Compare conversion rates between website versions"
STUDY_TYPE: "Online controlled experiment"
TEST_TYPE: "Chi-square test of independence"
EFFECT_SIZE_W: "0.1"
SAMPLE_SIZE_PER_GROUP: "5000"
MULTIPLE_TESTING: "Bonferroni correction for multiple metrics"
```


### Example 4: Longitudinal Analysis
```
RESEARCH_OBJECTIVE: "Track changes in cognitive performance over time"
STUDY_TYPE: "Longitudinal cohort study"
TEST_TYPE: "Repeated measures ANOVA"
TIME_POINTS: "4 assessments over 2 years"
SPHERICITY_CHECK: "Mauchly's test with Greenhouse-Geisser correction"
```


## Best Practices

1. **Focus**: Concentrate on the specific aspect covered by this template
2. **Integration**: Combine with related templates for comprehensive solutions
3. **Iteration**: Start simple and refine based on results
4. **Documentation**: Track your parameters and customizations

## Tips for Success

- Begin with the Quick Start section
- Customize variables to your specific context
- Validate outputs against your requirements
- Iterate and refine based on results

## Related Resources

See the overview file for the complete collection of related templates.

---

**Note:** This focused template is part of a comprehensive collection designed for improved usability.
