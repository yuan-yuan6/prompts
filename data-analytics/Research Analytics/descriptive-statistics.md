---
title: Descriptive Statistics Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, research, statistics, template]
use_cases:
  - Conducting comprehensive descriptive statistical analysis to summarize and explore data distributions, central tendencies, variability, and patterns using advanced statistical methods.
  - Data exploration and profiling
  - Exploratory data analysis
related_templates:
  - statistical-analysis-overview.md
  - hypothesis-testing.md
  - regression-analysis.md
last_updated: 2025-11-09
---

# Descriptive Statistics Template

## Purpose
Conduct comprehensive descriptive statistical analysis to summarize and explore data distributions, central tendencies, variability, and patterns using advanced statistical methods and visualization techniques.

## Template

```
You are a descriptive statistics expert. Conduct comprehensive descriptive analysis on [DATA_SOURCE] to summarize [DATA_CHARACTERISTICS] and explore [ANALYSIS_FOCUS] using [STATISTICAL_METHODS].

DATA EXPLORATION FRAMEWORK:
Analysis Context:
- Dataset: [DATA_SOURCE]
- Sample size: [SAMPLE_SIZE]
- Variables of interest: [VARIABLES]
- Analysis objective: [ANALYSIS_OBJECTIVE]
- Variable types: [VARIABLE_TYPES]
- Grouping variables: [GROUPING_VARIABLES]
- Time period: [TIME_PERIOD]
- Data completeness: [DATA_COMPLETENESS]

### COMPREHENSIVE DATA EXPLORATION

### Descriptive Statistics
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

### Distribution Assessment
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

                results[f"{var}_{group}"] = {
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

### VISUALIZATION

### Descriptive Visualizations
```python
import matplotlib.pyplot as plt
import seaborn as sns

def create_descriptive_plots(data, variables, plot_type='comprehensive'):
    """Create comprehensive descriptive visualizations"""

    fig, axes = plt.subplots(2, 3, figsize=(18, 12))

    for idx, var in enumerate(variables[:6]):
        row = idx // 3
        col = idx % 3
        ax = axes[row, col]

        if data[var].dtype in ['int64', 'float64']:
            # Histogram with density curve
            ax.hist(data[var].dropna(), bins=30, density=True, alpha=0.7, edgecolor='black')

            # Add normal distribution overlay
            mu, sigma = data[var].mean(), data[var].std()
            x = np.linspace(data[var].min(), data[var].max(), 100)
            ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2, label='Normal fit')

            ax.set_title(f'Distribution: {var}')
            ax.set_xlabel(var)
            ax.set_ylabel('Density')
            ax.legend()
        else:
            # Bar plot for categorical
            data[var].value_counts().plot(kind='bar', ax=ax)
            ax.set_title(f'Frequency: {var}')
            ax.set_xlabel(var)
            ax.set_ylabel('Count')

    plt.tight_layout()
    return fig

# Create visualizations
fig = create_descriptive_plots(df, [VARIABLES])
plt.savefig('[OUTPUT_PATH]/descriptive_plots.png', dpi=300, bbox_inches='tight')
```

OUTPUT REQUIREMENTS:
Deliver comprehensive descriptive analysis including:

1. **Summary Statistics**
   - Measures of central tendency (mean, median, mode)
   - Measures of dispersion (std, variance, range, IQR)
   - Measures of shape (skewness, kurtosis)
   - Confidence intervals for key statistics

2. **Distribution Analysis**
   - Normality assessment
   - Outlier detection and identification
   - Distribution shape and characteristics
   - Q-Q plots and diagnostic plots

3. **Group Comparisons**
   - Descriptive statistics by group
   - Group-level distributions
   - Variance homogeneity assessment

4. **Visual Summaries**
   - Histograms with density curves
   - Box plots and violin plots
   - Bar charts for categorical data
   - Q-Q plots for normality assessment

5. **Data Quality Report**
   - Missing data summary
   - Outlier summary
   - Data range validation
   - Completeness assessment
```

## Variables

### Analysis Variables
- `[DATA_SOURCE]` - Data source identifier
- `[DATA_CHARACTERISTICS]` - Key data characteristics to summarize
- `[ANALYSIS_FOCUS]` - Primary focus areas for analysis
- `[STATISTICAL_METHODS]` - Methods to use for description
- `[SAMPLE_SIZE]` - Total sample size
- `[VARIABLES]` - Variables to analyze
- `[ANALYSIS_OBJECTIVE]` - Objective of descriptive analysis
- `[VARIABLE_TYPES]` - Types of variables (continuous/categorical)
- `[GROUPING_VARIABLES]` - Variables for group comparisons
- `[TIME_PERIOD]` - Time period covered by data
- `[DATA_COMPLETENESS]` - Data completeness percentage

### Statistical Variables
- `[ANALYSIS_VARIABLES]` - List of variables for analysis
- `[OUTCOME_VARIABLES]` - Outcome variables to summarize
- `[GROUP_VARIABLE]` - Grouping variable name
- `[CONTINUOUS_VARIABLES]` - List of continuous variables
- `[OUTPUT_PATH]` - Path for saving outputs

## Usage Examples

### Example 1: Survey Data Summary
```
DATA_SOURCE: "Customer satisfaction survey responses"
SAMPLE_SIZE: "1,500 respondents"
VARIABLES: "satisfaction_score, age, income, region"
ANALYSIS_OBJECTIVE: "Summarize customer satisfaction patterns"
VARIABLE_TYPES: "2 continuous, 2 categorical"
GROUPING_VARIABLES: "region"
```

### Example 2: Clinical Trial Baseline
```
DATA_SOURCE: "Clinical trial baseline measurements"
SAMPLE_SIZE: "300 participants"
VARIABLES: "blood_pressure, cholesterol, BMI, age, gender"
ANALYSIS_OBJECTIVE: "Characterize baseline patient demographics"
GROUPING_VARIABLES: "treatment_group, gender"
```

## Best Practices

1. **Report all relevant statistics** - Include central tendency, dispersion, and shape
2. **Check assumptions** - Assess normality and homogeneity before further analysis
3. **Visualize distributions** - Always complement numbers with visualizations
4. **Identify outliers** - Document and investigate extreme values
5. **Compare groups carefully** - Use appropriate statistics for group comparisons
6. **Document missing data** - Report patterns and extent of missing data
7. **Use robust measures when appropriate** - Consider median and IQR for skewed data
8. **Provide context** - Interpret statistics in the context of the research question

## Tips for Success

- Start with univariate descriptions before examining relationships
- Use both graphical and numerical summaries
- Pay attention to data quality issues during exploration
- Document unusual patterns or unexpected findings
- Consider transformations for highly skewed distributions
- Report confidence intervals along with point estimates
- Use appropriate precision for reported statistics
- Create publication-ready tables and figures
