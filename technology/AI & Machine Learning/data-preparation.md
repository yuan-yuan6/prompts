# Data Preparation Template

## Purpose
Comprehensive data preparation for machine learning including feature engineering, data labeling, augmentation, preprocessing, and quality assurance for robust model training.

## Template Structure

### Data Overview
- **Dataset Name**: {dataset_name}
- **Data Source**: {data_source}
- **Data Type**: {data_type}
- **Data Size**: {data_size}
- **Domain**: {data_domain}
- **Quality Level**: {quality_level}
- **Collection Method**: {collection_method}
- **Update Frequency**: {update_frequency}
- **Privacy Level**: {privacy_level}
- **Compliance Requirements**: {compliance_requirements}

### Data Collection
- **Collection Strategy**: {collection_strategy}
- **Data Sources**: {data_sources}
- **Acquisition Methods**: {acquisition_methods}
- **Sampling Strategy**: {sampling_strategy}
- **Collection Tools**: {collection_tools}
- **Quality Control**: {collection_quality_control}
- **Validation Rules**: {validation_rules}
- **Error Handling**: {collection_error_handling}
- **Storage Format**: {storage_format}
- **Metadata Capture**: {metadata_capture}

### Feature Engineering
- **Feature Types**: {feature_types}
- **Feature Creation**: {feature_creation}
- **Feature Selection**: {feature_selection}
- **Feature Transformation**: {feature_transformation}
- **Encoding Methods**: {encoding_methods}
- **Scaling Techniques**: {scaling_techniques}
- **Dimensionality Reduction**: {dimensionality_reduction}
- **Feature Interaction**: {feature_interaction}
- **Temporal Features**: {temporal_features}
- **Domain Features**: {domain_features}

### Data Labeling
- **Labeling Strategy**: {labeling_strategy}
- **Annotation Guidelines**: {annotation_guidelines}
- **Labeling Tools**: {labeling_tools}
- **Quality Assurance**: {labeling_qa}
- **Inter-annotator Agreement**: {inter_annotator_agreement}
- **Active Learning**: {active_learning}
- **Semi-supervised Learning**: {semi_supervised_learning}
- **Weak Supervision**: {weak_supervision}
- **Label Noise Handling**: {label_noise_handling}
- **Version Control**: {label_version_control}

### Data Augmentation
- **Augmentation Strategy**: {augmentation_strategy}
- **Augmentation Techniques**: {augmentation_techniques}
- **Synthetic Data Generation**: {synthetic_data_generation}
- **Balance Strategy**: {balance_strategy}
- **Augmentation Pipeline**: {augmentation_pipeline}
- **Quality Control**: {augmentation_quality}
- **Performance Impact**: {augmentation_impact}
- **Domain Constraints**: {augmentation_constraints}
- **Evaluation Methods**: {augmentation_evaluation}
- **Tool Integration**: {augmentation_tools}

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

Data Augmentation:
- Apply rotation, flip, crop, brightness augmentation techniques
- Generate synthetic images using GANs synthetic data generation
- Balance classes using oversampling balance strategy
- Create Albumentations augmentation pipeline
- Maintain 90% accuracy quality control threshold
```

## Best Practices

1. **Understand data thoroughly before processing**
2. **Implement comprehensive quality checks**
3. **Version control all data and transformations**
4. **Document all preprocessing steps**
5. **Validate augmentation maintains data integrity**