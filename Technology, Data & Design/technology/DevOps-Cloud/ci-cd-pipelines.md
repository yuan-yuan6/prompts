---
category: technology
related_templates:
- technology/DevOps-Cloud/infrastructure-as-code.md
- technology/DevOps-Cloud/container-orchestration.md
- technology/DevOps-Cloud/cloud-architecture-framework.md
tags:
- devops
- ci-cd
- build-automation
- deployment-pipeline
title: CI/CD Pipeline Development
use_cases:
- Designing end-to-end CI/CD pipelines achieving <10 minute build times with automated testing, security scanning, and deployment to staging
- Implementing deployment strategies (blue-green, canary, rolling) with automated rollback on error rate thresholds for zero-downtime releases
- Building quality gates with coverage thresholds, vulnerability scanning, and approval workflows meeting SOC2/PCI-DSS compliance requirements
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: ci-cd-pipelines
---

# CI/CD Pipeline Development

## Purpose
Design and implement CI/CD pipelines automating build, test, security scan, and deployment stages achieving <10 minute feedback loops, 99%+ deployment success rates, and compliance with security and regulatory requirements.

## Template

Create CI/CD pipeline for {APPLICATION_TYPE} using {PLATFORM} deploying to {INFRASTRUCTURE} with {DEPLOYMENT_STRATEGY} achieving {BUILD_TIME} build time and {SUCCESS_RATE}% deployment success.

**PIPELINE ARCHITECTURE AND STAGES**

Structure pipeline stages for fast feedback and progressive confidence. Commit stage (<5 minutes): lint code, run unit tests, static analysis, build artifacts—provides immediate feedback on code quality. Test stage (5-15 minutes): integration tests, contract tests, security scans—validates component interactions and security posture. Deployment stages: staging (automatic on main branch merge), production (manual approval or canary automation)—progressive validation with increasing blast radius.

Choose pipeline platform matching team expertise and infrastructure. GitHub Actions: native GitHub integration, YAML-based, free for public repos, matrix builds for multi-platform. GitLab CI: integrated with GitLab, Auto DevOps for quick start, built-in container registry. Jenkins: most flexible and extensible, requires maintenance, best for complex enterprise requirements. Azure DevOps: Microsoft ecosystem integration, excellent for .NET, good hybrid cloud support. CircleCI/BuildKite: fast execution, good caching, orbs/plugins ecosystem.

Configure triggers balancing automation with control. Push triggers: run on every commit to validate continuously, use path filters to skip irrelevant changes (docs-only PRs). Pull request triggers: full validation before merge, require status checks to pass. Branch-specific: feature branches run fast subset, main branch runs full pipeline including deploy. Scheduled: nightly full regression, weekly dependency updates, monthly security audits. Manual: production deployments with approval, hotfix fast-track with reduced gates.

**BUILD OPTIMIZATION AND ARTIFACT MANAGEMENT**

Optimize build speed through caching and parallelization. Dependency caching: cache node_modules/vendor by lockfile hash, 60-80% build time reduction. Layer caching: Docker BuildKit with registry cache, reuse unchanged layers. Parallel execution: run independent steps concurrently (lint, type-check, test in parallel). Incremental builds: Nx/Turborepo affected commands build only changed packages in monorepos. Remote caching: share build cache across team members and CI runners.

Configure build agents matching workload requirements. Cloud-hosted runners: fastest setup, pay-per-minute, limited customization. Self-hosted runners: full control, persistent caching, cost-effective at scale. Ephemeral containers: clean environment per build, no state pollution, slightly slower startup. Resource sizing: 2 vCPU/4GB for typical builds, 4+ vCPU for compilation-heavy projects, GPU runners for ML pipelines. Auto-scaling: scale runners 2-20 based on queue depth, spot instances for cost savings.

Manage artifacts with versioning and retention policies. Naming conventions: {service}-{version}-{sha} for traceability (api-v1.2.3-abc1234). Container images: push to ECR/GCR/Harbor with immutable tags, scan for vulnerabilities on push. Semantic versioning: major.minor.patch for releases, git SHA suffix for dev builds. Retention: production artifacts 1 year, staging 90 days, dev builds 30 days. Artifact signing: Cosign keyless signing, SLSA provenance for supply chain security.

**TESTING STRATEGY AND QUALITY GATES**

Implement test pyramid with appropriate coverage at each level. Unit tests (70% of tests): fast (<1ms each), isolated, mock dependencies, run on every commit. Integration tests (20%): test component interactions, use test containers for real databases, run on PR merge. End-to-end tests (10%): critical user journeys only, run in staging environment, slower but highest confidence. Contract tests: Pact for consumer-driven contracts between services, catch breaking API changes early.

Configure quality gates enforcing standards. Code coverage: 80% line coverage minimum, 70% branch coverage, fail build if below threshold. Code quality: SonarQube rules, cyclomatic complexity <10, no new critical issues. Security: zero critical/high vulnerabilities with known exploits, dependency audit passing. Performance: build time <10 minutes, test execution <5 minutes, deployment <5 minutes. Documentation: README required for new services, API docs auto-generated.

Implement security scanning at multiple layers. SAST (Static): SonarQube/CodeQL/Semgrep scan source code for vulnerabilities, run on every commit. SCA (Dependency): Snyk/Dependabot scan dependencies for known CVEs, auto-create PRs for updates. Container scanning: Trivy/Clair scan images for OS and application vulnerabilities, block critical. DAST (Dynamic): OWASP ZAP scan running application in staging, weekly full scans. Secret detection: GitLeaks/TruffleHog pre-commit hooks prevent credential commits.

Handle test failures and flakiness systematically. Retry strategy: automatic retry 2x for flaky tests, separate flaky test report. Quarantine: move consistently failing tests to quarantine, fix within sprint. Root cause analysis: categorize failures (environment, timing, data, code), track patterns. Test data management: isolated test data per suite, cleanup after tests, synthetic data generation.

**DEPLOYMENT STRATEGIES AND ROLLBACK**

Select deployment strategy matching risk tolerance and infrastructure. Rolling deployment: update pods gradually (25% at a time), zero downtime, simple but slow rollback. Blue-green deployment: full parallel environment, instant cutover, requires 2x resources during deploy. Canary deployment: route 5% traffic to new version, monitor metrics, gradually increase to 100%. Feature flags: deploy code disabled, enable for percentage of users, fastest rollback (toggle off).

Configure canary deployments with automated analysis. Traffic routing: Istio/Linkerd/ALB weighted routing, start at 1-5%. Promotion criteria: error rate <0.5%, latency p99 within 10% of baseline, no new exceptions. Analysis duration: 15-30 minutes per stage (5% → 25% → 50% → 100%). Automated rollback triggers: error rate exceeds threshold, latency degrades, health checks fail. Tools: Argo Rollouts, Flagger, Spinnaker for Kubernetes-native progressive delivery.

Implement robust rollback procedures. Automated triggers: error rate >1% for 5 minutes, p99 latency >2x baseline, 3+ failed health checks. Rollback execution: previous version promotion (not rebuild), database forward-compatible migrations. Database strategy: expand-contract pattern, avoid breaking schema changes, support N-1 versions. Configuration rollback: GitOps revert commit, Helm rollback to previous release. Recovery time: target <5 minutes from trigger to full rollback completion.

Post-deployment validation ensures successful releases. Smoke tests: critical path verification (login, core features) within 2 minutes of deploy. Health checks: /health endpoint with dependency status, /ready for load balancer routing. Synthetic monitoring: continuous user journey tests from multiple regions. Business metrics: conversion rate, revenue, engagement compared to pre-deploy baseline. Observability: traces and logs correlated with deployment markers for debugging.

**ENVIRONMENT MANAGEMENT**

Provision environments consistently with infrastructure as code. Environment parity: dev/staging/production use same Terraform modules, config-only differences. Ephemeral environments: per-PR preview environments, 4-hour TTL, auto-cleanup. Resource optimization: dev uses t3.medium, staging t3.large, production m5.xlarge with auto-scaling. Cost management: non-production environments shut down nights/weekends (60% cost reduction).

Manage configuration and secrets securely. Configuration hierarchy: defaults → environment → deployment-specific overrides. Secret management: HashiCorp Vault/AWS Secrets Manager, never in code or environment variables in plain text. Secret rotation: automated rotation for database credentials, API keys quarterly. Feature flags: LaunchDarkly/Unleash for runtime configuration, gradual feature rollouts.

**MONITORING AND OBSERVABILITY**

Track pipeline health and performance metrics. DORA metrics: deployment frequency, lead time, change failure rate, MTTR—track weekly trends. Build metrics: success rate (target >95%), duration (track regressions), queue wait time. Test metrics: pass rate, flaky test percentage, coverage trends. Alert on degradation: build time increases >20%, success rate drops below 90%.

Integrate deployment observability. Deployment markers: annotate metrics dashboards with deployment times, correlate changes with incidents. Log correlation: trace ID from build through deployment to runtime logs. Error tracking: Sentry/Rollbar integration, group errors by deployment version. Custom metrics: deployments per day per service, rollback frequency, time-to-production.

Deliver CI/CD pipeline as:

1. **PIPELINE CONFIGURATION** - Platform-specific YAML/Jenkinsfile with stages, triggers, and conditions

2. **BUILD SPECIFICATION** - Dockerfile, build scripts, caching configuration, artifact naming

3. **TEST CONFIGURATION** - Test framework setup, coverage thresholds, parallel execution, retry policies

4. **SECURITY GATES** - SAST/DAST/SCA tool configuration, vulnerability thresholds, compliance checks

5. **DEPLOYMENT AUTOMATION** - Environment provisioning, deployment strategy implementation, rollback procedures

6. **MONITORING DASHBOARD** - Pipeline metrics, DORA metrics, alerting rules, SLO tracking

---

## Usage Examples

### Example 1: Node.js Microservices Platform
**Prompt:** Create CI/CD pipeline for Node.js microservices (25 services) using GitHub Actions deploying to AWS EKS with canary strategy achieving <8 minute builds and 99.5% deployment success.

**Expected Output:** Pipeline architecture: commit stage (4 min: lint, type-check, unit tests parallel), test stage (6 min: integration tests with Testcontainers, Pact contract tests), security stage (3 min: npm audit, Snyk SCA, CodeQL SAST), deploy staging (automatic on main merge), deploy production (canary with manual promotion). Build optimization: pnpm store cache (lockfile hash key), Docker BuildKit with ECR cache, Nx affected commands for monorepo. GitHub Actions config: matrix builds for Node 18/20, self-hosted runners (c6i.xlarge) for production deploys. Quality gates: 80% coverage (Jest), 0 critical vulnerabilities, all contract tests pass. Canary deployment: Argo Rollouts with 5% → 25% → 100% over 45 minutes, Prometheus metrics analysis (error rate <0.5%, latency p99 <200ms), automated rollback on SLO breach. Results: 7.5 minute average build, 12 deploys/day, 99.7% success rate, 8 minute MTTR.

### Example 2: Python ML Model Pipeline
**Prompt:** Create CI/CD pipeline for Python ML models using GitLab CI deploying to GCP Vertex AI with staged rollout achieving model validation gates and 6-hour deployment cycle.

**Expected Output:** Pipeline stages: code quality (pylint, black, mypy, pytest unit tests), data validation (Great Expectations schema checks, drift detection), model training (Vertex AI training job triggered by data or code changes), model validation (accuracy >92%, fairness metrics, comparison vs champion), staging deployment (10% traffic shadow mode), production rollout (10% → 25% → 50% → 100% over 72 hours). ML-specific gates: model metrics thresholds (precision >0.92, recall >0.88, AUC >0.95), fairness checks (demographic parity), explainability report (SHAP values), business metric simulation. Artifact management: MLflow model registry, versioned models with lineage, champion/challenger tracking. Monitoring: prediction accuracy tracking, data drift alerts (Evidently), model performance dashboard, weekly model review. Results: 6-hour deployment cycle (from 2 weeks), 23% reduction in false positives, automated rollback on quality degradation.

### Example 3: Mobile App Release Pipeline
**Prompt:** Create CI/CD pipeline for React Native app (iOS/Android) using CircleCI deploying to App Store and Google Play with phased rollout achieving weekly releases and 99.5% crash-free rate.

**Expected Output:** Pipeline stages: commit stage (yarn install, TypeScript, ESLint, Jest 3200 tests), iOS build (Xcode Cloud integration, code signing, Detox UI tests on simulators), Android build (Gradle parallel, device farm testing on BrowserStack), QA deployment (TestFlight internal + Google Play internal track). Quality gates: 85% coverage, accessibility tests (axe-core), performance tests (app launch <2s, 60fps animations), screenshot tests (Percy). Security: MobSF security audit, privacy manifest validation, SSL pinning verification. Release strategy: TestFlight beta (500 external testers, 72-hour soak), App Store phased release (1% → 10% → 50% → 100% over 7 days), Google Play staged rollout (5% → 20% → 100%). Monitoring: Crashlytics integration, ANR tracking, app rating monitoring, in-app analytics validation. Results: weekly releases (from monthly), 99.8% crash-free rate, 4.7 star rating (from 4.2), critical fixes deployed in 3 hours.

---

## Cross-References

- [Infrastructure as Code](infrastructure-as-code.md) - Terraform/Pulumi patterns for environment provisioning
- [Container Orchestration](container-orchestration.md) - Kubernetes deployment strategies and configurations
- [Cloud Architecture Framework](cloud-architecture-framework.md) - Cloud infrastructure patterns supporting CI/CD
