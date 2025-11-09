---
title: Exploratory Data Analysis Framework Template
category: data-analytics/Data Science
tags: [automation, data-analytics, data-science, design, framework, machine-learning, research, template]
use_cases:
  - Implementing conduct comprehensive exploratory data analysis to understand data characteristi...
  - Project planning and execution
  - Strategy development
related_templates:
  - dashboard-design-patterns.md
  - data-governance-framework.md
  - predictive-modeling-framework.md
last_updated: 2025-11-09
---

# Exploratory Data Analysis Framework Template

## Purpose
Conduct comprehensive exploratory data analysis to understand data characteristics, identify patterns, detect anomalies, and prepare insights for advanced analytics and modeling.

## Template

```
You are a data scientist performing exploratory data analysis. Conduct a thorough EDA on the dataset [DATASET_NAME] containing [DATA_DESCRIPTION] to support [ANALYSIS_OBJECTIVE] for [BUSINESS_CONTEXT].

PROJECT OVERVIEW:
Business Context:
- Industry domain: [INDUSTRY_DOMAIN]
- Business problem: [BUSINESS_PROBLEM]
- Stakeholders: [STAKEHOLDERS]
- Success criteria: [SUCCESS_CRITERIA]
- Timeline: [PROJECT_TIMELINE]
- Budget constraints: [BUDGET_CONSTRAINTS]

Analysis Objectives:
- Primary objective: [PRIMARY_OBJECTIVE]
- Secondary objectives: [SECONDARY_OBJECTIVES]
- Key questions: [KEY_QUESTIONS]
- Hypotheses to test: [HYPOTHESES]
- Expected outcomes: [EXPECTED_OUTCOMES]

DATASET OVERVIEW:
Basic Information:
- Dataset name: [DATASET_NAME]
- Source system: [SOURCE_SYSTEM]
- Collection method: [COLLECTION_METHOD]
- Collection period: [TIME_PERIOD]
- Last updated: [LAST_UPDATE]
- Update frequency: [UPDATE_FREQUENCY]
- File format: [FILE_FORMAT]
- File size: [FILE_SIZE]
- Compression: [COMPRESSION_TYPE]

Dimensions & Structure:
- Number of rows: [NUM_ROWS]
- Number of columns: [NUM_COLUMNS]
- Memory usage: [MEMORY_USAGE]
- Storage requirements: [STORAGE_REQUIREMENTS]
- Data lineage: [DATA_LINEAGE]
- Data governance: [GOVERNANCE_RULES]

Data Quality Overview:
- Completeness score: [COMPLETENESS_SCORE]%
- Accuracy score: [ACCURACY_SCORE]%
- Consistency score: [CONSISTENCY_SCORE]%
- Timeliness score: [TIMELINESS_SCORE]%
- Validity score: [VALIDITY_SCORE]%
- Uniqueness score: [UNIQUENESS_SCORE]%

VARIABLE PROFILING:
Column Inventory:
Total columns: [TOTAL_COLUMNS]
- Numerical columns: [NUM_COLUMNS_COUNT] ([NUM_PERCENTAGE]%)
- Categorical columns: [CAT_COLUMNS_COUNT] ([CAT_PERCENTAGE]%)
- DateTime columns: [DATE_COLUMNS_COUNT] ([DATE_PERCENTAGE]%)
- Text/String columns: [TEXT_COLUMNS_COUNT] ([TEXT_PERCENTAGE]%)
- Boolean columns: [BOOL_COLUMNS_COUNT] ([BOOL_PERCENTAGE]%)
- Mixed-type columns: [MIXED_COLUMNS_COUNT] ([MIXED_PERCENTAGE]%)

For each variable [VARIABLE_NAME]:

Metadata & Schema:
- Column name: [COLUMN_NAME]
- Data type: [DATA_TYPE]
- Variable classification: [VAR_CLASSIFICATION] (Continuous/Discrete/Ordinal/Nominal)
- Measurement level: [MEASUREMENT_LEVEL] (Ratio/Interval/Ordinal/Nominal)
- Business meaning: [BUSINESS_MEANING]
- Domain constraints: [DOMAIN_CONSTRAINTS]
- Expected range: [EXPECTED_RANGE]
- Units of measurement: [UNITS]

Data Quality Metrics:
- Total count: [TOTAL_COUNT]
- Non-null count: [NON_NULL_COUNT]
- Null count: [NULL_COUNT]
- Null percentage: [NULL_PERCENTAGE]%
- Zero count: [ZERO_COUNT]
- Zero percentage: [ZERO_PERCENTAGE]%
- Blank/empty count: [BLANK_COUNT]
- Invalid entries: [INVALID_COUNT]

NUMERICAL VARIABLES ANALYSIS:
For each numerical variable [NUM_VAR]:

Descriptive Statistics:
Central Tendency:
- Mean: [MEAN_VALUE]
- Median: [MEDIAN_VALUE]
- Mode: [MODE_VALUE]
- Trimmed mean (5%): [TRIMMED_MEAN_5]
- Trimmed mean (10%): [TRIMMED_MEAN_10]
- Geometric mean: [GEOMETRIC_MEAN]
- Harmonic mean: [HARMONIC_MEAN]

Variability Measures:
- Standard deviation: [STD_DEV]
- Variance: [VARIANCE]
- Range: [RANGE]
- Interquartile range (IQR): [IQR]
- Mean absolute deviation: [MAD]
- Coefficient of variation: [CV]
- Relative standard deviation: [RSD]

Distribution Shape:
- Skewness: [SKEWNESS]
- Kurtosis: [KURTOSIS]
- Excess kurtosis: [EXCESS_KURTOSIS]
- Distribution type: [DISTRIBUTION_TYPE]
- Normality assessment: [NORMALITY_ASSESSMENT]

Percentile Analysis:
- Minimum: [MIN_VALUE]
- 1st percentile: [P01]
- 5th percentile: [P05]
- 10th percentile: [P10]
- 25th percentile (Q1): [Q1]
- 50th percentile (Q2/Median): [Q2]
- 75th percentile (Q3): [Q3]
- 90th percentile: [P90]
- 95th percentile: [P95]
- 99th percentile: [P99]
- Maximum: [MAX_VALUE]

Distribution Testing:
Statistical Tests:
- Shapiro-Wilk test: W = [SHAPIRO_W], p = [SHAPIRO_P]
- Kolmogorov-Smirnov test: D = [KS_D], p = [KS_P]
- Anderson-Darling test: A² = [AD_A2], p = [AD_P]
- Jarque-Bera test: JB = [JB_STAT], p = [JB_P]
- D'Agostino-Pearson test: K² = [DP_K2], p = [DP_P]

Distribution Fitting:
- Best fit distribution: [BEST_FIT_DIST]
- Distribution parameters: [DIST_PARAMS]
- Goodness of fit (AIC): [AIC_SCORE]
- Goodness of fit (BIC): [BIC_SCORE]
- Kolmogorov-Smirnov p-value: [FIT_KS_P]

Outlier Detection:
IQR Method:
- Lower fence: [IQR_LOWER]
- Upper fence: [IQR_UPPER]
- Outliers count: [IQR_OUTLIERS_COUNT]
- Outlier percentage: [IQR_OUTLIER_PERCENT]%
- Extreme outliers: [IQR_EXTREME]

Z-Score Method:
- Outliers (|z| > 2): [Z2_OUTLIERS]
- Outliers (|z| > 3): [Z3_OUTLIERS]
- Maximum |z-score|: [MAX_ZSCORE]
- Outlier indices: [Z_OUTLIER_INDICES]

Modified Z-Score:
- Outliers (|modified z| > 3.5): [MOD_Z_OUTLIERS]
- Median absolute deviation: [MAD_VALUE]

Isolation Forest:
- Contamination fraction: [IF_CONTAMINATION]
- Anomaly count: [IF_ANOMALIES]
- Anomaly scores: [IF_SCORES]

Local Outlier Factor:
- LOF threshold: [LOF_THRESHOLD]
- LOF outliers: [LOF_OUTLIERS]
- Average LOF score: [AVG_LOF]

Business Rules Validation:
- Rule violations: [RULE_VIOLATIONS]
- Data consistency issues: [CONSISTENCY_ISSUES]
- Domain expert flagged values: [EXPERT_FLAGS]

CATEGORICAL VARIABLES ANALYSIS:
For each categorical variable [CAT_VAR]:

Cardinality Analysis:
- Unique values count: [UNIQUE_COUNT]
- Cardinality ratio: [CARDINALITY_RATIO]
- Effective cardinality: [EFFECTIVE_CARDINALITY]
- High cardinality flag: [HIGH_CARDINALITY_FLAG]

Value Distribution:
Most Frequent Values (Top 20):
1. [VALUE_1]: Count [COUNT_1] ([PERCENT_1]%)
2. [VALUE_2]: Count [COUNT_2] ([PERCENT_2]%)
3. [VALUE_3]: Count [COUNT_3] ([PERCENT_3]%)
4. [VALUE_4]: Count [COUNT_4] ([PERCENT_4]%)
5. [VALUE_5]: Count [COUNT_5] ([PERCENT_5]%)
[... continue for top 20]

Frequency Statistics:
- Mode (most frequent): [MODE_CAT]
- Mode frequency: [MODE_FREQ]
- Mode percentage: [MODE_PERCENT]%
- Second mode: [SECOND_MODE]
- Frequency of second mode: [SECOND_MODE_FREQ]

Category Distribution Metrics:
- Entropy: [ENTROPY]
- Gini impurity: [GINI_IMPURITY]
- Simpson's diversity: [SIMPSON_DIVERSITY]
- Shannon diversity: [SHANNON_DIVERSITY]
- Evenness index: [EVENNESS_INDEX]

Rare Category Analysis:
- Categories with < 1% frequency: [RARE_1_PERCENT]
- Categories with < 5% frequency: [RARE_5_PERCENT]
- Singleton categories (count = 1): [SINGLETON_COUNT]
- Categories representing 80% of data: [PARETO_80_CATEGORIES]
- Long tail categories: [LONG_TAIL_CATEGORIES]

TEMPORAL ANALYSIS:
(For time-series and date variables)

Time Range & Coverage:
- Start date/time: [START_DATETIME]
- End date/time: [END_DATETIME]
- Total duration: [TOTAL_DURATION]
- Time span in days: [DAYS_SPAN]
- Data granularity: [TIME_GRANULARITY]
- Expected frequency: [EXPECTED_FREQUENCY]
- Actual frequency: [ACTUAL_FREQUENCY]

Temporal Gaps:
- Missing time periods: [MISSING_PERIODS]
- Gap count: [GAP_COUNT]
- Average gap duration: [AVG_GAP_DURATION]
- Longest gap: [LONGEST_GAP]
- Gap pattern: [GAP_PATTERN]

Temporal Distribution:
- Records per day: [RECORDS_PER_DAY]
- Records per week: [RECORDS_PER_WEEK]
- Records per month: [RECORDS_PER_MONTH]
- Records per quarter: [RECORDS_PER_QUARTER]
- Records per year: [RECORDS_PER_YEAR]

Seasonality Analysis:
Seasonal Decomposition:
- Trend component: [TREND_COMPONENT]
- Seasonal component: [SEASONAL_COMPONENT]
- Residual component: [RESIDUAL_COMPONENT]
- Seasonal strength: [SEASONAL_STRENGTH]
- Trend strength: [TREND_STRENGTH]

Seasonal Patterns:
- Weekly seasonality: [WEEKLY_SEASONALITY]
- Monthly seasonality: [MONTHLY_SEASONALITY]
- Quarterly seasonality: [QUARTERLY_SEASONALITY]
- Annual seasonality: [ANNUAL_SEASONALITY]
- Holiday effects: [HOLIDAY_EFFECTS]

Time Series Statistics:
- Stationarity (ADF test): [ADF_STATISTIC], p = [ADF_PVALUE]
- KPSS test: [KPSS_STATISTIC], p = [KPSS_PVALUE]
- Phillips-Perron test: [PP_STATISTIC], p = [PP_PVALUE]
- Autocorrelation at lag 1: [ACF_LAG1]
- Partial autocorrelation at lag 1: [PACF_LAG1]

CORRELATION & ASSOCIATION ANALYSIS:
Numerical Correlation Matrix:
Pearson Correlations:
[PEARSON_CORRELATION_MATRIX]

Top Positive Correlations:
1. [VAR_A1] ↔ [VAR_B1]: r = [CORR_1] (p = [P_1])
2. [VAR_A2] ↔ [VAR_B2]: r = [CORR_2] (p = [P_2])
3. [VAR_A3] ↔ [VAR_B3]: r = [CORR_3] (p = [P_3])
4. [VAR_A4] ↔ [VAR_B4]: r = [CORR_4] (p = [P_4])
5. [VAR_A5] ↔ [VAR_B5]: r = [CORR_5] (p = [P_5])

Top Negative Correlations:
1. [VAR_C1] ↔ [VAR_D1]: r = [NEG_CORR_1] (p = [NEG_P_1])
2. [VAR_C2] ↔ [VAR_D2]: r = [NEG_CORR_2] (p = [NEG_P_2])
3. [VAR_C3] ↔ [VAR_D3]: r = [NEG_CORR_3] (p = [NEG_P_3])

Non-Parametric Correlations:
Spearman Rank Correlation:
[SPEARMAN_CORRELATION_MATRIX]

Kendall's Tau:
[KENDALL_CORRELATION_MATRIX]

Distance Correlation:
- Distance correlation matrix: [DISTANCE_CORR_MATRIX]
- Maximal information coefficient: [MIC_MATRIX]

Categorical Associations:
Chi-Square Independence Tests:
1. [CAT_VAR_1] × [CAT_VAR_2]: χ² = [CHI2_1], df = [DF_1], p = [P_CHI_1]
2. [CAT_VAR_3] × [CAT_VAR_4]: χ² = [CHI2_2], df = [DF_2], p = [P_CHI_2]
3. [CAT_VAR_5] × [CAT_VAR_6]: χ² = [CHI2_3], df = [DF_3], p = [P_CHI_3]

Association Strength:
Cramér's V:
1. [CAT_VAR_1] × [CAT_VAR_2]: V = [CRAMER_1]
2. [CAT_VAR_3] × [CAT_VAR_4]: V = [CRAMER_2]
3. [CAT_VAR_5] × [CAT_VAR_6]: V = [CRAMER_3]

Phi Coefficient (2x2 tables):
1. [BINARY_VAR_1] × [BINARY_VAR_2]: φ = [PHI_1]
2. [BINARY_VAR_3] × [BINARY_VAR_4]: φ = [PHI_2]

Mixed-Type Associations:
Point-Biserial Correlation:
1. [NUM_VAR_1] × [BINARY_VAR_1]: r_pb = [PB_CORR_1]
2. [NUM_VAR_2] × [BINARY_VAR_2]: r_pb = [PB_CORR_2]

ANOVA (Numerical vs Categorical):
1. [NUM_VAR_1] by [CAT_VAR_1]: F = [F_STAT_1], p = [P_ANOVA_1], η² = [ETA_SQ_1]
2. [NUM_VAR_2] by [CAT_VAR_2]: F = [F_STAT_2], p = [P_ANOVA_2], η² = [ETA_SQ_2]

MULTIVARIATE ANALYSIS:
Dimensionality Reduction:
Principal Component Analysis:
- Components for 90% variance: [PCA_90_COMPONENTS]
- Components for 95% variance: [PCA_95_COMPONENTS]
- Components for 99% variance: [PCA_99_COMPONENTS]
- PC1 variance explained: [PC1_VARIANCE]%
- PC2 variance explained: [PC2_VARIANCE]%
- PC3 variance explained: [PC3_VARIANCE]%
- Cumulative variance (first 5 PCs): [CUMVAR_5PC]%

Factor Analysis:
- Number of factors: [NUM_FACTORS]
- Factor loadings matrix: [FACTOR_LOADINGS]
- Communalities: [COMMUNALITIES]
- Kaiser-Meyer-Olkin (KMO): [KMO_SCORE]
- Bartlett's test: χ² = [BARTLETT_CHI2], p = [BARTLETT_P]

Independent Component Analysis:
- ICA components: [ICA_COMPONENTS]
- Mixing matrix condition: [MIXING_CONDITION]
- Source signal quality: [SOURCE_QUALITY]

t-SNE Analysis:
- Perplexity parameter: [TSNE_PERPLEXITY]
- Cluster visualization quality: [CLUSTER_SEPARATION]
- Dimensional embedding stress: [EMBEDDING_STRESS]

UMAP Analysis:
- Neighbors parameter: [UMAP_NEIGHBORS]
- Min distance parameter: [UMAP_MIN_DIST]
- Local connectivity: [LOCAL_CONNECTIVITY]
- Global structure preservation: [GLOBAL_STRUCTURE]

Clustering Tendency:
Hopkins Statistic: [HOPKINS_STATISTIC]
- Clustering tendency: [CLUSTERING_TENDENCY]
- Random data likelihood: [RANDOM_LIKELIHOOD]

Multicollinearity Assessment:
Variance Inflation Factors:
1. [VAR_VIF_1]: VIF = [VIF_1]
2. [VAR_VIF_2]: VIF = [VIF_2]
3. [VAR_VIF_3]: VIF = [VIF_3]
4. [VAR_VIF_4]: VIF = [VIF_4]
5. [VAR_VIF_5]: VIF = [VIF_5]

Variables with VIF > 5: [HIGH_VIF_VARS]
Variables with VIF > 10: [VERY_HIGH_VIF_VARS]

Condition Index: [CONDITION_INDEX]
Eigenvalue analysis: [EIGENVALUE_ANALYSIS]

DATA QUALITY DEEP DIVE:
Missing Data Analysis:
Missing Data Patterns:
- Complete cases: [COMPLETE_CASES] ([COMPLETE_PERCENT]%)
- Cases with any missing: [ANY_MISSING] ([ANY_MISSING_PERCENT]%)
- Variables with missing data: [VARS_WITH_MISSING]

Missing Data Mechanisms:
- MCAR test (Little's): χ² = [LITTLE_CHI2], p = [LITTLE_P]
- MAR assessment: [MAR_ASSESSMENT]
- MNAR indicators: [MNAR_INDICATORS]

Missing Data Patterns:
Pattern 1: [PATTERN_1] - Count: [PATTERN_1_COUNT]
Pattern 2: [PATTERN_2] - Count: [PATTERN_2_COUNT]
Pattern 3: [PATTERN_3] - Count: [PATTERN_3_COUNT]
[... for top patterns]

Imputation Impact Assessment:
- Mean imputation bias: [MEAN_IMP_BIAS]
- Median imputation bias: [MEDIAN_IMP_BIAS]
- Mode imputation bias: [MODE_IMP_BIAS]
- Advanced imputation options: [ADVANCED_IMP_OPTIONS]

Duplicate Analysis:
Exact Duplicates:
- Exact duplicate count: [EXACT_DUPES]
- Exact duplicate percentage: [EXACT_DUPE_PERCENT]%
- Duplicate patterns: [DUPE_PATTERNS]

Near Duplicates:
- Similarity threshold: [SIMILARITY_THRESHOLD]
- Near duplicate pairs: [NEAR_DUPE_PAIRS]
- Fuzzy matching results: [FUZZY_MATCHES]

Unique Identifier Analysis:
- Primary key candidates: [PK_CANDIDATES]
- Composite key options: [COMPOSITE_KEYS]
- Uniqueness violations: [UNIQUENESS_VIOLATIONS]

Data Consistency:
Cross-Field Validation:
- Logical consistency rules: [LOGIC_RULES]
- Rule violations count: [RULE_VIOLATIONS_COUNT]
- Consistency score: [CONSISTENCY_SCORE]%

Format Consistency:
- Date format issues: [DATE_FORMAT_ISSUES]
- Numeric format issues: [NUMERIC_FORMAT_ISSUES]
- Text encoding issues: [ENCODING_ISSUES]
- Case sensitivity issues: [CASE_ISSUES]

Referential Integrity:
- Foreign key violations: [FK_VIOLATIONS]
- Orphaned records: [ORPHANED_RECORDS]
- Referential consistency: [REF_CONSISTENCY]%

ADVANCED STATISTICAL ANALYSIS:
Distribution Analysis:
Goodness-of-Fit Testing:
For [VAR_NAME]:
- Normal distribution: KS = [NORMAL_KS], p = [NORMAL_P]
- Exponential distribution: KS = [EXP_KS], p = [EXP_P]
- Uniform distribution: KS = [UNIFORM_KS], p = [UNIFORM_P]
- Log-normal distribution: KS = [LOGNORM_KS], p = [LOGNORM_P]
- Gamma distribution: KS = [GAMMA_KS], p = [GAMMA_P]

Robust Statistics:
- Median absolute deviation: [MAD_ROBUST]
- Interquartile range: [IQR_ROBUST]
- Trimmed mean (10%): [TRIMMED_MEAN_10]
- Winsorized statistics: [WINSORIZED_STATS]
- Huber estimator: [HUBER_ESTIMATOR]

Bootstrap Analysis:
- Bootstrap samples: [BOOTSTRAP_SAMPLES]
- Confidence interval (95%): [CI_95_LOWER] - [CI_95_UPPER]
- Bootstrap bias: [BOOTSTRAP_BIAS]
- Bootstrap standard error: [BOOTSTRAP_SE]

Hypothesis Testing:
Two-Sample Tests:
- Independent t-test: t = [T_STAT], p = [T_P]
- Mann-Whitney U: U = [MW_U], p = [MW_P]
- Kolmogorov-Smirnov 2-sample: D = [KS2_D], p = [KS2_P]
- Chi-square test of independence: χ² = [CHI2_INDEP], p = [CHI2_INDEP_P]

Multiple Comparisons:
- Bonferroni correction: [BONFERRONI_ALPHA]
- Holm correction: [HOLM_ALPHA]
- FDR correction: [FDR_ALPHA]
- Tukey HSD: [TUKEY_HSD_RESULTS]

SEGMENTATION & PATTERN DISCOVERY:
Natural Segmentation:
K-Means Clustering:
- Optimal K (elbow method): [KMEANS_OPTIMAL_K]
- Optimal K (silhouette): [SILHOUETTE_OPTIMAL_K]
- Inertia at optimal K: [KMEANS_INERTIA]
- Silhouette score: [SILHOUETTE_SCORE]

Cluster Profiles:
Cluster 1 ([CLUSTER_1_SIZE] records):
- Key characteristics: [CLUSTER_1_PROFILE]
- Centroid values: [CLUSTER_1_CENTROID]
- Within-cluster variance: [CLUSTER_1_VARIANCE]

Cluster 2 ([CLUSTER_2_SIZE] records):
- Key characteristics: [CLUSTER_2_PROFILE]
- Centroid values: [CLUSTER_2_CENTROID]
- Within-cluster variance: [CLUSTER_2_VARIANCE]

Hierarchical Clustering:
- Linkage method: [LINKAGE_METHOD]
- Distance metric: [DISTANCE_METRIC]
- Dendrogram insights: [DENDROGRAM_INSIGHTS]
- Cophenetic correlation: [COPHENETIC_CORR]

DBSCAN Clustering:
- Epsilon parameter: [DBSCAN_EPS]
- Min samples: [DBSCAN_MIN_SAMPLES]
- Number of clusters: [DBSCAN_CLUSTERS]
- Noise points: [DBSCAN_NOISE]

Pattern Mining:
Association Rules:
- Frequent itemsets: [FREQUENT_ITEMSETS]
- Support threshold: [SUPPORT_THRESHOLD]
- Confidence threshold: [CONFIDENCE_THRESHOLD]
- Lift analysis: [LIFT_ANALYSIS]

Sequential Patterns:
- Pattern mining algorithm: [PATTERN_ALGORITHM]
- Discovered sequences: [DISCOVERED_SEQUENCES]
- Pattern confidence: [PATTERN_CONFIDENCE]

VISUALIZATION INSIGHTS:
Distribution Visualizations:
Histogram Analysis:
1. [VAR_HIST_1]:
   - Distribution shape: [HIST_SHAPE_1]
   - Modality: [HIST_MODALITY_1]
   - Optimal bins: [OPTIMAL_BINS_1]
   - Outlier visibility: [OUTLIER_VISIBILITY_1]

2. [VAR_HIST_2]:
   - Distribution shape: [HIST_SHAPE_2]
   - Modality: [HIST_MODALITY_2]
   - Optimal bins: [OPTIMAL_BINS_2]
   - Outlier visibility: [OUTLIER_VISIBILITY_2]

Box Plot Insights:
1. [VAR_BOX_1]:
   - Median position: [MEDIAN_POSITION_1]
   - IQR symmetry: [IQR_SYMMETRY_1]
   - Whisker length: [WHISKER_LENGTH_1]
   - Outlier count: [BOX_OUTLIER_COUNT_1]

2. [VAR_BOX_2]:
   - Median position: [MEDIAN_POSITION_2]
   - IQR symmetry: [IQR_SYMMETRY_2]
   - Whisker length: [WHISKER_LENGTH_2]
   - Outlier count: [BOX_OUTLIER_COUNT_2]

Violin Plot Analysis:
- Kernel density estimation: [KDE_BANDWIDTH]
- Distribution width variation: [DISTRIBUTION_WIDTH]
- Multi-modal indicators: [MULTIMODAL_INDICATORS]

Relationship Visualizations:
Scatter Plot Analysis:
1. [VAR_X_1] vs [VAR_Y_1]:
   - Relationship type: [RELATIONSHIP_TYPE_1]
   - Correlation strength: [VISUAL_CORR_1]
   - Outlier patterns: [SCATTER_OUTLIERS_1]
   - Cluster formations: [SCATTER_CLUSTERS_1]

2. [VAR_X_2] vs [VAR_Y_2]:
   - Relationship type: [RELATIONSHIP_TYPE_2]
   - Correlation strength: [VISUAL_CORR_2]
   - Outlier patterns: [SCATTER_OUTLIERS_2]
   - Cluster formations: [SCATTER_CLUSTERS_2]

Heatmap Insights:
Correlation Heatmap:
- Strong positive blocks: [POS_CORR_BLOCKS]
- Strong negative blocks: [NEG_CORR_BLOCKS]
- Correlation clusters: [CORR_CLUSTERS]

Missing Data Heatmap:
- Missing data patterns: [MISSING_PATTERNS_VISUAL]
- Systematic missingness: [SYSTEMATIC_MISSING]
- Random missingness: [RANDOM_MISSING]

Temporal Visualizations:
Time Series Plots:
- Trend identification: [VISUAL_TREND]
- Seasonal patterns: [VISUAL_SEASONALITY]
- Anomaly detection: [VISUAL_ANOMALIES]
- Volatility periods: [VOLATILITY_PERIODS]

Calendar Heatmaps:
- Daily patterns: [DAILY_PATTERNS]
- Weekly patterns: [WEEKLY_PATTERNS]
- Monthly patterns: [MONTHLY_PATTERNS]
- Holiday effects: [HOLIDAY_EFFECTS_VISUAL]

TARGET VARIABLE ANALYSIS:
(If supervised learning context)

Target Distribution:
- Target variable: [TARGET_VARIABLE]
- Variable type: [TARGET_TYPE]
- Distribution summary: [TARGET_DISTRIBUTION]
- Class balance (if classification): [CLASS_BALANCE]

Classification Targets:
- Number of classes: [NUM_CLASSES]
- Majority class: [MAJORITY_CLASS] ([MAJORITY_PERCENT]%)
- Minority class: [MINORITY_CLASS] ([MINORITY_PERCENT]%)
- Imbalance ratio: [IMBALANCE_RATIO]:1
- Class distribution: [CLASS_DISTRIBUTION]

Regression Targets:
- Target range: [TARGET_RANGE]
- Target mean: [TARGET_MEAN]
- Target median: [TARGET_MEDIAN]
- Target std: [TARGET_STD]
- Target skewness: [TARGET_SKEWNESS]

Feature-Target Relationships:
Top Predictive Features (Univariate):
1. [PRED_FEATURE_1]: Association = [ASSOCIATION_1]
2. [PRED_FEATURE_2]: Association = [ASSOCIATION_2]
3. [PRED_FEATURE_3]: Association = [ASSOCIATION_3]
4. [PRED_FEATURE_4]: Association = [ASSOCIATION_4]
5. [PRED_FEATURE_5]: Association = [ASSOCIATION_5]

Mutual Information Scores:
1. [MI_FEATURE_1]: MI = [MI_SCORE_1]
2. [MI_FEATURE_2]: MI = [MI_SCORE_2]
3. [MI_FEATURE_3]: MI = [MI_SCORE_3]

Information Value (for binary targets):
1. [IV_FEATURE_1]: IV = [IV_SCORE_1]
2. [IV_FEATURE_2]: IV = [IV_SCORE_2]
3. [IV_FEATURE_3]: IV = [IV_SCORE_3]

BUSINESS INSIGHTS:
Key Business Findings:
1. Market Segmentation:
   - Primary segments identified: [BUSINESS_SEGMENTS]
   - Segment characteristics: [SEGMENT_CHARACTERISTICS]
   - Business value per segment: [SEGMENT_VALUE]

2. Customer Behavior:
   - Usage patterns: [USAGE_PATTERNS]
   - Engagement metrics: [ENGAGEMENT_METRICS]
   - Churn indicators: [CHURN_INDICATORS]

3. Operational Insights:
   - Process bottlenecks: [PROCESS_BOTTLENECKS]
   - Efficiency opportunities: [EFFICIENCY_OPPORTUNITIES]
   - Cost drivers: [COST_DRIVERS]

4. Revenue Drivers:
   - High-value features: [HIGH_VALUE_FEATURES]
   - Revenue correlation: [REVENUE_CORRELATION]
   - Monetization opportunities: [MONETIZATION_OPPS]

Risk Assessment:
Data Risks:
- Data quality risks: [DQ_RISKS]
- Privacy concerns: [PRIVACY_CONCERNS]
- Compliance issues: [COMPLIANCE_ISSUES]
- Bias indicators: [BIAS_INDICATORS]

Business Risks:
- Sample bias: [SAMPLE_BIAS]
- Temporal relevance: [TEMPORAL_RELEVANCE]
- External validity: [EXTERNAL_VALIDITY]
- Confounding factors: [CONFOUNDING_FACTORS]

RECOMMENDATIONS:
Data Preparation Recommendations:
1. Missing Data Strategy:
   - Variables to drop: [DROP_VARIABLES]
   - Imputation methods: [IMPUTATION_METHODS]
   - Missing indicator creation: [MISSING_INDICATORS]

2. Outlier Treatment:
   - Variables for outlier removal: [OUTLIER_REMOVAL_VARS]
   - Variables for transformation: [TRANSFORM_VARS]
   - Winsorization candidates: [WINSORIZE_VARS]

3. Feature Engineering:
   - Derived features to create: [CREATE_FEATURES]
   - Interaction terms: [INTERACTION_TERMS]
   - Polynomial features: [POLYNOMIAL_FEATURES]
   - Binning recommendations: [BINNING_RECOMMENDATIONS]

4. Data Transformation:
   - Log transformations: [LOG_TRANSFORM_VARS]
   - Scaling requirements: [SCALING_VARS]
   - Encoding strategies: [ENCODING_STRATEGIES]
   - Normalization needs: [NORMALIZATION_VARS]

Modeling Recommendations:
1. Algorithm Selection:
   - Recommended algorithms: [RECOMMENDED_ALGORITHMS]
   - Algorithms to avoid: [AVOID_ALGORITHMS]
   - Ensemble opportunities: [ENSEMBLE_OPPORTUNITIES]

2. Validation Strategy:
   - Cross-validation approach: [CV_APPROACH]
   - Train/validation/test split: [DATA_SPLIT_STRATEGY]
   - Temporal validation needs: [TEMPORAL_VALIDATION]

3. Feature Selection:
   - Feature selection methods: [FEATURE_SELECTION_METHODS]
   - Dimensionality reduction: [DIMENSIONALITY_REDUCTION]
   - Feature importance focus: [FEATURE_IMPORTANCE_FOCUS]

Further Analysis Recommendations:
1. Deep Dive Areas:
   - Variables needing investigation: [INVESTIGATE_VARS]
   - Relationships to explore: [EXPLORE_RELATIONSHIPS]
   - Anomalies to understand: [UNDERSTAND_ANOMALIES]

2. Additional Data Needs:
   - External data sources: [EXTERNAL_DATA_SOURCES]
   - Missing variables: [MISSING_VARIABLES]
   - Temporal data needs: [TEMPORAL_DATA_NEEDS]

3. Hypothesis Testing:
   - Statistical tests to perform: [STATISTICAL_TESTS]
   - Business hypotheses: [BUSINESS_HYPOTHESES]
   - A/B test opportunities: [AB_TEST_OPPORTUNITIES]

Next Steps:
1. Immediate actions: [IMMEDIATE_ACTIONS]
2. Short-term priorities: [SHORT_TERM_PRIORITIES]
3. Long-term analysis plan: [LONG_TERM_PLAN]
4. Stakeholder communication: [STAKEHOLDER_COMMUNICATION]
5. Data governance improvements: [GOVERNANCE_IMPROVEMENTS]

OUTPUT: Deliver comprehensive EDA package including:
1. Executive summary with key insights
2. Detailed statistical analysis report
3. Interactive visualization dashboard
4. Data quality assessment
5. Feature engineering roadmap
6. Modeling strategy recommendations
7. Business insights and opportunities
8. Risk assessment and mitigation plan
```

## Variables
[DATASET_NAME, DATA_DESCRIPTION, ANALYSIS_OBJECTIVE, BUSINESS_CONTEXT, INDUSTRY_DOMAIN, BUSINESS_PROBLEM, STAKEHOLDERS, SUCCESS_CRITERIA, PROJECT_TIMELINE, BUDGET_CONSTRAINTS, PRIMARY_OBJECTIVE, SECONDARY_OBJECTIVES, KEY_QUESTIONS, HYPOTHESES, EXPECTED_OUTCOMES, SOURCE_SYSTEM, COLLECTION_METHOD, TIME_PERIOD, LAST_UPDATE, UPDATE_FREQUENCY, FILE_FORMAT, FILE_SIZE, COMPRESSION_TYPE, NUM_ROWS, NUM_COLUMNS, MEMORY_USAGE, STORAGE_REQUIREMENTS, DATA_LINEAGE, GOVERNANCE_RULES, COMPLETENESS_SCORE, ACCURACY_SCORE, CONSISTENCY_SCORE, TIMELINESS_SCORE, VALIDITY_SCORE, UNIQUENESS_SCORE, TOTAL_COLUMNS, NUM_COLUMNS_COUNT, NUM_PERCENTAGE, CAT_COLUMNS_COUNT, CAT_PERCENTAGE, DATE_COLUMNS_COUNT, DATE_PERCENTAGE, TEXT_COLUMNS_COUNT, TEXT_PERCENTAGE, BOOL_COLUMNS_COUNT, BOOL_PERCENTAGE, MIXED_COLUMNS_COUNT, MIXED_PERCENTAGE, VARIABLE_NAME, COLUMN_NAME, DATA_TYPE, VAR_CLASSIFICATION, MEASUREMENT_LEVEL, BUSINESS_MEANING, DOMAIN_CONSTRAINTS, EXPECTED_RANGE, UNITS, TOTAL_COUNT, NON_NULL_COUNT, NULL_COUNT, NULL_PERCENTAGE, ZERO_COUNT, ZERO_PERCENTAGE, BLANK_COUNT, INVALID_COUNT, NUM_VAR, MEAN_VALUE, MEDIAN_VALUE, MODE_VALUE, TRIMMED_MEAN_5, TRIMMED_MEAN_10, GEOMETRIC_MEAN, HARMONIC_MEAN, STD_DEV, VARIANCE, RANGE, IQR, MAD, CV, RSD, SKEWNESS, KURTOSIS, EXCESS_KURTOSIS, DISTRIBUTION_TYPE, NORMALITY_ASSESSMENT, MIN_VALUE, P01, P05, P10, Q1, Q2, Q3, P90, P95, P99, MAX_VALUE, SHAPIRO_W, SHAPIRO_P, KS_D, KS_P, AD_A2, AD_P, JB_STAT, JB_P, DP_K2, DP_P, BEST_FIT_DIST, DIST_PARAMS, AIC_SCORE, BIC_SCORE, FIT_KS_P, IQR_LOWER, IQR_UPPER, IQR_OUTLIERS_COUNT, IQR_OUTLIER_PERCENT, IQR_EXTREME, Z2_OUTLIERS, Z3_OUTLIERS, MAX_ZSCORE, Z_OUTLIER_INDICES, MOD_Z_OUTLIERS, MAD_VALUE, IF_CONTAMINATION, IF_ANOMALIES, IF_SCORES, LOF_THRESHOLD, LOF_OUTLIERS, AVG_LOF, RULE_VIOLATIONS, CONSISTENCY_ISSUES, EXPERT_FLAGS, CAT_VAR, UNIQUE_COUNT, CARDINALITY_RATIO, EFFECTIVE_CARDINALITY, HIGH_CARDINALITY_FLAG, VALUE_1, COUNT_1, PERCENT_1, VALUE_2, COUNT_2, PERCENT_2, VALUE_3, COUNT_3, PERCENT_3, VALUE_4, COUNT_4, PERCENT_4, VALUE_5, COUNT_5, PERCENT_5, MODE_CAT, MODE_FREQ, MODE_PERCENT, SECOND_MODE, SECOND_MODE_FREQ, ENTROPY, GINI_IMPURITY, SIMPSON_DIVERSITY, SHANNON_DIVERSITY, EVENNESS_INDEX, RARE_1_PERCENT, RARE_5_PERCENT, SINGLETON_COUNT, PARETO_80_CATEGORIES, LONG_TAIL_CATEGORIES, START_DATETIME, END_DATETIME, TOTAL_DURATION, DAYS_SPAN, TIME_GRANULARITY, EXPECTED_FREQUENCY, ACTUAL_FREQUENCY, MISSING_PERIODS, GAP_COUNT, AVG_GAP_DURATION, LONGEST_GAP, GAP_PATTERN, RECORDS_PER_DAY, RECORDS_PER_WEEK, RECORDS_PER_MONTH, RECORDS_PER_QUARTER, RECORDS_PER_YEAR, TREND_COMPONENT, SEASONAL_COMPONENT, RESIDUAL_COMPONENT, SEASONAL_STRENGTH, TREND_STRENGTH, WEEKLY_SEASONALITY, MONTHLY_SEASONALITY, QUARTERLY_SEASONALITY, ANNUAL_SEASONALITY, HOLIDAY_EFFECTS, ADF_STATISTIC, ADF_PVALUE, KPSS_STATISTIC, KPSS_PVALUE, PP_STATISTIC, PP_PVALUE, ACF_LAG1, PACF_LAG1, PEARSON_CORRELATION_MATRIX, VAR_A1, VAR_B1, CORR_1, P_1, VAR_A2, VAR_B2, CORR_2, P_2, VAR_A3, VAR_B3, CORR_3, P_3, VAR_A4, VAR_B4, CORR_4, P_4, VAR_A5, VAR_B5, CORR_5, P_5, VAR_C1, VAR_D1, NEG_CORR_1, NEG_P_1, VAR_C2, VAR_D2, NEG_CORR_2, NEG_P_2, VAR_C3, VAR_D3, NEG_CORR_3, NEG_P_3, SPEARMAN_CORRELATION_MATRIX, KENDALL_CORRELATION_MATRIX, DISTANCE_CORR_MATRIX, MIC_MATRIX, CAT_VAR_1, CAT_VAR_2, CHI2_1, DF_1, P_CHI_1, CAT_VAR_3, CAT_VAR_4, CHI2_2, DF_2, P_CHI_2, CAT_VAR_5, CAT_VAR_6, CHI2_3, DF_3, P_CHI_3, CRAMER_1, CRAMER_2, CRAMER_3, BINARY_VAR_1, BINARY_VAR_2, PHI_1, BINARY_VAR_3, BINARY_VAR_4, PHI_2, NUM_VAR_1, BINARY_VAR_1, PB_CORR_1, NUM_VAR_2, BINARY_VAR_2, PB_CORR_2, CAT_VAR_1, F_STAT_1, P_ANOVA_1, ETA_SQ_1, CAT_VAR_2, F_STAT_2, P_ANOVA_2, ETA_SQ_2, PCA_90_COMPONENTS, PCA_95_COMPONENTS, PCA_99_COMPONENTS, PC1_VARIANCE, PC2_VARIANCE, PC3_VARIANCE, CUMVAR_5PC, NUM_FACTORS, FACTOR_LOADINGS, COMMUNALITIES, KMO_SCORE, BARTLETT_CHI2, BARTLETT_P, ICA_COMPONENTS, MIXING_CONDITION, SOURCE_QUALITY, TSNE_PERPLEXITY, CLUSTER_SEPARATION, EMBEDDING_STRESS, UMAP_NEIGHBORS, UMAP_MIN_DIST, LOCAL_CONNECTIVITY, GLOBAL_STRUCTURE, HOPKINS_STATISTIC, CLUSTERING_TENDENCY, RANDOM_LIKELIHOOD, VAR_VIF_1, VIF_1, VAR_VIF_2, VIF_2, VAR_VIF_3, VIF_3, VAR_VIF_4, VIF_4, VAR_VIF_5, VIF_5, HIGH_VIF_VARS, VERY_HIGH_VIF_VARS, CONDITION_INDEX, EIGENVALUE_ANALYSIS, COMPLETE_CASES, COMPLETE_PERCENT, ANY_MISSING, ANY_MISSING_PERCENT, VARS_WITH_MISSING, LITTLE_CHI2, LITTLE_P, MAR_ASSESSMENT, MNAR_INDICATORS, PATTERN_1, PATTERN_1_COUNT, PATTERN_2, PATTERN_2_COUNT, PATTERN_3, PATTERN_3_COUNT, MEAN_IMP_BIAS, MEDIAN_IMP_BIAS, MODE_IMP_BIAS, ADVANCED_IMP_OPTIONS, EXACT_DUPES, EXACT_DUPE_PERCENT, DUPE_PATTERNS, SIMILARITY_THRESHOLD, NEAR_DUPE_PAIRS, FUZZY_MATCHES, PK_CANDIDATES, COMPOSITE_KEYS, UNIQUENESS_VIOLATIONS, LOGIC_RULES, RULE_VIOLATIONS_COUNT, CONSISTENCY_SCORE, DATE_FORMAT_ISSUES, NUMERIC_FORMAT_ISSUES, ENCODING_ISSUES, CASE_ISSUES, FK_VIOLATIONS, ORPHANED_RECORDS, REF_CONSISTENCY, VAR_NAME, NORMAL_KS, NORMAL_P, EXP_KS, EXP_P, UNIFORM_KS, UNIFORM_P, LOGNORM_KS, LOGNORM_P, GAMMA_KS, GAMMA_P, MAD_ROBUST, IQR_ROBUST, TRIMMED_MEAN_10, WINSORIZED_STATS, HUBER_ESTIMATOR, BOOTSTRAP_SAMPLES, CI_95_LOWER, CI_95_UPPER, BOOTSTRAP_BIAS, BOOTSTRAP_SE, T_STAT, T_P, MW_U, MW_P, KS2_D, KS2_P, CHI2_INDEP, CHI2_INDEP_P, BONFERRONI_ALPHA, HOLM_ALPHA, FDR_ALPHA, TUKEY_HSD_RESULTS, KMEANS_OPTIMAL_K, SILHOUETTE_OPTIMAL_K, KMEANS_INERTIA, SILHOUETTE_SCORE, CLUSTER_1_SIZE, CLUSTER_1_PROFILE, CLUSTER_1_CENTROID, CLUSTER_1_VARIANCE, CLUSTER_2_SIZE, CLUSTER_2_PROFILE, CLUSTER_2_CENTROID, CLUSTER_2_VARIANCE, LINKAGE_METHOD, DISTANCE_METRIC, DENDROGRAM_INSIGHTS, COPHENETIC_CORR, DBSCAN_EPS, DBSCAN_MIN_SAMPLES, DBSCAN_CLUSTERS, DBSCAN_NOISE, FREQUENT_ITEMSETS, SUPPORT_THRESHOLD, CONFIDENCE_THRESHOLD, LIFT_ANALYSIS, PATTERN_ALGORITHM, DISCOVERED_SEQUENCES, PATTERN_CONFIDENCE, VAR_HIST_1, HIST_SHAPE_1, HIST_MODALITY_1, OPTIMAL_BINS_1, OUTLIER_VISIBILITY_1, VAR_HIST_2, HIST_SHAPE_2, HIST_MODALITY_2, OPTIMAL_BINS_2, OUTLIER_VISIBILITY_2, VAR_BOX_1, MEDIAN_POSITION_1, IQR_SYMMETRY_1, WHISKER_LENGTH_1, BOX_OUTLIER_COUNT_1, VAR_BOX_2, MEDIAN_POSITION_2, IQR_SYMMETRY_2, WHISKER_LENGTH_2, BOX_OUTLIER_COUNT_2, KDE_BANDWIDTH, DISTRIBUTION_WIDTH, MULTIMODAL_INDICATORS, VAR_X_1, VAR_Y_1, RELATIONSHIP_TYPE_1, VISUAL_CORR_1, SCATTER_OUTLIERS_1, SCATTER_CLUSTERS_1, VAR_X_2, VAR_Y_2, RELATIONSHIP_TYPE_2, VISUAL_CORR_2, SCATTER_OUTLIERS_2, SCATTER_CLUSTERS_2, POS_CORR_BLOCKS, NEG_CORR_BLOCKS, CORR_CLUSTERS, MISSING_PATTERNS_VISUAL, SYSTEMATIC_MISSING, RANDOM_MISSING, VISUAL_TREND, VISUAL_SEASONALITY, VISUAL_ANOMALIES, VOLATILITY_PERIODS, DAILY_PATTERNS, WEEKLY_PATTERNS, MONTHLY_PATTERNS, HOLIDAY_EFFECTS_VISUAL, TARGET_VARIABLE, TARGET_TYPE, TARGET_DISTRIBUTION, CLASS_BALANCE, NUM_CLASSES, MAJORITY_CLASS, MAJORITY_PERCENT, MINORITY_CLASS, MINORITY_PERCENT, IMBALANCE_RATIO, CLASS_DISTRIBUTION, TARGET_RANGE, TARGET_MEAN, TARGET_MEDIAN, TARGET_STD, TARGET_SKEWNESS, PRED_FEATURE_1, ASSOCIATION_1, PRED_FEATURE_2, ASSOCIATION_2, PRED_FEATURE_3, ASSOCIATION_3, PRED_FEATURE_4, ASSOCIATION_4, PRED_FEATURE_5, ASSOCIATION_5, MI_FEATURE_1, MI_SCORE_1, MI_FEATURE_2, MI_SCORE_2, MI_FEATURE_3, MI_SCORE_3, IV_FEATURE_1, IV_SCORE_1, IV_FEATURE_2, IV_SCORE_2, IV_FEATURE_3, IV_SCORE_3, BUSINESS_SEGMENTS, SEGMENT_CHARACTERISTICS, SEGMENT_VALUE, USAGE_PATTERNS, ENGAGEMENT_METRICS, CHURN_INDICATORS, PROCESS_BOTTLENECKS, EFFICIENCY_OPPORTUNITIES, COST_DRIVERS, HIGH_VALUE_FEATURES, REVENUE_CORRELATION, MONETIZATION_OPPS, DQ_RISKS, PRIVACY_CONCERNS, COMPLIANCE_ISSUES, BIAS_INDICATORS, SAMPLE_BIAS, TEMPORAL_RELEVANCE, EXTERNAL_VALIDITY, CONFOUNDING_FACTORS, DROP_VARIABLES, IMPUTATION_METHODS, MISSING_INDICATORS, OUTLIER_REMOVAL_VARS, TRANSFORM_VARS, WINSORIZE_VARS, CREATE_FEATURES, INTERACTION_TERMS, POLYNOMIAL_FEATURES, BINNING_RECOMMENDATIONS, LOG_TRANSFORM_VARS, SCALING_VARS, ENCODING_STRATEGIES, NORMALIZATION_VARS, RECOMMENDED_ALGORITHMS, AVOID_ALGORITHMS, ENSEMBLE_OPPORTUNITIES, CV_APPROACH, DATA_SPLIT_STRATEGY, TEMPORAL_VALIDATION, FEATURE_SELECTION_METHODS, DIMENSIONALITY_REDUCTION, FEATURE_IMPORTANCE_FOCUS, INVESTIGATE_VARS, EXPLORE_RELATIONSHIPS, UNDERSTAND_ANOMALIES, EXTERNAL_DATA_SOURCES, MISSING_VARIABLES, TEMPORAL_DATA_NEEDS, STATISTICAL_TESTS, BUSINESS_HYPOTHESES, AB_TEST_OPPORTUNITIES, IMMEDIATE_ACTIONS, SHORT_TERM_PRIORITIES, LONG_TERM_PLAN, STAKEHOLDER_COMMUNICATION, GOVERNANCE_IMPROVEMENTS]

## Usage Examples

### Example 1: Customer Churn Dataset EDA
```
DATASET_NAME: "Telecommunications Customer Churn Data"
NUM_ROWS: "7,043 customers"
ANALYSIS_OBJECTIVE: "Identify factors contributing to customer churn for retention strategy"
BUSINESS_CONTEXT: "Telecom company experiencing 26.5% annual churn rate"
KEY_FINDING: "Customers with month-to-month contracts have 42% churn vs 11% for two-year contracts"
CORRELATION_INSIGHT: "Monthly charges and total charges highly correlated (r=0.65) but differ in churn impact"
CLASS_BALANCE: "26.5% churned, 73.5% retained"
TOP_PREDICTOR: "Contract type has highest predictive power (IV=1.44)"
```

### Example 2: E-commerce Sales Transaction EDA
```
DATASET_NAME: "Online Retail Transaction Data"
TIME_PERIOD: "January 2023 - December 2023"
BUSINESS_CONTEXT: "E-commerce platform analyzing sales patterns for inventory optimization"
SEASONALITY_FINDING: "Strong weekly pattern with 40% higher sales on weekends"
OUTLIER_PATTERN: "Black Friday sales 15x normal daily volume, Valentine's Day 8x"
SEGMENT_INSIGHT: "Premium customers (3% of base) generate 28% of revenue"
MISSING_PATTERN: "Customer IDs missing for 12% of transactions (guest checkouts)"
TEMPORAL_ANOMALY: "Website downtime on March 15th created data gap"
```

### Example 3: Manufacturing IoT Sensor Data
```
DATASET_NAME: "Production Line Sensor Measurements"
GRANULARITY: "Temperature, pressure, vibration readings every 5 seconds"
BUSINESS_CONTEXT: "Smart factory optimizing production quality and equipment maintenance"
ANOMALY_DETECTION: "Temperature spikes >85°C correlate with 67% of quality defects"
MISSING_PATTERN: "Systematic data gaps during shift changes (6am, 2pm, 10pm)"
MULTIVARIATE_FINDING: "3 principal components explain 89% of sensor variance"
SEASONALITY_DISCOVERY: "Equipment performance degrades 15% during summer months"
CORRELATION_INSIGHT: "Vibration and product defect rate correlation increases over equipment age"
```

### Example 4: Healthcare Patient Records EDA
```
DATASET_NAME: "Patient Electronic Health Records"
BUSINESS_CONTEXT: "Hospital system analyzing readmission risk factors"
PRIVACY_CONSIDERATION: "PHI anonymized, geographic data aggregated to ZIP+4 level"
MISSING_PATTERN: "Lab values missing for 23% of emergency admissions"
OUTLIER_FINDING: "Length of stay >30 days represents 2% of cases but 18% of costs"
DEMOGRAPHIC_INSIGHT: "Readmission rate varies from 8.2% to 24.7% across demographic segments"
TEMPORAL_PATTERN: "Readmissions peak on Mondays (22% higher than average)"
COMORBIDITY_ANALYSIS: "Patients with 3+ chronic conditions have 3.4x readmission risk"
```

## Customization Options

1. **Analysis Depth**
   - Quick data profiling (1-2 hours)
   - Standard comprehensive EDA (1-2 days)  
   - Deep statistical analysis (3-5 days)
   - Advanced multivariate exploration (1-2 weeks)
   - Longitudinal pattern analysis (2-4 weeks)

2. **Data Types & Sources**
   - Structured tabular data
   - Time series datasets
   - Mixed structured/unstructured
   - Streaming data analysis
   - Multi-source data integration
   - Big data platforms (Spark, Hadoop)

3. **Industry Specialization**
   - Financial services (risk, fraud, credit)
   - Healthcare (clinical, claims, outcomes)
   - Retail/E-commerce (transactions, behavior)
   - Manufacturing (IoT, quality, maintenance)
   - Technology (user behavior, performance)
   - Government (census, surveys, compliance)

4. **Analytical Focus**
   - Statistical summary emphasis
   - Visual exploration priority
   - Data quality assessment focus
   - Pattern and anomaly discovery
   - Predictive modeling preparation
   - Business insight generation

5. **Technical Environment**
   - Python ecosystem (Pandas, NumPy, SciPy)
   - R statistical environment
   - SQL-based analysis
   - Cloud platforms (AWS, GCP, Azure)
   - Big data frameworks
   - Specialized tools (SAS, SPSS, Tableau)

6. **Output Formats**
   - Executive dashboard
   - Technical deep-dive report
   - Interactive Jupyter notebooks
   - PowerPoint presentation
   - PDF statistical report
   - Web-based visualization portal

7. **Compliance & Privacy**
   - GDPR compliance requirements
   - HIPAA healthcare data
   - Financial regulations (SOX, Basel)
   - Data anonymization needs
   - Audit trail requirements
   - Ethical AI considerations
```