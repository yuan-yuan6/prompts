---
title: Generative AI Implementation Readiness Assessment (Governance)
category: ai-ml-applications
tags:
- ai-governance
- ai-safety
- ai-compliance
- ai-deployment
- readiness-assessment
use_cases:
- Implementing AI safety and risk mitigation, establishing security frameworks, ensuring
  privacy and compliance, managing deployment and change, driving adoption, and governing
  AI systems responsibly
- AI governance and compliance
- Deployment and change management
related_prompts:
- generative-ai-implementation-01-foundation.md
- generative-ai-implementation-02-technical.md
related_templates: []
type: framework
difficulty: intermediate
slug: generative-ai-implementation-03-governance
---

# Generative AI Implementation Readiness Assessment (Governance)

## Purpose
Assess readiness for governance and risk controls needed to deploy generative AI safely, including policies, reviews, and operational accountability.

## Quick Prompt

> Assess GenAI governance readiness for [ORGANIZATION] deploying [USE_CASES]. Score readiness (1–5) across: (1) Risk taxonomy & policy, (2) Data privacy & security, (3) Model/vendor risk, (4) Review & approvals, (5) Monitoring & incident response, (6) Training & accountability. Provide a scorecard and a governance rollout plan.

## Readiness Scorecard (1–5)

### 1) Risk Taxonomy & Policy
- 1 — Initial: No clear policy; risk decisions are inconsistent.
- 3 — Defined: Risk taxonomy and acceptable-use policy documented.
- 5 — Optimized: Policy is enforced and updated; teams understand boundaries.

### 2) Data Privacy & Security
- 1 — Initial: PII handling unclear; access controls weak.
- 3 — Defined: Controls for PII, retention, access, and encryption are defined.
- 5 — Optimized: Controls are audited; incidents are detected and remediated quickly.

### 3) Model/Vendor Risk
- 1 — Initial: Vendor risks unmanaged; contracts lack controls.
- 3 — Defined: Vendor assessment process; contractual and technical safeguards.
- 5 — Optimized: Vendor portfolio is managed; risks are monitored continuously.

### 4) Review & Approvals
- 1 — Initial: No review process; deployments are uncontrolled.
- 3 — Defined: Lightweight review gates and documentation requirements.
- 5 — Optimized: Approvals are fast and consistent; governance scales with usage.

### 5) Monitoring & Incident Response
- 1 — Initial: No monitoring; incidents are reactive.
- 3 — Defined: Monitoring for abuse, drift, and failures; incident playbooks.
- 5 — Optimized: Operational maturity with drills, alerting, and continuous improvements.

### 6) Training & Accountability
- 1 — Initial: Teams lack training; ownership unclear.
- 3 — Defined: Training for builders/users; named owners and responsibilities.
- 5 — Optimized: Accountability is embedded; safe adoption scales across teams.

## Deliverables
- Governance readiness scorecard and gap list
- Policy set (acceptable use, data handling, model use)
- Vendor risk checklist and required controls
- Review/approval workflow and documentation standard
- Monitoring and incident response playbooks

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [ORGANIZATION]: Organization name
- [USE_CASES]: Use cases
- [POLICIES]: Policy set
- [VENDORS]: Vendors
- [RISK_LEVELS]: Risk levels
- [INCIDENT_PLAYBOOKS]: Incident playbooks

## Example (Condensed)
- Use cases: Copilots for HR and support teams
- Scores (1–5): Policy 2; Security 3; Vendor 2; Approvals 2; Monitoring 2; Training 2
- 90-day priorities: Publish policies; define review gates; implement monitoring and incident playbooks; train builders and users

