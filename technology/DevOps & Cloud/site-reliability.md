---
category: technology/DevOps & Cloud
last_updated: 2025-11-09
related_templates:
- cloud-architecture-framework.md
- site-reliability-engineering.md
- cloud-migration-strategy.md
tags:
- communication
- design
- documentation
- management
- strategy
- technology
- template
title: Site Reliability Engineering Template
use_cases:
- Creating implement comprehensive sre practices including slo/sli definition, error
  budgets, incident management, monitoring, alerting, and reliability engineering
  for production systems.
- Project planning and execution
- Strategy development
---

# Site Reliability Engineering Template

## Purpose
Implement comprehensive SRE practices including SLO/SLI definition, error budgets, incident management, monitoring, alerting, and reliability engineering for production systems.

## Quick Start

**Implement SRE practices in 5 steps:**

1. **Define Service Level Indicators (SLIs)**: Identify key metrics that matter to users - availability, latency, error rate, throughput
2. **Set Service Level Objectives (SLOs)**: Establish realistic targets (e.g., 99.9% availability, <200ms p95 latency) with measurement windows
3. **Calculate Error Budgets**: Define acceptable downtime (e.g., 0.1% = 43.2 min/month) and burn rate thresholds
4. **Deploy Monitoring Stack**: Set up Prometheus/Grafana or DataDog with dashboards showing SLI compliance and error budget burn
5. **Create Incident Runbooks**: Document response procedures, escalation paths, and postmortem templates

**Quick SLO Example:**
```yaml
service: api-gateway
slo:
  availability: 99.9%  # 43.2 min downtime/month
  latency_p95: 200ms
  error_rate: <1%
  measurement_window: 30_days

error_budget:
  total: 0.1%
  alert_on_burn_rate: 2x  # Alert if burning budget 2x faster than planned
```

## Template Structure

### SRE Overview
- **Service Name**: [SERVICE_NAME]
- **Service Type**: [SERVICE_TYPE]
- **Business Criticality**: [BUSINESS_CRITICALITY]
- **User Base**: [USER_BASE]
- **Traffic Pattern**: [TRAFFIC_PATTERN]
- **Reliability Requirements**: [RELIABILITY_REQUIREMENTS]
- **Team Structure**: [SRE_TEAM_STRUCTURE]
- **Responsibilities**: [SRE_RESPONSIBILITIES]
- **Tools and Technologies**: [SRE_TOOLS]
- **Budget**: [SRE_BUDGET]

### Service Level Objectives
- **SLI Definitions**: [SLI_DEFINITIONS]
- **SLO Targets**: [SLO_TARGETS]
- **Measurement Methods**: [MEASUREMENT_METHODS]
- **Data Sources**: [DATA_SOURCES]
- **Calculation Logic**: [CALCULATION_LOGIC]
- **Reporting Period**: [REPORTING_PERIOD]
- **SLO Review Process**: [SLO_REVIEW_PROCESS]
- **Stakeholder Agreement**: [STAKEHOLDER_AGREEMENT]
- **SLO Documentation**: [SLO_DOCUMENTATION]
- **Communication Plan**: [SLO_COMMUNICATION]

### Error Budget Management
- **Error Budget Definition**: [ERROR_BUDGET_DEFINITION]
- **Budget Calculation**: [BUDGET_CALCULATION]
- **Burn Rate**: [BURN_RATE]
- **Budget Tracking**: [BUDGET_TRACKING]
- **Budget Alerts**: [BUDGET_ALERTS]
- **Budget Policies**: [BUDGET_POLICIES]
- **Escalation Triggers**: [ESCALATION_TRIGGERS]
- **Feature Release Gates**: [RELEASE_GATES]
- **Budget Reporting**: [BUDGET_REPORTING]
- **Recovery Actions**: [RECOVERY_ACTIONS]

### Monitoring and Observability
- **Monitoring Strategy**: [SRE_MONITORING_STRATEGY]
- **Metrics Collection**: [SRE_METRICS_COLLECTION]
- **Log Management**: [SRE_LOG_MANAGEMENT]
- **Distributed Tracing**: [SRE_DISTRIBUTED_TRACING]
- **Dashboard Design**: [SRE_DASHBOARD_DESIGN]
- **Alerting Strategy**: [SRE_ALERTING_STRATEGY]
- **On-Call Management**: [ONCALL_MANAGEMENT]
- **Runbook Creation**: [RUNBOOK_CREATION]
- **Playbook Development**: [PLAYBOOK_DEVELOPMENT]
- **Tool Integration**: [SRE_TOOL_INTEGRATION]

### Incident Management
- **Incident Classification**: [INCIDENT_CLASSIFICATION]
- **Response Procedures**: [RESPONSE_PROCEDURES]
- **Escalation Matrix**: [ESCALATION_MATRIX]
- **Communication Plan**: [INCIDENT_COMMUNICATION]
- **Status Page Management**: [STATUS_PAGE]
- **Postmortem Process**: [POSTMORTEM_PROCESS]
- **Action Item Tracking**: [ACTION_ITEM_TRACKING]
- **Lessons Learned**: [LESSONS_LEARNED]
- **Process Improvement**: [INCIDENT_PROCESS_IMPROVEMENT]
- **Training Requirements**: [INCIDENT_TRAINING]

### Capacity Planning
- **Capacity Modeling**: [CAPACITY_MODELING]
- **Growth Projections**: [GROWTH_PROJECTIONS]
- **Resource Planning**: [RESOURCE_PLANNING]
- **Performance Testing**: [SRE_PERFORMANCE_TESTING]
- **Load Testing**: [SRE_LOAD_TESTING]
- **Stress Testing**: [SRE_STRESS_TESTING]
- **Capacity Monitoring**: [CAPACITY_MONITORING]
- **Scaling Policies**: [SRE_SCALING_POLICIES]
- **Cost Optimization**: [SRE_COST_OPTIMIZATION]
- **Procurement Planning**: [PROCUREMENT_PLANNING]

### Reliability Engineering
- **Reliability Principles**: [RELIABILITY_PRINCIPLES]
- **Fault Tolerance**: [FAULT_TOLERANCE]
- **Circuit Breakers**: [SRE_CIRCUIT_BREAKERS]
- **Retry Logic**: [SRE_RETRY_LOGIC]
- **Graceful Degradation**: [GRACEFUL_DEGRADATION]
- **Chaos Engineering**: [CHAOS_ENGINEERING]
- **Disaster Recovery**: [SRE_DISASTER_RECOVERY]
- **Backup Strategy**: [SRE_BACKUP_STRATEGY]
- **Testing Strategy**: [SRE_TESTING_STRATEGY]
- **Release Engineering**: [RELEASE_ENGINEERING]

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
| `[SERVICE_NAME]` | Specify the service name | "John Smith" |
| `[SERVICE_TYPE]` | Specify the service type | "Standard" |
| `[BUSINESS_CRITICALITY]` | Specify the business criticality | "[specify value]" |
| `[USER_BASE]` | Specify the user base | "[specify value]" |
| `[TRAFFIC_PATTERN]` | Specify the traffic pattern | "[specify value]" |
| `[RELIABILITY_REQUIREMENTS]` | Specify the reliability requirements | "[specify value]" |
| `[SRE_TEAM_STRUCTURE]` | Specify the sre team structure | "[specify value]" |
| `[SRE_RESPONSIBILITIES]` | Specify the sre responsibilities | "[specify value]" |
| `[SRE_TOOLS]` | Specify the sre tools | "[specify value]" |
| `[SRE_BUDGET]` | Specify the sre budget | "$500,000" |
| `[SLI_DEFINITIONS]` | Specify the sli definitions | "[specify value]" |
| `[SLO_TARGETS]` | Specify the slo targets | "[specify value]" |
| `[MEASUREMENT_METHODS]` | Specify the measurement methods | "[specify value]" |
| `[DATA_SOURCES]` | Specify the data sources | "[specify value]" |
| `[CALCULATION_LOGIC]` | Specify the calculation logic | "[specify value]" |
| `[REPORTING_PERIOD]` | Specify the reporting period | "[specify value]" |
| `[SLO_REVIEW_PROCESS]` | Specify the slo review process | "[specify value]" |
| `[STAKEHOLDER_AGREEMENT]` | Specify the stakeholder agreement | "[specify value]" |
| `[SLO_DOCUMENTATION]` | Specify the slo documentation | "[specify value]" |
| `[SLO_COMMUNICATION]` | Specify the slo communication | "[specify value]" |
| `[ERROR_BUDGET_DEFINITION]` | Specify the error budget definition | "$500,000" |
| `[BUDGET_CALCULATION]` | Specify the budget calculation | "$500,000" |
| `[BURN_RATE]` | Specify the burn rate | "[specify value]" |
| `[BUDGET_TRACKING]` | Specify the budget tracking | "$500,000" |
| `[BUDGET_ALERTS]` | Specify the budget alerts | "$500,000" |
| `[BUDGET_POLICIES]` | Specify the budget policies | "$500,000" |
| `[ESCALATION_TRIGGERS]` | Specify the escalation triggers | "[specify value]" |
| `[RELEASE_GATES]` | Specify the release gates | "[specify value]" |
| `[BUDGET_REPORTING]` | Specify the budget reporting | "$500,000" |
| `[RECOVERY_ACTIONS]` | Specify the recovery actions | "[specify value]" |
| `[SRE_MONITORING_STRATEGY]` | Specify the sre monitoring strategy | "[specify value]" |
| `[SRE_METRICS_COLLECTION]` | Specify the sre metrics collection | "[specify value]" |
| `[SRE_LOG_MANAGEMENT]` | Specify the sre log management | "[specify value]" |
| `[SRE_DISTRIBUTED_TRACING]` | Specify the sre distributed tracing | "[specify value]" |
| `[SRE_DASHBOARD_DESIGN]` | Specify the sre dashboard design | "[specify value]" |
| `[SRE_ALERTING_STRATEGY]` | Specify the sre alerting strategy | "[specify value]" |
| `[ONCALL_MANAGEMENT]` | Specify the oncall management | "[specify value]" |
| `[RUNBOOK_CREATION]` | Specify the runbook creation | "[specify value]" |
| `[PLAYBOOK_DEVELOPMENT]` | Specify the playbook development | "[specify value]" |
| `[SRE_TOOL_INTEGRATION]` | Specify the sre tool integration | "[specify value]" |
| `[INCIDENT_CLASSIFICATION]` | Specify the incident classification | "[specify value]" |
| `[RESPONSE_PROCEDURES]` | Specify the response procedures | "[specify value]" |
| `[ESCALATION_MATRIX]` | Specify the escalation matrix | "[specify value]" |
| `[INCIDENT_COMMUNICATION]` | Specify the incident communication | "[specify value]" |
| `[STATUS_PAGE]` | Specify the status page | "In Progress" |
| `[POSTMORTEM_PROCESS]` | Specify the postmortem process | "[specify value]" |
| `[ACTION_ITEM_TRACKING]` | Specify the action item tracking | "[specify value]" |
| `[LESSONS_LEARNED]` | Specify the lessons learned | "[specify value]" |
| `[INCIDENT_PROCESS_IMPROVEMENT]` | Specify the incident process improvement | "[specify value]" |
| `[INCIDENT_TRAINING]` | Specify the incident training | "[specify value]" |
| `[CAPACITY_MODELING]` | Specify the capacity modeling | "[specify value]" |
| `[GROWTH_PROJECTIONS]` | Specify the growth projections | "[specify value]" |
| `[RESOURCE_PLANNING]` | Specify the resource planning | "[specify value]" |
| `[SRE_PERFORMANCE_TESTING]` | Specify the sre performance testing | "[specify value]" |
| `[SRE_LOAD_TESTING]` | Specify the sre load testing | "[specify value]" |
| `[SRE_STRESS_TESTING]` | Specify the sre stress testing | "[specify value]" |
| `[CAPACITY_MONITORING]` | Specify the capacity monitoring | "[specify value]" |
| `[SRE_SCALING_POLICIES]` | Specify the sre scaling policies | "[specify value]" |
| `[SRE_COST_OPTIMIZATION]` | Specify the sre cost optimization | "[specify value]" |
| `[PROCUREMENT_PLANNING]` | Specify the procurement planning | "[specify value]" |
| `[RELIABILITY_PRINCIPLES]` | Specify the reliability principles | "[specify value]" |
| `[FAULT_TOLERANCE]` | Specify the fault tolerance | "[specify value]" |
| `[SRE_CIRCUIT_BREAKERS]` | Specify the sre circuit breakers | "[specify value]" |
| `[SRE_RETRY_LOGIC]` | Specify the sre retry logic | "[specify value]" |
| `[GRACEFUL_DEGRADATION]` | Specify the graceful degradation | "[specify value]" |
| `[CHAOS_ENGINEERING]` | Specify the chaos engineering | "[specify value]" |
| `[SRE_DISASTER_RECOVERY]` | Specify the sre disaster recovery | "[specify value]" |
| `[SRE_BACKUP_STRATEGY]` | Specify the sre backup strategy | "[specify value]" |
| `[SRE_TESTING_STRATEGY]` | Specify the sre testing strategy | "[specify value]" |
| `[RELEASE_ENGINEERING]` | Specify the release engineering | "[specify value]" |



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Site Reliability Engineering Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/DevOps & Cloud](../../technology/DevOps & Cloud/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating implement comprehensive sre practices including slo/sli definition, error budgets, incident management, monitoring, alerting, and reliability engineering for production systems.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Define meaningful SLIs that reflect user experience**
2. **Set realistic SLOs based on business requirements**
3. **Use error budgets to balance reliability and velocity**
4. **Implement comprehensive monitoring and alerting**
5. **Conduct blameless postmortems and act on learnings**