---
category: education
title: Research Paper Readiness Assessment
tags:
- research-papers
- manuscript-writing
- scientific-argumentation
- evidence-presentation
- readiness-assessment
use_cases:
- Determining whether a manuscript is ready to draft, submit, or revise
- Identifying gaps in story, methods reporting, results framing, and journal fit
- Producing a concise manuscript blueprint (IMRAD) and revision checklist
- Aligning co-authors on claims, evidence standards, and submission workflow
related_templates:
- education/Academic-Research/publication-writing.md
- education/Scientific-Communication/peer-review.md
- education/Scientific-Communication/data-visualization.md
- education/curriculum-development.md
- education/curriculum-development-framework.md
industries:
- education
- government
- healthcare
- manufacturing
type: framework
difficulty: intermediate
slug: research-papers
---

# Research Paper Readiness Assessment

## Purpose
Assess whether your research paper is ready to draft or submit by scoring six dimensions: Journal & Audience Fit, Core Story & Contribution, Methods & Reporting Completeness, Results & Evidence Presentation, Discussion & Limitations, and Submission & Revision Workflow. Use the output to decide **go / revise-first** and to produce a tight manuscript plan.

## 🚀 Quick Assessment Prompt

> Assess **research paper readiness** for **{MANUSCRIPT_CONTEXT}** targeting **{TARGET_VENUE}** with **{CONSTRAINTS}**. Score each dimension 1–5 with brief evidence: (1) journal & audience fit, (2) story & contribution, (3) methods & reporting completeness, (4) results & evidence, (5) discussion & limitations, (6) submission & revision workflow. Provide an overall maturity level, a go/revise-first recommendation, and a prioritized revision plan.

**Usage:** Replace the curly-brace placeholders with your specifics.

---

## Template

Conduct a research paper readiness assessment for {MANUSCRIPT_CONTEXT} targeting {TARGET_VENUE} with {CONSTRAINTS}.

Assess readiness across six dimensions, scoring each 1–5:

**1. JOURNAL & AUDIENCE FIT READINESS**
Evaluate whether the manuscript matches venue expectations: scope, article type, novelty bar, methodological norms, word/figure limits, and audience background. Confirm you can meet required checklists (reporting standards, declarations, data sharing) and that your framing speaks to what the venue values.

**2. CORE STORY & CONTRIBUTION READINESS**
Evaluate whether the “why” is crisp: problem/gap, aim(s), and the contribution (new evidence, method, theory, or practical implication). Confirm the manuscript can be summarized in a 2–3 sentence abstract-level statement without hand-waving and that claims are proportional to evidence.

**3. METHODS & REPORTING COMPLETENESS READINESS**
Evaluate whether a reader could reproduce or audit the work: design, sample/setting, measures, procedures, and analysis decisions are documented at an appropriate level. Identify missing details that block review (eligibility, recruitment, preprocessing, assumptions, preregistration, ethics approvals).

**4. RESULTS & EVIDENCE PRESENTATION READINESS**
Evaluate whether results are clear and defensible: primary outcomes are prioritized, uncertainty is reported, and figures/tables support the claims. Confirm that exploratory analyses are labeled and that you avoid p-hacking vibes by documenting decision rules.

**5. DISCUSSION & LIMITATIONS READINESS**
Evaluate whether interpretation is honest and useful: connect back to the gap, compare to prior work, explain mechanisms cautiously, and state limitations without burying them. Confirm boundaries of generalizability and what would change your conclusion.

**6. SUBMISSION & REVISION WORKFLOW READINESS**
Evaluate whether you can ship: authorship order, roles, internal deadlines, journal formatting tasks, required files (cover letter, disclosures, figures, supplements), and a plan for revision cycles. Confirm you have a response-to-reviewers strategy and evidence you can produce if challenged.

---

## Required Output Format

1. **EXECUTIVE SUMMARY** - Overall readiness score (X.X/5.0), maturity level, go/revise-first, top 3 risks

2. **DIMENSION SCORECARD** - Table: dimension, score (1–5), evidence, biggest gap, highest-impact fix

3. **ONE-PAGE MANUSCRIPT BLUEPRINT**
- Title + 2-sentence abstract gist
- IMRAD bullet outline (what each section must accomplish)
- Figures/tables list (what claim each supports)

4. **REVISION PLAN (TOP 10)** - The next edits to make, ranked by impact

5. **SUBMISSION CHECKLIST** - Required files + compliance items

---

## Maturity Scale (1–5)
- **1 — Initial:** Story unclear; methods/results incomplete; high mismatch to venue.
- **2 — Developing:** Draftable, but major reporting/logic gaps and weak contribution framing.
- **3 — Defined:** Coherent manuscript; evidence mostly aligned; needs tightening and compliance polish.
- **4 — Managed:** Strong narrative and figures; robust reporting; submission-ready workflow.
- **5 — Optimized:** Highly competitive package; reusable assets; fast revision cycles with minimal rework.

---

## Variables (Use Max 3)

| Variable | What to include | Example |
|---|---|---|
| `{MANUSCRIPT_CONTEXT}` | Study type + domain + main finding | “Observational cohort; ICU outcomes; calibrated risk model” |
| `{TARGET_VENUE}` | Journal/track + article type + constraints | “JMIR; original research; 4500 words; open data preferred” |
| `{CONSTRAINTS}` | Timeline, co-author availability, data sharing limits | “Submit in 3 weeks; IRB limits data sharing; 4 authors” |

---

## Example (Filled)

**Input**
- `{MANUSCRIPT_CONTEXT}`: “Mixed-methods evaluation of a new nurse training program across 3 hospitals.”
- `{TARGET_VENUE}`: “Health services journal; original research; requires limitations and implementation relevance.”
- `{CONSTRAINTS}`: “Submit in 4 weeks; 2 co-authors limited availability; de-identified data only.”

**Output (abridged)**
- Executive summary: 3.0/5 (Defined), **revise-first**
- Biggest gaps: unclear primary outcome; figures not tied to claims; discussion overstates causality
- Next edits: specify primary outcome and estimand; rebuild results section around 2–3 core figures; add limitations and implementation boundary conditions; align title/abstract to venue framing

---

## Best Practices (8)

1. Make one primary claim and design the paper around proving it.
2. Keep methods complete enough for audit/reproducibility.
3. Label exploratory analyses clearly; don’t blend them with confirmatory results.
4. Use figures/tables to support specific claims (one claim per figure).
5. Report uncertainty and limitations without weakening the main point.
6. Match the venue’s norms for contribution and tone.
7. Treat compliance items as schedule constraints.
8. Use structured revision cycles: logic → evidence → clarity → formatting.

---

## Related Resources
- Improve academic publication workflow: `publication-writing.md`
- Strengthen reviewer expectations: `peer-review.md`
- Make figures defensible and readable: `data-visualization.md`
