---
category: technology
related_templates:
- technology/DevOps-Cloud/devops-infrastructure-as-code.md
- technology/Data-Engineering/data-pipeline-architecture.md
- data-analytics/Analytics-Engineering/pipeline-infrastructure.md
tags:
- data-infrastructure
- terraform
- data-lake
- data-warehouse
title: Data Infrastructure as Code
use_cases:
- Provisioning data platform infrastructure (data lakes, warehouses, streaming) using Terraform/Pulumi with modular design and environment parity
- Building self-service data infrastructure enabling data engineers to provision Spark clusters, Kafka topics, and databases without tickets
- Implementing data platform governance with cost tagging, access controls, and compliance automation for regulated industries
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: data-infrastructure-as-code
---

# Data Infrastructure as Code

## Purpose
Design and implement infrastructure as code for data platforms covering data lakes, warehouses, streaming infrastructure, and compute clusters achieving reproducible, compliant, cost-optimized data infrastructure with self-service capabilities.

## Template

Provision data platform infrastructure on {CLOUD_PROVIDER} using {IAC_TOOL} supporting {DATA_VOLUME} daily data with {COMPLIANCE_REQUIREMENTS} compliance and {BUDGET} monthly budget.

**DATA LAKE INFRASTRUCTURE**

Design multi-zone data lake architecture for governance and performance. Landing zone (raw): receive data from sources unchanged, partitioned by ingestion date, short retention (30 days). Bronze zone (validated): schema-validated, deduplicated, full history retained, partitioned by event date. Silver zone (transformed): business logic applied, joined datasets, optimized for analytics, partitioned by common query dimensions. Gold zone (curated): aggregated metrics, ML features, served to applications, optimized for read performance.

Configure object storage with appropriate settings per zone. Landing/Bronze: S3 Standard/GCS Standard, versioning disabled (managed by pipeline), lifecycle to Glacier/Archive after 90 days. Silver: S3 Standard-IA/GCS Nearline for infrequently accessed historical data, lifecycle transitions. Gold: S3 Standard/GCS Standard for active serving, CloudFront/CDN for high-read workloads. Cross-region replication: enable for disaster recovery, replicate Gold zone to DR region.

Implement data lake security and governance. IAM: role-based access per zone, data engineers write to Bronze/Silver, analysts read from Silver/Gold. Encryption: SSE-S3/SSE-KMS at rest, TLS in transit, customer-managed keys for regulated data. Access logging: S3 server access logging, CloudTrail for API calls, Lake Formation for fine-grained access control. Data catalog: AWS Glue Data Catalog, Azure Purview, GCP Data Catalog for discovery and governance.

**DATA WAREHOUSE PROVISIONING**

Configure warehouse infrastructure matching workload patterns. Snowflake: separate warehouses per workload (ETL: X-Large, BI: Medium, ad-hoc: Small), auto-suspend (1 minute), auto-resume. BigQuery: on-demand for variable workloads, flat-rate slots for predictable high-volume, reservations for guaranteed capacity. Redshift: RA3 nodes for separate compute/storage scaling, concurrency scaling for burst, Redshift Serverless for variable workloads.

Manage warehouse resources via Terraform. Snowflake provider: databases, schemas, warehouses, roles, users, grants. BigQuery provider: datasets, tables, views, routines, row-level security policies. Redshift provider: clusters, parameter groups, subnet groups, IAM roles. State management: separate state files per environment, remote backend with locking.

Implement warehouse governance and cost controls. Role hierarchy: ACCOUNTADMIN (platform team only), SYSADMIN (data engineering), data-specific roles (analysts per domain). Resource monitors: Snowflake credit quotas per warehouse, BigQuery custom quotas, Redshift WLM queues. Query governance: max query duration limits, result size limits, query tagging for cost allocation.

**STREAMING INFRASTRUCTURE**

Provision streaming platform for real-time data. Kafka on Kubernetes: Strimzi operator for cluster management, 3-broker minimum for HA, ZooKeeper or KRaft mode. Amazon MSK: managed Kafka, serverless for variable load, provisioned for predictable throughput. Kinesis: Data Streams for ingestion, Firehose for delivery to S3/Redshift, auto-scaling shards. Event Hubs: Azure native, capture to ADLS, Kafka protocol compatibility.

Configure topics and streams with appropriate settings. Partitioning: partition count based on throughput (1 partition ~1 MB/s write), key-based partitioning for ordering. Retention: 7 days default, 30 days for reprocessing capability, infinite for audit requirements. Replication: factor 3 for production, factor 2 for dev/staging. Compaction: enable for changelog topics, retain latest value per key.

Manage streaming infrastructure via IaC. Kafka topics: Terraform Kafka provider, topic configuration (partitions, replication, retention). Schema registry: Confluent Schema Registry, AWS Glue Schema Registry, subject naming conventions. Consumer groups: provisioned via application config, monitoring via consumer lag metrics. Access control: SASL/SCRAM authentication, ACLs per topic, Kafka RBAC for Confluent.

**COMPUTE CLUSTER PROVISIONING**

Configure Spark infrastructure for batch and streaming workloads. EMR: cluster templates (transient for batch, long-running for streaming), instance fleets (mix on-demand + spot), auto-scaling policies. Databricks: Unity Catalog for governance, cluster policies for cost control, jobs clusters vs all-purpose clusters. Dataproc: workflow templates, autoscaling policies, component gateway for web UIs.

Implement cluster templates for common patterns. Batch processing: transient cluster, spot instances (70%), auto-terminate after job, sized for data volume. Interactive analysis: long-running, on-demand instances, auto-scale based on users, idle timeout. Streaming: long-running, mixed fleet, checkpoint to S3/GCS, graceful shutdown handling. ML training: GPU instances, spot with checkpointing, auto-scale based on experiments.

Manage compute via Terraform modules. EMR: cluster configuration, instance groups, bootstrap actions, security configuration. Databricks: workspace, clusters, jobs, secrets, Unity Catalog resources. Instance profiles: IAM roles for cluster access to S3, Glue, Secrets Manager. Networking: VPC placement, security groups, private subnets for data processing.

**NETWORKING AND CONNECTIVITY**

Design data platform network architecture. VPC design: dedicated VPC for data platform, CIDR planning for growth, private subnets for compute. Connectivity: VPC peering to application VPCs, Transit Gateway for multi-VPC, PrivateLink for SaaS (Snowflake, Databricks). Egress control: NAT Gateway for internet access, VPC endpoints for AWS services (S3, Glue, Secrets Manager). Firewall: security groups per service type, NACLs for subnet-level control.

Configure connectivity to external data sources. Database connectivity: VPN or Direct Connect to on-premises, JDBC/ODBC through bastion or proxy. SaaS integrations: Fivetran/Airbyte in private subnet, PrivateLink where available. Partner access: dedicated subnets for vendor access, time-limited credentials, audit logging. Multi-cloud: dedicated interconnect (AWS Direct Connect, Azure ExpressRoute, GCP Cloud Interconnect).

**SECURITY AND COMPLIANCE**

Implement data platform security baseline. IAM: service accounts per application, role assumption for cross-account, no long-lived credentials. Encryption: KMS keys per data classification, key rotation policies, envelope encryption for large datasets. Network: private endpoints, no public IPs on compute, WAF for APIs. Secrets: AWS Secrets Manager/HashiCorp Vault, automatic rotation, no secrets in code.

Configure compliance controls for regulated data. Data classification: tagging for PII/PHI/PCI, automated discovery with Macie/DLP. Access governance: Lake Formation permissions, row/column security, audit trails. Retention policies: automated lifecycle rules, legal hold capabilities, deletion verification. Compliance reporting: AWS Config rules, automated compliance dashboards, evidence collection.

**CI/CD FOR DATA INFRASTRUCTURE**

Build pipeline for infrastructure deployment. Validation stage: terraform fmt, terraform validate, tflint, checkov security scan. Plan stage: terraform plan, output to PR comment, cost estimation with Infracost. Apply stage: terraform apply (auto for dev, approval for prod), state verification. Testing: Terratest for module validation, integration tests in ephemeral environment.

Manage state and environments. Backend: S3 + DynamoDB locking (AWS), GCS (GCP), Azure Blob (Azure), Terraform Cloud (managed). Environment separation: separate state files per environment, workspace or directory-based. Promotion: dev → staging → prod, same modules with environment-specific variables. Drift detection: scheduled plan runs, alert on unexpected changes.

**COST MANAGEMENT AND OPTIMIZATION**

Implement FinOps for data infrastructure. Tagging strategy: mandatory tags (environment, team, cost-center, data-domain), enforced by policy. Cost allocation: per-team dashboards, chargeback for compute usage, showback for storage. Budget alerts: 80% threshold warning, 100% alert, weekly cost trend reports. Anomaly detection: CloudWatch anomaly detection, Kubecost for Kubernetes, custom alerts for unusual patterns.

Optimize data platform costs. Storage: lifecycle policies to cold tiers, intelligent tiering for unknown patterns, cleanup orphaned data. Compute: spot instances for fault-tolerant jobs (60-90% savings), reserved capacity for baseline, auto-terminate idle. Warehouse: auto-suspend, right-sized warehouses, query optimization reducing scanned data. Streaming: right-sized partitions, data compression, retention optimization.

Deliver data infrastructure as code as:

1. **DATA LAKE MODULES** - Storage buckets, zones, lifecycle policies, access controls per zone

2. **WAREHOUSE CONFIGURATION** - Databases, schemas, warehouses/clusters, roles, grants

3. **STREAMING INFRASTRUCTURE** - Kafka/Kinesis clusters, topics, schemas, consumer configuration

4. **COMPUTE CLUSTERS** - Spark cluster templates, instance configurations, auto-scaling policies

5. **NETWORKING** - VPC, subnets, security groups, connectivity (peering, endpoints, VPN)

6. **SECURITY CONTROLS** - IAM roles, encryption configuration, compliance policies, audit logging

7. **CI/CD PIPELINE** - Validation, planning, apply workflow, state management, testing

---

## Usage Examples

### Example 1: Enterprise Data Lake on AWS
**Prompt:** Provision data lake infrastructure on AWS using Terraform supporting 50TB daily ingestion with SOC2 compliance and $80K/month budget.

**Expected Output:** Data lake: S3 buckets per zone (landing, bronze, silver, gold) in us-east-1, cross-region replication to us-west-2 for DR. Configuration per zone: landing (Standard, 30-day lifecycle to delete), bronze (Standard, versioning, 90-day to Glacier), silver (Intelligent-Tiering), gold (Standard with CloudFront). Security: SSE-KMS with customer-managed keys, Lake Formation for fine-grained access, IAM roles per team (data-eng-write, analyst-read). Glue Data Catalog for metadata, crawlers per zone, partition indexes for query optimization. Networking: dedicated VPC (10.0.0.0/16), private subnets, VPC endpoints for S3/Glue/KMS, no NAT for data path. Compute: EMR clusters provisioned separately (batch processing, streaming), instance profiles with S3 access. CI/CD: GitHub Actions, terraform plan on PR, apply on merge to main, separate workspaces per environment. Cost: $75K/month (storage $30K, compute $35K, networking $5K, other $5K), lifecycle policies saving 25% on storage.

### Example 2: Modern Data Stack on GCP
**Prompt:** Provision modern data stack on GCP using Terraform with BigQuery warehouse, Dataflow streaming, and Composer orchestration for Series B startup.

**Expected Output:** Warehouse: BigQuery datasets (raw, staging, mart), IAM roles per domain team, authorized views for row-level security. Storage: GCS buckets (landing, archive), lifecycle to Nearline after 30 days, Coldline after 90 days. Streaming: Pub/Sub topics for event ingestion, Dataflow templates for streaming ETL, BigQuery streaming inserts. Orchestration: Cloud Composer (Airflow 2.x), small environment, DAGs deployed via CI/CD. Compute: Dataproc for Spark workloads (autoscaling 2-10 nodes), preemptible workers. Networking: VPC with Private Google Access, Cloud NAT for external APIs, VPC Service Controls for BigQuery. Security: customer-managed encryption keys, Data Catalog for discovery, DLP for PII scanning. CI/CD: Cloud Build, Terraform state in GCS, workspaces per environment. Cost: $25K/month (BigQuery $12K on-demand, storage $5K, Composer $3K, Dataproc $4K, other $1K), optimize with flat-rate slots when query volume increases.

### Example 3: Regulated Data Platform on Azure
**Prompt:** Provision HIPAA-compliant data platform on Azure using Terraform with Synapse, Databricks, and Event Hubs for healthcare analytics company.

**Expected Output:** Data lake: ADLS Gen2 with hierarchical namespace, containers per zone (raw/curated/consumption), AAD-based access control. Warehouse: Azure Synapse dedicated SQL pool (DW1000c), serverless SQL for ad-hoc, Spark pools for data engineering. Compute: Databricks workspace with Unity Catalog, cluster policies enforcing PHI-compliant configurations, private link. Streaming: Event Hubs (Standard tier, 4 TUs), capture to ADLS, Kafka endpoint for compatibility. Security: customer-managed keys in Key Vault, private endpoints for all services, Purview for data governance and lineage. Compliance: Azure Policy for HIPAA controls, diagnostic settings to Log Analytics, Microsoft Defender for Cloud. Networking: hub-and-spoke VNet, Azure Firewall for egress, private endpoints to all PaaS services. Access: AAD groups mapped to Synapse/Databricks roles, conditional access policies, PIM for privileged access. CI/CD: Azure DevOps, Terraform state in Azure Storage with service principal, environment-specific variable groups. Cost: $60K/month (Synapse $25K, Databricks $20K, storage $8K, networking $4K, other $3K), reserved capacity for 30% savings.

---

## Cross-References

- [DevOps Infrastructure as Code](../DevOps-Cloud/devops-infrastructure-as-code.md) - General IaC patterns and practices
- [Data Pipeline Architecture](data-pipeline-architecture.md) - Pipeline design using provisioned infrastructure
- [Pipeline Infrastructure](../../data-analytics/Analytics-Engineering/pipeline-infrastructure.md) - Analytics infrastructure patterns
