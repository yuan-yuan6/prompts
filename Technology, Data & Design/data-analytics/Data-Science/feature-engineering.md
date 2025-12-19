---
category: data-analytics
title: Feature Engineering & Selection Framework
tags:
- data-science
- feature-engineering
- feature-selection
- machine-learning
use_cases:
- Creating predictive features from raw data
- Encoding categorical and temporal variables
- Selecting optimal feature sets for modeling
- Building reproducible feature pipelines
related_templates:
- data-analytics/Data-Science/exploratory-analysis.md
- data-analytics/predictive-modeling-framework.md
- data-analytics/Data-Science/experimentation-design.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: feature-engineering
---

# Feature Engineering & Selection Framework

## Purpose
Design and implement feature engineering strategies that transform raw data into predictive signals. This framework covers feature creation, transformation, encoding, selection, and validation to improve model performance while maintaining interpretability and avoiding data leakage.

## 🚀 Quick Start Prompt

> Engineer features for **[ML TASK]** predicting **[TARGET]** from **[DATASET DESCRIPTION]**. Create: (1) **Transformations**—what numeric scaling, binning, or mathematical transforms? (2) **Encodings**—how to handle categoricals (target, one-hot, embedding) and dates (cyclical, lag, rolling)? (3) **Interactions**—what ratios, products, or domain-specific combinations? (4) **Selection**—which features to keep based on importance, correlation, and stability? Deliver: feature engineering pipeline, selected feature set with importance scores, and validation results.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid feature engineering.

---

## Template

Design a feature engineering pipeline for {ML_TASK} predicting {TARGET_VARIABLE} from {RAW_DATA_DESCRIPTION}.

**1. RAW DATA ASSESSMENT**

Understand your starting point:

Feature inventory: Catalog all available columns by type—numeric continuous, numeric discrete, categorical nominal, categorical ordinal, datetime, text, boolean. Note the target variable and any identifiers that shouldn't be features. Count features by type to understand the engineering challenge.

Data quality check: Assess missing rates, outlier prevalence, and value distributions for each feature. Features with >50% missing need special handling or exclusion. Features with near-zero variance provide no signal. Document quality issues that will affect engineering choices.

Leakage assessment: Identify features that might leak target information—features collected after the prediction point, features derived from the target, or proxies that won't be available at prediction time. Leakage creates models that work in training but fail in production.

Domain context: What business meaning does each feature carry? Domain knowledge guides engineering—which features to combine, what transformations make sense, what derived features would be valuable. Work with subject matter experts when possible.

**2. NUMERIC FEATURE ENGINEERING**

Transform continuous variables:

Scaling and normalization: Most algorithms benefit from scaled features. StandardScaler (zero mean, unit variance) works for normally distributed features. MinMaxScaler (0-1 range) preserves zero values. RobustScaler uses median and IQR, handling outliers better. Match scaling to algorithm requirements—tree models don't need it, linear models do.

Mathematical transformations: Log transforms compress right-skewed distributions (income, counts, prices). Square root softens skew less aggressively. Box-Cox and Yeo-Johnson find optimal power transformations automatically. Apply transformations to achieve approximate normality when algorithms assume it.

Binning and discretization: Convert continuous to categorical when relationships are non-linear or interpretability matters. Equal-width bins are simple but sensitive to outliers. Equal-frequency (quantile) bins ensure balanced groups. Custom bins encode domain knowledge (age groups, income brackets). Decision tree binning finds optimal splits automatically.

Outlier handling: Winsorize (cap) at percentiles (1st/99th or 5th/95th) to reduce outlier influence while preserving information. Log transforms naturally compress outlier impact. Create outlier indicator features—the presence of outliers may itself be predictive. Don't blindly remove outliers; understand why they exist.

**3. CATEGORICAL FEATURE ENGINEERING**

Encode discrete variables appropriately:

One-hot encoding: Creates binary columns for each category. Best for low-cardinality (<10 categories) nominal variables. Handles unknown categories poorly. Watch for dummy variable trap in linear models—drop one category or use regularization.

Ordinal encoding: Maps categories to integers preserving order. Use for truly ordinal variables (education level, rating). Don't use for nominal categories—creates false ordering that misleads algorithms. Define the order explicitly based on domain knowledge.

Target encoding: Replaces categories with mean target value for that category. Powerful for high-cardinality categoricals. Must use cross-validation or smoothing to prevent target leakage—never encode using the same rows you'll train on. Add regularization toward global mean for rare categories.

Frequency encoding: Replaces categories with their occurrence count or frequency. Works well when category popularity correlates with the target. Doesn't leak target information. Handles new categories gracefully by assigning low counts.

Binary and hash encoding: Binary encoding represents categories in binary, reducing dimensions for high-cardinality variables. Feature hashing maps categories to fixed-size vectors, handling arbitrary cardinality. Both sacrifice some information for efficiency.

Embedding encoding: Neural network-learned embeddings capture category similarities in dense vectors. Powerful for very high-cardinality features (user IDs, product IDs). Requires sufficient data to learn meaningful representations. Can use pretrained embeddings when available.

**4. TEMPORAL FEATURE ENGINEERING**

Extract signal from datetime variables:

Date component extraction: Extract year, month, day, day of week, hour, minute from timestamps. Different components capture different patterns—month for seasonality, day of week for weekly cycles, hour for daily patterns. Create is_weekend, is_holiday, is_business_hours flags.

Cyclical encoding: Represent cyclical features (hour, day of week, month) with sine and cosine transforms to preserve continuity—hour 23 is close to hour 0, December is close to January. Use sin(2π × value / period) and cos(2π × value / period).

Recency features: Time since last event (days since last purchase, hours since last login). Time until next scheduled event. Age of records. Recency often strongly predicts behavior—recent customers behave differently than dormant ones.

Lag features: Past values of time-varying features—yesterday's sales, last week's traffic, previous month's revenue. Choose lags based on domain knowledge and autocorrelation analysis. Be careful about leakage—lags must be available at prediction time.

Rolling window features: Statistics over recent time windows—rolling mean, sum, std, min, max over last 7 days, 30 days, etc. Capture trends and volatility. Expanding windows for cumulative statistics. Exponentially weighted means for recent-weighted averages.

**5. INTERACTION FEATURES**

Capture relationships between variables:

Arithmetic combinations: Ratios reveal relative relationships (revenue/cost = margin, clicks/impressions = CTR). Differences capture gaps (actual - expected). Products capture joint effects. Sums aggregate related quantities.

Domain-specific features: Encode business logic—RFM scores (recency, frequency, monetary), customer lifetime value, conversion funnels, cohort metrics. These often outperform generic features because they capture meaningful concepts.

Polynomial features: Squared terms capture U-shaped relationships. Interaction terms (A × B) capture effects that depend on both variables. Use sparingly—polynomial expansion creates many features, most uninformative. Let tree models find interactions automatically.

Group aggregations: Statistics of numeric features within categorical groups—average purchase by customer segment, max transaction by merchant, count of events by user. These capture entity-level patterns from transaction-level data.

**6. TEXT FEATURE ENGINEERING**

Extract features from text fields:

Basic text features: Character count, word count, sentence count, average word length. Punctuation patterns, capitalization ratio, numeric content. Simple features often surprisingly predictive.

Bag-of-words and TF-IDF: Convert text to numeric vectors based on word occurrence. TF-IDF weights by inverse document frequency, emphasizing distinctive words. Use n-grams (bigrams, trigrams) to capture phrases. Limit vocabulary size to most frequent/informative terms.

Word embeddings: Dense vector representations (Word2Vec, GloVe, FastText) capture semantic meaning. Average word embeddings for document representation. Use pretrained embeddings for common vocabulary. Fine-tune or train custom embeddings for domain-specific text.

Transformer embeddings: BERT, sentence-transformers provide contextualized embeddings capturing nuanced meaning. More powerful but more expensive. Use for high-value text classification or when semantic understanding matters.

**7. FEATURE SELECTION**

Choose the optimal feature set:

Filter methods: Fast, model-agnostic screening. Variance threshold removes near-constant features. Correlation with target identifies univariate predictors. Mutual information captures non-linear relationships. Chi-square for categorical features. Use for initial reduction from thousands to hundreds.

Wrapper methods: Use model performance to evaluate feature subsets. Forward selection adds features iteratively. Backward elimination removes features iteratively. Recursive feature elimination (RFE) combines with model importance. More expensive but finds better sets.

Embedded methods: Feature selection built into model training. LASSO (L1 regularization) drives coefficients to zero. Tree-based importance from Random Forest or XGBoost. These balance performance and selection in one step.

Stability selection: Run selection multiple times on data subsamples. Features consistently selected are truly important. Reduces selection variance and improves generalization. Use with any base selector.

Correlation filtering: Remove highly correlated features (|r| > 0.8-0.9)—they provide redundant information. Keep the one with higher target correlation or better interpretability. Multicollinearity hurts linear models; tree models are more robust.

**8. VALIDATION AND TESTING**

Ensure features work properly:

Leakage detection: Test feature importance before and after shuffling the target. Features that lose importance after shuffling are valid. Features maintaining high importance may leak. Check temporal ordering—features must be available before prediction time.

Stability testing: Do features maintain predictive power across time periods? Across data subsets? Features that work only in certain conditions may not generalize. Test on multiple holdout periods.

Importance analysis: Compare feature importance across different models. Features important across models are robust. Features important only in one model may be fitting noise. SHAP values provide consistent importance across model types.

Performance impact: Measure model performance with and without feature groups. Quantify the lift from engineering effort. Focus resources on high-impact features. Sometimes raw features outperform engineered ones—test, don't assume.

**9. PIPELINE IMPLEMENTATION**

Build reproducible feature pipelines:

Pipeline architecture: Use sklearn Pipeline or similar to chain preprocessing, engineering, and selection. Fit on training data only, transform both training and test. This prevents leakage and ensures consistency between training and serving.

Feature store integration: For production systems, store computed features in a feature store. Enable feature reuse across models. Track feature lineage and versions. Serve features consistently for training and inference.

Monitoring and drift: Track feature distributions in production. Detect when input distributions shift (data drift). Monitor feature importance stability over time. Trigger retraining when drift exceeds thresholds.

Documentation: Document each feature—definition, formula, dependencies, expected range, business meaning. Future maintainers (including yourself) will thank you. Good documentation enables feature reuse.

Deliver your feature engineering solution as:

1. **RAW DATA PROFILE** - Feature inventory, types, quality issues, leakage risks

2. **ENGINEERING PLAN** - Transformations, encodings, and interactions by feature type

3. **SELECTED FEATURE SET** - Final features with importance scores, stability metrics

4. **PIPELINE SPECIFICATION** - Processing steps, fit/transform logic, dependencies

5. **VALIDATION RESULTS** - Leakage tests, stability analysis, performance impact

6. **DOCUMENTATION** - Feature definitions, formulas, business meaning

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{ML_TASK}` | Prediction task type | "Customer churn classification", "Revenue regression", "Fraud detection" |
| `{TARGET_VARIABLE}` | What you're predicting | "30-day churn probability", "Next month revenue", "Fraudulent transaction flag" |
| `{RAW_DATA_DESCRIPTION}` | Input data characteristics | "100K customers with 50 features (demographics, transactions, engagement)" |

## Usage Examples

### Example 1: Customer Churn Prediction

```
Design a feature engineering pipeline for Customer Churn Classification 
predicting 30-day churn probability from 100K customers with 50 raw 
features (demographics, 2 years of transactions, engagement metrics).
```

**Expected Output:**
- Raw: 50 features (15 numeric, 20 categorical, 10 dates, 5 text)
- Numeric: Log-transform spend amounts, scale tenure, bin age into life stages
- Categorical: Target encode product categories, one-hot encode region
- Temporal: Recency (days since last purchase), frequency (monthly transaction counts), rolling 30/60/90 day aggregates
- Interactions: RFM score, spend velocity (recent vs historical), engagement trend
- Selection: 35 features selected via XGBoost importance + stability filtering
- Result: AUC improved from 0.72 (raw) to 0.86 (engineered)

### Example 2: Real Estate Price Prediction

```
Design a feature engineering pipeline for House Price Regression 
predicting sale price from 20K properties with 80 raw features 
(property attributes, location, market conditions).
```

**Expected Output:**
- Raw: 80 features (40 numeric, 35 categorical, 5 dates)
- Numeric: Log-transform price and square footage, create price-per-sqft ratios
- Categorical: Target encode neighborhood (high cardinality), ordinal encode quality ratings
- Location: Distance to amenities, school district scores, crime rates, walkability
- Interactions: Bed/bath ratio, age × condition, location × property type
- Selection: 45 features via LASSO + correlation filtering
- Result: RMSE reduced 23%, R² improved from 0.78 to 0.89

### Example 3: Fraud Detection

```
Design a feature engineering pipeline for Transaction Fraud Detection 
predicting fraud probability from 10M transactions with 30 raw features 
(transaction details, merchant info, user history).
```

**Expected Output:**
- Raw: 30 features (12 numeric, 15 categorical, 3 timestamps)
- Numeric: Log-transform amounts, z-score within user history
- Categorical: Frequency encode merchant categories, binary encode high-risk flags
- Temporal: Time since last transaction, hour-of-day cyclical encoding, velocity features (transactions per hour)
- Aggregations: User-level stats (avg amount, typical merchants, usual hours), merchant-level anomaly scores
- Interactions: Amount deviation from user average, merchant risk × transaction size
- Selection: 40 features via permutation importance + stability selection
- Result: Precision at 1% FPR improved from 45% to 72%

## Cross-References

- **Exploratory Analysis:** exploratory-analysis.md - Understand data before engineering features
- **Predictive Modeling:** predictive-modeling-framework.md - Use features in model building
- **Experimentation:** experimentation-design.md - Test feature impact rigorously
- **Data Quality:** data-governance-framework.md - Ensure feature data quality
