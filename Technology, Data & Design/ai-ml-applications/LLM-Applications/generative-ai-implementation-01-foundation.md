---
title: Generative AI Implementation Readiness Assessment (Foundation)
category: ai-ml-applications
tags:
- generative-ai
- foundation-models
- ai-use-cases
- llm-selection
- readiness-assessment
use_cases:
- Defining generative AI strategy, identifying business value and use cases, selecting
  foundation models, establishing technical infrastructure, and implementing governance
  fundamentals
- AI strategy development
- Use case identification
related_prompts:
- generative-ai-implementation-02-technical.md
- generative-ai-implementation-03-governance.md
- cloud-architecture-framework.md
related_templates: []
type: framework
difficulty: intermediate
slug: generative-ai-implementation-01-foundation
---

# Generative AI Implementation Readiness Assessment (Foundation)

## Purpose
Assess readiness for the foundational capabilities required to deliver generative AI safely and reliably, including scope, data access, evaluation, and operating model.

## Quick Prompt

> Assess GenAI foundation readiness for [ORGANIZATION] targeting [USE_CASE]. Score readiness (1–5) across: (1) Use case & constraints, (2) Data access & permissions, (3) Evaluation baseline, (4) Architecture foundation, (5) Governance & risk, (6) Operating model. Provide a scorecard and a 90-day foundation plan.

## Readiness Scorecard (1–5)

### 1) Use Case & Value
- 1 — Initial: Use case is exploratory; value not quantified.
- 3 — Defined: Use case prioritized with success metrics and scope.
- 5 — Optimized: Use cases are portfolio-managed with measured ROI and outcomes.

### 2) Data & Knowledge
- 1 — Initial: Data/knowledge sources unclear; access is manual.
- 3 — Defined: Sources identified; access patterns and data quality expectations set.
- 5 — Optimized: Data is governed, versioned, and monitored for quality and freshness.

### 3) Model & Prompt Strategy
- 1 — Initial: Model choice and prompts are ad-hoc; no evaluation.
- 3 — Defined: Model/prompt approach documented; baseline evaluation exists.
- 5 — Optimized: Approach is optimized with systematic evaluation and iteration.

### 4) Engineering & Reliability
- 1 — Initial: Prototype-only; limited testing/observability.
- 3 — Defined: Service architecture defined; testing, monitoring, and fallbacks exist.
- 5 — Optimized: Production-grade reliability with SLOs, load testing, and incident response.

### 5) Security, Privacy & Governance
- 1 — Initial: Risks unmanaged; policies unclear.
- 3 — Defined: Risk controls defined (PII, retention, access); review process exists.
- 5 — Optimized: Controls are audited; governance supports safe scaling.

### 6) Adoption & Operations
- 1 — Initial: No rollout plan; limited user feedback loop.
- 3 — Defined: Rollout and training plan; feedback captured; operational ownership set.
- 5 — Optimized: Adoption is measured; operations improve continuously; scaling is repeatable.

## Deliverables
- Foundation readiness scorecard and gap list
- Use case scope and constraints document
- Data access/permissions plan and source inventory
- Evaluation baseline and test set outline
- Operating model (owners, SLAs, support)

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [ORGANIZATION]: Organization name
- [USE_CASE]: Target use case
- [DATA_ACCESS]: Access constraints
- [EVALUATION_SET]: Evaluation set definition
- [OWNERS]: Responsible owners
- [RISK_CONTROLS]: Risk controls

## Example (Condensed)
- Use case: Policy Q&A assistant with restricted documents
- Scores (1–5): Scope 3; Data 2; Evaluation 1; Engineering 2; Governance 2; Ops 2
- 90-day priorities: Build evaluation set; implement permissions-aware retrieval; define governance and operational ownership

