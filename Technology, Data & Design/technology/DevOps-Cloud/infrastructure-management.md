---
category: technology
related_templates:
- technology/DevOps-Cloud/cloud-architecture.md
- technology/DevOps-Cloud/devops-infrastructure-as-code.md
- technology/DevOps-Cloud/site-reliability-engineering.md
tags:
- infrastructure-management
- provisioning
- auto-scaling
- capacity-planning
title: Infrastructure Management
use_cases:
- Managing cloud and hybrid infrastructure at scale with automated provisioning, configuration management, and self-service capabilities
- Implementing auto-scaling strategies based on CPU, memory, and custom metrics achieving 70% cost efficiency with <5 minute scale response
- Establishing maintenance operations including automated patching, backup procedures, and disaster recovery with <1 hour RTO
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: infrastructure-management
---

# Infrastructure Management

## Purpose
Comprehensive infrastructure management covering provisioning automation, scaling strategies, monitoring and observability, maintenance operations, and cost optimization for cloud, hybrid, and on-premises environments achieving operational excellence with SLA compliance.

## 🚀 Quick Infrastructure Management Prompt

> Manage infrastructure for **[APPLICATION]** on **[AWS/AZURE/GCP/HYBRID]**. Scale: **[SERVERS]** servers, **[DATABASES]** databases, **[SERVICES]** services. Provisioning: **[TERRAFORM/ANSIBLE/CLOUDFORMATION]**. Scaling: auto-scale **[MIN]-[MAX]** based on **[CPU/MEMORY/CUSTOM]** at **[THRESHOLD]**%. Monitoring: **[CLOUDWATCH/PROMETHEUS/DATADOG]** with **[ALERTING_TOOL]** alerts. Backup: **[FREQUENCY]** with **[RETENTION]** retention. DR: RPO **[MINUTES]**, RTO **[HOURS]**. Cost target: **[BUDGET]**/month.

---

## Template

Manage infrastructure for {APPLICATION_TYPE} on {PLATFORM} supporting {SCALE_REQUIREMENTS} with {AVAILABILITY_TARGET}% availability and {BUDGET} monthly budget.

**PROVISIONING AND CONFIGURATION**

Implement infrastructure as code for consistent provisioning. Terraform: declarative infrastructure definitions, state management, provider ecosystem for multi-cloud. CloudFormation/ARM: cloud-native options with deep integration, managed state. Ansible: configuration management and application deployment, agentless, idempotent playbooks. Pulumi: general-purpose languages for complex infrastructure logic. Layered approach: Terraform for infrastructure, Ansible for configuration, CI/CD for deployment.

Design self-service provisioning for developer productivity. Service catalog: pre-approved infrastructure patterns (web app, database, data pipeline) with guardrails. Portal/CLI: Backstage, ServiceNow, or custom portal for resource requests. Approval workflows: auto-approve non-production, require approval for production or cost thresholds. Quotas and limits: per-team resource quotas preventing runaway provisioning. Cost allocation: automatic tagging with team/project for chargeback visibility.

Manage configuration drift and compliance. Drift detection: scheduled terraform plan comparing actual vs desired state, alert on differences. Configuration baselines: AWS Config rules, Azure Policy, GCP Organization Policy for compliance. Remediation: auto-remediate simple drift, alert for complex changes requiring investigation. Change management: all changes through IaC, no manual console changes in production.

**SCALING STRATEGIES**

Implement horizontal scaling for stateless workloads. Auto Scaling Groups (AWS): target tracking (70% CPU), step scaling for rapid response, scheduled scaling for known patterns. Kubernetes HPA: CPU/memory metrics, custom metrics via Prometheus adapter (requests-per-second, queue depth). Scaling parameters: min instances (2 for HA), max instances (cost ceiling), desired (optimal baseline). Cooldown periods: 300 seconds scale-down (prevent thrashing), 60 seconds scale-up (respond quickly).

Configure vertical scaling for stateful workloads. Instance right-sizing: Compute Optimizer recommendations, weekly utilization reviews. Database scaling: Aurora auto-scaling for read replicas, RDS instance class upgrades during maintenance. Kubernetes VPA: automatic resource request adjustment, recommendation mode for production safety. Memory scaling: identify memory-bound applications, adjust instance types or add caching.

Implement predictive and event-driven scaling. Predictive scaling: ML-based capacity forecasting for known patterns (business hours, weekly cycles). Event-driven: scale based on SQS queue depth, Kafka consumer lag, custom business metrics. Pre-scaling: scale up before known events (marketing campaigns, product launches). Reserve capacity: maintain warm pool for rapid scale-out, balance cost vs response time.

**MONITORING AND OBSERVABILITY**

Implement comprehensive infrastructure monitoring. Metrics collection: CloudWatch agent, Prometheus node exporter, Datadog agent on all instances. Key metrics: CPU utilization, memory usage, disk I/O, network throughput, load average. Container metrics: pod CPU/memory, container restart counts, pending pods, node capacity. Database metrics: connections, query latency, replication lag, storage consumption, deadlocks.

Configure intelligent alerting with actionable thresholds. Alert tiers: critical (P1, immediate response), warning (P2, business hours), informational (tracked, no page). Threshold tuning: static thresholds for known limits, anomaly detection for variable workloads. Alert fatigue prevention: proper severity classification, alert aggregation, meaningful alert names. Escalation paths: PagerDuty/Opsgenie for on-call, Slack for non-urgent, auto-acknowledge on recovery.

Build operational dashboards for visibility. NOC dashboard: high-level system health, active incidents, deployment status, cost tracking. Service dashboards: per-service metrics (latency, error rate, throughput), SLI/SLO tracking. Infrastructure dashboard: resource utilization, capacity headroom, scaling activity, cost trends. Executive dashboard: availability metrics, incident summary, cost vs budget, capacity projections.

Implement centralized logging for troubleshooting. Log aggregation: CloudWatch Logs, Elasticsearch/OpenSearch, Loki for cost-effective storage. Structured logging: JSON format with consistent fields (timestamp, service, level, trace_id). Log retention: 7 days hot storage (fast search), 30-90 days warm, archive to S3/Glacier for compliance. Log analysis: automated pattern detection, error rate tracking, security event correlation.

**MAINTENANCE OPERATIONS**

Establish automated patch management. Patch cadence: security patches within 48 hours (critical), monthly patch cycles (standard), quarterly for stable systems. AWS Systems Manager: Patch Manager for automated patching, maintenance windows, compliance reporting. Rolling updates: patch instances in batches maintaining availability, health check between batches. Testing pipeline: patch dev first, promote to staging after 24 hours, production after 72 hours validation.

Implement comprehensive backup strategy. Backup types: daily automated snapshots (databases, volumes), continuous replication (critical data), configuration backups (IaC repo). Retention policy: 7 days for rapid recovery, 30 days for month-end, 1 year for compliance, indefinite for legal hold. Cross-region backups: replicate critical backups to DR region, verify restoration capability. Backup verification: monthly restoration tests, automated integrity checks, documented recovery procedures.

Design disaster recovery procedures. DR strategy: pilot light (minimal infrastructure in DR region, scale up on failover), warm standby (reduced capacity running). RTO/RPO targets: critical systems (RTO <1 hour, RPO <15 minutes), standard (RTO <4 hours, RPO <1 hour). Failover automation: Route 53 health checks with automatic DNS failover, database promotion scripts. DR testing: quarterly failover drills, document actual RTO/RPO, update runbooks based on findings.

Manage maintenance windows effectively. Change windows: Tuesday/Thursday 2-6 AM UTC for standard changes, any time with approval for emergencies. Communication: stakeholder notification 48 hours before planned maintenance, status page updates during. Rollback plan: every change has documented rollback procedure, tested before execution. Freeze periods: no changes during peak business periods, Black Friday, end-of-quarter.

**CAPACITY PLANNING**

Forecast capacity requirements proactively. Utilization analysis: weekly/monthly reports on CPU, memory, storage consumption trends. Growth modeling: linear extrapolation for steady growth, event-based modeling for step changes. Lead time planning: 4-week lead time for reserved capacity, 2-week for on-demand expansion. Budget correlation: capacity plans aligned with financial planning cycles.

Optimize resource utilization for cost efficiency. Right-sizing: Compute Optimizer recommendations, target 60-70% average utilization. Reserved capacity: 1-year reservations for baseline (30% savings), 3-year for stable workloads (60% savings). Spot instances: batch processing, CI/CD, non-critical dev workloads (60-90% savings). Idle resource cleanup: automated identification and termination of unused resources.

Plan for growth and peak events. Capacity buffer: maintain 30% headroom for organic growth, additional for planned events. Event scaling: pre-scale infrastructure before known high-traffic events, auto-scale during unknown spikes. Database capacity: plan storage growth, connection pool sizing, read replica scaling. Network capacity: bandwidth planning, CDN for traffic offload, multi-region for geographic distribution.

**COST MANAGEMENT**

Implement FinOps practices for cost visibility. Tagging strategy: mandatory tags (Environment, Owner, CostCenter, Application) enforced by policy. Cost allocation: detailed cost breakdown by team/service/environment, showback/chargeback reports. Budget alerts: 80% warning, 100% alert, 120% escalation to leadership. Anomaly detection: CloudWatch anomaly detection for cost, investigate spikes immediately.

Optimize costs continuously. Reserved capacity: analyze usage patterns, commit to reservations for steady-state workloads. Spot/preemptible: use for fault-tolerant workloads, implement graceful handling of interruptions. Storage tiering: S3 Intelligent-Tiering, lifecycle policies for automatic tier transitions. Cleanup automation: Lambda/scheduled jobs to terminate unused resources, orphaned volumes, old snapshots.

Deliver infrastructure management as:

1. **PROVISIONING AUTOMATION** - IaC templates, self-service catalog, approval workflows, drift detection

2. **SCALING CONFIGURATION** - Auto-scaling policies, scaling metrics, thresholds, cooldown periods

3. **MONITORING SETUP** - Metrics collection, dashboards, alerting rules, escalation paths

4. **MAINTENANCE PROCEDURES** - Patching schedule, backup strategy, DR procedures, change windows

5. **CAPACITY PLAN** - Utilization analysis, growth forecasts, reserved capacity recommendations

6. **COST OPTIMIZATION** - Right-sizing recommendations, reserved instance analysis, cleanup automation

---

## Usage Examples

### Example 1: E-commerce Platform Infrastructure
**Prompt:** Manage infrastructure for EcommercePlatform on AWS supporting 500 EC2 instances, 10 RDS databases, 50 microservices with 99.9% availability and $150K/month budget.

**Expected Output:** Provisioning: Terraform modules for VPC, ECS, RDS, organized by environment (dev/staging/prod), GitHub Actions for CI/CD with plan on PR and apply on merge. Self-service: Backstage portal for new service provisioning, pre-approved templates for ECS services, approval required for RDS creation. Scaling: ECS auto-scaling (target tracking 70% CPU, min 2 max 50 tasks), RDS read replica auto-scaling, KEDA for event-driven scaling on order processing queue. Monitoring: Datadog for unified observability, custom dashboards per service team, PagerDuty integration with 3-tier escalation, SLO tracking (99.9% availability, p99 <500ms). Maintenance: AWS Systems Manager for patching (weekly dev, monthly prod), AWS Backup for daily snapshots (35-day retention), cross-region DR (pilot light in us-west-2). Capacity: monthly utilization reviews, Compute Optimizer for right-sizing, 40% reserved instances for baseline. Cost: $145K/month (compute $80K, database $35K, network $15K, storage $10K, other $5K), 15% savings potential from right-sizing and reservations.

### Example 2: Healthcare Data Platform
**Prompt:** Manage infrastructure for HealthDataPlatform on Azure supporting 200 VMs, 5 SQL databases, data lake with HIPAA compliance, <1 hour RTO.

**Expected Output:** Provisioning: Terraform with Azure provider, Azure DevOps pipelines, separate subscriptions per environment, Azure Policy for HIPAA compliance guardrails. Configuration: Ansible for VM configuration, Azure Automation for DSC, Azure Key Vault for secrets. Scaling: VM Scale Sets with custom health probes, Azure SQL elastic pools for database scaling, Azure Data Factory auto-scaling for ETL. Monitoring: Azure Monitor with Log Analytics, custom workbooks for compliance dashboards, Azure Sentinel for security monitoring, ServiceNow integration for incident management. Maintenance: Azure Update Management for patching (security within 48 hours, monthly standard), Azure Backup with GRS (daily, 30-day retention, yearly archives), Azure Site Recovery for VM replication (RPO 15 minutes). Compliance: encryption at rest (customer-managed keys), encryption in transit (TLS 1.2+), audit logging to immutable storage, access reviews quarterly. DR: warm standby in paired region, automated failover for SQL (auto-failover groups), VM recovery within 1 hour via Site Recovery. Cost: $120K/month, reserved instances for 60% of compute, Azure Hybrid Benefit for Windows licensing.

### Example 3: Startup SaaS Platform
**Prompt:** Manage infrastructure for SaaSSatrup on GCP supporting 50 GKE nodes, Cloud SQL, with rapid scaling requirements and $30K/month budget constraint.

**Expected Output:** Provisioning: Terraform with GCP provider, GitHub Actions for GitOps, single project with namespace isolation for environments. Self-service: minimal overhead, developers can create namespaces with Helm templates, pre-approved patterns. Scaling: GKE cluster autoscaler (1-50 nodes), HPA for all services (70% CPU target), Cloud SQL automatic storage increase. Monitoring: Google Cloud Monitoring + Prometheus (cost-effective), Grafana dashboards, PagerDuty with Slack integration, minimal alert set (critical only). Maintenance: GKE auto-upgrade for patch versions, manual upgrades for minor versions (staged rollout), Cloud SQL automated backups (7-day retention), weekly disaster recovery to Cloud Storage. Cost optimization: preemptible nodes for 60% of capacity (70% savings), committed use discounts for baseline, spot instances for batch jobs. Capacity: lean approach, scale horizontally first, right-size monthly. DR: regional GKE cluster (survives zone failure), Cloud SQL HA, Cloud Storage multi-region for critical data. Cost: $28K/month (GKE $15K, Cloud SQL $8K, networking $3K, storage $2K), optimized for startup budget with room for 50% growth.

---

## Cross-References

- [Cloud Architecture](cloud-architecture.md) - Cloud infrastructure design patterns
- [Infrastructure as Code](devops-infrastructure-as-code.md) - IaC implementation with Terraform/Pulumi
- [Site Reliability Engineering](site-reliability-engineering.md) - SRE practices for reliability
