---
category: operations
title: Six Sigma & Statistical Quality Excellence Readiness Assessment
tags:
- six-sigma
- dmaic
- statistical-quality
- defect-reduction
- readiness-assessment
use_cases:
- Assessing readiness to implement Six Sigma methodology and statistical quality control
- Identifying gaps in DMAIC capability, SPC deployment, and problem-solving culture
- Improving process capability, reducing defects, and achieving Six Sigma performance
related_templates:
- operations/Manufacturing/quality-management.md
- operations/Manufacturing/lean-manufacturing.md
industries:
- finance
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: six-sigma-readiness-assessment
---

# Six Sigma & Statistical Quality Excellence Readiness Assessment

## Purpose
Assess readiness to **implement Six Sigma methodology** and achieve statistical quality excellence through systematic defect reduction, process capability improvement, and data-driven problem-solving. Use this to diagnose gaps in DMAIC execution, SPC deployment, belt capability, and quality culture.

## Template

Conduct a Six Sigma & statistical quality excellence readiness assessment for {SIX_SIGMA_CONTEXT}.

Score each dimension **1–5** (1 = ad hoc, 5 = optimized). Ground findings in observable signals (sigma level, DPMO, process capability Cp/Cpk, belt count, project completion rate, cost of quality reduction).

**1) DMAIC PROJECT EXECUTION CAPABILITY**
- DMAIC methodology is understood and practiced (Define, Measure, Analyze, Improve, Control)
- Projects are selected based on business impact (Pareto, cost-benefit analysis)
- Project charter discipline exists (problem statement, goals, scope, team, timeline)
- Project completion rate is high (>80% projects complete within 6 months)

**2) STATISTICAL METHODS & SPC DEPLOYMENT**
- Statistical Process Control (SPC) is deployed on critical processes (X-bar R, p-charts)
- Process capability studies are conducted systematically (Cp/Cpk measured, >1.33 target)
- Measurement System Analysis (MSA/GRR) validates gage accuracy (<10% GRR)
- Statistical tools are applied correctly (hypothesis testing, DOE, regression, ANOVA)

**3) BELT CAPABILITY & EXPERTISE**
- Belt infrastructure exists (Black Belts, Green Belts, Yellow Belts certified)
- Black Belts lead complex projects and mentor Green Belts effectively
- Green Belts execute projects within their functional areas successfully
- Training curriculum is comprehensive (statistics, tools, project management, software)

**4) DEFECT REDUCTION & PROCESS IMPROVEMENT**
- Defect rate (DPMO) is measured and trending down systematically
- Root cause analysis is rigorous (5-Whys, fishbone, FMEA, hypothesis testing)
- Corrective actions are validated with data (before/after comparison, statistical significance)
- Process capability improves (Cp/Cpk increases from <1.0 to >1.33 to >1.67)

**5) COST OF QUALITY OPTIMIZATION**
- Cost of Quality (CoQ) is measured (prevention, appraisal, internal failure, external failure)
- CoQ is trending down (target <2% of revenue, best-in-class <1%)
- Investment shifts from appraisal/failure to prevention (proactive vs. reactive)
- Financial benefits from Six Sigma projects are tracked and verified

**6) SIX SIGMA CULTURE & SUSTAINABILITY**
- Leadership demonstrates commitment (sponsor projects, remove barriers, recognize success)
- Six Sigma is integrated into business operations (not standalone program)
- Data-driven decision-making is the norm (facts trump opinions)
- Continuous improvement mindset is embedded (kaizen, problem-solving daily)

---

## Required Output Format (6 Deliverables)

1) **EXECUTIVE SUMMARY**
- Overall maturity level, Six Sigma risks, and key improvement priorities

2) **DIMENSION SCORECARD**
- Table with score (1–5) + 1–2 findings per dimension

3) **QUALITY PERFORMANCE PROFILE**
- Current sigma level, DPMO, process capability (Cp/Cpk), first-pass yield
- Belt count and productivity, project completion rate, cost of quality

4) **DMAIC PROJECT PORTFOLIO ASSESSMENT**
- Active projects by phase (Define, Measure, Analyze, Improve, Control)
- Project selection quality, completion rate, financial impact

5) **STATISTICAL CAPABILITY & SPC STATUS**
- SPC deployment coverage (% of critical processes with SPC)
- Process capability distribution (how many processes Cp/Cpk >1.33)
- MSA/GRR status, statistical tool proficiency

6) **90-DAY SIX SIGMA ACCELERATION PLAN**
- Actions to improve DMAIC execution, SPC deployment, belt training, project selection
- Metrics (sigma level, DPMO, Cp/Cpk, projects completed, CoQ, belt count)

---

## Maturity Scale (Use for Overall + Per-Dimension Scoring)
- 1.0–1.9: Initial (no Six Sigma program, ad hoc quality, 2-3 sigma typical)
- 2.0–2.9: Developing (pilot projects, basic SPC, Green Belt training started)
- 3.0–3.9: Defined (DMAIC practiced, SPC deployed, Black Belts active, 4 sigma achieved)
- 4.0–4.9: Managed (mature Six Sigma, high Cp/Cpk, 5 sigma achieved, embedded culture)
- 5.0: Optimized (world-class 6 sigma, <3.4 DPMO, best-in-class capability)

---

## Variables (≤3)
- {SIX_SIGMA_CONTEXT}: Industry, products, current sigma level/DPMO, quality maturity
- {OBJECTIVES}: Target sigma level, DPMO reduction, Cp/Cpk improvement, CoQ reduction
- {CONSTRAINTS}: Budget, belt expertise, data quality, leadership support

---

## Example (Filled)

**Input**
- {SIX_SIGMA_CONTEXT}: Aerospace components manufacturer (machining, assembly, testing). Products: 8 product families, mix of commercial and defense. Current quality: 3.6 sigma level (25,000 DPMO), 91% first-pass yield, 3.8% cost of quality. Process capability: 40% of critical processes Cp/Cpk <1.0 (not capable), 50% Cp/Cpk 1.0-1.33 (marginal), 10% Cp/Cpk >1.33 (capable). Belt infrastructure: 0 Black Belts, 2 Green Belts (self-taught, no formal training), 0 Yellow Belts. SPC deployed on 15% of critical processes.
- {OBJECTIVES}: Achieve 4.5 sigma level (1,500 DPMO, -94%), 99% FPY (+8%), <2% cost of quality (-47%), 80% of processes Cp/Cpk >1.33. Train and certify 3 Black Belts, 15 Green Belts, 100 Yellow Belts. Complete 20 DMAIC projects in Year 1 with $2M savings target.
- {CONSTRAINTS}: $400K Six Sigma program budget (training, software, consulting); no in-house statistical expertise (need external Black Belt training); customer pressure (aerospace quality standards, AS9100); aging equipment limits process capability; 6-month timeline to show results (CFO skeptical of Six Sigma ROI).

**1) EXECUTIVE SUMMARY**
- Overall maturity: 2.1 (Developing)
- Key risks: 3.6 sigma (25,000 DPMO) = 1 in 40 parts defective, unacceptable for aerospace; 40% of processes not capable (Cp/Cpk <1.0) = high scrap/rework; zero Black Belts = no DMAIC project leadership; 3.8% CoQ ($760K/year on $20M revenue) = waste opportunity
- Top improvements: (1) train and deploy 3 Black Belts to lead DMAIC projects on highest-defect processes, (2) deploy SPC on all critical processes (currently 15%, target 100%), (3) conduct process capability studies and improve Cp/Cpk from <1.0 to >1.33, (4) establish rigorous DMAIC project selection and governance

**2) DIMENSION SCORECARD**
- DMAIC Project Execution: 2/5 — 2 informal improvement projects (not DMAIC), no project charters, no formal methodology, limited data analysis, weak root cause analysis
- Statistical Methods & SPC: 2/5 — SPC on 15% of processes (85% gap), process capability unknown for 60% of processes, no MSA/GRR in 2 years, limited statistical tool proficiency
- Belt Capability & Expertise: 1/5 — 0 Black Belts, 2 Green Belts (self-taught, no certification), 0 Yellow Belts, no training curriculum, statistical expertise very limited
- Defect Reduction & Process Improvement: 2/5 — DPMO 25,000 (3.6 sigma, poor), limited root cause analysis (5-Whys only, no statistical validation), corrective actions not validated with data
- Cost of Quality Optimization: 2/5 — CoQ 3.8% measured but not actively managed, breakdown: prevention 5%, appraisal 20%, internal failure 50%, external failure 25% (too much failure cost)
- Six Sigma Culture & Sustainability: 2/5 — leadership interested but not committed, quality seen as QA department's job (not everyone's), data-driven decision-making limited, firefighting culture dominates

**3) QUALITY PERFORMANCE PROFILE**
- Current sigma level & DPMO:
  - Sigma level: 3.6 (industry avg 4.0, aerospace target 5.0+)
  - DPMO: 25,000 (25,000 defects per million opportunities)
  - Defect rate: 2.5% (1 in 40 parts defective)
  - Top defects: dimensional out-of-spec (40%), surface finish (25%), assembly errors (20%), material defects (15%)
- Process capability (Cp/Cpk):
  - Not capable (Cp/Cpk <1.0): 40% of critical processes (16 of 40) — high defect risk, constant firefighting
    - Examples: CNC dimension Cpk 0.78, surface roughness Cpk 0.65, heat treat hardness Cpk 0.92
  - Marginally capable (Cp/Cpk 1.0-1.33): 50% of processes (20 of 40) — some defects, improvement needed
    - Examples: drilling position Cpk 1.15, torque Cpk 1.22, coating thickness Cpk 1.08
  - Capable (Cp/Cpk >1.33): 10% of processes (4 of 40) — low defect risk, good performance
    - Examples: visual inspection Cpk 1.45, packaging Cpk 1.62
  - Target: 80% of processes Cp/Cpk >1.33 (32 of 40)
- First-pass yield: 91% (9% scrap/rework = $360K/year internal failure cost)
- Cost of Quality: 3.8% of revenue ($760K on $20M revenue)
  - Prevention: $38K (5% of CoQ) — underfunded, should be 15-20%
  - Appraisal: $152K (20% of CoQ) — inspection, testing
  - Internal failure: $380K (50% of CoQ) — scrap, rework, re-inspection
  - External failure: $190K (25% of CoQ) — customer returns, warranty, sorting, containment
- Belt count and productivity:
  - Black Belts: 0 (target 3, need to train)
  - Green Belts: 2 (self-taught, no certification, limited effectiveness)
  - Yellow Belts: 0 (target 100)
  - Projects completed: 2 informal projects in past year (not DMAIC, limited rigor)
  - Financial impact: $50K savings claimed (not validated)
- SPC deployment coverage:
  - Critical processes identified: 40
  - SPC deployed: 6 processes (15%)
  - Gap: 34 processes lacking SPC (85%)

**4) DMAIC PROJECT PORTFOLIO ASSESSMENT**
- Active projects by phase:
  - Define: 0 projects (need to launch first wave of 5-8 projects)
  - Measure: 0 projects
  - Analyze: 1 project (CNC dimension variation—informal, not following DMAIC)
  - Improve: 1 project (surface finish improvement—testing new parameters)
  - Control: 0 projects (no projects have reached Control phase)
- Project selection quality: 2/5
  - Current: ad hoc, based on loudest complaint or customer pressure
  - No Pareto analysis of defect costs
  - No business case or ROI calculation
  - No alignment with strategic priorities
  - Recommended: conduct Pareto analysis, select top 5-8 projects by financial impact (target $200K+ savings each)
- Project completion rate: N/A (no formal DMAIC projects tracked)
  - Target: >80% of projects complete within 6 months
- Financial impact:
  - Current: $50K savings claimed (2 informal projects, not validated)
  - Target Year 1: $2M savings (20 DMAIC projects × $100K avg = $2M)
  - Validation needed: before/after data, statistical significance testing

**5) STATISTICAL CAPABILITY & SPC STATUS**
- SPC deployment coverage:
  - Current: 6 of 40 critical processes (15%)
    - CNC critical dimension: X-bar R chart, manual plotting, Cpk 0.78 (not capable)
    - Surface roughness: X-bar R chart, Cpk 0.65 (not capable)
    - Heat treat hardness: X-bar R chart, Cpk 0.92 (marginal)
    - Assembly torque: X-bar R chart, Cpk 1.22 (marginal)
    - Coating thickness: X-bar R chart, Cpk 1.08 (marginal)
    - Visual inspection: p-chart, Cpk 1.45 (capable)
  - Target: 40 of 40 processes (100%)
  - Gap: 34 processes need SPC deployment (prioritize by defect cost)
- Process capability distribution:
  - Cp/Cpk studies completed: 16 of 40 processes (40%)
  - Gap: 24 processes need capability studies (60%)
  - Distribution:
    - <1.0 not capable: 16 processes (40%) — urgent improvement needed
    - 1.0-1.33 marginal: 20 processes (50%) — improvement needed
    - >1.33 capable: 4 processes (10%) — maintain performance
    - >1.67 highly capable: 0 processes (0%) — stretch goal
- MSA/GRR status:
  - Last GRR studies: 2 years ago (outdated)
  - Known issues: caliper GRR 18% (target <10%), CMM GRR 12% (marginal), hardness tester GRR unknown
  - Recommendation: conduct GRR on all 10 critical measurement systems, replace/repair gages with >10% GRR
- Statistical tool proficiency:
  - Current: 5-Whys (basic), fishbone (basic), Pareto (basic), control charts (limited)
  - Gap: hypothesis testing, DOE, regression, ANOVA, confidence intervals, statistical software (Minitab)
  - Training needed: Black Belt 4 weeks (160 hours), Green Belt 2 weeks (80 hours), Yellow Belt 1 day (8 hours)

**6) 90-DAY SIX SIGMA ACCELERATION PLAN**
- 30 days: select and train 3 Black Belt candidates (send to external 4-week training, Minitab certification); conduct Pareto analysis of defects by cost (identify top 20 improvement opportunities); select first 5 DMAIC projects (charter discipline: problem statement, baseline DPMO, target improvement, business case $200K+ each, team assigned); deploy SPC on 5 additional critical processes (prioritize highest-defect processes, train operators on control chart interpretation)
- 60 days: Black Belts complete training and return (lead first wave of 5 DMAIC projects); train 8 Green Belts (2-week course, support Black Belt projects); conduct process capability studies on 10 additional processes (measure Cp/Cpk, identify improvement opportunities); conduct MSA/GRR on 5 critical measurement systems (calipers, CMM, hardness tester, profilometer, torque wrench—ensure <10% GRR)
- 90 days: measure sigma level (baseline 3.6, goal 3.8 via first DMAIC improvements = 17,000 DPMO, -32%), process capability improvement (baseline 10% Cpk >1.33, goal 20% = 8 of 40 processes improved to capable), projects in progress (goal 5 DMAIC projects Define/Measure phase complete, Analyze phase started), belt count (goal 3 Black Belts trained, 8 Green Belts trained), SPC deployment (baseline 15%, goal 40% = 16 of 40 processes with SPC)
- Metrics to track: sigma level (goal 3.8 by 90 days, 4.5 by 12 months), DPMO (goal 17,000 by 90 days, 1,500 by 12 months), Cp/Cpk distribution (goal 20% capable by 90 days, 80% by 12 months), projects completed (goal 5 in Analyze phase by 90 days, 20 completed by 12 months), CoQ (goal 3.2% by 90 days, <2% by 12 months), belt count (goal 3 BB + 8 GB by 90 days, 3 BB + 15 GB + 100 YB by 12 months)

---

## Best Practices (Exactly 8)
1) Select projects by financial impact: Pareto analysis ranks defects by cost; focus Black Belts on $200K+ opportunities, not small irritations.
2) Follow DMAIC rigorously: Define problem with data, Measure baseline, Analyze root cause statistically, Improve with validated solutions, Control with SPC—shortcuts fail.
3) Deploy SPC on all critical processes: X-bar R charts detect variation early, prevent defects before they escape; target Cp/Cpk >1.33 (capable), >1.67 (highly capable).
4) Invest in Black Belt training: external 4-week certification builds statistical expertise; self-taught Green Belts lack rigor for complex projects.
5) Validate measurement systems first: if GRR >10%, you're measuring noise not signal; fix gages before capability studies or you'll chase ghosts.
6) Shift CoQ from failure to prevention: reduce appraisal/failure costs (reactive), increase prevention costs (training, poka-yoke, FMEA)—ROI is 10:1+.
7) Make Six Sigma part of business, not a program: integrate DMAIC into strategic planning, operations reviews, and performance management—not a side project.
8) Celebrate data-driven wins: recognize belt projects that deliver savings, improve capability, reduce defects—visible success builds culture and momentum.
