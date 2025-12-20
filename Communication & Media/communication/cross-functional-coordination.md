---
category: communication
title: Cross-Functional Coordination Readiness Assessment
tags:
- cross-functional
- team-alignment
- dependency-management
- inter-departmental
- readiness-assessment
related_templates:
- communication/meeting-management-framework.md
- communication/crisis-communication-plan.md
use_cases:
- Assessing readiness to coordinate effectively across teams and functions
- Identifying friction in dependencies, handoffs, and alignment
- Improving collaboration, visibility, and delivery velocity
industries:
- finance
- government
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: cross-functional-coordination-readiness-assessment
---

# Cross-Functional Coordination Readiness Assessment

## Purpose
Assess readiness to **coordinate seamlessly across teams, functions, and departments** to deliver complex initiatives on time with minimal friction. Use this to diagnose gaps in alignment, dependency management, and collaboration mechanisms.

## 🚀 Quick Prompt

> Assess **cross-functional coordination readiness** for {COORDINATION_CONTEXT}. The coordination objectives are {OBJECTIVES}. Account for {CONSTRAINTS}. Score 1–5 across the six dimensions below and produce the required output (six deliverables).

---

## Template

Conduct a cross-functional coordination readiness assessment for {COORDINATION_CONTEXT}.

Score each dimension **1–5** (1 = ad hoc, 5 = optimized). Ground findings in observable signals (delivery velocity, escalations, rework, team satisfaction).

**1) DEPENDENCY MAPPING & VISIBILITY**
- Dependencies across teams are identified early and tracked centrally
- Owners, deadlines, and criticality are clear for each dependency
- Shared roadmaps or timelines provide cross-team visibility
- Dependency conflicts are surfaced and resolved proactively

**2) ROLES, ACCOUNTABILITY & DECISION RIGHTS**
- RACI or equivalent exists for key deliverables and decisions
- Handoffs between teams have clear criteria and ownership
- Liaison or coordination roles are designated per team
- Decision-making authority is clear and escalation paths exist

**3) COMMUNICATION & SYNC CADENCE**
- Regular cross-team syncs exist with clear agendas and timeboxes
- Communication channels are established and consistently used
- Status updates are proactive and structured (blockers, risks, changes)
- Meeting hygiene is strong (attendance, prep, follow-up)

**4) SHARED TOOLS & ARTIFACTS**
- Shared trackers or dashboards show status, blockers, and priorities
- Documentation is centralized and accessible across teams
- Version control and handoff artifacts reduce ambiguity
- Tools enable asynchronous collaboration across time zones

**5) CONFLICT RESOLUTION & ESCALATION**
- Conflicts are surfaced early and addressed constructively
- Escalation process exists with defined thresholds and owners
- Trade-offs are negotiated transparently based on business priorities
- Retrospectives identify friction points and drive improvement

**6) TRUST, CULTURE & COLLABORATION**
- Teams understand each other's constraints and priorities
- Collaboration is default; siloed behavior is addressed
- Wins and contributions are recognized across functions
- Psychological safety enables raising issues without blame

---

## Required Output Format (6 Deliverables)

1) **EXECUTIVE SUMMARY**
- Overall maturity level, biggest coordination friction, and key improvement priorities

2) **DIMENSION SCORECARD**
- Table with score (1–5) + 1–2 findings per dimension

3) **DEPENDENCY MAP**
- Visual or table showing team-to-team dependencies (who needs what, by when, status)
- Highlight critical path and at-risk dependencies

4) **RACI MATRIX**
- For top 5 cross-functional deliverables: who is Responsible, Accountable, Consulted, Informed

5) **FRICTION LOG**
- Recent blockers, escalations, and delays (root causes and owners)
- Patterns: handoff failures, decision bottlenecks, communication gaps

6) **30/60/90-DAY COORDINATION PLAN**
- Actions to improve dependency visibility, decision clarity, and sync discipline
- Metrics (delivery velocity, escalation rate, rework %, team satisfaction)

---

## Maturity Scale (Use for Overall + Per-Dimension Scoring)
- 1.0–1.9: Initial (reactive, siloed, high friction, frequent delays)
- 2.0–2.9: Developing (basic coordination, gaps in visibility and accountability)
- 3.0–3.9: Defined (repeatable process, solid communication, scaling challenges)
- 4.0–4.9: Managed (proactive, high trust, minimal friction, continuous improvement)
- 5.0: Optimized (seamless, anticipates needs, high velocity, low escalations)

---

## Variables (≤3)
- {COORDINATION_CONTEXT}: Teams involved, initiative scope, timeline, current tools/practices
- {OBJECTIVES}: Delivery velocity, quality, team satisfaction, and escalation reduction goals
- {CONSTRAINTS}: Org structure, geography, tools, cultural dynamics, resourcing

---

## Example (Filled)

**Input**
- {COORDINATION_CONTEXT}: New product launch involving Eng (20), Product (5), Design (4), Marketing (6), Sales (12). 6-month timeline. Tools: Jira, Slack, Google Docs. Weekly all-hands; no dependency tracker.
- {OBJECTIVES}: Launch on time with zero critical bugs, reduce escalations by 50%, improve team satisfaction from 6.5 to 8/10.
- {CONSTRAINTS}: Teams in 3 time zones; Engineering prioritizes bug fixes over features; Marketing needs assets 4 weeks before launch.

**1) EXECUTIVE SUMMARY**
- Overall maturity: 2.6 (Developing)
- Biggest friction: late handoffs from Design to Eng (3 delays), unclear decision rights on scope changes, Marketing surprised by feature cuts
- Fix first: implement shared dependency tracker, clarify RACI for scope decisions, establish Design-Eng sync

**2) DIMENSION SCORECARD**
- Dependency Mapping & Visibility: 2/5 — dependencies tracked in silos; no shared view
- Roles & Accountability: 2/5 — RACI informal; handoff criteria unclear
- Communication & Sync: 3/5 — weekly all-hands exists; ad hoc syncs reactive
- Shared Tools: 2/5 — Jira used inconsistently; docs scattered
- Conflict Resolution: 3/5 — conflicts escalate to VP; no clear process
- Trust & Culture: 3/5 — good intent but blame surfaces during delays

**3) DEPENDENCY MAP**
- Design → Eng: UI specs (due Week 8, status: 2 weeks late, blocker: Design bandwidth)
- Eng → Marketing: Beta build (due Week 16, status: on track)
- Product → Sales: Feature brief (due Week 12, status: pending scope decision)
- Marketing → Sales: Launch materials (due Week 22, status: at risk if Design delays)
- Critical path: Design delays impact Eng timeline, which risks Marketing asset delivery

**4) RACI MATRIX (Top 5 Deliverables)**
- Scope decision: Product (A), Eng/Design/Marketing (C), Sales (I)
- UI specs: Design (R), Eng (A), Product (C), Marketing (I)
- Beta build: Eng (R/A), Product (C), Marketing (I)
- Launch materials: Marketing (R/A), Product/Sales (C)
- Sales enablement: Sales (R), Product (A), Marketing (C)

**5) FRICTION LOG**
- Week 6: Design specs late (cause: underestimated scope, no buffer); escalated to VP
- Week 10: Eng cut 2 features (cause: velocity miss); Marketing learned via Slack; materials rework needed
- Week 14: Sales surprised by pricing model change (cause: not included in RACI); customer calls awkward
- Patterns: late handoffs (2x), communication gaps (3x), unclear decision rights (2x)

**6) 30/60/90-DAY COORDINATION PLAN**
- 30 days: deploy shared dependency tracker in Jira; clarify RACI for scope/feature decisions; establish Design-Eng biweekly sync
- 60 days: standardize handoff checklist (e.g., Design → Eng requires specs + Figma + review); run retrospective on friction log themes
- 90 days: reduce escalations by 50%; track delivery velocity (story points/sprint); improve team satisfaction to 8/10 via pulse survey
- Metrics: on-time handoffs (goal 95%), escalations (goal <5/month), team satisfaction (goal 8/10)

---

## Best Practices (Exactly 8)
1) Map dependencies early in planning; track them centrally with owners and deadlines.
2) Define RACI for every key deliverable and decision; make it visible to all teams.
3) Establish regular cross-team syncs focused on blockers, handoffs, and changes—not status.
4) Use shared tools and dashboards so every team sees the same truth in real time.
5) Create clear handoff criteria (definition of done) to prevent rework and ambiguity.
6) Escalate early based on objective triggers (deadline risk, blocker unresolved >3 days).
7) Run retrospectives after major milestones to identify and fix coordination friction.
8) Build trust by celebrating cross-team wins and addressing blame culture directly.
