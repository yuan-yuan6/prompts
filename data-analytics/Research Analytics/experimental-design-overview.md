---
category: data-analytics/Research Analytics
last_updated: 2025-11-10
related_templates:
- experimental-design-setup.md
- randomization-and-power-analysis.md
- treatment-effect-analysis.md
- validity-and-diagnostics.md
- variables-and-implementation.md
tags:
- causal-inference
- data-analytics
- navigation
- research
- template
title: Experimental Design and Causal Inference Overview
use_cases:
- Navigate the experimental design framework and select appropriate prompts for designing,
  implementing, and analyzing controlled experiments including RCTs, A/B tests, and
  causal inference studies
---

# Experimental Design and Causal Inference Overview

## Purpose

This framework provides a comprehensive system for designing, implementing, and analyzing controlled experiments to establish causal relationships with statistical rigor. Whether you're conducting randomized controlled trials, A/B tests, or quasi-experimental studies, this suite of prompts guides you through every phase from initial design to final analysis and interpretation.

## Framework Components

This experimental design framework is organized into 5 specialized prompts, each focusing on a critical phase of experimental research:

### 1. [Experimental Design Setup](experimental-design-setup.md)
**Purpose:** Select and configure the appropriate experimental design structure

**Use when you need to:**
- Choose from 8 different design types (RCT, A/B test, factorial, crossover, cluster, stepped wedge, quasi-experimental, regression discontinuity)
- Configure treatment conditions and allocation schemes
- Create participant assignment frameworks
- Generate design matrices and allocation tables

**Key features:**
- ExperimentalDesigner class with 8 design type implementations
- Automated allocation table generation
- Design-specific configuration options
- Implementation planning templates

**Typical outputs:**
- Complete design specification document
- Participant/unit allocation scheme
- Design matrix or allocation table
- Implementation timeline

---

### 2. [Randomization and Power Analysis](randomization-and-power-analysis.md)
**Purpose:** Plan pre-experiment procedures including randomization and sample size calculations

**Use when you need to:**
- Implement randomization procedures (simple, block, stratified, cluster, adaptive)
- Calculate required sample sizes for adequate statistical power
- Perform power analysis for different test types
- Generate minimum detectable effect (MDE) estimates

**Key features:**
- RandomizationManager class with 6 randomization methods
- PowerAnalyzer class supporting 5 test types
- Reproducible randomization with seed control
- Power curves and sensitivity analyses

**Typical outputs:**
- Power analysis report with sample size recommendations
- Randomization code with reproducible seed
- Allocation verification results
- Power curves and effect size sensitivity plots

---

### 3. [Treatment Effect Analysis](treatment-effect-analysis.md)
**Purpose:** Perform comprehensive treatment effect analysis using causal inference methods

**Use when you need to:**
- Analyze treatment effects using multiple analytical approaches
- Calculate intention-to-treat (ITT) estimates
- Perform per-protocol (PP) and CACE analyses
- Conduct dose-response and subgroup analyses

**Key features:**
- TreatmentEffectAnalyzer class with 6 analysis methods
- ITT, per-protocol, instrumental variable, and CACE implementations
- Dose-response relationship modeling
- Subgroup analysis with interaction testing

**Typical outputs:**
- Treatment effect estimates with confidence intervals
- Comparison of ITT vs. PP vs. CACE results
- Dose-response curves
- Subgroup effect estimates with forest plots

---

### 4. [Validity and Diagnostics](validity-and-diagnostics.md)
**Purpose:** Assess experimental validity and perform diagnostic checks

**Use when you need to:**
- Verify randomization success and covariate balance
- Analyze attrition and compliance patterns
- Detect contamination and spillover effects
- Check statistical assumptions

**Key features:**
- ExperimentalValidityChecker class with 8 assessment methods
- Randomization balance verification
- Attrition and compliance analysis
- Statistical assumption checking

**Typical outputs:**
- Comprehensive validity assessment report
- Balance tables with standardized differences
- Attrition analysis results
- Assumption verification results
- Threat-to-validity evaluation

---

### 5. [Variables and Implementation Guide](variables-and-implementation.md)
**Purpose:** Complete reference guide with 400+ variables and implementation best practices

**Use when you need to:**
- Look up variable definitions and usage
- Find implementation examples
- Review best practices and common pitfalls
- Understand output requirements

**Key features:**
- 400+ comprehensive variable definitions
- Organized by category (design, randomization, analysis, etc.)
- 5 detailed usage examples across domains
- Customization options and tips

**Typical outputs:**
- Variable reference for your specific study
- Implementation checklist
- Best practices guide
- Domain-specific examples

## Experimental Design Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXPERIMENTAL DESIGN WORKFLOW                  │
└─────────────────────────────────────────────────────────────────┘

Phase 1: DESIGN SELECTION AND SETUP
┌──────────────────────────────────────────┐
│  experimental-design-setup.md            │
│                                          │
│  • Choose design type                    │
│  • Configure treatment conditions        │
│  • Define participant allocation         │
│  • Create design specification           │
└──────────────────────────────────────────┘
                    ↓
Phase 2: PRE-EXPERIMENT PLANNING
┌──────────────────────────────────────────┐
│  randomization-and-power-analysis.md     │
│                                          │
│  • Calculate required sample size        │
│  • Perform power analysis                │
│  • Implement randomization               │
│  • Verify allocation balance             │
└──────────────────────────────────────────┘
                    ↓
         DATA COLLECTION PHASE
         (Outside this framework)
                    ↓
Phase 3: VALIDITY ASSESSMENT
┌──────────────────────────────────────────┐
│  validity-and-diagnostics.md             │
│                                          │
│  • Check randomization success           │
│  • Assess covariate balance              │
│  • Analyze attrition patterns            │
│  • Verify statistical assumptions        │
└──────────────────────────────────────────┘
                    ↓
Phase 4: TREATMENT EFFECT ANALYSIS
┌──────────────────────────────────────────┐
│  treatment-effect-analysis.md            │
│                                          │
│  • Perform ITT analysis                  │
│  • Calculate treatment effects           │
│  • Conduct subgroup analyses             │
│  • Generate effect estimates             │
└──────────────────────────────────────────┘
                    ↓
Phase 5: IMPLEMENTATION REFERENCE
┌──────────────────────────────────────────┐
│  variables-and-implementation.md         │
│                                          │
│  • Reference variable definitions        │
│  • Review best practices                 │
│  • Check output requirements             │
│  • Find usage examples                   │
└──────────────────────────────────────────┘
```

## Design Type Selection Guide

Use this decision tree to select the appropriate experimental design:

```
START: What is your research context?
│
├─ Can you randomly assign treatment?
│  │
│  ├─ YES → Randomized Design
│  │  │
│  │  ├─ Individual-level randomization possible?
│  │  │  │
│  │  │  ├─ YES → Testing single treatment?
│  │  │  │  │
│  │  │  │  ├─ YES → Standard RCT
│  │  │  │  │        Use: experimental-design-setup.md → setup_rct()
│  │  │  │  │
│  │  │  │  └─ NO → Testing multiple factors?
│  │  │  │     │
│  │  │  │     ├─ YES → Factorial Design
│  │  │  │     │        Use: experimental-design-setup.md → setup_factorial_design()
│  │  │  │     │
│  │  │  │     └─ NO → Multiple variants (e.g., A/B/C test)?
│  │  │  │              Use: experimental-design-setup.md → setup_ab_test()
│  │  │  │
│  │  │  └─ NO → Each person can receive multiple treatments?
│  │  │           │
│  │  │           ├─ YES → Crossover Design
│  │  │           │        Use: experimental-design-setup.md → setup_crossover_design()
│  │  │           │
│  │  │           └─ NO → Must randomize groups/clusters?
│  │  │                    │
│  │  │                    ├─ All at once → Cluster RCT
│  │  │                    │                Use: experimental-design-setup.md → setup_cluster_trial()
│  │  │                    │
│  │  │                    └─ Staggered rollout → Stepped Wedge
│  │  │                                        Use: experimental-design-setup.md → setup_stepped_wedge()
│  │
│  └─ NO → Non-randomized Design
│     │
│     ├─ Treatment assigned by cutoff rule?
│     │  │
│     │  ├─ YES → Sharp cutoff (everyone above/below gets treatment)?
│     │  │        │
│     │  │        └─ YES → Regression Discontinuity Design
│     │  │                 Use: experimental-design-setup.md → setup_regression_discontinuity()
│     │  │
│     │  └─ NO → Quasi-Experimental Design
│     │           Use: experimental-design-setup.md → setup_quasi_experimental()
│     │
│     └─ Natural experiment or observational data?
│              → Consider other causal inference methods
│                 (propensity scores, difference-in-differences, etc.)
```

## Quick Start Pathways

### Pathway 1: Digital A/B Test (Fast Track)
**Timeline: 1-2 hours planning**

1. **Design Setup** (15 min)
   - Use `experimental-design-setup.md` → `setup_ab_test()`
   - Configure variants and traffic allocation
   - Define randomization unit (user/session)

2. **Power Analysis** (20 min)
   - Use `randomization-and-power-analysis.md` → `proportion_power_analysis()`
   - Calculate required sample size
   - Determine test duration

3. **Implementation** (15 min)
   - Use `variables-and-implementation.md` for variable reference
   - Implement randomization with seed
   - Set up tracking

4. **Analysis Ready** (10 min)
   - Prepare `treatment-effect-analysis.md` → `intention_to_treat_analysis()`
   - Plan validity checks with `validity-and-diagnostics.md`

---

### Pathway 2: Clinical Trial (Comprehensive)
**Timeline: 2-4 weeks planning**

1. **Week 1: Design & Planning**
   - Use `experimental-design-setup.md` → `setup_rct()`
   - Define eligibility criteria, treatments, outcomes
   - Plan stratification variables

2. **Week 1-2: Sample Size & Randomization**
   - Use `randomization-and-power-analysis.md`
   - Perform comprehensive power analysis
   - Design stratified block randomization
   - Create randomization code with allocation concealment

3. **Week 2-3: Protocol Development**
   - Use `variables-and-implementation.md` for complete variable list
   - Document all procedures
   - Plan data collection and monitoring

4. **Week 3-4: Analysis Planning**
   - Pre-specify analyses with `treatment-effect-analysis.md`
   - Plan validity checks with `validity-and-diagnostics.md`
   - Define stopping rules and interim analyses

---

### Pathway 3: Educational Intervention (Cluster Design)
**Timeline: 1 week planning**

1. **Day 1-2: Cluster Design Setup**
   - Use `experimental-design-setup.md` → `setup_cluster_trial()`
   - Define clusters (schools/classrooms)
   - Account for intracluster correlation (ICC)

2. **Day 3: Power Analysis with Design Effect**
   - Use `randomization-and-power-analysis.md`
   - Calculate design effect: 1 + (cluster_size - 1) × ICC
   - Determine required number of clusters

3. **Day 4-5: Randomization & Balance**
   - Implement cluster randomization
   - Plan baseline covariate balance checks
   - Prepare stratification by school characteristics

4. **Day 6-7: Analysis Planning**
   - Plan multi-level analysis accounting for clustering
   - Prepare validity assessment protocol
   - Define implementation fidelity measures

## Common Use Cases

### Research & Academia
- **Clinical trials** - Medical interventions, drug efficacy
- **Educational research** - Teaching methods, curriculum changes
- **Psychological experiments** - Behavioral interventions, cognitive studies
- **Social science research** - Policy interventions, social programs

### Business & Technology
- **A/B testing** - Website optimization, feature testing
- **Product experiments** - New features, pricing strategies
- **Marketing campaigns** - Ad creative, messaging, channels
- **User experience** - Design changes, onboarding flows

### Policy & Government
- **Program evaluation** - Social programs, healthcare initiatives
- **Policy testing** - Pilot programs, regulatory changes
- **Public health** - Health interventions, prevention programs
- **Development economics** - Aid programs, microfinance

## Statistical Concepts Reference

### Key Concepts Covered

**Design Types:**
- Randomized Controlled Trials (RCT)
- A/B and multivariate testing
- Factorial designs (2×2, 3×2, etc.)
- Crossover/within-subjects designs
- Cluster randomized trials
- Stepped wedge designs
- Quasi-experimental designs
- Regression discontinuity designs

**Randomization Methods:**
- Simple randomization
- Block randomization
- Stratified randomization
- Cluster randomization
- Adaptive randomization
- Minimization algorithms

**Power Analysis:**
- Sample size calculations
- Power curves
- Minimum detectable effects
- Effect size estimation
- Type I and Type II errors

**Treatment Effect Estimation:**
- Intention-to-treat (ITT)
- Per-protocol (PP)
- Complier average causal effect (CACE)
- Instrumental variable (IV) methods
- Dose-response relationships
- Subgroup and heterogeneous effects

**Validity Assessment:**
- Internal validity
- External validity
- Statistical conclusion validity
- Construct validity
- Covariate balance
- Attrition analysis
- Contamination detection



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Experimental Design Setup](experimental-design-setup.md)** - Complementary approaches and methodologies
- **[Randomization And Power Analysis](randomization-and-power-analysis.md)** - Complementary approaches and methodologies
- **[Treatment Effect Analysis](treatment-effect-analysis.md)** - Complementary approaches and methodologies
- **[Validity And Diagnostics](validity-and-diagnostics.md)** - Complementary approaches and methodologies
- **[Variables And Implementation](variables-and-implementation.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Experimental Design and Causal Inference Overview)
2. Use [Experimental Design Setup](experimental-design-setup.md) for deeper analysis
3. Apply [Randomization And Power Analysis](randomization-and-power-analysis.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Research Analytics](../../data-analytics/Research Analytics/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Navigate the experimental design framework and select appropriate prompts for designing, implementing, and analyzing controlled experiments including RCTs, A/B tests, and causal inference studies**: Combine this template with related analytics and strategy frameworks

## Best Practices Summary

### Design Phase
1. Pre-specify all analyses before data collection
2. Choose design that matches research question and constraints
3. Calculate adequate sample size with power analysis
4. Plan for expected attrition (typically add 15-20%)
5. Consider clustering and adjust sample size accordingly

### Implementation Phase
6. Use reproducible randomization with documented seed
7. Maintain allocation concealment to prevent selection bias
8. Implement blinding when feasible
9. Monitor data quality continuously
10. Track protocol deviations systematically

### Analysis Phase
11. Check randomization balance before outcome analysis
12. Use ITT as primary analysis
13. Pre-specify and limit subgroup analyses
14. Apply multiple testing corrections
15. Conduct sensitivity analyses

### Reporting Phase
16. Follow CONSORT guidelines for RCTs
17. Report all pre-specified outcomes
18. Include effect sizes and confidence intervals
19. Discuss clinical/practical significance
20. Make data and code available when possible

## Getting Help

### When to Use Which Prompt

| **Your Goal** | **Use This Prompt** |
|---------------|---------------------|
| Choose experimental design type | experimental-design-setup.md |
| Calculate sample size | randomization-and-power-analysis.md |
| Implement randomization | randomization-and-power-analysis.md |
| Analyze treatment effects | treatment-effect-analysis.md |
| Check validity and assumptions | validity-and-diagnostics.md |
| Look up variable definitions | variables-and-implementation.md |
| Find usage examples | variables-and-implementation.md |
| Review best practices | variables-and-implementation.md |

### Integration with Other Templates

This experimental design framework integrates well with:

- **[Predictive Modeling Framework](../predictive-modeling-framework.md)** - For outcome prediction models
- **[Dashboard Design Patterns](../dashboard-design-patterns.md)** - For experiment monitoring dashboards
- **[Data Governance Framework](../data-governance-framework.md)** - For data quality and compliance

## Additional Resources

### Recommended Reading
- Clinical trials: CONSORT guidelines
- A/B testing: "Trustworthy Online Controlled Experiments" by Kohavi et al.
- Causal inference: "Causal Inference: The Mixtape" by Cunningham
- Experimental design: "Design and Analysis of Experiments" by Montgomery

### Statistical Software
- R packages: `pwr`, `randomizr`, `estimatr`, `DeclareDesign`
- Python packages: `statsmodels`, `scipy.stats`, `scikit-learn`
- Specialized: G*Power for power analysis, PASS for sample size

### Online Tools
- Sample size calculators for various test types
- Randomization sequence generators
- Power analysis software
- Effect size converters

---

## Quick Reference Card

**Design Selection:** experimental-design-setup.md
**Power & Randomization:** randomization-and-power-analysis.md
**Effect Analysis:** treatment-effect-analysis.md
**Validity Checks:** validity-and-diagnostics.md
**Variables & Examples:** variables-and-implementation.md

**Key Principles:**
1. Randomize when possible
2. Calculate adequate sample size
3. Pre-specify analyses
4. Use ITT as primary
5. Check validity systematically
6. Report completely and transparently

**Success Checklist:**
- [ ] Design type selected and configured
- [ ] Power analysis completed
- [ ] Randomization implemented and verified
- [ ] Data collection plan documented
- [ ] Analysis plan pre-specified
- [ ] Validity checks planned
- [ ] Reporting standards identified
