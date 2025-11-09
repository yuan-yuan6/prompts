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

Network Architecture:
- Design multi-AZ VPC with public/private subnet strategy
- Configure route tables, NAT gateways routing configuration
- Apply security groups for web/app/data tiers security groups
- Balance with ALB, NLB cloud load balancing with CloudFront CDN
- Connect with Site-to-Site VPN vpn configuration

Security Architecture:
- Apply AWS Well-Architected cloud security framework
- Use IAM, Cognito cloud identity management with RBAC cloud access control
- Protect with KMS encryption, VPC security cloud data protection
- Monitor with CloudTrail, GuardDuty cloud monitoring security
- Manage keys with AWS KMS cloud key management and CloudWatch threat detection

Scalability Design:
- Apply predictive cloud scaling strategy with ASG, ECS auto scaling
- Optimize with CloudWatch metrics cloud performance optimization
- Plan with AWS Trusted Advisor cloud capacity planning
- Monitor with CloudWatch cloud monitoring strategy with SNS cloud alerting
```

## Best Practices

1. **Design for cloud-native architectures and services**
2. **Implement multi-region deployment for high availability**
3. **Use managed services to reduce operational overhead**
4. **Apply security best practices and principle of least privilege**
5. **Optimize costs through right-sizing and reserved capacity**