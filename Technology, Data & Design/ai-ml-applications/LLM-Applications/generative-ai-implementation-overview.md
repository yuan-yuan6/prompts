---
title: Generative AI Implementation Readiness Assessment (Overview)
category: ai-ml-applications
tags:
- generative-ai
- llm-implementation
- ai-strategy
- enterprise-ai
- readiness-assessment
use_cases:
- Creating comprehensive generative AI implementation strategies covering large language
  models, diffusion models, prompting techniques, fine-tuning approaches, retrieval-augmented
  generation, AI agents, and ethical considerations
industries:
- government
- healthcare
- manufacturing
- technology
type: framework
difficulty: intermediate
slug: generative-ai-implementation-overview
---

# Generative AI Implementation Readiness Assessment (Overview)

## Purpose
Assess readiness to implement generative AI across an organization, covering strategy, technology, governance, and operational adoption.

## Quick Prompt

> Assess GenAI implementation readiness for [ORGANIZATION] targeting [USE_CASES]. Score readiness (1–5) across: (1) Use case & value, (2) Data & knowledge, (3) Model & prompt strategy, (4) Engineering & reliability, (5) Security/privacy/governance, (6) Adoption & operations. Provide a scorecard, top risks, and a 90-day implementation roadmap.

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
- Readiness scorecard and risk register
- Prioritized GenAI use case portfolio with success metrics
- Target architecture and integration approach
- Governance and security controls checklist
- 90-day implementation roadmap (pilots → production)

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [ORGANIZATION]: Organization name
- [USE_CASES]: Target use cases
- [DATA_SOURCES]: Knowledge bases and datasets
- [MODEL_PROVIDER]: Model provider(s)
- [RISK_TOLERANCE]: Risk tolerance level
- [ADOPTION_METRICS]: Adoption metrics

## Example (Condensed)
- Use cases: Customer support copilot + internal knowledge assistant
- Scores (1–5): Value 3; Data 2; Model 3; Engineering 2; Governance 2; Adoption 2
- 90-day priorities: Build evaluation harness; implement retrieval with access controls; define governance and rollout plan

