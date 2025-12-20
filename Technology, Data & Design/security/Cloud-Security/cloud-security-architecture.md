---
category: security
title: Cloud Security Architecture Framework
tags:
- security
- cloud-security
- aws-azure-gcp
- cspm
use_cases:
- Designing secure cloud infrastructure with network segmentation, IAM least-privilege, encryption at-rest/in-transit achieving SOC2/HIPAA/PCI-DSS compliance
- Implementing cloud security controls across AWS/Azure/GCP with centralized logging, threat detection (GuardDuty/Defender/SCC), CSPM for multi-cloud
- Cloud migration security strategy with zero-trust networking, secrets management, disaster recovery achieving FedRAMP/GDPR compliance
related_templates:
- security/Cybersecurity/security-architecture.md
- technology/DevOps-Cloud/cloud-architecture.md
- security/Cloud-Security/kubernetes-security.md
industries:
- technology
- financial-services
- healthcare
- government
type: framework
difficulty: intermediate
slug: cloud-security-architecture
---

# Cloud Security Architecture Framework

## Purpose
Design secure cloud infrastructure covering network architecture, IAM, data protection, logging/monitoring, compute/container/serverless security, compliance, and disaster recovery for AWS, Azure, GCP, and multi-cloud environments.

## 🚀 Quick Cloud Security Prompt

> Design secure **[CLOUD_PROVIDER]** (AWS/Azure/GCP) architecture for **[WORKLOAD]** handling **[DATA_CLASSIFICATION]** (PII/PHI/PCI). Implement: network segmentation **[VPC/VNET]**, IAM least-privilege, encryption **[AT_REST/IN_TRANSIT]**, logging **[CLOUDTRAIL/MONITOR/AUDIT]**, threat detection **[GUARDDUTY/DEFENDER/SCC]**. Compliance: **[SOC2/HIPAA/PCI/FEDRAMP]**. Deliver: architecture diagram, security controls matrix.

---

## Template

Design secure cloud architecture for {WORKLOAD} on {CLOUD_PROVIDER} processing {DATA_CLASSIFICATION} data achieving {COMPLIANCE_REQUIREMENTS} compliance with {HA_DR_REQUIREMENTS}.

**NETWORK SECURITY ARCHITECTURE**

Design defense-in-depth network controls. Network segmentation: 3-tier architecture (public subnet for internet-facing load balancers, private subnet for application tier, data subnet for databases with no internet access), dedicated subnets per availability zone for high availability, separate VPC/VNet for production vs non-production, network isolation for compliance zones (PCI CDE, PHI systems). CIDR planning: avoid overlapping ranges for VPC peering/VNet peering, plan for growth (start with /16 VPC, use /24 subnets), reserve space for future regions.

Traffic control: security groups as stateful firewalls (instance-level, allow-list approach), network ACLs as stateless subnet-level controls (backup layer), default deny with explicit allows, separate security groups per tier (web-sg, app-sg, db-sg). Web application firewall: AWS WAF/Azure WAF/Cloud Armor with OWASP Core Rule Set, bot detection and mitigation, rate limiting per IP/session, geo-blocking for non-operating regions, custom rules for application-specific threats.

Cloud connectivity: site-to-site VPN for hybrid connectivity (AWS VPN, Azure VPN Gateway, Cloud VPN), Direct Connect/ExpressRoute/Cloud Interconnect for dedicated bandwidth, private endpoints/Private Link for PaaS services (eliminates public internet exposure), PrivateLink for cross-account access, service endpoints for regional services. Zero trust networking: assume breach posture, verify every request (identity, device, location), micro-segmentation between workloads, encrypt all traffic end-to-end.

**IDENTITY AND ACCESS MANAGEMENT**

Implement least-privilege access control. Authentication: federate with corporate identity (SAML/OIDC with Okta/Azure AD/Google Workspace), enforce MFA for all human access, service accounts for application-to-cloud authentication (AWS IAM roles, Azure managed identities, GCP service accounts), short-lived credentials preferred (STS temporary credentials, federated tokens). Root/admin account protection: hardware MFA on root account, separate billing-only root account (no operational use), admin access requires approval workflow, audit all root account usage.

Authorization: role-based access control with least privilege (start with zero, add minimally required permissions), avoid wildcard permissions (no Resource:"*" or Action:"*"), policy boundaries prevent privilege escalation, resource tagging for attribute-based access control (ABAC), cross-account access via assume role (not access keys). Cloud-native patterns: AWS IAM roles for EC2/Lambda/ECS, Azure managed identities for VMs/App Service/Functions, GCP service accounts with Workload Identity, temporary credentials only (no long-lived access keys).

Privileged access management: just-in-time access (time-boxed privilege elevation), break-glass procedures for emergency access, session recording for privileged actions (CloudTrail data events, Azure Monitor), bastion host alternatives (AWS Systems Manager Session Manager, Azure Bastion, IAP for GCP), require approval for production access. Regular access reviews: quarterly review of IAM permissions, automated detection of unused permissions (Access Advisor, Azure AD access reviews), revoke stale credentials, principle of least privilege enforced through automation.

**DATA PROTECTION AND ENCRYPTION**

Protect data at rest and in transit. Encryption at rest: enable default encryption for all storage (S3, EBS, Azure Storage, GCS with AES-256), database encryption (RDS, DynamoDB, Cosmos DB, Cloud SQL with transparent data encryption), application-layer encryption for sensitive fields (PII, PHI, PCI). Key management: cloud-managed keys for default encryption (easy, automatic rotation), customer-managed keys for compliance (bring your own key, control rotation), envelope encryption (data keys encrypted with master keys), HSM-backed keys for PCI/HIPAA (AWS CloudHSM, Azure Dedicated HSM, Cloud HSM).

Encryption in transit: TLS 1.3 for all HTTPS traffic, certificate management via cloud services (AWS Certificate Manager, Azure Key Vault, Google-managed certificates), automated certificate renewal, internal service-to-service encryption (private CA, mTLS), database connection encryption mandatory. Secrets management: centralized secrets (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager), no secrets in code or environment variables, automatic rotation (30-90 days), application retrieval at runtime (not build time), audit all secret access.

Data classification and protection: tag resources by data sensitivity (public, internal, confidential, restricted), enforce encryption based on tags, data loss prevention (DLP) policies (AWS Macie, Azure Information Protection, Cloud DLP), monitor for sensitive data in logs, secure deletion procedures (crypto-shredding, multi-pass overwrites for compliance).

**LOGGING, MONITORING, AND THREAT DETECTION**

Build comprehensive security visibility. Centralized logging: enable cloud-native audit logs (AWS CloudTrail all regions, Azure Activity Log, GCP Cloud Audit Logs), VPC/VNet flow logs (network traffic metadata for forensics), application/system logs aggregated centrally, S3/Azure Storage/GCS for log archive (WORM for compliance), retention per requirements (7 years for SOX, 6 years for HIPAA). Log analysis: ship logs to SIEM (Splunk, Sentinel, Chronicle), correlation with threat intelligence, automated alerting on suspicious activity, baseline normal behavior then detect deviations.

Cloud-native threat detection: AWS GuardDuty (ML-based threat detection for AWS accounts), Azure Defender/Sentinel (integrated threat protection), GCP Security Command Center (asset discovery and threat detection), enable all detectors (malware, crypto-mining, unusual API calls, credential access). Configuration compliance: AWS Config/Azure Policy/GCP Security Health Analytics for continuous compliance, CIS benchmark assessments (automated with Cloud Custodian, Prowler, ScoutSuite), detect configuration drift, auto-remediate common issues.

Vulnerability management: container image scanning (ECR scanning, ACR scanning, Artifact Registry scanning), serverless code scanning (Lambda, Azure Functions, Cloud Functions), infrastructure vulnerability scanning (AWS Inspector, Azure Defender for Servers, Security Command Center). Incident response: automated response playbooks (isolate compromised instance, rotate credentials, block IP), alert integration (PagerDuty, Slack, ServiceNow), forensics readiness (EBS snapshots, disk imaging, memory capture).

**COMPUTE AND WORKLOAD SECURITY**

Secure compute resources across deployment models. Virtual machines: hardened base images (CIS-benchmarked AMIs, Azure Marketplace hardened images, GCP hardened images), automated patching (AWS Systems Manager Patch Manager, Azure Update Management, GCP OS Patch Management), endpoint protection (AWS GuardDuty Runtime, Azure Defender for Servers, GCP Security Command Center), host-based firewalls enabled, disable SSH/RDP from internet (use Session Manager, Bastion, IAP).

Containers: image scanning in CI/CD (Trivy, Snyk, Aqua), private registries only (ECR, ACR, Artifact Registry), runtime security (Falco, Sysdig, Aqua), Kubernetes security (see kubernetes-security template for details), secrets via external stores (not in images or ConfigMaps). Serverless: function-level IAM roles (minimal permissions per function), code and dependency scanning, environment variable encryption, VPC integration for private resource access, execution time limits, concurrency limits prevent resource exhaustion.

**COMPLIANCE AND GOVERNANCE**

Map security controls to regulatory requirements. Compliance frameworks: SOC 2 (access controls, encryption, monitoring, change management), HIPAA (PHI encryption, audit logs, access controls, BAA with cloud provider), PCI-DSS (network segmentation for CDE, encryption, logging, quarterly scans), FedRAMP (FIPS 140-2 encryption, continuous monitoring, configuration management), GDPR (data residency, encryption, right to deletion, breach notification). Evidence automation: infrastructure-as-code for repeatable deployments, policy-as-code for compliance checks (AWS Config rules, Azure Policy, GCP Organization Policies), automated evidence collection (screenshots, logs, configuration exports).

Governance: resource tagging strategy (owner, environment, cost-center, data-classification, compliance-scope), enforce tagging via policy, cost allocation by tag, automated cleanup of untagged resources. Policy enforcement: service control policies (SCPs) for AWS Organizations, Azure Policy for subscription-level enforcement, GCP Organization Policies for folder/project constraints, deny public access by default, require encryption, enforce regions for data residency.

**DISASTER RECOVERY AND HIGH AVAILABILITY**

Design for resilience. High availability: multi-AZ deployments for production (distribute across 3 AZs), auto-scaling for elasticity (scale out on demand, scale in to save cost), load balancing (ALB, Azure Load Balancer, Cloud Load Balancing), health checks and automatic failover, database replication (RDS Multi-AZ, Cosmos DB multi-region, Cloud SQL HA).

Backup strategy: automated backups with retention (daily backups, 30-day retention, extend for compliance), cross-region replication for geographic redundancy, backup encryption and access control (separate IAM permissions for restore), regular restore testing (quarterly DR drills), immutable backups for ransomware protection (S3 Object Lock, Azure Immutable Blob Storage). Disaster recovery: define RTO/RPO (Recovery Time Objective, Recovery Point Objective), pilot light (minimal infrastructure always on, scale up on DR), warm standby (scaled-down environment ready to scale), multi-region active-active for critical workloads, automated failover with health checks, DR runbooks with step-by-step procedures.

Deliver cloud security architecture as:

1. **NETWORK ARCHITECTURE** - VPC/VNet design, subnet layout, security groups/NSGs, connectivity diagram

2. **IAM STRATEGY** - Role hierarchy, policy examples, federation design, privileged access workflow

3. **ENCRYPTION DESIGN** - At-rest/in-transit encryption, key management, certificate lifecycle

4. **LOGGING AND MONITORING** - Log collection, SIEM integration, alert configuration, threat detection

5. **COMPLIANCE CONTROLS** - Control mapping to frameworks, policy-as-code, evidence automation

6. **DR/HA ARCHITECTURE** - Backup strategy, multi-region design, failover procedures, RTO/RPO achievement

7. **IMPLEMENTATION GUIDE** - Infrastructure-as-code templates (Terraform, CloudFormation, ARM, Deployment Manager)

---

## Usage Examples

### Example 1: SaaS Startup on AWS (SOC 2)
**Prompt:** Design secure AWS architecture for CustomerHub B2B SaaS processing customer PII with SOC 2 Type II compliance, 99.9% uptime SLA.

**Expected Output:** Network: VPC in us-east-1 (primary) + us-west-2 (DR), 3-tier architecture (public subnet for ALB only, private for ECS Fargate, data subnet for RDS PostgreSQL), VPC Flow Logs enabled, no public database access. IAM: Okta SSO with SAML federation, AWS SSO for console access with MFA, IAM roles for ECS tasks (no access keys), service control policies (SCPs) deny public S3 buckets. Encryption: S3 default encryption (SSE-S3), RDS encryption with customer-managed KMS keys, TLS 1.3 for all APIs (ACM certificates), secrets in AWS Secrets Manager with automatic 30-day rotation. Logging: CloudTrail all regions → S3 (7-year retention) → Splunk, VPC Flow Logs for network forensics, ECS container logs → CloudWatch, GuardDuty enabled (malware detection, crypto-mining alerts). Monitoring: CloudWatch dashboards (latency, errors, throughput), GuardDuty findings → SNS → PagerDuty, AWS Config rules for CIS benchmark (90% compliance target), Security Hub aggregates findings. Compliance: SOC 2 control mapping (CC6.1 logical access = IAM policies, CC6.6 encryption = KMS), automated evidence (Config snapshots, CloudTrail logs), quarterly penetration testing. HA/DR: RDS Multi-AZ, ECS tasks across 3 AZs, Route53 health checks with failover to us-west-2 (RTO 4h, RPO 1h), automated RDS snapshots cross-region. Cost: ~$5K/month (ECS, RDS, data transfer, GuardDuty).

### Example 2: Financial Services Multi-Cloud (PCI-DSS)
**Prompt:** Design secure multi-cloud architecture for PaymentCorp processing payment card data across AWS (primary) and Azure (DR) achieving PCI-DSS 4.0 compliance.

**Expected Output:** Network: AWS VPC dedicated to PCI CDE (cardholder data environment), network segmentation (CDE isolated from corporate), AWS Transit Gateway for hub-and-spoke, Azure VNet in West US 2 for DR, site-to-site VPN AWS-Azure (IPsec encrypted). CDE security: dedicated VPC (10.1.0.0/16) with no internet gateway, private subnet only, VPC endpoints for AWS services (S3, DynamoDB no internet), security groups deny all except required ports (HTTPS 443, database 5432), network ACLs as second layer, flow logs to S3 for PCI audit. IAM: centralized through Okta, CyberArk PAM for privileged access (no direct SSH/RDP), JIT access with 4-hour expiration, audit all CDE access in CloudTrail data events. Encryption: RDS encryption with CloudHSM for PCI compliance (FIPS 140-2 Level 3), TLS 1.3 for all connections, encryption at application layer for PAN (primary account number), tokenization for stored card data. Logging: CloudTrail + Azure Activity Log → Splunk (SIEM), 7-year retention for SOX, alert on CDE access, quarterly log reviews for PCI. Compliance: PCI-DSS 4.0 control mapping (Requirement 1 = network segmentation, Requirement 3 = encryption, Requirement 10 = logging), quarterly external ASV scans, annual penetration test by QSA, AWS Config rules for PCI controls. DR: Azure as warm standby (RTO 1h, RPO 15min), RDS cross-region replication to Azure Cosmos DB, automated failover via Route53 + Azure Traffic Manager, quarterly DR test. Multi-cloud orchestration: Terraform for both AWS and Azure, unified monitoring in Splunk, federated identity via Okta.

### Example 3: Healthcare Platform on Azure (HIPAA)
**Prompt:** Design secure Azure architecture for HealthConnect telehealth platform integrating with Epic EHR, processing PHI with HIPAA compliance.

**Expected Output:** Network: Azure VNet in East US 2 + West US 2 (zone-redundant), private endpoints for all PaaS services (App Service, Cosmos DB, Functions, Storage—no public internet access), Azure Firewall for egress filtering, no NSG allowing internet inbound except WAF. IAM: Azure AD B2C for patient authentication (MFA via SMS/email), Azure AD for clinician access (conditional access policies requiring compliant devices), managed identities for applications (no service principal secrets), PIM (Privileged Identity Management) for admin access with approval. Encryption: customer-managed keys in Azure Key Vault (FIPS 140-2 for HIPAA), Cosmos DB encryption at rest, TLS 1.3 for all connections, PHI encrypted at application layer (AES-256), Storage Account encryption with CMK. Logging: Azure Activity Log (10-year retention for HIPAA), NSG Flow Logs, App Service diagnostic logs → Log Analytics → Sentinel, Azure Monitor alerts for suspicious PHI access. Compliance: HIPAA BAA with Microsoft, PHI access logging (who accessed which patient record), encrypt PHI at rest and in transit, audit logs for breach notification, Azure Policy enforces encryption and private endpoints. Sentinel: healthcare threat detection rules (mass PHI download, after-hours access anomalies, geolocation anomalies), automated response (disable user account, alert compliance officer), integration with Epic audit logs via API. HA: zone-redundant App Service (99.95% SLA), Cosmos DB multi-region write (active-active), Azure Front Door for global load balancing, automatic failover between regions. DR: geo-redundant storage for backups, quarterly DR drill (failover to West US 2), RTO 2h/RPO 15min.

---

## Cross-References

- [Kubernetes Security](kubernetes-security.md) - Container-specific security controls
- [Security Architecture](../Cybersecurity/security-architecture.md) - Enterprise security architecture principles
- [Cloud Architecture](../../technology/DevOps-Cloud/cloud-architecture.md) - Cloud infrastructure patterns
