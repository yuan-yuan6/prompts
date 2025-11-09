# CI/CD Pipelines Template

## Purpose
Design and implement comprehensive CI/CD pipelines for automated build, test, and deployment processes with quality gates, security scanning, and deployment strategies.

## Template Structure

### Pipeline Overview
- **Pipeline Name**: {pipeline_name}
- **Application Type**: {application_type}
- **Technology Stack**: {pipeline_technology_stack}
- **Deployment Environment**: {deployment_environment}
- **Pipeline Strategy**: {pipeline_strategy}
- **Team**: {pipeline_team}
- **Business Requirements**: {business_requirements}
- **Compliance Requirements**: {pipeline_compliance}
- **Performance Requirements**: {pipeline_performance}
- **Security Requirements**: {pipeline_security}

### Source Control Integration
- **Version Control System**: {version_control_system}
- **Branching Strategy**: {branching_strategy}
- **Merge Strategy**: {merge_strategy}
- **Code Review Process**: {code_review_process}
- **Commit Standards**: {commit_standards}
- **Trigger Conditions**: {trigger_conditions}
- **Webhook Configuration**: {webhook_configuration}
- **Branch Protection**: {branch_protection}
- **Access Controls**: {source_access_controls}
- **Audit Logging**: {source_audit_logging}

### Build Process
- **Build Tools**: {build_tools}
- **Build Environment**: {build_environment}
- **Dependency Management**: {dependency_management}
- **Artifact Generation**: {artifact_generation}
- **Build Optimization**: {build_optimization}
- **Caching Strategy**: {build_caching}
- **Parallel Builds**: {parallel_builds}
- **Build Notifications**: {build_notifications}
- **Build Metrics**: {build_metrics}
- **Failure Handling**: {build_failure_handling}

### Testing Strategy
- **Testing Framework**: {testing_framework}
- **Unit Testing**: {unit_testing}
- **Integration Testing**: {integration_testing}
- **End-to-End Testing**: {e2e_testing}
- **Performance Testing**: {performance_testing}
- **Security Testing**: {security_testing}
- **Test Data Management**: {test_data_management}
- **Test Environment**: {test_environment}
- **Test Reporting**: {test_reporting}
- **Coverage Requirements**: {coverage_requirements}

### Quality Gates
- **Gate Criteria**: {gate_criteria}
- **Code Quality**: {code_quality}
- **Security Scanning**: {security_scanning}
- **Vulnerability Assessment**: {vulnerability_assessment}
- **Compliance Checks**: {compliance_checks}
- **Performance Benchmarks**: {performance_benchmarks}
- **Approval Process**: {approval_process}
- **Override Procedures**: {override_procedures}
- **Gate Reporting**: {gate_reporting}
- **Metrics Collection**: {gate_metrics}

### Deployment Strategy
- **Deployment Model**: {deployment_model}
- **Environment Promotion**: {environment_promotion}
- **Blue-Green Deployment**: {blue_green_deployment}
- **Canary Deployment**: {canary_deployment}
- **Rolling Updates**: {rolling_updates}
- **Feature Flags**: {feature_flags}
- **Rollback Strategy**: {rollback_strategy}
- **Smoke Testing**: {smoke_testing}
- **Health Checks**: {deployment_health_checks}
- **Deployment Notifications**: {deployment_notifications}

Please provide detailed pipeline configurations, testing strategies, quality gates, and deployment procedures.

## Usage Examples

### Microservices CI/CD Pipeline
```
Design CI/CD pipeline for OrderService microservice using Docker containerization with Kubernetes deployment targeting AWS EKS environment.

Pipeline Overview:
- Microservices application type using Node.js, Express, PostgreSQL pipeline technology stack
- Deploy to dev, staging, prod deployment environment
- Use GitOps pipeline strategy with Platform Engineering pipeline team
- Meet <15min deployment business requirements with SOC2 pipeline compliance

Build Process:
- Use Docker, npm build tools in containerized build environment
- Manage with npm, package-lock.json dependency management
- Generate Docker images, Helm charts artifact generation
- Optimize with multi-stage builds, layer caching build optimization
- Cache node_modules, Docker layers build caching

Testing Strategy:
- Use Jest, Supertest testing framework
- Run unit tests with 90% coverage unit testing
- Execute API, database integration testing
- Perform Cypress e2e testing on staging
- Run k6 performance testing with SLA validation
- Scan with Snyk, OWASP ZAP security testing

Deployment Strategy:
- Use Kubernetes rolling updates deployment model
- Promote through dev → staging → prod environment promotion
- Implement Argo Rollouts canary deployment with 10/50/100% traffic
- Use LaunchDarkly feature flags for gradual rollout
- Enable automatic rollback on health check failures rollback strategy
```

## Best Practices

1. **Automate everything from build to deployment**
2. **Implement comprehensive testing at every stage**
3. **Use infrastructure as code for consistency**
4. **Monitor and measure pipeline performance**
5. **Plan for rollback and disaster recovery scenarios**