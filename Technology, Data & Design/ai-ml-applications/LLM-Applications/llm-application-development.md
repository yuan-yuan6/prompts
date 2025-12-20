---
category: ai-ml-applications
title: LLM Application Development Readiness Assessment
tags:
- llm-development
- llm-integration
- production-llm
- llm-api
- readiness-assessment
use_cases:
- Building production LLM-powered applications and products
- Integrating LLM capabilities into existing software systems
- Creating AI-native features for web and mobile applications
- Developing customer-facing AI applications with reliability and safety
related_templates:
- ai-ml-applications/LLM-Applications/prompt-engineering-workflows.md
- ai-ml-applications/LLM-Applications/rag-systems.md
- ai-ml-applications/LLM-Applications/ai-agents-autonomous-systems.md
- ai-ml-applications/MLOps-Deployment/mlops-model-deployment.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: llm-application-development
---

# LLM Application Development Readiness Assessment

## Purpose
Assess readiness to build LLM-powered applications with sound product requirements, evaluation, architecture, and operational reliability.

## Quick Prompt

> Assess LLM app development readiness for [USE_CASE] with target users [USERS]. Score readiness (1–5) across: (1) Product requirements, (2) Data & grounding, (3) Evaluation & testing, (4) Architecture & integrations, (5) Safety/security, (6) Operations & iteration. Provide a scorecard, top gaps, and a 90-day plan.

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
- LLM app readiness scorecard and prioritized gaps
- Product requirements and success metrics
- Evaluation plan and benchmark dataset outline
- Architecture and integration plan
- Operations plan (monitoring, incident response, iteration)

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [USE_CASE]: Target use case
- [USERS]: Target users
- [MODEL]: Model selection
- [TOOLS]: Tools/functions the model can call
- [RAG]: Retrieval approach
- [QUALITY_METRICS]: Quality metrics

## Example (Condensed)
- Use case: Sales enablement assistant integrated with CRM
- Scores (1–5): Requirements 3; Data 2; Evaluation 2; Engineering 3; Governance 2; Adoption 3
- 90-day priorities: Build evaluation set; implement grounding and logging; add monitoring and staged rollout

