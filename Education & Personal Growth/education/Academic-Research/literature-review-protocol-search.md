---
category: education
related_templates:
- education/Academic-Research/literature-review-selection-quality.md
- education/Academic-Research/literature-review-extraction-synthesis.md
- education/Academic-Research/literature-reviews-overview.md
tags:
- review-protocol
- search-strategy
- database-search
- methodological-framework
- capability-assessment
title: Literature Review Protocol & Search Strategy Readiness Assessment
use_cases:
- Evaluating readiness to start a rigorous literature review (systematic, scoping, or meta-analysis)
- Designing a defensible search strategy with transparent inclusion/exclusion rules
- Producing a protocol that is auditable, reproducible, and ready for registration
- Creating a practical plan from protocol → screening → extraction → synthesis
industries:
- education
- government
- healthcare
- manufacturing
type: framework
difficulty: intermediate
slug: literature-review-protocol-search
---

# Literature Review Protocol & Search Strategy Readiness Assessment

## Purpose
Assess whether a review team is ready to launch a literature review with a protocol and search strategy that are rigorous, reproducible, and aligned to the research question. This framework helps you avoid common failure modes (vague scope, untestable questions, unreplicable searches, and inconsistent selection decisions) and produce a protocol that can be registered and executed.

## 🚀 Quick Assessment Prompt

> Assess **protocol & search readiness** for **{REVIEW_CONTEXT}** using **{REVIEW_METHOD}** with a planned search scope of **{SEARCH_SCOPE}**. Evaluate: (1) question clarity and protocol scope, (2) eligibility criteria and decision rules, (3) search strategy design and database coverage, (4) screening workflow and quality controls, (5) governance, documentation, and reproducibility, and (6) feasibility (timeline, resources, stakeholder needs). Provide a scorecard (1–5), top risks, a minimum viable protocol outline, and a step-by-step plan to register and execute the search.

---

## Template

Conduct a protocol and search strategy readiness assessment for {REVIEW_CONTEXT} using {REVIEW_METHOD} with {SEARCH_SCOPE}.

Score each dimension from 1.0 to 5.0 and justify scores using concrete artifacts (draft protocol sections, pilot search results, sample inclusion/exclusion decisions, PRISMA-P checklist mapping, librarian peer review feedback, and a realistic timeline/resource plan).

### 1) Research Question & Scope Readiness
Assess whether the review is well-framed by evaluating whether the question can be answered with available evidence, whether the review type matches the objective (systematic review for effectiveness/associations, scoping review for mapping, meta-analysis when effect estimates are combinable), whether the question is expressed with an appropriate framing tool (PICO/PEO/SPIDER or equivalent) without forcing a poor fit, whether outcomes and time horizons are explicit, whether the scope is bounded tightly enough to be feasible, and whether the intended decision use is clear (publication, guideline input, policy brief, internal decision support).

A strong score implies the question is answerable, the scope is controlled, and the review type is justified.

### 2) Eligibility Criteria & Decision Rules Readiness
Evaluate whether selection decisions will be consistent by assessing whether inclusion/exclusion criteria are specific and testable (population, setting, study design, interventions/exposures, comparators, outcomes, time period, language), whether ambiguous cases have pre-defined rules (mixed populations, unclear interventions, overlapping datasets), whether the approach to grey literature and preprints is explicit, whether the plan addresses duplicate publications and multiple reports of the same study, whether there is a rule for handling non-English evidence, and whether the team has piloted criteria on a small sample to identify confusion.

A strong score implies different reviewers would make the same decisions given the same abstract/full text.

### 3) Search Strategy & Database Coverage Readiness
Assess whether the search is likely to be comprehensive and reproducible by evaluating whether key concepts are translated into a controlled vocabulary and free-text synonym set, whether Boolean logic is designed to balance recall and precision, whether database choices fit the domain (discipline-specific plus multidisciplinary), whether the plan includes citation chaining and grey literature where needed, whether date limits and filters are justified (not convenience-driven), whether the search syntax is documented per database, and whether the strategy is peer reviewed (e.g., librarian review, PRESS-style review) when appropriate.

A strong score implies another researcher could rerun the search and obtain materially similar results.

### 4) Screening Workflow, Quality Control & Bias Mitigation Readiness
Evaluate whether screening will be reliable by assessing whether the team has a defined workflow (deduplication, title/abstract screening, full-text screening), whether dual screening is planned (or a defensible alternative with verification), whether disagreements are resolved with a defined arbitration process, whether inter-rater agreement will be checked early (to detect drift), whether exclusion reasons are captured in a standardized way, whether the PRISMA flow diagram can be produced from the tracking data, and whether common biases are addressed (language bias, database bias, time-lag bias, selective inclusion).

A strong score implies screening can be executed at scale without losing traceability or consistency.

### 5) Documentation, Registration & Reproducibility Readiness
Assess whether the protocol can be audited by evaluating whether the protocol includes the minimum required sections (rationale, question, eligibility, information sources, selection process, extraction plan, synthesis plan, bias assessment), whether deviations will be tracked and reported, whether versioning is defined, whether data management plans exist (where records live, who has access, backups), and whether the plan includes protocol registration or public posting (PROSPERO, OSF, or equivalent) when appropriate.

A strong score implies the protocol is publication-ready and defensible under peer review.

### 6) Feasibility, Resources & Stakeholder Fit Readiness
Evaluate feasibility by assessing whether timelines and milestones are realistic, whether the team has the right roles covered (content expert, methods lead, librarian/information specialist, statistician if needed), whether software/tooling is selected for screening and tracking, whether stakeholder needs are understood (what outputs they need and when), whether the plan anticipates bottlenecks (full-text retrieval, translation, author contact), and whether the review is sized to the available capacity.

A strong score implies the protocol is not only rigorous but also executable.

---

## Required Output Format

Provide:

1) Executive summary with overall readiness (X.X/5.0), maturity stage, and top 3 blockers.

2) Dimension scorecard with evidence-based rationale.

3) Minimum viable protocol outline (headings and the minimum content required).

4) Search strategy summary including key concepts, example strings, databases, and inclusion of citation chaining/grey literature.

5) Screening and QC plan describing roles, dual review approach, arbitration, and tracking.

6) Risk register (top 10) with mitigation and owner type.

7) Execution plan from protocol finalization → registration → search run → screening → handoff to extraction/synthesis.

---

## Maturity Scale

- 1.0–1.9: Ad-hoc (question and search are unclear; cannot be reproduced)
- 2.0–2.9: Drafting (protocol drafted; criteria/search need piloting and tightening)
- 3.0–3.9: Registrable (scope bounded; search documented; QC defined)
- 4.0–4.9: Execution-ready (piloted and validated; strong tracking and reproducibility)
- 5.0: Gold-standard (peer-reviewed search; strong governance; audit-ready end-to-end)

---

## Variables

| Variable | Description | Examples |
|----------|-------------|----------|
| `{REVIEW_CONTEXT}` | Topic and decision context | "Telehealth interventions for diabetes management", "AI tutoring in K–12" |
| `{REVIEW_METHOD}` | Review type and framing | "Systematic review (PICO)", "Scoping review (PCC)", "Meta-analysis" |
| `{SEARCH_SCOPE}` | Databases, date/language limits, grey literature | "PubMed + Scopus + ERIC; 2015–2025; English+Spanish; include grey literature" |

---

## Usage Example (Single Example)

**Scenario:** A team is planning {REVIEW_CONTEXT}. They intend to run {REVIEW_METHOD} and define {SEARCH_SCOPE}.

**Scores (1–5):** Question & Scope 3.1, Eligibility Rules 2.6, Search Strategy 2.8, Screening/QC 2.4, Documentation/Registration 2.7, Feasibility 2.9. Overall readiness: 2.8/5.0 (Drafting).

**Key findings:** The question is promising but still too broad, and the eligibility criteria are not specific enough to prevent inconsistent screening decisions. The search approach covers major databases but lacks documented database-specific syntax and does not specify how citation chaining and grey literature will be handled. The fastest readiness gains come from piloting eligibility criteria on 50 abstracts, tightening decision rules, and writing a reproducible search appendix that can be rerun and peer reviewed.

---

## Related Resources

- [Literature Review Selection & Quality](education/Academic-Research/literature-review-selection-quality.md)
- [Literature Review Data Extraction & Synthesis](education/Academic-Research/literature-review-extraction-synthesis.md)
- [Literature Reviews Overview](education/Academic-Research/literature-reviews-overview.md)
