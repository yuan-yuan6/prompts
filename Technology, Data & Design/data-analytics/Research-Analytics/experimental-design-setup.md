---
category: data-analytics
description: Configure experimental designs including RCTs, A/B tests, factorial, crossover, cluster trials, stepped-wedge, quasi-experimental, and regression discontinuity designs
title: Experimental Design Setup
tags:
- experimental-design
- rct
- ab-testing
- research-analytics
use_cases:
- Configuring randomized controlled trials with stratification and allocation concealment
- Setting up A/B and multivariate tests with proper traffic allocation
- Designing factorial experiments to test multiple factors and interactions
- Planning cluster randomized trials accounting for intracluster correlation
related_templates:
- data-analytics/Research-Analytics/experimental-design-overview.md
- data-analytics/Research-Analytics/randomization-and-power-analysis.md
- data-analytics/Research-Analytics/treatment-effect-analysis.md
- data-analytics/Research-Analytics/validity-and-diagnostics.md
industries:
- healthcare
- technology
- education
- government
- finance
type: framework
difficulty: intermediate
slug: experimental-design-setup
---

# Experimental Design Setup

## Purpose
Configure the appropriate experimental design structure for your research objectives. This framework guides setup for eight design types—randomized controlled trials, A/B tests, factorial designs, crossover designs, cluster randomized trials, stepped-wedge designs, quasi-experimental designs, and regression discontinuity designs—with complete specifications for randomization, allocation, and implementation.

## Template

Configure a complete experimental design for {RESEARCH_OBJECTIVE}, testing {TREATMENT_INTERVENTION} with {STUDY_PARAMETERS}.

**1. Design Type Selection and Configuration**

Select and configure the experimental design that best matches your research context. For individual-level randomization testing a single intervention, configure a standard randomized controlled trial (RCT) specifying total sample size, treatment-to-control allocation ratio (commonly 1:1 but consider 2:1 if treatment assessment is more informative), and whether parallel or crossover structure suits your outcomes. For digital experiments with large user bases, configure an A/B test (or A/B/n for multiple variants) specifying variants, traffic allocation percentages, and randomization unit (user ID for persistent experiences, session for independent interactions). For testing multiple interventions simultaneously, configure a factorial design specifying factors, levels per factor, and whether full factorial (all combinations) or fractional factorial (subset of combinations) is needed. Document your design choice with explicit configuration parameters and rationale for key decisions.

**2. Treatment and Control Specification**

Define treatment and control conditions with operational precision. For treatment conditions, specify the intervention components, dosage or intensity, duration, delivery mechanism, and who delivers it. Create implementation protocols ensuring consistent delivery across sites, providers, or time periods. For control conditions, specify exactly what controls receive—placebo (inert substitute matching treatment appearance), active control (alternative intervention), treatment as usual (document what usual care entails), or waitlist (delayed treatment access). Consider attention placebo controls when treatment involves human interaction to separate specific effects from attention effects. For factorial designs, specify each factor level with the same operational detail. Document any treatment variations allowed (flexibility) versus required standardization (fidelity), and plan measurement of treatment fidelity.

**3. Randomization Scheme Design**

Design the randomization procedure that will create comparable groups. Simple randomization (independent random assignment like coin flips) works for large samples but can create imbalance in smaller studies—use when N > 200 per arm. Block randomization ensures equal allocation within sequential blocks—specify block sizes (typically 4-8, or random varying blocks to prevent prediction). Stratified randomization first divides participants by key prognostic factors then randomizes within strata—limit to 2-3 stratification variables to avoid sparse cells. For cluster designs, specify cluster-level randomization with stratification by cluster characteristics. Design allocation concealment ensuring those enrolling participants cannot predict assignments—use centralized computer randomization, sequentially numbered sealed envelopes, or pharmacy-controlled allocation. Specify who generates the sequence, who enrolls, and who assigns—ideally separate individuals.

**4. Factorial Design Configuration**

For factorial designs, configure the factor structure and analysis approach. Specify each factor with its levels—for a 2×2 design, name both factors (e.g., drug A presence/absence, drug B presence/absence) creating four conditions. Calculate participants per cell needed for adequate power on main effects and interactions—interactions typically require 4x the sample size of main effects for equivalent power. Decide between full factorial (all combinations, most informative) versus fractional factorial (subset of combinations, more efficient but aliases some effects). Plan the analysis model specifying main effects and which interactions to test. For more than two factors, prioritize hypotheses—three-way and higher interactions are rarely interpretable and require enormous samples. Document the design matrix showing all conditions with participant allocation targets.

**5. Crossover Design Configuration**

For within-subject designs where participants receive multiple treatments, configure crossover parameters. Specify the number of periods and treatments—a standard 2×2 crossover has two periods with two treatments, each participant receiving both in randomized order. Design treatment sequences ensuring balance—use Latin square arrangements for designs with more than two treatments. Specify washout period duration between treatments sufficient for the first treatment's effects to dissipate—base on pharmacokinetic half-life for drugs or expected decay of behavioral interventions. Address carryover effects by testing for them statistically and designing washout accordingly. Plan period effect assessment since outcomes may change over time independent of treatment. Document sequence assignment showing which participants receive which treatment order, ensuring balanced allocation across sequences.

**6. Cluster Trial Configuration**

For designs randomizing groups rather than individuals, configure cluster parameters. Specify the clustering structure—what constitutes a cluster (school, clinic, community), how many clusters, and expected individuals per cluster. Estimate the intracluster correlation coefficient (ICC) from pilot data or literature—typical ICCs range from 0.01-0.05 for health outcomes within clinics to 0.15-0.25 for educational outcomes within schools. Calculate the design effect: DE = 1 + (m-1) × ICC, where m is average cluster size—this inflates required sample size substantially. Determine whether to randomize intact clusters or match clusters before randomization. For unequal cluster sizes, use the coefficient of variation of cluster sizes to adjust design effect calculations. Consider stratifying cluster randomization by cluster-level characteristics (size, baseline outcomes, geography) to improve balance.

**7. Stepped-Wedge and Sequential Designs**

For designs with staggered treatment rollout, configure the temporal structure. In stepped-wedge designs, all clusters begin as control and sequentially cross over to treatment at randomly determined times—specify number of clusters, number of time periods, and how many clusters switch at each step. Design the rollout schedule balancing operational feasibility with statistical efficiency—more steps with fewer clusters per step provides more treatment effect information but increases logistical complexity. Account for secular trends since all clusters are exposed to treatment later in the study when outcomes may naturally differ. Plan repeated outcome measurement at each time period for all clusters. For adaptive sequential designs, specify interim analysis timing, stopping rules for efficacy or futility, and alpha-spending function for Type I error control. Document the complete timeline showing when each cluster transitions.

**8. Quasi-Experimental and RDD Configuration**

For non-randomized designs, configure the identification strategy. In quasi-experimental designs, specify the assignment mechanism creating treatment and control groups—natural variation, policy implementation, eligibility rules, or self-selection. Document threats to validity from this non-random assignment and planned analytical adjustments (propensity score matching, difference-in-differences, instrumental variables). For regression discontinuity designs, specify the assignment variable (running variable), cutoff value determining treatment, and whether the design is sharp (deterministic assignment at cutoff) or fuzzy (probabilistic assignment). Select bandwidth for local estimation—narrower bandwidths increase internal validity near the cutoff but reduce sample size; use data-driven selection methods (IK, MSE-optimal). Plan manipulation tests (McCrary density test) to verify the cutoff wasn't gamed. Specify functional form for modeling the relationship between running variable and outcome on each side of cutoff.

Deliver your experimental design setup as:

1. **Design specification** with type, configuration parameters, and rationale for key choices
2. **Treatment protocol** detailing intervention and control conditions with implementation guidance
3. **Randomization procedure** specifying method, stratification, blocking, and allocation concealment
4. **Allocation table** showing treatment assignments for all participants/clusters/sequences
5. **Design matrix** for factorial designs showing all conditions and planned sample per cell
6. **Cluster parameters** for cluster trials including ICC, design effect, and effective sample size
7. **Timeline** for stepped-wedge or sequential designs showing rollout schedule
8. **Implementation checklist** with pre-study, during-study, and data-collection milestones

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{RESEARCH_OBJECTIVE}` | Hypothesis and research question | "testing whether gamified exercises improve physical therapy adherence compared to standard exercises" |
| `{TREATMENT_INTERVENTION}` | Intervention and control conditions | "gamified app-based exercise program versus standard printed exercise handout" |
| `{STUDY_PARAMETERS}` | Sample, duration, and constraints | "200 knee replacement patients across 4 clinics over 12-week recovery period" |

---

## Usage Examples

### Example 1: Clinical RCT Setup
**Prompt:** "Configure a complete experimental design for {RESEARCH_OBJECTIVE: testing whether cognitive behavioral therapy delivered via telehealth is non-inferior to in-person CBT for depression}, testing {TREATMENT_INTERVENTION: 12-session telehealth CBT versus 12-session in-person CBT with therapist-delivered manualized protocol}, with {STUDY_PARAMETERS: 300 adults with moderate depression, 6-month follow-up, non-inferiority margin of 2 points on PHQ-9}."

**Expected Output:** Design specification for parallel-group non-inferiority RCT with 1:1 allocation (150 per arm). Treatment protocol: 12 weekly 50-minute CBT sessions following Beck protocol—telehealth via HIPAA-compliant video platform, in-person at clinic. Randomization: stratified by baseline PHQ-9 severity (moderate/moderately-severe) and prior therapy (yes/no), permuted blocks of 4 and 6, centralized web-based system. Allocation table generated at enrollment. Analysis plan: per-protocol primary for non-inferiority with ITT sensitivity, 95% CI for difference must exclude -2 points. Implementation checklist covering therapist training, fidelity monitoring, session recording, outcome assessment blinding.

### Example 2: Digital A/B Test Setup
**Prompt:** "Configure a complete experimental design for {RESEARCH_OBJECTIVE: testing which onboarding flow maximizes 7-day user retention for a fitness app}, testing {TREATMENT_INTERVENTION: current 5-screen onboarding (control) versus streamlined 2-screen onboarding versus personalized 4-screen onboarding with goal-setting}, with {STUDY_PARAMETERS: 90,000 new users over 3 weeks, minimum detectable effect of 3% relative retention lift}."

**Expected Output:** Design specification for A/B/C test with 33/33/34% traffic allocation across three variants. Treatment protocol: Control shows current 5-screen flow; Variant A shows condensed 2-screen flow (account creation + main feature); Variant B shows 4-screen personalized flow with fitness goal selection affecting initial content. Randomization: user-ID-based hash ensuring consistent experience across sessions, triggered at first app launch. Allocation based on user_id mod 100 mapped to variants. Primary metric: binary retention (opened app on day 7+). Analysis: chi-square test with Bonferroni correction for 3 pairwise comparisons, 95% CI for each variant vs. control. Implementation checklist: event logging verification, bot filtering, segment validation (new users only).

### Example 3: Cluster Trial Setup
**Prompt:** "Configure a complete experimental design for {RESEARCH_OBJECTIVE: testing whether a nurse-led care coordination program reduces hospital readmissions}, testing {TREATMENT_INTERVENTION: dedicated nurse coordinator assigned to high-risk patients versus usual discharge planning}, with {STUDY_PARAMETERS: 24 hospitals, average 50 eligible patients per hospital per month, expected ICC of 0.03, 6-month enrollment period}."

**Expected Output:** Design specification for cluster RCT randomizing hospitals with 1:1 allocation. Treatment protocol: Treatment hospitals assign RN coordinator to patients with readmission risk score >50; coordinator conducts discharge planning, 48-hour post-discharge call, and weekly check-ins for 30 days. Control hospitals continue existing discharge procedures. Cluster parameters: 24 clusters, m=50/month, ICC=0.03, design effect=2.47, effective N per arm reduced from 600 to 243. Randomization: stratified by hospital size (small/large) and baseline readmission rate (tertiles), 12 hospitals per arm. Primary outcome: 30-day all-cause readmission (binary). Analysis: mixed-effects logistic regression with hospital random intercept, adjusted for patient-level risk factors. Implementation checklist: hospital recruitment, coordinator training, patient identification workflow, outcome tracking via claims data.

---

## Cross-References

- [experimental-design-overview.md](experimental-design-overview.md) - Design selection guidance and workflow navigation
- [randomization-and-power-analysis.md](randomization-and-power-analysis.md) - Sample size calculation and randomization implementation
- [treatment-effect-analysis.md](treatment-effect-analysis.md) - Analyzing experimental results
- [validity-and-diagnostics.md](validity-and-diagnostics.md) - Verifying design validity and checking assumptions
