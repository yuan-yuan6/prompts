---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- devops
- ci-cd
- quality-gates
- continuous-deployment
title: CI/CD Pipelines Template
use_cases:
- Creating design and implement comprehensive ci/cd pipelines for automated build,
  test, and deployment processes with quality gates, security scanning, and deployment
  strategies.
- Project planning and execution
- Strategy development
industries:
- manufacturing
- technology
type: template
difficulty: intermediate
slug: cicd-pipelines
---

# CI/CD Pipelines Template

## Purpose
Design and implement comprehensive CI/CD pipelines for automated build, test, and deployment processes with quality gates, security scanning, and deployment strategies.

## Quick DevOps Pipeline Prompt
Design CI/CD pipeline for [application type] using [CI tool]. Stack: [language], [framework], [database]. Pipeline: lint → build → test (unit/integration) → security scan → deploy. Environments: dev (auto-deploy) → staging (on PR merge) → production (manual approval). Include: artifact versioning, environment-specific configs, <[X] min total pipeline time.

## Quick Start

**Need to set up automated deployments quickly?** Use this minimal example:

### Minimal Example
```
Design a CI/CD pipeline for my Node.js API using GitHub Actions with Docker deployment to AWS ECS. Include unit tests, security scanning with Snyk, and automated rollback on failures. Deploy to staging on PR merge, production on main branch merge with manual approval gate.
```

### When to Use This
- Automating build, test, and deployment processes for applications
- Implementing quality gates and security scanning in delivery workflow
- Setting up multi-environment deployment strategies (dev/staging/prod)
- Reducing manual deployment errors and improving release velocity

### Basic 3-Step Workflow
1. **Define Pipeline Structure** - Specify application type, tech stack, environments, and deployment strategy
2. **Configure Build & Test** - Set up build tools, testing frameworks, quality gates, and security scanning
3. **Design Deployment Strategy** - Choose deployment model (rolling, blue-green, canary) and rollback procedures

**Time to complete**: 30 minutes for basic pipeline design, 4-8 hours for comprehensive enterprise pipeline

---

## Template Structure

### Pipeline Overview
- **Pipeline Name**: [PIPELINE_NAME]
- **Application Type**: [APPLICATION_TYPE]
- **Technology Stack**: [PIPELINE_TECHNOLOGY_STACK]
- **Deployment Environment**: [DEPLOYMENT_ENVIRONMENT]
- **Pipeline Strategy**: [PIPELINE_STRATEGY]
- **Team**: [PIPELINE_TEAM]
- **Business Requirements**: [BUSINESS_REQUIREMENTS]
- **Compliance Requirements**: [PIPELINE_COMPLIANCE]
- **Performance Requirements**: [PIPELINE_PERFORMANCE]
- **Security Requirements**: [PIPELINE_SECURITY]

### Source Control Integration
- **Version Control System**: [VERSION_CONTROL_SYSTEM]
- **Branching Strategy**: [BRANCHING_STRATEGY]
- **Merge Strategy**: [MERGE_STRATEGY]
- **Code Review Process**: [CODE_REVIEW_PROCESS]
- **Commit Standards**: [COMMIT_STANDARDS]
- **Trigger Conditions**: [TRIGGER_CONDITIONS]
- **Webhook Configuration**: [WEBHOOK_CONFIGURATION]
- **Branch Protection**: [BRANCH_PROTECTION]
- **Access Controls**: [SOURCE_ACCESS_CONTROLS]
- **Audit Logging**: [SOURCE_AUDIT_LOGGING]

### Build Process
- **Build Tools**: [BUILD_TOOLS]
- **Build Environment**: [BUILD_ENVIRONMENT]
- **Dependency Management**: [DEPENDENCY_MANAGEMENT]
- **Artifact Generation**: [ARTIFACT_GENERATION]
- **Build Optimization**: [BUILD_OPTIMIZATION]
- **Caching Strategy**: [BUILD_CACHING]
- **Parallel Builds**: [PARALLEL_BUILDS]
- **Build Notifications**: [BUILD_NOTIFICATIONS]
- **Build Metrics**: [BUILD_METRICS]
- **Failure Handling**: [BUILD_FAILURE_HANDLING]

### Testing Strategy
- **Testing Framework**: [TESTING_FRAMEWORK]
- **Unit Testing**: [UNIT_TESTING]
- **Integration Testing**: [INTEGRATION_TESTING]
- **End-to-End Testing**: [E2E_TESTING]
- **Performance Testing**: [PERFORMANCE_TESTING]
- **Security Testing**: [SECURITY_TESTING]
- **Test Data Management**: [TEST_DATA_MANAGEMENT]
- **Test Environment**: [TEST_ENVIRONMENT]
- **Test Reporting**: [TEST_REPORTING]
- **Coverage Requirements**: [COVERAGE_REQUIREMENTS]

### Quality Gates
- **Gate Criteria**: [GATE_CRITERIA]
- **Code Quality**: [CODE_QUALITY]
- **Security Scanning**: [SECURITY_SCANNING]
- **Vulnerability Assessment**: [VULNERABILITY_ASSESSMENT]
- **Compliance Checks**: [COMPLIANCE_CHECKS]
- **Performance Benchmarks**: [PERFORMANCE_BENCHMARKS]
- **Approval Process**: [APPROVAL_PROCESS]
- **Override Procedures**: [OVERRIDE_PROCEDURES]
- **Gate Reporting**: [GATE_REPORTING]
- **Metrics Collection**: [GATE_METRICS]

### Deployment Strategy
- **Deployment Model**: [DEPLOYMENT_MODEL]
- **Environment Promotion**: [ENVIRONMENT_PROMOTION]
- **Blue-Green Deployment**: [BLUE_GREEN_DEPLOYMENT]
- **Canary Deployment**: [CANARY_DEPLOYMENT]
- **Rolling Updates**: [ROLLING_UPDATES]
- **Feature Flags**: [FEATURE_FLAGS]
- **Rollback Strategy**: [ROLLBACK_STRATEGY]
- **Smoke Testing**: [SMOKE_TESTING]
- **Health Checks**: [DEPLOYMENT_HEALTH_CHECKS]
- **Deployment Notifications**: [DEPLOYMENT_NOTIFICATIONS]

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

### Testing Strategy
- Use Jest, Supertest testing framework
- Run unit tests with 90% coverage unit testing
- Execute API, database integration testing
- Perform Cypress e2e testing on staging
- Run k6 performance testing with SLA validation
- Scan with Snyk, OWASP ZAP security testing

### Deployment Strategy
- Use Kubernetes rolling updates deployment model
- Promote through dev → staging → prod environment promotion
- Implement Argo Rollouts canary deployment with 10/50/100% traffic
- Use LaunchDarkly feature flags for gradual rollout
- Enable automatic rollback on health check failures rollback strategy
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[PIPELINE_NAME]` | Specify the pipeline name | "John Smith" |
| `[APPLICATION_TYPE]` | Specify the application type | "Standard" |
| `[PIPELINE_TECHNOLOGY_STACK]` | Specify the pipeline technology stack | "Node.js + TypeScript", "Java Spring Boot + Maven", "Python + Poetry", "Go + Docker", ".NET Core + NuGet" |
| `[DEPLOYMENT_ENVIRONMENT]` | Specify the deployment environment | "AWS EKS (dev/staging/prod)", "Azure AKS multi-region", "GCP GKE + Cloud Run", "On-premise Kubernetes" |
| `[PIPELINE_STRATEGY]` | Specify the pipeline strategy | "GitOps with ArgoCD", "Trunk-based development", "Feature branch workflow", "Release train model" |
| `[PIPELINE_TEAM]` | Specify the pipeline team | "Platform Engineering team", "DevOps Center of Excellence", "SRE team", "Embedded DevOps engineers" |
| `[BUSINESS_REQUIREMENTS]` | Specify the business requirements | "<15min deployment time", "Zero-downtime releases", "Multi-region deployment", "Compliance audit trail" |
| `[PIPELINE_COMPLIANCE]` | Specify the pipeline compliance | "SOC2 Type II", "PCI-DSS Level 1", "HIPAA", "FedRAMP Moderate", "ISO 27001" |
| `[PIPELINE_PERFORMANCE]` | Specify the pipeline performance | "<5min build time", "<10min full pipeline", "95% success rate", "50 deployments/day capacity" |
| `[PIPELINE_SECURITY]` | Specify the pipeline security | "SAST/DAST integrated", "Container scanning", "Signed artifacts", "Secret rotation", "SBOM generation" |
| `[VERSION_CONTROL_SYSTEM]` | Specify the version control system | "GitHub Enterprise", "GitLab Self-hosted", "Azure DevOps Repos", "Bitbucket Cloud" |
| `[BRANCHING_STRATEGY]` | Specify the branching strategy | "GitFlow", "GitHub Flow", "Trunk-based development", "Release branching" |
| `[MERGE_STRATEGY]` | Specify the merge strategy | "Squash and merge", "Rebase and merge", "Merge commit", "Fast-forward only" |
| `[CODE_REVIEW_PROCESS]` | Specify the code review process | "2 approvers required", "CODEOWNERS enforcement", "Automated review assignment", "PR templates mandatory" |
| `[COMMIT_STANDARDS]` | Specify the commit standards | "Conventional Commits", "Signed commits required", "Jira ticket reference", "DCO sign-off" |
| `[TRIGGER_CONDITIONS]` | Specify the trigger conditions | "Push to main/develop", "Pull request opened", "Tag creation", "Scheduled nightly", "Manual approval" |
| `[WEBHOOK_CONFIGURATION]` | Specify the webhook configuration | "GitHub webhooks to Jenkins", "GitLab CI triggers", "Slack notifications", "PagerDuty alerts" |
| `[BRANCH_PROTECTION]` | Specify the branch protection | "Required status checks", "No force push on main", "Linear history required", "Admin enforcement" |
| `[SOURCE_ACCESS_CONTROLS]` | Specify the source access controls | "SSO with Okta/Azure AD", "Team-based permissions", "Read/write segregation", "IP allowlisting" |
| `[SOURCE_AUDIT_LOGGING]` | Specify the source audit logging | "Git audit log enabled", "CloudTrail integration", "SIEM forwarding", "90-day retention" |
| `[BUILD_TOOLS]` | Specify the build tools | "Docker + BuildKit", "Maven/Gradle", "npm/yarn/pnpm", "Bazel", "Make + CMake" |
| `[BUILD_ENVIRONMENT]` | Specify the build environment | "GitHub Actions runners", "Jenkins agents (ephemeral)", "GitLab CI Docker executors", "Self-hosted Kubernetes pods" |
| `[DEPENDENCY_MANAGEMENT]` | Specify the dependency management | "npm + package-lock.json", "Maven Central + Nexus proxy", "pip + requirements.txt", "Go modules" |
| `[ARTIFACT_GENERATION]` | Specify the artifact generation | "Docker images to ECR/GCR", "Helm charts to ChartMuseum", "npm packages to Artifactory", "JAR/WAR to Nexus" |
| `[BUILD_OPTIMIZATION]` | Specify the build optimization | "Multi-stage Docker builds", "Layer caching", "Incremental compilation", "Parallel test execution" |
| `[BUILD_CACHING]` | Specify the build caching | "Docker layer cache", "npm/Maven cache", "GitHub Actions cache", "Remote build cache (Gradle)" |
| `[PARALLEL_BUILDS]` | Specify the parallel builds | "Matrix builds for multi-platform", "Parallel test sharding", "Monorepo affected-only builds" |
| `[BUILD_NOTIFICATIONS]` | Specify the build notifications | "Slack #builds channel", "Email on failure", "GitHub commit status", "Teams webhook" |
| `[BUILD_METRICS]` | Specify the build metrics | "Build duration", "Queue time", "Success/failure rate", "Cache hit ratio", "Resource utilization" |
| `[BUILD_FAILURE_HANDLING]` | Specify the build failure handling | "Auto-retry on flaky tests", "Slack alert + assignee notification", "Auto-rollback trigger", "Incident creation" |
| `[TESTING_FRAMEWORK]` | Specify the testing framework | "Jest + React Testing Library", "JUnit 5 + Mockito", "pytest + coverage.py", "Go testing + testify" |
| `[UNIT_TESTING]` | Specify the unit testing | "80% coverage minimum", "Jest with snapshots", "JUnit parallel execution", "Mock external services" |
| `[INTEGRATION_TESTING]` | Specify the integration testing | "Testcontainers for databases", "WireMock for APIs", "LocalStack for AWS", "Docker Compose test env" |
| `[E2E_TESTING]` | Specify the e2e testing | "Cypress for web UI", "Playwright cross-browser", "Selenium Grid", "Appium for mobile" |
| `[PERFORMANCE_TESTING]` | Specify the performance testing | "k6 load testing", "JMeter for APIs", "Gatling scenarios", "Lighthouse CI for frontend" |
| `[SECURITY_TESTING]` | Specify the security testing | "Snyk for dependencies", "OWASP ZAP DAST", "SonarQube SAST", "Trivy container scanning" |
| `[TEST_DATA_MANAGEMENT]` | Specify the test data management | "Faker.js generated data", "Sanitized production snapshots", "Test fixtures in repo", "Database seeding scripts" |
| `[TEST_ENVIRONMENT]` | Specify the test environment | "Ephemeral Kubernetes namespace", "Docker Compose local", "AWS dev account", "Preview environments per PR" |
| `[TEST_REPORTING]` | Specify the test reporting | "JUnit XML + Allure reports", "Code coverage to Codecov", "Test results in PR comments", "Grafana dashboards" |
| `[COVERAGE_REQUIREMENTS]` | Specify the coverage requirements | "80% line coverage", "70% branch coverage", "100% critical paths", "No decrease from baseline" |
| `[GATE_CRITERIA]` | Specify the gate criteria | "All tests passing", "No critical vulnerabilities", "Coverage threshold met", "Performance SLA achieved" |
| `[CODE_QUALITY]` | Specify the code quality | "SonarQube Quality Gate", "ESLint/Prettier zero warnings", "Checkstyle compliance", "Complexity limits" |
| `[SECURITY_SCANNING]` | Specify the security scanning | "Snyk in CI pipeline", "Trivy image scan", "OWASP dependency check", "GitLeaks secret detection" |
| `[VULNERABILITY_ASSESSMENT]` | Specify the vulnerability assessment | "No critical/high CVEs", "CVSS score threshold <7", "48hr remediation SLA", "Exception approval workflow" |
| `[COMPLIANCE_CHECKS]` | Specify the compliance checks | "License compliance (FOSSA)", "SBOM generation", "Policy-as-code (OPA)", "Audit log verification" |
| `[PERFORMANCE_BENCHMARKS]` | Specify the performance benchmarks | "p95 latency <200ms", "Throughput >1000 RPS", "Error rate <0.1%", "Memory <512MB per pod" |
| `[APPROVAL_PROCESS]` | Specify the approval process | "Auto-approve for dev", "Tech lead for staging", "Change Advisory Board for prod", "Emergency bypass with audit" |
| `[OVERRIDE_PROCEDURES]` | Specify the override procedures | "Senior engineer approval", "Incident commander authority", "Documented exception", "Time-limited bypass" |
| `[GATE_REPORTING]` | Specify the gate reporting | "Pipeline dashboard in Grafana", "Weekly quality metrics email", "PR gate status checks", "Compliance audit reports" |
| `[GATE_METRICS]` | Specify the gate metrics | "Gate pass rate", "Average gate duration", "Override frequency", "Blocked deployments count" |
| `[DEPLOYMENT_MODEL]` | Specify the deployment model | "Kubernetes rolling update", "Blue-green with ALB", "Canary with Istio", "A/B testing with LaunchDarkly" |
| `[ENVIRONMENT_PROMOTION]` | Specify the environment promotion | "dev → staging → prod", "Feature branch → preview → main", "Ring-based rollout", "Multi-region progressive" |
| `[BLUE_GREEN_DEPLOYMENT]` | Specify the blue green deployment | "AWS ALB target group switching", "Kubernetes service selector swap", "DNS weighted routing", "Instant rollback capability" |
| `[CANARY_DEPLOYMENT]` | Specify the canary deployment | "Argo Rollouts with 10/50/100% progression", "Flagger with Istio", "AWS AppMesh canary", "Manual promotion gates" |
| `[ROLLING_UPDATES]` | Specify the rolling updates | "maxSurge: 25%, maxUnavailable: 0", "One pod at a time", "Health check validation between batches" |
| `[FEATURE_FLAGS]` | Specify the feature flags | "LaunchDarkly", "Split.io", "Unleash self-hosted", "AWS AppConfig", "Environment variables" |
| `[ROLLBACK_STRATEGY]` | Specify the rollback strategy | "Automatic on health check failure", "One-click GitOps revert", "Database migration rollback scripts", "Blue-green instant switch" |
| `[SMOKE_TESTING]` | Specify the smoke testing | "Health endpoint verification", "Critical path API tests", "Synthetic transaction monitoring", "Canary metrics validation" |
| `[DEPLOYMENT_HEALTH_CHECKS]` | Specify the deployment health checks | "Kubernetes liveness/readiness probes", "HTTP 200 on /health", "Database connectivity check", "Downstream service availability" |
| `[DEPLOYMENT_NOTIFICATIONS]` | Specify the deployment notifications | "Slack #deployments channel", "PagerDuty for failures", "Email stakeholders", "GitHub deployment status" |



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (CI/CD Pipelines Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/DevOps & Cloud](../../technology/DevOps & Cloud/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating design and implement comprehensive ci/cd pipelines for automated build, test, and deployment processes with quality gates, security scanning, and deployment strategies.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Automate everything from build to deployment**
2. **Implement comprehensive testing at every stage**
3. **Use infrastructure as code for consistency**
4. **Monitor and measure pipeline performance**
5. **Plan for rollback and disaster recovery scenarios**