---
category: education
related_templates:
- education/Academic-Research/literature-review-protocol-search.md
- education/Academic-Research/literature-review-extraction-synthesis.md
- education/Academic-Research/literature-reviews-overview.md
tags:
- study-selection
- quality-assessment
- bias-evaluation
- prisma-screening
- capability-assessment
title: Literature Review Selection & Quality Assessment Readiness Assessment
use_cases:
- Evaluating readiness to screen studies consistently and defend inclusion decisions
- Planning quality assessment and bias evaluation with pre-defined criteria
- Producing PRISMA-compliant flow diagrams and audit trails
- Creating defensible study sets ready for extraction and synthesis
industries:
- education
- government
- healthcare
- technology
type: framework
difficulty: intermediate
slug: literature-review-selection-quality
---

# Literature Review Selection & Quality Assessment Readiness Assessment

## Purpose
Assess whether a review team is ready to screen, select, and quality-assess studies in a way that is consistent, auditable, and defensible under peer review. This framework helps you avoid the common failure mode where screening decisions cannot be reproduced, quality assessments are inconsistent, and PRISMA flow diagrams cannot be constructed from available tracking data.

## Template

Conduct a selection and quality assessment readiness assessment for {REVIEW_CONTEXT} screening {STUDY_VOLUME} using {SELECTION_TOOLS}.

Score each dimension from 1.0 to 5.0 and justify scores with concrete artifacts (eligibility criteria decision rules, piloted screening results, quality assessment rubrics, inter-rater agreement checks, PRISMA flow mockup, and a realistic timeline).

### 1) Eligibility Criteria Operationalization & Testability Readiness
Assess whether screening decisions will be consistent by evaluating whether eligibility criteria are testable from titles/abstracts and full texts (not requiring information that studies typically do not report), whether each PICO/PEO element has decision rules for ambiguous cases, whether edge cases have been piloted and resolved, whether "unclear" is minimized by defining what counts as sufficient information, whether exclusion reasons are mutually exclusive and collectively exhaustive, and whether the team can demonstrate that two screeners would independently reach the same decision on sample studies.

A strong score implies eligibility criteria are precise enough that screening can scale without "criteria drift."

### 2) Screening Workflow, Dual Review & Tracking Readiness
Evaluate whether screening can be executed reliably by assessing whether the workflow is defined (deduplication → title/abstract → full-text → included set), whether dual review is planned for at least a subset with a defined sampling or coverage strategy, whether disagreements are resolved with a documented process (discussion, arbitration, tie-breaker rules), whether exclusion reasons are captured in a standardized taxonomy, whether the tracking system can produce PRISMA flow counts at each stage, and whether inter-rater agreement will be checked early enough to correct problems.

A strong score implies the team can run screening at scale with quality controls that detect and correct inconsistency.

### 3) Quality & Bias Assessment Tool Selection & Reliability Readiness
Assess whether quality/bias assessment will be defensible by evaluating whether the correct tool is selected for study designs in scope (RoB2 for RCTs, ROBINS-I for observational, CASP for qualitative, etc.), whether domain scoring is operationalized with examples, whether the tool output can feed into certainty rating (e.g., GRADE), whether dual assessment or verification is planned, whether inter-rater reliability will be calculated and is likely to be acceptable, and whether the team has piloted the tool to surface ambiguities.

A strong score implies quality assessment will be reproducible and the results will be credible for downstream synthesis and recommendations.

### 4) Documentation, PRISMA Compliance & Auditability Readiness
Evaluate whether the process is audit-ready by assessing whether deduplication methods and counts are documented, whether excluded full texts can be listed with reasons, whether the PRISMA flow diagram can be populated from tracking data (no manual reconstruction), whether screening decisions are timestamped and versioned, whether the final included set has stable study IDs that link to extraction, and whether quality assessment ratings are traceable to justifications.

A strong score implies peer reviewers and readers can verify the selection process without relying on memory or missing records.

### 5) Discrepancy Resolution, Arbitration & Consensus Readiness
Assess whether disagreements will be handled systematically by evaluating whether the arbitration process is defined (who resolves, what evidence is required), whether the team can escalate unclear cases without stalling, whether resolution decisions are logged and can inform criteria refinement, whether the process avoids "voting" (which hides reasons), and whether resolved decisions can be reviewed later to check for patterns or biases in resolution.

A strong score implies the team has a fair and transparent process that maintains trust and prevents criteria erosion over time.

### 6) Feasibility, Timeline & Reviewer Training Readiness
Evaluate feasibility by assessing whether the timeline accounts for realistic screening rates (titles/abstracts: ~100–500/hour; full texts: ~5–20/hour depending on complexity), whether reviewer training includes calibration exercises, whether the team has contingency plans for delays (full-text retrieval, translation), whether roles are clear (who screens, who arbitrates, who manages tracking), and whether the workload is balanced and sustainable.

A strong score implies the plan is executable within the available time and capacity, with minimal risk of burnout or corner-cutting.

---

## Required Output Format

Provide:

1) Executive summary with overall readiness (X.X/5.0), maturity stage, and top 3 blockers.

2) Dimension scorecard with brief evidence.

3) Minimum viable screening checklist (eligibility rules, exclusion taxonomy, arbitration process).

4) Quality/bias assessment tool selection with domain definitions and scoring examples.

5) PRISMA flow mockup showing expected counts at each stage and how tracking will populate it.

6) Risk register (top 10) with mitigation and owner.

7) Execution plan from deduplication → title/abstract screening → full-text screening → quality assessment → handoff to extraction.

---

## Maturity Scale

- 1.0–1.9: Ad-hoc (vague criteria; no QC; inconsistent decisions)
- 2.0–2.9: Developing (criteria drafted; QC planned but not piloted)
- 3.0–3.9: Operational (criteria tested; dual review and tracking functional)
- 4.0–4.9: Rigorous (high inter-rater agreement; audit-ready documentation)
- 5.0: Gold-standard (validated tools; transparent audit trail; exemplary PRISMA compliance)

---

## Variables

| Variable | Description | Examples |
|----------|-------------|----------|
| `{REVIEW_CONTEXT}` | Topic and scope of the review | "Telehealth for diabetes", "School-based mental health" |
| `{STUDY_VOLUME}` | Expected screening load | "~5,000 records → ~500 full texts → ~50 included", "~1,200 records total" |
| `{SELECTION_TOOLS}` | Screening and quality tools | "Covidence + RoB2 + GRADE", "Rayyan + Newcastle-Ottawa Scale" |

---

## Usage Example (Single Example)

**Scenario:** A team is conducting {REVIEW_CONTEXT} and must screen {STUDY_VOLUME} using {SELECTION_TOOLS}.

**Scores (1–5):** Eligibility Operationalization 2.7, Screening Workflow/Tracking 2.5, Quality/Bias Tool 2.9, Documentation/PRISMA 2.4, Discrepancy Resolution 2.6, Feasibility/Training 2.8. Overall readiness: 2.7/5.0 (Developing).

**Key findings:** Eligibility criteria exist but are not operationalized for edge cases (e.g., mixed populations, unclear interventions), which will cause inconsistent screening. The tracking plan relies on a spreadsheet that cannot easily produce PRISMA flow counts, increasing error risk. Quality assessment tool selection is appropriate, but the team has not piloted it to check inter-rater reliability. The fastest readiness gains are to pilot screening on 50 records, tighten decision rules, migrate tracking to a purpose-built tool (Covidence/Rayyan), and run a quality assessment calibration session.

---

## Related Resources

- [Literature Review Protocol & Search Strategy](education/Academic-Research/literature-review-protocol-search.md)
- [Literature Review Data Extraction & Synthesis](education/Academic-Research/literature-review-extraction-synthesis.md)
- [Literature Reviews Overview](education/Academic-Research/literature-reviews-overview.md)
