---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- design
- development
- ai-ml
- management
- security
- strategy
title: Infrastructure as Code (IaC) Development Template
use_cases:
- General application
- Professional use
- Project implementation
industries:
- finance
- government
- healthcare
- manufacturing
- technology
type: template
difficulty: intermediate
slug: devops-infrastructure-as-code
---

# Infrastructure as Code (IaC) Development Template

## Overview
This comprehensive template enables organizations to develop, deploy, and manage infrastructure using code-based approaches across multiple cloud providers and platforms. It covers everything from basic resource provisioning to advanced multi-cloud orchestration strategies.

## Quick DevOps IaC Prompt
Create IaC for [cloud: AWS/Azure/GCP] using [Terraform/CloudFormation/Pulumi]. Resources: [VPC/networking], [compute: EC2/ECS/Lambda], [database: RDS/DynamoDB], [storage: S3]. Requirements: [environments: dev/staging/prod], [regions]. Structure: modular design, remote state with locking, CI/CD integration (plan on PR, apply on merge). Include: tagging strategy, encryption, least-privilege IAM.

## Quick Start

**Get started with Infrastructure as Code in 5 steps:**

1. **Choose Your IaC Tool**: Select Terraform, CloudFormation, or Pulumi based on your cloud provider and team expertise
2. **Set Up State Management**: Configure remote state backend (S3, Azure Blob, or Terraform Cloud) with encryption and locking
3. **Define Core Infrastructure**: Create modular code for VPC/networking, compute resources, and storage with proper variable management
4. **Implement CI/CD Pipeline**: Integrate IaC validation, planning, and deployment into your existing CI/CD workflow
5. **Enable Monitoring**: Deploy infrastructure monitoring, drift detection, and compliance scanning from day one

**First Infrastructure Deployment:**
```bash
# Initialize provider and backend
terraform init

# Validate syntax and plan changes
terraform validate && terraform plan -out=tfplan

# Apply infrastructure changes
terraform apply tfplan

# Verify deployment and outputs
terraform output
```

---

## Section 1: Infrastructure Architecture & Design

### Cloud Infrastructure Framework
Please develop an Infrastructure as Code solution for [ORGANIZATION_NAME] with the following specifications:

**Primary Requirements:**
- Target cloud provider: [PRIMARY_CLOUD_PROVIDER] (AWS/Azure/GCP/Multi-Cloud)
- Secondary providers: [SECONDARY_CLOUD_PROVIDERS]
- Infrastructure scale: [INFRASTRUCTURE_SCALE] (Small/Medium/Large/Enterprise)
- Environment count: [ENVIRONMENT_COUNT] (Dev/Staging/Prod/[CUSTOM_ENVIRONMENTS])
- Geographic regions: [TARGET_REGIONS]
- Compliance requirements: [COMPLIANCE_STANDARDS] (SOC2/HIPAA/PCI-DSS/GDPR/[CUSTOM_COMPLIANCE])
- Budget constraints: [BUDGET_RANGE]
- Timeline: [PROJECT_TIMELINE]

**Architecture Components:**
- Network topology: [NETWORK_ARCHITECTURE] (VPC/VNet/Hub-Spoke/Mesh/[CUSTOM_TOPOLOGY])
- Compute resources: [COMPUTE_TYPES] (EC2/VM/Container/Serverless/[HYBRID_COMPUTE])
- Storage solutions: [STORAGE_TYPES] (Block/Object/File/Database/[CUSTOM_STORAGE])
- Load balancing: [LOAD_BALANCER_TYPE] (Application/Network/Global/[CUSTOM_LB])
- Security groups: [SECURITY_GROUP_STRATEGY]
- DNS management: [DNS_PROVIDER] (Route53/CloudDNS/Azure DNS/[CUSTOM_DNS])
- CDN integration: [CDN_PROVIDER] (CloudFront/CloudFlare/Azure CDN/[CUSTOM_CDN])
- Monitoring stack: [MONITORING_TOOLS] (CloudWatch/Prometheus/DataDog/[CUSTOM_MONITORING])

### Resource Provisioning Strategy
**Core Infrastructure:**
- Identity management: [IDENTITY_PROVIDER] (AWS IAM/Azure AD/GCP IAM/[CUSTOM_IDENTITY])
- Access controls: [ACCESS_CONTROL_MODEL] (RBAC/ABAC/[CUSTOM_ACCESS])
- Encryption standards: [ENCRYPTION_REQUIREMENTS] (At-rest/In-transit/[CUSTOM_ENCRYPTION])
- Backup strategy: [BACKUP_APPROACH] (Automated/Scheduled/Real-time/[CUSTOM_BACKUP])
- Disaster recovery: [DR_STRATEGY] (Multi-region/Multi-zone/[CUSTOM_DR])
- Cost optimization: [COST_OPTIMIZATION_METHODS]
- Resource tagging: [TAGGING_STRATEGY]
- Lifecycle management: [RESOURCE_LIFECYCLE_POLICY]

---

## Section 2: IaC Tool Selection & Configuration

### Tool Selection Matrix
**Primary IaC Tool:** [PRIMARY_IAC_TOOL] (Terraform/CloudFormation/ARM/Pulumi/CDK/Ansible)
**Secondary Tools:** [SECONDARY_IAC_TOOLS]
**Configuration Management:** [CONFIG_MGMT_TOOL] (Ansible/Chef/Puppet/SaltStack)
**Container Orchestration:** [CONTAINER_PLATFORM] (Kubernetes/Docker Swarm/ECS/AKS/GKE)
**Service Mesh:** [SERVICE_MESH] (Istio/Linkerd/Consul Connect/[CUSTOM_MESH])
**CI/CD Platform:** [CICD_PLATFORM] (Jenkins/GitLab CI/Azure DevOps/GitHub Actions/CircleCI)

### Tool Configuration Parameters
**Terraform Configuration:**
- Provider versions: [TERRAFORM_PROVIDER_VERSIONS]
- State management: [STATE_BACKEND] (S3/Azure Blob/GCS/Terraform Cloud)
- Module structure: [MODULE_ORGANIZATION]
- Workspace strategy: [WORKSPACE_STRATEGY]
- Variable management: [VARIABLE_MANAGEMENT_APPROACH]
- Secret handling: [SECRET_MANAGEMENT] (Vault/Key Vault/Secret Manager/[CUSTOM_SECRET_MGR])
- Remote execution: [REMOTE_EXECUTION_PLATFORM]
- State locking: [STATE_LOCKING_MECHANISM]

**CloudFormation Configuration:**
- Template format: [CF_TEMPLATE_FORMAT] (JSON/YAML)
- Stack organization: [STACK_ORGANIZATION_STRATEGY]
- Parameter management: [CF_PARAMETER_STRATEGY]
- Cross-stack references: [CROSS_STACK_REFERENCE_APPROACH]
- Nested stacks: [NESTED_STACK_STRATEGY]
- Change sets: [CHANGE_SET_POLICY]
- Stack policies: [STACK_PROTECTION_POLICIES]
- Rollback configuration: [ROLLBACK_STRATEGY]

---

## Section 3: Code Organization & Module Development

### Repository Structure
```
[PROJECT_NAME]/
├── [ENVIRONMENT_FOLDERS]/
├── [MODULE_DIRECTORIES]/
├── [SHARED_COMPONENTS]/
├── [CONFIGURATION_FILES]/
└── [DOCUMENTATION_PATH]/
```

**Module Development Framework:**
- Module naming convention: [MODULE_NAMING_CONVENTION]
- Input variable standards: [INPUT_VARIABLE_STANDARDS]
- Output specifications: [OUTPUT_SPECIFICATIONS]
- Documentation requirements: [MODULE_DOCUMENTATION_REQUIREMENTS]
- Testing framework: [MODULE_TESTING_FRAMEWORK] (Terratest/InSpec/Kitchen/[CUSTOM_TESTING])
- Version control: [MODULE_VERSIONING_STRATEGY]
- Registry usage: [MODULE_REGISTRY] (Terraform Registry/Private Registry/[CUSTOM_REGISTRY])
- Dependency management: [DEPENDENCY_MANAGEMENT_APPROACH]

### Configuration Management
**Environment Configuration:**
- Development settings: [DEV_ENVIRONMENT_CONFIG]
- Staging parameters: [STAGING_ENVIRONMENT_CONFIG]
- Production specifications: [PROD_ENVIRONMENT_CONFIG]
- Custom environments: [CUSTOM_ENVIRONMENT_CONFIGS]
- Variable precedence: [VARIABLE_PRECEDENCE_ORDER]
- Configuration validation: [CONFIG_VALIDATION_RULES]
- Environment promotion: [ENVIRONMENT_PROMOTION_PROCESS]
- Configuration drift detection: [DRIFT_DETECTION_STRATEGY]

---

## Section 4: Security & Compliance Implementation

### Security Framework Integration
**Infrastructure Security:**
- Security baseline: [SECURITY_BASELINE_STANDARDS]
- Network segmentation: [NETWORK_SEGMENTATION_STRATEGY]
- Access control implementation: [ACCESS_CONTROL_IMPLEMENTATION]
- Encryption key management: [KEY_MANAGEMENT_STRATEGY]
- Certificate management: [CERTIFICATE_MANAGEMENT_APPROACH]
- Vulnerability scanning: [VULNERABILITY_SCANNING_TOOLS]
- Security monitoring: [SECURITY_MONITORING_SOLUTIONS]
- Incident response: [IR_INTEGRATION_APPROACH]

### Compliance Automation
**Compliance Standards:**
- Regulatory requirements: [SPECIFIC_REGULATORY_REQUIREMENTS]
- Audit trail configuration: [AUDIT_TRAIL_REQUIREMENTS]
- Data residency: [DATA_RESIDENCY_REQUIREMENTS]
- Retention policies: [DATA_RETENTION_POLICIES]
- Privacy controls: [PRIVACY_CONTROL_IMPLEMENTATION]
- Compliance monitoring: [COMPLIANCE_MONITORING_TOOLS]
- Reporting automation: [COMPLIANCE_REPORTING_AUTOMATION]
- Remediation workflows: [COMPLIANCE_REMEDIATION_PROCESSES]

### Policy as Code
- Policy definition: [POLICY_DEFINITION_LANGUAGE] (OPA/Sentinel/Azure Policy/[CUSTOM_POLICY])
- Policy enforcement: [POLICY_ENFORCEMENT_POINTS]
- Policy testing: [POLICY_TESTING_FRAMEWORK]
- Policy versioning: [POLICY_VERSION_CONTROL]
- Exception handling: [POLICY_EXCEPTION_PROCESS]
- Policy monitoring: [POLICY_MONITORING_APPROACH]
- Violation responses: [POLICY_VIOLATION_RESPONSES]
- Governance integration: [GOVERNANCE_INTEGRATION_STRATEGY]

---

## Section 5: Deployment & Orchestration

### CI/CD Pipeline Integration
**Pipeline Configuration:**
- Source control integration: [SOURCE_CONTROL_SYSTEM] (Git/SVN/[CUSTOM_VCS])
- Branching strategy: [BRANCHING_STRATEGY] (GitFlow/GitHub Flow/[CUSTOM_BRANCHING])
- Trigger mechanisms: [PIPELINE_TRIGGERS]
- Build stages: [BUILD_STAGE_CONFIGURATION]
- Testing phases: [TESTING_PHASE_CONFIGURATION]
- Deployment stages: [DEPLOYMENT_STAGE_CONFIGURATION]
- Approval processes: [APPROVAL_PROCESS_REQUIREMENTS]
- Rollback mechanisms: [ROLLBACK_AUTOMATION_STRATEGY]

### Deployment Strategies
**Deployment Approaches:**
- Blue-green deployment: [BLUE_GREEN_IMPLEMENTATION]
- Canary deployment: [CANARY_DEPLOYMENT_STRATEGY]
- Rolling updates: [ROLLING_UPDATE_CONFIGURATION]
- Immutable infrastructure: [IMMUTABLE_INFRA_APPROACH]
- Multi-environment promotion: [MULTI_ENV_PROMOTION_PROCESS]
- Feature flags: [FEATURE_FLAG_INTEGRATION]
- Deployment validation: [DEPLOYMENT_VALIDATION_TESTS]
- Health checks: [HEALTH_CHECK_CONFIGURATION]

### Orchestration Automation
- Workflow orchestration: [WORKFLOW_ORCHESTRATION_TOOL]
- Job scheduling: [JOB_SCHEDULING_SYSTEM]
- Event-driven automation: [EVENT_DRIVEN_AUTOMATION]
- Dependency management: [DEPENDENCY_RESOLUTION]
- Parallel execution: [PARALLEL_EXECUTION_STRATEGY]
- Error handling: [ERROR_HANDLING_PROCEDURES]
- Notification systems: [NOTIFICATION_INTEGRATION]
- Metrics collection: [METRICS_COLLECTION_STRATEGY]

---

## Section 6: State Management & Data Persistence

### State Backend Configuration
**State Management Strategy:**
- Backend selection: [STATE_BACKEND_CHOICE]
- State encryption: [STATE_ENCRYPTION_METHOD]
- State versioning: [STATE_VERSIONING_APPROACH]
- Concurrent access: [CONCURRENT_ACCESS_CONTROL]
- State backup: [STATE_BACKUP_STRATEGY]
- State recovery: [STATE_RECOVERY_PROCEDURES]
- State migration: [STATE_MIGRATION_PROCESS]
- State validation: [STATE_VALIDATION_CHECKS]

### Data Management
**Data Persistence:**
- Database provisioning: [DATABASE_PROVISIONING_STRATEGY]
- Data migration: [DATA_MIGRATION_APPROACH]
- Backup automation: [BACKUP_AUTOMATION_CONFIGURATION]
- Point-in-time recovery: [PITR_IMPLEMENTATION]
- Cross-region replication: [CROSS_REGION_REPLICATION]
- Data archival: [DATA_ARCHIVAL_STRATEGY]
- Data lifecycle: [DATA_LIFECYCLE_MANAGEMENT]
- Performance optimization: [DATABASE_PERFORMANCE_OPTIMIZATION]

---

## Section 7: Monitoring & Observability

### Infrastructure Monitoring
**Monitoring Stack:**
- Metrics collection: [METRICS_COLLECTION_TOOLS]
- Log aggregation: [LOG_AGGREGATION_SOLUTION]
- Distributed tracing: [DISTRIBUTED_TRACING_IMPLEMENTATION]
- Dashboard configuration: [DASHBOARD_SETUP_REQUIREMENTS]
- Alerting rules: [ALERTING_RULE_CONFIGURATION]
- SLA definitions: [SLA_DEFINITIONS]
- Performance baselines: [PERFORMANCE_BASELINE_METRICS]
- Capacity planning: [CAPACITY_PLANNING_METRICS]

### Operational Intelligence
- Cost monitoring: [COST_MONITORING_IMPLEMENTATION]
- Resource utilization: [RESOURCE_UTILIZATION_TRACKING]
- Performance analytics: [PERFORMANCE_ANALYTICS_TOOLS]
- Trend analysis: [TREND_ANALYSIS_CONFIGURATION]
- Anomaly detection: [ANOMALY_DETECTION_SETUP]
- Predictive analytics: [PREDICTIVE_ANALYTICS_IMPLEMENTATION]
- Business metrics: [BUSINESS_METRICS_INTEGRATION]
- ROI tracking: [ROI_TRACKING_METHODOLOGY]

### Incident Management
- Incident detection: [INCIDENT_DETECTION_MECHANISMS]
- Escalation procedures: [ESCALATION_PROCEDURES]
- Response automation: [RESPONSE_AUTOMATION_WORKFLOWS]
- Communication protocols: [INCIDENT_COMMUNICATION_PROTOCOLS]
- Post-incident analysis: [POST_INCIDENT_ANALYSIS_PROCESS]
- Continuous improvement: [CONTINUOUS_IMPROVEMENT_PROCESS]
- Documentation requirements: [INCIDENT_DOCUMENTATION_REQUIREMENTS]
- Training programs: [INCIDENT_RESPONSE_TRAINING]

---

## Section 8: Testing & Validation

### Infrastructure Testing Framework
**Testing Strategy:**
- Unit testing: [UNIT_TESTING_APPROACH] (Terratest/InSpec/[CUSTOM_TESTING])
- Integration testing: [INTEGRATION_TESTING_STRATEGY]
- End-to-end testing: [E2E_TESTING_FRAMEWORK]
- Performance testing: [PERFORMANCE_TESTING_TOOLS]
- Security testing: [SECURITY_TESTING_INTEGRATION]
- Compliance testing: [COMPLIANCE_TESTING_AUTOMATION]
- Disaster recovery testing: [DR_TESTING_PROCEDURES]
- Chaos engineering: [CHAOS_ENGINEERING_IMPLEMENTATION]

### Validation Procedures
**Pre-deployment Validation:**
- Syntax validation: [SYNTAX_VALIDATION_TOOLS]
- Plan review: [PLAN_REVIEW_PROCESS]
- Cost estimation: [COST_ESTIMATION_VALIDATION]
- Security scan: [SECURITY_SCANNING_INTEGRATION]
- Compliance check: [COMPLIANCE_CHECKING_AUTOMATION]
- Resource limits: [RESOURCE_LIMIT_VALIDATION]
- Dependency verification: [DEPENDENCY_VERIFICATION_PROCESS]
- Environment readiness: [ENVIRONMENT_READINESS_CHECKS]

### Quality Assurance
- Code review standards: [CODE_REVIEW_STANDARDS]
- Documentation review: [DOCUMENTATION_REVIEW_PROCESS]
- Performance benchmarks: [PERFORMANCE_BENCHMARK_CRITERIA]
- Reliability testing: [RELIABILITY_TESTING_METHODOLOGY]
- Scalability validation: [SCALABILITY_VALIDATION_APPROACH]
- Maintainability assessment: [MAINTAINABILITY_ASSESSMENT_CRITERIA]
- Technical debt tracking: [TECHNICAL_DEBT_TRACKING]
- Quality metrics: [QUALITY_METRICS_COLLECTION]

---

## Section 9: Optimization & Cost Management

### Resource Optimization
**Cost Optimization Strategy:**
- Right-sizing analysis: [RIGHT_SIZING_ANALYSIS_APPROACH]
- Reserved instances: [RESERVED_INSTANCE_STRATEGY]
- Spot instances: [SPOT_INSTANCE_UTILIZATION]
- Auto-scaling configuration: [AUTO_SCALING_OPTIMIZATION]
- Storage optimization: [STORAGE_OPTIMIZATION_STRATEGY]
- Network optimization: [NETWORK_COST_OPTIMIZATION]
- Scheduling automation: [RESOURCE_SCHEDULING_AUTOMATION]
- Lifecycle policies: [RESOURCE_LIFECYCLE_OPTIMIZATION]

### Performance Optimization
- Compute optimization: [COMPUTE_PERFORMANCE_OPTIMIZATION]
- Storage performance: [STORAGE_PERFORMANCE_TUNING]
- Network performance: [NETWORK_PERFORMANCE_OPTIMIZATION]
- Database optimization: [DATABASE_PERFORMANCE_TUNING]
- Caching strategies: [CACHING_IMPLEMENTATION_STRATEGY]
- CDN configuration: [CDN_OPTIMIZATION_CONFIGURATION]
- Load balancing: [LOAD_BALANCING_OPTIMIZATION]
- Regional distribution: [REGIONAL_DISTRIBUTION_OPTIMIZATION]

### Governance & Best Practices
- Resource governance: [RESOURCE_GOVERNANCE_FRAMEWORK]
- Naming conventions: [RESOURCE_NAMING_CONVENTIONS]
- Tagging standards: [RESOURCE_TAGGING_STANDARDS]
- Access governance: [ACCESS_GOVERNANCE_POLICIES]
- Change management: [CHANGE_MANAGEMENT_PROCESS]
- Documentation standards: [DOCUMENTATION_STANDARDS]
- Training requirements: [TRAINING_REQUIREMENTS]
- Certification tracking: [CERTIFICATION_TRACKING_SYSTEM]

---

## Section 10: Migration & Modernization

### Migration Strategy
**Legacy System Migration:**
- Current state assessment: [CURRENT_STATE_ASSESSMENT_APPROACH]
- Migration planning: [MIGRATION_PLANNING_METHODOLOGY]
- Phased migration: [PHASED_MIGRATION_STRATEGY]
- Data migration: [DATA_MIGRATION_APPROACH]
- Application migration: [APPLICATION_MIGRATION_STRATEGY]
- Testing during migration: [MIGRATION_TESTING_STRATEGY]
- Rollback planning: [MIGRATION_ROLLBACK_PLANNING]
- Go-live procedures: [GO_LIVE_PROCEDURES]

### Modernization Framework
- Architecture modernization: [ARCHITECTURE_MODERNIZATION_APPROACH]
- Technology stack updates: [TECHNOLOGY_STACK_MODERNIZATION]
- Process modernization: [PROCESS_MODERNIZATION_STRATEGY]
- Team skill development: [TEAM_SKILL_DEVELOPMENT_PLAN]
- Tool modernization: [TOOL_MODERNIZATION_ROADMAP]
- Automation enhancement: [AUTOMATION_ENHANCEMENT_PLAN]
- Integration modernization: [INTEGRATION_MODERNIZATION_APPROACH]
- Security modernization: [SECURITY_MODERNIZATION_STRATEGY]

### Continuous Improvement
- Feedback loops: [FEEDBACK_LOOP_IMPLEMENTATION]
- Performance metrics: [PERFORMANCE_METRICS_TRACKING]
- Innovation pipeline: [INNOVATION_PIPELINE_PROCESS]
- Technology evaluation: [TECHNOLOGY_EVALUATION_PROCESS]
- Best practice sharing: [BEST_PRACTICE_SHARING_MECHANISMS]
- Community engagement: [COMMUNITY_ENGAGEMENT_STRATEGY]
- Vendor relationships: [VENDOR_RELATIONSHIP_MANAGEMENT]
- Future roadmap: [FUTURE_ROADMAP_PLANNING]

---

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: Multi-Cloud Enterprise Infrastructure
```yaml
# Configuration for large enterprise with multi-cloud requirements
organization_name: "Global Enterprise Corp"
primary_cloud_provider: "AWS"
secondary_cloud_providers: ["Azure", "GCP"]
infrastructure_scale: "Enterprise"
environment_count: ["Dev", "Test", "Staging", "Prod", "DR"]
target_regions: ["us-east-1", "eu-west-1", "ap-southeast-1"]
compliance_standards: ["SOC2", "HIPAA", "GDPR"]
network_architecture: "Hub-Spoke"
primary_iac_tool: "Terraform"
state_backend: "S3"
monitoring_tools: ["CloudWatch", "Prometheus", "DataDog"]
```

### Example 2: Startup Rapid Deployment
```yaml
# Configuration for startup with rapid deployment needs
organization_name: "TechStart Innovations"
primary_cloud_provider: "AWS"
infrastructure_scale: "Medium"
environment_count: ["Dev", "Prod"]
target_regions: ["us-west-2"]
compliance_standards: ["SOC2"]
network_architecture: "VPC"
primary_iac_tool: "CDK"
cicd_platform: "GitHub Actions"
monitoring_tools: ["CloudWatch"]
```

### Example 3: Government Compliance Infrastructure
```yaml
# Configuration for government with strict compliance
organization_name: "Federal Agency X"
primary_cloud_provider: "AWS GovCloud"
infrastructure_scale: "Large"
compliance_standards: ["FedRAMP", "FISMA", "NIST"]
encryption_requirements: ["At-rest", "In-transit", "End-to-end"]
network_architecture: "Zero-Trust"
security_baseline_standards: ["CIS Benchmarks", "NIST Framework"]
primary_iac_tool: "CloudFormation"
```

---



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Infrastructure as Code (IaC) Development Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/DevOps & Cloud](../../technology/DevOps & Cloud/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **General application**: Combine this template with related analytics and strategy frameworks
- **Professional use**: Combine this template with related analytics and strategy frameworks
- **Project implementation**: Combine this template with related analytics and strategy frameworks

## Customization Options

### Option 1: Cloud Provider Adaptation
Customize the template for specific cloud providers by:
- Adjusting resource types and configurations
- Modifying service integrations
- Adapting compliance frameworks
- Updating cost optimization strategies
- Changing monitoring and alerting approaches

### Option 2: Scale Customization
Adapt the template for different organizational scales:
- **Small Scale:** Simplified configurations, minimal environments
- **Medium Scale:** Balanced complexity, multiple environments
- **Large Scale:** Advanced features, comprehensive governance
- **Enterprise Scale:** Full automation, extensive compliance

### Option 3: Industry Specialization
Tailor the template for specific industries:
- **Financial Services:** Enhanced security, regulatory compliance
- **Healthcare:** HIPAA compliance, data privacy focus
- **Government:** FedRAMP, security controls
- **Retail:** Scalability, performance optimization
- **Manufacturing:** Industrial IoT integration

### Option 4: Deployment Model Customization
Adjust for different deployment models:
- **Public Cloud:** Full cloud-native services
- **Private Cloud:** On-premises focus
- **Hybrid Cloud:** Multi-environment integration
- **Multi-Cloud:** Cross-provider strategies

### Option 5: Maturity Level Adaptation
Customize based on organizational maturity:
- **Beginner:** Basic implementations, learning focus
- **Intermediate:** Standard practices, process improvement
- **Advanced:** Sophisticated automation, optimization
- **Expert:** Innovation, cutting-edge practices

---

*This Infrastructure as Code template provides a comprehensive framework for organizations to implement robust, scalable, and secure infrastructure automation. Each variable should be carefully considered and customized based on specific organizational requirements, technical constraints, and business objectives.*

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ORGANIZATION_NAME]` | Name of the organization | "John Smith" |
| `[PRIMARY_CLOUD_PROVIDER]` | Specify the primary cloud provider | "AWS", "Azure", "GCP", "Multi-cloud" |
| `[SECONDARY_CLOUD_PROVIDERS]` | Specify the secondary cloud providers | "Azure for DR", "GCP for ML workloads", "On-premises VMware", "None" |
| `[INFRASTRUCTURE_SCALE]` | Specify the infrastructure scale | "Small (1-10 services)", "Medium (10-50)", "Large (50-200)", "Enterprise (200+)" |
| `[ENVIRONMENT_COUNT]` | Specify the environment count | "10" |
| `[CUSTOM_ENVIRONMENTS]` | Specify the custom environments | "QA", "UAT", "Performance", "DR", "Sandbox" |
| `[TARGET_REGIONS]` | Target or intended regions | "North America" |
| `[COMPLIANCE_STANDARDS]` | Specify the compliance standards | "SOC2 Type II", "PCI-DSS", "HIPAA", "GDPR", "FedRAMP", "ISO 27001" |
| `[CUSTOM_COMPLIANCE]` | Specify the custom compliance | "Internal security standards", "Industry-specific regulations", "Data residency requirements" |
| `[BUDGET_RANGE]` | Budget allocation for range | "$500,000" |
| `[PROJECT_TIMELINE]` | Timeline or schedule for project | "6 months" |
| `[NETWORK_ARCHITECTURE]` | Specify the network architecture | "VPC with public/private subnets", "Hub-spoke topology", "Service mesh", "Zero-trust network" |
| `[CUSTOM_TOPOLOGY]` | Specify the custom topology | "Multi-region mesh", "Hybrid on-prem/cloud", "Edge computing nodes" |
| `[COMPUTE_TYPES]` | Type or category of compute s | "Standard" |
| `[HYBRID_COMPUTE]` | Specify the hybrid compute | "On-prem VMs + Cloud containers", "EKS Anywhere", "Azure Arc", "Anthos" |
| `[STORAGE_TYPES]` | Type or category of storage s | "Standard" |
| `[CUSTOM_STORAGE]` | Specify the custom storage | "NetApp ONTAP", "Pure Storage", "MinIO S3-compatible", "Ceph distributed storage" |
| `[LOAD_BALANCER_TYPE]` | Type or category of load balancer | "Standard" |
| `[CUSTOM_LB]` | Specify the custom lb | "F5 BIG-IP", "HAProxy", "Traefik", "Kong Gateway" |
| `[SECURITY_GROUP_STRATEGY]` | Strategy or approach for security group | "Least privilege per service", "Tiered access (web/app/data)", "Tag-based dynamic groups" |
| `[DNS_PROVIDER]` | Specify the dns provider | "Route 53", "Cloud DNS", "Azure DNS", "Cloudflare DNS" |
| `[CUSTOM_DNS]` | Specify the custom dns | "BIND on-premises", "Infoblox", "External-DNS for K8s" |
| `[CDN_PROVIDER]` | Specify the cdn provider | "CloudFront", "Cloudflare", "Fastly", "Akamai" |
| `[CUSTOM_CDN]` | Specify the custom cdn | "Varnish cache layer", "Nginx reverse proxy", "Custom edge nodes" |
| `[MONITORING_TOOLS]` | Specify the monitoring tools | "Prometheus + Grafana", "Datadog", "New Relic", "CloudWatch" |
| `[CUSTOM_MONITORING]` | Specify the custom monitoring | "OpenTelemetry collectors", "Custom metrics exporters", "Telegraf agents" |
| `[IDENTITY_PROVIDER]` | Specify the identity provider | "AWS IAM", "Azure AD", "Okta", "Google Workspace" |
| `[CUSTOM_IDENTITY]` | Specify the custom identity | "Keycloak", "Auth0", "PingIdentity", "On-prem Active Directory" |
| `[ACCESS_CONTROL_MODEL]` | Specify the access control model | "RBAC (Role-Based)", "ABAC (Attribute-Based)", "PBAC (Policy-Based)" |
| `[CUSTOM_ACCESS]` | Specify the custom access | "OPA Gatekeeper policies", "Kubernetes RBAC", "Custom admission controllers" |
| `[ENCRYPTION_REQUIREMENTS]` | Specify the encryption requirements | "AES-256 at rest", "TLS 1.3 in transit", "End-to-end encryption", "Field-level encryption" |
| `[CUSTOM_ENCRYPTION]` | Specify the custom encryption | "Customer-managed keys (BYOK)", "HSM-backed keys", "Application-level encryption" |
| `[BACKUP_APPROACH]` | Specify the backup approach | "Daily automated snapshots", "Continuous replication", "Point-in-time recovery" |
| `[CUSTOM_BACKUP]` | Specify the custom backup | "Velero for K8s", "Commvault", "Veeam", "Custom scripts to S3" |
| `[DR_STRATEGY]` | Strategy or approach for dr | "Active-passive multi-region", "Pilot light", "Warm standby", "Active-active" |
| `[CUSTOM_DR]` | Specify the custom dr | "Custom failover automation", "Cross-cloud DR", "On-prem to cloud DR" |
| `[COST_OPTIMIZATION_METHODS]` | Specify the cost optimization methods | "Reserved Instances", "Spot/Preemptible", "Right-sizing", "Auto-shutdown dev envs" |
| `[TAGGING_STRATEGY]` | Strategy or approach for tagging | "Cost center tags", "Environment tags", "Owner tags", "Application tags" |
| `[RESOURCE_LIFECYCLE_POLICY]` | Specify the resource lifecycle policy | "S3 lifecycle rules", "Auto-delete dev after 30 days", "Archive to Glacier after 90 days" |
| `[PRIMARY_IAC_TOOL]` | Specify the primary iac tool | "Terraform", "Pulumi", "AWS CDK", "CloudFormation", "Crossplane" |
| `[SECONDARY_IAC_TOOLS]` | Specify the secondary iac tools | "Ansible for config", "Packer for images", "Helm for K8s", "Kustomize" |
| `[CONFIG_MGMT_TOOL]` | Specify the config mgmt tool | "Ansible", "Chef", "Puppet", "SaltStack", "AWS Systems Manager" |
| `[CONTAINER_PLATFORM]` | Specify the container platform | "EKS", "GKE", "AKS", "OpenShift", "Rancher", "K3s" |
| `[SERVICE_MESH]` | Specify the service mesh | "Istio", "Linkerd", "Consul Connect", "AWS App Mesh" |
| `[CUSTOM_MESH]` | Specify the custom mesh | "Cilium service mesh", "Open Service Mesh", "Kuma" |
| `[CICD_PLATFORM]` | Specify the cicd platform | "GitHub Actions", "GitLab CI", "Jenkins", "ArgoCD", "Tekton" |
| `[TERRAFORM_PROVIDER_VERSIONS]` | Specify the terraform provider versions | "aws ~> 5.0", "azurerm ~> 3.0", "google ~> 5.0", "kubernetes ~> 2.0" |
| `[STATE_BACKEND]` | Specify the state backend | "S3 + DynamoDB locking", "Terraform Cloud", "Azure Storage", "GCS bucket" |
| `[MODULE_ORGANIZATION]` | Specify the module organization | "Monorepo with modules/", "Separate repos per module", "Private registry" |
| `[WORKSPACE_STRATEGY]` | Strategy or approach for workspace | "One workspace per environment", "One per region", "Separate state per component" |
| `[VARIABLE_MANAGEMENT_APPROACH]` | Specify the variable management approach | "tfvars per environment", "Terraform Cloud variables", "SSM Parameter Store" |
| `[SECRET_MANAGEMENT]` | Specify the secret management | "HashiCorp Vault", "AWS Secrets Manager", "Azure Key Vault", "SOPS" |
| `[CUSTOM_SECRET_MGR]` | Specify the custom secret mgr | "External Secrets Operator", "Sealed Secrets", "Vault Agent Injector" |
| `[REMOTE_EXECUTION_PLATFORM]` | Specify the remote execution platform | "Terraform Cloud", "Atlantis", "Spacelift", "env0", "Scalr" |
| `[STATE_LOCKING_MECHANISM]` | Specify the state locking mechanism | "DynamoDB table", "Consul locks", "Azure Blob lease", "PostgreSQL advisory locks" |
| `[CF_TEMPLATE_FORMAT]` | Specify the cf template format | "YAML (preferred)", "JSON", "Mixed with nested JSON in YAML" |
| `[STACK_ORGANIZATION_STRATEGY]` | Strategy or approach for stack organization | "One stack per environment", "Layered stacks (network/compute/app)", "Service-oriented stacks" |
| `[CF_PARAMETER_STRATEGY]` | Strategy or approach for cf parameter | "SSM Parameter Store references", "Secrets Manager for sensitive values", "Parameter files per environment" |
| `[CROSS_STACK_REFERENCE_APPROACH]` | Specify the cross stack reference approach | "Export/Import values", "SSM Parameter Store", "AWS CDK cross-stack references" |
| `[NESTED_STACK_STRATEGY]` | Strategy or approach for nested stack | "Parent stack with child modules", "S3-hosted nested templates", "Reusable component stacks" |
| `[CHANGE_SET_POLICY]` | Specify the change set policy | "Always review change sets before apply", "Auto-execute for non-prod", "Require approval for production" |
| `[STACK_PROTECTION_POLICIES]` | Specify the stack protection policies | "Termination protection enabled", "Stack policy preventing resource deletion", "DeletionPolicy: Retain for databases" |
| `[ROLLBACK_STRATEGY]` | Strategy or approach for rollback | "Automatic rollback on failure", "Manual rollback with previous template version", "Blue-green stack swap"
| `[PROJECT_NAME]` | Name of the project | "Digital Transformation Initiative" |
| `[ENVIRONMENT_FOLDERS]` | Specify the environment folders | "environments/dev/", "environments/staging/", "environments/prod/", "environments/dr/" |
| `[MODULE_DIRECTORIES]` | Specify the module directories | "modules/networking/", "modules/compute/", "modules/storage/", "modules/security/" |
| `[SHARED_COMPONENTS]` | Specify the shared components | "shared/providers.tf", "shared/backend.tf", "shared/variables.tf", "shared/outputs.tf" |
| `[CONFIGURATION_FILES]` | Specify the configuration files | "terraform.tfvars", "backend.hcl", "versions.tf", ".terraform-version" |
| `[DOCUMENTATION_PATH]` | Specify the documentation path | "docs/README.md", "docs/architecture.md", "docs/runbooks/", "CHANGELOG.md" |
| `[MODULE_NAMING_CONVENTION]` | Specify the module naming convention | "terraform-aws-{resource}", "tf-{provider}-{component}", "module-{service}-{function}" |
| `[INPUT_VARIABLE_STANDARDS]` | Specify the input variable standards | "Required: type, description, validation", "Optional: default, sensitive, nullable" |
| `[OUTPUT_SPECIFICATIONS]` | Specify the output specifications | "id, arn, name for all resources", "Structured output objects", "Sensitive outputs marked" |
| `[MODULE_DOCUMENTATION_REQUIREMENTS]` | Specify the module documentation requirements | "README.md with examples", "CHANGELOG.md", "terraform-docs generated", "Architecture diagrams" |
| `[MODULE_TESTING_FRAMEWORK]` | Specify the module testing framework | "Terratest (Go)", "Kitchen-Terraform", "Terragrunt validate", "Conftest OPA" |
| `[CUSTOM_TESTING]` | Specify the custom testing | "Custom Go tests", "Python pytest-terraform", "Bash validation scripts" |
| `[MODULE_VERSIONING_STRATEGY]` | Strategy or approach for module versioning | "Semantic versioning (semver)", "Git tags for releases", "CHANGELOG-driven versions" |
| `[MODULE_REGISTRY]` | Specify the module registry | "Terraform Cloud private registry", "GitHub releases", "S3 module bucket" |
| `[CUSTOM_REGISTRY]` | Specify the custom registry | "Artifactory Terraform repository", "GitLab Package Registry", "Nexus Repository" |
| `[DEPENDENCY_MANAGEMENT_APPROACH]` | Specify the dependency management approach | "Terragrunt dependency blocks", "Module version constraints", "Provider lock files" |
| `[DEV_ENVIRONMENT_CONFIG]` | Specify the dev environment config | "Small instances (t3.small)", "Minimal HA", "Auto-shutdown after hours", "Relaxed security for testing" |
| `[STAGING_ENVIRONMENT_CONFIG]` | Specify the staging environment config | "Production-like sizing", "Full HA configuration", "Production security policies", "Synthetic data" |
| `[PROD_ENVIRONMENT_CONFIG]` | Specify the prod environment config | "Right-sized instances", "Multi-AZ HA", "Full security controls", "Reserved capacity", "Encryption enabled" |
| `[CUSTOM_ENVIRONMENT_CONFIGS]` | Specify the custom environment configs | "DR: Cross-region replica", "QA: Ephemeral on-demand", "Performance: Load testing setup" |
| `[VARIABLE_PRECEDENCE_ORDER]` | Specify the variable precedence order | "1. CLI args, 2. .auto.tfvars, 3. terraform.tfvars, 4. Environment vars, 5. Defaults" |
| `[CONFIG_VALIDATION_RULES]` | Specify the config validation rules | "terraform validate", "tflint rules", "Custom validation blocks", "Pre-commit hooks" |
| `[ENVIRONMENT_PROMOTION_PROCESS]` | Specify the environment promotion process | "Dev -> QA (auto) -> Staging (manual) -> Prod (approval)", "GitOps PR-based promotion" |
| `[DRIFT_DETECTION_STRATEGY]` | Strategy or approach for drift detection | "Scheduled terraform plan", "AWS Config rules", "Terraform Cloud drift detection", "Custom scripts"
| `[SECURITY_BASELINE_STANDARDS]` | Specify the security baseline standards | "CIS Benchmarks", "AWS Well-Architected Security", "NIST Cybersecurity Framework", "CSA CCM" |
| `[NETWORK_SEGMENTATION_STRATEGY]` | Strategy or approach for network segmentation | "VPC per environment", "Subnet tiering (public/private/data)", "Security groups per service" |
| `[ACCESS_CONTROL_IMPLEMENTATION]` | Specify the access control implementation | "IAM roles with least privilege", "SSO integration", "MFA enforcement", "Service accounts" |
| `[KEY_MANAGEMENT_STRATEGY]` | Strategy or approach for key management | "AWS KMS with CMK", "Key rotation policy", "Envelope encryption", "HSM for sensitive keys" |
| `[CERTIFICATE_MANAGEMENT_APPROACH]` | Specify the certificate management approach | "ACM for AWS certificates", "Let's Encrypt automation", "cert-manager for K8s" |
| `[VULNERABILITY_SCANNING_TOOLS]` | Specify the vulnerability scanning tools | "Snyk", "Trivy", "Checkov", "tfsec", "Prowler" |
| `[SECURITY_MONITORING_SOLUTIONS]` | Specify the security monitoring solutions | "AWS GuardDuty", "CloudTrail", "Security Hub", "SIEM integration" |
| `[IR_INTEGRATION_APPROACH]` | Specify the ir integration approach | "PagerDuty integration", "Automated runbooks", "Lambda response functions" |
| `[SPECIFIC_REGULATORY_REQUIREMENTS]` | Specify the specific regulatory requirements | "SOC 2 Type II", "PCI-DSS", "HIPAA", "GDPR", "FedRAMP" |
| `[AUDIT_TRAIL_REQUIREMENTS]` | Specify the audit trail requirements | "CloudTrail all regions", "90-day retention minimum", "Immutable logs to S3" |
| `[DATA_RESIDENCY_REQUIREMENTS]` | Specify the data residency requirements | "EU data in eu-west-1", "US data in us-east-1", "Data sovereignty controls" |
| `[DATA_RETENTION_POLICIES]` | Specify the data retention policies | "7 years for financial", "3 years for logs", "S3 lifecycle rules" |
| `[PRIVACY_CONTROL_IMPLEMENTATION]` | Specify the privacy control implementation | "Data classification tagging", "Encryption at rest/transit", "Access logging" |
| `[COMPLIANCE_MONITORING_TOOLS]` | Specify the compliance monitoring tools | "AWS Config Rules", "Azure Policy", "Prisma Cloud", "Dome9" |
| `[COMPLIANCE_REPORTING_AUTOMATION]` | Specify the compliance reporting automation | "AWS Audit Manager", "Scheduled compliance reports", "Dashboard alerts" |
| `[COMPLIANCE_REMEDIATION_PROCESSES]` | Specify the compliance remediation processes | "Auto-remediation Lambda", "Ticketing integration", "SLA-based escalation" |
| `[POLICY_DEFINITION_LANGUAGE]` | Specify the policy definition language | "Open Policy Agent (Rego)", "HashiCorp Sentinel", "AWS SCPs", "Azure Policy JSON" |
| `[CUSTOM_POLICY]` | Specify the custom policy | "Organization-specific OPA rules", "Custom Sentinel policies", "Internal compliance checks" |
| `[POLICY_ENFORCEMENT_POINTS]` | Specify the policy enforcement points | "CI/CD pipeline gates", "Terraform Cloud run tasks", "K8s admission controllers" |
| `[POLICY_TESTING_FRAMEWORK]` | Specify the policy testing framework | "Conftest for OPA", "Sentinel test framework", "Policy unit tests in CI" |
| `[POLICY_VERSION_CONTROL]` | Specify the policy version control | "Git repository for policies", "Semantic versioning", "Change history tracking" |
| `[POLICY_EXCEPTION_PROCESS]` | Specify the policy exception process | "Jira approval workflow", "Time-limited exceptions", "Documented risk acceptance" |
| `[POLICY_MONITORING_APPROACH]` | Specify the policy monitoring approach | "Real-time policy evaluation", "Drift alerts", "Compliance dashboards" |
| `[POLICY_VIOLATION_RESPONSES]` | Specify the policy violation responses | "Block deployment", "Alert and log", "Auto-remediate if possible" |
| `[GOVERNANCE_INTEGRATION_STRATEGY]` | Strategy or approach for governance integration | "ServiceNow integration", "ITSM ticketing", "Change management workflow"
| `[SOURCE_CONTROL_SYSTEM]` | Specify the source control system | "GitHub Enterprise", "GitLab Self-Hosted", "Azure DevOps Repos", "Bitbucket Cloud" |
| `[CUSTOM_VCS]` | Specify the custom vcs | "Self-hosted Gitea", "AWS CodeCommit", "Perforce for large binaries" |
| `[BRANCHING_STRATEGY]` | Strategy or approach for branching | "GitFlow", "GitHub Flow", "Trunk-based development", "Release branching" |
| `[CUSTOM_BRANCHING]` | Specify the custom branching | "Feature flags + trunk-based", "Environment branches", "Team-based branches" |
| `[PIPELINE_TRIGGERS]` | Specify the pipeline triggers | "Push to main/develop", "Pull request events", "Tag creation", "Scheduled (cron)" |
| `[BUILD_STAGE_CONFIGURATION]` | Specify the build stage configuration | "terraform init/validate/plan", "Docker build", "Artifact packaging" |
| `[TESTING_PHASE_CONFIGURATION]` | Specify the testing phase configuration | "Terratest unit tests", "Integration tests", "Compliance checks", "Security scans" |
| `[DEPLOYMENT_STAGE_CONFIGURATION]` | Specify the deployment stage configuration | "terraform apply", "kubectl apply", "Helm upgrade", "ArgoCD sync" |
| `[APPROVAL_PROCESS_REQUIREMENTS]` | Specify the approval process requirements | "Auto-approve dev", "Tech lead for staging", "Manager + CAB for production" |
| `[ROLLBACK_AUTOMATION_STRATEGY]` | Strategy or approach for rollback automation | "Git revert + re-apply", "Terraform state rollback", "Blue-green switch" |
| `[BLUE_GREEN_IMPLEMENTATION]` | Specify the blue green implementation | "Two identical environments", "DNS or LB switching", "Zero-downtime cutover" |
| `[CANARY_DEPLOYMENT_STRATEGY]` | Strategy or approach for canary deployment | "Progressive traffic shift (5%/25%/100%)", "Metrics-based promotion", "Auto-rollback on errors"
| `[ROLLING_UPDATE_CONFIGURATION]` | Specify the rolling update configuration | "2025-01-15" |
| `[IMMUTABLE_INFRA_APPROACH]` | Specify the immutable infra approach | "AMI-based deployments", "Container images", "No in-place updates", "Replace not modify" |
| `[MULTI_ENV_PROMOTION_PROCESS]` | Specify the multi env promotion process | "PR-based promotion", "Terraform workspace switching", "Kustomize overlays" |
| `[FEATURE_FLAG_INTEGRATION]` | Specify the feature flag integration | "LaunchDarkly", "Split.io", "Unleash", "ConfigCat" |
| `[DEPLOYMENT_VALIDATION_TESTS]` | Specify the deployment validation tests | "Smoke tests post-deploy", "Health endpoint checks", "Integration verification" |
| `[HEALTH_CHECK_CONFIGURATION]` | Specify the health check configuration | "HTTP /health endpoint", "TCP port checks", "Deep health with dependencies" |
| `[WORKFLOW_ORCHESTRATION_TOOL]` | Specify the workflow orchestration tool | "GitHub Actions", "GitLab CI", "Atlantis", "Terraform Cloud" |
| `[JOB_SCHEDULING_SYSTEM]` | Specify the job scheduling system | "Cron jobs", "AWS EventBridge", "Kubernetes CronJobs", "Airflow" |
| `[EVENT_DRIVEN_AUTOMATION]` | Specify the event driven automation | "AWS Lambda triggers", "CloudWatch Events", "Webhooks", "SNS notifications" |
| `[DEPENDENCY_RESOLUTION]` | Specify the dependency resolution | "Terragrunt dependencies", "Module version locking", "Provider constraints" |
| `[PARALLEL_EXECUTION_STRATEGY]` | Strategy or approach for parallel execution | "Independent module parallel apply", "Parallelism limit (10)", "Resource targeting" |
| `[ERROR_HANDLING_PROCEDURES]` | Specify the error handling procedures | "Retry with backoff", "Alert on failure", "Auto-rollback triggers" |
| `[NOTIFICATION_INTEGRATION]` | Specify the notification integration | "Slack webhooks", "PagerDuty alerts", "Email notifications", "Teams integration" |
| `[METRICS_COLLECTION_STRATEGY]` | Strategy or approach for metrics collection | "CloudWatch metrics", "Prometheus exporters", "Custom Terraform metrics" |
| `[STATE_BACKEND_CHOICE]` | Specify the state backend choice | "S3 + DynamoDB", "Terraform Cloud", "Azure Storage Account", "GCS bucket" |
| `[STATE_ENCRYPTION_METHOD]` | Specify the state encryption method | "SSE-S3", "KMS encryption", "Customer-managed keys", "Client-side encryption" |
| `[STATE_VERSIONING_APPROACH]` | Specify the state versioning approach | "S3 versioning enabled", "State snapshots before changes", "Git-backed state" |
| `[CONCURRENT_ACCESS_CONTROL]` | Specify the concurrent access control | "DynamoDB locking", "Consul locks", "Terraform Cloud remote operations" |
| `[STATE_BACKUP_STRATEGY]` | Strategy or approach for state backup | "Automated S3 versioning", "Cross-region replication", "Daily snapshots" |
| `[STATE_RECOVERY_PROCEDURES]` | Specify the state recovery procedures | "Restore from S3 version", "terraform state push", "Import existing resources" |
| `[STATE_MIGRATION_PROCESS]` | Specify the state migration process | "terraform state mv", "terraform import", "Backend migration steps" |
| `[STATE_VALIDATION_CHECKS]` | Specify the state validation checks | "terraform plan comparison", "State file integrity checks", "Resource drift detection" |
| `[DATABASE_PROVISIONING_STRATEGY]` | Strategy or approach for database provisioning | "RDS via Terraform", "Aurora with read replicas", "DynamoDB tables" |
| `[DATA_MIGRATION_APPROACH]` | Specify the data migration approach | "AWS DMS", "pg_dump/restore", "Blue-green database cutover" |
| `[BACKUP_AUTOMATION_CONFIGURATION]` | Specify the backup automation configuration | "AWS Backup plans", "Automated snapshots", "Cross-region backup copy" |
| `[PITR_IMPLEMENTATION]` | Specify the pitr implementation | "RDS point-in-time recovery", "DynamoDB PITR", "5-minute backup windows"
| `[CROSS_REGION_REPLICATION]` | Specify the cross region replication | "North America" |
| `[DATA_ARCHIVAL_STRATEGY]` | Strategy or approach for data archival | "S3 Glacier for cold data", "Lifecycle transitions", "7-year retention archives" |
| `[DATA_LIFECYCLE_MANAGEMENT]` | Specify the data lifecycle management | "S3 lifecycle policies", "Auto-delete after 90 days", "Tier transitions" |
| `[DATABASE_PERFORMANCE_OPTIMIZATION]` | Specify the database performance optimization | "Query optimization", "Index tuning", "Connection pooling", "Read replicas" |
| `[METRICS_COLLECTION_TOOLS]` | Specify the metrics collection tools | "Prometheus", "CloudWatch", "Datadog", "New Relic" |
| `[LOG_AGGREGATION_SOLUTION]` | Specify the log aggregation solution | "ELK Stack", "CloudWatch Logs", "Loki + Grafana", "Splunk" |
| `[DISTRIBUTED_TRACING_IMPLEMENTATION]` | Specify the distributed tracing implementation | "AWS X-Ray", "Jaeger", "Zipkin", "OpenTelemetry" |
| `[DASHBOARD_SETUP_REQUIREMENTS]` | Specify the dashboard setup requirements | "Grafana dashboards", "CloudWatch dashboards", "Executive summary views" |
| `[ALERTING_RULE_CONFIGURATION]` | Specify the alerting rule configuration | "Prometheus AlertManager", "CloudWatch Alarms", "PagerDuty integration" |
| `[SLA_DEFINITIONS]` | Specify the sla definitions | "99.9% availability", "< 200ms p95 latency", "< 1% error rate" |
| `[PERFORMANCE_BASELINE_METRICS]` | Specify the performance baseline metrics | "Request latency", "Throughput", "Error rate", "Resource utilization" |
| `[CAPACITY_PLANNING_METRICS]` | Specify the capacity planning metrics | "CPU/memory trends", "Storage growth", "Network bandwidth", "Cost projections" |
| `[COST_MONITORING_IMPLEMENTATION]` | Specify the cost monitoring implementation | "AWS Cost Explorer", "CloudHealth", "Spot.io", "Infracost" |
| `[RESOURCE_UTILIZATION_TRACKING]` | Specify the resource utilization tracking | "CloudWatch Container Insights", "Prometheus node exporter", "Custom utilization dashboards" |
| `[PERFORMANCE_ANALYTICS_TOOLS]` | Specify the performance analytics tools | "Grafana analytics", "AWS Compute Optimizer", "Performance Insights" |
| `[TREND_ANALYSIS_CONFIGURATION]` | Specify the trend analysis configuration | "Weekly trend reports", "Growth rate calculations", "Forecasting models" |
| `[ANOMALY_DETECTION_SETUP]` | Specify the anomaly detection setup | "CloudWatch Anomaly Detection", "ML-based alerting", "Datadog anomalies" |
| `[PREDICTIVE_ANALYTICS_IMPLEMENTATION]` | Specify the predictive analytics implementation | "Capacity forecasting", "Cost prediction", "Traffic pattern modeling" |
| `[BUSINESS_METRICS_INTEGRATION]` | Specify the business metrics integration | "Revenue per request", "User conversion", "Business KPI correlation" |
| `[ROI_TRACKING_METHODOLOGY]` | Specify the roi tracking methodology | "Cost savings reports", "Efficiency gains", "Automation ROI calculation" |
| `[INCIDENT_DETECTION_MECHANISMS]` | Specify the incident detection mechanisms | "Automated monitoring alerts", "Synthetic checks", "User-reported issues" |
| `[ESCALATION_PROCEDURES]` | Specify the escalation procedures | "L1 > L2 > L3 escalation", "Time-based escalation", "Severity-based routing" |
| `[RESPONSE_AUTOMATION_WORKFLOWS]` | Specify the response automation workflows | "Auto-scaling triggers", "Self-healing Lambda", "Runbook automation" |
| `[INCIDENT_COMMUNICATION_PROTOCOLS]` | Specify the incident communication protocols | "Slack #incidents", "Status page updates", "Email stakeholders" |
| `[POST_INCIDENT_ANALYSIS_PROCESS]` | Specify the post incident analysis process | "Blameless postmortem", "5 Whys analysis", "Action item tracking" |
| `[CONTINUOUS_IMPROVEMENT_PROCESS]` | Specify the continuous improvement process | "Weekly retros", "Quarterly reviews", "Automation backlog" |
| `[INCIDENT_DOCUMENTATION_REQUIREMENTS]` | Specify the incident documentation requirements | "Timeline", "Impact assessment", "Root cause", "Remediation actions" |
| `[INCIDENT_RESPONSE_TRAINING]` | Specify the incident response training | "Game days", "Tabletop exercises", "On-call shadowing"
| `[UNIT_TESTING_APPROACH]` | Specify the unit testing approach | "Terratest for modules", "Go unit tests", "pytest-terraform", "OPA unit tests" |
| `[INTEGRATION_TESTING_STRATEGY]` | Strategy or approach for integration testing | "Deploy to test environment", "API integration tests", "Cross-module testing" |
| `[E2E_TESTING_FRAMEWORK]` | Specify the e2e testing framework | "Terratest with full deployment", "Kitchen-Terraform", "InSpec verification" |
| `[PERFORMANCE_TESTING_TOOLS]` | Specify the performance testing tools | "terraform plan timing", "k6 for load testing", "Benchmark scripts" |
| `[SECURITY_TESTING_INTEGRATION]` | Specify the security testing integration | "tfsec in CI", "Checkov scans", "KICS security checks", "Snyk IaC" |
| `[COMPLIANCE_TESTING_AUTOMATION]` | Specify the compliance testing automation | "Conftest OPA policies", "AWS Config conformance packs", "Sentinel policies" |
| `[DR_TESTING_PROCEDURES]` | Specify the dr testing procedures | "Quarterly DR drills", "Failover testing", "Backup restoration tests" |
| `[CHAOS_ENGINEERING_IMPLEMENTATION]` | Specify the chaos engineering implementation | "AWS Fault Injection Simulator", "Gremlin", "LitmusChaos", "Chaos Monkey" |
| `[SYNTAX_VALIDATION_TOOLS]` | Specify the syntax validation tools | "terraform validate", "terraform fmt", "tflint", "yamllint" |
| `[PLAN_REVIEW_PROCESS]` | Specify the plan review process | "PR comment with plan output", "Manual review required", "Atlantis plan preview" |
| `[COST_ESTIMATION_VALIDATION]` | Specify the cost estimation validation | "Infracost PR comments", "Cost thresholds", "Budget alerts" |
| `[SECURITY_SCANNING_INTEGRATION]` | Specify the security scanning integration | "Pre-commit hooks", "CI pipeline stage", "PR blocking on critical findings" |
| `[COMPLIANCE_CHECKING_AUTOMATION]` | Specify the compliance checking automation | "Policy-as-code gates", "Automated compliance reports", "Continuous monitoring" |
| `[RESOURCE_LIMIT_VALIDATION]` | Specify the resource limit validation | "AWS service quotas check", "Account limit verification", "Resource count limits" |
| `[DEPENDENCY_VERIFICATION_PROCESS]` | Specify the dependency verification process | "Module version checks", "Provider compatibility", "Lock file validation" |
| `[ENVIRONMENT_READINESS_CHECKS]` | Specify the environment readiness checks | "Pre-deploy validation", "DNS propagation", "Certificate validity" |
| `[CODE_REVIEW_STANDARDS]` | Specify the code review standards | "2 approvers required", "CODEOWNERS enforcement", "Checklist completion" |
| `[DOCUMENTATION_REVIEW_PROCESS]` | Specify the documentation review process | "README updates required", "terraform-docs generation", "Changelog entries" |
| `[PERFORMANCE_BENCHMARK_CRITERIA]` | Specify the performance benchmark criteria | "Plan time < 2 min", "Apply time < 10 min", "Resource creation thresholds" |
| `[RELIABILITY_TESTING_METHODOLOGY]` | Specify the reliability testing methodology | "Chaos engineering", "Failure injection", "Recovery time measurement" |
| `[SCALABILITY_VALIDATION_APPROACH]` | Specify the scalability validation approach | "Load testing", "Scale-out verification", "Capacity planning validation" |
| `[MAINTAINABILITY_ASSESSMENT_CRITERIA]` | Specify the maintainability assessment criteria | "Module complexity", "Code duplication", "Documentation coverage" |
| `[TECHNICAL_DEBT_TRACKING]` | Specify the technical debt tracking | "Jira tech debt epic", "Quarterly cleanup sprints", "Deprecation tracking" |
| `[QUALITY_METRICS_COLLECTION]` | Specify the quality metrics collection | "Test coverage", "Plan success rate", "Apply success rate", "Drift frequency"
| `[RIGHT_SIZING_ANALYSIS_APPROACH]` | Specify the right sizing analysis approach | "AWS Compute Optimizer", "CloudHealth recommendations", "Custom utilization analysis" |
| `[RESERVED_INSTANCE_STRATEGY]` | Strategy or approach for reserved instance | "1-year standard for baseline", "3-year convertible for flexible", "Savings Plans" |
| `[SPOT_INSTANCE_UTILIZATION]` | Specify the spot instance utilization | "Spot for batch jobs", "Spot fleet with diversification", "Fallback to on-demand" |
| `[AUTO_SCALING_OPTIMIZATION]` | Specify the auto scaling optimization | "Target tracking policies", "Predictive scaling", "Step scaling for bursts" |
| `[STORAGE_OPTIMIZATION_STRATEGY]` | Strategy or approach for storage optimization | "GP3 for cost efficiency", "Tiered storage", "S3 Intelligent-Tiering" |
| `[NETWORK_COST_OPTIMIZATION]` | Specify the network cost optimization | "VPC endpoints for S3/DynamoDB", "NAT Gateway optimization", "Data transfer analysis" |
| `[RESOURCE_SCHEDULING_AUTOMATION]` | Specify the resource scheduling automation | "Instance Scheduler", "Lambda start/stop", "Dev env auto-shutdown" |
| `[RESOURCE_LIFECYCLE_OPTIMIZATION]` | Specify the resource lifecycle optimization | "S3 lifecycle rules", "EBS snapshot cleanup", "Unused resource deletion" |
| `[COMPUTE_PERFORMANCE_OPTIMIZATION]` | Specify the compute performance optimization | "Instance type selection", "CPU credits management", "Burst vs sustained" |
| `[STORAGE_PERFORMANCE_TUNING]` | Specify the storage performance tuning | "IOPS provisioning", "Throughput optimization", "EBS volume types" |
| `[NETWORK_PERFORMANCE_OPTIMIZATION]` | Specify the network performance optimization | "Enhanced networking", "Placement groups", "Network bandwidth planning" |
| `[DATABASE_PERFORMANCE_TUNING]` | Specify the database performance tuning | "Query optimization", "Connection pooling", "Read replicas", "Caching layer" |
| `[CACHING_IMPLEMENTATION_STRATEGY]` | Strategy or approach for caching implementation | "ElastiCache Redis/Memcached", "DAX for DynamoDB", "CloudFront caching" |
| `[CDN_OPTIMIZATION_CONFIGURATION]` | Specify the cdn optimization configuration | "CloudFront distributions", "Cache behaviors", "Origin shield", "Edge functions" |
| `[LOAD_BALANCING_OPTIMIZATION]` | Specify the load balancing optimization | "ALB for HTTP/HTTPS", "NLB for TCP/UDP", "Cross-zone balancing"
| `[REGIONAL_DISTRIBUTION_OPTIMIZATION]` | Specify the regional distribution optimization | "North America" |
| `[RESOURCE_GOVERNANCE_FRAMEWORK]` | Specify the resource governance framework | "AWS Control Tower", "Landing Zone", "Service Catalog", "Tag policies" |
| `[RESOURCE_NAMING_CONVENTIONS]` | Specify the resource naming conventions | "{env}-{app}-{resource}-{region}", "Lowercase with hyphens", "Include owner tag" |
| `[RESOURCE_TAGGING_STANDARDS]` | Specify the resource tagging standards | "Environment, Owner, CostCenter, Application, Team required tags" |
| `[ACCESS_GOVERNANCE_POLICIES]` | Specify the access governance policies | "Least privilege", "Role-based access", "Regular access reviews", "Break-glass procedures" |
| `[CHANGE_MANAGEMENT_PROCESS]` | Specify the change management process | "RFC process", "CAB approval for prod", "Change windows", "Emergency change procedures" |
| `[DOCUMENTATION_STANDARDS]` | Specify the documentation standards | "README in every module", "Architecture diagrams", "Runbooks", "terraform-docs" |
| `[TRAINING_REQUIREMENTS]` | Specify the training requirements | "Terraform certification", "Cloud certifications", "Security training", "On-call training" |
| `[CERTIFICATION_TRACKING_SYSTEM]` | Specify the certification tracking system | "Learning management system", "Certification database", "Skills matrix tracking" |
| `[CURRENT_STATE_ASSESSMENT_APPROACH]` | Specify the current state assessment approach | "Infrastructure inventory", "Dependency mapping", "Cost analysis", "Security assessment" |
| `[MIGRATION_PLANNING_METHODOLOGY]` | Specify the migration planning methodology | "AWS Migration Hub", "6 Rs framework", "Wave planning", "Dependency mapping" |
| `[PHASED_MIGRATION_STRATEGY]` | Strategy or approach for phased migration | "Pilot -> Wave 1 -> Wave 2 -> Final", "Risk-based prioritization" |
| `[APPLICATION_MIGRATION_STRATEGY]` | Strategy or approach for application migration | "Rehost (lift-shift)", "Replatform", "Refactor", "Replace (SaaS)" |
| `[MIGRATION_TESTING_STRATEGY]` | Strategy or approach for migration testing | "Parallel run", "Smoke tests", "Performance validation", "User acceptance testing" |
| `[MIGRATION_ROLLBACK_PLANNING]` | Specify the migration rollback planning | "DNS failback", "Data sync maintenance", "Rollback runbook", "Cutover checkpoints" |
| `[GO_LIVE_PROCEDURES]` | Specify the go live procedures | "Cutover checklist", "Traffic switch", "Monitoring verification", "On-call readiness" |
| `[ARCHITECTURE_MODERNIZATION_APPROACH]` | Specify the architecture modernization approach | "Microservices decomposition", "Event-driven patterns", "API-first design" |
| `[TECHNOLOGY_STACK_MODERNIZATION]` | Specify the technology stack modernization | "Container adoption", "Serverless migration", "Managed services transition" |
| `[PROCESS_MODERNIZATION_STRATEGY]` | Strategy or approach for process modernization | "DevOps adoption", "GitOps workflow", "Automated testing", "CI/CD implementation" |
| `[TEAM_SKILL_DEVELOPMENT_PLAN]` | Specify the team skill development plan | "Cloud training roadmap", "Certification paths", "Hands-on labs", "Mentorship programs" |
| `[TOOL_MODERNIZATION_ROADMAP]` | Specify the tool modernization roadmap | "IaC adoption", "Monitoring stack upgrade", "CI/CD pipeline modernization" |
| `[AUTOMATION_ENHANCEMENT_PLAN]` | Specify the automation enhancement plan | "Manual task automation", "Self-service portals", "Policy automation", "Testing automation" |
| `[INTEGRATION_MODERNIZATION_APPROACH]` | Specify the integration modernization approach | "API Gateway adoption", "Event-driven integration", "Service mesh implementation" |
| `[SECURITY_MODERNIZATION_STRATEGY]` | Strategy or approach for security modernization | "Zero trust implementation", "DevSecOps adoption", "Automated compliance" |
| `[FEEDBACK_LOOP_IMPLEMENTATION]` | Specify the feedback loop implementation | "User surveys", "Developer NPS", "Incident reviews", "Retrospectives" |
| `[PERFORMANCE_METRICS_TRACKING]` | Specify the performance metrics tracking | "DORA metrics", "Lead time", "Deployment frequency", "MTTR", "Change failure rate" |
| `[INNOVATION_PIPELINE_PROCESS]` | Specify the innovation pipeline process | "Hackathons", "Innovation sprints", "Tech radar evaluation", "POC process" |
| `[TECHNOLOGY_EVALUATION_PROCESS]` | Specify the technology evaluation process | "Tech radar", "POC criteria", "Build vs buy analysis", "Vendor assessment" |
| `[BEST_PRACTICE_SHARING_MECHANISMS]` | Specify the best practice sharing mechanisms | "Internal tech blog", "Lunch & learns", "CoP meetings", "Documentation wiki" |
| `[COMMUNITY_ENGAGEMENT_STRATEGY]` | Strategy or approach for community engagement | "Open source contributions", "Conference presentations", "User group participation" |
| `[VENDOR_RELATIONSHIP_MANAGEMENT]` | Specify the vendor relationship management | "Regular business reviews", "Escalation paths", "Contract management", "SLA tracking" |
| `[FUTURE_ROADMAP_PLANNING]` | Specify the future roadmap planning | "Quarterly planning", "Technology roadmap", "Capacity forecasting", "Budget planning"
