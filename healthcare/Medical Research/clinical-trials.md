---
title: Clinical Trials Template
category: healthcare/Medical Research
tags: [automation, data-science, design, healthcare, machine-learning, research, template]
use_cases:
  - Creating design comprehensive clinical trial protocols, consent forms, and analysis plans for conducting ethical, scientifically rigorous research studies to advance medical knowledge and patient care.

  - Project planning and execution
  - Strategy development
related_templates:
  - telemedicine-platform-design.md
  - patient-care-pathway.md
  - clinical-trials-management.md
last_updated: 2025-11-09
---

# Clinical Trials Template

## Purpose
Design comprehensive clinical trial protocols, consent forms, and analysis plans for conducting ethical, scientifically rigorous research studies to advance medical knowledge and patient care.

## Quick Start

### For Phase I Trial Protocol
1. Define primary objective: `PRIMARY_OBJECTIVE: "Determine maximum tolerated dose (MTD)"`
2. Select study design: `STUDY_DESIGN: "3+3 dose escalation"`
3. Establish safety monitoring: DSMB with defined stopping rules for DLTs
4. Calculate starting dose: Base on 1/10 of NOAEL from animal studies
5. Register trial: Submit to ClinicalTrials.gov before enrolling first patient

### For Phase III RCT
1. Power sample size: `SAMPLE_SIZE: "450 patients (225 per arm)"` based on expected effect
2. Design randomization: Use permuted blocks, stratify by key prognostic factors
3. Define endpoints: Primary must be clinically meaningful, secondary hypothesis-driven
4. Plan interim analyses: Specify timing and alpha-spending function (O'Brien-Fleming)
5. Prepare regulatory submissions: IND/IDE application, multi-center IRB protocol

### Research Compliance Essentials
- IRB approval before any study activities (including screening)
- Informed consent must be voluntary, documented, and comprehension-verified
- Register interventional trials on ClinicalTrials.gov (FDAAA compliance)
- Report SAEs to IRB within 24-48 hours, FDA within 15 days
- Maintain regulatory binder: protocol, consents, amendments, correspondence
- Ensure data integrity: source documentation, audit trails, query resolution

### Publication Planning
- Register study prospectively to avoid publication bias
- Follow CONSORT/STROBE reporting guidelines
- Plan authorship according to ICMJE criteria upfront
- Deposit data in repository per journal/funder requirements
- Disclose conflicts of interest and funding sources

## Template

```
You are a clinical research specialist. Design [TRIAL_TYPE] for [RESEARCH_CONDITION] in [STUDY_POPULATION] using [STUDY_DESIGN] to investigate [RESEARCH_HYPOTHESIS] with [PRIMARY_ENDPOINT] as the primary outcome.

STUDY OVERVIEW:

Protocol Identification:
- Study title: [STUDY_TITLE]
- Protocol number: [PROTOCOL_NUMBER]
- Protocol version: [PROTOCOL_VERSION] - Date: [VERSION_DATE]
- Sponsor: [STUDY_SPONSOR]
- Principal investigator: [PRINCIPAL_INVESTIGATOR]
- Institution: [INVESTIGATIONAL_SITE]
- ClinicalTrials.gov identifier: [CLINICALTRIALS_GOV_ID]

### Study Classification
- Study phase: [STUDY_PHASE] - Phase I/II/III/IV
- Study type: [STUDY_TYPE] - Interventional/Observational
- Allocation: [ALLOCATION_TYPE] - Randomized/Non-randomized
- Intervention model: [INTERVENTION_MODEL] - Parallel/Crossover/Single group
- Masking: [MASKING_TYPE] - Open-label/Single-blind/Double-blind
- Primary purpose: [PRIMARY_PURPOSE] - Treatment/Prevention/Diagnostic/Supportive care

### BACKGROUND AND RATIONALE

### Disease Background
### Condition Overview
[CONDITION_OVERVIEW]
- Prevalence: [DISEASE_PREVALENCE]
- Incidence: [DISEASE_INCIDENCE]
- Mortality/Morbidity: [DISEASE_BURDEN]
- Economic impact: [ECONOMIC_IMPACT]

### Pathophysiology
[PATHOPHYSIOLOGY_DESCRIPTION]
- Molecular mechanisms: [MOLECULAR_MECHANISMS]
- Disease progression: [DISEASE_PROGRESSION]
- Risk factors: [RISK_FACTORS]
- Biomarkers: [RELEVANT_BIOMARKERS]

### Current Standard of Care
### Available Treatments
1. [STANDARD_TREATMENT_1] - Efficacy: [EFFICACY_1] - Limitations: [LIMITATIONS_1]
2. [STANDARD_TREATMENT_2] - Efficacy: [EFFICACY_2] - Limitations: [LIMITATIONS_2]
3. [STANDARD_TREATMENT_3] - Efficacy: [EFFICACY_3] - Limitations: [LIMITATIONS_3]

### Treatment Gaps
- Unmet medical needs: [UNMET_MEDICAL_NEEDS]
- Treatment limitations: [TREATMENT_LIMITATIONS]
- Patient populations underserved: [UNDERSERVED_POPULATIONS]
- Quality of life issues: [QOL_ISSUES]

Investigational Agent/Intervention:
### Agent Description
- Name: [INVESTIGATIONAL_AGENT_NAME]
- Mechanism of action: [MECHANISM_OF_ACTION]
- Chemical structure: [CHEMICAL_STRUCTURE]
- Formulation: [FORMULATION_DETAILS]
- Route of administration: [ROUTE_OF_ADMINISTRATION]

### Preclinical Data
- In vitro studies: [IN_VITRO_DATA] - Results: [IN_VITRO_RESULTS]
- Animal studies: [ANIMAL_STUDIES] - Species: [ANIMAL_SPECIES] - Results: [ANIMAL_RESULTS]
- Toxicology: [TOXICOLOGY_DATA] - NOAEL: [NOAEL] - Safety margin: [SAFETY_MARGIN]
- Pharmacokinetics: [PK_DATA] - Half-life: [HALF_LIFE] - Metabolism: [METABOLISM]

### Previous Clinical Experience
- Phase I studies: [PHASE_I_EXPERIENCE] - Dose range: [DOSE_RANGE] - Safety: [PHASE_I_SAFETY]
- Phase II studies: [PHASE_II_EXPERIENCE] - Efficacy signals: [EFFICACY_SIGNALS]
- Safety database: [SAFETY_DATABASE_SIZE] - SAEs: [SERIOUS_ADVERSE_EVENTS]

### STUDY OBJECTIVES

### Primary Objective
[PRIMARY_OBJECTIVE_STATEMENT]
- Primary endpoint: [PRIMARY_ENDPOINT]
- Measurement method: [PRIMARY_MEASUREMENT_METHOD]
- Time point: [PRIMARY_TIMEPOINT]
- Statistical hypothesis: [STATISTICAL_HYPOTHESIS]

### Secondary Objectives
1. [SECONDARY_OBJECTIVE_1]
   - Secondary endpoint: [SECONDARY_ENDPOINT_1]
   - Measurement: [SECONDARY_MEASUREMENT_1]
   - Timepoint: [SECONDARY_TIMEPOINT_1]

2. [SECONDARY_OBJECTIVE_2]
   - Secondary endpoint: [SECONDARY_ENDPOINT_2]
   - Measurement: [SECONDARY_MEASUREMENT_2]
   - Timepoint: [SECONDARY_TIMEPOINT_2]

3. [SECONDARY_OBJECTIVE_3]
   - Secondary endpoint: [SECONDARY_ENDPOINT_3]
   - Measurement: [SECONDARY_MEASUREMENT_3]

### Exploratory Objectives
- Biomarker analysis: [BIOMARKER_OBJECTIVES]
- Pharmacokinetic assessment: [PK_OBJECTIVES]
- Quality of life evaluation: [QOL_OBJECTIVES]
- Pharmacogenomics: [PGX_OBJECTIVES]

### STUDY DESIGN

### Study Schema
[STUDY_SCHEMA_DESCRIPTION]
- Study arms: [NUMBER_OF_ARMS]
- Randomization ratio: [RANDOMIZATION_RATIO]
- Stratification factors: [STRATIFICATION_FACTORS]
- Control group: [CONTROL_GROUP_DESCRIPTION]

### Study Population
### Target Population
[TARGET_POPULATION_DESCRIPTION]
- Population size: [TARGET_POPULATION_SIZE]
- Demographics: [TARGET_DEMOGRAPHICS]
- Disease characteristics: [DISEASE_CHARACTERISTICS]
- Geographic distribution: [GEOGRAPHIC_DISTRIBUTION]

### Inclusion Criteria
1. [INCLUSION_CRITERION_1]
2. [INCLUSION_CRITERION_2]
3. [INCLUSION_CRITERION_3]
4. [INCLUSION_CRITERION_4]
5. [INCLUSION_CRITERION_5]
6. [INCLUSION_CRITERION_6]
7. [INCLUSION_CRITERION_7]
8. [INCLUSION_CRITERION_8]

### Exclusion Criteria
1. [EXCLUSION_CRITERION_1]
2. [EXCLUSION_CRITERION_2]
3. [EXCLUSION_CRITERION_3]
4. [EXCLUSION_CRITERION_4]
5. [EXCLUSION_CRITERION_5]
6. [EXCLUSION_CRITERION_6]
7. [EXCLUSION_CRITERION_7]
8. [EXCLUSION_CRITERION_8]

### Sample Size Calculation
- Primary endpoint assumption: [ENDPOINT_ASSUMPTION]
- Expected effect size: [EXPECTED_EFFECT_SIZE]
- Power: [STATISTICAL_POWER]% - Alpha: [ALPHA_LEVEL]
- Dropout rate: [EXPECTED_DROPOUT_RATE]%
- Sample size per arm: [SAMPLE_SIZE_PER_ARM]
- Total sample size: [TOTAL_SAMPLE_SIZE]

### STUDY PROCEDURES

### Screening Period
Screening Assessments (Day -28 to -1):
- Informed consent: [CONSENT_PROCESS]
- Medical history: [MEDICAL_HISTORY_COLLECTION]
- Physical examination: [PHYSICAL_EXAM_DETAILS]
- Vital signs: [VITAL_SIGNS_FREQUENCY]
- Laboratory tests: [SCREENING_LABS]
  - Hematology: [HEMATOLOGY_TESTS]
  - Chemistry: [CHEMISTRY_TESTS]
  - Liver function: [LFT_TESTS]
  - Kidney function: [KIDNEY_FUNCTION_TESTS]
  - Coagulation: [COAGULATION_TESTS]
  - Urinalysis: [URINALYSIS_DETAILS]
- Imaging: [SCREENING_IMAGING] - Type: [IMAGING_TYPE] - Frequency: [IMAGING_FREQUENCY]
- Electrocardiogram: [ECG_REQUIREMENTS]
- Pregnancy test: [PREGNANCY_TEST_DETAILS]
- Biomarker collection: [BIOMARKER_COLLECTION]

### Eligibility Confirmation
- Inclusion/exclusion review: [ELIGIBILITY_REVIEW_PROCESS]
- Medical monitor approval: [MEDICAL_MONITOR_APPROVAL]
- Randomization eligibility: [RANDOMIZATION_ELIGIBILITY]

### Treatment Period
### Randomization
- Randomization method: [RANDOMIZATION_METHOD]
- Stratification: [STRATIFICATION_DETAILS]
- Block size: [BLOCK_SIZE]
- Allocation concealment: [ALLOCATION_CONCEALMENT]

### Treatment Administration
Study Drug/Intervention:
- Dosing schedule: [DOSING_SCHEDULE]
- Administration route: [ADMINISTRATION_ROUTE]
- Dose modifications: [DOSE_MODIFICATION_CRITERIA]
- Concomitant medications: [CONCOMITANT_MEDICATION_RULES]
- Treatment duration: [TREATMENT_DURATION]

### Visit Schedule
Baseline Visit (Day 1):
- Pre-dose assessments: [BASELINE_ASSESSMENTS]
- Randomization: [RANDOMIZATION_PROCESS]
- First dose administration: [FIRST_DOSE_PROCESS]
- Post-dose monitoring: [POST_DOSE_MONITORING]

### Treatment Visits
Week 2 Visit:
- Safety assessments: [WEEK_2_SAFETY]
- Efficacy assessments: [WEEK_2_EFFICACY]
- Laboratory tests: [WEEK_2_LABS]
- Adverse event review: [WEEK_2_AE_REVIEW]

Week 4 Visit:
- Physical examination: [WEEK_4_PHYSICAL_EXAM]
- Vital signs: [WEEK_4_VITALS]
- Laboratory monitoring: [WEEK_4_LABS]
- Imaging assessments: [WEEK_4_IMAGING]

Week 8 Visit:
- Primary endpoint assessment: [WEEK_8_PRIMARY_ENDPOINT]
- Secondary endpoints: [WEEK_8_SECONDARY_ENDPOINTS]
- Safety evaluation: [WEEK_8_SAFETY]

Week 12 Visit:
- End-of-treatment assessments: [WEEK_12_ASSESSMENTS]
- Final safety evaluation: [WEEK_12_SAFETY]
- Treatment compliance review: [COMPLIANCE_REVIEW]

Follow-up Period:
Safety Follow-up:
- Duration: [SAFETY_FOLLOWUP_DURATION]
- Visit schedule: [FOLLOWUP_VISIT_SCHEDULE]
- Safety assessments: [FOLLOWUP_SAFETY_ASSESSMENTS]
- Long-term adverse event monitoring: [LONG_TERM_AE_MONITORING]

Survival Follow-up (if applicable):
- Contact frequency: [SURVIVAL_CONTACT_FREQUENCY]
- Information collected: [SURVIVAL_DATA_COLLECTED]
- Duration of follow-up: [SURVIVAL_FOLLOWUP_DURATION]

### SAFETY MONITORING

### Safety Oversight
Data Safety Monitoring Board (DSMB):
- Composition: [DSMB_COMPOSITION]
- Meeting frequency: [DSMB_MEETING_FREQUENCY]
- Review criteria: [DSMB_REVIEW_CRITERIA]
- Stopping rules: [STOPPING_RULES]

### Safety Review Committee
- Internal safety committee: [INTERNAL_SAFETY_COMMITTEE]
- Review triggers: [SAFETY_REVIEW_TRIGGERS]
- Escalation procedures: [SAFETY_ESCALATION]

### Adverse Event Monitoring
### AE Classification
- Severity grading: [AE_SEVERITY_GRADING] - Scale: [SEVERITY_SCALE]
- Causality assessment: [CAUSALITY_ASSESSMENT_METHOD]
- Expectedness: [EXPECTEDNESS_CRITERIA]
- Serious adverse events: [SAE_DEFINITION]

### Reporting Requirements
- Expedited reporting: [EXPEDITED_REPORTING_TIMELINE]
- Regulatory reporting: [REGULATORY_REPORTING_REQUIREMENTS]
- IRB/Ethics committee reporting: [IRB_REPORTING_REQUIREMENTS]
- Sponsor notification: [SPONSOR_NOTIFICATION_TIMELINE]

### Safety Stopping Rules
- Individual patient: [INDIVIDUAL_STOPPING_CRITERIA]
- Study-wide: [STUDY_STOPPING_CRITERIA]
- Futility analysis: [FUTILITY_ANALYSIS_PLAN]

### STATISTICAL ANALYSIS PLAN

### Analysis Populations
- Intent-to-treat (ITT): [ITT_POPULATION_DEFINITION]
- Per-protocol (PP): [PP_POPULATION_DEFINITION]
- Safety population: [SAFETY_POPULATION_DEFINITION]
- Modified intent-to-treat: [mITT_POPULATION_DEFINITION]

### Statistical Methods
### Primary Analysis
- Statistical test: [PRIMARY_STATISTICAL_TEST]
- Significance level: [PRIMARY_SIGNIFICANCE_LEVEL]
- Confidence interval: [PRIMARY_CONFIDENCE_INTERVAL]
- Handling of missing data: [MISSING_DATA_APPROACH]
- Multiple testing adjustment: [MULTIPLE_TESTING_CORRECTION]

### Secondary Analyses
- [SECONDARY_ANALYSIS_1]: Method [SECONDARY_METHOD_1]
- [SECONDARY_ANALYSIS_2]: Method [SECONDARY_METHOD_2]
- [SECONDARY_ANALYSIS_3]: Method [SECONDARY_METHOD_3]

### Interim Analyses
- Number of interim analyses: [NUMBER_INTERIM_ANALYSES]
- Timing: [INTERIM_ANALYSIS_TIMING]
- Alpha spending function: [ALPHA_SPENDING_FUNCTION]
- Futility boundaries: [FUTILITY_BOUNDARIES]

### Subgroup Analyses
- Pre-specified subgroups: [PRESPECIFIED_SUBGROUPS]
- Biomarker-defined subgroups: [BIOMARKER_SUBGROUPS]
- Interaction testing: [INTERACTION_TESTING_APPROACH]

### REGULATORY AND ETHICAL CONSIDERATIONS

### Regulatory Framework
- Regulatory pathway: [REGULATORY_PATHWAY]
- IND/CTA status: [IND_CTA_STATUS]
- GCP compliance: [GCP_COMPLIANCE_STATEMENT]
- Regulatory guidance followed: [REGULATORY_GUIDANCE]

### Ethics Approval
- IRB/Ethics committee: [IRB_ETHICS_COMMITTEE]
- Approval date: [ETHICS_APPROVAL_DATE]
- Approval number: [ETHICS_APPROVAL_NUMBER]
- Continuing review schedule: [CONTINUING_REVIEW_SCHEDULE]

### Informed Consent
### Consent Process
- Consent form version: [CONSENT_FORM_VERSION]
- Language(s): [CONSENT_LANGUAGES]
- Special populations: [SPECIAL_POPULATION_CONSENT]
- Witness requirements: [WITNESS_REQUIREMENTS]

### Key Elements
- Study purpose: [CONSENT_STUDY_PURPOSE]
- Procedures: [CONSENT_PROCEDURES]
- Risks: [CONSENT_RISKS]
- Benefits: [CONSENT_BENEFITS]
- Alternatives: [CONSENT_ALTERNATIVES]
- Confidentiality: [CONSENT_CONFIDENTIALITY]
- Compensation: [CONSENT_COMPENSATION]
- Contact information: [CONSENT_CONTACTS]

### QUALITY ASSURANCE

### Data Management
### Electronic Data Capture
- System: [EDC_SYSTEM]
- Database lock procedures: [DATABASE_LOCK_PROCEDURES]
- Data validation: [DATA_VALIDATION_PROCEDURES]
- Audit trail: [AUDIT_TRAIL_REQUIREMENTS]

### Site Monitoring
- Monitoring frequency: [MONITORING_FREQUENCY]
- Source data verification: [SDV_PERCENTAGE]
- Key data points: [KEY_DATA_POINTS]
- Risk-based monitoring: [RISK_BASED_MONITORING_APPROACH]

### Quality Control
- Internal audits: [INTERNAL_AUDIT_SCHEDULE]
- External audits: [EXTERNAL_AUDIT_POSSIBILITY]
- Training requirements: [TRAINING_REQUIREMENTS]
- Protocol deviations: [PROTOCOL_DEVIATION_HANDLING]

### STUDY LOGISTICS

### Timeline
### Study Milestones
- First patient first visit: [FIRST_PATIENT_FIRST_VISIT]
- Last patient first visit: [LAST_PATIENT_FIRST_VISIT]
- Last patient last visit: [LAST_PATIENT_LAST_VISIT]
- Database lock: [DATABASE_LOCK_DATE]
- Final report: [FINAL_REPORT_DATE]

### Enrollment
- Enrollment rate assumption: [ENROLLMENT_RATE_ASSUMPTION]
- Sites participating: [NUMBER_OF_SITES]
- Geographic distribution: [SITE_GEOGRAPHIC_DISTRIBUTION]
- Site selection criteria: [SITE_SELECTION_CRITERIA]

### Budget and Resources
- Study budget: [STUDY_BUDGET]
- Cost per patient: [COST_PER_PATIENT]
- Resource requirements: [RESOURCE_REQUIREMENTS]
- Equipment needs: [EQUIPMENT_NEEDS]

### RISK MANAGEMENT

### Study Risks
### Enrollment Risks
- Slow enrollment: [SLOW_ENROLLMENT_RISK] - Mitigation: [ENROLLMENT_MITIGATION]
- Competing studies: [COMPETING_STUDIES_RISK]
- Patient retention: [PATIENT_RETENTION_RISK]

### Safety Risks
- Expected safety profile: [EXPECTED_SAFETY_PROFILE]
- Potential safety signals: [POTENTIAL_SAFETY_SIGNALS]
- Risk mitigation strategies: [SAFETY_RISK_MITIGATION]

### Operational Risks
- Site performance: [SITE_PERFORMANCE_RISK]
- Data quality: [DATA_QUALITY_RISK]
- Regulatory changes: [REGULATORY_CHANGE_RISK]
- Supply chain: [SUPPLY_CHAIN_RISK]

### Contingency Planning
- Protocol amendments: [PROTOCOL_AMENDMENT_PLANNING]
- Site replacement: [SITE_REPLACEMENT_STRATEGY]
- Study modification: [STUDY_MODIFICATION_CRITERIA]

### DISSEMINATION PLAN

### Publication Strategy
- Primary publication: [PRIMARY_PUBLICATION_PLAN]
- Secondary publications: [SECONDARY_PUBLICATION_PLAN]
- Authorship guidelines: [AUTHORSHIP_GUIDELINES]
- Data sharing: [DATA_SHARING_POLICY]

### Regulatory Submissions
- Marketing application: [MARKETING_APPLICATION_PLAN]
- Regulatory meetings: [REGULATORY_MEETING_PLAN]
- Label negotiations: [LABEL_NEGOTIATION_PLAN]

### Medical Communications
- Scientific presentations: [SCIENTIFIC_PRESENTATION_PLAN]
- Medical education: [MEDICAL_EDUCATION_PLAN]
- Stakeholder communication: [STAKEHOLDER_COMMUNICATION]

### COMPLETE CLINICAL TRIAL PROTOCOL

### Protocol Summary
Study: [FINAL_STUDY_TITLE]
Phase: [FINAL_STUDY_PHASE]
Population: [FINAL_STUDY_POPULATION]
Primary Objective: [FINAL_PRIMARY_OBJECTIVE]
Sample Size: [FINAL_SAMPLE_SIZE]
Duration: [FINAL_STUDY_DURATION]

Principal Investigator: [FINAL_PI_NAME]
Institution: [FINAL_INSTITUTION]
Sponsor: [FINAL_SPONSOR]
Protocol Version: [FINAL_PROTOCOL_VERSION]
Date: [FINAL_PROTOCOL_DATE]

---

### Protocol Development Checklist
✓ Scientific rationale established: [SCIENTIFIC_RATIONALE_STATUS]
✓ Primary objective clearly defined: [PRIMARY_OBJECTIVE_STATUS]
✓ Study design appropriate: [STUDY_DESIGN_STATUS]
✓ Sample size justified: [SAMPLE_SIZE_STATUS]
✓ Safety monitoring plan complete: [SAFETY_MONITORING_STATUS]
✓ Statistical plan appropriate: [STATISTICAL_PLAN_STATUS]
✓ Regulatory requirements addressed: [REGULATORY_STATUS]
✓ Ethical considerations complete: [ETHICS_STATUS]

Protocol quality: [PROTOCOL_QUALITY_RATING]
```

## Variables
[500+ variables covering comprehensive clinical trial design including study objectives, population, procedures, safety monitoring, statistical analysis, regulatory requirements, and quality assurance]

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
### Example 1: Phase III Cancer Trial
```
TRIAL_TYPE: "Phase III randomized controlled trial"
RESEARCH_CONDITION: "Metastatic breast cancer"
STUDY_POPULATION: "Post-menopausal women with HR+ HER2- disease"
STUDY_DESIGN: "Double-blind, placebo-controlled, multicenter"
RESEARCH_HYPOTHESIS: "Experimental drug improves progression-free survival"
PRIMARY_ENDPOINT: "Progression-free survival by RECIST 1.1"
```

### Example 2: Phase I Dose Escalation
```
TRIAL_TYPE: "Phase I dose escalation study"
RESEARCH_CONDITION: "Advanced solid tumors"
STUDY_POPULATION: "Patients with refractory cancers"
STUDY_DESIGN: "Open-label, 3+3 dose escalation"
RESEARCH_HYPOTHESIS: "Determine maximum tolerated dose"
PRIMARY_ENDPOINT: "Dose-limiting toxicities in first cycle"
```

### Example 3: Device Trial
```
TRIAL_TYPE: "Pivotal device trial"
RESEARCH_CONDITION: "Coronary artery disease"
STUDY_POPULATION: "Patients requiring percutaneous intervention"
STUDY_DESIGN: "Randomized controlled trial"
RESEARCH_HYPOTHESIS: "New stent is non-inferior to standard of care"
PRIMARY_ENDPOINT: "Target lesion failure at 12 months"
```

## Customization Options

1. **Trial Types**
   - Phase I dose escalation
   - Phase II efficacy
   - Phase III confirmatory
   - Phase IV post-market
   - Device trials
   - Diagnostic trials
   - Prevention trials
   - Behavioral intervention trials

2. **Study Designs**
   - Randomized controlled trials
   - Single-arm studies
   - Crossover designs
   - Cluster randomized trials
   - Adaptive designs
   - Basket/umbrella trials
   - Registry studies
   - Real-world evidence studies

3. **Therapeutic Areas**
   - Oncology
   - Cardiovascular
   - Neurology
   - Infectious diseases
   - Immunology
   - Endocrinology
   - Psychiatry
   - Rare diseases

4. **Study Phases**
   - Preclinical research
   - First-in-human studies
   - Proof-of-concept trials
   - Pivotal studies
   - Post-marketing surveillance
   - Investigator-initiated trials
   - Academic research
   - Industry-sponsored trials