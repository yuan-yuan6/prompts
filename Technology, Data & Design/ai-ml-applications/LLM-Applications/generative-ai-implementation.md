---
title: Generative AI Implementation Readiness Assessment
category: ai-ml-applications
tags:
- generative-ai
- llm
- rag
- ai-implementation
- readiness-assessment
use_cases:
- Creating generative AI implementation strategies for enterprise deployment
- Selecting and customizing foundation models (LLMs, diffusion models)
- Building RAG systems, AI agents, and multimodal applications
- Establishing responsible AI governance and safety controls
related_templates:
- ai-ml-applications/LLM-Applications/generative-ai-implementation-01-foundation.md
- ai-ml-applications/LLM-Applications/generative-ai-implementation-02-technical.md
- ai-ml-applications/LLM-Applications/generative-ai-implementation-03-governance.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: generative-ai-implementation
---

# Generative AI Implementation Readiness Assessment

## Purpose
Assess readiness to implement a generative AI solution from pilot to production, including evaluation, architecture, governance, and rollout.

## Quick Prompt

> Assess readiness to implement a GenAI solution for [USE_CASE]. Score readiness (1–5) across: (1) Use case & requirements, (2) Data & context, (3) Model/prompt strategy & evaluation, (4) Engineering & reliability, (5) Safety/security/governance, (6) Rollout & operations. Provide a scorecard, gaps, and a 60–90 day execution plan.

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
- Implementation readiness scorecard and prioritized gaps
- Evaluation plan (offline + online) and baseline metrics
- Architecture diagram and integration plan
- Safety/security controls and governance checklist
- Rollout plan with ownership and success metrics

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [USE_CASE]: Target use case
- [USERS]: Target users
- [DATA_SOURCES]: Data/knowledge sources
- [QUALITY_METRICS]: Quality metrics
- [LATENCY_TARGET]: Latency target
- [COST_TARGET]: Cost target

## Example (Condensed)
- Use case: Internal IT helpdesk assistant
- Scores (1–5): Requirements 3; Data 2; Evaluation 2; Engineering 3; Governance 2; Operations 2
- 90-day priorities: Define evaluation set; implement retrieval with permissions; add monitoring and incident playbook

