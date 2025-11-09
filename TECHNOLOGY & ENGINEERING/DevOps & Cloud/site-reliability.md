# Site Reliability Engineering Template

## Purpose
Implement comprehensive SRE practices including SLO/SLI definition, error budgets, incident management, monitoring, alerting, and reliability engineering for production systems.

## Template Structure

### SRE Overview
- **Service Name**: {service_name}
- **Service Type**: {service_type}
- **Business Criticality**: {business_criticality}
- **User Base**: {user_base}
- **Traffic Pattern**: {traffic_pattern}
- **Reliability Requirements**: {reliability_requirements}
- **Team Structure**: {sre_team_structure}
- **Responsibilities**: {sre_responsibilities}
- **Tools and Technologies**: {sre_tools}
- **Budget**: {sre_budget}

### Service Level Objectives
- **SLI Definitions**: {sli_definitions}
- **SLO Targets**: {slo_targets}
- **Measurement Methods**: {measurement_methods}
- **Data Sources**: {data_sources}
- **Calculation Logic**: {calculation_logic}
- **Reporting Period**: {reporting_period}
- **SLO Review Process**: {slo_review_process}
- **Stakeholder Agreement**: {stakeholder_agreement}
- **SLO Documentation**: {slo_documentation}
- **Communication Plan**: {slo_communication}

### Error Budget Management
- **Error Budget Definition**: {error_budget_definition}
- **Budget Calculation**: {budget_calculation}
- **Burn Rate**: {burn_rate}
- **Budget Tracking**: {budget_tracking}
- **Budget Alerts**: {budget_alerts}
- **Budget Policies**: {budget_policies}
- **Escalation Triggers**: {escalation_triggers}
- **Feature Release Gates**: {release_gates}
- **Budget Reporting**: {budget_reporting}
- **Recovery Actions**: {recovery_actions}

### Monitoring and Observability
- **Monitoring Strategy**: {sre_monitoring_strategy}
- **Metrics Collection**: {sre_metrics_collection}
- **Log Management**: {sre_log_management}
- **Distributed Tracing**: {sre_distributed_tracing}
- **Dashboard Design**: {sre_dashboard_design}
- **Alerting Strategy**: {sre_alerting_strategy}
- **On-Call Management**: {oncall_management}
- **Runbook Creation**: {runbook_creation}
- **Playbook Development**: {playbook_development}
- **Tool Integration**: {sre_tool_integration}

### Incident Management
- **Incident Classification**: {incident_classification}
- **Response Procedures**: {response_procedures}
- **Escalation Matrix**: {escalation_matrix}
- **Communication Plan**: {incident_communication}
- **Status Page Management**: {status_page}
- **Postmortem Process**: {postmortem_process}
- **Action Item Tracking**: {action_item_tracking}
- **Lessons Learned**: {lessons_learned}
- **Process Improvement**: {incident_process_improvement}
- **Training Requirements**: {incident_training}

### Capacity Planning
- **Capacity Modeling**: {capacity_modeling}
- **Growth Projections**: {growth_projections}
- **Resource Planning**: {resource_planning}
- **Performance Testing**: {sre_performance_testing}
- **Load Testing**: {sre_load_testing}
- **Stress Testing**: {sre_stress_testing}
- **Capacity Monitoring**: {capacity_monitoring}
- **Scaling Policies**: {sre_scaling_policies}
- **Cost Optimization**: {sre_cost_optimization}
- **Procurement Planning**: {procurement_planning}

### Reliability Engineering
- **Reliability Principles**: {reliability_principles}
- **Fault Tolerance**: {fault_tolerance}
- **Circuit Breakers**: {sre_circuit_breakers}
- **Retry Logic**: {sre_retry_logic}
- **Graceful Degradation**: {graceful_degradation}
- **Chaos Engineering**: {chaos_engineering}
- **Disaster Recovery**: {sre_disaster_recovery}
- **Backup Strategy**: {sre_backup_strategy}
- **Testing Strategy**: {sre_testing_strategy}
- **Release Engineering**: {release_engineering}

Please provide detailed SLO definitions, monitoring setups, incident procedures, and reliability practices.

## Usage Examples

### E-commerce Platform SRE
```
Implement SRE practices for ShoppingPlatform web service with critical business criticality supporting 1M+ user base with peak traffic pattern.

Service Level Objectives:
- Define availability, latency, throughput SLI definitions
- Target 99.9% availability, <200ms p95 latency SLO targets
- Measure with load balancer logs, APM data sources
- Calculate monthly rolling window reporting period
- Review quarterly SLO targets with engineering/product stakeholder agreement

Error Budget Management:
- Define 0.1% monthly downtime error budget definition
- Calculate based on successful requests budget calculation
- Track 1%/5%/10% burn rate thresholds with Prometheus budget tracking
- Alert on 2x burn rate budget alerts with escalation to engineering manager
- Gate releases when budget <10% release gates

Monitoring Strategy:
- Use four golden signals sre monitoring strategy
- Collect RED/USE metrics sre metrics collection
- Aggregate with ELK stack sre log management
- Trace with Jaeger sre distributed tracing
- Create Grafana dashboards showing SLIs/SLOs sre dashboard design

Incident Management:
- Classify SEV1/2/3/4 based on user impact incident classification
- Follow ITIL-based response procedures with 15min/1hr/4hr escalation matrix
- Communicate via Slack, email, status page incident communication
- Conduct blameless postmortem process within 48 hours
- Track with Jira action item tracking and quarterly lessons learned reviews
```

## Best Practices

1. **Define meaningful SLIs that reflect user experience**
2. **Set realistic SLOs based on business requirements** 
3. **Use error budgets to balance reliability and velocity**
4. **Implement comprehensive monitoring and alerting**
5. **Conduct blameless postmortems and act on learnings**