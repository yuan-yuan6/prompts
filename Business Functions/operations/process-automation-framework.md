---
category: operations
title: Process Automation Readiness Assessment
tags:
- process-automation
- rpa
- workflow-automation
- bpm
- readiness-assessment
use_cases:
- Assessing readiness to automate manual workflows using RPA, workflow/BPM, integrations, and AI-assisted automation
- Prioritizing automation opportunities by impact, feasibility, and risk
- Creating a roadmap for an automation CoE, platform rollout, and measurable benefit realization
related_templates:
- strategy/digital-transformation-roadmap.md
- operations/lean-six-sigma-implementation.md
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
slug: process-automation-readiness-assessment
---

# Process Automation Readiness Assessment

## Purpose
Assess an organization's readiness to successfully deliver, operate, and scale process automation across six dimensions: Process Discovery & Prioritization, Data & Integration, Platform & Architecture, Delivery Operating Model, Governance & Risk, and Adoption & Operations. Identify gaps, prioritize investments, and build a 12-month roadmap.

## 🚀 Quick Prompt

> Assess **process automation readiness** for **[ORGANIZATION]** targeting **[PROCESS_SCOPE]** to achieve **[AUTOMATION_TARGET]**. Evaluate across: (1) **Process discovery**—do you have a repeatable way to identify and size automation opportunities? (2) **Data & integration**—are inputs structured, systems accessible (APIs/EDI), and exception paths understood? (3) **Platform & architecture**—what automation tools exist (RPA/workflow/iPaaS/AI) and how are they secured and governed? (4) **Delivery model**—do you have product ownership, standards, testing, and release management for automations? (5) **Governance & risk**—how do you handle controls, auditability, privacy, and change approvals? (6) **Adoption & operations**—monitoring, incident response, bot runbooks, and continuous improvement. Provide a maturity scorecard (1-5), gap analysis, prioritized recommendations, and a 12-month rollout plan.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid automation readiness evaluation.

---

## Template

Conduct a comprehensive process automation readiness assessment for {ORGANIZATION}, a {INDUSTRY} organization planning to automate {PROCESS_SCOPE}.

Assess readiness across six dimensions, scoring each 1-5:

**1. PROCESS DISCOVERY & PRIORITIZATION**
- Intake process for automation candidates (funnel, triage, backlog)
- Opportunity sizing (volume, time saved, error reduction, compliance impact)
- Process documentation quality (as-is maps, decision rules, exceptions)
- Standard criteria for feasibility (stability, rule-based steps, data availability)
- Prioritization method (impact/effort/risk, dependency-aware sequencing)
- Ownership model (process owner accountability and sign-off)

**2. DATA & INTEGRATION READINESS**
- Data inputs quality and availability (structured vs unstructured)
- System accessibility (APIs, iPaaS, database access, UI-only constraints)
- Exception handling paths and human-in-the-loop workflows
- Identity and access model for automations (least privilege, secrets handling)
- Logging/audit trails for transactions and decisions
- Environment parity (dev/test/prod), test data availability

**3. PLATFORM & ARCHITECTURE READINESS**
- Tooling fit: workflow/BPM vs RPA vs integration vs AI-assisted automation
- Reference architecture (orchestration, queues, retries, idempotency)
- Security posture (segregation of duties, key management, network controls)
- Scalability model (bot runners, concurrency, scheduling)
- Reuse standards (components, connectors, templates)
- Vendor management and licensing strategy

**4. DELIVERY OPERATING MODEL**
- Team structure (CoE, federated, product teams) and responsibilities
- Development standards (coding practices, naming, documentation)
- Testing strategy (unit/integration/UAT, regression suites)
- Release management (CI/CD, approvals, versioning)
- Performance engineering (throughput, latency, stability)
- Benefit realization tracking (baseline, expected vs realized)

**5. GOVERNANCE, RISK & CONTROLS**
- Risk assessment process (data sensitivity, controls, operational risk)
- Compliance requirements (audit, privacy, retention, industry regulation)
- Change control and approvals (CAB/controls sign-off)
- Model for managing exceptions, overrides, and escalations
- Third-party/vendor risk management for automation tools
- Documentation standards for auditability and continuity

**6. ADOPTION & OPERATIONS**
- Monitoring and alerting (SLAs, failures, queue depth, business KPIs)
- Incident response and runbooks (on-call, rollback, manual fallback)
- Bot lifecycle management (maintenance windows, credential rotation)
- User training and communication for process changes
- Continuous improvement loop (postmortems, backlog grooming)
- Governance cadence for reviewing performance and expanding scope

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** - Overall score, maturity level, top 3 priorities, investment range and timeline

2. **DIMENSION SCORECARD** - Table with score (X.X/5) and key finding per dimension

3. **AUTOMATION PORTFOLIO** - Candidate list with impact, feasibility, risk (✓/△/✗), and recommended sequencing

4. **GAP ANALYSIS** - Top 5 gaps blocking scale, with specific remediation actions

5. **ROADMAP** - Quarterly plan covering platform rollout, governance/CoE, pilot automations, and scale-out

6. **SUCCESS METRICS** - Baseline vs 6-month and 12-month targets for: hours saved, error reduction, cycle time, automation uptime, incident rate, audit findings

Use this maturity scale:
- 1.0-1.9: Initial (ad-hoc scripts, limited standards, fragile automations)
- 2.0-2.9: Developing (pilot automations, basic governance, inconsistent quality)
- 3.0-3.9: Defined (standard delivery, clear ownership, repeatable tooling)
- 4.0-4.9: Managed (scaled platform, measurable benefits, strong controls)
- 5.0: Optimized (automation as a product, continuous improvement, high reliability)

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ORGANIZATION]` | Name of the organization | "Regional BankCo" |
| `[PROCESS_SCOPE]` | Target workflows and domains | "KYC onboarding, accounts payable, claims intake" |
| `[AUTOMATION_TARGET]` | Desired outcome/target | "40% reduction in cycle time and 60% fewer manual touches" |

## Example

**Financial Services - Back Office Automation Rollout**

> Assess process automation readiness for **Regional BankCo** targeting **KYC onboarding, accounts payable, claims intake** to achieve **40% reduction in cycle time and 60% fewer manual touches**. (1) Process discovery—opportunities identified informally, limited baseline time studies, exceptions not mapped. (2) Data & integration—core systems have partial APIs; many steps are UI-only; identity and credential handling is inconsistent. (3) Platform—RPA exists but no orchestration standards; workflow approvals are email-based; limited environment separation. (4) Delivery—no CI/CD; testing is manual; releases are risky and infrequent. (5) Governance—compliance reviews are late-stage; audit trails are incomplete; change approvals unclear. (6) Operations—monitoring is reactive; no runbooks or manual fallback procedures. Provide scorecard, gap analysis, a pilot plan for 3 automations, and a 12-month roadmap to a governed platform with 99.5% automation uptime.

