---
title: Survey Response Analysis Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, research, strategy, template]
use_cases:
  - Analyze survey response data with comprehensive data cleaning, derived variable creation, missing data handling, and descriptive statistical analysis to prepare for advanced statistical testing.
  - Project planning and execution
  - Strategy development
related_templates:
  - survey-analysis-overview.md
  - survey-data-collection.md
  - survey-statistical-validation.md
last_updated: 2025-11-09
---

# Survey Response Analysis Template

## Purpose
Analyze survey response data with comprehensive data cleaning, derived variable creation, missing data handling, and descriptive statistical analysis to prepare for advanced statistical testing.

## Template

```
You are a survey data analysis expert. Analyze survey response data for [RESEARCH_PURPOSE] with [TOTAL_RESPONSES] responses, focusing on data quality, cleaning, and descriptive analysis.

RESPONSE ANALYSIS FRAMEWORK:

Data Preparation:
```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Survey data cleaning and preparation
class SurveyDataProcessor:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.cleaned_data = None
        self.cleaning_log = []

    def comprehensive_cleaning(self):
        """Comprehensive survey data cleaning pipeline"""

        data = self.raw_data.copy()

        # 1. Remove test responses
        if 'test_flag' in data.columns:
            test_responses = data['test_flag'].sum()
            data = data[data['test_flag'] != 1]
            self.cleaning_log.append(f"Removed {test_responses} test responses")

        # 2. Remove incomplete responses
        completion_threshold = 0.75  # 75% completion required
        completion_rate = data.count(axis=1) / len(data.columns)
        incomplete = (completion_rate < completion_threshold).sum()
        data = data[completion_rate >= completion_threshold]
        self.cleaning_log.append(f"Removed {incomplete} incomplete responses")

        # 3. Response time filtering
        if 'response_time' in data.columns:
            # Remove too fast responses (< 5th percentile)
            fast_cutoff = data['response_time'].quantile(0.05)
            too_fast = (data['response_time'] < fast_cutoff).sum()
            data = data[data['response_time'] >= fast_cutoff]

            # Remove too slow responses (> 95th percentile)
            slow_cutoff = data['response_time'].quantile(0.95)
            too_slow = (data['response_time'] > slow_cutoff).sum()
            data = data[data['response_time'] <= slow_cutoff]

            self.cleaning_log.append(f"Removed {too_fast} too fast and {too_slow} too slow responses")

        # 4. Straight-lining detection
        scale_columns = [col for col in data.columns if col.startswith('scale_')]
        if scale_columns:
            # Calculate variance across scale items for each respondent
            scale_variance = data[scale_columns].var(axis=1)
            straight_line_threshold = 0.1
            straight_liners = (scale_variance < straight_line_threshold).sum()
            data = data[scale_variance >= straight_line_threshold]
            self.cleaning_log.append(f"Removed {straight_liners} straight-line responses")

        # 5. Outlier detection for continuous variables
        continuous_vars = data.select_dtypes(include=[np.number]).columns
        outlier_count = 0
        for var in continuous_vars:
            if var in ['response_time', 'id']:
                continue

            Q1 = data[var].quantile(0.25)
            Q3 = data[var].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 3 * IQR
            upper_bound = Q3 + 3 * IQR

            outliers = ((data[var] < lower_bound) | (data[var] > upper_bound)).sum()
            outlier_count += outliers

        self.cleaning_log.append(f"Identified {outlier_count} outlier values across variables")

        # 6. Duplicate response detection
        if 'email' in data.columns:
            duplicates = data.duplicated(subset=['email']).sum()
            data = data.drop_duplicates(subset=['email'])
            self.cleaning_log.append(f"Removed {duplicates} duplicate responses")

        self.cleaned_data = data
        return data, self.cleaning_log

    def create_derived_variables(self):
        """Create derived variables and indices"""

        data = self.cleaned_data.copy()

        # 1. Create scale scores (average of scale items)
        scale_groups = {}
        for col in data.columns:
            if '_' in col:
                prefix = col.split('_')[0]
                if prefix not in scale_groups:
                    scale_groups[prefix] = []
                scale_groups[prefix].append(col)

        # Calculate scale means
        for scale_name, items in scale_groups.items():
            if len(items) > 1:  # Only create scales with multiple items
                data[f'{scale_name}_mean'] = data[items].mean(axis=1)
                data[f'{scale_name}_count'] = data[items].count(axis=1)

        # 2. Create demographic categories
        if 'age' in data.columns:
            data['age_group'] = pd.cut(data['age'],
                                     bins=[0, 25, 35, 45, 55, 65, 100],
                                     labels=['18-25', '26-35', '36-45', '46-55', '56-65', '66+'])

        if 'income' in data.columns:
            income_percentiles = data['income'].quantile([0.33, 0.67]).values
            data['income_tertile'] = pd.cut(data['income'],
                                          bins=[-np.inf, income_percentiles[0], income_percentiles[1], np.inf],
                                          labels=['Low', 'Medium', 'High'])

        # 3. Create response behavior indicators
        data['total_responses'] = data.count(axis=1)
        data['response_completeness'] = data.count(axis=1) / len(data.columns)

        return data

# Missing data analysis
def missing_data_analysis(data):
    """Comprehensive missing data analysis"""

    missing_summary = {
        'overall_missing_rate': data.isnull().sum().sum() / (data.shape[0] * data.shape[1]),
        'variables_missing_rate': data.isnull().sum() / len(data),
        'cases_missing_rate': data.isnull().sum(axis=1) / data.shape[1],
        'missing_patterns': data.isnull().sum(axis=1).value_counts().sort_index()
    }

    # Missing data visualization
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Missing by variable
    missing_by_var = data.isnull().sum().sort_values(ascending=False)
    missing_by_var.plot(kind='bar', ax=axes[0, 0])
    axes[0, 0].set_title('Missing Data by Variable')
    axes[0, 0].set_ylabel('Count Missing')

    # Missing pattern heatmap
    missing_matrix = data.isnull().astype(int)
    sns.heatmap(missing_matrix.iloc[:100], ax=axes[0, 1], cbar=True)
    axes[0, 1].set_title('Missing Data Pattern (First 100 Cases)')

    # Missing by case
    missing_by_case = data.isnull().sum(axis=1)
    missing_by_case.hist(bins=20, ax=axes[1, 0])
    axes[1, 0].set_title('Distribution of Missing Values per Case')
    axes[1, 0].set_xlabel('Number Missing')

    # Response rate over time (if timestamp available)
    if 'timestamp' in data.columns:
        data['date'] = pd.to_datetime(data['timestamp']).dt.date
        daily_responses = data.groupby('date').size()
        daily_responses.plot(ax=axes[1, 1])
        axes[1, 1].set_title('Response Rate Over Time')

    plt.tight_layout()

    return missing_summary

# Survey weighting
def calculate_survey_weights(sample_data, population_benchmarks):
    """Calculate survey weights to adjust for non-response bias"""

    # Post-stratification weighting
    weights = pd.Series(1.0, index=sample_data.index)

    for var, benchmarks in population_benchmarks.items():
        if var in sample_data.columns:
            sample_dist = sample_data[var].value_counts(normalize=True)

            for category, pop_prop in benchmarks.items():
                if category in sample_dist.index:
                    sample_prop = sample_dist[category]
                    weight_factor = pop_prop / sample_prop
                    mask = sample_data[var] == category
                    weights[mask] *= weight_factor

    # Trim extreme weights
    weight_percentiles = weights.quantile([0.01, 0.99])
    weights = weights.clip(lower=weight_percentiles[0.01], upper=weight_percentiles[0.99])

    # Normalize weights to sum to sample size
    weights = weights / weights.mean()

    return weights
```

DESCRIPTIVE ANALYSIS:
```python
# Survey data analysis framework
class SurveyAnalysis:
    def __init__(self, data, weights=None, design_info=None):
        self.data = data
        self.weights = weights
        self.design_info = design_info or {}

    def descriptive_analysis(self, variables):
        """Comprehensive descriptive analysis for survey data"""

        results = {}

        for var in variables:
            if var in self.data.columns:
                # Basic statistics
                if self.data[var].dtype in ['int64', 'float64']:
                    # Continuous variable
                    stats_dict = {
                        'count': self.data[var].count(),
                        'mean': self.data[var].mean(),
                        'weighted_mean': np.average(self.data[var].dropna(),
                                                  weights=self.weights[self.data[var].notna()] if self.weights is not None else None),
                        'median': self.data[var].median(),
                        'std': self.data[var].std(),
                        'min': self.data[var].min(),
                        'max': self.data[var].max(),
                        'q25': self.data[var].quantile(0.25),
                        'q75': self.data[var].quantile(0.75),
                        'skewness': self.data[var].skew(),
                        'kurtosis': self.data[var].kurtosis()
                    }

                    # Confidence interval for mean
                    sem = stats.sem(self.data[var].dropna())
                    ci = stats.t.interval(0.95, len(self.data[var].dropna())-1,
                                        loc=stats_dict['mean'], scale=sem)
                    stats_dict['ci_95_lower'] = ci[0]
                    stats_dict['ci_95_upper'] = ci[1]

                else:
                    # Categorical variable
                    value_counts = self.data[var].value_counts()
                    proportions = self.data[var].value_counts(normalize=True)

                    # Weighted proportions if weights available
                    if self.weights is not None:
                        weighted_counts = self.data.groupby(var).apply(
                            lambda x: self.weights[x.index].sum()
                        )
                        weighted_proportions = weighted_counts / self.weights.sum()
                    else:
                        weighted_proportions = proportions

                    stats_dict = {
                        'value_counts': value_counts.to_dict(),
                        'proportions': proportions.to_dict(),
                        'weighted_proportions': weighted_proportions.to_dict(),
                        'mode': self.data[var].mode().iloc[0],
                        'unique_values': self.data[var].nunique(),
                        'most_common': value_counts.index[0],
                        'most_common_freq': value_counts.iloc[0],
                        'most_common_prop': proportions.iloc[0]
                    }

                    # Confidence intervals for proportions
                    for category, prop in proportions.items():
                        n = len(self.data[var].dropna())
                        se = np.sqrt(prop * (1 - prop) / n)
                        ci = stats.norm.interval(0.95, loc=prop, scale=se)
                        stats_dict[f'{category}_ci_lower'] = ci[0]
                        stats_dict[f'{category}_ci_upper'] = ci[1]

                results[var] = stats_dict

        return results

    def cross_tabulation_analysis(self, row_var, col_var, test_independence=True):
        """Cross-tabulation analysis with statistical tests"""

        # Create contingency table
        crosstab = pd.crosstab(self.data[row_var], self.data[col_var],
                              margins=True, normalize=False)

        # Proportions
        prop_total = pd.crosstab(self.data[row_var], self.data[col_var],
                               normalize='all')
        prop_row = pd.crosstab(self.data[row_var], self.data[col_var],
                             normalize='index')
        prop_col = pd.crosstab(self.data[row_var], self.data[col_var],
                             normalize='columns')

        results = {
            'frequencies': crosstab,
            'proportions_total': prop_total,
            'proportions_row': prop_row,
            'proportions_column': prop_col
        }

        # Statistical tests
        if test_independence:
            # Chi-square test
            chi2, p_chi2, dof, expected = stats.chi2_contingency(
                crosstab.iloc[:-1, :-1]  # Remove margin totals
            )

            # Cramér's V effect size
            n = crosstab.iloc[-1, -1]  # Total sample size
            cramers_v = np.sqrt(chi2 / (n * (min(crosstab.shape) - 2)))

            # Fisher's exact test (for 2x2 tables)
            if crosstab.shape == (3, 3):  # Including margins
                if crosstab.iloc[:-1, :-1].shape == (2, 2):
                    _, p_fisher = stats.fisher_exact(crosstab.iloc[:-1, :-1])
                    results['fisher_exact_p'] = p_fisher

            results.update({
                'chi2_statistic': chi2,
                'chi2_p_value': p_chi2,
                'degrees_of_freedom': dof,
                'expected_frequencies': expected,
                'cramers_v': cramers_v
            })

        return results

# Advanced survey analysis methods
def complex_sample_analysis(data, design_info, weights=None):
    """Analysis accounting for complex survey design"""

    design_effects = {}

    if design_info.get('clustering'):
        # Calculate design effect due to clustering
        # DEFF = 1 + (n_cluster - 1) * ICC
        cluster_var = design_info['clustering']['cluster_var']
        avg_cluster_size = data.groupby(cluster_var).size().mean()

        # Estimate ICC (would need multilevel analysis)
        estimated_icc = 0.05  # Placeholder
        design_effect_clustering = 1 + (avg_cluster_size - 1) * estimated_icc
        design_effects['clustering'] = design_effect_clustering

    if design_info.get('stratification'):
        # Stratification typically reduces design effect
        strata_var = design_info['stratification']['strata_var']
        strata_sizes = data.groupby(strata_var).size()
        design_effect_stratification = 1.0 - (strata_sizes.var() / strata_sizes.mean()**2)
        design_effects['stratification'] = max(design_effect_stratification, 0.5)

    if weights is not None:
        # Calculate design effect due to weighting
        weight_variance = weights.var()
        weight_mean_squared = (weights.mean())**2
        design_effect_weighting = 1 + (weight_variance / weight_mean_squared)
        design_effects['weighting'] = design_effect_weighting

    # Overall design effect
    overall_design_effect = 1
    for effect in design_effects.values():
        overall_design_effect *= effect

    # Effective sample size
    effective_n = len(data) / overall_design_effect

    return {
        'design_effects': design_effects,
        'overall_design_effect': overall_design_effect,
        'effective_sample_size': effective_n,
        'actual_sample_size': len(data)
    }
```

OUTPUT REQUIREMENTS:
Deliver comprehensive response analysis including:

1. **Data Cleaning Report**
   - Cleaning procedures applied
   - Number of cases removed at each stage
   - Outlier detection results
   - Duplicate removal summary
   - Final sample characteristics

2. **Missing Data Analysis**
   - Overall missing data rate
   - Missing data by variable
   - Missing data patterns
   - Missing data mechanism assessment
   - Imputation strategy (if applicable)

3. **Descriptive Statistics**
   - Univariate statistics for all variables
   - Frequency distributions
   - Measures of central tendency and dispersion
   - Confidence intervals
   - Weighted and unweighted estimates

4. **Cross-Tabulation Analysis**
   - Key variable cross-tabulations
   - Chi-square test results
   - Effect size measures
   - Proportion comparisons
   - Subgroup analysis

5. **Sample Quality Assessment**
   - Response rate analysis
   - Demographic representativeness
   - Weighting diagnostics
   - Design effect calculations
   - Effective sample size
```

## Variables

### Response Analysis Variables
- [RESEARCH_PURPOSE] - Primary purpose of the survey research
- [TOTAL_RESPONSES] - Total number of responses received
- [COMPLETE_RESPONSES] - Number of complete responses
- [PARTIAL_RESPONSES] - Number of partial responses
- [RESPONSE_RATE] - Overall response rate percentage
- [COMPLETION_RATE] - Survey completion rate percentage
- [DROPOUT_RATE] - Survey dropout rate percentage
- [MEDIAN_RESPONSE_TIME] - Median time to complete survey
- [RESPONSE_QUALITY] - Assessment of response quality
- [STRAIGHT_LINING] - Incidence of straight-line responses
- [ITEM_NONRESPONSE] - Item-level nonresponse rates
- [DATA_CLEANING_STEPS] - Data cleaning procedures performed
- [OUTLIER_DETECTION] - Outlier detection and handling methods
- [MISSING_DATA_PATTERN] - Pattern of missing data
- [IMPUTATION_METHOD] - Missing data imputation methods used

### Weighting Variables
- [WEIGHTING_METHOD] - Method used for calculating weights
- [POPULATION_BENCHMARKS] - Population benchmarks for weighting
- [POST_STRATIFICATION] - Post-stratification variables and procedures
- [WEIGHT_TRIMMING] - Weight trimming procedures applied
- [EFFECTIVE_SAMPLE_SIZE] - Effective sample size after weighting
- [DESIGN_EFFECTS_WEIGHTS] - Design effects due to weighting

### Analysis Variables
- [ANALYSIS_PLAN] - Statistical analysis plan overview
- [SIGNIFICANCE_LEVEL] - Statistical significance level used
- [CONFIDENCE_INTERVALS] - Confidence interval levels reported
- [COMPLEX_SAMPLE_METHODS] - Methods accounting for complex sample design
- [VARIANCE_ESTIMATION] - Variance estimation procedures

## Usage Examples

### Example 1: Customer Satisfaction Survey Analysis
```
TOTAL_RESPONSES: "3,245 responses"
COMPLETE_RESPONSES: "2,987 (92% completion rate)"
DATA_CLEANING_STEPS: "Removed 145 incomplete, 23 duplicate, 90 straight-liners"
WEIGHTING_METHOD: "Post-stratification by age, gender, region"
EFFECTIVE_SAMPLE_SIZE: "2,654 (design effect = 1.12)"
```

### Example 2: Public Opinion Poll
```
TOTAL_RESPONSES: "1,523 adults"
RESPONSE_RATE: "18% (AAPOR RR3)"
WEIGHTING_METHOD: "Raking to Census demographics"
DESIGN_EFFECTS_WEIGHTS: "1.35 due to weighting"
EFFECTIVE_SAMPLE_SIZE: "1,128 weighted responses"
```

## Best Practices

1. **Document all cleaning decisions** - Maintain transparency in data preparation
2. **Examine missing data patterns** - Understand why data is missing
3. **Use appropriate weights** - Adjust for sampling and non-response
4. **Calculate design effects** - Account for complex sampling
5. **Report both weighted and unweighted** - Show impact of weighting
6. **Check data distributions** - Identify skewness and outliers
7. **Validate derived variables** - Ensure correct computation
8. **Compare respondents to non-respondents** - Assess non-response bias
9. **Use robust methods** - Guard against violations of assumptions
10. **Provide complete documentation** - Enable replication

## Tips for Success

- Start with exploratory data analysis before formal testing
- Use visualizations to understand distributions and relationships
- Check for multicollinearity among predictor variables
- Consider both statistical and practical significance
- Report effect sizes along with p-values
- Be transparent about data quality issues
- Use multiple methods to assess representativeness
- Account for clustering in standard error calculations
- Trim extreme weights carefully to balance bias and variance
- Document all assumptions and their justifications
