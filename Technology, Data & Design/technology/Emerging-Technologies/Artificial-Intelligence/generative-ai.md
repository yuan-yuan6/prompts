---
category: technology
related_templates:
- technology/Emerging-Technologies/generative-ai-implementation.md
tags:
- generative-ai
- llm
- rag
- ai-safety
- capability-assessment
title: Generative AI Readiness Assessment
use_cases:
- Evaluating readiness to deploy generative AI products and copilots
- Identifying architecture, safety, and operational gaps before piloting
- Selecting between prompt-only, RAG, and fine-tuning approaches
- Creating a 90-day pilot plan and 12-month scaling roadmap
industries:
- finance
- government
- healthcare
- manufacturing
- technology
type: framework
difficulty: intermediate
slug: generative-ai
---

# Generative AI Readiness Assessment

## Purpose
Assess whether an organization is ready to design, deploy, and operate generative AI systems (LLM-powered copilots, assistants, and workflows) in a way that is safe, measurable, and operationally sustainable. This assessment focuses on the decisions that most often drive success or failure—use case fit, knowledge and data readiness, model/architecture choices, safety and trust controls, delivery and operations, and organizational adoption.

## 🚀 Quick Prompt

> Assess **generative AI readiness** for **{ORGANIZATION}** planning to implement **{GENAI_USE_CASES}** in **{DEPLOYMENT_CONTEXT}**. Evaluate: (1) value and workflow fit, (2) knowledge/data and grounding readiness, (3) model and architecture choices (prompt-only vs RAG vs fine-tune), (4) safety, privacy, and compliance controls, (5) delivery, evaluation, and operations (LLMOps), and (6) people/process readiness and change adoption. Provide a scorecard (1–5 per dimension), top risks, recommended architecture approach per use case, a 90-day pilot plan with evidence gates, and a 12-month roadmap.

---

## Template

Conduct a comprehensive generative AI readiness assessment for {ORGANIZATION} planning to implement {GENAI_USE_CASES} in {DEPLOYMENT_CONTEXT}.

Score each dimension from 1.0 to 5.0 and justify scores with evidence. Evidence can include workflow maps, user research notes, prompt logs, retrieval experiments, evaluation results, security reviews, vendor contracts, cost models, incident runbooks, and stakeholder alignment artifacts.

### 1) Use Case & Workflow Readiness
Assess whether the selected use cases are worth building by examining whether they represent repeatable workflows with measurable impact (cycle time, quality, customer outcomes, cost), whether the task is appropriate for probabilistic systems (tolerant to variance and uncertainty, with clear human review points where needed), whether there is an explicit definition of “good output” and a plan to measure it, whether the user experience is designed around assistance rather than automation theater, whether failure modes are acceptable (and where escalation or refusal is required), and whether the organization is prepared to simplify the scope to a small number of high-value workflows rather than attempting a broad enterprise assistant that lacks grounding.

A strong score implies the use cases are specific, measurable, adoption-ready, and scoped to the organization’s ability to deliver safely.

### 2) Knowledge, Data & Grounding Readiness
Assess whether responses can be grounded in reliable information by evaluating whether the organization has authoritative knowledge sources (policies, product docs, SOPs, contracts, knowledge bases) that are current and internally consistent, whether there is clarity on what information is allowed to be used (privacy, confidentiality, IP, regulated data), whether documents are structured enough for retrieval or can be made retrievable (clean text, stable identifiers, versioning), whether the team can define “source of truth” ownership and update workflows, whether the system can attach citations or references to internal documents when appropriate, and whether the organization can measure and improve answer quality via evaluation sets that reflect real user questions.

A strong score implies the organization can ground outputs in trustworthy sources and maintain that trust as content changes.

### 3) Model & Architecture Readiness
Evaluate whether the model and system architecture are well-chosen by determining whether the team understands the trade-offs between prompt-only, RAG, and fine-tuning, whether model selection is driven by requirements (latency, cost, context size, multilingual, tool use, reasoning, safety needs) rather than hype, whether the design accounts for tool calling and guardrailed actions when the assistant must change systems of record, whether the solution includes robust prompting and prompt management practices (versioning, regression tests, change control), whether the architecture plans for multi-turn conversations and state safely, and whether the team can validate performance with realistic end-to-end tests rather than relying on anecdotal demos.

A strong score implies the architecture is minimal, defensible, testable, and aligned to operational constraints.

### 4) Safety, Privacy & Compliance Readiness
Assess whether the solution can be deployed responsibly by evaluating whether sensitive data handling is defined (PII, PHI, PCI, trade secrets), whether privacy and retention are addressed (logging, redaction, data minimization, deletion), whether the system design mitigates common GenAI risks (hallucinations, prompt injection, data exfiltration via retrieval, overconfident tone, unsafe content), whether the organization has policies for human review and escalation for high-risk actions, whether there is an approach to authorization (who can see what, based on identity and role), whether vendor and model risk are assessed (contracts, data use terms, regional requirements), and whether compliance stakeholders can sign off based on evidence, not assurances.

A strong score implies safety is treated as an engineering and operational discipline with measurable controls and clear ownership.

### 5) Delivery, Evaluation & LLMOps Readiness
Evaluate the ability to ship and maintain the system by assessing whether the team can run disciplined evaluations (golden sets, offline tests, online monitoring, human review sampling), whether quality metrics are defined for each use case (task success, helpfulness, factuality, retrieval precision/recall, refusal correctness), whether the deployment has observability for both product and model behavior (latency, token cost, tool-call success, citation rates, error rates, jailbreak attempts), whether there is a release process that prevents silent regressions (canary releases, prompt/model version tracking), whether incident response is defined for model failures (rollbacks, temporary restrictions, communications), and whether cost management is planned (rate limits, caching, model routing, budgets).

A strong score implies the organization can treat LLM behavior as production software with test suites, monitoring, and safe rollout processes.

### 6) People, Process & Adoption Readiness
Assess organizational readiness by evaluating whether there is clear product ownership and an operating model (who owns prompts, retrieval content, evaluation, approvals, and incident response), whether end users are engaged early and trained to use the system appropriately, whether the organization can change workflows to capture value rather than layering a chatbot on top of broken processes, whether there is executive sponsorship and cross-functional alignment across product, engineering, security, legal, and operations, whether the team can manage expectations about limitations, and whether adoption will be measured and improved with feedback loops that influence the roadmap.

A strong score implies the organization can drive adoption and sustain improvements beyond the initial launch.

---

## Required Output Format

Provide:

1) Executive summary with overall readiness (X.X/5.0), maturity stage, the single highest-leverage next step, and top 3 blockers.

2) Dimension scorecard with scores and short evidence-based rationale.

3) Use case recommendations describing, for each target use case, the most appropriate approach (prompt-only, RAG, fine-tune, tool-enabled workflow) and why.

4) Risk register listing the top 10 risks with likelihood, impact, mitigation, and owner type.

5) 90-day pilot plan with scope, success metrics, evaluation approach, and evidence gates for go/no-go.

6) 12-month roadmap describing scaling steps for quality, safety, content governance, and operations.

---

## Maturity Scale

- 1.0–1.9: Exploratory (demos and curiosity; weak grounding, safety, and ops)
- 2.0–2.9: Prototyping (working prototypes; inconsistent quality; limited controls)
- 3.0–3.9: Piloting (scoped pilots; evaluation discipline; controlled deployment)
- 4.0–4.9: Production (reliable operations; measurable outcomes; strong governance)
- 5.0: Leading (optimized systems; continuous improvement; strong safety culture)

---

## Variables

| Variable | Description | Examples |
|----------|-------------|----------|
| `{ORGANIZATION}` | The organization or team being assessed | "Regional bank", "State agency", "Manufacturing group" |
| `{GENAI_USE_CASES}` | The intended GenAI workflows and users | "Customer support drafting", "Policy Q&A", "Engineer copilot" |
| `{DEPLOYMENT_CONTEXT}` | Where and how it will be deployed | "Internal copilot for 2,000 employees", "Public-facing assistant", "Hybrid" |

---

## Usage Example (Single Example)

**Scenario:** A healthcare provider wants an internal clinician-facing assistant that answers policy and procedure questions and drafts patient communication templates. The assistant will be used by 1,200 staff in a secured environment, must avoid PHI exposure, and must cite approved internal policies.

**Scores (1–5):** Use Case & Workflow 3.2, Knowledge/Data & Grounding 2.4, Model & Architecture 2.9, Safety/Privacy/Compliance 2.6, Delivery/Evaluation/LLMOps 2.2, People/Process/Adoption 2.8. Overall readiness: 2.7/5.0 (Prototyping).

**Key findings:** The use case is high-value because it reduces time spent searching policies and improves consistency, but the knowledge base is fragmented across multiple systems with inconsistent naming and ownership. A RAG approach is appropriate because the assistant must cite approved documents and policies change frequently, but retrieval quality will be the primary risk until content is consolidated and versioned. Safety and compliance concerns are manageable if the system is restricted to internal use, enforces role-based access to documents, and logs are minimized and redacted, but incident response and review workflows are not yet defined. Delivery maturity is the weakest area: there is no evaluation set, no regression testing for prompts, and no monitoring plan for hallucinations, injection attempts, or citation failure.

**90-day pilot plan:** In weeks 1–2, define the top 25 real staff questions, build an evaluation set with target answers and approved citations, and establish a content ownership process. In weeks 3–5, implement a limited RAG prototype using only the approved policy corpus with citations required and strict refusal behavior when sources are missing. In weeks 6–8, run a controlled pilot with 50 users, measure task success and citation correctness, and tune retrieval and prompts based on failure analysis. In weeks 9–12, implement monitoring and incident response, expand corpus coverage, and run a go/no-go review based on quality thresholds and compliance sign-off.

---

## Related Resources

- [Generative AI Implementation](technology/Emerging-Technologies/generative-ai-implementation.md)
