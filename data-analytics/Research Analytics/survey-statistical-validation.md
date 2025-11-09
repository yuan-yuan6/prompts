---
title: Survey Statistical Validation Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, research, strategy, template, testing]
use_cases:
  - Validate survey instruments and data through reliability analysis, validity testing, factor analysis, and psychometric evaluation to ensure measurement quality and construct validity.
  - Project planning and execution
  - Strategy development
related_templates:
  - survey-analysis-overview.md
  - survey-design-questionnaire.md
  - survey-response-analysis.md
last_updated: 2025-11-09
---

# Survey Statistical Validation Template

## Purpose
Validate survey instruments and data through reliability analysis, validity testing, factor analysis, and psychometric evaluation to ensure measurement quality and construct validity.

## Template

```
You are a survey psychometrics expert. Validate survey instruments for [RESEARCH_PURPOSE] with focus on reliability, validity, and psychometric properties of [SCALE_CONSTRUCTION] measuring [CONSTRUCTS].

STATISTICAL VALIDATION FRAMEWORK:

Scale Reliability Analysis:
```python
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt
import seaborn as sns

class SurveyAnalysis:
    def __init__(self, data, weights=None):
        self.data = data
        self.weights = weights

    def scale_reliability_analysis(self, scale_items):
        """Reliability analysis for multi-item scales"""

        # Cronbach's Alpha
        scale_data = self.data[scale_items].dropna()

        def cronbachs_alpha(items):
            items_df = items.dropna()
            N = items_df.shape[1]
            variance_sum = items_df.var(axis=0, ddof=1).sum()
            total_variance = items_df.sum(axis=1).var(ddof=1)
            alpha = (N / (N - 1)) * (1 - variance_sum / total_variance)
            return alpha

        alpha = cronbachs_alpha(scale_data)

        # Item-total correlations
        scale_sum = scale_data.sum(axis=1)
        item_total_corr = {}
        for item in scale_items:
            item_total_corr[item] = scale_data[item].corr(scale_sum)

        # Alpha if item deleted
        alpha_if_deleted = {}
        for item in scale_items:
            remaining_items = [i for i in scale_items if i != item]
            alpha_if_deleted[item] = cronbachs_alpha(scale_data[remaining_items])

        # Inter-item correlations
        inter_item_corr = scale_data.corr()
        mean_inter_item_corr = inter_item_corr.values[np.triu_indices_from(inter_item_corr.values, k=1)].mean()

        return {
            'cronbachs_alpha': alpha,
            'item_total_correlations': item_total_corr,
            'alpha_if_item_deleted': alpha_if_deleted,
            'inter_item_correlation_matrix': inter_item_corr,
            'mean_inter_item_correlation': mean_inter_item_corr,
            'n_items': len(scale_items),
            'n_valid_cases': len(scale_data)
        }

    def factor_analysis(self, variables, n_factors=None, rotation='varimax'):
        """Exploratory Factor Analysis"""

        # Prepare data
        fa_data = self.data[variables].dropna()

        # Determine number of factors if not specified
        if n_factors is None:
            # Eigenvalue > 1 rule (Kaiser criterion)
            correlation_matrix = fa_data.corr()
            eigenvalues = np.linalg.eigvals(correlation_matrix)
            n_factors = np.sum(eigenvalues > 1)

        # Fit factor analysis model
        fa = FactorAnalysis(n_components=n_factors, random_state=42)
        fa.fit(fa_data)

        # Factor loadings
        loadings = fa.components_.T
        loadings_df = pd.DataFrame(loadings,
                                 index=variables,
                                 columns=[f'Factor_{i+1}' for i in range(n_factors)])

        # Communalities
        communalities = np.sum(loadings**2, axis=1)

        # Variance explained
        eigenvalues_fa = np.sum(loadings**2, axis=0)
        variance_explained = eigenvalues_fa / len(variables)
        cumulative_variance = np.cumsum(variance_explained)

        return {
            'n_factors': n_factors,
            'factor_loadings': loadings_df,
            'communalities': dict(zip(variables, communalities)),
            'eigenvalues': eigenvalues_fa,
            'variance_explained': variance_explained,
            'cumulative_variance_explained': cumulative_variance,
            'rotation': rotation
        }

# Split-half reliability
def split_half_reliability(data, scale_items):
    """Calculate split-half reliability"""

    scale_data = data[scale_items].dropna()

    # Split items into two halves
    n_items = len(scale_items)
    half1_items = scale_items[:n_items//2]
    half2_items = scale_items[n_items//2:]

    # Calculate half scores
    half1_score = scale_data[half1_items].sum(axis=1)
    half2_score = scale_data[half2_items].sum(axis=1)

    # Correlation between halves
    correlation = half1_score.corr(half2_score)

    # Spearman-Brown correction
    spearman_brown = (2 * correlation) / (1 + correlation)

    return {
        'split_half_correlation': correlation,
        'spearman_brown_coefficient': spearman_brown,
        'half1_items': len(half1_items),
        'half2_items': len(half2_items)
    }

# Test-retest reliability (if longitudinal data available)
def test_retest_reliability(time1_data, time2_data, variables):
    """Calculate test-retest reliability"""

    reliability_results = {}

    for var in variables:
        if var in time1_data.columns and var in time2_data.columns:
            # Merge on respondent ID
            merged = pd.merge(time1_data[[var]], time2_data[[var]],
                            left_index=True, right_index=True,
                            suffixes=('_t1', '_t2'))

            # Correlation
            correlation = merged[f'{var}_t1'].corr(merged[f'{var}_t2'])

            # Intraclass correlation coefficient (ICC)
            # Using ICC(2,1) - two-way random effects, absolute agreement
            mean_t1 = merged[f'{var}_t1'].mean()
            mean_t2 = merged[f'{var}_t2'].mean()
            grand_mean = (mean_t1 + mean_t2) / 2

            ss_between = len(merged) * ((mean_t1 - grand_mean)**2 + (mean_t2 - grand_mean)**2)
            ss_within = ((merged[f'{var}_t1'] - mean_t1)**2 + (merged[f'{var}_t2'] - mean_t2)**2).sum()

            ms_between = ss_between / 1  # 1 degree of freedom (2 time points - 1)
            ms_within = ss_within / (len(merged) * 2)

            icc = (ms_between - ms_within) / (ms_between + ms_within)

            reliability_results[var] = {
                'pearson_correlation': correlation,
                'icc': icc,
                'n_pairs': len(merged)
            }

    return reliability_results
```

VALIDITY ASSESSMENT:
```python
# Construct validity assessment
def assess_construct_validity(data, scale_items, criterion_var=None, convergent_vars=None, divergent_vars=None):
    """Comprehensive construct validity assessment"""

    validity_results = {}

    # Calculate scale score
    scale_score = data[scale_items].mean(axis=1)

    # 1. Convergent validity
    if convergent_vars:
        convergent_correlations = {}
        for var in convergent_vars:
            if var in data.columns:
                corr, p_value = stats.pearsonr(scale_score.dropna(),
                                              data[var].dropna())
                convergent_correlations[var] = {
                    'correlation': corr,
                    'p_value': p_value
                }
        validity_results['convergent_validity'] = convergent_correlations

    # 2. Divergent (discriminant) validity
    if divergent_vars:
        divergent_correlations = {}
        for var in divergent_vars:
            if var in data.columns:
                corr, p_value = stats.pearsonr(scale_score.dropna(),
                                              data[var].dropna())
                divergent_correlations[var] = {
                    'correlation': corr,
                    'p_value': p_value
                }
        validity_results['divergent_validity'] = divergent_correlations

    # 3. Criterion validity (if criterion available)
    if criterion_var and criterion_var in data.columns:
        corr, p_value = stats.pearsonr(scale_score.dropna(),
                                       data[criterion_var].dropna())
        validity_results['criterion_validity'] = {
            'correlation': corr,
            'p_value': p_value,
            'criterion_variable': criterion_var
        }

    return validity_results

# Known-groups validity
def known_groups_validity(data, scale_items, group_var):
    """Test if scale discriminates between known groups"""

    scale_score = data[scale_items].mean(axis=1)
    groups = data[group_var].unique()

    # ANOVA if more than 2 groups
    if len(groups) > 2:
        group_scores = [scale_score[data[group_var] == group].dropna() for group in groups]
        f_stat, p_value = stats.f_oneway(*group_scores)

        # Effect size (eta-squared)
        group_means = [scores.mean() for scores in group_scores]
        grand_mean = scale_score.mean()
        ss_between = sum([len(scores) * (mean - grand_mean)**2
                         for scores, mean in zip(group_scores, group_means)])
        ss_total = ((scale_score - grand_mean)**2).sum()
        eta_squared = ss_between / ss_total

        results = {
            'test': 'ANOVA',
            'f_statistic': f_stat,
            'p_value': p_value,
            'eta_squared': eta_squared,
            'group_means': dict(zip(groups, group_means))
        }

    # T-test if 2 groups
    else:
        group1_scores = scale_score[data[group_var] == groups[0]].dropna()
        group2_scores = scale_score[data[group_var] == groups[1]].dropna()

        t_stat, p_value = stats.ttest_ind(group1_scores, group2_scores)

        # Cohen's d effect size
        pooled_std = np.sqrt((group1_scores.var() + group2_scores.var()) / 2)
        cohens_d = (group1_scores.mean() - group2_scores.mean()) / pooled_std

        results = {
            'test': 't-test',
            't_statistic': t_stat,
            'p_value': p_value,
            'cohens_d': cohens_d,
            'group_means': {
                groups[0]: group1_scores.mean(),
                groups[1]: group2_scores.mean()
            }
        }

    return results

# Confirmatory Factor Analysis (CFA) framework
def confirmatory_factor_analysis(data, factor_structure):
    """
    Confirmatory Factor Analysis to test hypothesized factor structure

    factor_structure: dict mapping factor names to lists of items
    Example: {'Factor1': ['item1', 'item2'], 'Factor2': ['item3', 'item4']}
    """

    # This is a conceptual framework - would typically use specialized packages
    # like lavaan in R or semopy in Python

    cfa_framework = {
        'model_specification': factor_structure,
        'fit_indices': {
            'chi_square': 'Model chi-square test',
            'cfi': 'Comparative Fit Index (CFI) - should be > 0.95',
            'tli': 'Tucker-Lewis Index (TLI) - should be > 0.95',
            'rmsea': 'Root Mean Square Error of Approximation - should be < 0.06',
            'srmr': 'Standardized Root Mean Square Residual - should be < 0.08'
        },
        'parameter_estimates': {
            'factor_loadings': 'Standardized loadings should be > 0.50',
            'factor_correlations': 'Correlations between factors',
            'error_variances': 'Item error variances'
        },
        'modification_indices': 'Suggest model improvements if fit is poor'
    }

    return cfa_framework
```

MEASUREMENT INVARIANCE:
```python
# Measurement invariance testing
def test_measurement_invariance(data, scale_items, group_var):
    """Test measurement invariance across groups"""

    # This is a conceptual framework for multi-group CFA
    # Would typically use specialized SEM software

    invariance_levels = {
        'configural_invariance': {
            'description': 'Same factor structure across groups',
            'constraint': 'None - baseline model',
            'test': 'Test if model fits in each group separately'
        },

        'metric_invariance': {
            'description': 'Equal factor loadings across groups',
            'constraint': 'Factor loadings constrained equal',
            'test': 'Chi-square difference test vs. configural'
        },

        'scalar_invariance': {
            'description': 'Equal item intercepts across groups',
            'constraint': 'Loadings and intercepts constrained equal',
            'test': 'Chi-square difference test vs. metric'
        },

        'strict_invariance': {
            'description': 'Equal error variances across groups',
            'constraint': 'Loadings, intercepts, and errors constrained',
            'test': 'Chi-square difference test vs. scalar'
        }
    }

    return invariance_levels

# Item Response Theory (IRT) analysis
def irt_analysis(data, scale_items, model='2PL'):
    """
    Item Response Theory analysis for scale items

    model: '1PL' (Rasch), '2PL' (2-parameter logistic), or '3PL' (3-parameter)
    """

    irt_framework = {
        'model_type': model,

        '1PL_rasch': {
            'parameters': 'Item difficulty (b)',
            'assumptions': 'Equal discrimination across items',
            'use_case': 'Educational testing, ability measures'
        },

        '2PL': {
            'parameters': 'Item difficulty (b) and discrimination (a)',
            'assumptions': 'No guessing',
            'use_case': 'Most attitude and personality scales'
        },

        '3PL': {
            'parameters': 'Difficulty (b), discrimination (a), and guessing (c)',
            'assumptions': 'Accounts for guessing',
            'use_case': 'Multiple choice tests with guessing'
        },

        'outputs': {
            'item_parameters': 'Difficulty and discrimination estimates',
            'person_abilities': 'Estimated ability/trait levels',
            'item_information': 'Measurement precision at different trait levels',
            'test_information': 'Overall test precision curve',
            'item_fit': 'How well items fit the model'
        }
    }

    return irt_framework
```

OUTPUT REQUIREMENTS:
Deliver comprehensive statistical validation including:

1. **Reliability Analysis**
   - Cronbach's alpha for all scales
   - Item-total correlations
   - Alpha if item deleted
   - Split-half reliability
   - Test-retest reliability (if available)
   - Inter-item correlation matrix

2. **Factor Analysis**
   - Exploratory factor analysis results
   - Factor loadings and structure
   - Eigenvalues and scree plot
   - Variance explained by factors
   - Factor correlation matrix
   - Communalities

3. **Validity Evidence**
   - Convergent validity correlations
   - Divergent validity correlations
   - Criterion validity assessment
   - Known-groups validity tests
   - Face and content validity discussion

4. **Psychometric Properties**
   - Scale distributions
   - Item difficulty indices
   - Item discrimination indices
   - Response option analysis
   - Floor and ceiling effects

5. **Measurement Quality**
   - Standard error of measurement
   - Confidence intervals for scores
   - Measurement invariance results
   - Differential item functioning
   - Recommendations for scale improvement
```

## Variables

### Scale Development Variables
- [RESEARCH_PURPOSE] - Primary purpose of the survey research
- [SCALE_CONSTRUCTION] - Scale construction methodology
- [CONSTRUCTS] - Constructs being measured
- [ITEM_DEVELOPMENT] - Item development procedures
- [SCALE_VALIDATION] - Scale validation procedures
- [RELIABILITY_MEASURES] - Reliability measures calculated
- [VALIDITY_EVIDENCE] - Types of validity evidence collected
- [FACTOR_ANALYSIS] - Factor analysis procedures and results
- [ITEM_ANALYSIS] - Item analysis procedures and results
- [SCALE_SCORING] - Scale scoring procedures
- [PSYCHOMETRIC_PROPERTIES] - Summary of psychometric properties
- [SCALE_INTERPRETATION] - Guidelines for scale interpretation
- [CUT_POINTS] - Meaningful cut points or categories
- [RELIABILITY_COEFFICIENTS] - Specific reliability coefficients
- [CONSTRUCT_VALIDITY] - Construct validity evidence

### Analysis Variables
- [SIGNIFICANCE_LEVEL] - Statistical significance level used
- [CONFIDENCE_INTERVALS] - Confidence interval levels reported
- [EFFECT_SIZE_MEASURES] - Effect size measures calculated
- [MULTIPLE_TESTING] - Multiple testing correction procedures

## Usage Examples

### Example 1: Job Satisfaction Scale Validation
```
SCALE_CONSTRUCTION: "15-item job satisfaction scale"
RELIABILITY_COEFFICIENTS: "Cronbach's alpha = 0.89"
FACTOR_ANALYSIS: "Three factors: work environment, compensation, growth"
CONSTRUCT_VALIDITY: "Convergent with engagement (r=0.65), divergent with turnover intent (r=-0.45)"
```

### Example 2: Customer Experience Scale
```
SCALE_CONSTRUCTION: "Multi-dimensional customer experience scale"
RELIABILITY_MEASURES: "Alpha range 0.82-0.91 across dimensions"
VALIDITY_EVIDENCE: "Criterion validity with NPS (r=0.73), known-groups validity confirmed"
FACTOR_ANALYSIS: "Five factors explaining 68% of variance"
```

### Example 3: Health Behavior Scale
```
CONSTRUCTS: "Health beliefs, self-efficacy, behavioral intentions"
RELIABILITY_COEFFICIENTS: "Test-retest r=0.84 over 2 weeks"
MEASUREMENT_INVARIANCE: "Scalar invariance established across age groups"
IRT_ANALYSIS: "2PL model, good item discrimination (a > 1.0)"
```

## Best Practices

1. **Report multiple reliability estimates** - Don't rely on alpha alone
2. **Assess both internal and external validity** - Multiple types of validity evidence
3. **Use factor analysis appropriately** - EFA for exploration, CFA for confirmation
4. **Examine item properties** - Item-total correlations and distributions
5. **Test measurement invariance** - Before comparing groups
6. **Report complete psychometric information** - Enable meta-analysis
7. **Consider IRT for scale refinement** - More information than CTT alone
8. **Document scale development** - Enable replication and extension
9. **Assess practical significance** - Not just statistical significance
10. **Validate in multiple samples** - Cross-validation is essential

## Tips for Success

- Start with clear construct definitions before item writing
- Use both EFA and CFA in separate samples when possible
- Aim for Cronbach's alpha between 0.70 and 0.95
- Examine item-total correlations > 0.30 as minimum
- Look for factor loadings > 0.40 as meaningful
- Test validity with multiple types of evidence
- Consider both convergent and divergent validity
- Document all psychometric properties thoroughly
- Report confidence intervals for reliability estimates
- Use appropriate sample sizes for factor analysis (N > 200)
