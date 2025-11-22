---
category: security
last_updated: 2025-11-22
title: Cloud Security Architecture Framework
tags:
- security
- cloud
- infrastructure
- compliance
use_cases:
- Designing secure cloud infrastructure and architecture
- Implementing cloud security controls and best practices
- Multi-cloud security strategy development
- Cloud compliance and governance frameworks
related_templates:
- security/Cybersecurity/security-architecture.md
- technology/DevOps-Cloud/cloud-architecture.md
- security/Cloud-Security/kubernetes-security.md
industries:
- finance
- government
- healthcare
- technology
type: template
difficulty: intermediate
slug: cloud-security-architecture
---

# Cloud Security Architecture Framework

## Purpose
Comprehensive framework for designing secure cloud infrastructure, implementing security controls across IaaS/PaaS/SaaS, ensuring compliance, and establishing governance for AWS, Azure, GCP, and multi-cloud environments.

## Quick Start

**Need to design secure cloud architecture?** Use this minimal example:

### Minimal Example
\`\`\`
Design secure AWS architecture for a web application handling customer PII, including VPC design, IAM policies, encryption strategy, logging/monitoring, and compliance controls for SOC2 and GDPR requirements.
\`\`\`

### When to Use This
- Designing new cloud infrastructure from scratch
- Migrating applications to cloud with security requirements
- Implementing security controls in existing cloud environments
- Multi-cloud security strategy development

### Basic 3-Step Workflow
1. **Define Security Requirements** - Identify data classification, compliance needs, threat model (30-45 min)
2. **Design Security Controls** - Network segmentation, IAM, encryption, monitoring (1-2 hours)
3. **Implement & Validate** - Deploy controls, test security posture, document architecture (2-4 hours)

**Time to complete**: 4-6 hours for initial architecture, ongoing refinement

---

## Template

\`\`\`markdown
I need to design a secure cloud security architecture. Please provide comprehensive cloud security design and implementation guidance.

## CLOUD ENVIRONMENT CONTEXT

### Infrastructure Details
- Cloud provider: [AWS_AZURE_GCP_MULTI_CLOUD_HYBRID]
- Deployment model: [PUBLIC_PRIVATE_HYBRID_COMMUNITY]
- Services used: [COMPUTE_STORAGE_DATABASE_SERVERLESS_CONTAINERS_PAAS]
- Workload type: [WEB_APP_DATA_ANALYTICS_ML_IOT_MICROSERVICES]
- Geographic regions: [REGIONS_AND_AVAILABILITY_ZONES]
- High availability needs: [YES_NO_PARTIAL]
- Disaster recovery RPO/RTO: [SPECIFY_REQUIREMENTS]

### Data & Compliance
- Data types: [PUBLIC_INTERNAL_CONFIDENTIAL_PII_PHI_PCI]
- Data residency requirements: [REGIONS_OR_COUNTRIES]
- Compliance frameworks: [SOC2_ISO27001_HIPAA_PCI_DSS_GDPR_CCPA_FedRAMP]
- Audit requirements: [FREQUENCY_AND_SCOPE]
- Data retention policies: [DURATION_AND_REQUIREMENTS]
- Encryption requirements: [AT_REST_IN_TRANSIT_IN_USE]

### Security Requirements
- Network isolation: [PUBLIC_PRIVATE_FULLY_ISOLATED]
- Identity management: [SSO_MFA_FEDERATION_DIRECTORY_INTEGRATION]
- Privileged access: [BASTION_VPN_PAM_JUST_IN_TIME]
- Threat detection: [IDS_IPS_SIEM_CLOUDNATIVE_THIRD_PARTY]
- Incident response: [AUTOMATED_MANUAL_HYBRID]
- Security monitoring: [24x7_BUSINESS_HOURS_AUTOMATED]

## CLOUD SECURITY ARCHITECTURE DESIGN

### 1. Network Security Architecture
Design secure network architecture including:

**VPC/VNet Design:**
- Network segmentation strategy (public, private, data subnets)
- CIDR block allocation
- Availability zone distribution
- Peering and connectivity requirements

**Traffic Control:**
- Security groups / Network ACLs configuration
- Web Application Firewall (WAF) rules
- DDoS protection (AWS Shield, Azure DDoS, Cloud Armor)
- Load balancer security
- API Gateway security

**Connectivity:**
- VPN connectivity (site-to-site, client VPN)
- Direct Connect / ExpressRoute / Cloud Interconnect
- Service endpoints / Private Link
- DNS security (Route53, Azure DNS, Cloud DNS)

Provide:
- Network architecture diagram
- Security group/ACL rules
- Traffic flow documentation
- Zero-trust network principles

### 2. Identity & Access Management (IAM)
Design comprehensive IAM strategy:

**Authentication:**
- User authentication mechanisms
- MFA requirements and implementation
- Service account management
- API key and token management
- Federation with corporate directory (SAML, OIDC)

**Authorization:**
- Least privilege access policies
- Role-based access control (RBAC) design
- Resource-based policies
- Permission boundaries
- Cross-account access patterns
- Temporary credentials (STS, managed identities)

**Privileged Access:**
- Root/admin account protection
- Privileged access management (PAM)
- Just-in-time (JIT) access
- Bastion hosts / jump servers
- Session recording and auditing

Provide:
- IAM policy examples
- Role hierarchy and assignments
- Service account strategy
- Privileged access workflow

### 3. Data Protection & Encryption
Design comprehensive data protection:

**Encryption at Rest:**
- Storage encryption (EBS, S3, Azure Storage, GCS)
- Database encryption (RDS, DynamoDB, Cosmos DB, Cloud SQL)
- Key management strategy (KMS, Key Vault, Cloud KMS)
- Customer-managed keys vs cloud-managed keys
- Encryption key rotation policies

**Encryption in Transit:**
- TLS/SSL certificate management
- API encryption requirements
- Database connection encryption
- Inter-service communication security
- Certificate lifecycle management

**Data Loss Prevention:**
- Data classification and tagging
- Access logging and monitoring
- Data exfiltration prevention
- Backup encryption and security
- Secure data deletion procedures

Provide:
- Encryption architecture diagram
- Key management workflow
- Certificate management strategy
- Data classification scheme

### 4. Logging, Monitoring & Threat Detection
Design security visibility architecture:

**Centralized Logging:**
- CloudTrail / Activity Log / Cloud Audit Logs configuration
- VPC Flow Logs / NSG Flow Logs
- Application and system logs
- Log aggregation strategy (CloudWatch, Monitor, Logging)
- Log retention and compliance
- SIEM integration

**Security Monitoring:**
- GuardDuty / Defender / Security Command Center
- Config / Policy / Security Health Analytics
- Inspector / Defender for Cloud / Security Scanner
- Anomaly detection and alerting
- Security metrics and dashboards

**Incident Response:**
- Automated response playbooks
- Alert escalation procedures
- Forensics and investigation tools
- Backup and recovery procedures
- Communication and reporting workflows

Provide:
- Monitoring architecture
- Alert configuration examples
- Incident response runbooks
- Log analysis queries

### 5. Compute Security
Secure compute resources:

**VM/Instance Security:**
- Hardened AMI / VM images
- Patch management strategy
- Antivirus / endpoint protection
- Host-based firewalls
- Configuration management
- Vulnerability scanning

**Container Security:**
- Container image scanning
- Runtime security (Falco, Aqua)
- Kubernetes security (pod security, RBAC, network policies)
- Registry security and access control
- Secrets management for containers

**Serverless Security:**
- Function IAM roles and permissions
- Code and dependency scanning
- Environment variable security
- API Gateway security
- Function timeout and resource limits

Provide:
- Baseline hardening configurations
- Patch management workflow
- Container security policies
- Serverless security checklist

### 6. Application Security
Secure applications in cloud:

**Application Layer:**
- Web application firewall (WAF) rules
- DDoS protection
- Bot management
- Rate limiting and throttling
- Content delivery network (CDN) security

**API Security:**
- API authentication and authorization
- API Gateway configuration
- Rate limiting and quota management
- API versioning and deprecation
- Request/response validation

**Secrets Management:**
- Secrets Manager / Key Vault / Secret Manager
- Application credential rotation
- Database connection security
- API key management
- Certificate storage and retrieval

Provide:
- WAF rule configurations
- API security policies
- Secrets management architecture
- Application security controls

### 7. Compliance & Governance
Implement compliance controls:

**Compliance Frameworks:**
- Control mapping (SOC2, ISO 27001, HIPAA, PCI-DSS)
- Evidence collection automation
- Compliance reporting
- Audit trail maintenance

**Governance:**
- Resource tagging strategy
- Cost allocation and monitoring
- Policy enforcement (SCP, Azure Policy, Organization Policies)
- Automated compliance checking
- Configuration drift detection

**Security Standards:**
- CIS Benchmarks implementation
- Cloud security best practices
- Security baseline documentation
- Regular security assessments

Provide:
- Compliance control matrix
- Policy-as-code examples
- Tagging strategy
- Compliance automation approach

### 8. Disaster Recovery & Business Continuity
Design resilience and recovery:

**Backup Strategy:**
- Automated backup configuration
- Cross-region backup replication
- Backup encryption and access control
- Backup testing procedures
- Retention policies

**High Availability:**
- Multi-AZ/multi-region architecture
- Auto-scaling configuration
- Load balancing strategy
- Database replication
- Failover procedures

**Disaster Recovery:**
- DR site configuration
- RTO/RPO achievement strategy
- Failover and failback procedures
- DR testing schedule
- Communication plan

Provide:
- Backup and recovery architecture
- HA configuration examples
- DR runbooks
- Testing schedule and procedures

## CLOUD-SPECIFIC SECURITY

### AWS Security
- IAM best practices and policies
- VPC security configuration
- GuardDuty, Config, Inspector setup
- S3 bucket security
- RDS/DynamoDB security
- Lambda security
- CloudTrail logging

### Azure Security
- Azure AD and conditional access
- Network Security Groups and ASGs
- Azure Security Center / Defender
- Storage account security
- Cosmos DB / SQL Database security
- Azure Functions security
- Activity Log and diagnostics

### GCP Security
- Cloud IAM and service accounts
- VPC Service Controls
- Security Command Center
- Cloud Storage security
- Cloud SQL security
- Cloud Functions security
- Cloud Audit Logs

### Multi-Cloud Considerations
- Unified identity management
- Cross-cloud networking
- Centralized security monitoring
- Consistent policy enforcement
- Multi-cloud SIEM integration

## SECURITY VALIDATION

Provide validation approach:

1. **Security Testing**
   - Penetration testing procedures
   - Vulnerability scanning schedule
   - Configuration auditing
   - Compliance validation

2. **Continuous Monitoring**
   - Real-time threat detection
   - Configuration drift monitoring
   - Compliance status tracking
   - Security posture scoring

3. **Regular Reviews**
   - Architecture review schedule
   - Access review procedures
   - Policy update process
   - Incident post-mortems

## OUTPUT REQUIREMENTS

Please provide:

1. **Architecture Diagrams**
   - Network topology
   - Data flow diagrams
   - Security zones and boundaries
   - Integration points

2. **Implementation Guides**
   - Step-by-step deployment
   - Configuration templates
   - Infrastructure-as-code examples
   - Validation procedures

3. **Security Policies**
   - IAM policies
   - Network security rules
   - Encryption policies
   - Monitoring configurations

4. **Operational Runbooks**
   - Incident response procedures
   - Backup and recovery steps
   - Patching procedures
   - Access provisioning/deprovisioning

5. **Compliance Documentation**
   - Control mapping
   - Evidence requirements
   - Audit procedures
   - Reporting templates
\`\`\`

---

## Usage Examples

### Example 1: Startup SaaS Application (AWS)

**Context:** B2B SaaS platform processing customer PII, 50 employees, SOC 2 compliance required

\`\`\`
Design secure AWS architecture for CustomerHub SaaS application handling customer PII
with SOC 2 Type II compliance requirements and hybrid workforce.

CLOUD ENVIRONMENT CONTEXT:
- Cloud provider: AWS
- Services: EC2, RDS PostgreSQL, S3, Lambda, ECS
- Workload: Multi-tenant SaaS with REST APIs
- Regions: us-east-1 (primary), us-west-2 (DR)
- HA needs: Yes (99.9% uptime SLA)
- DR RPO/RTO: 1 hour / 4 hours

Data & Compliance:
- Data types: Customer PII (names, emails, company data)
- Compliance: SOC 2 Type II, GDPR (EU customers)
- Encryption: AES-256 at rest, TLS 1.3 in transit

Security Requirements:
- Network: Private subnets for data tier, public for ALB only
- Identity: Okta SSO with SAML, MFA enforced
- Privileged access: AWS SSM Session Manager (no bastion)
- Monitoring: 24/7 automated with PagerDuty integration
\`\`\`

**Expected Output:**
- VPC with 3-tier architecture (public/private/data subnets)
- IAM roles with least privilege, no long-lived credentials
- RDS encryption, S3 bucket policies blocking public access
- GuardDuty, Config, CloudTrail enabled
- WAF with OWASP Core Rule Set

### Example 2: Financial Services Multi-Cloud (AWS + Azure)

**Context:** Mid-size financial company, PCI-DSS and SOX compliance, multi-cloud for resilience

\`\`\`
Design secure multi-cloud architecture for PaymentCorp spanning AWS (primary) and
Azure (DR/burst), processing payment card data with PCI-DSS 4.0 compliance.

CLOUD ENVIRONMENT CONTEXT:
- Cloud providers: AWS (primary), Azure (DR + burst capacity)
- Services: EKS, RDS, Lambda (AWS); AKS, Cosmos DB (Azure)
- Workload: Payment processing microservices
- HA: Active-passive failover, 99.99% uptime
- DR RPO/RTO: 15 minutes / 1 hour

Data & Compliance:
- Data types: PCI (card data), PII, financial transactions
- Compliance: PCI-DSS 4.0, SOX, GLBA
- Data residency: US only

Security Requirements:
- Network segmentation: CDE isolated, micro-segmentation
- Identity: Centralized IAM (Okta), cross-cloud federation
- Privileged access: CyberArk PAM, JIT access
- Monitoring: Splunk SIEM (cloud-agnostic), 24/7 SOC
\`\`\`

**Expected Output:**
- CDE network isolation with dedicated VPC/VNet
- Cross-cloud identity federation through Okta
- HSM-backed key management for encryption keys
- Centralized logging to Splunk across both clouds
- PCI-DSS control mapping with evidence automation

### Example 3: Healthcare Platform (Azure)

**Context:** Digital health startup with telehealth and EHR integration, HIPAA compliance

\`\`\`
Design secure Azure architecture for HealthConnect telehealth platform integrating
with Epic EHR systems, processing PHI with HIPAA compliance requirements.

CLOUD ENVIRONMENT CONTEXT:
- Cloud provider: Azure (HIPAA BAA in place)
- Services: Azure App Service, Cosmos DB, Azure Functions, API Management
- Workload: Telehealth video + patient portal + EHR integration
- Regions: East US 2 (primary), West US 2 (DR)
- HA: Zone-redundant, 99.95% uptime

Data & Compliance:
- Data types: PHI (patient records, prescriptions), video recordings
- Compliance: HIPAA, HITECH, state privacy laws
- Data residency: US only (ITAR-like restrictions)

Security Requirements:
- Network: Private endpoints for all PaaS services
- Identity: Azure AD B2C (patients), Azure AD (staff)
- Access: Conditional access policies, device compliance
- Monitoring: Microsoft Sentinel, anomaly detection
\`\`\`

**Expected Output:**
- Private endpoints eliminating public PaaS exposure
- Azure AD Conditional Access with device compliance
- PHI encryption with customer-managed keys
- Sentinel with healthcare-specific detection rules
- HIPAA control mapping and BAA documentation

## Best Practices

1. **Start with threat modeling** - Understand what you're protecting before designing controls
2. **Implement least privilege everywhere** - IAM, network, and application layers
3. **Encrypt by default** - All data at rest and in transit
4. **Monitor continuously** - Real-time threat detection and alerting
5. **Automate security controls** - Infrastructure-as-code with security policies embedded
