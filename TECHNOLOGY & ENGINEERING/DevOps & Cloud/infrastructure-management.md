# Infrastructure Management Template

## Purpose
Comprehensive infrastructure management including provisioning, scaling, monitoring, maintenance, and optimization for cloud and on-premises environments.

## Template Structure

### Infrastructure Overview
- **Infrastructure Name**: {infrastructure_name}
- **Infrastructure Type**: {infrastructure_type}
- **Environment**: {infrastructure_environment}
- **Scale**: {infrastructure_scale}
- **Technology Stack**: {infrastructure_technology_stack}
- **Cloud Provider**: {cloud_provider}
- **Management Approach**: {management_approach}
- **Team**: {infrastructure_team}
- **Budget**: {infrastructure_budget}
- **SLA Requirements**: {sla_requirements}

### Provisioning Strategy
- **Provisioning Method**: {provisioning_method}
- **Infrastructure as Code**: {infrastructure_as_code}
- **Template Management**: {template_management}
- **Resource Organization**: {resource_organization}
- **Configuration Management**: {configuration_management}
- **Environment Management**: {environment_management}
- **Version Control**: {infrastructure_version_control}
- **Change Management**: {infrastructure_change_management}
- **Approval Workflows**: {approval_workflows}
- **Rollback Procedures**: {infrastructure_rollback}

### Scaling Management
- **Scaling Strategy**: {scaling_strategy}
- **Auto Scaling**: {auto_scaling}
- **Horizontal Scaling**: {horizontal_scaling}
- **Vertical Scaling**: {vertical_scaling}
- **Scaling Metrics**: {scaling_metrics}
- **Scaling Policies**: {scaling_policies}
- **Load Balancing**: {load_balancing}
- **Capacity Planning**: {capacity_planning}
- **Performance Optimization**: {performance_optimization}
- **Cost Optimization**: {infrastructure_cost_optimization}

### Monitoring and Observability
- **Monitoring Strategy**: {monitoring_strategy}
- **Infrastructure Monitoring**: {infrastructure_monitoring}
- **Application Monitoring**: {application_monitoring}
- **Performance Monitoring**: {infrastructure_performance_monitoring}
- **Health Checks**: {infrastructure_health_checks}
- **Alerting**: {infrastructure_alerting}
- **Dashboards**: {infrastructure_dashboards}
- **Logging**: {infrastructure_logging}
- **Metrics Collection**: {infrastructure_metrics}
- **Distributed Tracing**: {infrastructure_tracing}

### Maintenance and Operations
- **Maintenance Strategy**: {maintenance_strategy}
- **Patch Management**: {patch_management}
- **Update Procedures**: {update_procedures}
- **Backup Strategy**: {infrastructure_backup}
- **Recovery Procedures**: {infrastructure_recovery}
- **Security Updates**: {security_updates}
- **Performance Tuning**: {performance_tuning}
- **Capacity Management**: {capacity_management}
- **Incident Response**: {infrastructure_incident_response}
- **Change Windows**: {change_windows}

Please provide detailed management procedures, automation scripts, monitoring setups, and operational runbooks.

## Usage Examples

### Cloud Infrastructure Management
```
Implement infrastructure management for EcommercePlatform cloud infrastructure using Terraform provisioning with AWS cloud provider supporting 99.9% SLA requirements.

Provisioning Strategy:
- Use Terraform infrastructure as code with modular template management
- Organize by environment/service/region resource organization
- Apply Ansible configuration management with GitOps environment management
- Control with Git infrastructure version control and PR-based infrastructure change management
- Implement manager approval workflows with automated infrastructure rollback

Scaling Management:
- Apply predictive scaling strategy with CloudWatch auto scaling
- Scale horizontally with ASG, vertically with instance resizing
- Monitor CPU, memory, request rate scaling metrics
- Use target tracking, step scaling policies
- Balance with ALB, NLB load balancing with CloudWatch capacity planning

Monitoring Strategy:
- Monitor with CloudWatch, DataDog infrastructure monitoring
- Track with APM, custom metrics application monitoring
- Check with ELB health checks, custom health checks infrastructure health checks
- Alert via PagerDuty, Slack infrastructure alerting
- Visualize with Grafana dashboards, CloudWatch logs infrastructure logging
```

## Best Practices

1. **Automate infrastructure provisioning and management**
2. **Use infrastructure as code for consistency and repeatability**
3. **Implement comprehensive monitoring and alerting**
4. **Plan for scalability and performance requirements**
5. **Maintain proper backup and disaster recovery procedures**