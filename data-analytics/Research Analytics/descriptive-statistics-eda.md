---
title: Descriptive Statistics & Exploratory Data Analysis
category: data-analytics/Research Analytics
tags: ['statistics', 'eda', 'descriptive', 'data-analysis']
use_cases:
  - Perform comprehensive descriptive statistics and exploratory data analysis including summary statistics, distributions, visualizations, and data profiling.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Descriptive Statistics & Exploratory Data Analysis

## Purpose
Perform comprehensive descriptive statistics and exploratory data analysis including summary statistics, distributions, visualizations, and data profiling.

## Quick Start

### For Researchers & Statisticians

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific needs for perform
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
- Perform comprehensive descriptive statistics and exploratory data analysis including summary statistics, distributions, visualizations, and data profiling.
- Project-specific implementations
- Practical applications and deployments



## Template

# Correlation power analysis
power_corr <- pwr.r.test(
    n = [SAMPLE_SIZE],
    r = [CORRELATION_COEFFICIENT],
    sig.level = [ALPHA_LEVEL],
    power = [DESIRED_POWER],
    alternative = "[ALTERNATIVE]"
)


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

Distribution Assessment:
```python

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


1. **Study Design Summary**

2. **Descriptive Analysis**

   - Comprehensive descriptive statistics

   - Distribution analysis

   - Posterior distributions

8. **Visualization Package**

   - Descriptive plots

   - Effect size visualizations

    - Visualization code

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
