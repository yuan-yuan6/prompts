---
category: healthcare/Clinical-Practice
last_updated: 2025-11-09
related_templates:
- telemedicine-platform-design.md
- patient-care-pathway.md
- clinical-trials-management.md
tags:
- documentation
- healthcare
- template
title: Clinical Decision Support Template
use_cases:
- Creating comprehensive clinical decision support tools including diagnostic algorithms,
  treatment guidelines, risk assessments, and evidence-based recommendations to enhance
  clinical judgment and improve patient outcomes.
- Project planning and execution
- Strategy development
---

# Clinical Decision Support Template

## Purpose
Create comprehensive clinical decision support tools including diagnostic algorithms, treatment guidelines, risk assessments, and evidence-based recommendations to enhance clinical judgment and improve patient outcomes.

## Quick Start

### For Diagnostic Decision Support
1. Define clinical question: `CLINICAL_QUESTION: "Should this patient be admitted for chest pain?"`
2. Apply risk stratification: Use validated tools (HEART score, TIMI, Wells criteria)
3. Review evidence level: Specify guideline source (ACC/AHA, USPSTF, etc.)
4. Document decision rationale: Record clinical reasoning and supporting data
5. Communicate with patient: Use shared decision-making, document preferences

### For Treatment Algorithm Development
1. Specify condition: `CONDITION_NAME: "Community-acquired pneumonia"`
2. Select guideline: Reference current evidence (IDSA/ATS guidelines 2019)
3. Create decision tree: Include patient factors, severity, allergies
4. Add safety checks: Drug interactions, renal/hepatic dosing, contraindications
5. Define monitoring: Specify clinical response criteria and follow-up timing

### HIPAA Considerations for Clinical Tools
- Anonymize patient cases used in teaching algorithms
- Secure storage of decision support tools containing patient data
- Audit trail for clinical decisions made using automated tools
- Obtain consent if patient data will be used for algorithm development
- Ensure third-party CDS tools have Business Associate Agreements

### Point-of-Care Best Practices
- Validate scoring systems are appropriate for your patient population
- Update protocols when new guidelines are released
- Document exceptions to standard pathways with clinical justification
- Review outcomes data to ensure algorithms improve care quality

## Template

```
You are a clinical decision support specialist. Create [DECISION_TOOL_TYPE] for [CLINICAL_SCENARIO] based on [EVIDENCE_LEVEL] to support [DECISION_CONTEXT] in [CARE_SETTING].

CLINICAL DECISION FRAMEWORK:
Decision Context:
- Clinical question: [CLINICAL_QUESTION]
- Decision type: [DECISION_TYPE] (Diagnostic/Therapeutic/Prognostic/Screening)
- Urgency level: [URGENCY_LEVEL]
- Available resources: [AVAILABLE_RESOURCES]
- Time constraints: [TIME_CONSTRAINTS]
- Setting limitations: [SETTING_LIMITATIONS]

### Evidence Base
- Guidelines referenced: [CLINICAL_GUIDELINES]
- Evidence level: [EVIDENCE_LEVEL]
- Literature support: [KEY_STUDIES]
- Expert consensus: [EXPERT_CONSENSUS]
- Local protocols: [INSTITUTIONAL_PROTOCOLS]

### Patient Factors
- Demographics: [PATIENT_DEMOGRAPHICS]
- Comorbidities: [COMORBIDITIES]
- Risk factors: [RISK_FACTORS]
- Contraindications: [CONTRAINDICATIONS]
- Patient preferences: [PREFERENCES]

### DIAGNOSTIC DECISION SUPPORT

### Differential Diagnosis Algorithm
Presenting Symptom: [CHIEF_COMPLAINT]

```
Initial Assessment:
├── Red Flags Present?
│   ├── YES → [EMERGENCY_PATHWAY]
│   └── NO → Continue Assessment
│
├── Primary Differential:
│   ├── [DIAGNOSIS_1] (Probability: [PROB_1]%)
│   │   ├── Supporting: [SUPPORT_1]
│   │   └── Against: [AGAINST_1]
│   ├── [DIAGNOSIS_2] (Probability: [PROB_2]%)
│   │   ├── Supporting: [SUPPORT_2]
│   │   └── Against: [AGAINST_2]
│   └── [DIAGNOSIS_3] (Probability: [PROB_3]%)
│       ├── Supporting: [SUPPORT_3]
│       └── Against: [AGAINST_3]
│
└── Diagnostic Workup:
    ├── Tier 1 Tests: [INITIAL_TESTS]
    ├── Tier 2 Tests: [SECONDARY_TESTS]
    └── Tier 3 Tests: [ADVANCED_TESTS]
```

Clinical Scoring Systems:
Score 1: [SCORE_NAME_1]
```
### Criteria
□ [CRITERION_1]: [POINTS_1]
□ [CRITERION_2]: [POINTS_2]
□ [CRITERION_3]: [POINTS_3]
□ [CRITERION_4]: [POINTS_4]
□ [CRITERION_5]: [POINTS_5]

Total Score: ___
Interpretation:
- Low risk (0-2): [LOW_RISK_ACTION]
- Moderate risk (3-5): [MOD_RISK_ACTION]
- High risk (>5): [HIGH_RISK_ACTION]
```

Diagnostic Test Interpretation:
Test: [TEST_NAME]
- Sensitivity: [SENSITIVITY]%
- Specificity: [SPECIFICITY]%
- PPV: [PPV]%
- NPV: [NPV]%
- Likelihood ratios: +LR [PLR], -LR [NLR]

Pre-test Probability → Post-test Probability:
- Low (<20%): [LOW_PRETEST]
- Moderate (20-80%): [MOD_PRETEST]
- High (>80%): [HIGH_PRETEST]

### TREATMENT DECISION ALGORITHMS

### Treatment Selection Matrix
```
Patient Characteristics × Treatment Options

                 [TREATMENT_1]  [TREATMENT_2]  [TREATMENT_3]
[FACTOR_1]       ✓✓✓           ✓✓            ✓
[FACTOR_2]       ✓✓            ✓✓✓           ✓
[FACTOR_3]       ✓             ✓✓            ✓✓✓
[FACTOR_4]       ✗             ✓✓            ✓

✓✓✓ = Strongly recommended
✓✓ = Recommended
✓ = Consider
✗ = Contraindicated
```

Medication Selection Tool:
Primary Options:
1. [FIRST_LINE_MED]
   - Efficacy: [EFFICACY_1]
   - Safety: [SAFETY_1]
   - Cost: [COST_1]
   - Convenience: [CONVENIENCE_1]
   - Contraindications: [CONTRAINDICATIONS_1]

2. [SECOND_LINE_MED]
   - Efficacy: [EFFICACY_2]
   - Safety: [SAFETY_2]
   - Cost: [COST_2]
   - Convenience: [CONVENIENCE_2]
   - Contraindications: [CONTRAINDICATIONS_2]

### Decision Factors
- Renal function: [RENAL_ADJUSTMENT]
- Hepatic function: [HEPATIC_ADJUSTMENT]
- Drug interactions: [INTERACTION_CHECK]
- Allergies: [ALLERGY_CHECK]
- Insurance coverage: [COVERAGE_CHECK]

### RISK ASSESSMENT TOOLS

### Cardiovascular Risk Calculator
```
10-Year ASCVD Risk:
Age: [AGE] years
Sex: [SEX]
Race: [RACE]
Total Cholesterol: [TC] mg/dL
HDL-C: [HDL] mg/dL
Systolic BP: [SBP] mmHg
BP Treatment: [BP_TREATED]
Diabetes: [DIABETES]
Smoking: [SMOKING]

Calculated Risk: [RISK_PERCENT]%

### Recommendations
< 5%: [LOW_RISK_REC]
5-7.5%: [BORDERLINE_REC]
7.5-20%: [INTERMEDIATE_REC]
≥ 20%: [HIGH_RISK_REC]
```

Surgical Risk Assessment:
RCRI Score:
□ High-risk surgery: [HIGH_RISK_SURGERY]
□ Ischemic heart disease: [IHD]
□ Heart failure: [HF]
□ Cerebrovascular disease: [CVD]
□ Diabetes on insulin: [DM_INSULIN]
□ Creatinine > 2.0: [RENAL]

### Risk Class
- Class I (0 points): 0.4% risk
- Class II (1 point): 0.9% risk
- Class III (2 points): 6.6% risk
- Class IV (≥3 points): >11% risk

### CLINICAL PATHWAYS

### Acute Chest Pain Pathway
```
ENTRY: Chest Pain Presentation
│
├── EKG within 10 minutes
│   ├── STEMI → Cath Lab
│   ├── NSTEMI → ACS Protocol
│   └── Normal → Continue
│
├── Troponin & Risk Stratification
│   ├── High Risk → Admit CCU
│   ├── Intermediate → Admit Telemetry
│   └── Low Risk → Consider Discharge
│
└── Stress Test/CT Angio Decision
    ├── Positive → Cardiology Consult
    └── Negative → Discharge Planning
```

Sepsis Management Pathway:
```
Recognition (Time 0)
├── qSOFA ≥2 or Suspicion
└── Initiate Sepsis Bundle

Hour 1:
├── Lactate level
├── Blood cultures x2
├── Broad-spectrum antibiotics
├── 30 mL/kg crystalloid if hypotensive/lactate ≥4
└── Vasopressors if needed

Hours 2-6:
├── Reassess volume status
├── Repeat lactate if elevated
├── Target MAP ≥65
└── Consider ICU transfer
```

EVIDENCE-BASED RECOMMENDATIONS:

Guideline Integration:
Condition: [CONDITION_NAME]
Guidelines:
1. [GUIDELINE_1]: Class [CLASS_1], Level [LEVEL_1]
2. [GUIDELINE_2]: Class [CLASS_2], Level [LEVEL_2]
3. [GUIDELINE_3]: Class [CLASS_3], Level [LEVEL_3]

### Recommendation Strength
- Class I: Should be performed (Benefit >>> Risk)
- Class IIa: Reasonable to perform (Benefit >> Risk)
- Class IIb: May be considered (Benefit ≥ Risk)
- Class III: Not recommended (Risk ≥ Benefit)

### Evidence Levels
- Level A: Multiple RCTs or meta-analyses
- Level B: Single RCT or large observational
- Level C: Expert opinion or small studies

### SCREENING RECOMMENDATIONS

### Cancer Screening Guidelines
### Breast Cancer
- Age 40-49: [BREAST_40_49]
- Age 50-74: [BREAST_50_74]
- Age ≥75: [BREAST_75_PLUS]
- High risk: [BREAST_HIGH_RISK]

### Colorectal Cancer
- Age 45-49: [COLON_45_49]
- Age 50-75: [COLON_50_75]
- Age >75: [COLON_75_PLUS]
- High risk: [COLON_HIGH_RISK]

### Lung Cancer
- Eligibility criteria: [LUNG_CRITERIA]
- Screening method: [LUNG_METHOD]
- Frequency: [LUNG_FREQUENCY]

### Preventive Care Checklist
### Immunizations
□ Influenza: [FLU_STATUS]
□ Pneumococcal: [PNEUMO_STATUS]
□ Tdap/Td: [TDAP_STATUS]
□ Zoster: [ZOSTER_STATUS]
□ COVID-19: [COVID_STATUS]

### Health Maintenance
□ Blood pressure: [BP_SCREENING]
□ Lipids: [LIPID_SCREENING]
□ Diabetes: [DM_SCREENING]
□ Depression: [DEPRESSION_SCREENING]
□ Fall risk: [FALL_SCREENING]

### PROGNOSTIC TOOLS

### Mortality Prediction
### ICU Mortality Score
- APACHE II: [APACHE_SCORE]
- SOFA: [SOFA_SCORE]
- Expected mortality: [MORTALITY_PERCENT]%

### Cancer Prognosis
- Stage: [CANCER_STAGE]
- Grade: [CANCER_GRADE]
- Molecular markers: [MOLECULAR_MARKERS]
- 5-year survival: [FIVE_YEAR_SURVIVAL]%

### Functional Prognosis
- Current function: [CURRENT_FUNCTION]
- Expected recovery: [EXPECTED_RECOVERY]
- Time to recovery: [RECOVERY_TIME]
- Limiting factors: [LIMITING_FACTORS]

### DRUG INTERACTION CHECKER

### Interaction Analysis
### Current Medications
1. [CURRENT_MED_1]
2. [CURRENT_MED_2]
3. [CURRENT_MED_3]

New Medication: [NEW_MEDICATION]

### Interactions Identified
- Major: [MAJOR_INTERACTIONS]
- Moderate: [MODERATE_INTERACTIONS]
- Minor: [MINOR_INTERACTIONS]

### Management Recommendations
- Contraindicated combinations: [CONTRAINDICATED]
- Dose adjustments needed: [DOSE_ADJUSTMENTS]
- Monitoring required: [MONITORING_REQUIRED]
- Alternative options: [ALTERNATIVES]

### CLINICAL ALERTS

### Safety Alerts
High-Priority Alerts:
⚠️ [ALERT_1]: Action: [ACTION_1]
⚠️ [ALERT_2]: Action: [ACTION_2]
⚠️ [ALERT_3]: Action: [ACTION_3]

### Drug Allergy Alert
Patient Allergies: [KNOWN_ALLERGIES]
Cross-reactivity Risk: [CROSS_REACTIVITY]
Safe Alternatives: [SAFE_ALTERNATIVES]

### Critical Values
### Lab Critical Values
- [LAB_1]: Critical at [CRITICAL_VALUE_1]
- [LAB_2]: Critical at [CRITICAL_VALUE_2]
- [LAB_3]: Critical at [CRITICAL_VALUE_3]

### DECISION DOCUMENTATION

### Decision Summary
Clinical Question: [FINAL_QUESTION]
Evidence Reviewed: [EVIDENCE_SUMMARY]
Decision Made: [DECISION_MADE]
Rationale: [DECISION_RATIONALE]
Alternatives Considered: [ALTERNATIVES_CONSIDERED]

### Shared Decision Making
### Options Presented
1. [OPTION_1]: Pros/Cons: [OPTION_1_ANALYSIS]
2. [OPTION_2]: Pros/Cons: [OPTION_2_ANALYSIS]
3. [OPTION_3]: Pros/Cons: [OPTION_3_ANALYSIS]

Patient Choice: [PATIENT_CHOICE]
Reasoning: [PATIENT_REASONING]

### QUALITY METRICS

### Adherence to Guidelines
- Guideline compliance: [COMPLIANCE_RATE]%
- Core measures met: [CORE_MEASURES_MET]
- Documentation complete: [DOCUMENTATION_COMPLETE]
- Time targets met: [TIME_TARGETS_MET]

### Outcome Tracking
- Expected outcome: [EXPECTED_OUTCOME]
- Actual outcome: [ACTUAL_OUTCOME]
- Variance analysis: [VARIANCE_ANALYSIS]
- Learning points: [LEARNING_POINTS]

### CLINICAL RESOURCES

### Quick References
- Normal values: [NORMAL_VALUES_REF]
- Drug dosing: [DOSING_REFERENCE]
- Calculators: [CALCULATOR_LINKS]
- Guidelines: [GUIDELINE_LINKS]
- Protocols: [PROTOCOL_LINKS]

### Educational Materials
- Patient handouts: [PATIENT_MATERIALS]
- Provider resources: [PROVIDER_RESOURCES]
- Video tutorials: [VIDEO_RESOURCES]
- Decision aids: [DECISION_AIDS]

### DECISION OUTPUT
[Generate comprehensive clinical decision support with all elements]

Decision Type: [FINAL_DECISION_TYPE]
Clinical Scenario: [FINAL_SCENARIO]
Recommendation: [FINAL_RECOMMENDATION]

[COMPLETE_DECISION_SUPPORT]

---

### Decision Summary
- Evidence strength: [EVIDENCE_STRENGTH]
- Recommendation grade: [RECOMMENDATION_GRADE]
- Confidence level: [CONFIDENCE_LEVEL]
- Review date: [REVIEW_DATE]
- Updates needed: [UPDATE_FLAGS]

OUTPUT: Deliver comprehensive clinical decision support with:
1. Evidence-based algorithms
2. Risk assessment tools
3. Treatment guidelines
4. Diagnostic pathways
5. Drug interaction checks
6. Safety alerts
7. Quality metrics
```

## Variables
[All 250+ variables for comprehensive clinical decision support]

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: Chest Pain Evaluation
```
DECISION_TOOL_TYPE: "Diagnostic algorithm"
CLINICAL_SCENARIO: "Acute chest pain in ED"
EVIDENCE_LEVEL: "ACC/AHA Guidelines"
DECISION_CONTEXT: "Risk stratification"
CARE_SETTING: "Emergency department"
```

### Example 2: Antibiotic Selection
```
DECISION_TOOL_TYPE: "Treatment algorithm"
CLINICAL_SCENARIO: "Community-acquired pneumonia"
PATIENT_FACTORS: "Penicillin allergy, moderate severity"
EVIDENCE_BASE: "IDSA/ATS guidelines"
SETTING: "Hospital ward"
```

### Example 3: Cancer Screening
```
DECISION_TOOL_TYPE: "Screening recommendations"
CLINICAL_SCENARIO: "Average-risk 55-year-old"
GUIDELINES: "USPSTF recommendations"
RISK_FACTORS: "Family history assessment"
SETTING: "Primary care clinic"
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Telemedicine Platform Design](telemedicine-platform-design.md)** - Complementary approaches and methodologies
- **[Patient Care Pathway](patient-care-pathway.md)** - Complementary approaches and methodologies
- **[Clinical Trials Management](clinical-trials-management.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Clinical Decision Support Template)
2. Use [Telemedicine Platform Design](telemedicine-platform-design.md) for deeper analysis
3. Apply [Patient Care Pathway](patient-care-pathway.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[healthcare/Clinical Practice](../../healthcare/Clinical Practice/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive clinical decision support tools including diagnostic algorithms, treatment guidelines, risk assessments, and evidence-based recommendations to enhance clinical judgment and improve patient outcomes.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Customization Options

1. **Decision Types**
   - Diagnostic algorithms
   - Treatment selection
   - Risk stratification
   - Screening guidelines
   - Prognostic tools
   - Triage protocols

2. **Clinical Areas**
   - Emergency medicine
   - Critical care
   - Primary care
   - Specialty care
   - Surgical decisions
   - Pediatrics

3. **Evidence Levels**
   - Systematic reviews
   - Clinical guidelines
   - Expert consensus
   - Local protocols
   - Best practices

4. **Tool Formats**
   - Flowcharts
   - Scoring systems
   - Calculators
   - Checklists
   - Decision trees
   - Matrix tables

5. **Implementation**
   - Point-of-care tools
   - EMR integration
   - Mobile apps
   - Quick reference cards
   - Order sets
```