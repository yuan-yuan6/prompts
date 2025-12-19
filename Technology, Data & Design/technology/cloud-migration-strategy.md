---
category: technology
related_templates:
- technology/DevOps-Cloud/cloud-architecture.md
- technology/DevOps-Cloud/devops-infrastructure-as-code.md
- technology/DevOps-Cloud/ci-cd-pipelines.md
tags:
- cloud-migration
- rehost-refactor
- landing-zone
- lift-and-shift
title: Cloud Migration Strategy
use_cases:
- Planning and executing cloud migrations using 7Rs framework (rehost, replatform, refactor, rebuild, replace, retain, retire) for enterprise application portfolios
- Building cloud landing zones with VPC design, IAM baseline, security controls, and compliance automation enabling secure workload migration
- Managing wave-based migration execution with pilot validation, rollback procedures, and cutover planning achieving <1 hour RTO
industries:
- technology
- financial-services
- healthcare
- government
- retail
type: framework
difficulty: intermediate
slug: cloud-migration-strategy
---

# Cloud Migration Strategy

## Purpose
Plan and execute cloud migration initiatives covering assessment, migration patterns (7Rs), landing zone setup, wave-based execution, security implementation, and operational transformation achieving cost reduction, improved agility, and compliance requirements.

## 🚀 Quick Cloud Migration Prompt

> Plan migration of **[APP_COUNT]** applications, **[DATA_VOLUME]** data to **[AWS/AZURE/GCP]** over **[MONTHS]** months. Pattern mix: **[X%]** rehost, **[Y%]** replatform, **[Z%]** refactor. Build landing zone: VPC, IAM, security baseline, monitoring. Execute: pilot (**[2-3]** apps) → waves (**[20-30]** apps each). Target: **[X%]** cost reduction, **[Y%]** availability. Include: rollback plan, success criteria, decommissioning.

---

## Template

Execute cloud migration for {ORGANIZATION} migrating {APPLICATION_COUNT} applications, {DATA_VOLUME} data to {CLOUD_PROVIDER} achieving {COST_TARGET}% cost reduction, {AVAILABILITY_TARGET}% availability over {TIMELINE} timeline.

**MIGRATION ASSESSMENT**

Conduct application portfolio analysis for migration planning. Discovery: inventory all applications (name, owner, technology stack, dependencies, data stores), use automated tools (AWS Migration Hub, Azure Migrate, CloudHealth) for accuracy. Dependency mapping: identify upstream/downstream dependencies, integration points, shared databases, network requirements. Business criticality: classify as critical (revenue-generating, customer-facing), important (internal operations), or low (development, testing). Technical complexity: assess cloud readiness, architectural constraints, compliance requirements.

Score applications for migration priority. Readiness factors: cloud-compatible technology (containerized, stateless), minimal dependencies, modern architecture. Risk factors: legacy technology, complex integrations, compliance constraints, data sensitivity. Business factors: strategic importance, transformation opportunity, cost reduction potential. Prioritization matrix: high readiness + low risk + high business value = early migration candidates.

Define success criteria and migration timeline. Phase structure: foundation (2-3 months), pilot (1-2 months), waves (6-12 months), optimization (ongoing). Milestones: landing zone operational, pilot validation complete, 50% migrated, 100% migrated, decommissioning complete. KPIs: applications migrated per month, cost savings realized, availability achieved, incidents per migration.

**MIGRATION PATTERNS (7Rs)**

Select migration strategy matching application characteristics and business goals. Rehost (lift-and-shift): move VMs as-is to cloud, fastest option (2-4 weeks per app), minimal changes, 10-30% cost savings from infrastructure efficiency. Best for: legacy applications with short remaining lifespan, quick wins, applications with minimal technical debt. Tools: AWS MGN, Azure Migrate, GCP Migrate for Compute Engine.

Replatform (lift-tinker-and-shift): minimal changes to leverage managed services, moderate effort (4-8 weeks), 30-50% cost savings. Common changes: move to managed database (RDS instead of self-managed), containerize (ECS/EKS), use managed load balancing. Best for: database-heavy applications, applications that benefit from managed services without redesign.

Refactor (re-architect): redesign for cloud-native, significant effort (3-6 months), highest long-term value, 50-70% cost savings plus scalability. Approach: decompose monoliths to microservices, implement serverless where appropriate, redesign for horizontal scaling. Best for: strategic applications, high-growth workloads, applications with scalability limitations.

Rebuild: rewrite from scratch using cloud-native technologies, major effort (6-12 months), fresh architecture. When appropriate: legacy technology with no migration path, applications requiring fundamental capability changes. Risk mitigation: parallel operation during transition, phased feature migration.

Replace: substitute with SaaS solution, eliminates maintenance burden. Candidates: commodity functions (CRM, ERP, HR systems), applications with mature SaaS alternatives. Considerations: data migration, integration requirements, vendor lock-in, total cost of ownership.

Retain: keep on-premises for valid reasons. Reasons: regulatory requirements prohibiting cloud, recent major investment, pending retirement. Strategy: hybrid architecture with cloud connectivity, plan for eventual migration.

Retire: decommission applications no longer needed. Identification: low usage applications, redundant systems, end-of-life software. Process: data archival, user communication, license termination, cost elimination.

**LANDING ZONE SETUP**

Build cloud foundation enabling secure migration. Account structure: multi-account strategy (AWS Organizations, Azure Management Groups), separate accounts for workloads (production, staging, development), shared services (networking, security), and sandbox. Organizational units: group accounts by environment, business unit, or compliance requirement. Service control policies: preventive guardrails (restrict regions, block public resources, enforce encryption).

Configure networking for connectivity and isolation. VPC design: hub-and-spoke topology with Transit Gateway, dedicated VPCs for production/non-production, CIDR planning for growth. Connectivity: Direct Connect/ExpressRoute for on-premises (dedicated bandwidth, consistent latency), VPN backup for redundancy. Subnets: public (load balancers, NAT), private (applications), isolated (databases), across multiple AZs. Egress control: NAT Gateway for outbound, VPC endpoints for AWS services (S3, DynamoDB), firewall for inspection.

Implement security baseline before workload migration. Identity: SSO integration with corporate directory, federated access, MFA enforced. IAM: permission boundaries, role-based access (admin, developer, readonly), service accounts with least privilege. Encryption: KMS for data at rest, TLS 1.2+ in transit, certificate management. Logging: CloudTrail for API calls, VPC Flow Logs for network, centralized logging account. Monitoring: GuardDuty for threat detection, Security Hub for findings aggregation, Config for compliance.

Deploy operational tooling for day-2 readiness. Monitoring: CloudWatch dashboards, cross-account observability, alerting to on-call. Cost management: budget alerts, cost allocation tags (mandatory: environment, team, application), Cost Explorer access. Backup: AWS Backup policies, cross-region replication for critical data, tested restore procedures. Deployment: CI/CD pipelines (CodePipeline, GitHub Actions), infrastructure as code (Terraform, CloudFormation).

**DATA MIGRATION STRATEGY**

Choose data migration method matching volume and downtime tolerance. Online migration: continuous replication with minimal downtime, use AWS DMS, Azure Database Migration Service. Approach: initial full load, ongoing CDC (change data capture), cutover when replication lag acceptable (<1 minute). Offline migration: bulk transfer for large datasets, use Snowball/Snowmobile for PB-scale, scheduled transfer windows.

Plan database migration with appropriate tooling. Homogeneous (same engine): native replication, simpler migration, minimal transformation. Heterogeneous (engine change): schema conversion (AWS SCT, Azure Database Migration), code remediation, testing critical. Common patterns: Oracle to PostgreSQL (cost reduction), SQL Server to Aurora (managed service), MongoDB to DocumentDB.

Handle storage migration efficiently. File storage: DataSync for continuous sync, Transfer Family for SFTP workflows, Storage Gateway for hybrid. Object storage: S3 batch operations for large migrations, cross-region replication, lifecycle policies from day one. Data validation: row counts, checksums, sample data comparison, application-level validation.

**WAVE-BASED EXECUTION**

Execute pilot migration validating approach. Pilot selection: 3-5 low-risk applications, representative of portfolio, willing application owners. Validation: functional testing, performance comparison, security assessment, user acceptance. Lessons learned: document issues encountered, refine runbooks, update timeline estimates. Success criteria: applications running stable for 2 weeks, performance within 10% of baseline, no critical issues.

Plan production waves with increasing complexity. Wave structure: 20-30 applications per wave, 4-6 week duration, grouped by dependencies or business domain. Wave 1: quick wins (high readiness, low complexity), build team confidence, refine processes. Wave 2-N: progressively complex applications, critical workloads in later waves. Dependencies: migrate dependent applications together, coordinate cutover windows.

Implement cutover procedures minimizing risk. Pre-cutover: final data sync, DNS TTL reduction, stakeholder communication. Cutover window: typically weekend (48 hours), defined go/no-go criteria, rollback decision point. Validation: smoke tests, health checks, performance validation, user acceptance. Rollback: keep source running (7-14 days), DNS failback capability, data sync for write-back if needed.

**SECURITY AND COMPLIANCE**

Map compliance requirements to cloud controls. Framework mapping: SOC 2 → AWS Config rules, PCI-DSS → encryption + network isolation, HIPAA → BAA + PHI protection. Evidence collection: automated compliance reporting (AWS Audit Manager, Azure Compliance Center), continuous monitoring. Audit preparation: documentation of controls, access logs, change records, incident response procedures.

Implement zero-trust security architecture. Identity-first: verify every access request, no implicit trust based on network location. Micro-segmentation: security groups per workload, explicit allow rules, default deny. Continuous verification: session monitoring, anomaly detection, re-authentication for sensitive operations. Data protection: encryption everywhere, classification-based access controls, DLP for sensitive data.

**OPERATIONAL TRANSFORMATION**

Transform operations alongside migration. Traditional to cloud operations: shift from ticket-based to self-service, from manual to automated, from reactive to proactive. SRE practices: SLOs for all services, error budgets, blameless postmortems. Automation priority: infrastructure provisioning (100% IaC), deployments (CI/CD), incident response (runbook automation).

Build cloud skills across organization. Training paths: cloud certifications (Solutions Architect, DevOps Engineer, Security Specialty), hands-on labs. Centers of excellence: cloud platform team providing guidance, reusable patterns, enablement. Community: internal knowledge sharing, lunch-and-learns, migration retrospectives.

**COST MANAGEMENT AND OPTIMIZATION**

Implement FinOps from migration start. Tagging strategy: mandatory tags (environment, team, cost-center, application) enforced by policy. Cost visibility: per-application cost tracking, showback reports, budget vs actual. Optimization cadence: weekly utilization review, monthly right-sizing, quarterly reserved capacity assessment.

Optimize costs progressively. Migration phase: focus on functional success, accept temporary inefficiency. Stabilization phase: right-size instances based on actual usage, implement auto-scaling. Optimization phase: reserved instances for stable workloads (30-50% savings), spot for fault-tolerant (60-90% savings). Continuous: Compute Optimizer recommendations, storage tiering, architecture improvements.

Deliver cloud migration as:

1. **ASSESSMENT REPORT** - Application inventory, readiness scores, migration patterns, prioritized roadmap

2. **LANDING ZONE DESIGN** - Account structure, networking, security baseline, operational tooling

3. **MIGRATION PATTERNS** - Per-application migration strategy (7Rs), effort estimates, dependencies

4. **DATA MIGRATION PLAN** - Database migration approach, storage migration, validation procedures

5. **WAVE PLAN** - Wave groupings, timelines, cutover procedures, rollback plans

6. **SECURITY CONTROLS** - Compliance mapping, security architecture, monitoring setup

7. **OPERATIONAL READINESS** - Runbooks, training plan, support model, cost management

---

## Usage Examples

### Example 1: Enterprise Financial Services Migration
**Prompt:** Plan migration of 200 applications, 500TB data to AWS over 18 months for FinanceCorp achieving 35% cost reduction, 99.99% availability with SOC 2 and PCI-DSS compliance.

**Expected Output:** Assessment: 200 applications inventoried (120 Java/.NET, 50 legacy COBOL/mainframe, 30 COTS), 500TB data (300TB relational, 150TB files, 50TB archive). Migration patterns: 40% rehost (legacy apps with 3-year horizon), 35% replatform (move to RDS/Aurora, containerize), 15% refactor (core banking modernization), 5% replace (HR to Workday, CRM to Salesforce), 5% retire (redundant systems). Landing zone: AWS Control Tower with 15 accounts (prod, non-prod, shared services, security, logging per BU), Transit Gateway hub-spoke, Direct Connect 10Gbps with VPN backup. Compliance: PCI-DSS network isolation (dedicated VPC for cardholder data), SOC 2 Config rules, Security Hub enabled, GuardDuty threat detection. Data migration: Oracle to Aurora PostgreSQL (AWS SCT + DMS), SQL Server to RDS (native backup/restore), file shares to S3 + FSx. Waves: pilot (5 low-risk internal apps), Wave 1-3 (non-critical internal), Wave 4-6 (customer-facing), Wave 7-8 (core systems). Timeline: landing zone (months 1-3), pilot (months 4-5), production waves (months 6-16), optimization (months 17-18). Cost: $15M migration investment, $8M annual savings (35% reduction), 2-year payback.

### Example 2: Healthcare SaaS Platform Migration
**Prompt:** Plan migration of 50 applications, 100TB data to GCP over 12 months for HealthTech achieving HIPAA compliance and 10x scalability for growth.

**Expected Output:** Assessment: 50 applications (monolithic .NET platform, microservices APIs, data analytics), 100TB (patient data, imaging, analytics). Migration patterns: 60% refactor (decompose monolith to microservices on GKE), 30% replatform (databases to Cloud SQL, storage to Cloud Storage), 10% rebuild (real-time analytics on BigQuery). Landing zone: GCP organization with folders (prod, non-prod, shared), hub-spoke VPC with Cloud NAT, Cloud Interconnect for customer connectivity. HIPAA compliance: BAA with GCP, encryption with CMEK, VPC Service Controls for PHI perimeter, Access Transparency logging, DLP API for PHI scanning. Data migration: SQL Server to Cloud SQL (DMS), blob storage to Cloud Storage with gsutil, BigQuery for analytics warehouse. Architecture: GKE Autopilot for microservices, Cloud Run for APIs, Cloud SQL HA for transactional, BigQuery for analytics. Scalability: horizontal auto-scaling (2 to 200 pods), multi-region deployment (us-east, us-west), global load balancing. Timeline: landing zone (months 1-2), pilot microservices (months 3-4), core platform migration (months 5-9), analytics migration (months 10-12). Cost: $3M migration, enables 10x customer growth without infrastructure rebuild.

### Example 3: Government Agency Cloud Modernization
**Prompt:** Plan migration of 150 applications to Azure Government over 24 months for FedAgency achieving FedRAMP High compliance with zero-trust architecture.

**Expected Output:** Assessment: 150 applications (80 legacy .NET, 40 COTS, 30 custom), FedRAMP High authorization required, classified data handling, air-gapped requirements for some systems. Migration patterns: 50% rehost (COTS and stable legacy), 30% replatform (modernize .NET to containers), 10% replace (move to FedRAMP-authorized SaaS), 5% rebuild (citizen-facing portals), 5% retain (classified systems on-prem). Landing zone: Azure Government with management groups aligned to agency structure, Azure Policy for FedRAMP High controls, Azure Blueprint for consistent deployments. Zero-trust: Azure AD with CAC/PIV authentication, Conditional Access policies, micro-segmentation with NSGs, Azure Bastion for admin access, no persistent VPN. FedRAMP High: 421 controls mapped, continuous monitoring (Azure Security Center), POA&M tracking, 3PAO assessment coordination. Connectivity: ExpressRoute to agency data centers, Azure Government Secret regions for classified spillover. Data: SQL Server to Azure SQL MI (backup/restore), file shares to Azure Files, Azure Blob with government region replication. Waves: 24-month program in 6-month phases (foundation, pilot, production waves 1-3, optimization). Security: Azure Sentinel SIEM, Microsoft Defender for Cloud, Key Vault with HSM, FIPS 140-2 validated encryption. Cost: $20M over 24 months, $5M annual savings, improved security posture, modern citizen services.

---

## Cross-References

- [Cloud Architecture](DevOps-Cloud/cloud-architecture.md) - Target cloud architecture patterns
- [Infrastructure as Code](DevOps-Cloud/devops-infrastructure-as-code.md) - IaC for landing zone and workload deployment
- [CI/CD Pipelines](DevOps-Cloud/ci-cd-pipelines.md) - Deployment automation for migrated workloads
