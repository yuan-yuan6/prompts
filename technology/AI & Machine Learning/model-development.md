# Model Development Template

## Purpose
Comprehensive machine learning model development including training, evaluation, deployment, monitoring, and optimization with MLOps best practices for scalable and reliable AI systems.

## Template Structure

### Project Overview
- **Model Name**: {model_name}
- **Problem Type**: {problem_type}
- **Business Objective**: {business_objective}
- **Use Case**: {use_case}
- **Stakeholders**: {stakeholders}
- **Success Metrics**: {success_metrics}
- **Timeline**: {project_timeline}
- **Budget**: {project_budget}
- **Regulatory Requirements**: {regulatory_requirements}
- **Ethical Considerations**: {ethical_considerations}

### Data Strategy
- **Data Sources**: {data_sources}
- **Data Volume**: {data_volume}
- **Data Quality**: {data_quality}
- **Data Collection**: {data_collection}
- **Data Preprocessing**: {data_preprocessing}
- **Feature Engineering**: {feature_engineering}
- **Data Splitting**: {data_splitting}
- **Data Versioning**: {data_versioning}
- **Data Privacy**: {data_privacy}
- **Data Governance**: {data_governance}

### Model Architecture
- **Algorithm Selection**: {algorithm_selection}
- **Model Type**: {model_type}
- **Architecture Design**: {architecture_design}
- **Framework**: {ml_framework}
- **Libraries**: {libraries}
- **Model Complexity**: {model_complexity}
- **Feature Selection**: {feature_selection}
- **Hyperparameters**: {hyperparameters}
- **Model Size**: {model_size}
- **Computational Requirements**: {computational_requirements}

### Training Strategy
- **Training Approach**: {training_approach}
- **Training Data**: {training_data}
- **Validation Strategy**: {validation_strategy}
- **Cross Validation**: {cross_validation}
- **Training Infrastructure**: {training_infrastructure}
- **Distributed Training**: {distributed_training}
- **Training Monitoring**: {training_monitoring}
- **Early Stopping**: {early_stopping}
- **Regularization**: {regularization}
- **Optimization**: {optimization}

### Model Evaluation
- **Evaluation Metrics**: {evaluation_metrics}
- **Performance Benchmarks**: {performance_benchmarks}
- **Baseline Models**: {baseline_models}
- **A/B Testing**: {ab_testing}
- **Model Comparison**: {model_comparison}
- **Statistical Tests**: {statistical_tests}
- **Error Analysis**: {error_analysis}
- **Bias Detection**: {bias_detection}
- **Fairness Evaluation**: {fairness_evaluation}
- **Interpretability**: {interpretability}

### Model Deployment
- **Deployment Strategy**: {deployment_strategy}
- **Deployment Environment**: {deployment_environment}
- **Model Serving**: {model_serving}
- **API Design**: {model_api_design}
- **Scaling Strategy**: {scaling_strategy}
- **Load Balancing**: {load_balancing}
- **Caching**: {model_caching}
- **Security**: {deployment_security}
- **Monitoring**: {deployment_monitoring}
- **Rollback Strategy**: {rollback_strategy}

### MLOps Implementation
- **MLOps Strategy**: {mlops_strategy}
- **Version Control**: {model_version_control}
- **CI/CD Pipeline**: {mlops_cicd}
- **Model Registry**: {model_registry}
- **Experiment Tracking**: {experiment_tracking}
- **Automation**: {mlops_automation}
- **Testing Framework**: {mlops_testing}
- **Deployment Pipeline**: {deployment_pipeline}
- **Monitoring Pipeline**: {monitoring_pipeline}
- **Governance**: {mlops_governance}

Please provide detailed implementation plans, code examples, evaluation frameworks, deployment configurations, and monitoring setups.

## Usage Examples

### Image Classification Model
```
Develop CNN image classification model for ProductCategorization to achieve 95% accuracy for E-commerce team within 3-month timeline using PyTorch framework.

Data Strategy:
- Use product images from S3, internal catalogs with 1M+ images data volume
- Implement image augmentation, normalization data preprocessing
- Apply ResNet feature engineering with 80/10/10 data splitting
- Version with DVC data versioning ensuring GDPR data privacy

Model Architecture:
- Select ResNet-50 algorithm selection for image classification model type
- Design transfer learning architecture design using PyTorch ml framework
- Configure 224x224 input, 1000 classes model complexity
- Optimize with Adam optimization and 0.001 learning rate hyperparameters

Training Strategy:
- Use supervised training approach with labeled product images training data
- Implement 5-fold cross validation validation strategy
- Deploy on AWS SageMaker training infrastructure with multi-GPU distributed training
- Monitor with TensorBoard training monitoring and patience=10 early stopping
```

## Best Practices

1. **Start with clear business objectives and success metrics**
2. **Ensure high-quality, representative training data**
3. **Use proper validation and testing strategies**
4. **Implement comprehensive monitoring and alerting**
5. **Follow MLOps best practices for reproducibility**