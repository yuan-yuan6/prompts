---
category: data-analytics
title: Exploratory Data Analysis Framework
tags:
- data-science
- eda
- data-profiling
- visualization
use_cases:
- Understanding new datasets before modeling
- Identifying data quality issues and anomalies
- Discovering patterns and relationships in data
- Generating hypotheses for further analysis
related_templates:
- data-analytics/Data-Science/experimentation-design.md
- data-analytics/dashboard-design-patterns.md
- data-analytics/predictive-modeling-framework.md
industries:
- technology
- healthcare
- finance
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: exploratory-analysis
---

# Exploratory Data Analysis Framework

## Purpose
Conduct systematic exploratory data analysis to understand data characteristics, assess quality, identify patterns, detect anomalies, and prepare insights for modeling or decision-making. This framework covers data profiling, statistical analysis, visualization, and insight generation.

## �� Quick Start Prompt

> Perform **EDA** on **[DATASET]** with **[ROWS x COLUMNS]** to support **[ANALYSIS GOAL]**. Analyze: (1) **Data profiling**—what are the types, distributions, missing values, and cardinality? (2) **Statistical summary**—what are the central tendencies, variability, and outliers? (3) **Relationships**—what correlations and associations exist between variables? (4) **Patterns**—what segments, trends, or anomalies emerge? Deliver: data quality report, key visualizations, statistical findings, and actionable recommendations.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid exploratory analysis.

---

## Template

Perform exploratory data analysis on {DATASET_DESCRIPTION} containing {DATA_DIMENSIONS} to support {ANALYSIS_OBJECTIVE}.

**1. DATA PROFILING**

Understand what you're working with:

Dataset overview: How many rows and columns? What's the memory footprint? What time period does the data cover? What's the granularity—one row per transaction, customer, day? Understanding the unit of analysis is fundamental.

Variable inventory: Categorize columns by type—numeric (continuous vs discrete), categorical (nominal vs ordinal), datetime, text, boolean. Identify the target variable if supervised learning is the goal. Note which variables are features vs identifiers vs metadata.

Data types assessment: Check if inferred types match semantic meaning. Numeric IDs should often be categorical. Dates stored as strings need conversion. Mixed-type columns indicate data quality issues. Document any type conversions needed.

Cardinality analysis: For categorical variables, count unique values. High-cardinality categoricals (>50 values) need special handling—encoding, grouping, or embedding. Low-cardinality numerics might be better treated as categorical. Identify primary key candidates.

**2. MISSING DATA ANALYSIS**

Assess completeness systematically:

Missing value counts: Calculate missing percentage for each variable. Visualize with a missing data heatmap. Variables with >50% missing may need to be dropped. Variables with <5% missing are usually manageable.

Missing patterns: Is missingness random (MCAR), dependent on observed data (MAR), or dependent on unobserved data (MNAR)? Use Little's MCAR test if needed. Patterns inform imputation strategy—mean/median for MCAR, model-based for MAR, domain expertise for MNAR.

Cross-variable patterns: Do certain variables have correlated missingness? Missing together suggests a common cause—perhaps a data collection process issue. Visualize missing patterns across rows to identify systematic gaps.

Business interpretation: Why is data missing? Survey non-response? System logging gaps? Optional fields? Understanding the mechanism helps choose appropriate handling and prevents biased conclusions.

**3. UNIVARIATE ANALYSIS**

Examine each variable individually:

Numeric distributions: Calculate mean, median, mode, standard deviation, IQR, skewness, and kurtosis. Visualize with histograms and box plots. Identify the distribution shape—normal, skewed, bimodal, uniform. Note the range and check for impossible values (negative ages, future dates).

Outlier detection: Use multiple methods—IQR (1.5x outside quartiles), z-score (>3 standard deviations), and domain knowledge. Distinguish between errors (data quality issues) and genuine extreme values (important signals). Document outliers but don't automatically remove them.

Categorical distributions: Calculate frequency counts and percentages. Visualize with bar charts. Identify dominant categories, rare categories (<1% frequency), and unexpected values. Check for typos and inconsistent coding (e.g., "Yes", "yes", "Y").

Temporal patterns: For datetime variables, check the range, gaps, and granularity. Look for day-of-week effects, seasonality, and trends. Identify anomalous periods that might affect analysis.

**4. BIVARIATE ANALYSIS**

Explore relationships between pairs of variables:

Numeric-numeric relationships: Calculate Pearson correlation for linear relationships, Spearman for monotonic. Visualize with scatter plots and correlation heatmaps. Look for non-linear patterns that correlation coefficients miss. Note that correlation doesn't imply causation.

Categorical-categorical associations: Use chi-square tests for independence. Calculate Cramér's V for association strength. Visualize with heatmaps of contingency tables. Identify which category combinations are over- or under-represented.

Numeric-categorical relationships: Compare distributions across categories with box plots or violin plots. Use t-tests (2 groups) or ANOVA (>2 groups) to test for significant differences. Calculate effect sizes (Cohen's d, eta-squared) not just p-values.

Target variable relationships: If you have a target, analyze how each feature relates to it. For classification, compare feature distributions across classes. For regression, examine correlations and scatter plots. This informs feature selection and engineering.

**5. MULTIVARIATE ANALYSIS**

Look at higher-order patterns:

Correlation structure: Examine the full correlation matrix. Identify clusters of correlated variables—they provide redundant information. High correlations (>0.8) indicate multicollinearity issues for linear models. Consider which to keep based on business meaning and data quality.

Dimensionality reduction: Apply PCA to understand variance structure. How many components explain 90% of variance? Examine loadings to interpret components. Use t-SNE or UMAP for visualization of high-dimensional data—look for natural clusters.

Interaction effects: Some relationships only appear when conditioning on a third variable. Simpson's paradox is real. Facet plots by key categorical variables to reveal hidden patterns.

Multicollinearity assessment: Calculate VIF (variance inflation factor) for regression contexts. VIF > 5 indicates concerning collinearity. VIF > 10 requires action—drop variables, combine them, or use regularization.

**6. DATA QUALITY ASSESSMENT**

Evaluate fitness for purpose:

Accuracy: Do values match reality? Validate against known truths or cross-reference with other sources. Check for systematic biases—are certain groups under-represented?

Consistency: Are related fields logically consistent? Does end_date always follow start_date? Do quantities match totals? Do categories align with definitions?

Completeness: Beyond missing values, is the data representative? Are there gaps in time series? Are all expected categories present? Is the sample size sufficient for the analysis goals?

Timeliness: Is the data current enough for the use case? How old is the most recent record? How frequently is it updated? Stale data may not reflect current reality.

**7. SEGMENTATION AND PATTERNS**

Discover natural groupings:

Clustering exploration: Apply k-means with different k values. Use elbow method and silhouette scores to select k. Profile clusters—what makes each distinct? Clusters often reveal natural customer segments, product categories, or behavior patterns.

Anomaly detection: Use isolation forest, LOF, or DBSCAN to identify unusual records. Anomalies may be errors to fix or interesting cases to investigate. Separate technical anomalies (data issues) from substantive anomalies (genuine outliers).

Temporal patterns: For time series, decompose into trend, seasonality, and residual. Identify change points where patterns shift. Look for cyclical patterns at different frequencies—daily, weekly, monthly, yearly.

Subgroup analysis: Segment by key categorical variables and repeat univariate analysis. Do patterns hold across segments or do they differ? Segment-specific insights often drive the most actionable recommendations.

**8. VISUALIZATION AND COMMUNICATION**

Create compelling visual stories:

Distribution visualizations: Histograms for continuous, bar charts for categorical, box plots for comparisons. Use appropriate bin sizes. Label axes clearly. Include summary statistics in annotations.

Relationship visualizations: Scatter plots with trend lines for numeric pairs. Heatmaps for correlation matrices. Faceted plots for conditional relationships. Pair plots for overview of all numeric relationships.

Composition and comparison: Stacked bars for proportions. Grouped bars for comparisons. Small multiples for patterns across categories. Choose chart types that match the analytical question.

Dashboard assembly: Arrange visualizations to tell a story. Start with overview, then drill into details. Highlight key findings with callouts. Make it easy for stakeholders to extract insights quickly.

**9. FINDINGS AND RECOMMENDATIONS**

Synthesize insights into action:

Key findings summary: What are the 5-7 most important discoveries? Prioritize by business impact and surprise value. Support each finding with specific statistics and visualizations.

Data quality recommendations: What cleaning is needed before modeling? Which variables need imputation, transformation, or encoding? What records should be excluded and why?

Feature engineering opportunities: What derived variables would be valuable? Ratios, aggregations, time-based features? What domain knowledge could be encoded?

Next steps: What additional analysis would be valuable? What hypotheses should be tested? What modeling approaches are appropriate given the data characteristics?

Deliver your exploratory analysis as:

1. **EXECUTIVE SUMMARY** - 5-7 key findings with business implications

2. **DATA QUALITY REPORT** - Completeness, accuracy, consistency assessment with remediation plan

3. **STATISTICAL PROFILE** - Variable summaries, distributions, relationships

4. **VISUALIZATION GALLERY** - Key charts with interpretations

5. **PATTERN INSIGHTS** - Segments, anomalies, trends discovered

6. **RECOMMENDATIONS** - Data preparation steps, feature engineering, modeling guidance

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{DATASET_DESCRIPTION}` | Dataset name and context | "E-commerce transaction log", "Patient health records", "IoT sensor readings" |
| `{DATA_DIMENSIONS}` | Size and structure | "500K rows × 45 columns spanning 2 years", "10M events with 20 features" |
| `{ANALYSIS_OBJECTIVE}` | Purpose of the analysis | "Prepare for churn prediction model", "Understand customer segments", "Identify data quality issues" |

## Usage Examples

### Example 1: E-commerce Customer Analysis

```
Perform exploratory data analysis on E-commerce Customer Dataset 
containing 100K customers × 35 columns over 3 years to support 
customer segmentation and lifetime value modeling.
```

**Expected Output:**
- Profile: 35 columns (12 numeric, 15 categorical, 8 datetime), 2.3% overall missing
- Quality: Email inconsistencies (5%), duplicate phone numbers (1.2%), future order dates (0.1%)
- Key finding: 20% of customers drive 80% of revenue; clear RFM segments emerge
- Correlations: Order frequency strongly predicts LTV (r=0.72); acquisition channel affects retention
- Segments: 5 natural clusters—high-value loyalists, discount seekers, one-time buyers, dormant, new
- Recommendations: Impute missing demographics with mode, create recency/frequency/monetary features, address duplicate detection before modeling

### Example 2: Manufacturing Sensor Data

```
Perform exploratory data analysis on Production Line Sensors 
containing 5M readings × 50 sensors over 6 months to support 
predictive maintenance modeling.
```

**Expected Output:**
- Profile: 50 sensor columns (all numeric), timestamp index, 0.3% missing (sensor dropouts)
- Quality: 12 sensors show periodic calibration drift; 3 sensors have stuck-at values
- Key finding: Temperature and vibration spikes precede 85% of failures by 2-4 hours
- Correlations: Strong multicollinearity among related sensors; 15 principal components explain 95% variance
- Anomalies: 47 anomalous periods identified; 38 correlate with maintenance logs
- Recommendations: Engineer rolling statistics (mean, std, trend over 1hr windows), handle sensor drift with normalization, use PCA features to reduce dimensionality

### Example 3: Healthcare Claims Data

```
Perform exploratory data analysis on Insurance Claims Dataset 
containing 2M claims × 60 fields over 5 years to support 
fraud detection model development.
```

**Expected Output:**
- Profile: 60 columns (25 numeric, 30 categorical, 5 datetime), 8% overall missing
- Quality: Diagnosis code inconsistencies (3%), provider ID duplicates (0.5%), claim amount outliers (2%)
- Key finding: 0.5% of claims show fraud indicators; concentrated in specific provider networks
- Relationships: Claim amount correlates with diagnosis complexity (r=0.45); length of stay predicts cost
- Patterns: Seasonal spikes in certain procedure codes; weekend claims 30% more likely to be flagged
- Recommendations: Create provider-level aggregates, engineer claim velocity features, address class imbalance (0.5% fraud rate) in modeling strategy

## Cross-References

- **Experimentation:** experimentation-design.md - When EDA generates hypotheses to test
- **Modeling:** predictive-modeling-framework.md - Taking EDA insights into model building
- **Dashboards:** dashboard-design-patterns.md - Presenting EDA findings to stakeholders
- **Data Quality:** data-governance-framework.md - Systematic data quality management
