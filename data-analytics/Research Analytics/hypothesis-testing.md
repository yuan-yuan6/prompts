---
title: Hypothesis Testing Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, research, statistics, template]
use_cases:
  - Conducting rigorous hypothesis testing to evaluate research questions, test statistical significance, and draw valid conclusions from data using parametric and non-parametric methods.
  - A/B testing and experiments
  - Research hypothesis evaluation
related_templates:
  - statistical-analysis-overview.md
  - descriptive-statistics.md
  - anova-experimental.md
last_updated: 2025-11-09
---

# Hypothesis Testing Template

## Purpose
Conduct rigorous hypothesis testing to evaluate research questions, test statistical significance, and draw valid conclusions from data using appropriate parametric and non-parametric methods.

## Template

```
You are a hypothesis testing expert. Test the hypothesis that [HYPOTHESIS_STATEMENT] using [TEST_TYPE] on [DATA_SOURCE] with significance level [ALPHA_LEVEL] and power [STATISTICAL_POWER].

HYPOTHESIS TESTING FRAMEWORK:
Research Context:
- Research question: [RESEARCH_QUESTION]
- Null hypothesis (H₀): [NULL_HYPOTHESIS]
- Alternative hypothesis (H₁): [ALTERNATIVE_HYPOTHESIS]
- Hypothesis direction: [HYPOTHESIS_DIRECTION] (One-tailed/Two-tailed)
- Significance level (α): [ALPHA_LEVEL]
- Statistical power (1-β): [STATISTICAL_POWER]
- Effect size: [EXPECTED_EFFECT_SIZE]
- Sample size: [SAMPLE_SIZE]

### PARAMETRIC HYPOTHESIS TESTS

### T-Tests and Confidence Intervals
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

### NON-PARAMETRIC HYPOTHESIS TESTS

### Mann-Whitney U Test
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
```

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

# Proportion test power analysis
power_prop <- pwr.2p.test(
    h = [EFFECT_SIZE_H],
    n = [SAMPLE_SIZE_PER_GROUP],
    sig.level = [ALPHA_LEVEL],
    power = [DESIRED_POWER],
    alternative = "[ALTERNATIVE]"
)

# Print results
print(paste("Required sample size:", ceiling(power_analysis$n)))
print(paste("Achieved power:", power_analysis$power))
```

### RESULTS REPORTING

### Format Statistical Results
```python
def format_hypothesis_test_results(test_results, test_type, alpha=0.05):
    """Format hypothesis test results for reporting"""

    def format_p_value(p):
        if p < 0.001:
            return "p < .001"
        elif p < 0.01:
            return f"p = {p:.3f}"
        else:
            return f"p = {p:.3f}"

    if test_type == 'ttest_ind':
        results_text = f"""
        An independent samples t-test revealed a {'statistically significant' if test_results['p_value'] < alpha else 'non-significant'}
        difference between groups, t({test_results['df']:.0f}) = {test_results['t_statistic']:.3f},
        {format_p_value(test_results['p_value'])}, Cohen's d = {test_results['cohens_d']:.3f},
        95% CI [{test_results['ci_lower']:.3f}, {test_results['ci_upper']:.3f}].
        """
        return results_text.strip()

    elif test_type == 'mann_whitney':
        results_text = f"""
        A Mann-Whitney U test revealed a {'statistically significant' if test_results['p_value'] < alpha else 'non-significant'}
        difference between groups, U = {test_results['u_statistic']:.0f},
        {format_p_value(test_results['p_value'])}, rank-biserial r = {test_results['rank_biserial_r']:.3f}.
        """
        return results_text.strip()
```

OUTPUT REQUIREMENTS:
Deliver comprehensive hypothesis testing results including:

1. **Test Results**
   - Test statistic values
   - P-values with appropriate precision
   - Degrees of freedom
   - Direction of effect

2. **Effect Sizes**
   - Cohen's d for t-tests
   - Rank-biserial correlation for non-parametric tests
   - Confidence intervals for effect sizes

3. **Statistical Decision**
   - Reject or fail to reject null hypothesis
   - Practical significance assessment
   - Confidence intervals for estimates

4. **Assumption Checks**
   - Normality assessment results
   - Homogeneity of variance results
   - Independence verification

5. **Power Analysis**
   - Achieved power
   - Sample size justification
   - Sensitivity analysis
```

## Variables

- `[HYPOTHESIS_STATEMENT]` - Statement of hypothesis to test
- `[TEST_TYPE]` - Type of hypothesis test to conduct
- `[DATA_SOURCE]` - Source of data for analysis
- `[ALPHA_LEVEL]` - Significance level (e.g., 0.05)
- `[STATISTICAL_POWER]` - Desired statistical power (e.g., 0.80)
- `[RESEARCH_QUESTION]` - Primary research question
- `[NULL_HYPOTHESIS]` - Null hypothesis statement
- `[ALTERNATIVE_HYPOTHESIS]` - Alternative hypothesis statement
- `[HYPOTHESIS_DIRECTION]` - One-tailed or two-tailed
- `[EXPECTED_EFFECT_SIZE]` - Expected effect size
- `[SAMPLE_SIZE]` - Total or per-group sample size

## Usage Examples

### Example 1: A/B Test
```
HYPOTHESIS_STATEMENT: "Version B has higher conversion rate than Version A"
NULL_HYPOTHESIS: "No difference in conversion rates between versions"
ALTERNATIVE_HYPOTHESIS: "Version B conversion rate > Version A"
TEST_TYPE: "Two-proportion z-test"
ALPHA_LEVEL: "0.05"
HYPOTHESIS_DIRECTION: "One-tailed"
```

### Example 2: Clinical Trial
```
HYPOTHESIS_STATEMENT: "New treatment reduces blood pressure more than placebo"
NULL_HYPOTHESIS: "No difference in blood pressure reduction"
ALTERNATIVE_HYPOTHESIS: "Treatment group has greater reduction"
TEST_TYPE: "Independent samples t-test"
ALPHA_LEVEL: "0.05"
STATISTICAL_POWER: "0.80"
```

## Best Practices

1. **State hypotheses clearly** - Before collecting data
2. **Choose appropriate test** - Based on data type and assumptions
3. **Check assumptions** - Verify test requirements are met
4. **Report effect sizes** - Not just statistical significance
5. **Use two-tailed tests** - Unless strong directional prediction
6. **Correct for multiple testing** - When conducting multiple tests
7. **Report confidence intervals** - Along with p-values
8. **Consider practical significance** - Not just statistical significance
