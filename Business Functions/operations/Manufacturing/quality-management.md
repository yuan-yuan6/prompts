---
category: operations
title: Quality Management System Readiness Assessment
tags:
- quality-management
- iso-standards
- quality-assurance
- continuous-improvement
- readiness-assessment
use_cases:
- Assessing readiness to implement or improve quality management systems
- Identifying gaps in quality processes, supplier quality, and regulatory compliance
- Improving first-pass yield, defect rates, and cost of quality
related_templates:
- operations/Manufacturing/lean-manufacturing.md
- operations/Manufacturing/production-planning.md
industries:
- finance
- government
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: quality-management-readiness-assessment
---

# Quality Management System Readiness Assessment

## Purpose
Assess readiness to **implement world-class quality management system** that ensures product quality, regulatory compliance, customer satisfaction, and continuous improvement. Use this to diagnose gaps in quality processes, statistical control, supplier quality, and quality culture.

## 🚀 Quick Assessment Prompt

> Assess **quality management system readiness** for {QUALITY_CONTEXT}. The quality objectives are {OBJECTIVES}. Account for {CONSTRAINTS}. Score 1–5 across the six dimensions below and produce the required output (six deliverables).

---

## Template

Conduct a quality management system readiness assessment for {QUALITY_CONTEXT}.

Score each dimension **1–5** (1 = ad hoc, 5 = optimized). Ground findings in observable signals (PPM defect rate, first-pass yield, cost of quality %, ISO certification status, customer complaints, CAPA effectiveness).

**1) QUALITY SYSTEM FOUNDATION & ISO COMPLIANCE**
- Quality policy, objectives, and manual are documented and communicated
- ISO 9001 (or industry-specific ISO/IATF/AS) compliance level is adequate
- Documented procedures and work instructions exist and are followed
- Internal audits are conducted regularly and drive improvement

**2) PROCESS QUALITY CONTROL & SPC**
- Critical processes are identified and controlled (control plans, SPC)
- Statistical Process Control (SPC) is deployed on key characteristics
- Process capability is measured and improved (Cp/Cpk targets achieved)
- Measurement system analysis (MSA/GRR) validates gage accuracy and precision

**3) SUPPLIER QUALITY MANAGEMENT**
- Supplier selection and qualification processes are rigorous
- Supplier performance is measured and managed (PPM, OTD, CAPA response)
- Incoming inspection is risk-based and effective (AQL, skip-lot where appropriate)
- Supplier development improves capability and reduces defects

**4) CUSTOMER QUALITY & SATISFACTION**
- Customer requirements are translated into product/process specs accurately
- Customer satisfaction is measured systematically (surveys, NPS, complaints)
- Customer complaints are resolved rapidly (CAPA, root cause, corrective action)
- Field quality data (returns, warranty) is analyzed and drives improvement

**5) DEFECT PREVENTION & PROBLEM-SOLVING**
- Quality is built in, not inspected in (poka-yoke, jidoka, mistake-proofing)
- Root cause analysis is systematic and effective (5-Whys, fishbone, 8D, FMEA)
- Corrective/Preventive Action (CAPA) system drives continuous improvement
- Quality culture emphasizes prevention over detection (stop-the-line authority, empowerment)

**6) QUALITY PERFORMANCE & COST OF QUALITY**
- First-pass yield (FPY) is high and improving (target 99%+)
- Defect rate (PPM) is competitive and trending down (target <500 PPM)
- Cost of Quality (CoQ) is measured and optimized (target <2% of sales)
- Quality metrics are visible, reviewed, and drive action (daily/weekly reviews)

---

## Required Output Format (6 Deliverables)

1) **EXECUTIVE SUMMARY**
- Overall maturity level, quality risks, and key improvement priorities

2) **DIMENSION SCORECARD**
- Table with score (1–5) + 1–2 findings per dimension

3) **QUALITY PERFORMANCE PROFILE**
- PPM defect rate, first-pass yield, cost of quality (COPQ), scrap/rework rates
- Customer complaints, CAPA effectiveness, supplier quality

4) **ISO & COMPLIANCE ASSESSMENT**
- ISO 9001 (or industry-specific standard) compliance gaps
- Regulatory compliance status, certification readiness

5) **PROCESS CAPABILITY & CONTROL**
- Critical process identification, SPC deployment, Cp/Cpk values
- MSA/GRR status, control plan effectiveness

6) **90-DAY QUALITY EXCELLENCE ACCELERATION PLAN**
- Actions to improve process control, supplier quality, defect prevention, CAPA effectiveness
- Metrics (PPM, FPY, CoQ, customer complaints, CAPA closure rate)

---

## Maturity Scale (Use for Overall + Per-Dimension Scoring)
- 1.0–1.9: Initial (inspect-in quality, reactive firefighting, no formal QMS)
- 2.0–2.9: Developing (some procedures, basic quality control, pursuing ISO certification)
- 3.0–3.9: Defined (ISO certified, SPC deployed, solid CAPA system, good FPY)
- 4.0–4.9: Managed (advanced quality methods, low defects, strong supplier quality, cost of quality optimized)
- 5.0: Optimized (world-class quality, Six Sigma culture, <100 PPM, benchmark performance)

---

## Variables (≤3)
- {QUALITY_CONTEXT}: Manufacturing type, products, quality standards, current quality metrics
- {OBJECTIVES}: PPM, FPY, cost of quality, ISO certification, customer satisfaction targets
- {CONSTRAINTS}: Budget, quality staffing, supplier maturity, regulatory requirements

---

## Example (Filled)

**Input**
- {QUALITY_CONTEXT}: Medical device contract manufacturer (Class II devices). Products: surgical instruments, diagnostic equipment components. Regulatory: FDA 21 CFR Part 820 (QSR), ISO 13485 required. Current metrics: 2,800 PPM defect rate (industry avg 1,000 PPM, best-in-class <200 PPM), 92% first-pass yield (target 99%), 4.2% cost of quality (target <2%), 18 customer complaints/month (causing audit scrutiny). ISO 13485 certification lapsed 2 years ago (customer requirement to recertify within 12 months). 140 employees, 45 suppliers (12 critical).
- {OBJECTIVES}: Achieve <500 PPM defects (-82%), 99% FPY (+7%), <2% cost of quality (-52%), recertify ISO 13485 within 12 months, reduce customer complaints to <5/month (-72%). Pass pending FDA audit (scheduled in 6 months).
- {CONSTRAINTS}: $600K quality improvement budget; 3-person quality team (overworked, limited SPC expertise); supplier quality weak (8 of 12 critical suppliers have quality issues); aging equipment (measurement system accuracy concerns); FDA audit pressure (non-compliance risk = loss of customers).

**1) EXECUTIVE SUMMARY**
- Overall maturity: 2.5 (Developing)
- Key risks: 2,800 PPM defect rate drives customer complaints and rework costs; ISO 13485 lapse = customer audit findings, potential loss of business; FDA audit in 6 months with known gaps (CAPA effectiveness, process validation, supplier audits); cost of quality 4.2% = $840K/year waste on $20M revenue
- Top improvements: (1) establish robust CAPA system with root cause analysis and effectiveness checks, (2) deploy SPC on critical processes to improve process capability, (3) implement supplier audit and development program to reduce incoming defects, (4) prepare for ISO 13485 recertification (gap remediation, documentation, internal audits)

**2) DIMENSION SCORECARD**
- Quality System Foundation & ISO: 2/5 — ISO 13485 lapsed, documentation incomplete (50% of procedures outdated), internal audits infrequent (annual vs. required quarterly), training records incomplete
- Process Quality Control & SPC: 2/5 — SPC deployed on <10% of critical processes, process capability unknown (no Cp/Cpk studies in 3 years), control plans exist but not followed consistently
- Supplier Quality Management: 2/5 — 8 of 12 critical suppliers have quality issues (>1,000 PPM), incoming inspection detects 40% of supplier defects (should be <10%), no supplier audits in 2 years
- Customer Quality & Satisfaction: 3/5 — customer complaints 18/month (high), CAPA closure avg 90 days (target 30 days), complaint root causes repeat (systemic issues not fixed)
- Defect Prevention & Problem-Solving: 2/5 — quality inspected in, not built in; limited poka-yoke devices; root cause analysis superficial (5-Whys done, but corrective actions weak); quality culture reactive
- Quality Performance & CoQ: 2/5 — 2,800 PPM (3x industry avg), 92% FPY (7% scrap/rework = $840K/year), CoQ 4.2% (target <2%), metrics not visible (monthly reports, no daily review)

**3) QUALITY PERFORMANCE PROFILE**
- Current metrics:
  - PPM defect rate: 2,800 (parts per million shipped defective)
    - Breakdown: internal defects caught 5,200 PPM (scrap/rework), external defects 2,800 PPM (customer complaints, returns)
    - Total defect generation: 8,000 PPM (internal + external)
    - Top defects: dimensional variation (40%), surface finish (25%), assembly errors (20%), material defects (15%)
  - First-pass yield: 92% (8% scrap/rework rate)
    - Best process: final inspection 98% FPY (but too late—defects already created)
    - Worst process: CNC machining 85% FPY (dimensional variation, tool wear, setup errors)
    - Assembly: 90% FPY (missing parts, incorrect torque, sequence errors)
    - Packaging: 95% FPY (labeling errors, damage)
  - Cost of Quality (COPQ): 4.2% of sales ($840K on $20M revenue)
    - Prevention costs: $80K (1% of CoQ—underfunded, should be 15-20%)
    - Appraisal costs: $200K (24% of CoQ—inspection, testing, audits)
    - Internal failure: $400K (48% of CoQ—scrap, rework, re-inspection)
    - External failure: $160K (19% of CoQ—returns, warranty, complaint investigation, customer visits)
    - Opportunity: reduce CoQ to <2% ($400K) = save $440K/year
  - Scrap/rework rates:
    - Scrap: 3% of production ($600K material + labor write-off)
    - Rework: 5% of production ($400K labor + overhead)
    - Target: <1% scrap, <2% rework (99% FPY)
  - Customer complaints: 18/month avg (range 10-28)
    - Top complaints: dimensional out-of-spec (40%), cosmetic defects (30%), functional failures (20%), packaging/documentation (10%)
    - Response time: avg 10 days to initial response (target 48 hours)
    - CAPA closure: avg 90 days (target 30 days), 35% effectiveness rate (measured by recurrence)
  - Supplier quality:
    - Incoming inspection defect rate: 4,000 PPM (40% of total defects come from suppliers)
    - Top supplier issues: dimensional variation (45%), material properties (30%), contamination (15%), packaging (10%)
    - 8 of 12 critical suppliers on corrective action (>1,000 PPM each)
    - Supplier CAPA response: avg 60 days (slow), limited root cause analysis

**4) ISO & COMPLIANCE ASSESSMENT**
- ISO 13485 compliance status:
  - Certification: lapsed 2 years ago (customer requirement to recertify within 12 months)
  - Last audit findings (2 years ago): 8 major non-conformances, 22 minor
    - Major NCs: CAPA effectiveness, design validation, process validation, supplier audits, calibration, training, document control, management review
  - Gap assessment (current state vs. ISO 13485 requirements):
    - Clause 4 (QMS): 60% compliant — quality manual outdated, procedures incomplete, records gaps
    - Clause 5 (Management): 70% compliant — management review irregular, quality objectives not measurable
    - Clause 6 (Resource): 65% compliant — training records incomplete, infrastructure aging
    - Clause 7 (Product Realization): 55% compliant — design controls weak, process validation missing, purchasing controls inadequate
    - Clause 8 (Measurement): 60% compliant — CAPA system ineffective, internal audits infrequent, data analysis limited
- FDA QSR (21 CFR Part 820) compliance status:
  - FDA audit scheduled in 6 months (triggered by customer complaints)
  - Known gaps (from mock audit 3 months ago):
    - §820.100 CAPA: weak root cause analysis, corrective actions not effective (recurrence rate high)
    - §820.75 Process validation: 40% of processes not validated (or validation outdated >5 years)
    - §820.50 Purchasing: supplier audits not current (>3 years old), incoming inspection inadequate
    - §820.72 Inspection: measurement system accuracy not validated (no MSA/GRR in 3 years)
    - §820.180 Records: training records incomplete (30% of operators missing required training documentation)
  - Risk: FDA warning letter or consent decree if major gaps not remediated
- Certification readiness: 6-9 months to recertify (with focused effort and investment)
  - Critical path: CAPA effectiveness, process validation, supplier audits, document control, training

**5) PROCESS CAPABILITY & CONTROL**
- Critical process identification:
  - 15 critical processes identified (CNC machining, welding, heat treatment, plating, assembly, sterilization, etc.)
  - Risk analysis (FMEA) completed for 10 of 15 processes (33% missing)
  - Control plans exist for all 15, but adherence inconsistent (spot-checks show 60% compliance)
- SPC deployment:
  - Current: SPC deployed on 2 of 15 critical processes (13%)
    - Process 1 (CNC machining—critical dimension): X-bar R chart, manual plotting, Cpk 1.15 (marginal)
    - Process 2 (hardness testing): X-bar R chart, manual plotting, Cpk 1.42 (capable)
  - Gap: 13 of 15 critical processes lack SPC (87% gap)
  - Opportunity: deploy SPC on top 8 processes (cover 80% of defects) = improve capability, reduce variation
- Process capability (Cp/Cpk):
  - Measured on 4 of 15 critical processes (27%)
    - CNC machining (critical dimension): Cpk 1.15 (marginal, 3.4 sigma = 1,350 PPM expected)
    - Hardness testing: Cpk 1.42 (capable)
    - Surface roughness: Cpk 0.85 (not capable, out-of-spec risk)
    - Assembly torque: Cpk 1.10 (marginal)
  - Target: Cpk >1.33 (capable, <64 PPM expected), Cpk >1.67 (highly capable, <0.6 PPM expected)
  - Gap: 11 of 15 processes have unknown capability (need studies)
- Measurement System Analysis (MSA/GRR):
  - Last GRR study: 3 years ago (outdated, equipment and operators changed)
  - Known issues: calipers out-of-calibration (15% past due), gage variation suspected (operators get different readings)
  - Gap: conduct GRR on 10 critical measurement systems (ensure <10% GRR, 30% target)
- Control plan effectiveness:
  - Control plans exist for all 15 critical processes (documented)
  - Adherence: spot-checks show 60% compliance (operators skip steps, data not recorded)
  - Gap: reinforce training, simplify data collection, add visual controls, audit compliance weekly

**6) 90-DAY QUALITY EXCELLENCE ACCELERATION PLAN**
- 30 days: establish CAPA effectiveness criteria (require root cause analysis, corrective action validation, effectiveness check 90 days post-implementation); conduct process capability studies on top 5 defect-generating processes (CNC machining, welding, heat treatment, plating, assembly—measure Cpk, identify improvement opportunities); launch supplier quality initiative (audit top 3 suppliers with quality issues, issue CARs, establish improvement plans); update quality manual and critical procedures for ISO 13485 (engage consultant if needed)
- 60 days: deploy SPC on top 3 critical processes (CNC machining, welding, heat treatment—install SPC software, train operators, establish reaction plans); conduct MSA/GRR on 5 critical measurement systems (calipers, hardness tester, CMM, torque wrench, profilometer—ensure <10% GRR); improve CAPA closure time (assign owner, weekly reviews, 30-day target); complete internal audits for all ISO 13485 clauses (identify gaps, assign corrective actions)
- 90 days: measure PPM defect rate (baseline 2,800, goal 1,500 = -46% via SPC + CAPA), FPY (baseline 92%, goal 95% via process capability improvement), CoQ (baseline 4.2%, goal 3.0% via scrap/rework reduction), customer complaints (baseline 18/month, goal 12/month via CAPA effectiveness), CAPA closure time (baseline 90 days, goal 45 days = 50% faster), ISO 13485 gap closure (goal 80% of major NCs closed)
- Metrics to track: PPM (goal 1,500 by 90 days, <500 by 12 months), FPY (goal 95% by 90 days, 99% by 12 months), CoQ (goal 3.0% by 90 days, <2% by 12 months), customer complaints (goal 12/month by 90 days, <5/month by 12 months), CAPA closure (goal 45 days by 90 days, 30 days by 6 months), ISO 13485 recertification (goal audit-ready in 9 months, certified in 12 months)

---

## Best Practices (Exactly 8)
1) Build quality in, don't inspect it in: poka-yoke devices, jidoka (stop-the-line), and mistake-proofing prevent defects better than inspection catches them.
2) Deploy SPC on critical processes: statistical control (X-bar R charts, Cp/Cpk) identifies variation early and prevents defects before they escape.
3) Require robust root cause analysis: 5-Whys alone is insufficient; use fishbone, 8D, FMEA to dig deep and prevent recurrence.
4) Measure CAPA effectiveness: 30% of CAPAs fail (defects recur); validate corrective actions with data (before/after PPM) and effectiveness checks.
5) Optimize cost of quality: shift spend from appraisal and failure (reactive) to prevention (proactive)—invest in training, poka-yoke, process improvement.
6) Audit and develop suppliers: 40-60% of defects come from suppliers; audit critical suppliers annually, issue CARs, develop capability systematically.
7) Make quality visible: daily quality boards (PPM, FPY, top defects, CAPA status) drive urgency and accountability better than monthly reports.
8) Pursue ISO/industry certification: ISO 9001/13485/IATF 16949 discipline improves quality maturity; certification opens doors to customers and drives continuous improvement.
