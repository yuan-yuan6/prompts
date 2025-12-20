---
category: education
related_templates:
- education/Academic-Research/research-design-overview.md
- education/Academic-Research/research-design-foundation.md
- education/Academic-Research/research-design-sampling-data.md
- education/Academic-Research/research-design-analysis-quality.md
- education/Academic-Research/research-design-ethics-implementation.md
- education/Academic-Research/research-design-impact.md
tags:
- research-methodology
- study-design
- readiness-assessment
- quantitative-qualitative
- mixed-methods
- research-governance
title: Research Design Readiness Assessment (Master)
use_cases:
- Determining whether a study is ready for preregistration, IRB submission, or fieldwork
- Producing a concise, defensible study design plan with identified risks and fixes
- Aligning advisors, collaborators, and stakeholders on scope, feasibility, and rigor
- Routing into the specialized Research Design suite modules
industries:
- education
- finance
- government
- healthcare
- nonprofit
- technology
type: framework
difficulty: intermediate
slug: research-design
---

# Research Design Readiness Assessment (Master)

## Purpose
Assess whether your study is ready to proceed by evaluating six core dimensions of research design: Framing & Contribution, Design & Inference Fit, Sampling & Data Collection, Analysis & Quality Assurance, Ethics & Implementation, and Reporting & Impact. Use this as an end-to-end “go/no-go” gate and as a router into the Research Design suite modules.

## 🚀 Quick Prompt

> Assess **research design readiness** for **{STUDY_CONTEXT}** addressing **{PRIMARY_RESEARCH_QUESTIONS}** under **{CONSTRAINTS}**. Score each dimension 1–5 with brief evidence: (1) **Framing & contribution**, (2) **Design & inference fit**, (3) **Sampling & data collection**, (4) **Analysis & quality assurance**, (5) **Ethics & implementation**, (6) **Reporting & impact**. Provide an overall maturity level, a go/revise-first recommendation, and a prioritized action plan mapped to the appropriate Research Design suite module(s).


---

## Template

Conduct a research design readiness assessment for {STUDY_CONTEXT} addressing {PRIMARY_RESEARCH_QUESTIONS} under {CONSTRAINTS}.

Assess readiness across six dimensions, scoring each 1–5:

**1. FRAMING & CONTRIBUTION READINESS**
Evaluate whether the study is worth doing and well-scoped by assessing whether the problem is clearly defined, the target contribution is explicit (theory, method, evidence, practice), and the questions are specific enough to drive design decisions. Examine whether key constructs are operationally defined, whether the study is positioned relative to prior work, and whether the scope matches available resources.

**2. DESIGN & INFERENCE FIT READINESS**
Evaluate whether the chosen design supports the intended inference by assessing alignment between research questions and design type (experimental/quasi-experimental/observational/qualitative/mixed). Examine whether identification logic is clear for causal claims, whether comparators/counterfactuals are plausible, whether threats to validity are recognized, and whether the design choices are justified given constraints.

**3. SAMPLING & DATA COLLECTION READINESS**
Evaluate whether you can obtain the right evidence by assessing whether the target population and eligibility criteria are testable, the sampling approach is defensible (power/saturation logic), recruitment and retention are feasible, and instruments/protocols are fit for population and setting. Examine whether pilots, training, SOPs, and quality checks are defined.

**4. ANALYSIS & QUALITY ASSURANCE READINESS**
Evaluate whether analysis decisions are pre-specified and defensible by assessing whether the analysis plan maps to questions and variables, whether decision rules for cleaning/exclusions are explicit, and whether robustness/credibility checks are planned. Examine whether reproducibility is operational (versioning, audit trail, code organization), and whether reporting plans prevent p-hacking/HARKing where relevant.

**5. ETHICS & IMPLEMENTATION READINESS**
Evaluate whether the study can be conducted responsibly and on time by assessing participant risk, consent, privacy/security, and compliance requirements (IRB, permissions, data use). Examine whether roles, timeline, budget, and dependencies are realistic, and whether risk mitigations exist for predictable failures (access delays, attrition, instrument issues, data pipeline breakdowns).

**6. REPORTING & IMPACT READINESS**
Evaluate whether results will be communicated appropriately by assessing target audiences, outputs, and dissemination channels. Examine whether the reporting plan matches evidence strength and limitations, whether transparency expectations are defined (materials/data/code sharing where permissible), and whether there is a plan to translate findings into action, replication, or follow-on studies.

---

## Required Output Format

1. **EXECUTIVE SUMMARY** - Overall readiness score (X.X/5.0), maturity level, go/revise-first recommendation, top 3 risks

2. **DIMENSION SCORECARD** - Table: dimension, score (X.X/5), key gap, highest-impact fix, and which suite module to use

3. **STUDY DESIGN ONE-PAGER** - Design type, setting, units of analysis, timeline, key outcomes/constructs, intended inference

4. **DATA PLAN** - Population/eligibility, sampling approach and sample size logic, recruitment workflow, instruments, pilot/QC plan

5. **ANALYSIS & QA PLAN** - Primary analyses, assumptions, robustness checks, missing data plan, reproducibility controls

6. **ETHICS & EXECUTION PLAN** - Risks, consent, privacy/security, approvals needed, roles, dependencies, mitigations

7. **REPORTING & DISSEMINATION PLAN** - Target audiences, outputs, transparency plan, impact/translation steps

Use this maturity scale:
- **1.0–1.9: Ad hoc** (insufficient clarity/rigor; not ready to proceed)
- **2.0–2.9: Developing** (basic plan exists; major gaps remain)
- **3.0–3.9: Defined** (credible plan; targeted revisions required)
- **4.0–4.9: Managed** (strong readiness; execute with monitoring)
- **5.0: Exemplary** (high rigor, feasibility, and transparency)

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{STUDY_CONTEXT}` | Topic + design + setting | "Quasi-experimental evaluation of a workforce training program across 12 sites" |
| `{PRIMARY_RESEARCH_QUESTIONS}` | The key questions/hypotheses | "Does training increase earnings at 6 months, and for whom?" |
| `{CONSTRAINTS}` | Real-world constraints | "No randomization; admin data only; 9-month deadline; limited budget" |

---

## Usage Example

**Input:**
"{STUDY_CONTEXT}: Mixed-methods evaluation of a new onboarding program for junior nurses"
"{PRIMARY_RESEARCH_QUESTIONS}: Does onboarding reduce early turnover, and what barriers do new nurses report?"
"{CONSTRAINTS}: Small sample; 4-month window; IRB required; limited survey fatigue tolerance"

**Output (abridged):**
- Overall Readiness: **2.9/5.0 (Developing)**
- Recommendation: **REVISE-FIRST** (pilot instruments + formalize QC and governance)
- Top Risks: recruitment/participation burden, unclear identification strategy for outcomes, under-specified data handling
- Module Routing: **Foundation** → **Sampling & Data** → **Ethics & Implementation** → **Analysis & Quality**

---

## Related Resources

- **[Research Design Suite Readiness Assessment (Overview)](research-design-overview.md)** - Quick routing into the right module
- **[Research Design Foundation Readiness Assessment](research-design-foundation.md)** - Questions, theory, and design selection
- **[Research Sampling & Data Collection Readiness Assessment](research-design-sampling-data.md)** - Sampling, recruitment, instruments, fieldwork
- **[Research Analysis & Quality Assurance Readiness Assessment](research-design-analysis-quality.md)** - Analysis plan, rigor, reproducibility
- **[Research Ethics & Implementation Readiness Assessment](research-design-ethics-implementation.md)** - Compliance, risk, timeline, operations
- **[Research Impact, Innovation & Improvement Readiness Assessment](research-design-impact.md)** - Dissemination, usage, iteration---