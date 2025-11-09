---
title: Site Reliability Engineering Template
category: technology/DevOps & Cloud
tags: [communication, design, documentation, management, strategy, technology, template]
use_cases:
  - Implementing implement comprehensive sre practices including slo/sli definition, error budget...
  - Project planning and execution
  - Strategy development
related_templates:
  - cloud-architecture-framework.md
  - site-reliability-engineering.md
  - cloud-migration-strategy.md
last_updated: 2025-11-09
---

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

### Monitoring Strategy
- Use four golden signals sre monitoring strategy
- Collect RED/USE metrics sre metrics collection
- Aggregate with ELK stack sre log management
- Trace with Jaeger sre distributed tracing
- Create Grafana dashboards showing SLIs/SLOs sre dashboard design

### Incident Management
- Classify SEV1/2/3/4 based on user impact incident classification
- Follow ITIL-based response procedures with 15min/1hr/4hr escalation matrix
- Communicate via Slack, email, status page incident communication
- Conduct blameless postmortem process within 48 hours
- Track with Jira action item tracking and quarterly lessons learned reviews
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `{service_name}` | Specify the service name | "John Smith" |
| `{service_type}` | Specify the service type | "Standard" |
| `{business_criticality}` | Specify the business criticality | "[specify value]" |
| `{user_base}` | Specify the user base | "[specify value]" |
| `{traffic_pattern}` | Specify the traffic pattern | "[specify value]" |
| `{reliability_requirements}` | Specify the reliability requirements | "[specify value]" |
| `{sre_team_structure}` | Specify the sre team structure | "[specify value]" |
| `{sre_responsibilities}` | Specify the sre responsibilities | "[specify value]" |
| `{sre_tools}` | Specify the sre tools | "[specify value]" |
| `{sre_budget}` | Specify the sre budget | "$500,000" |
| `{sli_definitions}` | Specify the sli definitions | "[specify value]" |
| `{slo_targets}` | Specify the slo targets | "[specify value]" |
| `{measurement_methods}` | Specify the measurement methods | "[specify value]" |
| `{data_sources}` | Specify the data sources | "[specify value]" |
| `{calculation_logic}` | Specify the calculation logic | "[specify value]" |
| `{reporting_period}` | Specify the reporting period | "[specify value]" |
| `{slo_review_process}` | Specify the slo review process | "[specify value]" |
| `{stakeholder_agreement}` | Specify the stakeholder agreement | "[specify value]" |
| `{slo_documentation}` | Specify the slo documentation | "[specify value]" |
| `{slo_communication}` | Specify the slo communication | "[specify value]" |
| `{error_budget_definition}` | Specify the error budget definition | "$500,000" |
| `{budget_calculation}` | Specify the budget calculation | "$500,000" |
| `{burn_rate}` | Specify the burn rate | "[specify value]" |
| `{budget_tracking}` | Specify the budget tracking | "$500,000" |
| `{budget_alerts}` | Specify the budget alerts | "$500,000" |
| `{budget_policies}` | Specify the budget policies | "$500,000" |
| `{escalation_triggers}` | Specify the escalation triggers | "[specify value]" |
| `{release_gates}` | Specify the release gates | "[specify value]" |
| `{budget_reporting}` | Specify the budget reporting | "$500,000" |
| `{recovery_actions}` | Specify the recovery actions | "[specify value]" |
| `{sre_monitoring_strategy}` | Specify the sre monitoring strategy | "[specify value]" |
| `{sre_metrics_collection}` | Specify the sre metrics collection | "[specify value]" |
| `{sre_log_management}` | Specify the sre log management | "[specify value]" |
| `{sre_distributed_tracing}` | Specify the sre distributed tracing | "[specify value]" |
| `{sre_dashboard_design}` | Specify the sre dashboard design | "[specify value]" |
| `{sre_alerting_strategy}` | Specify the sre alerting strategy | "[specify value]" |
| `{oncall_management}` | Specify the oncall management | "[specify value]" |
| `{runbook_creation}` | Specify the runbook creation | "[specify value]" |
| `{playbook_development}` | Specify the playbook development | "[specify value]" |
| `{sre_tool_integration}` | Specify the sre tool integration | "[specify value]" |
| `{incident_classification}` | Specify the incident classification | "[specify value]" |
| `{response_procedures}` | Specify the response procedures | "[specify value]" |
| `{escalation_matrix}` | Specify the escalation matrix | "[specify value]" |
| `{incident_communication}` | Specify the incident communication | "[specify value]" |
| `{status_page}` | Specify the status page | "In Progress" |
| `{postmortem_process}` | Specify the postmortem process | "[specify value]" |
| `{action_item_tracking}` | Specify the action item tracking | "[specify value]" |
| `{lessons_learned}` | Specify the lessons learned | "[specify value]" |
| `{incident_process_improvement}` | Specify the incident process improvement | "[specify value]" |
| `{incident_training}` | Specify the incident training | "[specify value]" |
| `{capacity_modeling}` | Specify the capacity modeling | "[specify value]" |
| `{growth_projections}` | Specify the growth projections | "[specify value]" |
| `{resource_planning}` | Specify the resource planning | "[specify value]" |
| `{sre_performance_testing}` | Specify the sre performance testing | "[specify value]" |
| `{sre_load_testing}` | Specify the sre load testing | "[specify value]" |
| `{sre_stress_testing}` | Specify the sre stress testing | "[specify value]" |
| `{capacity_monitoring}` | Specify the capacity monitoring | "[specify value]" |
| `{sre_scaling_policies}` | Specify the sre scaling policies | "[specify value]" |
| `{sre_cost_optimization}` | Specify the sre cost optimization | "[specify value]" |
| `{procurement_planning}` | Specify the procurement planning | "[specify value]" |
| `{reliability_principles}` | Specify the reliability principles | "[specify value]" |
| `{fault_tolerance}` | Specify the fault tolerance | "[specify value]" |
| `{sre_circuit_breakers}` | Specify the sre circuit breakers | "[specify value]" |
| `{sre_retry_logic}` | Specify the sre retry logic | "[specify value]" |
| `{graceful_degradation}` | Specify the graceful degradation | "[specify value]" |
| `{chaos_engineering}` | Specify the chaos engineering | "[specify value]" |
| `{sre_disaster_recovery}` | Specify the sre disaster recovery | "[specify value]" |
| `{sre_backup_strategy}` | Specify the sre backup strategy | "[specify value]" |
| `{sre_testing_strategy}` | Specify the sre testing strategy | "[specify value]" |
| `{release_engineering}` | Specify the release engineering | "[specify value]" |



## Best Practices

1. **Define meaningful SLIs that reflect user experience**
2. **Set realistic SLOs based on business requirements** 
3. **Use error budgets to balance reliability and velocity**
4. **Implement comprehensive monitoring and alerting**
5. **Conduct blameless postmortems and act on learnings**