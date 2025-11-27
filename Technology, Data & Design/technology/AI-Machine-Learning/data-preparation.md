---
category: technology
last_updated: 2025-11-23
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- machine-learning
- data-preparation
- feature-engineering
- data-labeling
title: Data Preparation Template
use_cases:
- Creating comprehensive data preparation for machine learning including feature engineering,
  data labeling, augmentation, preprocessing, and quality assurance for robust model
  training.
- Project planning and execution
- Strategy development
industries:
- manufacturing
- retail
- technology
type: template
difficulty: intermediate
slug: data-preparation
---

# Data Preparation Template

## Purpose
Comprehensive data preparation for machine learning including feature engineering, data labeling, augmentation, preprocessing, and quality assurance for robust model training.

## Quick Data Prep Prompt
Prepare ML dataset with [X rows], [Y features] for [model type]. Steps: handle missing values ([strategy]), remove duplicates, fix outliers. Engineer features: encode categoricals ([one-hot/label]), scale numericals ([standard/minmax]), create [domain-specific features]. Split: [70/15/15] train/val/test. Apply augmentation for [imbalanced classes/small dataset]. Validate: no leakage, distribution alignment. Document transformations.

## Quick Start

**Prepare ML data in 5 steps:**

1. **Collect & Clean Data**: Gather raw data from sources, handle missing values, remove duplicates, fix data types and outliers
2. **Perform EDA**: Analyze distributions, correlations, class balance; visualize patterns; identify data quality issues
3. **Engineer Features**: Create new features, encode categoricals (one-hot/label), scale numericals (standard/min-max), select top features
4. **Split & Augment**: Create train/val/test splits (70/15/15), apply augmentation to training data (rotation, noise, SMOTE)
5. **Validate Quality**: Check for data leakage, verify distributions match, ensure no test contamination, document transformations

**Quick Data Preparation Pipeline:**
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load and clean
df = pd.read_csv('data.csv')
df = df.dropna().drop_duplicates()

# Feature engineering
df['new_feature'] = df['col1'] / df['col2']
df = pd.get_dummies(df, columns=['category'])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df.drop('target', axis=1), df['target'], test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

## Template Structure

### Data Overview
- **Dataset Name**: [DATASET_NAME]
- **Data Source**: [DATA_SOURCE]
- **Data Type**: [DATA_TYPE]
- **Data Size**: [DATA_SIZE]
- **Domain**: [DATA_DOMAIN]
- **Quality Level**: [QUALITY_LEVEL]
- **Collection Method**: [COLLECTION_METHOD]
- **Update Frequency**: [UPDATE_FREQUENCY]
- **Privacy Level**: [PRIVACY_LEVEL]
- **Compliance Requirements**: [COMPLIANCE_REQUIREMENTS]

### Data Collection
- **Collection Strategy**: [COLLECTION_STRATEGY]
- **Data Sources**: [DATA_SOURCES]
- **Acquisition Methods**: [ACQUISITION_METHODS]
- **Sampling Strategy**: [SAMPLING_STRATEGY]
- **Collection Tools**: [COLLECTION_TOOLS]
- **Quality Control**: [COLLECTION_QUALITY_CONTROL]
- **Validation Rules**: [VALIDATION_RULES]
- **Error Handling**: [COLLECTION_ERROR_HANDLING]
- **Storage Format**: [STORAGE_FORMAT]
- **Metadata Capture**: [METADATA_CAPTURE]

### Feature Engineering
- **Feature Types**: [FEATURE_TYPES]
- **Feature Creation**: [FEATURE_CREATION]
- **Feature Selection**: [FEATURE_SELECTION]
- **Feature Transformation**: [FEATURE_TRANSFORMATION]
- **Encoding Methods**: [ENCODING_METHODS]
- **Scaling Techniques**: [SCALING_TECHNIQUES]
- **Dimensionality Reduction**: [DIMENSIONALITY_REDUCTION]
- **Feature Interaction**: [FEATURE_INTERACTION]
- **Temporal Features**: [TEMPORAL_FEATURES]
- **Domain Features**: [DOMAIN_FEATURES]

### Data Labeling
- **Labeling Strategy**: [LABELING_STRATEGY]
- **Annotation Guidelines**: [ANNOTATION_GUIDELINES]
- **Labeling Tools**: [LABELING_TOOLS]
- **Quality Assurance**: [LABELING_QA]
- **Inter-annotator Agreement**: [INTER_ANNOTATOR_AGREEMENT]
- **Active Learning**: [ACTIVE_LEARNING]
- **Semi-supervised Learning**: [SEMI_SUPERVISED_LEARNING]
- **Weak Supervision**: [WEAK_SUPERVISION]
- **Label Noise Handling**: [LABEL_NOISE_HANDLING]
- **Version Control**: [LABEL_VERSION_CONTROL]

### Data Augmentation
- **Augmentation Strategy**: [AUGMENTATION_STRATEGY]
- **Augmentation Techniques**: [AUGMENTATION_TECHNIQUES]
- **Synthetic Data Generation**: [SYNTHETIC_DATA_GENERATION]
- **Balance Strategy**: [BALANCE_STRATEGY]
- **Augmentation Pipeline**: [AUGMENTATION_PIPELINE]
- **Quality Control**: [AUGMENTATION_QUALITY]
- **Performance Impact**: [AUGMENTATION_IMPACT]
- **Domain Constraints**: [AUGMENTATION_CONSTRAINTS]
- **Evaluation Methods**: [AUGMENTATION_EVALUATION]
- **Tool Integration**: [AUGMENTATION_TOOLS]

Please provide detailed preprocessing pipelines, feature engineering code, labeling workflows, and quality metrics.

## Usage Examples

### Image Data Preparation
```
Prepare image dataset for ProductClassification with 100K images to achieve 95% model accuracy using computer vision techniques.

Data Collection:
- Collect from e-commerce catalogs, web scraping using Scrapy, BeautifulSoup tools
- Apply stratified sampling ensuring balanced product categories
- Implement duplicate detection and quality filtering validation rules
- Store in hierarchical folder storage format with JSON metadata capture

Feature Engineering:
- Extract RGB, HSV, texture features using OpenCV
- Apply histogram equalization, edge detection feature transformation
- Use one-hot encoding for categorical attributes
- Scale pixel values to [0,1] range using min-max scaling techniques
- Reduce dimensions with PCA for visualization

### Data Augmentation
- Apply rotation, flip, crop, brightness augmentation techniques
- Generate synthetic images using GANs synthetic data generation
- Balance classes using oversampling balance strategy
- Create Albumentations augmentation pipeline
- Maintain 90% accuracy quality control threshold
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[DATASET_NAME]` | Unique identifier for the dataset | "CustomerChurn_v3", "ProductImages_2024Q1", "TransactionFraud_cleaned" |
| `[DATA_SOURCE]` | Where data originates from | "PostgreSQL production database", "AWS S3 bucket (s3://data-lake/raw/)", "Snowflake analytics warehouse", "Kaggle competition dataset" |
| `[DATA_TYPE]` | Primary data modality | "Tabular (CSV/Parquet)", "Images (JPEG/PNG)", "Text (JSON documents)", "Time-series", "Audio (WAV)", "Mixed multimodal" |
| `[DATA_SIZE]` | Volume of data | "5M rows, 2.3GB Parquet", "100K images (250GB)", "10TB across 3 years", "500K documents (50GB)" |
| `[DATA_DOMAIN]` | Business domain of data | "E-commerce transactions", "Healthcare patient records", "Financial fraud detection", "Manufacturing IoT sensors" |
| `[QUALITY_LEVEL]` | Data quality assessment | "High: 98% complete, validated", "Medium: 85% complete, some noise", "Low: significant cleaning needed" |
| `[COLLECTION_METHOD]` | How data is collected | "Real-time API ingestion", "Daily batch ETL", "Manual upload", "Web scraping", "Sensor streaming" |
| `[UPDATE_FREQUENCY]` | How often data refreshes | "Real-time streaming", "Daily at 2am UTC", "Weekly batch", "Monthly snapshots", "One-time historical" |
| `[PRIVACY_LEVEL]` | Data sensitivity classification | "Public", "Internal only", "Confidential (PII)", "Highly restricted (PHI/PCI)" |
| `[COMPLIANCE_REQUIREMENTS]` | Regulatory compliance needs | "GDPR (EU data subjects)", "HIPAA (healthcare)", "PCI-DSS (payment data)", "SOC2", "None" |
| `[COLLECTION_STRATEGY]` | Overall collection approach | "Full historical backfill + incremental daily", "Streaming with 7-day retention", "Sample 10% of production traffic" |
| `[DATA_SOURCES]` | All source systems | "PostgreSQL, MongoDB, Salesforce API, Google Analytics, S3 logs", "Single source: data warehouse" |
| `[ACQUISITION_METHODS]` | Technical collection methods | "JDBC connector, REST API polling, Kafka consumer, File drop monitoring", "AWS Glue crawlers" |
| `[SAMPLING_STRATEGY]` | Sampling approach if applicable | "Stratified sampling (maintain class ratio)", "Random 10% sample", "Time-based (last 2 years)", "Full population" |
| `[COLLECTION_TOOLS]` | Tools used for collection | "Apache Airflow, Fivetran, AWS Glue, custom Python scripts", "dbt + Snowflake" |
| `[COLLECTION_QUALITY_CONTROL]` | QC during collection | "Schema validation, null checks, deduplication, freshness alerts", "Great Expectations suite" |
| `[VALIDATION_RULES]` | Data validation criteria | "email must match regex, age 0-120, timestamp not future, amount > 0", "Custom business rules in dbt tests" |
| `[COLLECTION_ERROR_HANDLING]` | Error handling approach | "Dead letter queue for failed records, alert on >1% failure rate, manual review queue" |
| `[STORAGE_FORMAT]` | Data storage format | "Parquet (columnar, compressed)", "Delta Lake", "CSV", "JSON Lines", "TFRecord" |
| `[METADATA_CAPTURE]` | Metadata tracked | "Source timestamp, ingestion timestamp, schema version, row count, file hash" |
| `[FEATURE_TYPES]` | Types of features in dataset | "Numerical (25), Categorical (15), DateTime (3), Text (2), Boolean (5)" |
| `[FEATURE_CREATION]` | New features to create | "Lag features (7/14/30 day), rolling averages, ratios, interaction terms, text embeddings" |
| `[FEATURE_SELECTION]` | Feature selection method | "Correlation filter (>0.9 removed), RFE with XGBoost, SHAP importance top 50" |
| `[FEATURE_TRANSFORMATION]` | Transformations applied | "Log transform skewed features, Box-Cox normalization, binning age into groups" |
| `[ENCODING_METHODS]` | Categorical encoding | "One-hot for low cardinality (<10), Target encoding for high cardinality, Label encoding for ordinal" |
| `[SCALING_TECHNIQUES]` | Numerical scaling | "StandardScaler (zero mean, unit variance)", "MinMaxScaler (0-1 range)", "RobustScaler for outliers" |
| `[DIMENSIONALITY_REDUCTION]` | Dimension reduction method | "PCA (95% variance retained)", "UMAP for visualization", "Autoencoder bottleneck", "None needed" |
| `[FEATURE_INTERACTION]` | Interaction features | "Polynomial features (degree=2)", "Manual interactions: price_per_unit = price/quantity", "None" |
| `[TEMPORAL_FEATURES]` | Time-based features | "Hour of day, day of week, month, is_weekend, days_since_last_purchase, seasonal decomposition" |
| `[DOMAIN_FEATURES]` | Domain-specific features | "RFM scores (Recency, Frequency, Monetary)", "Customer lifetime value", "Product category embeddings" |
| `[LABELING_STRATEGY]` | Labeling approach | "In-house annotation team", "Outsourced to Scale AI", "Crowdsourcing via MTurk", "Programmatic labeling" |
| `[ANNOTATION_GUIDELINES]` | Labeling instructions | "Detailed 10-page guideline with examples, edge cases, and decision trees", "Simple binary yes/no criteria" |
| `[LABELING_TOOLS]` | Annotation platform | "Label Studio", "Labelbox", "Amazon SageMaker Ground Truth", "Prodigy", "Custom internal tool" |
| `[LABELING_QA]` | Quality assurance process | "10% double-annotation, consensus review, expert spot-checks, automated consistency checks" |
| `[INTER_ANNOTATOR_AGREEMENT]` | Agreement metric | "Cohen's Kappa >0.8 required", "Fleiss' Kappa for multi-annotator", "95% agreement threshold" |
| `[ACTIVE_LEARNING]` | Active learning approach | "Uncertainty sampling for edge cases", "Query-by-committee", "Not using active learning" |
| `[SEMI_SUPERVISED_LEARNING]` | Semi-supervised approach | "Self-training with high-confidence pseudo-labels", "MixMatch", "Label propagation", "Not applicable" |
| `[WEAK_SUPERVISION]` | Weak supervision methods | "Snorkel labeling functions", "Keyword rules + heuristics", "Distant supervision from knowledge base" |
| `[LABEL_NOISE_HANDLING]` | Handling noisy labels | "Confident learning to identify mislabels", "Label smoothing", "Robust loss functions", "Manual review" |
| `[LABEL_VERSION_CONTROL]` | Label versioning | "Git tags for label schema changes", "DVC for label files", "Label Studio project versions" |
| `[AUGMENTATION_STRATEGY]` | Overall augmentation approach | "Online augmentation during training", "Offline pre-augmented dataset", "Both" |
| `[AUGMENTATION_TECHNIQUES]` | Specific augmentation methods | "Images: rotation, flip, crop, color jitter, mixup. Text: back-translation, synonym replacement. Tabular: SMOTE" |
| `[SYNTHETIC_DATA_GENERATION]` | Synthetic data approach | "CTGAN for tabular", "Stable Diffusion for images", "GPT-4 for text generation", "Not using synthetic data" |
| `[BALANCE_STRATEGY]` | Class balancing method | "SMOTE oversampling minority", "Random undersampling majority", "Class weights in loss function", "Focal loss" |
| `[AUGMENTATION_PIPELINE]` | Augmentation implementation | "Albumentations pipeline", "torchvision transforms", "nlpaug library", "Custom augmentation class" |
| `[AUGMENTATION_QUALITY]` | Quality validation | "Visual inspection of samples", "Model performance on augmented vs original", "Distribution comparison" |
| `[AUGMENTATION_IMPACT]` | Expected improvement | "+5% accuracy from augmentation", "Reduces overfitting by 20%", "Improves minority class recall by 15%" |
| `[AUGMENTATION_CONSTRAINTS]` | Constraints to respect | "Preserve label semantics", "Don't augment test set", "Medical images: no geometric distortion" |
| `[AUGMENTATION_EVALUATION]` | Evaluation methodology | "A/B test with/without augmentation", "Learning curve analysis", "Cross-validation comparison" |
| `[AUGMENTATION_TOOLS]` | Tools and libraries | "Albumentations, imgaug, nlpaug, audiomentations, imblearn", "Custom augmentation module" |



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Data Preparation Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/AI & Machine Learning](../../technology/AI & Machine Learning/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive data preparation for machine learning including feature engineering, data labeling, augmentation, preprocessing, and quality assurance for robust model training.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Understand data thoroughly before processing**
2. **Implement comprehensive quality checks**
3. **Version control all data and transformations**
4. **Document all preprocessing steps**
5. **Validate augmentation maintains data integrity**