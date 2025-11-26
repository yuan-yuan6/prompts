---
category: ai-ml-applications
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- automation
- design
- development
- ai-ml
- management
- optimization
- security
title: MLOps Template
use_cases:
- Creating implement comprehensive mlops practices including ci/cd pipelines, model
  monitoring, versioning, automated testing, and governance for scalable and reliable
  machine learning systems.
- Project planning and execution
- Strategy development
industries:
- manufacturing
- technology
type: template
difficulty: intermediate
slug: mlops
---

# MLOps Template

## Purpose
Implement comprehensive MLOps practices including CI/CD pipelines, model monitoring, versioning, automated testing, and governance for scalable and reliable machine learning systems.

## 🚀 Quick Pipeline Prompt

> Design an **MLOps pipeline** for **[ML USE CASE]** at **[ORGANIZATION SIZE/MATURITY]** using **[TECH STACK: cloud provider, ML framework]**. Guide me through: (1) **CI/CD setup**—what's the pipeline from code commit to production? What quality gates (tests, validations) at each stage? (2) **Model lifecycle**—how to handle experiment tracking, model registry, versioning, and promotion? (3) **Monitoring & retraining**—what drift detection triggers retraining? How to automate the feedback loop? (4) **Governance**—what approval workflows, audit trails, and compliance checks? Provide pipeline configuration (GitHub Actions/Kubeflow), infrastructure-as-code templates, and a maturity roadmap.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid MLOps implementation.

---

## Quick Start

**Implement MLOps in 5 steps:**

1. **Version Everything**: Use Git for code, DVC/MLflow for data/models, track experiments with parameters and metrics
2. **Automate Training Pipeline**: Create reproducible training with Airflow/Kubeflow, schedule retraining, log all artifacts
3. **Deploy with CI/CD**: Build Docker images, run tests (unit, integration, model validation), deploy to staging then production
4. **Monitor Production Models**: Track prediction drift, data drift, model performance, latency, errors with dashboards and alerts
5. **Enable Governance**: Implement model registry, approval workflows, A/B testing, rollback procedures, audit logging

**Quick MLOps Pipeline:**
```python
# mlflow_training.py
import mlflow
from sklearn.ensemble import RandomForestClassifier

mlflow.set_experiment("production-model")

with mlflow.start_run():
    # Log parameters
    params = {'n_estimators': 100, 'max_depth': 10}
    mlflow.log_params(params)

    # Train model
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    # Log metrics
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)

    # Save model
    mlflow.sklearn.log_model(model, "model")
```

```yaml
# .github/workflows/ml-pipeline.yml
name: ML Pipeline
on: [push]
jobs:
  train-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Train model
        run: python mlflow_training.py
      - name: Run tests
        run: pytest tests/
      - name: Deploy to production
        run: mlflow models serve -m models:/production-model/latest
```

## Template Structure

### MLOps Strategy
- **MLOps Maturity**: [MLOPS_MATURITY]
- **Organization Size**: [ORGANIZATION_SIZE]
- **Use Cases**: [MLOPS_USE_CASES]
- **Technology Stack**: [TECHNOLOGY_STACK]
- **Team Structure**: [TEAM_STRUCTURE]
- **Budget**: [MLOPS_BUDGET]
- **Timeline**: [IMPLEMENTATION_TIMELINE]
- **Success Metrics**: [MLOPS_SUCCESS_METRICS]
- **Governance Model**: [GOVERNANCE_MODEL]
- **Compliance Requirements**: [MLOPS_COMPLIANCE]

### Model Lifecycle
- **Experimentation**: [EXPERIMENTATION]
- **Development**: [MODEL_DEVELOPMENT]
- **Training**: [TRAINING_PIPELINE]
- **Validation**: [VALIDATION_PIPELINE]
- **Deployment**: [DEPLOYMENT_PIPELINE]
- **Monitoring**: [MONITORING_PIPELINE]
- **Retraining**: [RETRAINING_PIPELINE]
- **Retirement**: [MODEL_RETIREMENT]
- **Version Control**: [LIFECYCLE_VERSIONING]
- **Governance**: [LIFECYCLE_GOVERNANCE]

### CI/CD Pipeline
- **Version Control**: [VERSION_CONTROL_SYSTEM]
- **Build Process**: [BUILD_PROCESS]
- **Testing Strategy**: [TESTING_STRATEGY]
- **Deployment Strategy**: [DEPLOYMENT_STRATEGY]
- **Environment Management**: [ENVIRONMENT_MANAGEMENT]
- **Artifact Management**: [ARTIFACT_MANAGEMENT]
- **Release Management**: [RELEASE_MANAGEMENT]
- **Rollback Strategy**: [ROLLBACK_STRATEGY]
- **Quality Gates**: [QUALITY_GATES]
- **Automation Level**: [AUTOMATION_LEVEL]

### Model Monitoring
- **Performance Monitoring**: [PERFORMANCE_MONITORING]
- **Data Drift Detection**: [DATA_DRIFT_DETECTION]
- **Model Drift Detection**: [MODEL_DRIFT_DETECTION]
- **Feature Monitoring**: [FEATURE_MONITORING]
- **Bias Monitoring**: [BIAS_MONITORING]
- **Fairness Monitoring**: [FAIRNESS_MONITORING]
- **Explainability**: [EXPLAINABILITY_MONITORING]
- **Alert System**: [ALERT_SYSTEM]
- **Dashboard Design**: [MONITORING_DASHBOARD]
- **Reporting**: [MONITORING_REPORTING]

### Infrastructure
- **Compute Infrastructure**: [COMPUTE_INFRASTRUCTURE]
- **Storage Infrastructure**: [STORAGE_INFRASTRUCTURE]
- **Model Serving**: [MODEL_SERVING]
- **Scaling Strategy**: [SCALING_STRATEGY]
- **Resource Management**: [RESOURCE_MANAGEMENT]
- **Cost Optimization**: [COST_OPTIMIZATION]
- **Security**: [INFRASTRUCTURE_SECURITY]
- **Networking**: [NETWORKING]
- **Backup Strategy**: [BACKUP_STRATEGY]
- **Disaster Recovery**: [DISASTER_RECOVERY]

Please provide detailed pipeline configurations, monitoring setups, infrastructure code, and governance frameworks.

## Usage Examples

### Production MLOps Pipeline
```
Implement MLOps pipeline for RecommendationSystem serving 1M+ users with <100ms latency using Kubernetes and MLflow.

CI/CD Pipeline:
- Use Git version control system with feature branch workflow
- Implement Docker containerization build process
- Apply unit, integration, model testing strategy
- Deploy with blue-green deployment strategy using ArgoCD
- Manage dev/staging/prod environment management with Helm

Model Monitoring:
- Track accuracy, precision, recall performance monitoring
- Detect statistical data drift detection with 95% confidence
- Monitor prediction model drift detection weekly
- Alert on >5% accuracy degradation alert system
- Create Grafana monitoring dashboard with daily reporting

### Infrastructure
- Deploy on AWS EKS compute infrastructure
- Use S3, EFS storage infrastructure for data and models
- Serve with Seldon model serving at 1K req/sec
- Scale with HPA scaling strategy based on CPU/memory
- Optimize costs with spot instances cost optimization
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[MLOPS_MATURITY]` | Specify the mlops maturity | "Level 0 - Manual, Level 1 - ML Pipeline Automation, Level 2 - CI/CD Pipeline Automation, Level 3 - Automated Retraining" |
| `[ORGANIZATION_SIZE]` | Specify the organization size | "Startup (5-50 employees), Mid-size (50-500), Enterprise (500+), 10 ML engineers, 3 data scientists" |
| `[MLOPS_USE_CASES]` | Specify the mlops use cases | "Real-time fraud detection, Recommendation systems, Demand forecasting, NLP pipelines, Computer vision inference" |
| `[TECHNOLOGY_STACK]` | Specify the technology stack | "MLflow + Kubeflow + AWS SageMaker, TensorFlow + Seldon + GCP Vertex AI, PyTorch + BentoML + Azure ML" |
| `[TEAM_STRUCTURE]` | Specify the team structure | "Platform team + embedded ML engineers, Centralized MLOps CoE, Hybrid model with shared services" |
| `[MLOPS_BUDGET]` | Specify the mlops budget | "$500,000" |
| `[IMPLEMENTATION_TIMELINE]` | Specify the implementation timeline | "6 months" |
| `[MLOPS_SUCCESS_METRICS]` | Specify the mlops success metrics | "Model deployment frequency, Time to production <2 weeks, Model failure rate <1%, Training cost reduction 30%" |
| `[GOVERNANCE_MODEL]` | Specify the governance model | "Centralized model registry approval, Federated with guardrails, Self-service with audit trails" |
| `[MLOPS_COMPLIANCE]` | Specify the mlops compliance | "SOC 2 Type II, GDPR model explainability, HIPAA for healthcare ML, FDA 21 CFR Part 11 for medical devices" |
| `[EXPERIMENTATION]` | Specify the experimentation | "Jupyter notebooks with MLflow tracking, Weights & Biases experiment sweeps, DVC experiments with Git branches" |
| `[MODEL_DEVELOPMENT]` | Specify the model development | "Feature engineering in feature store, Hyperparameter tuning with Optuna, Model selection with cross-validation" |
| `[TRAINING_PIPELINE]` | Specify the training pipeline | "Kubeflow Pipelines on Kubernetes, AWS SageMaker Pipelines, Apache Airflow DAGs with MLflow integration" |
| `[VALIDATION_PIPELINE]` | Specify the validation pipeline | "Great Expectations data validation, Model card generation, A/B test statistical analysis, Shadow mode testing" |
| `[DEPLOYMENT_PIPELINE]` | Specify the deployment pipeline | "ArgoCD GitOps deployment, AWS CodePipeline + SageMaker Endpoints, Seldon Core on Kubernetes" |
| `[MONITORING_PIPELINE]` | Specify the monitoring pipeline | "Evidently AI drift detection, Prometheus + Grafana metrics, WhyLabs continuous monitoring" |
| `[RETRAINING_PIPELINE]` | Specify the retraining pipeline | "Scheduled daily/weekly retraining, Drift-triggered automatic retraining, Champion-challenger evaluation" |
| `[MODEL_RETIREMENT]` | Specify the model retirement | "Gradual traffic reduction over 7 days, Archival to cold storage, Audit log retention for 7 years" |
| `[LIFECYCLE_VERSIONING]` | Specify the lifecycle versioning | "Semantic versioning (v1.2.3), MLflow Model Registry versions, DVC data versioning with Git tags" |
| `[LIFECYCLE_GOVERNANCE]` | Specify the lifecycle governance | "Model review board approval, Automated compliance checks, Production promotion gates" |
| `[VERSION_CONTROL_SYSTEM]` | Specify the version control system | "GitHub with branch protection, GitLab with merge request workflows, Bitbucket with DVC integration" |
| `[BUILD_PROCESS]` | Specify the build process | "Docker multi-stage builds, Conda environment packaging, Poetry + pip-tools dependency locking" |
| `[TESTING_STRATEGY]` | Specify the testing strategy | "Unit tests (pytest), Integration tests (model serving), Model validation tests (accuracy thresholds), Load tests (Locust)" |
| `[DEPLOYMENT_STRATEGY]` | Specify the deployment strategy | "Blue-green deployment, Canary releases (10% -> 50% -> 100%), Shadow mode, Rolling updates" |
| `[ENVIRONMENT_MANAGEMENT]` | Specify the environment management | "Helm charts for K8s, Terraform for infrastructure, Docker Compose for local dev, Conda environments" |
| `[ARTIFACT_MANAGEMENT]` | Specify the artifact management | "MLflow Model Registry, JFrog Artifactory, AWS ECR for containers, S3 for model artifacts" |
| `[RELEASE_MANAGEMENT]` | Specify the release management | "Semantic versioning with changelog, GitOps release automation, Staged rollouts with approval gates" |
| `[ROLLBACK_STRATEGY]` | Specify the rollback strategy | "Instant rollback to previous version, Traffic shifting to stable model, Automated rollback on error rate >5%" |
| `[QUALITY_GATES]` | Specify the quality gates | "Model accuracy >95%, Latency p99 <100ms, Code coverage >80%, Security scan pass, Bias audit pass" |
| `[AUTOMATION_LEVEL]` | Specify the automation level | "Fully automated CI/CD, Manual approval for production, Automated testing + manual deployment" |
| `[PERFORMANCE_MONITORING]` | Specify the performance monitoring | "Accuracy, precision, recall, F1 score tracking, Latency p50/p95/p99, Throughput (requests/sec), Error rates" |
| `[DATA_DRIFT_DETECTION]` | Specify the data drift detection | "KS test for numerical features, Chi-squared for categorical, PSI (Population Stability Index) >0.2 threshold" |
| `[MODEL_DRIFT_DETECTION]` | Specify the model drift detection | "Prediction distribution shift, Concept drift via accuracy decay, Feature importance changes" |
| `[FEATURE_MONITORING]` | Specify the feature monitoring | "Feature value distributions, Missing value rates, Feature store freshness, Schema validation" |
| `[BIAS_MONITORING]` | Specify the bias monitoring | "Demographic parity across protected attributes, Equalized odds monitoring, Disparate impact ratio" |
| `[FAIRNESS_MONITORING]` | Specify the fairness monitoring | "Equal opportunity difference <5%, Predictive equality, Fairlearn metrics dashboard" |
| `[EXPLAINABILITY_MONITORING]` | Specify the explainability monitoring | "SHAP value tracking, LIME explanations, Feature attribution shifts, Attention weight analysis" |
| `[ALERT_SYSTEM]` | Specify the alert system | "PagerDuty integration, Slack notifications, Email alerts, OpsGenie escalation, Custom webhooks" |
| `[MONITORING_DASHBOARD]` | Specify the monitoring dashboard | "Grafana dashboards, DataDog ML monitoring, MLflow UI, Custom Streamlit dashboard" |
| `[MONITORING_REPORTING]` | Specify the monitoring reporting | "Daily performance reports, Weekly drift summaries, Monthly model health scorecards, Quarterly reviews" |
| `[COMPUTE_INFRASTRUCTURE]` | Specify the compute infrastructure | "AWS EKS with GPU nodes, GCP GKE Autopilot, Azure AKS, On-premise Kubernetes with NVIDIA DGX" |
| `[STORAGE_INFRASTRUCTURE]` | Specify the storage infrastructure | "AWS S3 for artifacts, EFS for shared storage, Delta Lake for feature store, MinIO for on-premise" |
| `[MODEL_SERVING]` | Specify the model serving | "Seldon Core, TensorFlow Serving, TorchServe, NVIDIA Triton, BentoML, AWS SageMaker Endpoints" |
| `[SCALING_STRATEGY]` | Specify the scaling strategy | "Kubernetes HPA based on CPU/memory, Custom metrics (requests/sec), KEDA event-driven scaling" |
| `[RESOURCE_MANAGEMENT]` | Specify the resource management | "Kubernetes resource quotas, GPU time-sharing, Spot instances for training, Reserved capacity for serving" |
| `[COST_OPTIMIZATION]` | Specify the cost optimization | "Spot/preemptible instances for training (70% savings), Auto-shutdown idle endpoints, Right-sizing GPU instances" |
| `[INFRASTRUCTURE_SECURITY]` | Specify the infrastructure security | "VPC isolation, IAM roles with least privilege, Secrets Manager for credentials, TLS everywhere" |
| `[NETWORKING]` | Specify the networking | "Service mesh (Istio), Internal load balancers, VPC peering, Private endpoints, mTLS between services" |
| `[BACKUP_STRATEGY]` | Specify the backup strategy | "Daily model artifact snapshots, Cross-region replication, Versioned S3 buckets, 30-day retention" |
| `[DISASTER_RECOVERY]` | Specify the disaster recovery | "Multi-region deployment, RTO <1 hour RPO <15 minutes, Automated failover, Regular DR testing" |



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (MLOps Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/AI & Machine Learning](../../technology/AI & Machine Learning/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating implement comprehensive mlops practices including ci/cd pipelines, model monitoring, versioning, automated testing, and governance for scalable and reliable machine learning systems.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Start with simple automation and gradually increase complexity**
2. **Implement comprehensive testing at every stage**
3. **Monitor model performance continuously in production**
4. **Version everything: data, code, models, configurations**
5. **Build governance and compliance into the pipeline**