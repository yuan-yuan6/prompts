---
title: Generative AI Implementation Readiness Assessment (Technical)
category: ai-ml-applications
tags:
- llm-architecture
- rag
- prompt-engineering
- multi-agent
- readiness-assessment
use_cases:
- Implementing large language models, developing prompt engineering frameworks, building
  retrieval-augmented generation systems, creating multi-agent platforms, and deploying
  multimodal AI capabilities
- LLM implementation
- Technical architecture
related_prompts:
- generative-ai-implementation-01-foundation.md
- generative-ai-implementation-03-governance.md
related_templates: []
type: framework
difficulty: intermediate
slug: generative-ai-implementation-02-technical
---

# Generative AI Implementation Readiness Assessment (Technical)

## Purpose
Assess readiness for the technical implementation of generative AI, including architecture, integrations, evaluation, reliability, and cost/latency controls.

## Quick Assessment Prompt

> Assess GenAI technical readiness for [USE_CASE] with target latency [LATENCY_TARGET] and monthly budget [BUDGET]. Score readiness (1–5) across: (1) Architecture & integration, (2) Data & retrieval, (3) Evaluation & testing, (4) Observability & reliability, (5) Cost & performance, (6) Release & operations. Provide a scorecard and a technical execution plan.

## Readiness Scorecard (1–5)

### 1) Architecture & Integration
- 1 — Initial: Prototype code; integrations are manual or brittle.
- 3 — Defined: Service boundaries and integrations defined; environments exist.
- 5 — Optimized: Architecture is scalable and maintainable; integrations are resilient.

### 2) Data & Retrieval
- 1 — Initial: Retrieval is absent or low quality; access rules ignored.
- 3 — Defined: Retrieval pipeline exists; relevance and access controls implemented.
- 5 — Optimized: Retrieval quality is monitored; indexing and permissions are robust.

### 3) Evaluation & Testing
- 1 — Initial: No tests or evaluation; changes risk regressions.
- 3 — Defined: Offline eval set and regression tests; review gates exist.
- 5 — Optimized: Automated evaluation and CI gates prevent regressions at scale.

### 4) Observability & Reliability
- 1 — Initial: Limited logging; failures are hard to diagnose.
- 3 — Defined: Tracing/logging; error handling; fallbacks and retries.
- 5 — Optimized: SLOs, alerting, incident response; reliability is engineered.

### 5) Cost & Performance
- 1 — Initial: Costs uncontrolled; latency unpredictable.
- 3 — Defined: Caching, batching, and model selection; cost/latency tracked.
- 5 — Optimized: Cost is optimized per use case; performance is predictable and tuned.

### 6) Release & Operations
- 1 — Initial: No release process; changes are manual.
- 3 — Defined: Versioning, rollout strategy, and ownership defined.
- 5 — Optimized: Operations are mature; safe rollbacks and continuous improvements.

## Deliverables
- Technical readiness scorecard and gap list
- Target architecture and integration plan
- Evaluation harness and regression suite outline
- Observability plan (logs, traces, metrics)
- Cost/latency optimization plan and targets

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [USE_CASE]: Target use case
- [LATENCY_TARGET]: Latency target
- [BUDGET]: Budget
- [MODEL]: Model selection
- [RAG]: Retrieval strategy
- [SLOS]: SLO targets

## Example (Condensed)
- Use case: Customer support assistant with strict latency needs
- Scores (1–5): Architecture 3; Retrieval 2; Testing 2; Observability 2; Cost 2; Ops 2
- 90-day priorities: Build evaluation + CI gates; improve retrieval relevance; add tracing/alerting and cost dashboards

