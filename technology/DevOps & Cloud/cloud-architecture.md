---
title: Cloud Architecture Template
category: technology/DevOps & Cloud
tags: [data-science, design, machine-learning, management, optimization, security, strategy, technology]
use_cases:
  - Implementing design comprehensive cloud architecture patterns for aws, azure, gcp including m...
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
- **Architecture Name**: {architecture_name}
- **Cloud Provider**: {cloud_provider}
- **Architecture Type**: {architecture_type}
- **Deployment Model**: {deployment_model}
- **Business Objectives**: {business_objectives}
- **Technical Requirements**: {technical_requirements}
- **Compliance Requirements**: {cloud_compliance}
- **Budget**: {cloud_budget}
- **Timeline**: {architecture_timeline}
- **Stakeholders**: {cloud_stakeholders}

### Cloud Strategy
- **Cloud Model**: {cloud_model}
- **Service Model**: {service_model}
- **Multi-Cloud Strategy**: {multi_cloud_strategy}
- **Hybrid Strategy**: {hybrid_strategy}
- **Migration Strategy**: {cloud_migration_strategy}
- **Vendor Strategy**: {vendor_strategy}
- **Exit Strategy**: {exit_strategy}
- **Governance Model**: {cloud_governance}
- **Cost Strategy**: {cloud_cost_strategy}
- **Skills Strategy**: {skills_strategy}

### Infrastructure Design
- **Compute Services**: {compute_services}
- **Storage Services**: {storage_services}
- **Network Services**: {network_services}
- **Database Services**: {database_services}
- **Integration Services**: {integration_services}
- **Security Services**: {security_services}
- **Monitoring Services**: {monitoring_services}
- **Management Services**: {management_services}
- **AI/ML Services**: {aiml_services}
- **Analytics Services**: {analytics_services}

### Network Architecture
- **Network Design**: {network_design}
- **VPC Configuration**: {vpc_configuration}
- **Subnet Strategy**: {subnet_strategy}
- **Routing Configuration**: {routing_configuration}
- **Security Groups**: {security_groups}
- **Load Balancing**: {cloud_load_balancing}
- **CDN Configuration**: {cdn_configuration}
- **DNS Strategy**: {dns_strategy}
- **VPN Configuration**: {vpn_configuration}
- **Direct Connect**: {direct_connect}

### Security Architecture
- **Security Framework**: {cloud_security_framework}
- **Identity Management**: {cloud_identity_management}
- **Access Control**: {cloud_access_control}
- **Data Protection**: {cloud_data_protection}
- **Network Security**: {cloud_network_security}
- **Application Security**: {cloud_application_security}
- **Monitoring Security**: {cloud_monitoring_security}
- **Compliance Controls**: {compliance_controls}
- **Key Management**: {cloud_key_management}
- **Threat Detection**: {threat_detection}

### High Availability
- **Availability Design**: {availability_design}
- **Redundancy Strategy**: {redundancy_strategy}
- **Failover Mechanisms**: {failover_mechanisms}
- **Load Distribution**: {load_distribution}
- **Geographic Distribution**: {geographic_distribution}
- **Backup Strategy**: {cloud_backup_strategy}
- **Disaster Recovery**: {cloud_disaster_recovery}
- **Business Continuity**: {cloud_business_continuity}
- **RTO/RPO Targets**: {rto_rpo_targets}
- **Testing Strategy**: {availability_testing}

### Scalability Design
- **Scaling Strategy**: {cloud_scaling_strategy}
- **Auto Scaling**: {cloud_auto_scaling}
- **Performance Optimization**: {cloud_performance_optimization}
- **Capacity Planning**: {cloud_capacity_planning}
- **Resource Management**: {cloud_resource_management}
- **Monitoring Strategy**: {cloud_monitoring_strategy}
- **Alerting Configuration**: {cloud_alerting}
- **Performance Testing**: {cloud_performance_testing}
- **Optimization Recommendations**: {cloud_optimization}
- **Cost Management**: {cloud_cost_management}

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
| `{architecture_name}` | Specify the architecture name | "John Smith" |
| `{cloud_provider}` | Specify the cloud provider | "[specify value]" |
| `{architecture_type}` | Specify the architecture type | "Standard" |
| `{deployment_model}` | Specify the deployment model | "[specify value]" |
| `{business_objectives}` | Specify the business objectives | "Increase efficiency by 30%" |
| `{technical_requirements}` | Specify the technical requirements | "[specify value]" |
| `{cloud_compliance}` | Specify the cloud compliance | "[specify value]" |
| `{cloud_budget}` | Specify the cloud budget | "$500,000" |
| `{architecture_timeline}` | Specify the architecture timeline | "6 months" |
| `{cloud_stakeholders}` | Specify the cloud stakeholders | "[specify value]" |
| `{cloud_model}` | Specify the cloud model | "[specify value]" |
| `{service_model}` | Specify the service model | "[specify value]" |
| `{multi_cloud_strategy}` | Specify the multi cloud strategy | "[specify value]" |
| `{hybrid_strategy}` | Specify the hybrid strategy | "[specify value]" |
| `{cloud_migration_strategy}` | Specify the cloud migration strategy | "[specify value]" |
| `{vendor_strategy}` | Specify the vendor strategy | "[specify value]" |
| `{exit_strategy}` | Specify the exit strategy | "[specify value]" |
| `{cloud_governance}` | Specify the cloud governance | "[specify value]" |
| `{cloud_cost_strategy}` | Specify the cloud cost strategy | "[specify value]" |
| `{skills_strategy}` | Specify the skills strategy | "[specify value]" |
| `{compute_services}` | Specify the compute services | "[specify value]" |
| `{storage_services}` | Specify the storage services | "[specify value]" |
| `{network_services}` | Specify the network services | "[specify value]" |
| `{database_services}` | Specify the database services | "[specify value]" |
| `{integration_services}` | Specify the integration services | "[specify value]" |
| `{security_services}` | Specify the security services | "[specify value]" |
| `{monitoring_services}` | Specify the monitoring services | "[specify value]" |
| `{management_services}` | Specify the management services | "[specify value]" |
| `{aiml_services}` | Specify the aiml services | "[specify value]" |
| `{analytics_services}` | Specify the analytics services | "[specify value]" |
| `{network_design}` | Specify the network design | "[specify value]" |
| `{vpc_configuration}` | Specify the vpc configuration | "[specify value]" |
| `{subnet_strategy}` | Specify the subnet strategy | "[specify value]" |
| `{routing_configuration}` | Specify the routing configuration | "[specify value]" |
| `{security_groups}` | Specify the security groups | "[specify value]" |
| `{cloud_load_balancing}` | Specify the cloud load balancing | "[specify value]" |
| `{cdn_configuration}` | Specify the cdn configuration | "[specify value]" |
| `{dns_strategy}` | Specify the dns strategy | "[specify value]" |
| `{vpn_configuration}` | Specify the vpn configuration | "[specify value]" |
| `{direct_connect}` | Specify the direct connect | "[specify value]" |
| `{cloud_security_framework}` | Specify the cloud security framework | "[specify value]" |
| `{cloud_identity_management}` | Specify the cloud identity management | "[specify value]" |
| `{cloud_access_control}` | Specify the cloud access control | "[specify value]" |
| `{cloud_data_protection}` | Specify the cloud data protection | "[specify value]" |
| `{cloud_network_security}` | Specify the cloud network security | "[specify value]" |
| `{cloud_application_security}` | Specify the cloud application security | "[specify value]" |
| `{cloud_monitoring_security}` | Specify the cloud monitoring security | "[specify value]" |
| `{compliance_controls}` | Specify the compliance controls | "[specify value]" |
| `{cloud_key_management}` | Specify the cloud key management | "[specify value]" |
| `{threat_detection}` | Specify the threat detection | "[specify value]" |
| `{availability_design}` | Specify the availability design | "[specify value]" |
| `{redundancy_strategy}` | Specify the redundancy strategy | "[specify value]" |
| `{failover_mechanisms}` | Specify the failover mechanisms | "[specify value]" |
| `{load_distribution}` | Specify the load distribution | "[specify value]" |
| `{geographic_distribution}` | Specify the geographic distribution | "[specify value]" |
| `{cloud_backup_strategy}` | Specify the cloud backup strategy | "[specify value]" |
| `{cloud_disaster_recovery}` | Specify the cloud disaster recovery | "[specify value]" |
| `{cloud_business_continuity}` | Specify the cloud business continuity | "[specify value]" |
| `{rto_rpo_targets}` | Specify the rto rpo targets | "[specify value]" |
| `{availability_testing}` | Specify the availability testing | "[specify value]" |
| `{cloud_scaling_strategy}` | Specify the cloud scaling strategy | "[specify value]" |
| `{cloud_auto_scaling}` | Specify the cloud auto scaling | "[specify value]" |
| `{cloud_performance_optimization}` | Specify the cloud performance optimization | "[specify value]" |
| `{cloud_capacity_planning}` | Specify the cloud capacity planning | "[specify value]" |
| `{cloud_resource_management}` | Specify the cloud resource management | "[specify value]" |
| `{cloud_monitoring_strategy}` | Specify the cloud monitoring strategy | "[specify value]" |
| `{cloud_alerting}` | Specify the cloud alerting | "[specify value]" |
| `{cloud_performance_testing}` | Specify the cloud performance testing | "[specify value]" |
| `{cloud_optimization}` | Specify the cloud optimization | "[specify value]" |
| `{cloud_cost_management}` | Specify the cloud cost management | "[specify value]" |



## Best Practices

1. **Design for cloud-native architectures and services**
2. **Implement multi-region deployment for high availability**
3. **Use managed services to reduce operational overhead**
4. **Apply security best practices and principle of least privilege**
5. **Optimize costs through right-sizing and reserved capacity**