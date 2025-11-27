---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- sre
- slo-sli
- error-budgets
- incident-management
title: Site Reliability Engineering Template
use_cases:
- Creating implement comprehensive sre practices including slo/sli definition, error
  budgets, incident management, monitoring, alerting, and reliability engineering
  for production systems.
- Project planning and execution
- Strategy development
industries:
- technology
type: template
difficulty: intermediate
slug: site-reliability
---

# Site Reliability Engineering Template

## Purpose
Implement comprehensive SRE practices including SLO/SLI definition, error budgets, incident management, monitoring, alerting, and reliability engineering for production systems.

## Quick SRE Prompt
Implement SRE for [service] targeting [X users]. Define SLIs: availability, latency (p50/p95/p99), error rate, throughput. Set SLOs: [99.X%] availability, <[Y]ms latency. Calculate error budget ([Z] min/month downtime). Deploy: [Prometheus/DataDog] monitoring, PagerDuty alerting on burn rate. Create: on-call rotation, incident runbooks, postmortem template. Track: MTTR, incident frequency, error budget consumption.

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
| `[BUSINESS_CRITICALITY]` | Specify the business criticality | "Tier 1 - Revenue Critical", "Tier 2 - Business Essential", "Tier 3 - Internal Support" |
| `[USER_BASE]` | Specify the user base | "1M+ monthly active users", "10K enterprise customers", "Internal 5K employees" |
| `[TRAFFIC_PATTERN]` | Specify the traffic pattern | "Steady weekday traffic", "Seasonal peaks (Black Friday)", "Bursty event-driven" |
| `[RELIABILITY_REQUIREMENTS]` | Specify the reliability requirements | "99.9% availability (8.76hr downtime/year)", "99.99% for critical services" |
| `[SRE_TEAM_STRUCTURE]` | Specify the sre team structure | "Embedded SRE per product team", "Central SRE platform team", "Hybrid model" |
| `[SRE_RESPONSIBILITIES]` | Specify the sre responsibilities | "SLO definition", "Incident response", "Capacity planning", "Reliability reviews" |
| `[SRE_TOOLS]` | Specify the sre tools | "Prometheus + Grafana", "PagerDuty", "Datadog", "Jaeger", "Terraform"
| `[SRE_BUDGET]` | Specify the sre budget | "$500,000" |
| `[SLI_DEFINITIONS]` | Specify the sli definitions | "Availability: successful requests / total requests", "Latency: p95 response time", "Error rate: 5xx / total" |
| `[SLO_TARGETS]` | Specify the slo targets | "99.9% availability", "p95 latency < 200ms", "Error rate < 0.1%" |
| `[MEASUREMENT_METHODS]` | Specify the measurement methods | "Prometheus metrics", "Load balancer logs", "Synthetic monitoring", "Real user monitoring" |
| `[DATA_SOURCES]` | Specify the data sources | "CloudWatch metrics", "Application logs", "APM traces", "CDN analytics" |
| `[CALCULATION_LOGIC]` | Specify the calculation logic | "30-day rolling window", "Excluding planned maintenance", "Weighted by request volume" |
| `[REPORTING_PERIOD]` | Specify the reporting period | "30-day rolling", "Weekly reports", "Monthly review", "Quarterly business review" |
| `[SLO_REVIEW_PROCESS]` | Specify the slo review process | "Quarterly SLO review meeting", "Annual target adjustment", "Post-incident SLO analysis" |
| `[STAKEHOLDER_AGREEMENT]` | Specify the stakeholder agreement | "Engineering + Product alignment", "Executive sponsor sign-off", "Customer communication" |
| `[SLO_DOCUMENTATION]` | Specify the slo documentation | "Confluence SLO page", "Runbook links", "Dashboard URLs", "Contact information" |
| `[SLO_COMMUNICATION]` | Specify the slo communication | "Weekly Slack report", "Monthly email summary", "Real-time dashboard", "Status page"
| `[ERROR_BUDGET_DEFINITION]` | Specify the error budget definition | "$500,000" |
| `[BUDGET_CALCULATION]` | Specify the budget calculation | "$500,000" |
| `[BURN_RATE]` | Specify the burn rate | "1x (sustainable)", "2x (alert threshold)", "10x (critical - page immediately)"
| `[BUDGET_TRACKING]` | Specify the budget tracking | "$500,000" |
| `[BUDGET_ALERTS]` | Specify the budget alerts | "$500,000" |
| `[BUDGET_POLICIES]` | Specify the budget policies | "$500,000" |
| `[ESCALATION_TRIGGERS]` | Specify the escalation triggers | "50% budget consumed in 1 week", "10x burn rate for 5 minutes", "SLO breach imminent" |
| `[RELEASE_GATES]` | Specify the release gates | "Block releases when budget < 10%", "Require approval when < 25%", "Auto-approve when > 50%"
| `[BUDGET_REPORTING]` | Specify the budget reporting | "$500,000" |
| `[RECOVERY_ACTIONS]` | Specify the recovery actions | "Freeze deployments", "Enable feature flags", "Scale up resources", "Rollback last change" |
| `[SRE_MONITORING_STRATEGY]` | Specify the sre monitoring strategy | "Four Golden Signals (latency, traffic, errors, saturation)", "RED method", "USE method" |
| `[SRE_METRICS_COLLECTION]` | Specify the sre metrics collection | "Prometheus + exporters", "StatsD", "OpenTelemetry", "CloudWatch agent" |
| `[SRE_LOG_MANAGEMENT]` | Specify the sre log management | "ELK Stack (Elasticsearch, Logstash, Kibana)", "Loki + Grafana", "Splunk", "CloudWatch Logs" |
| `[SRE_DISTRIBUTED_TRACING]` | Specify the sre distributed tracing | "Jaeger", "Zipkin", "AWS X-Ray", "Datadog APM", "OpenTelemetry" |
| `[SRE_DASHBOARD_DESIGN]` | Specify the sre dashboard design | "SLO status overview", "Service health grid", "Error budget burn", "On-call summary" |
| `[SRE_ALERTING_STRATEGY]` | Specify the sre alerting strategy | "Symptom-based alerts", "Multi-window burn rate", "Alert routing by severity" |
| `[ONCALL_MANAGEMENT]` | Specify the oncall management | "PagerDuty rotation", "1-week shifts", "Follow-the-sun", "Secondary on-call backup" |
| `[RUNBOOK_CREATION]` | Specify the runbook creation | "Templated runbooks in Confluence", "Automated runbook links in alerts", "Version controlled" |
| `[PLAYBOOK_DEVELOPMENT]` | Specify the playbook development | "Incident response playbooks", "Disaster recovery procedures", "Escalation guides" |
| `[SRE_TOOL_INTEGRATION]` | Specify the sre tool integration | "Slack + PagerDuty", "Jira for tickets", "GitHub for code", "Terraform for infra" |
| `[INCIDENT_CLASSIFICATION]` | Specify the incident classification | "SEV1: Revenue impact, all-hands", "SEV2: Degraded, team response", "SEV3: Minor, async fix" |
| `[RESPONSE_PROCEDURES]` | Specify the response procedures | "Acknowledge < 5min", "Assemble team < 15min", "Status update every 30min" |
| `[ESCALATION_MATRIX]` | Specify the escalation matrix | "L1: On-call engineer", "L2: Team lead", "L3: Engineering manager", "L4: VP Engineering" |
| `[INCIDENT_COMMUNICATION]` | Specify the incident communication | "Slack #incidents channel", "Status page updates", "Customer email for SEV1"
| `[STATUS_PAGE]` | Specify the status page | "In Progress" |
| `[POSTMORTEM_PROCESS]` | Specify the postmortem process | "Blameless postmortem within 48hrs", "5 Whys analysis", "Timeline reconstruction" |
| `[ACTION_ITEM_TRACKING]` | Specify the action item tracking | "Jira epic per incident", "Owner assigned", "Due dates enforced", "Weekly review" |
| `[LESSONS_LEARNED]` | Specify the lessons learned | "Quarterly review meeting", "Shared knowledge base", "Pattern identification" |
| `[INCIDENT_PROCESS_IMPROVEMENT]` | Specify the incident process improvement | "Retrospective after each SEV1", "Tool improvements", "Runbook updates" |
| `[INCIDENT_TRAINING]` | Specify the incident training | "Quarterly incident response drills", "New hire on-call shadowing", "Game days" |
| `[CAPACITY_MODELING]` | Specify the capacity modeling | "Load testing extrapolation", "Historical growth trends", "Business forecast alignment" |
| `[GROWTH_PROJECTIONS]` | Specify the growth projections | "20% YoY traffic growth", "Seasonal peak 3x baseline", "New feature impact estimates" |
| `[RESOURCE_PLANNING]` | Specify the resource planning | "Quarterly capacity reviews", "Reserved instance planning", "Headroom buffers (20%)" |
| `[SRE_PERFORMANCE_TESTING]` | Specify the sre performance testing | "k6 load tests", "Gatling scenarios", "Production traffic replay" |
| `[SRE_LOAD_TESTING]` | Specify the sre load testing | "Weekly load tests", "Pre-release validation", "Peak traffic simulation" |
| `[SRE_STRESS_TESTING]` | Specify the sre stress testing | "Breaking point identification", "Failure mode analysis", "Recovery time measurement" |
| `[CAPACITY_MONITORING]` | Specify the capacity monitoring | "CPU/memory utilization trends", "Storage growth rates", "Connection pool usage" |
| `[SRE_SCALING_POLICIES]` | Specify the sre scaling policies | "HPA at 70% CPU", "Scale out before scale up", "Predictive scaling for known events" |
| `[SRE_COST_OPTIMIZATION]` | Specify the sre cost optimization | "Right-sizing recommendations", "Spot instances for batch", "Reserved capacity for baseline" |
| `[PROCUREMENT_PLANNING]` | Specify the procurement planning | "6-month hardware lead time", "Annual reserved instance commits", "Vendor negotiations" |
| `[RELIABILITY_PRINCIPLES]` | Specify the reliability principles | "Design for failure", "Automate recovery", "Prefer simplicity", "Monitor everything" |
| `[FAULT_TOLERANCE]` | Specify the fault tolerance | "Multi-AZ deployment", "Active-active regions", "N+1 redundancy", "Graceful failover" |
| `[SRE_CIRCUIT_BREAKERS]` | Specify the sre circuit breakers | "Resilience4j", "Hystrix (legacy)", "Envoy circuit breaking", "Custom implementations" |
| `[SRE_RETRY_LOGIC]` | Specify the sre retry logic | "Exponential backoff", "Jitter added", "Max 3 retries", "Idempotency required" |
| `[GRACEFUL_DEGRADATION]` | Specify the graceful degradation | "Feature flags for non-critical", "Cached fallbacks", "Static error pages", "Queue backpressure" |
| `[CHAOS_ENGINEERING]` | Specify the chaos engineering | "Chaos Monkey", "Gremlin", "LitmusChaos", "Monthly game days" |
| `[SRE_DISASTER_RECOVERY]` | Specify the sre disaster recovery | "RPO < 1hr", "RTO < 4hr", "Cross-region failover", "Annual DR drills" |
| `[SRE_BACKUP_STRATEGY]` | Specify the sre backup strategy | "Daily snapshots", "Cross-region replication", "Point-in-time recovery", "Backup testing" |
| `[SRE_TESTING_STRATEGY]` | Specify the sre testing strategy | "Canary deployments", "Blue-green releases", "Feature flag rollouts", "Synthetic testing" |
| `[RELEASE_ENGINEERING]` | Specify the release engineering | "GitOps with ArgoCD", "Automated rollbacks", "Progressive delivery", "Release trains"



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