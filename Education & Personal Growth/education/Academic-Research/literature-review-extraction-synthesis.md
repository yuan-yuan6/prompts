---
category: education
related_templates:
- education/Academic-Research/literature-review-selection-quality.md
- education/Academic-Research/literature-review-analysis-implications.md
- education/Academic-Research/literature-reviews-overview.md
tags:
- data-extraction
- meta-analysis
- thematic-synthesis
- evidence-integration
- capability-assessment
title: Literature Review Data Extraction & Synthesis Readiness Assessment
use_cases:
- Evaluating readiness to extract study data consistently and reproducibly
- Planning quantitative meta-analysis and qualitative synthesis with clear evidence rules
- Designing quality control, discrepancy resolution, and audit trails for extraction
- Producing synthesis-ready tables and artifacts for reporting and implications
industries:
- education
- healthcare
- manufacturing
type: framework
difficulty: intermediate
slug: literature-review-extraction-synthesis
---

# Literature Review Data Extraction & Synthesis Readiness Assessment

## Purpose
Assess whether a literature review team is ready to perform high-quality data extraction and defensible evidence synthesis (quantitative, qualitative, or mixed-methods). This framework helps you ensure that what you extract is consistent, what you synthesize is methodologically appropriate, and what you report is reproducible and decision-useful.

## Template

Conduct a data extraction and synthesis readiness assessment for {REVIEW_CONTEXT} using {STUDY_SET} and {SYNTHESIS_APPROACH}.

Score each dimension from 1.0 to 5.0 and justify scores with concrete evidence (protocol sections, extraction form drafts, codebook, piloting results, inter-rater agreement checks, analysis plan, and reproducibility artifacts).

### 1) Extraction Scope & Variable Definition Readiness
Assess whether the extraction plan is clear enough to produce consistent data by evaluating whether the review question and eligibility criteria map directly to the variables you will extract, whether every extracted element has an operational definition (including permissible values, units, timing, and directionality), whether outcomes are specified with priority order (primary, secondary, timepoints), whether intervention/exposure elements are decomposed into components that can be compared across studies, whether missing/unclear data rules are pre-defined (contact authors, impute, exclude), and whether you have rules for multi-arm trials, clustered designs, crossovers, and repeated measures.

A strong score implies two independent extractors would produce highly similar outputs from the same study without “interpretation drift.”

### 2) Quality Control, Discrepancy Resolution & Auditability Readiness
Evaluate whether extraction quality will hold under time pressure by assessing whether you have a dual extraction or verification plan, whether discrepancy resolution rules are explicit (who arbitrates, what evidence is required), whether you track decisions in an audit log (including protocol deviations), whether the team has a process for updating the extraction form without corrupting prior entries (versioning and migration rules), whether you can quantify extraction reliability (spot checks, inter-rater agreement where appropriate), and whether risk-of-bias and study quality indicators are captured in a way that can be used later in interpretation and sensitivity analyses.

A strong score implies the dataset can be defended in peer review because decisions are traceable and repeatable.

### 3) Quantitative Synthesis & Meta-Analysis Readiness
Assess readiness for quantitative synthesis by evaluating whether outcome types and effect metrics are selected appropriately (OR/RR/HR/MD/SMD), whether directionality is standardized, whether unit conversions and scale harmonization are planned, whether heterogeneity assessment and exploration are pre-specified (I², τ², prediction intervals, subgroup analysis), whether model choice is justified (fixed vs random effects, small-study adjustments), whether sensitivity analyses are planned (risk-of-bias exclusion, alternative metrics, influential studies), and whether publication bias assessment is appropriately scoped (recognizing limitations with small k).

A strong score implies the meta-analysis approach is pre-specified, implementable, and robust to common data issues.

### 4) Qualitative Synthesis & Thematic Rigor Readiness
Evaluate readiness for qualitative synthesis by assessing whether you have a clear synthesis method (thematic synthesis, framework synthesis, meta-ethnography, realist synthesis), whether coding procedures are specified (inductive vs deductive, codebook development, double coding strategy), whether you have rules for handling participant quotes versus author interpretations, whether reflexivity and analytic decisions are documented, whether you have a plan to seek disconfirming evidence and negative cases, and whether your synthesis outputs will be structured in a way that can inform practice or policy decisions rather than remaining purely descriptive.

A strong score implies the qualitative synthesis will be transparent, credible, and useful, not a loose collection of themes.

### 5) Mixed-Methods Integration & Synthesis Presentation Readiness
Assess whether results can be integrated and communicated by evaluating whether you know how quantitative and qualitative findings will relate (convergent, explanatory, sequential), whether you can produce joint displays that make alignment and disagreement visible, whether you have a plan to present findings at the right level of granularity for the audience (effect estimates with uncertainty; themes with supporting evidence), whether you can clearly distinguish evidence strength from interpretive narrative, and whether you can generate the specific artifacts needed for downstream steps (summary tables, forest plots, theme maps, evidence profiles).

A strong score implies the synthesis outputs will be decision-ready and easy to reuse in reporting and implications.

### 6) Tooling, Documentation & Reproducibility Readiness
Evaluate whether the work can be reproduced and maintained by assessing whether you have tooling for screening/extraction and analysis appropriate to team skill (spreadsheets, REDCap, review software, R/Stata), whether file organization and naming are standardized, whether analysis code and data transformations are version controlled, whether you can recreate figures/tables from raw extracted data without manual steps, whether you have a data dictionary and codebook, and whether you have a “data freeze” process with sign-off before analysis begins.

A strong score implies another team could replicate your extraction and synthesis decisions (or audit them) without relying on memory or undocumented steps.

---

## Required Output Format

Provide:

1) Executive summary with overall readiness (X.X/5.0), maturity stage, and top 3 blockers.

2) Dimension scorecard with brief evidence per score.

3) Minimum viable extraction form outline (the smallest set of fields required to answer the question correctly).

4) Data rules appendix: unit handling, directionality rules, timepoints, multi-arm studies, missing data handling, and discrepancy resolution.

5) Synthesis plan: quantitative methods (if applicable), qualitative methods (if applicable), and integration approach.

6) Risk register (top 10): extraction risks, analysis risks, bias risks, and mitigation.

7) Step-by-step execution plan from pilot extraction → full extraction → data freeze → synthesis → presentation artifacts.

---

## Maturity Scale

- 1.0–1.9: Ad-hoc (unclear variables, inconsistent extraction, unrepeatable process)
- 2.0–2.9: Developing (draft forms exist; QC and analysis rules incomplete)
- 3.0–3.9: Defined (piloted forms; pre-specified methods; basic reproducibility)
- 4.0–4.9: Robust (strong QC/audit trail; defensible synthesis; reusable artifacts)
- 5.0: Best-in-class (highly reproducible pipeline; strong integration; audit-ready)

---

## Variables

| Variable | Description | Examples |
|----------|-------------|----------|
| `{REVIEW_CONTEXT}` | Topic and research question scope | "Telehealth for diabetes outcomes", "Literacy interventions in K–12" |
| `{STUDY_SET}` | What studies are included | "27 RCTs (2015–2025)", "12 qualitative studies across 4 countries" |
| `{SYNTHESIS_APPROACH}` | Planned synthesis method | "Random-effects meta-analysis + sensitivity", "Thematic synthesis", "Mixed-methods joint displays" |

---

## Usage Example (Single Example)

**Scenario:** A team is conducting {REVIEW_CONTEXT} with {STUDY_SET}. They plan {SYNTHESIS_APPROACH} to support a guideline update.

**Scores (1–5):** Extraction Scope & Definitions 2.8, QC & Auditability 2.4, Quantitative Synthesis 3.1, Qualitative Synthesis 2.6, Integration & Presentation 2.5, Tooling & Reproducibility 2.3. Overall readiness: 2.6/5.0 (Developing).

**Key findings:** The team’s analysis plan is directionally appropriate, but the extraction codebook is not precise enough to prevent inconsistent timepoint handling and ambiguous outcome definitions. Quality control is under-specified: there is no clear discrepancy arbitration process or versioning plan for form changes after piloting. Reproducibility is weak because key transformations are planned “in Excel” without a defined audit trail. The fastest path to improvement is to pilot extraction on 3–5 studies, tighten definitions, lock the extraction form, and implement a minimal reproducible pipeline for tables and plots.

---

## Related Resources

- [Literature Review Selection & Quality](education/Academic-Research/literature-review-selection-quality.md)
- [Literature Review Analysis & Implications](education/Academic-Research/literature-review-analysis-implications.md)
- [Literature Reviews Overview](education/Academic-Research/literature-reviews-overview.md)
