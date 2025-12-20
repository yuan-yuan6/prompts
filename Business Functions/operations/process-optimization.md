---
category: operations
title: Process Optimization Readiness Assessment
tags:
- process-improvement
- value-stream-mapping
- bottleneck-analysis
- workflow-efficiency
- readiness-assessment
use_cases:
- Assessing readiness to optimize a specific end-to-end process (cycle time, cost, quality, customer experience)
- Identifying the biggest constraints and waste drivers before investing in automation or org redesign
- Creating a practical 90-day optimization roadmap with measurable targets and owners
related_templates:
- operations/lean-six-sigma-implementation.md
- operations/process-automation-framework.md
- operations/operations-resource-management.md
- strategy/okr-implementation-framework.md
industries:
- education
- finance
- government
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: process-optimization-readiness-assessment
---

# Process Optimization Readiness Assessment

## Purpose
Assess an organization's readiness to improve an end-to-end process across six dimensions: Process Visibility, Diagnosis, Standard Work & Controls, Data & Systems Enablement, People & Change, and Governance & Continuous Improvement. Identify gaps, prioritize interventions, and produce a roadmap tied to measurable outcomes.

## Template

Conduct a comprehensive process optimization readiness assessment for {ORGANIZATION}, a {INDUSTRY} organization seeking to improve {TARGET_PROCESS}.

Assess readiness across six dimensions, scoring each 1–5:

**1. PROCESS VISIBILITY & BASELINE READINESS**
- Clear scope boundaries (start/end, in-scope variants, upstream/downstream dependencies)
- Process map accuracy (happy path + key variants + exception paths)
- Baseline metrics availability (volume, cycle time, touch time, wait time, rework rate)
- Data definitions (what counts as “complete,” “defect,” “handoff,” “queue,” “SLA breach”)
- Measurement reliability (timestamps exist, sampling method, data freshness)
- Customer/stakeholder definition of value (what matters: speed, accuracy, compliance, experience)

**2. DIAGNOSIS & ROOT CAUSE READINESS**
- Ability to identify the constraint (Theory of Constraints) vs “local busywork”
- Waste identification (waiting, handoffs, rework, overprocessing, motion/transport)
- Root cause practice (5 Whys, Pareto, fishbone) applied to verified data
- Exception analysis (top drivers of variability, error categories, escalation patterns)
- Demand vs capacity understanding (arrival patterns, seasonality, peak handling)
- Benchmarking (internal best cells/teams; external where relevant)

**3. STANDARD WORK & CONTROLS READINESS**
- Standard work definition (steps, inputs, outputs, role clarity, service levels)
- Handoff quality (clear entry/exit criteria; reduced back-and-forth)
- Controls embedded (validation checks, error-proofing, approvals where risk-justified)
- Exception handling design (decision rules, routing, human-in-the-loop)
- Documentation + training readiness (job aids, SOP ownership, onboarding)
- Sustainment mechanisms (audits, control charts, escalation when metrics drift)

**4. DATA, SYSTEMS & AUTOMATION ENABLEMENT**
- Systems fit (workflow tools, case management, ERP/CRM, ticketing) and integration points
- Data capture and traceability (end-to-end timestamps, status codes, reason codes)
- Reporting/BI readiness (dashboards, drill-down, segmenting by variant/customer/channel)
- Automation feasibility (stable steps, clear rules, accessible systems, exception strategy)
- Security/compliance controls for tooling changes (audit trail, access, approvals)
- Tech delivery capability (release process, testing, rollback for process/tool changes)

**5. PEOPLE, CHANGE & CAPABILITY READINESS**
- Named process owner with authority (and time) to drive change
- SME availability and cross-functional involvement (ops, IT, compliance, customer)
- Change readiness (front-line engagement, psychological safety, feedback channels)
- Skills (process mapping, data analysis, facilitation, problem solving)
- Capacity planning (backfill, WIP limits, dedicated improvement time)
- Incentives aligned to outcomes (not just utilization or local metrics)

**6. GOVERNANCE & CONTINUOUS IMPROVEMENT READINESS**
- Decision rights and escalation paths (what can be changed, by whom, and how fast)
- KPI ownership and cadence (daily/weekly management, review rhythm)
- Portfolio management (pipeline of improvements; sequencing; dependency management)
- Benefits tracking (baseline vs realized; guardrails for quality/risk)
- Cross-team alignment (shared definitions, shared constraints, shared priorities)
- Learning system (retrospectives, playbooks, standard patterns captured)

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** - Overall score, maturity level, top 3 priorities, expected impact range

2. **DIMENSION SCORECARD** - Table with score (X.X/5) and key finding per dimension

3. **BASELINE & PROCESS MAP** - Scope, current-state map (incl. exceptions), baseline metrics (touch vs wait time)

4. **GAP ANALYSIS** - Top 5 gaps ranked by impact and urgency, with recommended actions

5. **90-DAY ROADMAP** - Sequenced actions (quick wins + enablement) with owners and checkpoints

6. **SUCCESS METRICS** - Baseline vs 30/60/90-day targets (cycle time, rework, SLA, cost-to-serve, CSAT)

Use this maturity scale:
- 1.0-1.9: Initial (ad-hoc, inconsistent, limited measurement)
- 2.0-2.9: Developing (basic mapping/metrics, isolated improvements)
- 3.0-3.9: Defined (standard methods, repeatable improvements, managed KPIs)
- 4.0-4.9: Managed (data-driven, integrated tooling, sustained control)
- 5.0: Optimized (continuous improvement system, predictive, resilient)

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ORGANIZATION]` | Name of the organization | "MetroCare Health" |
| `[TARGET_PROCESS]` | End-to-end process in scope | "Claims intake to adjudication" |
| `[OPTIMIZATION_GOALS]` | Desired outcomes and constraints | "-30% cycle time, -50% rework, maintain compliance controls" |

## Example

**Healthcare - Claims Intake and Adjudication**

> Assess process optimization readiness for **MetroCare Health** improving **claims intake to adjudication** to achieve **-30% cycle time, -50% rework, maintain compliance controls**. (1) Process visibility—maps exist but not validated; baseline shows 2.1 days touch time vs 18.4 days wait time; exception paths are undocumented. (2) Diagnosis—teams focus on utilization; constraint is downstream clinical review capacity with high variability; top waste is rework from missing documentation. (3) Standard work—handoff criteria differ by team; no consistent reason codes; quality checks occur late. (4) Data & systems—case system lacks consistent status codes; timestamps missing for key transitions; automation of intake is feasible if reason codes are standardized. (5) People & change—process owner exists but no dedicated CI time; SMEs available 2 hrs/week; frontline wants fewer handoffs. (6) Governance—weekly ops review exists but no KPI owners for rework/SLA. Provide scorecard, top gaps, and a 90-day roadmap focusing on standard work, constraint relief, and measurement instrumentation.

