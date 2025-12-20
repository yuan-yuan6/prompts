---
category: technology
related_templates:
- technology/DevOps-Cloud/infrastructure-management.md
- technology/DevOps-Cloud/cloud-architecture.md
- technology/DevOps-Cloud/ci-cd-pipelines.md
tags:
- sre
- slo-sli
- error-budgets
- incident-management
title: Site Reliability Engineering
use_cases:
- Implementing SLO/SLI frameworks with error budgets balancing reliability targets (99.9%) against feature velocity for production services
- Building incident management practices with on-call rotations, runbooks, and blameless postmortems achieving <15 minute MTTR for critical incidents
- Designing observability strategies with multi-window burn rate alerting reducing alert fatigue while catching real issues
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: site-reliability
---

# Site Reliability Engineering

## Purpose
Implement comprehensive SRE practices covering SLO/SLI definition, error budget management, incident response, observability, and reliability engineering achieving sustainable reliability targets while enabling feature velocity.

## 🚀 Quick SRE Prompt

> Implement SRE for **[SERVICE]** serving **[USERS]** users. SLIs: availability (**[GOOD_REQUESTS/TOTAL]**), latency (**[P50/P95/P99]**ms), error rate (**[X]**%). SLOs: **[99.X]**% availability, p95 <**[Y]**ms. Error budget: **[Z]** minutes/month downtime. Monitoring: **[PROMETHEUS/DATADOG]** with **[PAGERDUTY/OPSGENIE]** alerting. Burn rate thresholds: 2x (page), 6x (ticket). On-call: **[ROTATION]** shifts. Track: MTTR **[TARGET]**, incident frequency, budget consumption.

---

## Template

Implement SRE practices for {SERVICE_NAME} with {CRITICALITY} criticality serving {USER_BASE} achieving {AVAILABILITY_TARGET}% availability and {LATENCY_TARGET} p95 latency.

**SERVICE LEVEL OBJECTIVES**

Define SLIs measuring what users actually experience. Availability SLI: successful requests / total requests (exclude health checks, internal traffic). Latency SLI: requests completing within threshold (p50 <50ms, p95 <200ms, p99 <500ms are common targets). Error SLI: 5xx errors / total requests (distinguish client errors 4xx from server errors). Throughput SLI: requests per second capacity, critical for batch systems. Freshness SLI: data age for async systems (pipeline freshness, cache staleness).

Set SLOs based on user expectations and business requirements. Availability tiers: 99% (3.65 days downtime/year, acceptable for internal tools), 99.9% (8.76 hours, standard for most production services), 99.99% (52 minutes, premium/critical services), 99.999% (5 minutes, extremely high cost). Latency targets: measure at user-facing edge, not internal services. Composite SLOs: combine multiple SLIs (availability AND latency within target). Measurement window: 30-day rolling window most common, weekly for fast-moving services.

Calculate error budgets enabling reliability-velocity tradeoff. Budget calculation: 100% - SLO target = error budget (99.9% SLO = 0.1% budget = 43.2 min/month). Burn rate: how fast you're consuming budget (1x = sustainable, 2x = concerning, 10x = critical). Multi-window alerts: 1-hour window for fast burns (10x), 6-hour for moderate (2x), catch both acute and slow degradation. Budget policy: >50% remaining = ship features freely, 25-50% = ship with caution, <25% = reliability focus only, <10% = freeze releases.

**MONITORING AND OBSERVABILITY**

Implement the four golden signals for service health. Latency: response time distribution (p50/p95/p99), separate success vs error latency. Traffic: requests per second, concurrent users, message queue depth. Errors: error rate by type (4xx, 5xx, timeout), error budget burn. Saturation: CPU/memory utilization, connection pool usage, queue depth. Dashboard hierarchy: NOC view (all services), service view (single service health), debug view (detailed metrics).

Configure intelligent alerting minimizing noise while catching real issues. Symptom-based alerts: alert on user impact (error rate, latency), not causes (CPU high). Multi-window burn rate: short window (1hr) high threshold (14x) + long window (6hr) lower threshold (2x) = catch fast burns and slow bleeds. Alert severity: critical (page immediately, customer impact), warning (investigate next business day), info (tracked, no notification). Routing: PagerDuty/Opsgenie with escalation policies, acknowledge SLA, auto-escalate if not acknowledged.

Build debugging capability through observability. Metrics: Prometheus for collection, Grafana for visualization, 15-second scrape interval, 15-day retention (downsample for longer). Logs: structured JSON, correlation IDs, centralized aggregation (Loki, Elasticsearch), 7-day hot storage. Traces: OpenTelemetry instrumentation, distributed trace backends (Jaeger, Tempo), sampling 1-10% for cost control. Correlation: link traces to logs to metrics, enable drill-down from dashboard to specific request.

**INCIDENT MANAGEMENT**

Establish incident classification and response procedures. Severity levels: SEV1 (full outage, customer facing, all-hands), SEV2 (degraded service, significant impact), SEV3 (minor impact, single customer or feature), SEV4 (no current impact, potential issue). Response times: SEV1 acknowledge <5 min, assemble team <15 min, status updates every 30 min. Roles: Incident Commander (coordinates), Tech Lead (drives resolution), Communications Lead (updates stakeholders).

Implement effective on-call practices. Rotation structure: 1-week shifts, 2-person rotation (primary + secondary), handoff meetings. Compensation: on-call pay, time off after incidents, respect work-life balance. Escalation: primary has 5 min to acknowledge, then secondary, then manager. On-call load: target <2 pages per shift, investigate if consistently higher. Shadow program: new engineers shadow 2 weeks before joining rotation.

Create runbooks enabling consistent incident response. Runbook content: symptoms (what alert fires), diagnosis steps (how to investigate), remediation actions (how to fix), escalation criteria (when to escalate). Runbook format: concise, step-by-step, tested regularly, linked from alerts. Common runbooks: service restart, database failover, traffic reroute, dependency failure, capacity scaling. Automation: link runbooks to automated remediation where safe (restart pod, scale out).

Conduct blameless postmortems driving improvement. Postmortem timing: within 48 hours for SEV1/SEV2, within 1 week for SEV3. Format: timeline, impact, root cause (5 Whys), contributing factors, action items. Blameless culture: focus on systems and processes, not individuals, "how did the system allow this to happen?" Action items: specific, owned, due-dated, tracked to completion, reviewed in team meetings. Pattern analysis: quarterly review of incidents, identify themes, prioritize systemic fixes.

**RELIABILITY ENGINEERING**

Design systems for failure tolerance. Redundancy: N+1 for critical components, multi-AZ deployment, active-active when possible. Timeouts: explicit timeouts on all network calls (connect timeout + read timeout), fail fast. Retries: exponential backoff with jitter, max 3 retries, idempotent operations only. Circuit breakers: fail-open for non-critical dependencies, configurable thresholds (5 failures in 10 seconds). Bulkheads: isolate failure domains, separate thread pools for different dependencies.

Implement graceful degradation maintaining core functionality. Feature tiers: identify must-have (checkout) vs nice-to-have (recommendations) features. Degraded modes: serve cached data when backend slow, show partial results, disable expensive features. Load shedding: reject new requests when overloaded, prioritize existing users. Backpressure: slow down producers when consumers overwhelmed, queue depth limits. Feature flags: runtime control to disable problematic features without deployment.

Practice chaos engineering validating resilience. Chaos experiments: kill instances, inject latency, simulate AZ failure, exhaust resources. Game days: scheduled chaos experiments with team assembled, practice incident response. Steady state hypothesis: define normal behavior, verify system returns to normal after experiment. Blast radius: start small (single instance), expand gradually (AZ, region). Tools: Chaos Monkey, Gremlin, LitmusChaos, AWS Fault Injection Simulator.

**CAPACITY PLANNING**

Forecast capacity requirements proactively. Utilization monitoring: track CPU, memory, disk, network trends weekly. Growth modeling: linear extrapolation for steady growth, event-based modeling for launches. Headroom targets: 30% headroom for organic growth, additional buffer for peak events. Lead time: 4-week lead time for reserved capacity, plan quarterly. Performance testing: validate capacity model with load tests, identify bottlenecks before production.

Plan for peak events and disasters. Peak planning: 3x baseline capacity for known events (Black Friday, launches), pre-scaling 24 hours before. Disaster recovery: RPO (data loss tolerance) and RTO (downtime tolerance) targets, tested quarterly. Failover capacity: ensure DR region can handle production load, regular failover drills. Cost optimization: balance always-on capacity (expensive, instant) vs scale-on-demand (cheaper, delay).

Deliver SRE implementation as:

1. **SLO SPECIFICATION** - SLI definitions, SLO targets, measurement methods, error budget calculation

2. **MONITORING SETUP** - Metrics collection, dashboards (NOC/service/debug), alert rules with burn rates

3. **ALERTING CONFIGURATION** - Severity classification, routing rules, escalation policies, on-call schedule

4. **INCIDENT PROCEDURES** - Classification criteria, response runbooks, communication templates, postmortem process

5. **RELIABILITY PATTERNS** - Timeout/retry/circuit breaker configuration, degradation modes, chaos experiment plan

6. **CAPACITY PLAN** - Utilization analysis, growth forecast, peak planning, DR requirements

---

## Usage Examples

### Example 1: E-commerce Payment Service
**Prompt:** Implement SRE for PaymentService serving 5M transactions/day with 99.99% availability requirement and <100ms p99 latency for checkout flow.

**Expected Output:** SLIs: availability (successful payment API calls / total calls, excluding retries), latency (payment completion time p50/p95/p99), error rate (payment failures / total attempts, categorized by error type). SLOs: 99.99% availability (52 minutes downtime/year), p95 <50ms, p99 <100ms, error rate <0.01%. Error budget: 4.32 minutes/month, burn rate alerts at 2x (warning, ticket), 6x (page primary), 14x (page all). Monitoring: Prometheus with custom payment metrics, Grafana dashboards (payment volume, success rate, latency percentiles, error breakdown by type), PagerDuty with 3-tier escalation (on-call → team lead → engineering manager). Incident classification: SEV1 (all payments failing), SEV2 (>10% failure rate or >200ms p99), SEV3 (single payment provider degraded). Reliability: circuit breaker per payment provider (5 failures → open for 30 seconds), fallback to secondary provider, graceful degradation shows "payment processing" and retries. Runbooks: provider failover, database connection pool exhaustion, rate limiting activation. Postmortem SLA: within 24 hours for any payment outage.

### Example 2: API Platform for B2B SaaS
**Prompt:** Implement SRE for APIPlatform serving 500 enterprise customers with tiered SLAs (99.9% standard, 99.95% premium) and per-tenant rate limiting.

**Expected Output:** SLIs: availability per tenant (requests within rate limit that succeed), latency (p95 response time by endpoint), throughput (requests per second vs contractual limit), error rate (5xx excluding rate limits). SLOs: standard tier 99.9% (8.76 hours/year), premium 99.95% (4.38 hours/year), p95 <200ms all endpoints, p99 <500ms. Error budget: separate tracking per tier, budget dashboard per customer. Monitoring: multi-tenant Prometheus with tenant labels, per-customer SLO dashboards (embedded in customer portal), DataDog for APM tracing. Alerting: tenant-specific alerts for premium customers (direct PagerDuty integration), aggregate alerts for standard tier, burn rate with tenant breakdown. On-call: follow-the-sun rotation (US → EU → APAC), premium customer escalation path to account team. Incident communication: status page per customer tier, direct Slack integration for enterprise customers. Reliability: tenant isolation (separate rate limit buckets, noisy neighbor protection), graceful degradation (429 with retry-after header), queue-based rate limiting for burst tolerance. Capacity: per-tenant capacity allocation, auto-scaling with tenant-aware bin-packing.

### Example 3: Data Pipeline Platform
**Prompt:** Implement SRE for DataPlatform processing 10TB daily with freshness SLO (data available within 1 hour of event time) and 99.9% job success rate.

**Expected Output:** SLIs: freshness (time from event to queryable, measured at destination), completeness (records processed / records expected), job success (successful job runs / total scheduled runs), throughput (GB processed per hour). SLOs: freshness 99% of data within 1 hour, 99.9% within 4 hours, job success rate 99.9%, throughput meets business SLA. Error budget: 43 minutes of >4 hour freshness per month, track by pipeline and data source. Monitoring: custom pipeline metrics (records in/out, processing time, queue depth), Airflow task metrics, data quality checks (row counts, schema validation). Dashboards: pipeline health (DAG status, freshness heatmap), data quality (anomaly detection), capacity (processing rate vs backlog). Alerting: freshness breach approaching (warning at 45 min, critical at 55 min), job failure with retry exhausted, data quality anomaly. Incident response: data pipeline playbooks (upstream delay, schema change, infrastructure failure), data correction procedures, stakeholder communication for delayed reports. Reliability: idempotent processing (safe to retry), checkpoint/restart capability, dead letter queues for failed records, backfill automation. Chaos: simulate upstream delays, inject corrupt records, fail individual pipeline stages.

---

## Cross-References

- [Infrastructure Management](infrastructure-management.md) - Infrastructure operations supporting reliability
- [Cloud Architecture](cloud-architecture.md) - Architectural patterns for high availability
- [CI/CD Pipelines](ci-cd-pipelines.md) - Deployment practices affecting reliability
