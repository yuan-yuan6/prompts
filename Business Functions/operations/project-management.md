---
category: operations
title: Project Management Readiness Assessment
tags:
- project-planning
- milestone-tracking
- resource-coordination
- deliverable-management
- readiness-assessment
use_cases:
- Assessing readiness to deliver a complex initiative on time and on budget with clear governance
- Diagnosing delivery gaps (scope, estimation, dependencies, risk, change control, reporting)
- Creating a practical delivery roadmap and operating cadence for execution
related_templates:
- operations/operations-resource-management.md
- strategy/okr-implementation-framework.md
- strategy/digital-transformation-roadmap.md
- operations/dashboard-design-deployment.md
industries:
- finance
- government
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: project-management-readiness-assessment
---

# Project Management Readiness Assessment

## Purpose
Assess an organization's readiness to plan, govern, and execute projects effectively across six dimensions: Outcomes & Scope, Planning & Estimation, Governance & Decision Rights, Delivery Operating Model, Risk/Dependency & Change Control, and Reporting & Benefits Realization. Identify gaps, prioritize fixes, and build a delivery plan with measurable targets.

## 🚀 Quick Prompt

> Assess **project management readiness** for **[ORGANIZATION]** delivering **[INITIATIVE]** using **[DELIVERY_MODEL]**. Evaluate across: (1) **Outcomes & scope**—are goals, success metrics, and boundaries clear (and agreed)? (2) **Planning & estimation**—is the plan credible (schedule, budget, milestones, resourcing) and based on evidence? (3) **Governance**—are decision rights, approvals, and escalation paths clear and fast enough? (4) **Delivery operating model**—do teams have a workable cadence (agile/waterfall/hybrid), roles, and tooling to execute? (5) **Risk, dependencies & change control**—are risks owned, dependencies actively managed, and changes controlled without stalling progress? (6) **Reporting & benefits**—is status accurate, leading indicators tracked, and benefits measured post-delivery? Provide a 1–5 maturity scorecard, gap analysis, prioritized recommendations, and a 12-week stabilization roadmap.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid project delivery readiness evaluation.

---

## Template

Conduct a comprehensive project management readiness assessment for {ORGANIZATION}, a {INDUSTRY} organization planning to deliver {INITIATIVE}.

Assess readiness across six dimensions, scoring each 1–5:

**1. OUTCOMES & SCOPE READINESS**
- Clear problem statement, desired outcomes, and measurable success criteria
- Defined scope boundaries (in/out), assumptions, constraints, and acceptance criteria
- Stakeholder alignment (what “done” means; tradeoffs and priorities)
- Requirements clarity appropriate to the delivery model (epics/stories vs specs)
- Benefit hypothesis (how value is realized; who owns adoption)
- Non-functional requirements and guardrails (security, privacy, compliance, reliability)

**2. PLANNING & ESTIMATION READINESS**
- Work decomposition (WBS/backlog) with ownership and realistic sequencing
- Evidence-based estimates (historical velocity, benchmarks, reference classes)
- Resource plan (roles, availability, constraints, backfill, vendor capacity)
- Schedule quality (critical path, milestones, dependency mapping)
- Budget plan (run vs change, contingency, procurement lead times)
- Baseline and change management (what’s tracked vs what’s flexible)

**3. GOVERNANCE & DECISION RIGHTS READINESS**
- Clear decision rights (RACI/DACI) and fast escalation for blockers
- Steering cadence (frequency, agenda, decision log) matched to risk
- Approval gates that protect risk without becoming bottlenecks
- Vendor/partner governance (SLAs, deliverables, acceptance, change orders)
- Compliance and audit involvement integrated early (not end-loaded)
- Single accountable owner (sponsor) and empowered PM/Delivery Lead

**4. DELIVERY OPERATING MODEL READINESS**
- Delivery model fit (agile, waterfall, hybrid) for the work type and constraints
- Defined roles (PM, Product Owner, Tech Lead, QA, Ops/Support) and handoffs
- Working agreements (Definition of Ready/Done, branching/release strategy if software)
- Quality practices (test strategy, reviews, acceptance testing, sign-off)
- Collaboration tooling (tracking, docs, comms) with disciplined usage
- Team health and capacity practices (WIP limits, focus time, dependency buffers)

**5. RISK, DEPENDENCY & CHANGE CONTROL READINESS**
- Risk register with owners, mitigations, triggers, and review cadence
- Dependency mapping (internal/external) with accountable owners and dates
- Change control mechanism proportional to risk (lightweight CRs, impact assessment)
- Issue management flow (triage, priority, SLA, escalation)
- Cutover readiness (go-live criteria, rollback plan, runbooks)
- Stakeholder change management (training, comms, adoption measurement)

**6. REPORTING & BENEFITS REALIZATION READINESS**
- Accurate status reporting (progress vs plan; what changed; what’s at risk)
- Leading indicators (burn-up, throughput, milestone readiness, defect trends)
- Decision-quality dashboards (simple, consistent, role-based)
- Benefits tracking plan (baseline vs realized; post-launch measurement)
- Operational handover readiness (support model, SLAs, ownership)
- Lessons learned loop (retrospectives; playbooks; reusable standards)

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** - Overall score, maturity level, top 3 priorities, main delivery risks

2. **DIMENSION SCORECARD** - Table with score (X.X/5) and key finding per dimension

3. **INITIATIVE READINESS** - Readiness by workstream (✓/△/✗) and top dependency risks

4. **GAP ANALYSIS** - Top 5 gaps ranked by impact and urgency, with recommended actions

5. **12-WEEK STABILIZATION ROADMAP** - Weeks 1–4 / 5–8 / 9–12 actions across planning, governance, delivery, and reporting

6. **SUCCESS METRICS** - Baseline vs 6-week and 12-week targets (on-time delivery %, forecast accuracy, change fail %, stakeholder CSAT)

Use this maturity scale:
- 1.0-1.9: Initial (ad-hoc planning, unclear ownership, reactive delivery)
- 2.0-2.9: Developing (basic plans, inconsistent governance, frequent surprises)
- 3.0-3.9: Defined (repeatable methods, clear roles, managed risks)
- 4.0-4.9: Managed (predictable execution, strong controls, continuous optimization)
- 5.0: Optimized (high-velocity, high-quality delivery system with learning loops)

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ORGANIZATION]` | Name of the organization | "Apex Manufacturing" |
| `[INITIATIVE]` | Initiative/project being delivered | "ERP migration + warehouse scanning rollout" |
| `[DELIVERY_MODEL]` | Delivery approach | "Hybrid (waterfall milestones + agile sprints)" |

## Example

**Manufacturing - ERP Migration and Warehouse Rollout**

> Assess project management readiness for **Apex Manufacturing** delivering **ERP migration + warehouse scanning rollout** using **Hybrid (waterfall milestones + agile sprints)**. (1) Outcomes & scope—objectives are clear but acceptance criteria for warehouse workflows are ambiguous; non-functional requirements for uptime and cutover are not agreed. (2) Planning—schedule exists but critical path and procurement lead times are missing; resourcing assumes 80% availability for SMEs who are at capacity. (3) Governance—steering committee exists but decision rights are unclear; vendor change orders are handled ad-hoc. (4) Delivery model—teams run sprints but backlog is not prioritized against milestones; testing is late-stage. (5) Risk/deps—top risks (data quality, cutover downtime, training) are known but not owned with triggers; dependencies on IT infra upgrades are not tracked. (6) Reporting—status is “green” but leading indicators (defects, readiness) show rising risk; benefits tracking is undefined. Provide scorecard, top gaps, and a 12-week stabilization roadmap.

