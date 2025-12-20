---
category: data-analytics
title: Data Preparation and Feature Engineering for Predictive Models
tags:
- data-preparation
- feature-engineering
- data-quality
- machine-learning
use_cases:
- Preparing raw data for machine learning model development
- Engineering predictive features from domain knowledge and data
- Handling missing values, outliers, and data quality issues
- Preventing data leakage and ensuring valid train-test splits
related_templates:
- data-analytics/Data-Science/predictive-modeling.md
- data-analytics/Analytics-Engineering/pipeline-transformation.md
- data-analytics/Analytics-Engineering/analytics-data-quality.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: predictive-modeling-framework-01-data-preparation
---

# Data Preparation and Feature Engineering for Predictive Models

## Purpose
Design comprehensive data preparation and feature engineering strategies for predictive modeling projects. This framework covers data quality assessment, missing value treatment, feature creation, encoding strategies, and validation approaches to transform raw data into model-ready datasets while preventing leakage and maintaining reproducibility.

## Template

Design data preparation and feature engineering for {PREDICTION_OBJECTIVE} using {DATA_CHARACTERISTICS} with target of {MODEL_REQUIREMENTS}.

**DATA QUALITY ASSESSMENT AND REMEDIATION**

Evaluate data completeness analyzing missing value patterns to distinguish between missing completely at random where absence is independent of any variables, missing at random where missingness depends on observed data, and missing not at random where absence relates to the unobserved value itself. For MCAR scenarios, consider simple deletion if missingness is below five percent, otherwise implement mean or median imputation for numeric variables. For MAR patterns, use conditional imputation based on observed features or model-based approaches like KNN imputation. For MNAR situations, consider creating missing indicator features that may themselves be predictive rather than attempting to impute values.

Identify outliers through statistical methods including z-score analysis flagging values beyond three standard deviations, interquartile range detection identifying points below Q1 minus 1.5 IQR or above Q3 plus 1.5 IQR, and domain-specific thresholds based on business logic. Determine outlier treatment based on whether extreme values represent data errors requiring correction or removal, rare but legitimate observations requiring special handling, or influential points needing robust modeling techniques. Consider winsorization capping values at percentile thresholds rather than removal when preserving sample size is critical.

Assess data accuracy by validating against known constraints including range checks for bounded variables, referential integrity for related records, and business rule compliance. Implement automated quality checks flagging records with impossible combinations, temporal inconsistencies, or statistical anomalies. Document data quality issues systematically tracking prevalence, impact on target variable distribution, and remediation decisions for reproducibility and audit trails.

**FEATURE ENGINEERING STRATEGIES**

Create temporal features for time-series or dated data extracting components including year, quarter, month, week, day of week, day of month, hour, and minute enabling models to capture seasonality and cyclical patterns. Construct lag features shifting target and predictor variables by relevant time periods based on domain knowledge of influence timing. Calculate rolling statistics including moving averages, exponential smoothing, and rolling standard deviations over windows matching business cycles. Decompose time series into trend, seasonal, and residual components treating each as separate features.

Design interaction features multiplying or dividing related variables to capture synergistic effects the model might not learn independently. For example, create price-per-unit from total price and quantity, or credit-utilization from balance and limit. Construct ratio and proportion features encoding relationships more meaningfully than raw values. Engineer polynomial features cautiously as they increase dimensionality rapidly and risk overfitting without careful regularization.

Generate domain-specific features applying business knowledge to create predictive signals. For customer analytics, calculate RFM scores from recency, frequency, and monetary values. For credit modeling, derive debt-to-income ratios and payment-to-balance trends. For operational metrics, compute efficiency ratios and capacity utilization rates. Collaborate with domain experts to identify leading indicators and causal relationships not obvious from statistical analysis alone.

Implement automated feature generation techniques for exploratory analysis including polynomial combinations up to degree two or three, mathematical transformations like logarithmic and square root, and statistical aggregations across grouping variables. Use feature selection methods afterward to identify valuable derived features while discarding noise. Consider genetic algorithms or reinforcement learning approaches for complex feature spaces where manual engineering is intractable.

**ENCODING AND TRANSFORMATION**

Encode categorical variables selecting methods based on cardinality and relationship to target. For low-cardinality nominal categories with five to ten distinct values, use one-hot encoding creating binary indicator columns. For ordinal categories with inherent ordering like satisfaction ratings, use label encoding preserving ordinality. For high-cardinality categories exceeding twenty values, consider target encoding replacing categories with the mean target value for that category calculated on training data only to prevent leakage, or frequency encoding representing categories by their occurrence counts.

Handle rare categories consolidating infrequent values appearing in less than one percent of records into an "Other" category, preventing overfitting to noise and reducing dimensionality. For tree-based models that handle categories natively, consider leaving raw categories for the algorithm to optimize splits. For neural networks or distance-based algorithms requiring numeric inputs, use embedding layers learning distributed representations for high-cardinality categorical features.

Transform skewed numeric distributions to approximate normality when using algorithms sensitive to feature scales like linear models, neural networks, or distance-based methods. Apply log transformation for right-skewed distributions common in counts and monetary values. Use Box-Cox or Yeo-Johnson power transformations automatically optimizing the transformation parameter. Implement quantile transformation mapping features to uniform or normal distributions especially useful for features with outliers or multimodal distributions.

Scale numeric features using standardization subtracting mean and dividing by standard deviation when features have different units or vastly different scales. Use min-max normalization scaling to zero-one range when preserving zero values and bounded ranges matters. Apply robust scaling using median and interquartile range when data contains outliers that would distort mean and standard deviation. Note tree-based algorithms like random forests and gradient boosting are scale-invariant and do not require feature scaling.

**VALIDATION STRATEGY AND LEAKAGE PREVENTION**

Design train-test splits based on data structure and prediction scenario. For time-series forecasting, use temporal splits training on historical data and validating on future periods respecting temporal ordering and preventing look-ahead bias. Leave gaps between train and test sets matching the prediction horizon ensuring models are evaluated on realistic future data unavailability. For cross-sectional data without temporal dependencies, use stratified random sampling ensuring train and test sets have similar target variable distributions especially critical for imbalanced classification.

Implement cross-validation appropriate to data characteristics using k-fold with stratification for standard classification, time-series cross-validation with expanding or rolling windows for temporal data, and group-based cross-validation ensuring related records like multiple purchases by the same customer are not split across folds preventing information leakage through group patterns.

Prevent temporal leakage by ensuring all feature engineering, imputation, and scaling parameters are calculated on training data only and applied to validation and test sets. Create preprocessing pipelines that fit on train data and transform test data using those fitted parameters. Avoid features containing future information not available at prediction time including calculations requiring future data, aggregations computed on full datasets instead of point-in-time snapshots, and targets or target-derived features inadvertently included as predictors.

Detect leakage by monitoring for suspiciously perfect predictors showing near-zero training error and unrealistic validation performance, features with correlation to target above 0.95 unless causally justified, and validation performance significantly exceeding realistic expectations based on domain knowledge. Conduct out-of-time validation testing models on data from time periods not used in development to verify temporal generalization.

**DOCUMENTATION AND REPRODUCIBILITY**

Document feature definitions providing clear descriptions of calculation logic, data sources, assumptions, and business justification for each engineered feature. Maintain data dictionaries cataloging all variables with types, valid ranges, and example values. Record preprocessing decisions including imputation methods, outlier treatments, encoding strategies, and transformations applied.

Implement version control for feature engineering code ensuring reproducibility as data sources and business logic evolve. Use configuration files or feature stores to manage feature definitions centrally enabling consistent feature generation across training, validation, and production. Track data snapshots and processing timestamps preventing train-test contamination from different extraction times.

Establish data lineage tracking feature derivation from raw sources through transformations to model inputs. Document dependencies between features enabling impact analysis when source data changes. Maintain audit trails for data quality remediation decisions supporting model governance and regulatory compliance.

Deliver preparation design as:

1. **DATA QUALITY REPORT** - Completeness, accuracy, outlier summary, and remediation plan

2. **FEATURE CATALOG** - All engineered features with definitions, rationale, and example calculations

3. **ENCODING SPECIFICATION** - Categorical and numeric transformation methods with parameters

4. **VALIDATION STRATEGY** - Train-test split approach, cross-validation method, and leakage prevention controls

5. **PREPROCESSING PIPELINE** - Ordered transformation steps with code or pseudocode

6. **DATA DICTIONARY** - Complete variable catalog with types, distributions, and business definitions

---

## Usage Examples

### Example 1: Customer Churn Prediction
**Prompt:** Design data preparation pipeline for customer churn prediction using transaction history, account details, and support interactions with target of binary classification model achieving 80% recall on monthly churn.

**Expected Output:** Data quality report identifying 12% missing last-interaction dates imputed via forward-fill, outlier analysis capping account ages at 99th percentile. Feature catalog including RFM scores from transaction recency/frequency/monetary, support ticket velocity as tickets per month, engagement trend as three-month interaction change rate. One-hot encoding for product category, target encoding for high-cardinality customer segment. Temporal split using 18 months for training, most recent 3 months for validation with stratification on churn rate. Standardization for numeric features, no scaling for tree-based models.

### Example 2: Demand Forecasting
**Prompt:** Design data preparation pipeline for retail demand forecasting using sales history, promotions, weather, and holidays with target of daily SKU-store level predictions with MAPE under 15%.

**Expected Output:** Time-series feature engineering including 7-day and 28-day lag sales, rolling 7-day mean and standard deviation, day-of-week and month indicators, holiday flags with lead/lag for before-after effects. Weather integration as temperature bands and precipitation binary. Promotion encoding as discount percentage and promotion type one-hot. Log transformation for right-skewed sales distributions. Time-series cross-validation with expanding window training on cumulative history, validating on next 30 days, 10 folds. Min-max scaling for LSTM input, no scaling for XGBoost baseline.

### Example 3: Credit Risk Scoring
**Prompt:** Design data preparation pipeline for consumer credit risk prediction using credit bureau data, application information, and bank account history with target of default probability estimation meeting fair lending requirements.

**Expected Output:** Feature engineering including debt-to-income ratio, credit utilization across accounts, payment delinquency trends over 12 months, account age diversity, and inquiry rate. Missing income values imputed via regression on credit limits and payment patterns. Outlier capping for extreme debt values at 99th percentile. Target encoding for occupation with smoothing, one-hot for property ownership. Polynomial features for credit score interactions with utilization. Stratified split maintaining default rate distribution. Robust scaling resistant to outliers. Fairness assessment ensuring no protected class leakage, disparate impact testing across demographic groups.

---

## Cross-References

- [Predictive Modeling](../Data-Science/predictive-modeling.md) - Complete modeling workflow and algorithm selection
- [Pipeline Transformation](../Analytics-Engineering/pipeline-transformation.md) - Data transformation patterns and architectures
- [Analytics Data Quality](../Analytics-Engineering/analytics-data-quality.md) - Data quality frameworks and validation rules
- [Exploratory Analysis](../Data-Science/exploratory-analysis.md) - Understanding data distributions before feature engineering
