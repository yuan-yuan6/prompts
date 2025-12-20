---
category: technology
related_templates:
- technology/DevOps-Cloud/ci-cd-pipelines.md
- technology/DevOps-Cloud/container-orchestration.md
- technology/DevOps-Cloud/site-reliability.md
tags:
- platform-engineering
- developer-experience
- internal-developer-platform
- golden-paths
title: Platform Engineering & Developer Experience
use_cases:
- Building internal developer platforms with self-service infrastructure, golden paths, and service catalogs reducing time-to-production from weeks to hours
- Implementing developer portals (Backstage/Port) with service discovery, documentation, and API catalogs achieving 90%+ developer satisfaction
- Measuring and improving DORA metrics (deployment frequency, lead time, MTTR, change failure rate) targeting elite performance levels
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: platform-engineering
---

# Platform Engineering & Developer Experience

## Purpose
Design and implement internal developer platforms providing self-service infrastructure, golden paths, observability, and developer tools achieving elite DORA metrics (multiple deploys/day, <1 hour lead time, <1 hour MTTR, <5% change failure rate) while maximizing developer productivity and satisfaction.

## Template

Design internal developer platform for {ORGANIZATION} supporting {DEVELOPER_COUNT} developers across {TEAM_COUNT} teams achieving {DORA_TARGETS} DORA metrics with {SATISFACTION_TARGET} developer NPS.

**PLATFORM ARCHITECTURE**

Design platform layers enabling self-service while maintaining guardrails. Infrastructure layer: Kubernetes clusters, databases, storage, networking provisioned via Terraform modules with approval workflows. Platform services layer: CI/CD, observability, security scanning, secret management as shared capabilities. Developer interface layer: portal for discovery and self-service, CLI for power users, APIs for automation. Abstraction principle: hide complexity from developers, expose only what they need, maintain escape hatches for advanced use cases.

Choose developer portal technology matching team size and requirements. Backstage: open-source, extensible plugin ecosystem, requires engineering investment, best for 100+ developers. Port: managed platform, faster setup, less customization, good for 50-500 developers. Custom portal: maximum flexibility, highest engineering cost, justified only for unique requirements. Portal components: service catalog (discover all services), documentation (TechDocs), API catalog (OpenAPI specs), scaffolder (create new services from templates).

Implement platform-as-product mindset for sustainable platform development. Platform team structure: 1 platform engineer per 50-100 developers, product manager for roadmap, embedded SRE for reliability. User research: quarterly developer surveys, NPS tracking, support ticket analysis, usage analytics. Roadmap prioritization: balance quick wins (high impact, low effort) with strategic capabilities. Feedback loops: weekly office hours, Slack channel for support, feature request tracking.

**GOLDEN PATHS AND SERVICE TEMPLATES**

Create standardized templates reducing time-to-production. Microservice template: language-specific boilerplate (Node.js, Python, Go, Java), pre-configured CI/CD pipeline, observability instrumentation (metrics, logs, traces), security scanning enabled, Kubernetes manifests, documentation structure. Time to production: <30 minutes from template to running service in staging. Template coverage: target 80% of new services using golden paths, allow exceptions with justification.

Design templates for common workload patterns. API service: OpenAPI specification, authentication middleware, rate limiting, API gateway integration, contract testing. Frontend application: React/Vue/Next.js scaffold, CDN integration, performance monitoring, feature flags, A/B testing setup. Data pipeline: Airflow/Dagster DAG structure, data quality checks, lineage tracking, cost monitoring. Event-driven service: message queue integration, dead letter handling, idempotent processing, event schema registry.

Maintain templates with versioning and migration paths. Semantic versioning: major for breaking changes, minor for features, patch for fixes. Migration guides: document upgrade path between versions, automate where possible. Deprecation policy: 6-month notice before removing template versions, support n-1 version. Template testing: automated tests validating templates work as expected, security scanning on template code.

**SELF-SERVICE INFRASTRUCTURE**

Enable infrastructure provisioning without tickets. Compute resources: Kubernetes namespaces (<5 minutes), EKS clusters (<30 minutes), serverless functions (<5 minutes). Databases: RDS instances (<30 minutes), Aurora clusters (<1 hour), Redis clusters (<15 minutes). Storage: S3 buckets (<5 minutes), EFS mounts (<15 minutes). Networking: VPC peering (<30 minutes), security groups (<5 minutes). Approval workflows: auto-approve non-production, require approval for production or cost exceeding thresholds.

Implement guardrails preventing misuse while enabling speed. Resource quotas: per-team limits on compute, storage, database instances. Cost controls: budget alerts, approval required above thresholds, automatic recommendations for right-sizing. Security policies: OPA/Gatekeeper policies enforcing encryption, network isolation, approved configurations. Compliance automation: automatic tagging, audit logging, compliance reporting.

Build infrastructure catalog for discoverability. Resource documentation: what each resource type provides, when to use it, cost estimates. Provisioning guides: step-by-step instructions, common configurations, troubleshooting. Dependencies: show relationships between resources, impact of changes. Cost transparency: real-time cost per team/service, optimization recommendations.

**CI/CD PLATFORM**

Provide standardized pipelines as platform capability. Pipeline templates: language-specific build, test, security scan, deploy stages. Reusable components: shared actions/steps for common tasks (Docker build, Helm deploy, Terraform apply). Self-service pipeline creation: developers select template, configure parameters, pipeline auto-created. Pipeline time targets: <10 minutes for most builds, <5 minutes for incremental changes.

Integrate security scanning into developer workflow. Dependency scanning: Snyk/Dependabot on every commit, block on critical vulnerabilities. SAST: SonarQube/CodeQL on pull requests, quality gates enforced. Container scanning: Trivy on image build, fail build on critical CVEs. IaC scanning: tfsec/Checkov on infrastructure changes. Secret detection: GitLeaks pre-commit and in CI.

Enable progressive delivery reducing deployment risk. Feature flags: LaunchDarkly/Unleash integration, percentage rollouts, kill switches. Canary deployments: Argo Rollouts/Flagger for automated canary analysis. Blue-green: instant rollback capability for critical services. Deployment tracking: link deployments to commits, automatic release notes.

**OBSERVABILITY PLATFORM**

Provide auto-instrumented observability as default. Metrics: OpenTelemetry auto-instrumentation, Prometheus collection, standard dashboards per service. Logs: structured JSON logging library, centralized aggregation (Loki/Elasticsearch), correlation IDs. Traces: distributed tracing auto-enabled, Jaeger/Tempo backend, trace-to-logs linking. Zero-config goal: services get observability without developer effort.

Build observability into developer workflow. Service dashboards: auto-generated per service showing golden signals, customizable. Alert templates: standard alert rules for latency, error rate, saturation. On-call integration: PagerDuty/Opsgenie routing from platform, runbook links in alerts. Debugging tools: trace exploration, log search, metric correlation in single interface.

Provide cost-effective observability at scale. Retention tiers: 7 days hot (fast query), 30 days warm, 1 year cold archive. Sampling strategies: 100% for errors, 10% for normal traffic, adaptive sampling for high-volume services. Cardinality management: label guidelines preventing metric explosion, automated cardinality alerts. Cost allocation: observability cost per team/service, optimization recommendations.

**DEVELOPER PRODUCTIVITY METRICS**

Track DORA metrics as platform health indicators. Deployment frequency: target multiple deploys per day per service, track trend over time. Lead time for changes: commit to production, target <1 hour for elite, <1 day for high. Mean time to recovery: incident detection to resolution, target <1 hour. Change failure rate: deployments causing incidents, target <5%. Measurement: automated from CI/CD and incident systems, no manual reporting.

Measure developer experience beyond DORA. Developer satisfaction: quarterly NPS survey, target >50 (excellent). Time to productivity: new hire first PR to production, target <1 week. Cognitive load: tools learned to be productive, target single portal for 80% of tasks. Support ticket volume: requests to platform team, target reduction as self-service improves. Platform adoption: percentage of teams using platform capabilities.

Use metrics to drive platform investment. Correlation analysis: which platform capabilities improve DORA metrics most. ROI calculation: developer time saved × hourly cost vs platform investment. Bottleneck identification: where developers spend time waiting (approvals, builds, deployments). Prioritization framework: impact (developer hours saved) × reach (teams affected) / effort.

**PLATFORM ADOPTION AND ENABLEMENT**

Drive adoption through developer enablement. Onboarding program: new hire platform training in first week, guided first deployment. Documentation: getting started guides, API references, troubleshooting, video tutorials. Office hours: weekly drop-in sessions for questions and support. Champions program: platform advocates in each team, early access to features, feedback channel.

Support migration from legacy systems. Migration paths: documented steps from Jenkins/custom tooling to platform CI/CD. Coexistence: platform works alongside legacy systems during transition. Incentives: teams migrating get priority support, early access to new features. Success stories: showcase teams that migrated, quantify benefits.

Build community around platform. Internal tech talks: monthly demos of platform features, customer success stories. Feedback mechanisms: feature request voting, public roadmap, regular updates. Contribution model: teams can contribute plugins/templates, review and merge process. Recognition: highlight teams with great platform usage, share best practices.

Deliver platform engineering as:

1. **PLATFORM ARCHITECTURE** - Layer diagram, component selection, integration patterns, technology choices

2. **GOLDEN PATHS** - Service templates for each workload type, scaffolding tools, template versioning

3. **SELF-SERVICE CATALOG** - Infrastructure offerings, provisioning workflows, approval policies, guardrails

4. **CI/CD PLATFORM** - Pipeline templates, security integration, deployment strategies, metrics

5. **OBSERVABILITY STACK** - Auto-instrumentation, dashboards, alerting, cost management

6. **METRICS FRAMEWORK** - DORA tracking, developer experience metrics, platform adoption KPIs

7. **ENABLEMENT PROGRAM** - Onboarding, documentation, training, community building

---

## Usage Examples

### Example 1: Enterprise Platform (5000+ Developers)
**Prompt:** Design IDP for TechCorp with 5000 developers across 200 teams managing 1500 microservices targeting elite DORA metrics and 70+ developer NPS.

**Expected Output:** Platform architecture: multi-cluster Kubernetes (EKS) across 3 regions, shared platform services (CI/CD, observability, security), Backstage developer portal with 15 custom plugins. Golden paths: 5 templates (Node.js API, Python ML service, React frontend, Kafka consumer, data pipeline), 85% adoption, <30 min time-to-production. Self-service: infrastructure provisioned via ServiceNow + Terraform, <15 min for namespaces, <1 hour for databases, OPA policies for security/cost guardrails. CI/CD: GitHub Actions with reusable workflows, 8-minute average build time, Argo Rollouts for canary deployments. Observability: OpenTelemetry auto-instrumentation, Prometheus + Grafana + Tempo, $200K/month optimized from $350K via sampling. DORA: 15 deploys/day/team, 45-minute lead time, 35-minute MTTR, 3% change failure rate. Team: 50 platform engineers (1:100 ratio), 3 PMs, dedicated SRE embedded. Developer NPS: 72 (up from 35 in Year 1). Investment: $15M/year, ROI 4x via developer productivity gains.

### Example 2: Scale-up SaaS (200 Developers)
**Prompt:** Design IDP for GrowthSaaS with 200 developers across 25 teams, AWS-native, serverless-first, targeting 10x growth with 2x platform team.

**Expected Output:** Platform architecture: AWS-native (Lambda, ECS Fargate, Aurora Serverless), single EKS cluster for stateful workloads, Port.io for developer portal (managed, faster setup than Backstage). Golden paths: 3 templates (Lambda API, Fargate service, Next.js frontend), Cookiecutter + GitHub template repos, 90% adoption. Self-service: AWS Service Catalog for infrastructure, Terraform Cloud for IaC, auto-approve non-prod with cost <$500/month. CI/CD: GitHub Actions, 5-minute average builds, feature flags via LaunchDarkly for progressive delivery. Observability: Datadog (managed, reduces ops burden), auto-instrumented APM, $50K/month cost. DORA: 8 deploys/day/team, 2-hour lead time, 45-minute MTTR, 5% change failure rate. Team: 4 platform engineers (1:50 ratio), part-time PM, 1 SRE. Developer NPS: 65. Focus: automation over customization, managed services over self-hosted, scale-ready from day 1.

### Example 3: Digital Transformation (500 Developers)
**Prompt:** Design IDP for TradCorp transitioning 500 developers from monolith to microservices over 3 years with focus on culture change and skills development.

**Expected Output:** Platform architecture: hybrid cloud (on-prem VMware + AWS), progressive Kubernetes adoption, Backstage with gradual feature rollout. Golden paths: start with 2 templates (Java Spring Boot migration, new Node.js services), add templates as patterns emerge. Self-service: phased approach—Year 1 streamlined tickets (<24 hour), Year 2 portal-based with approval, Year 3 full self-service. CI/CD: Jenkins (existing) → GitLab CI migration, parallel operation during transition, migration incentives for early adopters. Observability: Prometheus + Grafana (open source, team skilled), migrate from legacy monitoring. DORA baseline: monthly deploys, 6-week lead time, 2-day MTTR, 20% change failure rate. DORA Year 3 target: weekly deploys, 1-week lead time, 4-hour MTTR, 8% change failure rate. Team: start with 6 platform engineers, grow to 12 by Year 3, heavy investment in training (platform champions per team). Developer NPS: Year 1 target 40 (from 15), Year 3 target 60. Focus: change management, skills development, incremental wins.

---

## Cross-References

- [CI/CD Pipelines](../DevOps-Cloud/ci-cd-pipelines.md) - Pipeline patterns for platform CI/CD
- [Container Orchestration](../DevOps-Cloud/container-orchestration.md) - Kubernetes platform layer
- [Site Reliability](../DevOps-Cloud/site-reliability.md) - SRE practices for platform reliability
