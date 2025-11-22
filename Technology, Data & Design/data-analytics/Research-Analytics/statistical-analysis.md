---
title: Statistical Analysis and Inference Template
category: data-analytics
tags:
- data-analytics
- ai-ml
- design
- research
use_cases:
- Creating conduct comprehensive statistical analysis and inference to test hypotheses,
  estimate parameters, make predictions, and draw valid conclusions from data using
  advanced statistical methods and frameworks.
- Project planning and execution
- Strategy development
related_templates:
- data-analytics/dashboard-design-patterns.md
- data-analytics/data-governance-framework.md
- data-analytics/predictive-modeling-framework.md
last_updated: 2025-11-09
industries:
- education
- government
- healthcare
- technology
type: template
difficulty: intermediate
slug: statistical-analysis
---

# Statistical Analysis and Inference Template

## Purpose
Conduct comprehensive statistical analysis and inference to test hypotheses, estimate parameters, make predictions, and draw valid conclusions from data using advanced statistical methods and frameworks.

## Quick Start

**Example: Analyzing A/B Test Results for E-commerce Conversion Rates**

```
You are a statistical analysis expert. Analyze A/B test results for a website redesign campaign comparing conversion rates between the control group (original design) and treatment group (new design) using hypothesis testing and effect size analysis.

DATA OVERVIEW:
- Control group: 5,000 visitors, 250 conversions (5.0% conversion rate)
- Treatment group: 5,000 visitors, 310 conversions (6.2% conversion rate)
- Test duration: 14 days
- Statistical significance level: α = 0.05
- Minimum detectable effect: 1% absolute difference

ANALYSIS TASKS:
1. Perform two-proportion z-test to determine if the difference is statistically significant
2. Calculate effect size (Cohen's h) and confidence intervals (95%)
3. Check for confounding variables (day-of-week effects, traffic sources)
4. Assess statistical power and sample size adequacy
5. Test assumptions (independence, normality if applicable)
6. Provide business recommendations based on statistical evidence

EXPECTED OUTPUT:
- Hypothesis test results with p-values and test statistics
- 95% confidence intervals for conversion rate difference
- Effect size interpretation (small/medium/large)
- Power analysis showing achieved power
- Visual comparison of conversion rates with error bars
- Recommendation: Implement new design or continue testing
```

## Template

```
You are a statistical inference expert. Conduct comprehensive statistical analysis on [DATA_SOURCE] to investigate [RESEARCH_QUESTION] using [STATISTICAL_METHODS] with focus on [INFERENCE_TYPE].

RESEARCH FRAMEWORK:
Study Design:
- Research objective: [RESEARCH_OBJECTIVE]
- Study type: [STUDY_TYPE] (Experimental/Observational/Meta-analysis/Systematic Review)
- Design: [DESIGN_TYPE] (RCT/Cohort/Case-Control/Cross-sectional/Longitudinal)
- Population: [TARGET_POPULATION]
- Sample frame: [SAMPLING_FRAME]
- Unit of analysis: [UNIT_OF_ANALYSIS]
- Time horizon: [TIME_HORIZON]

### Hypotheses
- Research question: [PRIMARY_RESEARCH_QUESTION]
- Statistical hypotheses: [STATISTICAL_HYPOTHESES]
- Null hypothesis (H₀): [NULL_HYPOTHESIS]
- Alternative hypothesis (H₁): [ALTERNATIVE_HYPOTHESIS]
- Direction: [HYPOTHESIS_DIRECTION] (One-tailed/Two-tailed)
- Type I error rate (α): [ALPHA_LEVEL]
- Type II error rate (β): [BETA_LEVEL]
- Statistical power (1-β): [STATISTICAL_POWER]

### Variables
- Primary outcome: [PRIMARY_OUTCOME]
- Secondary outcomes: [SECONDARY_OUTCOMES]
- Primary predictor: [PRIMARY_PREDICTOR]
- Covariates: [COVARIATES]
- Confounding variables: [CONFOUNDERS]
- Mediating variables: [MEDIATORS]
- Moderating variables: [MODERATORS]
- Stratification variables: [STRATIFICATION_VARS]

### POWER ANALYSIS AND SAMPLE SIZE
### Power Calculations
```r
# Load required libraries
library(pwr)
library(pwrss)
library(WebPower)

# T-test power analysis
power_ttest <- pwr.t.test(
    n = [SAMPLE_SIZE_PER_GROUP],
    d = [EFFECT_SIZE_COHENS_D],
    sig.level = [ALPHA_LEVEL],
    power = [DESIRED_POWER],
    type = "[TEST_TYPE]",  # two.sample, one.sample, paired
    alternative = "[ALTERNATIVE]"  # two.sided, greater, less
)

# ANOVA power analysis
power_anova <- pwr.anova.test(
    k = [NUMBER_OF_GROUPS],
    n = [SAMPLE_SIZE_PER_GROUP],
    f = [EFFECT_SIZE_F],
    sig.level = [ALPHA_LEVEL],
    power = [DESIRED_POWER]
)

# Regression power analysis
power_regression <- pwr.f2.test(
    u = [NUMERATOR_DF],
    v = [DENOMINATOR_DF],
    f2 = [EFFECT_SIZE_F2],
    sig.level = [ALPHA_LEVEL],
    power = [DESIRED_POWER]
)

# Proportion test power analysis
power_prop <- pwr.2p.test(
    h = [EFFECT_SIZE_H],
    n = [SAMPLE_SIZE_PER_GROUP],
    sig.level = [ALPHA_LEVEL],
    power = [DESIRED_POWER],
    alternative = "[ALTERNATIVE]"
)

# Chi-square test power analysis
power_chisq <- pwr.chisq.test(
    w = [EFFECT_SIZE_W],
    N = [TOTAL_SAMPLE_SIZE],
    df = [DEGREES_OF_FREEDOM],
    sig.level = [ALPHA_LEVEL],
    power = [DESIRED_POWER]
)

# Correlation power analysis
power_corr <- pwr.r.test(
    n = [SAMPLE_SIZE],
    r = [CORRELATION_COEFFICIENT],
    sig.level = [ALPHA_LEVEL],
    power = [DESIRED_POWER],
    alternative = "[ALTERNATIVE]"
)

# Print results
print(paste("Required sample size:", ceiling(power_analysis$n)))
print(paste("Achieved power:", power_analysis$power))
```

Sample Size Determination:
- Minimum detectable effect: [MINIMUM_EFFECT]
- Expected effect size: [EXPECTED_EFFECT_SIZE]
- Required sample size: [REQUIRED_N]
- Planned sample size: [PLANNED_N]
- Attrition rate: [ATTRITION_RATE]%
- Final sample size: [FINAL_N]
- Power achieved: [ACHIEVED_POWER]
- Precision: [CONFIDENCE_INTERVAL_WIDTH]

### DESCRIPTIVE ANALYSIS
### Data Exploration
```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.descriptivestats import describe

# Comprehensive descriptive statistics
def comprehensive_describe(data, variables):
    """Generate comprehensive descriptive statistics"""
    results = {}

    for var in variables:
        if data[var].dtype in ['int64', 'float64']:
            # Continuous variables
            desc = {
                'n': data[var].count(),
                'missing': data[var].isnull().sum(),
                'mean': data[var].mean(),
                'median': data[var].median(),
                'mode': data[var].mode().iloc[0] if len(data[var].mode()) > 0 else np.nan,
                'std': data[var].std(),
                'var': data[var].var(),
                'min': data[var].min(),
                'max': data[var].max(),
                'range': data[var].max() - data[var].min(),
                'q1': data[var].quantile(0.25),
                'q3': data[var].quantile(0.75),
                'iqr': data[var].quantile(0.75) - data[var].quantile(0.25),
                'skewness': data[var].skew(),
                'kurtosis': data[var].kurtosis(),
                'cv': data[var].std() / data[var].mean() if data[var].mean() != 0 else np.nan,
                'sem': data[var].std() / np.sqrt(data[var].count()),
                'ci_95_lower': data[var].mean() - 1.96 * data[var].std() / np.sqrt(data[var].count()),
                'ci_95_upper': data[var].mean() + 1.96 * data[var].std() / np.sqrt(data[var].count())
            }

            # Outlier detection
            desc['outliers_iqr'] = len(data[(data[var] < desc['q1'] - 1.5 * desc['iqr']) |
                                           (data[var] > desc['q3'] + 1.5 * desc['iqr'])])
            desc['outliers_z'] = len(data[np.abs(stats.zscore(data[var].dropna())) > 3])

        else:
            # Categorical variables
            desc = {
                'n': data[var].count(),
                'missing': data[var].isnull().sum(),
                'unique': data[var].nunique(),
                'mode': data[var].mode().iloc[0] if len(data[var].mode()) > 0 else np.nan,
                'mode_freq': data[var].value_counts().iloc[0] if len(data[var].value_counts()) > 0 else 0,
                'mode_prop': data[var].value_counts(normalize=True).iloc[0] if len(data[var].value_counts()) > 0 else 0
            }

            # Frequency table
            desc['frequency_table'] = data[var].value_counts().to_dict()
            desc['proportion_table'] = data[var].value_counts(normalize=True).to_dict()

        results[var] = desc

    return results

# Group comparison statistics
def group_descriptives(data, group_var, outcome_vars):
    """Generate descriptive statistics by group"""
    results = {}

    for outcome in outcome_vars:
        group_stats = data.groupby(group_var)[outcome].agg([
            'count', 'mean', 'std', 'median', 'min', 'max',
            ('q1', lambda x: x.quantile(0.25)),
            ('q3', lambda x: x.quantile(0.75)),
            ('se', lambda x: x.std() / np.sqrt(len(x))),
            ('ci_lower', lambda x: x.mean() - 1.96 * x.std() / np.sqrt(len(x))),
            ('ci_upper', lambda x: x.mean() + 1.96 * x.std() / np.sqrt(len(x))),
            ('skew', lambda x: x.skew()),
            ('kurtosis', lambda x: x.kurtosis())
        ])

        results[outcome] = group_stats

    return results

# Calculate descriptive statistics
desc_stats = comprehensive_describe(df, [ANALYSIS_VARIABLES])
group_stats = group_descriptives(df, '[GROUP_VARIABLE]', [OUTCOME_VARIABLES])
```

Distribution Assessment:
```python
# Normality testing suite
def test_normality_comprehensive(data, variables, groups=None):
    """Comprehensive normality testing"""
    from scipy.stats import shapiro, normaltest, jarque_bera, anderson, kstest

    results = {}

    for var in variables:
        if groups is None:
            # Test entire variable
            subset = data[var].dropna()

            results[var] = {
                'shapiro_w': shapiro(subset)[0],
                'shapiro_p': shapiro(subset)[1],
                'dagostino_k2': normaltest(subset)[0],
                'dagostino_p': normaltest(subset)[1],
                'jarque_bera_jb': jarque_bera(subset)[0],
                'jarque_bera_p': jarque_bera(subset)[1],
                'anderson_a2': anderson(subset)[0],
                'anderson_critical': anderson(subset)[1],
                'ks_d': kstest(subset, 'norm')[0],
                'ks_p': kstest(subset, 'norm')[1]
            }
        else:
            # Test by groups
            for group in data[groups].unique():
                subset = data[data[groups] == group][var].dropna()

                if len(subset) < 3:
                    continue

                results[f"[VAR]_[GROUP]"] = {
                    'shapiro_w': shapiro(subset)[0],
                    'shapiro_p': shapiro(subset)[1],
                    'dagostino_k2': normaltest(subset)[0],
                    'dagostino_p': normaltest(subset)[1],
                    'jarque_bera_jb': jarque_bera(subset)[0],
                    'jarque_bera_p': jarque_bera(subset)[1]
                }

    return results

# Homogeneity of variance tests
def test_homogeneity(data, outcome_var, group_var):
    """Test homogeneity of variance"""
    from scipy.stats import levene, bartlett, fligner

    groups = [group[outcome_var].values for name, group in data.groupby(group_var)]

    return {
        'levene_stat': levene(*groups)[0],
        'levene_p': levene(*groups)[1],
        'bartlett_stat': bartlett(*groups)[0],
        'bartlett_p': bartlett(*groups)[1],
        'fligner_stat': fligner(*groups)[0],
        'fligner_p': fligner(*groups)[1]
    }

normality_results = test_normality_comprehensive(df, [CONTINUOUS_VARIABLES], '[GROUP_VARIABLE]')
homogeneity_results = test_homogeneity(df, '[OUTCOME_VARIABLE]', '[GROUP_VARIABLE]')
```

STATISTICAL INFERENCE:
Parametric Inference:

1. T-Tests and Confidence Intervals:
```python
from scipy import stats
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel
import numpy as np

# One-sample t-test
def one_sample_ttest(data, pop_mean, confidence=0.95):
    """One-sample t-test with confidence interval"""
    n = len(data)
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    sem = sample_std / np.sqrt(n)

    # T-test
    t_stat, p_value = ttest_1samp(data, pop_mean)

    # Confidence interval
    t_critical = stats.t.ppf((1 + confidence) / 2, df=n-1)
    ci_lower = sample_mean - t_critical * sem
    ci_upper = sample_mean + t_critical * sem

    # Effect size (Cohen's d)
    cohens_d = (sample_mean - pop_mean) / sample_std

    return {
        'sample_mean': sample_mean,
        'population_mean': pop_mean,
        'mean_difference': sample_mean - pop_mean,
        't_statistic': t_stat,
        'df': n - 1,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'confidence_level': confidence
    }

# Independent samples t-test
def independent_ttest(group1, group2, equal_var=None, confidence=0.95):
    """Independent samples t-test with comprehensive output"""
    # Determine equal variance assumption
    if equal_var is None:
        _, levene_p = stats.levene(group1, group2)
        equal_var = levene_p > 0.05

    # Perform t-test
    t_stat, p_value = ttest_ind(group1, group2, equal_var=equal_var)

    # Sample statistics
    n1, n2 = len(group1), len(group2)
    mean1, mean2 = np.mean(group1), np.mean(group2)
    std1, std2 = np.std(group1, ddof=1), np.std(group2, ddof=1)

    # Mean difference and standard error
    mean_diff = mean1 - mean2

    if equal_var:
        # Pooled variance
        pooled_var = ((n1-1)*std1**2 + (n2-1)*std2**2) / (n1+n2-2)
        se_diff = np.sqrt(pooled_var * (1/n1 + 1/n2))
        df = n1 + n2 - 2
        # Cohen's d with pooled standard deviation
        cohens_d = mean_diff / np.sqrt(pooled_var)
    else:
        # Welch's t-test
        se_diff = np.sqrt(std1**2/n1 + std2**2/n2)
        df = (std1**2/n1 + std2**2/n2)**2 / ((std1**2/n1)**2/(n1-1) + (std2**2/n2)**2/(n2-1))
        # Cohen's d with separate standard deviations
        cohens_d = mean_diff / np.sqrt((std1**2 + std2**2) / 2)

    # Confidence interval for mean difference
    t_critical = stats.t.ppf((1 + confidence) / 2, df=df)
    ci_lower = mean_diff - t_critical * se_diff
    ci_upper = mean_diff + t_critical * se_diff

    return {
        'group1_mean': mean1,
        'group1_std': std1,
        'group1_n': n1,
        'group2_mean': mean2,
        'group2_std': std2,
        'group2_n': n2,
        'mean_difference': mean_diff,
        't_statistic': t_stat,
        'df': df,
        'p_value': p_value,
        'equal_var_assumed': equal_var,
        'cohens_d': cohens_d,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'confidence_level': confidence
    }

# Paired samples t-test
def paired_ttest(before, after, confidence=0.95):
    """Paired samples t-test"""
    differences = after - before
    n = len(differences)
    mean_diff = np.mean(differences)
    std_diff = np.std(differences, ddof=1)
    sem_diff = std_diff / np.sqrt(n)

    # T-test
    t_stat, p_value = ttest_rel(before, after)

    # Effect size (Cohen's d for paired samples)
    cohens_d = mean_diff / std_diff

    # Confidence interval
    t_critical = stats.t.ppf((1 + confidence) / 2, df=n-1)
    ci_lower = mean_diff - t_critical * sem_diff
    ci_upper = mean_diff + t_critical * sem_diff

    return {
        'before_mean': np.mean(before),
        'after_mean': np.mean(after),
        'mean_difference': mean_diff,
        't_statistic': t_stat,
        'df': n - 1,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'confidence_level': confidence
    }
```

2. ANOVA and F-Tests:
```python
import pandas as pd
from scipy.stats import f_oneway, f
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd, MultiComparison

# One-way ANOVA
def oneway_anova(data, outcome_var, group_var):
    """Comprehensive one-way ANOVA"""
    # Group data
    groups = [group[outcome_var].values for name, group in data.groupby(group_var)]

    # F-test
    f_stat, p_value = f_oneway(*groups)

    # Degrees of freedom
    k = len(groups)  # number of groups
    n = len(data)    # total sample size
    df_between = k - 1
    df_within = n - k

    # Sum of squares calculation
    grand_mean = data[outcome_var].mean()

    # Between-groups sum of squares
    ss_between = sum([len(group) * (np.mean(group) - grand_mean)**2 for group in groups])

    # Within-groups sum of squares
    ss_within = sum([np.sum((group - np.mean(group))**2) for group in groups])

    # Total sum of squares
    ss_total = ss_between + ss_within

    # Mean squares
    ms_between = ss_between / df_between
    ms_within = ss_within / df_within

    # Effect sizes
    eta_squared = ss_between / ss_total
    omega_squared = (ss_between - df_between * ms_within) / (ss_total + ms_within)

    # Post-hoc tests (Tukey HSD)
    mc = MultiComparison(data[outcome_var], data[group_var])
    tukey_result = mc.tukeyhsd()

    return {
        'f_statistic': f_stat,
        'p_value': p_value,
        'df_between': df_between,
        'df_within': df_within,
        'ss_between': ss_between,
        'ss_within': ss_within,
        'ss_total': ss_total,
        'ms_between': ms_between,
        'ms_within': ms_within,
        'eta_squared': eta_squared,
        'omega_squared': omega_squared,
        'tukey_results': tukey_result
    }

# Two-way ANOVA
def twoway_anova(data, outcome_var, factor1, factor2):
    """Two-way ANOVA with interaction"""
    # Create model formula
    formula = f'[OUTCOME_VAR] ~ C([FACTOR1]) + C([FACTOR2]) + C([FACTOR1]):C([FACTOR2])'

    # Fit model
    model = ols(formula, data=data).fit()
    anova_table = anova_lm(model, typ=2)

    # Effect sizes
    ss_total = anova_table['sum_sq'].sum()
    eta_squared = anova_table['sum_sq'] / ss_total

    # Partial eta squared
    residual_ss = anova_table['sum_sq'].iloc[-1]
    partial_eta_squared = anova_table['sum_sq'][:-1] / (anova_table['sum_sq'][:-1] + residual_ss)

    return {
        'anova_table': anova_table,
        'model': model,
        'eta_squared': eta_squared,
        'partial_eta_squared': partial_eta_squared,
        'r_squared': model.rsquared,
        'adj_r_squared': model.rsquared_adj
    }

# Repeated measures ANOVA
from statsmodels.stats.anova import AnovaRM

def repeated_measures_anova(data, subject_col, within_col, outcome_col):
    """Repeated measures ANOVA"""
    # Perform RM-ANOVA
    rm_anova = AnovaRM(data, outcome_col, subject_col, within=[within_col]).fit()

    # Sphericity testing (if multiple time points)
    # Note: statsmodels doesn't provide Mauchly's test directly

    return {
        'anova_results': rm_anova,
        'summary': rm_anova.summary()
    }
```

3. Regression Analysis:
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
        cat_terms = [f'C([VAR])' for var in categorical_vars if var in predictor_vars]
        cont_terms = [var for var in predictor_vars if var not in categorical_vars]
        predictors = ' + '.join(cont_terms + cat_terms)

    formula = f'[OUTCOME_VAR] ~ [PREDICTORS]'

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

# Logistic Regression
def logistic_regression(data, outcome_var, predictor_vars):
    """Logistic regression analysis"""
    # Prepare formula
    predictors = ' + '.join(predictor_vars)
    formula = f'[OUTCOME_VAR] ~ [PREDICTORS]'

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

    # Hosmer-Lemeshow test
    from scipy.stats import chi2
    # Custom implementation needed for H-L test

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

Non-Parametric Inference:

1. Mann-Whitney U Test:
```python
from scipy.stats import mannwhitneyu, ranksums

def mann_whitney_test(group1, group2, alternative='two-sided'):
    """Mann-Whitney U test with effect size"""
    # Perform test
    u_stat, p_value = mannwhitneyu(group1, group2, alternative=alternative)

    # Sample sizes
    n1, n2 = len(group1), len(group2)

    # Effect size (rank-biserial correlation)
    r = 1 - (2 * u_stat) / (n1 * n2)

    # Common language effect size
    cles = u_stat / (n1 * n2)

    # Hodges-Lehmann estimator
    differences = []
    for x in group1:
        for y in group2:
            differences.append(x - y)
    hl_estimator = np.median(differences)

    # Confidence interval for Hodges-Lehmann estimator
    from scipy.stats import norm
    se_hl = 1.2533 * np.std(differences) / np.sqrt(len(differences))
    z_critical = norm.ppf(0.975)
    hl_ci_lower = hl_estimator - z_critical * se_hl
    hl_ci_upper = hl_estimator + z_critical * se_hl

    return {
        'u_statistic': u_stat,
        'p_value': p_value,
        'n1': n1,
        'n2': n2,
        'rank_biserial_r': r,
        'common_language_es': cles,
        'hodges_lehmann_estimator': hl_estimator,
        'hl_ci_lower': hl_ci_lower,
        'hl_ci_upper': hl_ci_upper,
        'group1_median': np.median(group1),
        'group2_median': np.median(group2)
    }

# Wilcoxon Signed-Rank Test
from scipy.stats import wilcoxon

def wilcoxon_signed_rank_test(before, after):
    """Wilcoxon signed-rank test for paired samples"""
    # Calculate differences
    differences = after - before
    non_zero_diff = differences[differences != 0]

    # Perform test
    w_stat, p_value = wilcoxon(before, after, zero_method='wilcox')

    # Effect size (matched-pairs rank-biserial correlation)
    n = len(non_zero_diff)
    r = 1 - (2 * w_stat) / (n * (n + 1) / 2)

    return {
        'w_statistic': w_stat,
        'p_value': p_value,
        'n_pairs': n,
        'rank_biserial_r': r,
        'median_difference': np.median(differences),
        'before_median': np.median(before),
        'after_median': np.median(after)
    }

# Kruskal-Wallis Test
from scipy.stats import kruskal
from scikit_posthocs import posthoc_dunn

def kruskal_wallis_test(data, outcome_var, group_var):
    """Kruskal-Wallis test with post-hoc analysis"""
    # Prepare groups
    groups = [group[outcome_var].values for name, group in data.groupby(group_var)]

    # Perform test
    h_stat, p_value = kruskal(*groups)

    # Effect size (epsilon-squared)
    n = len(data)
    k = len(groups)
    epsilon_squared = (h_stat - k + 1) / (n - k)

    # Post-hoc tests (Dunn's test)
    dunn_results = posthoc_dunn(data, val_col=outcome_var, group_col=group_var,
                               p_adjust='bonferroni')

    return {
        'h_statistic': h_stat,
        'p_value': p_value,
        'degrees_of_freedom': k - 1,
        'epsilon_squared': epsilon_squared,
        'dunn_results': dunn_results,
        'group_medians': data.groupby(group_var)[outcome_var].median()
    }
```

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
```

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
```

CONFIDENCE INTERVALS:
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
```

EFFECT SIZE CALCULATIONS:
Comprehensive Effect Sizes:
```python
def comprehensive_effect_sizes(group1, group2=None, paired=False):
    """Calculate multiple effect size measures"""

    if group2 is None:
        # One-sample effect sizes
        n = len(group1)
        mean = np.mean(group1)
        std = np.std(group1, ddof=1)

        # One-sample Cohen's d (against population mean of 0)
        cohens_d = mean / std

        return {
            'cohens_d': cohens_d,
            'mean': mean,
            'std': std,
            'n': n
        }

    else:
        # Two-sample effect sizes
        n1, n2 = len(group1), len(group2)
        mean1, mean2 = np.mean(group1), np.mean(group2)
        std1, std2 = np.std(group1, ddof=1), np.std(group2, ddof=1)

        if paired:
            # Paired samples
            differences = group1 - group2
            cohens_d = np.mean(differences) / np.std(differences, ddof=1)

            # Correlation between measurements
            correlation = np.corrcoef(group1, group2)[0, 1]

            return {
                'cohens_d_paired': cohens_d,
                'mean_difference': np.mean(differences),
                'correlation': correlation,
                'n_pairs': n1
            }

        else:
            # Independent samples
            # Cohen's d
            pooled_std = np.sqrt(((n1-1)*std1**2 + (n2-1)*std2**2) / (n1+n2-2))
            cohens_d = (mean1 - mean2) / pooled_std

            # Hedges' g (unbiased Cohen's d)
            hedges_g = cohens_d * (1 - 3/(4*(n1+n2)-9))

            # Glass's delta
            glass_delta = (mean1 - mean2) / std2

            # Probability of superiority
            from scipy.stats import norm
            prob_superiority = norm.cdf(cohens_d / np.sqrt(2))

            # Common language effect size
            u_stat, _ = mannwhitneyu(group1, group2)
            cles = u_stat / (n1 * n2)

            return {
                'cohens_d': cohens_d,
                'hedges_g': hedges_g,
                'glass_delta': glass_delta,
                'prob_superiority': prob_superiority,
                'common_language_es': cles,
                'pooled_std': pooled_std,
                'mean_difference': mean1 - mean2
            }

# ANOVA effect sizes
def anova_effect_sizes(data, outcome_var, group_var):
    """Calculate effect sizes for ANOVA"""
    # Perform ANOVA to get sum of squares
    groups = [group[outcome_var].values for name, group in data.groupby(group_var)]
    f_stat, p_value = f_oneway(*groups)

    # Calculate sum of squares
    grand_mean = data[outcome_var].mean()
    n_total = len(data)
    k = len(groups)

    # Between-groups sum of squares
    ss_between = sum([len(group) * (np.mean(group) - grand_mean)**2 for group in groups])

    # Within-groups sum of squares
    ss_within = sum([np.sum((group - np.mean(group))**2) for group in groups])

    # Total sum of squares
    ss_total = ss_between + ss_within

    # Effect sizes
    eta_squared = ss_between / ss_total
    partial_eta_squared = ss_between / (ss_between + ss_within)
    omega_squared = (ss_between - (k-1) * (ss_within/(n_total-k))) / (ss_total + (ss_within/(n_total-k)))

    # Cohen's f
    cohens_f = np.sqrt(eta_squared / (1 - eta_squared))

    return {
        'eta_squared': eta_squared,
        'partial_eta_squared': partial_eta_squared,
        'omega_squared': omega_squared,
        'cohens_f': cohens_f,
        'f_statistic': f_stat,
        'p_value': p_value
    }
```

REPORTING AND INTERPRETATION:
Results Reporting Framework:
```python
def format_statistical_results(test_results, test_type, alpha=0.05):
    """Format statistical results for reporting"""

    def format_p_value(p):
        if p < 0.001:
            return "p < .001"
        elif p < 0.01:
            return f"p = {p:.3f}"
        else:
            return f"p = {p:.3f}"

    def interpret_effect_size(es, measure='cohens_d'):
        if measure == 'cohens_d':
            if abs(es) < 0.2:
                return "negligible"
            elif abs(es) < 0.5:
                return "small"
            elif abs(es) < 0.8:
                return "medium"
            else:
                return "large"
        elif measure == 'eta_squared':
            if es < 0.01:
                return "small"
            elif es < 0.06:
                return "medium"
            else:
                return "large"

    if test_type == 'ttest_ind':
        results_text = f"""
        An independent samples t-test revealed a {'statistically significant' if test_results['p_value'] < alpha else 'non-significant'}
        difference between groups, t({test_results['df']:.0f}) = {test_results['t_statistic']:.3f},
        {format_p_value(test_results['p_value'])}, Cohen's d = {test_results['cohens_d']:.3f}
        ({interpret_effect_size(test_results['cohens_d'])} effect size),
        95% CI [{test_results['ci_lower']:.3f}, {test_results['ci_upper']:.3f}].
        """

    elif test_type == 'anova_oneway':
        results_text = f"""
        A one-way ANOVA revealed a {'statistically significant' if test_results['p_value'] < alpha else 'non-significant'}
        effect, F({test_results['df_between']}, {test_results['df_within']}) = {test_results['f_statistic']:.3f},
        {format_p_value(test_results['p_value'])}, η² = {test_results['eta_squared']:.3f}
        ({interpret_effect_size(test_results['eta_squared'], 'eta_squared')} effect size).
        """

    return results_text.strip()

# Assumption checking report
def assumption_check_report(data, test_type):
    """Generate assumption checking report"""

    report = []

    if test_type in ['ttest', 'anova']:
        # Check normality
        normality_results = test_normality_comprehensive(data, continuous_variables)
        report.append("ASSUMPTION CHECKS:")
        report.append("1. Normality: ")
        for var, results in normality_results.items():
            if results['shapiro_p'] > 0.05:
                report.append(f"   - [VAR]: Normal (Shapiro-Wilk p = {results['shapiro_p']:.3f})")
            else:
                report.append(f"   - [VAR]: Non-normal (Shapiro-Wilk p = {results['shapiro_p']:.3f})")

    if test_type in ['ttest_ind', 'anova']:
        # Check homogeneity of variance
        homogeneity_results = test_homogeneity(data, outcome_var, group_var)
        report.append("2. Homogeneity of variance:")
        if homogeneity_results['levene_p'] > 0.05:
            report.append(f"   - Equal variances assumed (Levene's p = {homogeneity_results['levene_p']:.3f})")
        else:
            report.append(f"   - Unequal variances (Levene's p = {homogeneity_results['levene_p']:.3f})")

    return "\n".join(report)
```

VISUALIZATION:
Statistical Results Visualization:
```python
import matplotlib.pyplot as plt
import seaborn as sns

def create_statistical_plots(data, results, plot_type):
    """Create comprehensive statistical visualization"""

    fig, axes = plt.subplots(2, 3, figsize=(18, 12))

    if plot_type == 'ttest_comparison':
        # Group comparison plots

        # Box plot
        sns.boxplot(x=group_var, y=outcome_var, data=data, ax=axes[0, 0])
        axes[0, 0].set_title('Group Comparison (Box Plot)')

        # Violin plot with individual points
        sns.violinplot(x=group_var, y=outcome_var, data=data, ax=axes[0, 1])
        sns.swarmplot(x=group_var, y=outcome_var, data=data, ax=axes[0, 1],
                     color='white', alpha=0.7, size=3)
        axes[0, 1].set_title('Distribution Comparison')

        # Histogram overlay
        for i, group in enumerate(data[group_var].unique()):
            subset = data[data[group_var] == group][outcome_var]
            axes[0, 2].hist(subset, alpha=0.7, label=f'Group [GROUP]', bins=20)
        axes[0, 2].legend()
        axes[0, 2].set_title('Distribution Overlay')

        # Q-Q plots
        from scipy.stats import probplot
        groups = data.groupby(group_var)
        for i, (name, group) in enumerate(groups):
            probplot(group[outcome_var], dist="norm", plot=axes[1, i])
            axes[1, i].set_title(f'Q-Q Plot: [NAME]')

        # Effect size visualization
        effect_size = results['cohens_d']
        ci_lower = results['ci_lower']
        ci_upper = results['ci_upper']

        axes[1, 2].errorbar([0], [effect_size],
                           yerr=[[effect_size - ci_lower], [ci_upper - effect_size]],
                           fmt='o', capsize=10, capthick=2, elinewidth=2, markersize=8)
        axes[1, 2].axhline(y=0, color='red', linestyle='--', alpha=0.7)
        axes[1, 2].axhline(y=0.2, color='orange', linestyle=':', alpha=0.5, label='Small effect')
        axes[1, 2].axhline(y=0.5, color='yellow', linestyle=':', alpha=0.5, label='Medium effect')
        axes[1, 2].axhline(y=0.8, color='green', linestyle=':', alpha=0.5, label='Large effect')
        axes[1, 2].set_ylabel("Cohen's d")
        axes[1, 2].set_title('Effect Size with 95% CI')
        axes[1, 2].legend()
        axes[1, 2].set_xlim(-0.5, 0.5)

    elif plot_type == 'power_analysis':
        # Power analysis visualization
        from statsmodels.stats.power import TTestPower

        power_analysis = TTestPower()

        # Effect size vs Power
        effect_sizes = np.linspace(0, 2, 100)
        sample_sizes = [10, 20, 50, 100, 200]

        for n in sample_sizes:
            power_values = power_analysis.solve_power(effect_size=effect_sizes,
                                                     nobs=n, alpha=0.05)
            axes[0, 0].plot(effect_sizes, power_values, label=f'n=[N]')

        axes[0, 0].axhline(y=0.8, color='red', linestyle='--', label='Power=0.8')
        axes[0, 0].set_xlabel('Effect Size (Cohen\'s d)')
        axes[0, 0].set_ylabel('Statistical Power')
        axes[0, 0].set_title('Power vs Effect Size')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)

        # Sample size vs Power
        sample_sizes = np.arange(5, 200, 5)
        effect_sizes_power = [0.2, 0.5, 0.8, 1.0]

        for es in effect_sizes_power:
            power_values = power_analysis.solve_power(effect_size=es,
                                                     nobs=sample_sizes, alpha=0.05)
            axes[0, 1].plot(sample_sizes, power_values, label=f'd=[ES]')

        axes[0, 1].axhline(y=0.8, color='red', linestyle='--', label='Power=0.8')
        axes[0, 1].set_xlabel('Sample Size per Group')
        axes[0, 1].set_ylabel('Statistical Power')
        axes[0, 1].set_title('Power vs Sample Size')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    return fig

# Create publication-ready plots
def publication_plots(results_dict):
    """Create publication-ready statistical plots"""

    # Set publication style
    plt.style.use('seaborn-v0_8-whitegrid')

    # Create comprehensive results figure
    return create_statistical_plots(df, results_dict, 'ttest_comparison')
```

OUTPUT REQUIREMENTS:
Deliver comprehensive statistical analysis including:

1. **Study Design Summary**
   - Research questions and hypotheses
   - Study design and methodology
   - Sample size justification
   - Variable definitions

2. **Descriptive Analysis**
   - Comprehensive descriptive statistics
   - Data quality assessment
   - Distribution analysis
   - Outlier detection

3. **Assumption Testing**
   - Normality tests
   - Homogeneity of variance
   - Independence checks
   - Linearity assessment

4. **Statistical Tests**
   - Primary hypothesis tests
   - Effect size calculations
   - Confidence intervals
   - Power analysis

5. **Multiple Testing Correction**
   - Adjustment methods applied
   - Corrected p-values
   - False discovery rate control

6. **Sensitivity Analysis**
   - Robustness checks
   - Alternative methods
   - Outlier influence
   - Missing data impact

7. **Bayesian Analysis** (if applicable)
   - Posterior distributions
   - Credible intervals
   - Bayes factors

8. **Visualization Package**
   - Descriptive plots
   - Statistical test results
   - Effect size visualizations
   - Diagnostic plots

9. **Results Interpretation**
   - Statistical significance
   - Practical significance
   - Clinical/Business relevance
   - Limitations discussion

10. **Reproducible Code**
    - Complete analysis scripts
    - Data preprocessing code
    - Visualization code
    - Results formatting
```

## Variables

### Research Design Variables
- [RESEARCH_OBJECTIVE] - Primary research objective and goal
- [STUDY_TYPE] - Type of study design (experimental, observational, etc.)
- [DESIGN_TYPE] - Specific design methodology (RCT, cohort, etc.)
- [TARGET_POPULATION] - Population of interest for inference
- [SAMPLING_FRAME] - Accessible population for sampling
- [UNIT_OF_ANALYSIS] - Unit being analyzed (individuals, groups, etc.)
- [TIME_HORIZON] - Temporal scope of the study
- [PRIMARY_RESEARCH_QUESTION] - Main research question
- [STATISTICAL_HYPOTHESES] - Statistical hypotheses formulation
- [NULL_HYPOTHESIS] - Null hypothesis statement
- [ALTERNATIVE_HYPOTHESIS] - Alternative hypothesis statement
- [HYPOTHESIS_DIRECTION] - One-tailed or two-tailed test
- [ALPHA_LEVEL] - Type I error rate (significance level)
- [BETA_LEVEL] - Type II error rate
- [STATISTICAL_POWER] - Statistical power (1 - β)

### Variable Definitions
- [PRIMARY_OUTCOME] - Primary dependent variable
- [SECONDARY_OUTCOMES] - Secondary outcome measures
- [PRIMARY_PREDICTOR] - Main independent variable
- [COVARIATES] - Control variables
- [CONFOUNDERS] - Confounding variables
- [MEDIATORS] - Mediating variables
- [MODERATORS] - Moderating variables
- [STRATIFICATION_VARS] - Variables for stratification
- [CONTINUOUS_VARIABLES] - List of continuous variables
- [CATEGORICAL_VARIABLES] - List of categorical variables
- [GROUP_VARIABLE] - Grouping variable for comparisons
- [OUTCOME_VARIABLE] - Primary outcome variable name

### Sample Size and Power
- [EFFECT_SIZE_COHENS_D] - Expected Cohen's d effect size
- [EFFECT_SIZE_F] - Expected f effect size for ANOVA
- [EFFECT_SIZE_F2] - Expected f² effect size for regression
- [EFFECT_SIZE_H] - Expected h effect size for proportions
- [EFFECT_SIZE_W] - Expected w effect size for chi-square
- [SAMPLE_SIZE_PER_GROUP] - Sample size per group
- [NUMBER_OF_GROUPS] - Number of groups in analysis
- [TOTAL_SAMPLE_SIZE] - Total sample size
- [NUMERATOR_DF] - Numerator degrees of freedom
- [DENOMINATOR_DF] - Denominator degrees of freedom
- [CORRELATION_COEFFICIENT] - Expected correlation
- [MINIMUM_EFFECT] - Minimum detectable effect size
- [EXPECTED_EFFECT_SIZE] - Expected effect size
- [REQUIRED_N] - Required sample size
- [PLANNED_N] - Planned sample size
- [ATTRITION_RATE] - Expected attrition rate
- [FINAL_N] - Final sample size accounting for attrition
- [ACHIEVED_POWER] - Achieved statistical power
- [CONFIDENCE_INTERVAL_WIDTH] - Precision requirement

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

### Descriptive Statistics
- [SAMPLE_SIZE] - Sample size
- [MEAN] - Sample mean
- [MEDIAN] - Sample median
- [MODE] - Sample mode
- [STANDARD_DEVIATION] - Sample standard deviation
- [VARIANCE] - Sample variance
- [MINIMUM] - Minimum value
- [MAXIMUM] - Maximum value
- [RANGE] - Data range
- [Q1] - First quartile
- [Q3] - Third quartile
- [IQR] - Interquartile range
- [SKEWNESS] - Skewness measure
- [KURTOSIS] - Kurtosis measure
- [CV] - Coefficient of variation
- [SEM] - Standard error of the mean
- [CI_95_LOWER] - 95% CI lower bound
- [CI_95_UPPER] - 95% CI upper bound

### Test Results
- [TEST_STATISTIC] - Test statistic value
- [P_VALUE] - P-value
- [T_STATISTIC] - T-test statistic
- [F_STATISTIC] - F-test statistic
- [CHI_SQUARE_STATISTIC] - Chi-square statistic
- [U_STATISTIC] - Mann-Whitney U statistic
- [W_STATISTIC] - Wilcoxon W statistic
- [H_STATISTIC] - Kruskal-Wallis H statistic
- [Z_STATISTIC] - Z-test statistic
- [CRITICAL_VALUE] - Critical value
- [DEGREES_OF_FREEDOM_NUM] - Numerator DF
- [DEGREES_OF_FREEDOM_DEN] - Denominator DF

### Effect Sizes
- [COHENS_D] - Cohen's d effect size
- [HEDGES_G] - Hedges' g effect size
- [GLASS_DELTA] - Glass's delta effect size
- [ETA_SQUARED] - Eta-squared effect size
- [PARTIAL_ETA_SQUARED] - Partial eta-squared
- [OMEGA_SQUARED] - Omega-squared effect size
- [COHENS_F] - Cohen's f effect size
- [R_SQUARED] - R-squared (coefficient of determination)
- [ADJUSTED_R_SQUARED] - Adjusted R-squared
- [PARTIAL_R_SQUARED] - Partial R-squared
- [SEMIPARTIAL_R_SQUARED] - Semipartial R-squared
- [RANK_BISERIAL_R] - Rank-biserial correlation
- [COMMON_LANGUAGE_ES] - Common language effect size
- [PROBABILITY_SUPERIORITY] - Probability of superiority
- [HODGES_LEHMANN] - Hodges-Lehmann estimator

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

### Assumption Testing
- [NORMALITY_TEST] - Normality test used
- [NORMALITY_STATISTIC] - Normality test statistic
- [NORMALITY_P_VALUE] - Normality test p-value
- [SHAPIRO_W] - Shapiro-Wilk W statistic
- [SHAPIRO_P] - Shapiro-Wilk p-value
- [KOLMOGOROV_D] - Kolmogorov-Smirnov D statistic
- [KOLMOGOROV_P] - Kolmogorov-Smirnov p-value
- [ANDERSON_A2] - Anderson-Darling A² statistic
- [JARQUE_BERA_JB] - Jarque-Bera JB statistic
- [JARQUE_BERA_P] - Jarque-Bera p-value
- [LEVENE_STATISTIC] - Levene's test statistic
- [LEVENE_P_VALUE] - Levene's test p-value
- [BARTLETT_STATISTIC] - Bartlett's test statistic
- [BARTLETT_P_VALUE] - Bartlett's test p-value
- [FLIGNER_STATISTIC] - Fligner-Killeen statistic
- [FLIGNER_P_VALUE] - Fligner-Killeen p-value
- [DURBIN_WATSON] - Durbin-Watson statistic
- [BREUSCH_PAGAN_P] - Breusch-Pagan test p-value
- [WHITE_TEST_P] - White's test p-value

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

### Outlier Detection
- [OUTLIERS_IQR] - Number of IQR-based outliers
- [OUTLIERS_Z_SCORE] - Number of z-score outliers
- [OUTLIERS_MODIFIED_Z] - Modified z-score outliers
- [OUTLIER_THRESHOLD] - Outlier detection threshold
- [OUTLIER_METHOD] - Outlier detection method
- [EXTREME_VALUES] - Extreme values identified
- [INFLUENTIAL_POINTS] - Influential data points
- [LEVERAGE_CUTOFF] - Leverage cutoff value
- [COOK_CUTOFF] - Cook's distance cutoff

### Missing Data
- [MISSING_PATTERN] - Missing data pattern
- [MISSING_MECHANISM] - Missing data mechanism
- [LISTWISE_N] - Listwise deletion sample size
- [PAIRWISE_N] - Pairwise deletion sample size
- [IMPUTATION_METHOD] - Imputation method used
- [MULTIPLE_IMPUTATIONS] - Number of imputations
- [IMPUTATION_CONVERGENCE] - Imputation convergence
- [MICE_ITERATIONS] - MICE algorithm iterations

### Sensitivity Analysis
- [SENSITIVITY_METHODS] - Sensitivity analysis methods
- [ROBUST_RESULTS] - Robust analysis results
- [ALTERNATIVE_TESTS] - Alternative test results
- [BOOTSTRAP_RESULTS] - Bootstrap analysis results
- [JACKKNIFE_RESULTS] - Jackknife analysis results
- [LEAVE_ONE_OUT] - Leave-one-out analysis
- [INFLUENCE_MEASURES] - Influence measures
- [STABILITY_CHECK] - Stability check results

### Model Diagnostics
- [RESIDUAL_PLOTS] - Residual plot assessments
- [QQ_PLOT_ASSESSMENT] - Q-Q plot assessment
- [HOMOSCEDASTICITY] - Homoscedasticity assessment
- [LINEARITY_CHECK] - Linearity assumption check
- [INDEPENDENCE_CHECK] - Independence assumption check
- [MULTICOLLINEARITY] - Multicollinearity assessment
- [MODEL_ADEQUACY] - Overall model adequacy
- [GOODNESS_OF_FIT] - Goodness of fit measures
- [DEVIANCE_RESIDUALS] - Deviance residuals
- [PEARSON_RESIDUALS] - Pearson residuals

### Reporting Variables
- [RESULTS_SUMMARY] - Summary of main results
- [STATISTICAL_CONCLUSION] - Statistical conclusion
- [PRACTICAL_SIGNIFICANCE] - Practical significance assessment
- [CLINICAL_SIGNIFICANCE] - Clinical significance assessment
- [LIMITATIONS] - Study limitations
- [ASSUMPTIONS_MET] - Assumptions met/violated
- [ALTERNATIVE_APPROACHES] - Alternative analysis approaches
- [FUTURE_RESEARCH] - Future research recommendations
- [PUBLICATION_STATEMENT] - Publication-ready results statement

### Visualization Variables
- [PLOT_TITLE] - Plot title
- [X_AXIS_LABEL] - X-axis label
- [Y_AXIS_LABEL] - Y-axis label
- [LEGEND_LABELS] - Legend labels
- [COLOR_SCHEME] - Color scheme for plots
- [PLOT_THEME] - Plot theme/style
- [FIGURE_SIZE] - Figure dimensions
- [DPI_SETTING] - Figure resolution
- [ANNOTATION_TEXT] - Plot annotations

### Quality Control
- [DATA_QUALITY_CHECKS] - Data quality assessments
- [RANGE_CHECKS] - Variable range checks
- [CONSISTENCY_CHECKS] - Data consistency checks
- [VALIDATION_RESULTS] - Cross-validation results
- [REPLICATION_CHECK] - Result replication check
- [CODE_REVIEW_STATUS] - Code review status
- [PEER_REVIEW_STATUS] - Peer review status
- [DOCUMENTATION_COMPLETE] - Documentation completeness

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
### Example 1: Clinical Trial Analysis
```
RESEARCH_OBJECTIVE: "Evaluate efficacy of new treatment vs placebo"
STUDY_TYPE: "Randomized Controlled Trial"
NULL_HYPOTHESIS: "No difference in treatment outcomes between groups"
TEST_TYPE: "Independent samples t-test"
EFFECT_SIZE_COHENS_D: "0.5"
ALPHA_LEVEL: "0.05"
STATISTICAL_POWER: "0.80"
```

### Example 2: Survey Research Analysis
```
RESEARCH_OBJECTIVE: "Identify factors predicting job satisfaction"
STUDY_TYPE: "Cross-sectional survey"
DESIGN_TYPE: "Multiple regression analysis"
PRIMARY_OUTCOME: "job_satisfaction_score"
PREDICTOR_VARIABLES: "salary, work_life_balance, supervisor_support"
R_SQUARED: "0.35"
```

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

### Example 5: Meta-Analysis
```
RESEARCH_OBJECTIVE: "Synthesize evidence on intervention effectiveness"
STUDY_TYPE: "Systematic review and meta-analysis"
EFFECT_SIZE_MEASURE: "Standardized mean difference"
HETEROGENEITY_TEST: "Q-test and I² statistic"
RANDOM_EFFECTS_MODEL: "DerSimonian-Laird method"
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