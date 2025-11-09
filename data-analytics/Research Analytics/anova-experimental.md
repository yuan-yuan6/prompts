---
title: ANOVA and Experimental Design Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, experimental-design, research, statistics, template]
use_cases:
  - Conducting analysis of variance (ANOVA) to compare means across multiple groups and analyze experimental designs with factorial arrangements and repeated measures.
  - Experimental research
  - Group comparisons
related_templates:
  - statistical-analysis-overview.md
  - hypothesis-testing.md
  - regression-analysis.md
last_updated: 2025-11-09
---

# ANOVA and Experimental Design Template

## Purpose
Conduct analysis of variance (ANOVA) to compare means across multiple groups and analyze complex experimental designs including factorial, repeated measures, and mixed designs.

## Template

```
You are an ANOVA and experimental design expert. Analyze the effect of [FACTOR_VARIABLES] on [OUTCOME_VARIABLE] using [ANOVA_TYPE] with [EXPERIMENTAL_DESIGN] design and [POST_HOC_TESTS] comparisons.

ANOVA FRAMEWORK:
Experimental Context:
- Outcome variable: [OUTCOME_VARIABLE]
- Factor variables: [FACTOR_VARIABLES]
- ANOVA type: [ANOVA_TYPE] (One-way/Two-way/Repeated Measures/Mixed)
- Experimental design: [EXPERIMENTAL_DESIGN]
- Number of groups: [NUMBER_OF_GROUPS]
- Sample size per group: [SAMPLE_SIZE_PER_GROUP]
- Within-subjects factors: [WITHIN_SUBJECTS_FACTORS]
- Between-subjects factors: [BETWEEN_SUBJECTS_FACTORS]

### ONE-WAY ANOVA

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
```

### TWO-WAY ANOVA

```python
# Two-way ANOVA
def twoway_anova(data, outcome_var, factor1, factor2):
    """Two-way ANOVA with interaction"""
    # Create model formula
    formula = f'{outcome_var} ~ C({factor1}) + C({factor2}) + C({factor1}):C({factor2})'
    
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
```

### REPEATED MEASURES ANOVA

```python
# Repeated measures ANOVA
from statsmodels.stats.anova import AnovaRM

def repeated_measures_anova(data, subject_col, within_col, outcome_col):
    """Repeated measures ANOVA"""
    # Perform RM-ANOVA
    rm_anova = AnovaRM(data, outcome_col, subject_col, within=[within_col]).fit()
    
    return {
        'anova_results': rm_anova,
        'summary': rm_anova.summary()
    }
```

OUTPUT REQUIREMENTS:
1. **ANOVA Table** - F-statistics, p-values, effect sizes
2. **Post-hoc Tests** - Pairwise comparisons with corrections
3. **Effect Sizes** - Eta-squared, omega-squared, partial eta-squared
4. **Assumption Checks** - Normality, homogeneity of variance
5. **Interaction Plots** - For factorial designs
```

## Variables

- [FACTOR_VARIABLES] - Independent variables (factors)
- [OUTCOME_VARIABLE] - Dependent variable
- [ANOVA_TYPE] - Type of ANOVA design
- [EXPERIMENTAL_DESIGN] - Experimental design structure
- [POST_HOC_TESTS] - Post-hoc comparison method
- [NUMBER_OF_GROUPS] - Number of groups/levels
- [SAMPLE_SIZE_PER_GROUP] - Sample size per group
- [WITHIN_SUBJECTS_FACTORS] - Repeated measures factors
- [BETWEEN_SUBJECTS_FACTORS] - Between-subjects factors

## Usage Examples

### Example 1: Drug Comparison
```
OUTCOME_VARIABLE: "symptom_score"
FACTOR_VARIABLES: "drug_type (3 levels)"
ANOVA_TYPE: "One-way ANOVA"
POST_HOC_TESTS: "Tukey HSD"
NUMBER_OF_GROUPS: "3"
```

### Example 2: Factorial Design
```
OUTCOME_VARIABLE: "test_performance"
FACTOR_VARIABLES: "teaching_method, class_size"
ANOVA_TYPE: "Two-way ANOVA"
EXPERIMENTAL_DESIGN: "2x3 factorial"
```

## Best Practices

1. **Check assumptions** - Normality and homogeneity of variance
2. **Use appropriate post-hoc tests** - Control family-wise error rate
3. **Report effect sizes** - Not just statistical significance
4. **Test interactions** - In factorial designs
5. **Consider power** - Ensure adequate sample size
6. **Examine residuals** - Check for model violations
