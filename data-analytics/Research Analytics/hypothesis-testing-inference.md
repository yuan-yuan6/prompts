---
title: Hypothesis Testing & Statistical Inference
category: data-analytics/Research Analytics
tags: ['statistics', 'hypothesis-testing', 'inference', 'significance']
use_cases:
  - Conduct hypothesis testing and statistical inference including t-tests, ANOVA, chi-square, confidence intervals, p-values, and power analysis.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Hypothesis Testing & Statistical Inference

## Purpose
Conduct hypothesis testing and statistical inference including t-tests, ANOVA, chi-square, confidence intervals, p-values, and power analysis.

## Quick Start

### For Researchers & Statisticians

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific needs for conduct
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
- Conduct hypothesis testing and statistical inference including t-tests, ANOVA, chi-square, confidence intervals, p-values, and power analysis.
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


# Statistical Analysis and Inference Template


## Purpose
Conduct comprehensive statistical analysis and inference to test hypotheses, estimate parameters, make predictions, and draw valid conclusions from data using advanced statistical methods and frameworks.


## Quick Start

**Example: Analyzing A/B Test Results for E-commerce Conversion Rates**


You are a statistical analysis expert. Analyze A/B test results for a website redesign campaign comparing conversion rates between the control group (original design) and treatment group (new design) using hypothesis testing and effect size analysis.

- Test duration: 14 days

- Statistical significance level: α = 0.05

1. Perform two-proportion z-test to determine if the difference is statistically significant

2. Calculate effect size (Cohen's h) and confidence intervals (95%)

5. Test assumptions (independence, normality if applicable)

- Hypothesis test results with p-values and test statistics

- 95% confidence intervals for conversion rate difference

- Recommendation: Implement new design or continue testing
```


You are a statistical inference expert. Conduct comprehensive statistical analysis on [DATA_SOURCE] to investigate [RESEARCH_QUESTION] using [STATISTICAL_METHODS] with focus on [INFERENCE_TYPE].

- Null hypothesis (H₀): [NULL_HYPOTHESIS]

- Alternative hypothesis (H₁): [ALTERNATIVE_HYPOTHESIS]

- Direction: [HYPOTHESIS_DIRECTION] (One-tailed/Two-tailed)

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

CONFIDENCE INTERVALS:

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

[Content truncated for length - see original for full details]


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
