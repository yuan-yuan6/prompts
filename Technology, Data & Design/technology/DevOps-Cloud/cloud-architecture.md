---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- cloud-architecture
- aws-azure-gcp
- vpc-design
- cost-optimization
title: Cloud Architecture Template
use_cases:
- Creating design comprehensive cloud architecture patterns for aws, azure, gcp including
  multi-cloud, hybrid, and cloud-native solutions with scalability, security, and
  cost optimization.
- Project planning and execution
- Strategy development
industries:
- government
- technology
type: template
difficulty: intermediate
slug: cloud-architecture
---

# Cloud Architecture Template

## Purpose
Design comprehensive cloud architecture patterns for AWS, Azure, GCP including multi-cloud, hybrid, and cloud-native solutions with scalability, security, and cost optimization.

## Quick Cloud Architecture Prompt
Design cloud architecture on [AWS/Azure/GCP] for [application type] with [X users], [Y requests/sec]. Components: compute ([EC2/Lambda/ECS]), database ([RDS/DynamoDB]), cache ([ElastiCache]), storage ([S3]), CDN ([CloudFront]). Requirements: [99.X% uptime], [compliance: SOC2/HIPAA/PCI], budget $[X]/month. Include: VPC design, IAM policies, auto-scaling, disaster recovery (RPO/RTO), cost optimization.

## Quick Start

**Need to design cloud architecture quickly?** Use this minimal example:

### Minimal Example
```
Design a cloud architecture for a SaaS application with 50K users on AWS. Requirements: microservices-based, auto-scaling web tier, PostgreSQL database with read replicas, Redis caching, S3 for file storage, CloudFront CDN. Must handle 1000 requests/second, 99.9% uptime, and comply with SOC 2. Budget: $10K/month.
```

### When to Use This
- Designing new cloud-based applications or systems
- Migrating existing applications to the cloud
- Optimizing cloud infrastructure for performance and cost
- Creating disaster recovery and high-availability architectures

### Basic 3-Step Workflow
1. **Define requirements** - Performance, scalability, security, compliance, budget
2. **Design components** - Choose services, define tiers, plan data flow
3. **Document architecture** - Create diagrams, document decisions, estimate costs

**Time to complete**: 4-8 hours for initial design, 1-2 days for detailed architecture

---

## Template Structure

### Architecture Overview
- **Architecture Name**: [ARCHITECTURE_NAME]
- **Cloud Provider**: [CLOUD_PROVIDER]
- **Architecture Type**: [ARCHITECTURE_TYPE]
- **Deployment Model**: [DEPLOYMENT_MODEL]
- **Business Objectives**: [BUSINESS_OBJECTIVES]
- **Technical Requirements**: [TECHNICAL_REQUIREMENTS]
- **Compliance Requirements**: [CLOUD_COMPLIANCE]
- **Budget**: [CLOUD_BUDGET]
- **Timeline**: [ARCHITECTURE_TIMELINE]
- **Stakeholders**: [CLOUD_STAKEHOLDERS]

### Cloud Strategy
- **Cloud Model**: [CLOUD_MODEL]
- **Service Model**: [SERVICE_MODEL]
- **Multi-Cloud Strategy**: [MULTI_CLOUD_STRATEGY]
- **Hybrid Strategy**: [HYBRID_STRATEGY]
- **Migration Strategy**: [CLOUD_MIGRATION_STRATEGY]
- **Vendor Strategy**: [VENDOR_STRATEGY]
- **Exit Strategy**: [EXIT_STRATEGY]
- **Governance Model**: [CLOUD_GOVERNANCE]
- **Cost Strategy**: [CLOUD_COST_STRATEGY]
- **Skills Strategy**: [SKILLS_STRATEGY]

### Infrastructure Design
- **Compute Services**: [COMPUTE_SERVICES]
- **Storage Services**: [STORAGE_SERVICES]
- **Network Services**: [NETWORK_SERVICES]
- **Database Services**: [DATABASE_SERVICES]
- **Integration Services**: [INTEGRATION_SERVICES]
- **Security Services**: [SECURITY_SERVICES]
- **Monitoring Services**: [MONITORING_SERVICES]
- **Management Services**: [MANAGEMENT_SERVICES]
- **AI/ML Services**: [AIML_SERVICES]
- **Analytics Services**: [ANALYTICS_SERVICES]

### Network Architecture
- **Network Design**: [NETWORK_DESIGN]
- **VPC Configuration**: [VPC_CONFIGURATION]
- **Subnet Strategy**: [SUBNET_STRATEGY]
- **Routing Configuration**: [ROUTING_CONFIGURATION]
- **Security Groups**: [SECURITY_GROUPS]
- **Load Balancing**: [CLOUD_LOAD_BALANCING]
- **CDN Configuration**: [CDN_CONFIGURATION]
- **DNS Strategy**: [DNS_STRATEGY]
- **VPN Configuration**: [VPN_CONFIGURATION]
- **Direct Connect**: [DIRECT_CONNECT]

### Security Architecture
- **Security Framework**: [CLOUD_SECURITY_FRAMEWORK]
- **Identity Management**: [CLOUD_IDENTITY_MANAGEMENT]
- **Access Control**: [CLOUD_ACCESS_CONTROL]
- **Data Protection**: [CLOUD_DATA_PROTECTION]
- **Network Security**: [CLOUD_NETWORK_SECURITY]
- **Application Security**: [CLOUD_APPLICATION_SECURITY]
- **Monitoring Security**: [CLOUD_MONITORING_SECURITY]
- **Compliance Controls**: [COMPLIANCE_CONTROLS]
- **Key Management**: [CLOUD_KEY_MANAGEMENT]
- **Threat Detection**: [THREAT_DETECTION]

### High Availability
- **Availability Design**: [AVAILABILITY_DESIGN]
- **Redundancy Strategy**: [REDUNDANCY_STRATEGY]
- **Failover Mechanisms**: [FAILOVER_MECHANISMS]
- **Load Distribution**: [LOAD_DISTRIBUTION]
- **Geographic Distribution**: [GEOGRAPHIC_DISTRIBUTION]
- **Backup Strategy**: [CLOUD_BACKUP_STRATEGY]
- **Disaster Recovery**: [CLOUD_DISASTER_RECOVERY]
- **Business Continuity**: [CLOUD_BUSINESS_CONTINUITY]
- **RTO/RPO Targets**: [RTO_RPO_TARGETS]
- **Testing Strategy**: [AVAILABILITY_TESTING]

### Scalability Design
- **Scaling Strategy**: [CLOUD_SCALING_STRATEGY]
- **Auto Scaling**: [CLOUD_AUTO_SCALING]
- **Performance Optimization**: [CLOUD_PERFORMANCE_OPTIMIZATION]
- **Capacity Planning**: [CLOUD_CAPACITY_PLANNING]
- **Resource Management**: [CLOUD_RESOURCE_MANAGEMENT]
- **Monitoring Strategy**: [CLOUD_MONITORING_STRATEGY]
- **Alerting Configuration**: [CLOUD_ALERTING]
- **Performance Testing**: [CLOUD_PERFORMANCE_TESTING]
- **Optimization Recommendations**: [CLOUD_OPTIMIZATION]
- **Cost Management**: [CLOUD_COST_MANAGEMENT]

Please provide detailed architecture diagrams, service configurations, best practices, and implementation guides.

## Usage Examples

### AWS Multi-Tier Web Application
```
Design cloud architecture for EcommerceApp web application using AWS cloud provider with scalable three-tier architecture type.

Architecture Overview:
- Multi-tier web application architecture type using IaaS/PaaS service model
- Support 100K+ users business objectives with <200ms response technical requirements
- Ensure PCI DSS, SOC2 cloud compliance within $50K/month cloud budget
- Deploy across 3 availability zones geographic distribution

Infrastructure Design:
- Use EC2, ECS, Lambda compute services with S3, EBS, EFS storage services
- Deploy VPC, ALB, CloudFront network services with RDS, DynamoDB database services
- Integrate with API Gateway, EventBridge integration services
- Secure with IAM, Secrets Manager, WAF security services

### Network Architecture
- Design multi-AZ VPC with public/private subnet strategy
- Configure route tables, NAT gateways routing configuration
- Apply security groups for web/app/data tiers security groups
- Balance with ALB, NLB cloud load balancing with CloudFront CDN
- Connect with Site-to-Site VPN vpn configuration

### Security Architecture
- Apply AWS Well-Architected cloud security framework
- Use IAM, Cognito cloud identity management with RBAC cloud access control
- Protect with KMS encryption, VPC security cloud data protection
- Monitor with CloudTrail, GuardDuty cloud monitoring security
- Manage keys with AWS KMS cloud key management and CloudWatch threat detection

### Scalability Design
- Apply predictive cloud scaling strategy with ASG, ECS auto scaling
- Optimize with CloudWatch metrics cloud performance optimization
- Plan with AWS Trusted Advisor cloud capacity planning
- Monitor with CloudWatch cloud monitoring strategy with SNS cloud alerting
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ARCHITECTURE_NAME]` | Specify the architecture name | "John Smith" |
| `[CLOUD_PROVIDER]` | Specify the cloud provider | "AWS (EC2, EKS, Lambda)", "Azure (AKS, Functions)", "GCP (GKE, Cloud Run)", "Multi-cloud AWS+Azure" |
| `[ARCHITECTURE_TYPE]` | Specify the architecture type | "Standard" |
| `[DEPLOYMENT_MODEL]` | Specify the deployment model | "Multi-AZ high availability", "Multi-region active-active", "Hybrid cloud", "Edge computing" |
| `[BUSINESS_OBJECTIVES]` | Specify the business objectives | "Increase efficiency by 30%" |
| `[TECHNICAL_REQUIREMENTS]` | Specify the technical requirements | "99.99% uptime SLA", "<100ms latency", "Auto-scaling 1-100 instances", "Zero-downtime deployments" |
| `[CLOUD_COMPLIANCE]` | Specify the cloud compliance | "SOC2 Type II", "PCI-DSS", "HIPAA", "GDPR", "FedRAMP" |
| `[CLOUD_BUDGET]` | Specify the cloud budget | "$500,000" |
| `[ARCHITECTURE_TIMELINE]` | Specify the architecture timeline | "6 months" |
| `[CLOUD_STAKEHOLDERS]` | Specify the cloud stakeholders | "CTO, VP Engineering, Platform Team, Security Team, FinOps Team" |
| `[CLOUD_MODEL]` | Specify the cloud model | "Public cloud", "Private cloud", "Hybrid cloud", "Community cloud" |
| `[SERVICE_MODEL]` | Specify the service model | "IaaS (EC2, VMs)", "PaaS (App Service, Beanstalk)", "SaaS integration", "FaaS (Lambda)" |
| `[MULTI_CLOUD_STRATEGY]` | Specify the multi cloud strategy | "Primary AWS + DR on Azure", "Best-of-breed per workload", "Avoid vendor lock-in" |
| `[HYBRID_STRATEGY]` | Specify the hybrid strategy | "On-prem data center + AWS", "VMware Cloud on AWS", "Azure Arc", "Anthos" |
| `[CLOUD_MIGRATION_STRATEGY]` | Specify the cloud migration strategy | "Lift and shift", "Replatform to containers", "Refactor to microservices", "6 Rs approach" |
| `[VENDOR_STRATEGY]` | Specify the vendor strategy | "AWS preferred partner", "Multi-vendor competitive", "Strategic partnership" |
| `[EXIT_STRATEGY]` | Specify the exit strategy | "Portable containers", "Terraform abstraction", "Data export procedures", "30-day migration plan" |
| `[CLOUD_GOVERNANCE]` | Specify the cloud governance | "Cloud Center of Excellence", "Tagging policies", "Cost allocation", "Security guardrails" |
| `[CLOUD_COST_STRATEGY]` | Specify the cloud cost strategy | "FinOps practices", "Reserved capacity 60%", "Spot for batch", "Right-sizing automation" |
| `[SKILLS_STRATEGY]` | Specify the skills strategy | "AWS certifications program", "Hands-on training labs", "Cloud guild community", "External consultants" |
| `[COMPUTE_SERVICES]` | Specify the compute services | "EC2 (t3, m5, c5)", "Lambda functions", "ECS Fargate", "Batch processing" |
| `[STORAGE_SERVICES]` | Specify the storage services | "S3 (Standard, IA, Glacier)", "EBS gp3", "EFS", "FSx for Windows" |
| `[NETWORK_SERVICES]` | Specify the network services | "VPC", "Transit Gateway", "Direct Connect", "Global Accelerator", "CloudFront" |
| `[DATABASE_SERVICES]` | Specify the database services | "RDS Aurora PostgreSQL", "DynamoDB", "ElastiCache Redis", "DocumentDB" |
| `[INTEGRATION_SERVICES]` | Specify the integration services | "API Gateway", "EventBridge", "SQS/SNS", "Step Functions", "AppSync" |
| `[SECURITY_SERVICES]` | Specify the security services | "IAM", "Secrets Manager", "WAF", "Shield", "GuardDuty", "Security Hub" |
| `[MONITORING_SERVICES]` | Specify the monitoring services | "CloudWatch", "X-Ray", "CloudTrail", "Config", "Trusted Advisor" |
| `[MANAGEMENT_SERVICES]` | Specify the management services | "Systems Manager", "Control Tower", "Organizations", "Service Catalog" |
| `[AIML_SERVICES]` | Specify the aiml services | "SageMaker", "Bedrock", "Rekognition", "Comprehend", "Forecast" |
| `[ANALYTICS_SERVICES]` | Specify the analytics services | "Athena", "Redshift", "QuickSight", "Kinesis", "Glue" |
| `[NETWORK_DESIGN]` | Specify the network design | "Hub-and-spoke topology", "Segmented VPCs per environment", "Service mesh overlay" |
| `[VPC_CONFIGURATION]` | Specify the vpc configuration | "10.0.0.0/16 CIDR", "3 AZs", "Public/private/data subnets", "NAT Gateway per AZ" |
| `[SUBNET_STRATEGY]` | Specify the subnet strategy | "/24 subnets per tier/AZ", "Public for ALB", "Private for compute", "Isolated for databases" |
| `[ROUTING_CONFIGURATION]` | Specify the routing configuration | "Route tables per subnet tier", "Transit Gateway attachments", "VPC endpoints for AWS services" |
| `[SECURITY_GROUPS]` | Specify the security groups | "Least privilege rules", "App-tier to DB-tier only", "No 0.0.0.0/0 ingress", "Tag-based management" |
| `[CLOUD_LOAD_BALANCING]` | Specify the cloud load balancing | "ALB for HTTP/HTTPS", "NLB for TCP", "Cross-zone enabled", "Target group health checks" |
| `[CDN_CONFIGURATION]` | Specify the cdn configuration | "CloudFront distributions", "S3 origin with OAC", "Lambda@Edge for auth", "Cache behaviors per path" |
| `[DNS_STRATEGY]` | Specify the dns strategy | "Route 53 hosted zones", "Alias records to ALB", "Health check failover", "Geolocation routing" |
| `[VPN_CONFIGURATION]` | Specify the vpn configuration | "Site-to-site VPN", "Client VPN for remote access", "BGP routing", "Redundant tunnels" |
| `[DIRECT_CONNECT]` | Specify the direct connect | "1Gbps dedicated connection", "LAG for redundancy", "Private VIF to VPC", "Transit VIF to TGW" |
| `[CLOUD_SECURITY_FRAMEWORK]` | Specify the cloud security framework | "AWS Well-Architected Security", "CIS Benchmarks", "NIST CSF", "Zero Trust principles" |
| `[CLOUD_IDENTITY_MANAGEMENT]` | Specify the cloud identity management | "IAM Identity Center with Okta", "Role-based access", "MFA enforced", "Permission boundaries" |
| `[CLOUD_ACCESS_CONTROL]` | Specify the cloud access control | "RBAC with IAM policies", "SCP guardrails", "Resource-based policies", "Attribute-based (ABAC)" |
| `[CLOUD_DATA_PROTECTION]` | Specify the cloud data protection | "KMS CMK encryption", "S3 bucket policies", "RDS encryption", "Macie for PII discovery" |
| `[CLOUD_NETWORK_SECURITY]` | Specify the cloud network security | "Security groups", "NACLs", "WAF rules", "Network Firewall", "VPC Flow Logs" |
| `[CLOUD_APPLICATION_SECURITY]` | Specify the cloud application security | "Secrets Manager", "Parameter Store", "Certificate Manager", "Inspector scanning" |
| `[CLOUD_MONITORING_SECURITY]` | Specify the cloud monitoring security | "CloudTrail logging", "GuardDuty threat detection", "Security Hub aggregation", "SIEM integration" |
| `[COMPLIANCE_CONTROLS]` | Specify the compliance controls | "AWS Config rules", "Conformance packs", "Audit Manager", "Automated remediation" |
| `[CLOUD_KEY_MANAGEMENT]` | Specify the cloud key management | "KMS with automatic rotation", "Customer-managed CMK", "Key policies per service", "CloudHSM for compliance" |
| `[THREAT_DETECTION]` | Specify the threat detection | "GuardDuty findings", "Security Hub insights", "CloudWatch anomaly detection", "Third-party SIEM" |
| `[AVAILABILITY_DESIGN]` | Specify the availability design | "Multi-AZ deployment", "99.99% target SLA", "Active-active architecture", "Auto-healing" |
| `[REDUNDANCY_STRATEGY]` | Specify the redundancy strategy | "3 AZs minimum", "Cross-region read replicas", "S3 cross-region replication", "Global database" |
| `[FAILOVER_MECHANISMS]` | Specify the failover mechanisms | "Route 53 health check failover", "Aurora automatic failover", "ASG health checks", "ELB cross-zone" |
| `[LOAD_DISTRIBUTION]` | Specify the load distribution | "Round-robin across AZs", "Least connections", "Weighted routing", "Session affinity when needed" |
| `[GEOGRAPHIC_DISTRIBUTION]` | Specify the geographic distribution | "Primary us-east-1", "DR eu-west-1", "Edge locations via CloudFront", "Latency-based routing" |
| `[CLOUD_BACKUP_STRATEGY]` | Specify the cloud backup strategy | "AWS Backup centralized", "Daily automated snapshots", "35-day retention", "Cross-region copy" |
| `[CLOUD_DISASTER_RECOVERY]` | Specify the cloud disaster recovery | "Pilot light DR region", "Elastic Disaster Recovery", "RTO <1hr", "RPO <15min" |
| `[CLOUD_BUSINESS_CONTINUITY]` | Specify the cloud business continuity | "Multi-region architecture", "Runbook automation", "Quarterly DR testing", "Communication plan" |
| `[RTO_RPO_TARGETS]` | Specify the rto rpo targets | "RTO: 1 hour", "RPO: 15 minutes", "Tier-1 critical systems", "Tier-2: 4hr/1hr" |
| `[AVAILABILITY_TESTING]` | Specify the availability testing | "Chaos engineering with Fault Injection Simulator", "Game days quarterly", "Failover drills monthly" |
| `[CLOUD_SCALING_STRATEGY]` | Specify the cloud scaling strategy | "Horizontal scaling preferred", "Auto Scaling Groups", "Predictive scaling", "Scheduled scaling" |
| `[CLOUD_AUTO_SCALING]` | Specify the cloud auto scaling | "Target tracking 70% CPU", "Step scaling for spikes", "Min 2 / Max 50 instances", "Cooldown 300s" |
| `[CLOUD_PERFORMANCE_OPTIMIZATION]` | Specify the cloud performance optimization | "Instance right-sizing", "GP3 storage", "ElastiCache caching", "CloudFront edge caching" |
| `[CLOUD_CAPACITY_PLANNING]` | Specify the cloud capacity planning | "Monthly utilization reviews", "Compute Optimizer recommendations", "Reserved capacity planning" |
| `[CLOUD_RESOURCE_MANAGEMENT]` | Specify the cloud resource management | "Tagging standards", "Resource Groups", "Service Catalog products", "Infrastructure as Code" |
| `[CLOUD_MONITORING_STRATEGY]` | Specify the cloud monitoring strategy | "CloudWatch unified", "Container Insights", "Custom metrics", "Dashboard per service" |
| `[CLOUD_ALERTING]` | Specify the cloud alerting | "CloudWatch alarms", "SNS notifications", "PagerDuty integration", "Escalation policies" |
| `[CLOUD_PERFORMANCE_TESTING]` | Specify the cloud performance testing | "Load testing with k6", "AWS Load Testing service", "Baseline benchmarks", "Canary testing" |
| `[CLOUD_OPTIMIZATION]` | Specify the cloud optimization | "Trusted Advisor recommendations", "Compute Optimizer", "Cost Explorer analysis", "Graviton migration" |
| `[CLOUD_COST_MANAGEMENT]` | Specify the cloud cost management | "AWS Cost Explorer", "Budgets with alerts", "Cost allocation tags", "Savings Plans", "Kubecost" |



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Cloud Architecture Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/DevOps & Cloud](../../technology/DevOps & Cloud/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating design comprehensive cloud architecture patterns for aws, azure, gcp including multi-cloud, hybrid, and cloud-native solutions with scalability, security, and cost optimization.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Design for cloud-native architectures and services**
2. **Implement multi-region deployment for high availability**
3. **Use managed services to reduce operational overhead**
4. **Apply security best practices and principle of least privilege**
5. **Optimize costs through right-sizing and reserved capacity**