---
title: Cloud Architecture Template
category: technology/DevOps & Cloud
tags: [data-science, design, machine-learning, management, optimization, security, strategy, technology]
use_cases:
  - Creating design comprehensive cloud architecture patterns for aws, azure, gcp including multi-cloud, hybrid, and cloud-native solutions with scalability, security, and cost optimization.

  - Project planning and execution
  - Strategy development
related_templates:
  - cloud-architecture-framework.md
  - site-reliability-engineering.md
  - cloud-migration-strategy.md
last_updated: 2025-11-09
---

# Cloud Architecture Template

## Purpose
Design comprehensive cloud architecture patterns for AWS, Azure, GCP including multi-cloud, hybrid, and cloud-native solutions with scalability, security, and cost optimization.

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
| `[CLOUD_PROVIDER]` | Specify the cloud provider | "[specify value]" |
| `[ARCHITECTURE_TYPE]` | Specify the architecture type | "Standard" |
| `[DEPLOYMENT_MODEL]` | Specify the deployment model | "[specify value]" |
| `[BUSINESS_OBJECTIVES]` | Specify the business objectives | "Increase efficiency by 30%" |
| `[TECHNICAL_REQUIREMENTS]` | Specify the technical requirements | "[specify value]" |
| `[CLOUD_COMPLIANCE]` | Specify the cloud compliance | "[specify value]" |
| `[CLOUD_BUDGET]` | Specify the cloud budget | "$500,000" |
| `[ARCHITECTURE_TIMELINE]` | Specify the architecture timeline | "6 months" |
| `[CLOUD_STAKEHOLDERS]` | Specify the cloud stakeholders | "[specify value]" |
| `[CLOUD_MODEL]` | Specify the cloud model | "[specify value]" |
| `[SERVICE_MODEL]` | Specify the service model | "[specify value]" |
| `[MULTI_CLOUD_STRATEGY]` | Specify the multi cloud strategy | "[specify value]" |
| `[HYBRID_STRATEGY]` | Specify the hybrid strategy | "[specify value]" |
| `[CLOUD_MIGRATION_STRATEGY]` | Specify the cloud migration strategy | "[specify value]" |
| `[VENDOR_STRATEGY]` | Specify the vendor strategy | "[specify value]" |
| `[EXIT_STRATEGY]` | Specify the exit strategy | "[specify value]" |
| `[CLOUD_GOVERNANCE]` | Specify the cloud governance | "[specify value]" |
| `[CLOUD_COST_STRATEGY]` | Specify the cloud cost strategy | "[specify value]" |
| `[SKILLS_STRATEGY]` | Specify the skills strategy | "[specify value]" |
| `[COMPUTE_SERVICES]` | Specify the compute services | "[specify value]" |
| `[STORAGE_SERVICES]` | Specify the storage services | "[specify value]" |
| `[NETWORK_SERVICES]` | Specify the network services | "[specify value]" |
| `[DATABASE_SERVICES]` | Specify the database services | "[specify value]" |
| `[INTEGRATION_SERVICES]` | Specify the integration services | "[specify value]" |
| `[SECURITY_SERVICES]` | Specify the security services | "[specify value]" |
| `[MONITORING_SERVICES]` | Specify the monitoring services | "[specify value]" |
| `[MANAGEMENT_SERVICES]` | Specify the management services | "[specify value]" |
| `[AIML_SERVICES]` | Specify the aiml services | "[specify value]" |
| `[ANALYTICS_SERVICES]` | Specify the analytics services | "[specify value]" |
| `[NETWORK_DESIGN]` | Specify the network design | "[specify value]" |
| `[VPC_CONFIGURATION]` | Specify the vpc configuration | "[specify value]" |
| `[SUBNET_STRATEGY]` | Specify the subnet strategy | "[specify value]" |
| `[ROUTING_CONFIGURATION]` | Specify the routing configuration | "[specify value]" |
| `[SECURITY_GROUPS]` | Specify the security groups | "[specify value]" |
| `[CLOUD_LOAD_BALANCING]` | Specify the cloud load balancing | "[specify value]" |
| `[CDN_CONFIGURATION]` | Specify the cdn configuration | "[specify value]" |
| `[DNS_STRATEGY]` | Specify the dns strategy | "[specify value]" |
| `[VPN_CONFIGURATION]` | Specify the vpn configuration | "[specify value]" |
| `[DIRECT_CONNECT]` | Specify the direct connect | "[specify value]" |
| `[CLOUD_SECURITY_FRAMEWORK]` | Specify the cloud security framework | "[specify value]" |
| `[CLOUD_IDENTITY_MANAGEMENT]` | Specify the cloud identity management | "[specify value]" |
| `[CLOUD_ACCESS_CONTROL]` | Specify the cloud access control | "[specify value]" |
| `[CLOUD_DATA_PROTECTION]` | Specify the cloud data protection | "[specify value]" |
| `[CLOUD_NETWORK_SECURITY]` | Specify the cloud network security | "[specify value]" |
| `[CLOUD_APPLICATION_SECURITY]` | Specify the cloud application security | "[specify value]" |
| `[CLOUD_MONITORING_SECURITY]` | Specify the cloud monitoring security | "[specify value]" |
| `[COMPLIANCE_CONTROLS]` | Specify the compliance controls | "[specify value]" |
| `[CLOUD_KEY_MANAGEMENT]` | Specify the cloud key management | "[specify value]" |
| `[THREAT_DETECTION]` | Specify the threat detection | "[specify value]" |
| `[AVAILABILITY_DESIGN]` | Specify the availability design | "[specify value]" |
| `[REDUNDANCY_STRATEGY]` | Specify the redundancy strategy | "[specify value]" |
| `[FAILOVER_MECHANISMS]` | Specify the failover mechanisms | "[specify value]" |
| `[LOAD_DISTRIBUTION]` | Specify the load distribution | "[specify value]" |
| `[GEOGRAPHIC_DISTRIBUTION]` | Specify the geographic distribution | "[specify value]" |
| `[CLOUD_BACKUP_STRATEGY]` | Specify the cloud backup strategy | "[specify value]" |
| `[CLOUD_DISASTER_RECOVERY]` | Specify the cloud disaster recovery | "[specify value]" |
| `[CLOUD_BUSINESS_CONTINUITY]` | Specify the cloud business continuity | "[specify value]" |
| `[RTO_RPO_TARGETS]` | Specify the rto rpo targets | "[specify value]" |
| `[AVAILABILITY_TESTING]` | Specify the availability testing | "[specify value]" |
| `[CLOUD_SCALING_STRATEGY]` | Specify the cloud scaling strategy | "[specify value]" |
| `[CLOUD_AUTO_SCALING]` | Specify the cloud auto scaling | "[specify value]" |
| `[CLOUD_PERFORMANCE_OPTIMIZATION]` | Specify the cloud performance optimization | "[specify value]" |
| `[CLOUD_CAPACITY_PLANNING]` | Specify the cloud capacity planning | "[specify value]" |
| `[CLOUD_RESOURCE_MANAGEMENT]` | Specify the cloud resource management | "[specify value]" |
| `[CLOUD_MONITORING_STRATEGY]` | Specify the cloud monitoring strategy | "[specify value]" |
| `[CLOUD_ALERTING]` | Specify the cloud alerting | "[specify value]" |
| `[CLOUD_PERFORMANCE_TESTING]` | Specify the cloud performance testing | "[specify value]" |
| `[CLOUD_OPTIMIZATION]` | Specify the cloud optimization | "[specify value]" |
| `[CLOUD_COST_MANAGEMENT]` | Specify the cloud cost management | "[specify value]" |



## Best Practices

1. **Design for cloud-native architectures and services**
2. **Implement multi-region deployment for high availability**
3. **Use managed services to reduce operational overhead**
4. **Apply security best practices and principle of least privilege**
5. **Optimize costs through right-sizing and reserved capacity**