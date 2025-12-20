---
category: finance
title: Enterprise Risk Management (ERM) Readiness Assessment
tags:
- enterprise-risk-management
- risk-appetite
- three-lines-of-defense
- risk-culture
- readiness-assessment
use_cases:
- Assessing readiness to implement and operate an ERM program at scale
- Identifying gaps in governance, measurement, controls, and risk reporting
- Producing a prioritized ERM roadmap aligned to regulatory and business objectives
related_templates:
- finance/risk-management-framework.md
- finance/digital-banking-strategy.md
- finance/Investment-Management/investment-portfolio-management.md
industries:
- finance
- government
- technology
type: framework
difficulty: intermediate
slug: enterprise-risk-management-readiness-assessment
---

# Enterprise Risk Management (ERM) Readiness Assessment

## Purpose
Assess readiness to operate enterprise risk management across six dimensions: Governance & Accountability, Risk Appetite & Limits, Risk Identification & Taxonomy, Risk Measurement & Stress Testing, Controls & Assurance, and Reporting & Risk Culture. Identify gaps and produce an actionable ERM plan.

## 🚀 Quick Prompt

> Assess **ERM readiness** for **[INSTITUTION]** operating under **[REGULATORY_REGIME]**. Score 1–5 across: (1) **Governance**—are board/management roles, three-lines-of-defense, and decision rights clear? (2) **Appetite/limits**—is risk appetite translated into measurable limits with escalation and actions? (3) **Identification**—do we have a consistent taxonomy, RCSA process, and top-risk view? (4) **Measurement**—are KRIs, stress tests, and scenario analyses defined and used for decisions? (5) **Controls/assurance**—are controls designed, tested, and tracked with issues management? (6) **Reporting/culture**—are dashboards timely, actionable, and supported by training and accountability? Provide a scorecard, top gaps, and a 12-month roadmap.

**Usage:** Replace bracketed placeholders with your specifics.

---

## Template

Conduct an ERM readiness assessment for {INSTITUTION} under {REGULATORY_REGIME}.

Assess readiness across six dimensions, scoring each 1–5:

**1. GOVERNANCE & ACCOUNTABILITY READINESS**
- Board oversight and committee charters are clear
- Management committees have defined mandates and cadence
- Three lines of defense roles are explicit and enforced
- Decision rights and escalation thresholds are documented
- Risk ownership is assigned for material risks

**2. RISK APPETITE & LIMITS READINESS**
- Appetite statement is specific (not purely qualitative)
- Limits/thresholds are measurable and mapped to risk types
- Breach escalation and management actions are defined
- Capital/liquidity considerations are integrated where relevant
- Exceptions are governed (approvals, logs, time-bound remediation)

**3. RISK IDENTIFICATION & TAXONOMY READINESS**
- Risk taxonomy is consistent across the enterprise
- Risk assessments exist (RCSA, top risks, emerging risks)
- Material processes and critical services are mapped
- Third-party and technology risks are incorporated
- Change management feeds risk identification (new products, systems)

**4. RISK MEASUREMENT & STRESS TESTING READINESS**
- KRIs are defined with owners, thresholds, and data sources
- Loss event capture exists (operational losses, near misses)
- Scenario analysis and stress testing are practiced and reviewed
- Model risk is governed where applicable (validation, drift)
- Aggregation and correlation across risks are considered

**5. CONTROLS, ASSURANCE & ISSUE MANAGEMENT READINESS**
- Key controls are identified and mapped to risks
- Control testing is performed with documented evidence
- Issues are tracked to closure (root cause, owner, due date)
- Internal audit and compliance provide independent challenge
- Policies and procedures are current and usable

**6. REPORTING & RISK CULTURE READINESS**
- Dashboards are timely, accurate, and decision-oriented
- Reporting supports action (clear owners and next steps)
- Training and communication reinforce expected behaviors
- Incentives and accountability align with risk management
- Continuous improvement loop exists (lessons learned, updates)

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** - Overall score, maturity level, top 3 priorities
2. **DIMENSION SCORECARD** - Table with score (X.X/5) and key finding per dimension
3. **TOP RISKS & APPETITE MAP** - Top risks mapped to appetite/limits and owners
4. **GAP ANALYSIS** - Top 5 gaps ranked by impact and urgency, with recommended actions
5. **12-MONTH ROADMAP** - Quarterly actions across governance, measurement, assurance
6. **SUCCESS METRICS** - Limit breaches, issue aging, audit findings, decision turnaround

Use this maturity scale:
- 1.0-1.9: Initial (fragmented practices; limited oversight)
- 2.0-2.9: Developing (basic governance; inconsistent measurement)
- 3.0-3.9: Defined (repeatable ERM cycle with clear ownership)
- 4.0-4.9: Managed (disciplined limits, controls, and reporting)
- 5.0: Optimized (risk is integrated into strategy and operations)

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[INSTITUTION]` | Organization | "Regional Bank" |
| `[REGULATORY_REGIME]` | Applicable regime | "OCC / Federal Reserve" |
| `[RISK_APPETITE]` | Appetite summary | "Moderate; preserve capital" |
| `[TOP_RISKS]` | Top risks list | "Credit, market, cyber" |
| `[KRI_SET]` | KRI set | "5–7 per risk type" |

## Example

**Bank ERM - Readiness**

> Assess ERM readiness for **Regional Bank** operating under **OCC / Federal Reserve**. Governance exists but decision rights and three-lines responsibilities are inconsistently applied; appetite is documented but not translated into measurable limits with actions; taxonomy is mostly consistent but third-party and change-driven risks are not fully integrated; KRI ownership and stress testing cadence need tightening; controls testing and issue remediation are slow; reporting is frequent but not consistently action-oriented. Provide a scorecard and a 12-month roadmap.

