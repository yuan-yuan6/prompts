---
category: education
title: Literature Review Readiness Assessment
tags:
- literature-reviews
- research-synthesis
- systematic-reviews
- scoping-reviews
- meta-analysis
- readiness-assessment
use_cases:
- Determining whether a literature review is ready to execute and publish
- Identifying gaps in search strategy, screening, extraction, and synthesis plans
- Producing a defensible review protocol outline and execution checklist
- Aligning collaborators on scope, rigor, and deliverables
related_templates:
- education/Academic-Research/literature-reviews-overview.md
- education/Academic-Research/publication-writing.md
- education/Academic-Research/research-design-analysis-quality.md
- education/curriculum-development.md
- education/curriculum-development-framework.md
industries:
- education
- government
- healthcare
- manufacturing
- technology
type: framework
difficulty: intermediate
slug: literature-reviews
---

# Literature Review Readiness Assessment

## Purpose
Assess whether you’re ready to execute a rigorous literature review by scoring six dimensions: Scope & Questions, Search Strategy, Screening & Selection, Extraction & Data Management, Synthesis & Interpretation, and Reporting & Transparency. Use this as a **go / revise-first / stop** gate before investing heavy execution effort.

## Template

Conduct a literature review readiness assessment for {REVIEW_CONTEXT} using {REVIEW_TYPE} under {CONSTRAINTS}.

Assess readiness across six dimensions, scoring each 1–5:

**1. SCOPE & QUESTIONS READINESS**
Evaluate whether the review is well-posed by assessing whether the topic is bounded, the review questions are answerable, and inclusion decisions are defensible (population/context, interventions/exposures, outcomes/phenomena, study designs). Confirm that the review’s purpose is explicit (mapping field, estimating effects, explaining mechanisms, identifying gaps) and that scope matches constraints.

**2. SEARCH STRATEGY READINESS**
Evaluate whether you can reliably find relevant evidence by assessing database/source coverage, keyword strategy, controlled vocabulary usage, and grey literature plans (if needed). Confirm the search is reproducible (documented strings, dates, filters) and that it balances sensitivity vs precision for your review type.

**3. SCREENING & SELECTION READINESS**
Evaluate whether selection will be consistent and bias-aware by assessing inclusion/exclusion criteria clarity, screening workflow (title/abstract → full text), reviewer roles, calibration, and disagreement resolution. Confirm you have a plan for deduplication, recordkeeping, and reasons-for-exclusion.

**4. EXTRACTION & DATA MANAGEMENT READINESS**
Evaluate whether you can capture the right information by assessing extraction fields (study characteristics, methods, measures, results, context), coding rules, and data structures. Confirm versioning, audit trail, and a plan to handle missing/ambiguous reporting or multiple publications of the same study.

**5. SYNTHESIS & INTERPRETATION READINESS**
Evaluate whether synthesis choices match evidence type: narrative/thematic synthesis, meta-analysis, evidence mapping, or framework synthesis. Confirm plans for heterogeneity, subgroup/sensitivity analyses (if quantitative), or credibility checks and boundary conditions (if qualitative). Ensure interpretation standards prevent overclaiming.

**6. REPORTING & TRANSPARENCY READINESS**
Evaluate whether outputs will be publication-ready and transparent by assessing reporting standards (e.g., PRISMA where applicable), protocol documentation, limitation reporting, and sharing expectations (materials, extraction forms, code, data) within ethical and license constraints.

---

## Required Output Format

1. **EXECUTIVE SUMMARY** - Overall readiness score (X.X/5.0), maturity level, go/revise-first/stop, top 3 risks

2. **DIMENSION SCORECARD** - Table: dimension, score (1–5), evidence, biggest gap, highest-impact fix

3. **PROTOCOL OUTLINE (ONE PAGE)**
- Review questions
- Eligibility criteria (inclusion/exclusion)
- Sources + search plan (high level)
- Screening plan (roles + calibration)
- Extraction plan (fields + tools)
- Synthesis plan + reporting standard

4. **EXECUTION CHECKLIST (TOP 15)** - The most important next actions, in order

5. **RISK REGISTER (TOP 5)** - Bias/feasibility risks with mitigations

---

## Maturity Scale (1–5)
- **1 — Initial:** Topic vague; search/screening not reproducible; synthesis approach undefined.
- **2 — Developing:** Basic protocol exists; major gaps in criteria, workflow, or extraction/synthesis discipline.
- **3 — Defined:** Coherent protocol; feasible workflow; key risks identified; needs tightening and calibration.
- **4 — Managed:** Reproducible search + screening; strong extraction QA; synthesis/reporting standards clear.
- **5 — Optimized:** Highly efficient, low-bias system; reusable assets; strong transparency and reviewer anticipation.

---

## Variables (Use Max 3)

| Variable | What to include | Example |
|---|---|---|
| `{REVIEW_CONTEXT}` | Topic + domain + intended contribution | “AI triage tools in emergency medicine; safety and equity impacts” |
| `{REVIEW_TYPE}` | Systematic / scoping / narrative / meta-analysis + why | “Scoping review to map methods and gaps” |
| `{CONSTRAINTS}` | Timeline, access, languages, team size, tooling | “6 weeks, 2 reviewers, English only, limited database access” |

---

## Example (Filled)

**Input**
- `{REVIEW_CONTEXT}`: “Remote work interventions and employee burnout in knowledge workers.”
- `{REVIEW_TYPE}`: “Systematic review with narrative synthesis (outcomes heterogeneous).”
- `{CONSTRAINTS}`: “8 weeks, 2 reviewers, English only, no paywalled databases beyond institution.”

**Output (abridged)**
- Executive summary: 2.8/5 (Developing), **revise-first**
- Biggest gaps: unclear eligibility criteria; search strings not drafted; no calibration plan
- Next actions: finalize PICO/eligibility; draft and pilot search strings; set screening calibration (50 records) + disagreement rule; define extraction fields + QA spot-check

---

## Best Practices (8)

1. Write your eligibility criteria so two people apply them the same way.
2. Pilot the search and screening on a small set before committing.
3. Document search strings, dates, filters, and all sources for reproducibility.
4. Separate “what the evidence shows” from “what you think it implies.”
5. Predefine how you will handle heterogeneity and low-quality studies.
6. Use an audit trail: versions, decisions, and reasons-for-exclusion.
7. Treat scope control as a success metric; avoid “infinite review” expansion.
8. Report limitations and bias risks explicitly; don’t bury them.

---

## Related Resources
- Start with the suite entry point: `literature-reviews-overview.md`
- Align synthesis and QA practices: `research-design-analysis-quality.md`
- Turn the review into a publishable manuscript: `publication-writing.md`
