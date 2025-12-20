---
category: technology
related_templates:
- technology/DevOps-Cloud/infrastructure-as-code.md
- technology/DevOps-Cloud/container-orchestration.md
- technology/DevOps-Cloud/cloud-migration-strategy.md
tags:
- cloud-architecture
- aws-azure-gcp
- vpc-design
- cost-optimization
title: Cloud Architecture Design
use_cases:
- Designing multi-tier cloud architectures on AWS/Azure/GCP achieving 99.99% availability with auto-scaling, disaster recovery, and cost optimization
- Building secure cloud networks with VPC design, security groups, WAF, and compliance controls meeting SOC2/HIPAA/PCI-DSS requirements
- Implementing hybrid and multi-cloud strategies balancing vendor lock-in avoidance with operational simplicity and cost efficiency
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: cloud-architecture
---

# Cloud Architecture Design

## Purpose
Design production-grade cloud architectures on AWS, Azure, or GCP covering compute, storage, networking, security, high availability, and cost optimization achieving 99.9%+ uptime with compliance requirements and budget constraints.

## Template

Design cloud architecture on {CLOUD_PROVIDER} for {APPLICATION_TYPE} supporting {SCALE_REQUIREMENTS} with {AVAILABILITY_TARGET}% availability and {BUDGET} monthly budget.

**COMPUTE ARCHITECTURE**

Select compute model matching workload characteristics and operational preferences. EC2/VMs for persistent workloads: t3/t4g for variable CPU (burstable), m5/m6i for general purpose (balanced), c5/c6i for compute-intensive (high CPU), r5/r6i for memory-intensive (caching, analytics). Container orchestration for microservices: EKS/AKS/GKE managed Kubernetes, ECS Fargate for serverless containers (no node management), simplifies scaling and deployment. Serverless for event-driven: Lambda/Azure Functions/Cloud Functions for request-based pricing, auto-scales to zero, max 15-minute execution for Lambda.

Configure auto-scaling for cost efficiency and performance. Target tracking: 70% CPU utilization maintains headroom without waste. Step scaling: aggressive scale-out (add 50% capacity when >90% CPU for 2 minutes), conservative scale-in (remove 10% when <40% for 10 minutes). Predictive scaling: enable for predictable patterns (business hours traffic), learns usage patterns. Instance diversity: mix on-demand (baseline capacity 30-40%) with spot/preemptible (variable capacity 60-70%, 60-90% cost savings, handle interruptions gracefully).

Size instances based on actual utilization data. Start with Compute Optimizer/Azure Advisor recommendations, right-size after 2 weeks of production metrics. Graviton/ARM instances: 20-40% better price-performance for compatible workloads (containerized, interpreted languages). Reserved capacity planning: 1-year reserved instances for stable baseline (30% savings), 3-year for committed workloads (60% savings), Savings Plans for flexible compute.

**NETWORK ARCHITECTURE**

Design VPC topology for isolation and security. CIDR planning: /16 VPC (65K IPs), /24 subnets (256 IPs each), leave room for growth. Subnet strategy: public subnets for load balancers and bastion hosts, private subnets for application tier, isolated subnets for databases (no internet route). Multi-AZ: minimum 3 AZs for production (survives AZ failure), 2 AZs acceptable for non-production. NAT Gateway: one per AZ for high availability ($32/month + data processing), consider NAT instance for dev environments.

Implement hub-and-spoke for multi-VPC environments. Transit Gateway (AWS): central hub connecting VPCs and on-premises, simplifies routing (single route table vs N×N peering). VPC peering for simple topologies: direct connection between 2 VPCs, no transitive routing, lower latency than Transit Gateway. Private endpoints: VPC endpoints for AWS services (S3, DynamoDB, KMS) avoid NAT costs and improve security.

Configure load balancing for traffic distribution. Application Load Balancer (ALB): HTTP/HTTPS traffic, path-based routing, WebSocket support, integrates with WAF. Network Load Balancer (NLB): TCP/UDP, ultra-low latency (<1ms), static IPs, TLS passthrough. Global Accelerator/Azure Front Door: anycast IPs, global traffic routing, DDoS protection, 60% latency improvement for global users. Health checks: 10-second interval, 2 consecutive failures to mark unhealthy, path-based (/health) not just TCP.

**DATABASE AND STORAGE**

Select database matching access patterns and scale requirements. Relational (RDS Aurora/Cloud SQL): ACID transactions, complex queries, <100K TPS, Aurora scales reads to 15 replicas. NoSQL document (DynamoDB/CosmosDB/Firestore): flexible schema, single-digit millisecond latency, unlimited scale, partition key design critical. NoSQL key-value (ElastiCache Redis): sub-millisecond latency, session storage, caching (cache-aside pattern), pub/sub. Time-series (Timestream/TimescaleDB): metrics and events, optimized for time-range queries, automatic data lifecycle.

Design for high availability and disaster recovery. Multi-AZ deployment: synchronous replication to standby, automatic failover (<30 seconds for Aurora), RPO ~0. Read replicas: async replication for read scaling and regional DR, promote to primary in disaster. Cross-region replication: Aurora Global Database (1-second replication lag), DynamoDB Global Tables (eventual consistency). Backup strategy: automated daily snapshots (35-day retention), point-in-time recovery, cross-region backup copies.

Configure storage tiers for cost optimization. S3/Blob storage tiers: Standard (frequently accessed), Intelligent-Tiering (unknown patterns, auto-moves), Standard-IA (monthly access), Glacier (archival, minutes to hours retrieval). Lifecycle policies: transition to IA after 30 days, Glacier after 90 days, delete after 7 years (compliance). EBS/Managed Disks: gp3 for general purpose (baseline 3K IOPS, scale independently), io2 for high IOPS requirements (64K IOPS), throughput optimized for big data.

**SECURITY ARCHITECTURE**

Implement defense in depth across all layers. Network security: security groups (stateful, instance-level), NACLs (stateless, subnet-level), WAF (OWASP rules, rate limiting, geo-blocking), Shield for DDoS (Standard free, Advanced for enhanced protection). Application security: Secrets Manager for credentials (automatic rotation), Certificate Manager for TLS, Parameter Store for configuration. Data security: KMS encryption for data at rest (AES-256), TLS 1.2+ in transit, field-level encryption for sensitive data.

Configure identity and access management. IAM best practices: least privilege policies, role-based access (no long-lived credentials), permission boundaries for delegated admin. Service roles: EC2 instance profiles, ECS task roles, Lambda execution roles—no embedded credentials. MFA enforcement: required for console access, hardware tokens for privileged users. Cross-account access: AWS Organizations with SCPs (guardrails), assume role for controlled access.

Implement compliance controls and monitoring. Audit logging: CloudTrail (all API calls), VPC Flow Logs (network traffic), S3 access logging. Threat detection: GuardDuty (ML-based threat detection), Security Hub (centralized findings), Inspector (vulnerability scanning). Compliance automation: AWS Config rules (continuous compliance), conformance packs for SOC2/HIPAA/PCI, automated remediation with Lambda. Encryption at rest: default encryption for S3, EBS, RDS—customer-managed KMS keys for compliance.

**HIGH AVAILABILITY AND DISASTER RECOVERY**

Design for target availability tier. 99.9% (8.76 hours downtime/year): multi-AZ deployment, automated failover, standard DR. 99.99% (52 minutes/year): multi-region active-passive, automated failover, tested runbooks. 99.999% (5 minutes/year): multi-region active-active, global load balancing, zero-downtime deployments. Each additional 9 roughly doubles cost—match tier to business requirements.

Implement disaster recovery strategy matching RTO/RPO. Backup and restore (RTO hours, RPO hours): cheapest, restore from backups to new region. Pilot light (RTO minutes, RPO minutes): minimal infrastructure running in DR region, scale up on failover. Warm standby (RTO seconds, RPO seconds): scaled-down production in DR region, promote to full capacity. Active-active (RTO ~0, RPO ~0): full production in multiple regions, global load balancing, most expensive but zero data loss.

Test disaster recovery regularly. Automated DR tests: monthly automated failover to DR region during maintenance window. Game days: quarterly full DR exercise simulating region failure, measure actual RTO/RPO. Chaos engineering: Fault Injection Simulator/Chaos Monkey to test resilience (AZ failure, instance termination, network partition). Runbook validation: verify runbooks produce expected results, update based on findings.

**COST OPTIMIZATION**

Implement FinOps practices for cost visibility and control. Tagging strategy: mandatory tags (environment, owner, cost-center, application) enforced by SCP. Cost allocation: enable cost allocation tags, create per-team/per-application cost reports. Budgets and alerts: 80% threshold warning, 100% alert to FinOps, 120% escalation to leadership. Reserved capacity: analyze Savings Plans recommendations monthly, commit to 1-year minimum for stable workloads.

Optimize compute costs systematically. Right-sizing: Compute Optimizer recommendations, target 60-70% utilization. Spot instances: 60-90% savings, use for fault-tolerant workloads (batch processing, CI/CD, stateless web), Spot Fleet for capacity diversity. Graviton/ARM: 20-40% better price-performance, test compatibility before migration. Turn off unused resources: Lambda to stop/start dev environments nights/weekends, saves 65% on non-production.

Reduce data transfer and storage costs. VPC endpoints: eliminate NAT Gateway data processing charges for AWS service access. CloudFront/CDN: cache at edge, reduce origin load and egress costs. Storage tiering: lifecycle policies move data to cheaper tiers, S3 Intelligent-Tiering for unknown access patterns. Data compression: gzip/brotli for API responses, reduce transfer costs and improve latency.

Deliver cloud architecture as:

1. **ARCHITECTURE DIAGRAM** - Multi-tier architecture showing compute, network, database, and storage components with data flows

2. **NETWORK DESIGN** - VPC/VNET configuration, subnet strategy, security groups, load balancing, and connectivity

3. **COMPUTE SPECIFICATION** - Instance types, auto-scaling configuration, container orchestration, serverless functions

4. **DATA LAYER** - Database selection, replication strategy, caching layer, storage tiers

5. **SECURITY CONTROLS** - IAM design, encryption strategy, network security, compliance controls

6. **DR AND HA** - Availability design, backup strategy, disaster recovery procedures, RTO/RPO targets

7. **COST ESTIMATE** - Monthly cost breakdown, optimization recommendations, reserved capacity plan

---

## Usage Examples

### Example 1: E-commerce Platform on AWS
**Prompt:** Design cloud architecture on AWS for EcommerceApp supporting 100K concurrent users, 5000 requests/sec with 99.99% availability, PCI-DSS compliance, and $50K/month budget.

**Expected Output:** Compute: ECS Fargate for web tier (auto-scale 10-100 tasks), Lambda for async processing (order processing, notifications). Network: Multi-AZ VPC (3 AZs, /16 CIDR), ALB with WAF (OWASP rules, rate limiting 1000 req/min/IP), CloudFront CDN (100+ edge locations). Database: Aurora PostgreSQL (db.r6g.2xlarge primary, 3 read replicas, Multi-AZ), DynamoDB for sessions (on-demand capacity), ElastiCache Redis (cache.r6g.large, 3-node cluster). Storage: S3 for product images (CloudFront origin), lifecycle to IA after 90 days. Security: KMS encryption for PCI data, Secrets Manager for DB credentials, GuardDuty + Security Hub, AWS Config PCI conformance pack. DR: Aurora Global Database (us-west-2 DR), RTO 15 minutes, RPO <1 minute, monthly failover tests. Cost: $42K/month (compute $18K, database $12K, network $6K, storage $3K, other $3K), optimize with Graviton instances (-25%), Savings Plans for Fargate.

### Example 2: Healthcare Analytics Platform on Azure
**Prompt:** Design cloud architecture on Azure for HealthAnalytics processing 10TB patient data daily with HIPAA compliance, 99.9% availability, and $30K/month budget.

**Expected Output:** Compute: Azure Kubernetes Service (AKS) for data processing pipelines (D4s_v5 nodes, 5-20 node auto-scale), Azure Functions for event-driven ETL. Network: Hub-and-spoke VNETs (hub for shared services, spokes per environment), Azure Firewall for egress filtering, Private Link for all PaaS services. Database: Azure SQL Managed Instance (Business Critical, 8 vCores) for structured data, Azure Cosmos DB for patient events (multi-region writes), Azure Synapse for analytics warehouse. Storage: Data Lake Gen2 (hot/cool/archive tiers), 90-day lifecycle to cool, 1-year to archive. Security: Azure AD with Privileged Identity Management, Customer-managed keys in Key Vault, Microsoft Defender for Cloud, HIPAA blueprint compliance. DR: Geo-redundant storage (RA-GRS), SQL auto-failover groups, RTO 1 hour, RPO 5 minutes. Cost: $28K/month (AKS $10K, databases $9K, storage $5K, networking $2K, security $2K), optimize with Reserved VM instances for baseline nodes.

### Example 3: Global SaaS Application Multi-Cloud
**Prompt:** Design multi-cloud architecture on AWS (primary) and GCP (DR) for GlobalSaaS serving users in NA, EU, APAC with 99.99% availability and vendor lock-in mitigation.

**Expected Output:** Compute: Kubernetes on both clouds (EKS us-east-1/eu-west-1, GKE asia-east1), containerized applications with Helm charts portable across providers. Network: AWS Global Accelerator for NA/EU traffic, GCP Cloud CDN for APAC, Cloudflare as cloud-agnostic CDN/WAF layer. Database: CockroachDB multi-region (vendor-neutral distributed SQL), Redis Enterprise for caching (cloud-agnostic). Storage: MinIO-compatible object storage abstraction, actual storage on S3 (AWS) and GCS (GCP) with cross-cloud replication via Rclone. Abstraction layer: Terraform with provider-agnostic modules, Pulumi for complex orchestration, Kong API Gateway for service mesh. Security: HashiCorp Vault for secrets (centralized across clouds), OPA Gatekeeper for policy enforcement. DR: Active-passive (AWS primary, GCP warm standby), DNS failover via Cloudflare, quarterly cross-cloud failover tests. Cost: $75K/month total (AWS $55K primary, GCP $12K DR, Cloudflare $8K), multi-cloud premium ~40% vs single cloud for portability and resilience.

---

## Cross-References

- [Infrastructure as Code](infrastructure-as-code.md) - Terraform/CloudFormation patterns for cloud provisioning
- [Container Orchestration](container-orchestration.md) - Kubernetes architecture on cloud providers
- [Cloud Migration Strategy](cloud-migration-strategy.md) - Migration patterns and cloud adoption frameworks
