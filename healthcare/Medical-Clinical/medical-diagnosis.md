---
category: healthcare/Medical-Clinical
last_updated: 2025-11-09
related_templates:
- telemedicine-platform-design.md
- patient-care-pathway.md
- clinical-trials-management.md
tags:
- automation
- design
- documentation
- healthcare
- template
- testing
title: Medical Diagnosis Template
use_cases:
- General application
- Professional use
- Project implementation
---

# Medical Diagnosis Template

## Overview
This comprehensive template guides healthcare professionals through systematic diagnostic processes, incorporating evidence-based medicine, clinical reasoning, and differential diagnosis methodologies to achieve accurate and timely medical diagnoses.

## Quick Start

**HIPAA-Compliant Diagnostic Process:**

1. **Secure Patient Encounter** - Verify patient identity using two identifiers; conduct interview in private setting; document in encrypted system
2. **Comprehensive History (10 min)** - Chief complaint, HPI using OLDCARTS, past medical/surgical history, medications, allergies, family/social history
3. **Systematic Physical Exam (10 min)** - Vital signs, general appearance, focused system examination relevant to chief complaint
4. **Differential Diagnosis Development (5 min)** - List 3-5 diagnostic possibilities ranked by likelihood; identify must-rule-out conditions
5. **Evidence-Based Testing (5 min)** - Order appropriate labs/imaging based on pretest probability; document medical necessity for insurance
6. **Clinical Correlation (5 min)** - Integrate history, physical, and test results; calculate post-test probability
7. **Diagnosis & Plan Communication (5 min)** - Explain diagnosis in patient-friendly terms; discuss treatment options; obtain informed consent
8. **Secure Documentation** - Complete note with assessment and plan; authenticate within required timeframe; ensure proper encryption

**HIPAA Diagnostic Safeguards:** Only access patient information necessary for diagnosis. Document all disclosures (consultations, referrals). Obtain authorization before sharing diagnostic information with family members. Verify secure transmission methods for all test results and referrals.

## Template Structure

### 1. Initial Patient Presentation and Chief Complaint

**Structured History Taking Framework:**
```
As a [HEALTHCARE_PROVIDER_TYPE] with [SPECIALIZATION_AREA] working in [CLINICAL_SETTING] with [YEARS_OF_EXPERIENCE] years of experience, I am evaluating [PATIENT_AGE]-year-old [PATIENT_GENDER] [PATIENT_ETHNICITY] presenting with chief complaint of [PRIMARY_SYMPTOM] lasting [SYMPTOM_DURATION].

History of Present Illness: The [PRIMARY_SYMPTOM] started [ONSET_DESCRIPTION] and is characterized as [SYMPTOM_QUALITY], [SYMPTOM_SEVERITY_SCALE], [SYMPTOM_LOCATION], with [RADIATION_PATTERN]. The symptom is [AGGRAVATING_FACTORS] by [SPECIFIC_TRIGGERS] and [ALLEVIATING_FACTORS] by [RELIEF_METHODS].

Associated symptoms include [ASSOCIATED_SYMPTOM_1], [ASSOCIATED_SYMPTOM_2], [ASSOCIATED_SYMPTOM_3], [ASSOCIATED_SYMPTOM_4], and [ASSOCIATED_SYMPTOM_5]. Patient denies [PERTINENT_NEGATIVE_1], [PERTINENT_NEGATIVE_2], [PERTINENT_NEGATIVE_3].

Review of Systems: [CONSTITUTIONAL_SYMPTOMS], [CARDIOVASCULAR_SYMPTOMS], [PULMONARY_SYMPTOMS], [GASTROINTESTINAL_SYMPTOMS], [GENITOURINARY_SYMPTOMS], [MUSCULOSKELETAL_SYMPTOMS], [NEUROLOGICAL_SYMPTOMS], [PSYCHIATRIC_SYMPTOMS], [ENDOCRINE_SYMPTOMS], [HEMATOLOGIC_SYMPTOMS], [INTEGUMENTARY_SYMPTOMS].

Past Medical History: [CHRONIC_CONDITIONS_LIST], [PREVIOUS_HOSPITALIZATIONS], [SURGICAL_HISTORY], [MEDICATION_ALLERGIES], [ENVIRONMENTAL_ALLERGIES], [ADVERSE_DRUG_REACTIONS].

Current Medications: [PRESCRIPTION_MEDICATION_1] [DOSE_1] [FREQUENCY_1], [PRESCRIPTION_MEDICATION_2] [DOSE_2] [FREQUENCY_2], [OTC_MEDICATIONS], [HERBAL_SUPPLEMENTS], [VITAMINS_MINERALS].

Social History: [TOBACCO_USE_STATUS], [ALCOHOL_CONSUMPTION_PATTERN], [ILLICIT_DRUG_USE], [OCCUPATION_EXPOSURES], [TRAVEL_HISTORY_RECENT], [SEXUAL_HISTORY_RELEVANT], [LIVING_SITUATION], [SUPPORT_SYSTEM].

Family History: [MATERNAL_FAMILY_HISTORY], [PATERNAL_FAMILY_HISTORY], [GENETIC_CONDITIONS], [HEREDITARY_DISEASES], [AGE_OF_ONSET_PATTERNS].
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[HEALTHCARE_PROVIDER_TYPE]` | Type or category of healthcare provider | "Standard" |
| `[SPECIALIZATION_AREA]` | Specify the specialization area | "[specify value]" |
| `[CLINICAL_SETTING]` | Specify the clinical setting | "[specify value]" |
| `[YEARS_OF_EXPERIENCE]` | Specify the years of experience | "[specify value]" |
| `[PATIENT_AGE]` | Specify the patient age | "[specify value]" |
| `[PATIENT_GENDER]` | Specify the patient gender | "[specify value]" |
| `[PATIENT_ETHNICITY]` | Specify the patient ethnicity | "[specify value]" |
| `[PRIMARY_SYMPTOM]` | Specify the primary symptom | "[specify value]" |
| `[SYMPTOM_DURATION]` | Specify the symptom duration | "6 months" |
| `[ONSET_DESCRIPTION]` | Detailed description of onset | "[specify value]" |
| `[SYMPTOM_QUALITY]` | Specify the symptom quality | "[specify value]" |
| `[SYMPTOM_SEVERITY_SCALE]` | Specify the symptom severity scale | "[specify value]" |
| `[SYMPTOM_LOCATION]` | Specify the symptom location | "North America" |
| `[RADIATION_PATTERN]` | Specify the radiation pattern | "[specify value]" |
| `[AGGRAVATING_FACTORS]` | Specify the aggravating factors | "[specify value]" |
| `[SPECIFIC_TRIGGERS]` | Specify the specific triggers | "[specify value]" |
| `[ALLEVIATING_FACTORS]` | Specify the alleviating factors | "[specify value]" |
| `[RELIEF_METHODS]` | Specify the relief methods | "[specify value]" |
| `[ASSOCIATED_SYMPTOM_1]` | Specify the associated symptom 1 | "[specify value]" |
| `[ASSOCIATED_SYMPTOM_2]` | Specify the associated symptom 2 | "[specify value]" |
| `[ASSOCIATED_SYMPTOM_3]` | Specify the associated symptom 3 | "[specify value]" |
| `[ASSOCIATED_SYMPTOM_4]` | Specify the associated symptom 4 | "[specify value]" |
| `[ASSOCIATED_SYMPTOM_5]` | Specify the associated symptom 5 | "[specify value]" |
| `[PERTINENT_NEGATIVE_1]` | Specify the pertinent negative 1 | "[specify value]" |
| `[PERTINENT_NEGATIVE_2]` | Specify the pertinent negative 2 | "[specify value]" |
| `[PERTINENT_NEGATIVE_3]` | Specify the pertinent negative 3 | "[specify value]" |
| `[CONSTITUTIONAL_SYMPTOMS]` | Specify the constitutional symptoms | "[specify value]" |
| `[CARDIOVASCULAR_SYMPTOMS]` | Specify the cardiovascular symptoms | "[specify value]" |
| `[PULMONARY_SYMPTOMS]` | Specify the pulmonary symptoms | "[specify value]" |
| `[GASTROINTESTINAL_SYMPTOMS]` | Specify the gastrointestinal symptoms | "[specify value]" |
| `[GENITOURINARY_SYMPTOMS]` | Specify the genitourinary symptoms | "[specify value]" |
| `[MUSCULOSKELETAL_SYMPTOMS]` | Specify the musculoskeletal symptoms | "[specify value]" |
| `[NEUROLOGICAL_SYMPTOMS]` | Specify the neurological symptoms | "[specify value]" |
| `[PSYCHIATRIC_SYMPTOMS]` | Specify the psychiatric symptoms | "[specify value]" |
| `[ENDOCRINE_SYMPTOMS]` | Specify the endocrine symptoms | "[specify value]" |
| `[HEMATOLOGIC_SYMPTOMS]` | Specify the hematologic symptoms | "[specify value]" |
| `[INTEGUMENTARY_SYMPTOMS]` | Specify the integumentary symptoms | "[specify value]" |
| `[CHRONIC_CONDITIONS_LIST]` | Specify the chronic conditions list | "[specify value]" |
| `[PREVIOUS_HOSPITALIZATIONS]` | Specify the previous hospitalizations | "[specify value]" |
| `[SURGICAL_HISTORY]` | Specify the surgical history | "[specify value]" |
| `[MEDICATION_ALLERGIES]` | Specify the medication allergies | "[specify value]" |
| `[ENVIRONMENTAL_ALLERGIES]` | Specify the environmental allergies | "[specify value]" |
| `[ADVERSE_DRUG_REACTIONS]` | Specify the adverse drug reactions | "[specify value]" |
| `[PRESCRIPTION_MEDICATION_1]` | Specify the prescription medication 1 | "[specify value]" |
| `[DOSE_1]` | Specify the dose 1 | "[specify value]" |
| `[FREQUENCY_1]` | Specify the frequency 1 | "[specify value]" |
| `[PRESCRIPTION_MEDICATION_2]` | Specify the prescription medication 2 | "[specify value]" |
| `[DOSE_2]` | Specify the dose 2 | "[specify value]" |
| `[FREQUENCY_2]` | Specify the frequency 2 | "[specify value]" |
| `[OTC_MEDICATIONS]` | Specify the otc medications | "[specify value]" |
| `[HERBAL_SUPPLEMENTS]` | Specify the herbal supplements | "[specify value]" |
| `[VITAMINS_MINERALS]` | Specify the vitamins minerals | "[specify value]" |
| `[TOBACCO_USE_STATUS]` | Specify the tobacco use status | "In Progress" |
| `[ALCOHOL_CONSUMPTION_PATTERN]` | Specify the alcohol consumption pattern | "[specify value]" |
| `[ILLICIT_DRUG_USE]` | Specify the illicit drug use | "[specify value]" |
| `[OCCUPATION_EXPOSURES]` | Specify the occupation exposures | "[specify value]" |
| `[TRAVEL_HISTORY_RECENT]` | Specify the travel history recent | "[specify value]" |
| `[SEXUAL_HISTORY_RELEVANT]` | Specify the sexual history relevant | "[specify value]" |
| `[LIVING_SITUATION]` | Specify the living situation | "[specify value]" |
| `[SUPPORT_SYSTEM]` | Specify the support system | "[specify value]" |
| `[MATERNAL_FAMILY_HISTORY]` | Specify the maternal family history | "[specify value]" |
| `[PATERNAL_FAMILY_HISTORY]` | Specify the paternal family history | "[specify value]" |
| `[GENETIC_CONDITIONS]` | Specify the genetic conditions | "[specify value]" |
| `[HEREDITARY_DISEASES]` | Specify the hereditary diseases | "[specify value]" |
| `[AGE_OF_ONSET_PATTERNS]` | Specify the age of onset patterns | "[specify value]" |
| `[TEMPERATURE_VALUE]` | Specify the temperature value | "[specify value]" |
| `[SYSTOLIC_BP]` | Specify the systolic bp | "[specify value]" |
| `[DIASTOLIC_BP]` | Specify the diastolic bp | "[specify value]" |
| `[HEART_RATE_VALUE]` | Specify the heart rate value | "[specify value]" |
| `[RESPIRATORY_RATE_VALUE]` | Specify the respiratory rate value | "[specify value]" |
| `[O2_SAT_VALUE]` | Specify the o2 sat value | "[specify value]" |
| `[OXYGEN_DELIVERY_METHOD]` | Specify the oxygen delivery method | "[specify value]" |
| `[HEIGHT_MEASUREMENT]` | Specify the height measurement | "[specify value]" |
| `[WEIGHT_MEASUREMENT]` | Specify the weight measurement | "[specify value]" |
| `[BMI_CALCULATION]` | Specify the bmi calculation | "[specify value]" |
| `[OVERALL_APPEARANCE]` | Specify the overall appearance | "[specify value]" |
| `[DISTRESS_LEVEL]` | Specify the distress level | "[specify value]" |
| `[NUTRITIONAL_STATUS]` | Specify the nutritional status | "In Progress" |
| `[HYDRATION_STATUS]` | Specify the hydration status | "In Progress" |
| `[MENTAL_STATUS_DESCRIPTION]` | Detailed description of mental status | "In Progress" |
| `[HEAD_EXAMINATION_FINDINGS]` | Specify the head examination findings | "[specify value]" |
| `[EYE_EXAMINATION_DETAILS]` | Specify the eye examination details | "[specify value]" |
| `[PUPIL_EXAMINATION]` | Specify the pupil examination | "[specify value]" |
| `[FUNDOSCOPIC_FINDINGS]` | Specify the fundoscopic findings | "[specify value]" |
| `[EAR_EXAMINATION_RESULTS]` | Specify the ear examination results | "[specify value]" |
| `[NASAL_EXAMINATION]` | Specify the nasal examination | "[specify value]" |
| `[THROAT_EXAMINATION]` | Specify the throat examination | "[specify value]" |
| `[NECK_EXAMINATION]` | Specify the neck examination | "[specify value]" |
| `[LYMPH_NODE_ASSESSMENT]` | Specify the lymph node assessment | "[specify value]" |
| `[HEART_SOUNDS_DESCRIPTION]` | Detailed description of heart sounds | "[specify value]" |
| `[MURMUR_PRESENCE]` | Specify the murmur presence | "[specify value]" |
| `[PERIPHERAL_PULSES_ASSESSMENT]` | Specify the peripheral pulses assessment | "[specify value]" |
| `[CAPILLARY_REFILL_TIME]` | Specify the capillary refill time | "[specify value]" |
| `[JUGULAR_VENOUS_DISTENSION]` | Specify the jugular venous distension | "[specify value]" |
| `[EDEMA_ASSESSMENT]` | Specify the edema assessment | "[specify value]" |
| `[EXTREMITY_EXAMINATION]` | Specify the extremity examination | "[specify value]" |
| `[CHEST_WALL_INSPECTION]` | Specify the chest wall inspection | "[specify value]" |
| `[PERCUSSION_FINDINGS]` | Specify the percussion findings | "[specify value]" |
| `[AUSCULTATION_RESULTS]` | Specify the auscultation results | "[specify value]" |
| `[BREATH_SOUNDS_QUALITY]` | Specify the breath sounds quality | "[specify value]" |
| `[ADVENTITIOUS_SOUNDS]` | Specify the adventitious sounds | "[specify value]" |
| `[RESPIRATORY_EFFORT_DESCRIPTION]` | Detailed description of respiratory effort | "[specify value]" |
| `[INSPECTION_FINDINGS]` | Specify the inspection findings | "[specify value]" |
| `[AUSCULTATION_BOWEL_SOUNDS]` | Specify the auscultation bowel sounds | "[specify value]" |
| `[PERCUSSION_RESULTS]` | Specify the percussion results | "[specify value]" |
| `[PALPATION_FINDINGS]` | Specify the palpation findings | "[specify value]" |
| `[ORGAN_ENLARGEMENT]` | Specify the organ enlargement | "[specify value]" |
| `[TENDERNESS_LOCATION]` | Specify the tenderness location | "North America" |
| `[GUARDING_REBOUND]` | Specify the guarding rebound | "[specify value]" |
| `[SPECIAL_MANEUVERS]` | Specify the special maneuvers | "[specify value]" |
| `[JOINT_EXAMINATION]` | Specify the joint examination | "[specify value]" |
| `[RANGE_OF_MOTION_ASSESSMENT]` | Specify the range of motion assessment | "[specify value]" |
| `[MUSCLE_STRENGTH_TESTING]` | Specify the muscle strength testing | "[specify value]" |
| `[DEFORMITY_PRESENCE]` | Specify the deformity presence | "[specify value]" |
| `[SPINE_EXAMINATION]` | Specify the spine examination | "[specify value]" |
| `[GAIT_ASSESSMENT]` | Specify the gait assessment | "[specify value]" |
| `[MENTAL_STATUS_EXAM]` | Specify the mental status exam | "In Progress" |
| `[CRANIAL_NERVE_ASSESSMENT]` | Specify the cranial nerve assessment | "[specify value]" |
| `[MOTOR_EXAMINATION]` | Specify the motor examination | "[specify value]" |
| `[SENSORY_EXAMINATION]` | Specify the sensory examination | "[specify value]" |
| `[REFLEX_TESTING]` | Specify the reflex testing | "[specify value]" |
| `[CEREBELLAR_FUNCTION]` | Specify the cerebellar function | "[specify value]" |
| `[COORDINATION_TESTING]` | Specify the coordination testing | "[specify value]" |
| `[SKIN_COLOR_TEXTURE]` | Specify the skin color texture | "[specify value]" |
| `[LESION_DESCRIPTION]` | Detailed description of lesion | "[specify value]" |
| `[RASH_CHARACTERISTICS]` | Specify the rash characteristics | "[specify value]" |
| `[NAIL_EXAMINATION]` | Specify the nail examination | "[specify value]" |
| `[HAIR_ASSESSMENT]` | Specify the hair assessment | "[specify value]" |
| `[CHIEF_COMPLAINT]` | Specify the chief complaint | "[specify value]" |
| `[PATIENT_DEMOGRAPHIC]` | Specify the patient demographic | "[specify value]" |
| `[KEY_RISK_FACTORS]` | Specify the key risk factors | "[specify value]" |
| `[MOST_LIKELY_DIAGNOSIS]` | Specify the most likely diagnosis | "[specify value]" |
| `[LIKELIHOOD_PERCENTAGE]` | Specify the likelihood percentage | "25%" |
| `[SUPPORTING_SYMPTOM_1]` | Specify the supporting symptom 1 | "[specify value]" |
| `[SUPPORTING_SIGN_1]` | Specify the supporting sign 1 | "[specify value]" |
| `[SUPPORTING_HISTORY_1]` | Specify the supporting history 1 | "[specify value]" |
| `[CONTRADICTING_FACTOR_1]` | Specify the contradicting factor 1 | "[specify value]" |
| `[SECOND_LIKELY_DIAGNOSIS]` | Specify the second likely diagnosis | "[specify value]" |
| `[LIKELIHOOD_PERCENTAGE_2]` | Specify the likelihood percentage 2 | "25%" |
| `[SUPPORTING_SYMPTOM_2]` | Specify the supporting symptom 2 | "[specify value]" |
| `[SUPPORTING_SIGN_2]` | Specify the supporting sign 2 | "[specify value]" |
| `[SUPPORTING_HISTORY_2]` | Specify the supporting history 2 | "[specify value]" |
| `[CONTRADICTING_FACTOR_2]` | Specify the contradicting factor 2 | "[specify value]" |
| `[THIRD_LIKELY_DIAGNOSIS]` | Specify the third likely diagnosis | "[specify value]" |
| `[LIKELIHOOD_PERCENTAGE_3]` | Specify the likelihood percentage 3 | "25%" |
| `[SUPPORTING_SYMPTOM_3]` | Specify the supporting symptom 3 | "[specify value]" |
| `[SUPPORTING_SIGN_3]` | Specify the supporting sign 3 | "[specify value]" |
| `[SUPPORTING_HISTORY_3]` | Specify the supporting history 3 | "[specify value]" |
| `[CONTRADICTING_FACTOR_3]` | Specify the contradicting factor 3 | "[specify value]" |
| `[ALTERNATIVE_DIAGNOSIS_1]` | Specify the alternative diagnosis 1 | "[specify value]" |
| `[REASONING_1]` | Specify the reasoning 1 | "[specify value]" |
| `[ALTERNATIVE_DIAGNOSIS_2]` | Specify the alternative diagnosis 2 | "[specify value]" |
| `[REASONING_2]` | Specify the reasoning 2 | "[specify value]" |
| `[ALTERNATIVE_DIAGNOSIS_3]` | Specify the alternative diagnosis 3 | "[specify value]" |
| `[REASONING_3]` | Specify the reasoning 3 | "[specify value]" |
| `[EMERGENCY_CONDITION_1]` | Specify the emergency condition 1 | "[specify value]" |
| `[URGENT_TEST_1]` | Specify the urgent test 1 | "[specify value]" |
| `[EMERGENCY_CONDITION_2]` | Specify the emergency condition 2 | "[specify value]" |
| `[URGENT_TEST_2]` | Specify the urgent test 2 | "[specify value]" |
| `[EMERGENCY_CONDITION_3]` | Specify the emergency condition 3 | "[specify value]" |
| `[URGENT_TEST_3]` | Specify the urgent test 3 | "[specify value]" |
| `[RED_FLAG_SYMPTOM_1]` | Specify the red flag symptom 1 | "[specify value]" |
| `[RED_FLAG_SYMPTOM_2]` | Specify the red flag symptom 2 | "[specify value]" |
| `[RED_FLAG_SYMPTOM_3]` | Specify the red flag symptom 3 | "[specify value]" |
| `[DECISION_RULE_1]` | Specify the decision rule 1 | "[specify value]" |
| `[SCORE_1]` | Specify the score 1 | "[specify value]" |
| `[DECISION_RULE_2]` | Specify the decision rule 2 | "[specify value]" |
| `[RESULT_2]` | Specify the result 2 | "[specify value]" |
| `[LAB_TEST_1]` | Specify the lab test 1 | "[specify value]" |
| `[EXPECTED_RANGE_1]` | Specify the expected range 1 | "[specify value]" |
| `[SIGNIFICANCE_1]` | Specify the significance 1 | "[specify value]" |
| `[LAB_TEST_2]` | Specify the lab test 2 | "[specify value]" |
| `[EXPECTED_RANGE_2]` | Specify the expected range 2 | "[specify value]" |
| `[SIGNIFICANCE_2]` | Specify the significance 2 | "[specify value]" |
| `[LAB_TEST_3]` | Specify the lab test 3 | "[specify value]" |
| `[EXPECTED_RANGE_3]` | Specify the expected range 3 | "[specify value]" |
| `[SIGNIFICANCE_3]` | Specify the significance 3 | "[specify value]" |
| `[SPECIAL_LAB_TEST]` | Specify the special lab test | "[specify value]" |
| `[CONDITION_TESTED]` | Specify the condition tested | "[specify value]" |
| `[SENSITIVITY_PERCENTAGE]` | Specify the sensitivity percentage | "25%" |
| `[SPECIFICITY_PERCENTAGE]` | Specify the specificity percentage | "25%" |
| `[IMAGING_MODALITY_1]` | Specify the imaging modality 1 | "[specify value]" |
| `[INDICATION_1]` | Specify the indication 1 | "[specify value]" |
| `[EXPECTED_FINDINGS_1]` | Specify the expected findings 1 | "[specify value]" |
| `[IMAGING_MODALITY_2]` | Specify the imaging modality 2 | "[specify value]" |
| `[INDICATION_2]` | Specify the indication 2 | "[specify value]" |
| `[EXPECTED_FINDINGS_2]` | Specify the expected findings 2 | "[specify value]" |
| `[CONTRAST_STUDY]` | Specify the contrast study | "[specify value]" |
| `[CONTRAST_CONTRAINDICATIONS]` | Specify the contrast contraindications | "[specify value]" |
| `[PRE_MEDICATION_PROTOCOL]` | Specify the pre medication protocol | "[specify value]" |
| `[FUNCTIONAL_TEST_1]` | Specify the functional test 1 | "[specify value]" |
| `[TEST_PURPOSE_1]` | Specify the test purpose 1 | "[specify value]" |
| `[PATIENT_PREPARATION_1]` | Specify the patient preparation 1 | "[specify value]" |
| `[BIOPSY_PROCEDURE]` | Specify the biopsy procedure | "[specify value]" |
| `[BIOPSY_SITE]` | Specify the biopsy site | "[specify value]" |
| `[BIOPSY_METHOD]` | Specify the biopsy method | "[specify value]" |
| `[PATHOLOGY_FOCUS]` | Specify the pathology focus | "[specify value]" |
| `[CARDIAC_TESTING]` | Specify the cardiac testing | "[specify value]" |
| `[CARDIAC_TEST_TYPE]` | Type or category of cardiac test | "Standard" |
| `[CARDIAC_INDICATION]` | Specify the cardiac indication | "[specify value]" |
| `[CARDIAC_CONTRAINDICATIONS]` | Specify the cardiac contraindications | "[specify value]" |
| `[CULTURE_TYPE_1]` | Type or category of culture  1 | "Standard" |
| `[SPECIMEN_SOURCE_1]` | Specify the specimen source 1 | "[specify value]" |
| `[EXPECTED_ORGANISMS_1]` | Specify the expected organisms 1 | "[specify value]" |
| `[MOLECULAR_TEST]` | Specify the molecular test | "[specify value]" |
| `[TARGET_PATHOGEN]` | Target or intended pathogen | "[specify value]" |
| `[RESULT_TIMEFRAME]` | Specify the result timeframe | "[specify value]" |
| `[SEROLOGY_TEST]` | Specify the serology test | "[specify value]" |
| `[SEROLOGY_TARGET]` | Target or intended serology | "[specify value]" |
| `[RESULT_INTERPRETATION]` | Specify the result interpretation | "[specify value]" |
| `[POC_TEST_1]` | Specify the poc test 1 | "[specify value]" |
| `[IMMEDIATE_RESULT_1]` | Specify the immediate result 1 | "[specify value]" |
| `[CLINICAL_ACTION_1]` | Specify the clinical action 1 | "[specify value]" |
| `[BEDSIDE_ULTRASOUND]` | Specify the bedside ultrasound | "[specify value]" |
| `[ULTRASOUND_TARGET]` | Target or intended ultrasound | "[specify value]" |
| `[ULTRASOUND_FINDINGS]` | Specify the ultrasound findings | "[specify value]" |
| `[STAT_TESTS]` | Specify the stat tests | "[specify value]" |
| `[URGENT_TESTS]` | Specify the urgent tests | "[specify value]" |
| `[URGENT_TIMEFRAME]` | Specify the urgent timeframe | "[specify value]" |
| `[ROUTINE_TESTS]` | Specify the routine tests | "[specify value]" |
| `[LAB_RESULT_1]` | Specify the lab result 1 | "[specify value]" |
| `[ACTUAL_VALUE_1]` | Specify the actual value 1 | "[specify value]" |
| `[REFERENCE_RANGE_1]` | Specify the reference range 1 | "[specify value]" |
| `[CLINICAL_INTERPRETATION_1]` | Specify the clinical interpretation 1 | "[specify value]" |
| `[LAB_RESULT_2]` | Specify the lab result 2 | "[specify value]" |
| `[ACTUAL_VALUE_2]` | Specify the actual value 2 | "[specify value]" |
| `[REFERENCE_RANGE_2]` | Specify the reference range 2 | "[specify value]" |
| `[CLINICAL_INTERPRETATION_2]` | Specify the clinical interpretation 2 | "[specify value]" |
| `[CRITICAL_VALUE_ALERT]` | Specify the critical value alert | "[specify value]" |
| `[CRITICAL_LAB_VALUE]` | Specify the critical lab value | "[specify value]" |
| `[IMMEDIATE_ACTION_REQUIRED]` | Specify the immediate action required | "[specify value]" |
| `[IMAGING_FINDING_1]` | Specify the imaging finding 1 | "[specify value]" |
| `[IMAGING_STUDY_1]` | Specify the imaging study 1 | "[specify value]" |
| `[PATHOLOGY_SUGGESTED_1]` | Specify the pathology suggested 1 | "[specify value]" |
| `[IMAGING_FINDING_2]` | Specify the imaging finding 2 | "[specify value]" |
| `[ABNORMALITY_DESCRIPTION]` | Detailed description of abnormality | "[specify value]" |
| `[MEASUREMENT_VALUE]` | Specify the measurement value | "[specify value]" |
| `[INCIDENTAL_FINDING]` | Specify the incidental finding | "[specify value]" |
| `[FINDING_DESCRIPTION]` | Detailed description of finding | "[specify value]" |
| `[FOLLOW_UP_RECOMMENDATION]` | Specify the follow up recommendation | "[specify value]" |
| `[DIAGNOSTIC_CONFIDENCE_LEVEL]` | Specify the diagnostic confidence level | "[specify value]" |
| `[SUPPORTING_EVIDENCE_WEIGHT]` | Specify the supporting evidence weight | "[specify value]" |
| `[CONFLICTING_INFORMATION_ANALYSIS]` | Specify the conflicting information analysis | "[specify value]" |
| `[ADDITIONAL_TESTS_RATIONALE]` | Specify the additional tests rationale | "[specify value]" |
| `[DEFINITIVE_DIAGNOSIS_CRITERIA]` | Specify the definitive diagnosis criteria | "[specify value]" |
| `[PROBABLE_DIAGNOSIS_FEATURES]` | Specify the probable diagnosis features | "[specify value]" |
| `[POSSIBLE_DIAGNOSIS_UNCERTAINTY]` | Specify the possible diagnosis uncertainty | "[specify value]" |
| `[ALTERNATIVE_EXPLANATIONS_NEEDED]` | Specify the alternative explanations needed | "[specify value]" |
| `[SPECIALIST_TYPE_1]` | Type or category of specialist  1 | "Standard" |
| `[CONSULTATION_PURPOSE_1]` | Specify the consultation purpose 1 | "[specify value]" |
| `[CLINICAL_QUESTION_1]` | Specify the clinical question 1 | "[specify value]" |
| `[CONSULTATION_URGENCY_1]` | Specify the consultation urgency 1 | "[specify value]" |
| `[SPECIALIST_EXPERTISE_1]` | Specify the specialist expertise 1 | "[specify value]" |
| `[SPECIALIST_TYPE_2]` | Type or category of specialist  2 | "Standard" |
| `[CONSULTATION_PURPOSE_2]` | Specify the consultation purpose 2 | "[specify value]" |
| `[CLINICAL_QUESTION_2]` | Specify the clinical question 2 | "[specify value]" |
| `[CONSULTATION_URGENCY_2]` | Specify the consultation urgency 2 | "[specify value]" |
| `[SPECIALIST_EXPERTISE_2]` | Specify the specialist expertise 2 | "[specify value]" |
| `[TEAM_MEMBER_1]` | Specify the team member 1 | "[specify value]" |
| `[TEAM_MEMBER_2]` | Specify the team member 2 | "[specify value]" |
| `[TEAM_MEMBER_3]` | Specify the team member 3 | "[specify value]" |
| `[TEAM_MEMBER_4]` | Specify the team member 4 | "[specify value]" |
| `[PRESENTATION_FOCUS_AREAS]` | Specify the presentation focus areas | "[specify value]" |
| `[CONSENSUS_METHOD]` | Specify the consensus method | "[specify value]" |
| `[DECISION_DOCUMENTATION_PROCESS]` | Specify the decision documentation process | "[specify value]" |
| `[COMPLEXITY_ASSESSMENT]` | Specify the complexity assessment | "[specify value]" |
| `[CONSEQUENCE_ANALYSIS]` | Specify the consequence analysis | "[specify value]" |
| `[PATIENT_PREFERENCE_CONSIDERATION]` | Specify the patient preference consideration | "[specify value]" |
| `[POLICY_REQUIREMENTS]` | Specify the policy requirements | "[specify value]" |
| `[TELEHEALTH_PLATFORM]` | Specify the telehealth platform | "[specify value]" |
| `[TECHNICAL_SETUP]` | Specify the technical setup | "[specify value]" |
| `[DATA_SHARING_PROTOCOL]` | Specify the data sharing protocol | "[specify value]" |
| `[TELEMEDICINE_DOCUMENTATION]` | Specify the telemedicine documentation | "[specify value]" |
| `[DIAGNOSTIC_TEST_1]` | Specify the diagnostic test 1 | "[specify value]" |
| `[SENSITIVITY_VALUE_1]` | Specify the sensitivity value 1 | "[specify value]" |
| `[SPECIFICITY_VALUE_1]` | Specify the specificity value 1 | "[specify value]" |
| `[PPV_VALUE_1]` | Specify the ppv value 1 | "[specify value]" |
| `[NPV_VALUE_1]` | Specify the npv value 1 | "[specify value]" |
| `[DIAGNOSTIC_TEST_2]` | Specify the diagnostic test 2 | "[specify value]" |
| `[SENSITIVITY_VALUE_2]` | Specify the sensitivity value 2 | "[specify value]" |
| `[SPECIFICITY_VALUE_2]` | Specify the specificity value 2 | "[specify value]" |
| `[PPV_VALUE_2]` | Specify the ppv value 2 | "[specify value]" |
| `[NPV_VALUE_2]` | Specify the npv value 2 | "[specify value]" |
| `[PRETEST_PROBABILITY]` | Specify the pretest probability | "[specify value]" |
| `[POSTTEST_PROBABILITY]` | Specify the posttest probability | "[specify value]" |
| `[PREDICTION_RULE_1]` | Specify the prediction rule 1 | "[specify value]" |
| `[RULE_SCORE_1]` | Specify the rule score 1 | "[specify value]" |
| `[RISK_CATEGORY_1]` | Specify the risk category 1 | "[specify value]" |
| `[PREDICTION_RULE_2]` | Specify the prediction rule 2 | "[specify value]" |
| `[CRITERIA_MET_2]` | Specify the criteria met 2 | "[specify value]" |
| `[RULE_RECOMMENDATION_2]` | Specify the rule recommendation 2 | "[specify value]" |
| `[RULE_VALIDATION_STATUS]` | Specify the rule validation status | "In Progress" |
| `[DIAGNOSIS_TIME_HOURS]` | Specify the diagnosis time hours | "[specify value]" |
| `[TOTAL_TESTS_ORDERED]` | Specify the total tests ordered | "[specify value]" |
| `[DIAGNOSTIC_COST]` | Specify the diagnostic cost | "[specify value]" |
| `[OUTCOME_MEASURE]` | Specify the outcome measure | "[specify value]" |
| `[SATISFACTION_SCORE]` | Specify the satisfaction score | "[specify value]" |
| `[ACCURACY_PERCENTAGE]` | Specify the accuracy percentage | "25%" |
| `[BIAS_TYPE_1]` | Type or category of bias  1 | "Standard" |
| `[BIAS_TYPE_2]` | Type or category of bias  2 | "Standard" |
| `[BIAS_TYPE_3]` | Type or category of bias  3 | "Standard" |
| `[SAFETY_MECHANISM_1]` | Specify the safety mechanism 1 | "[specify value]" |
| `[SAFETY_MECHANISM_2]` | Specify the safety mechanism 2 | "[specify value]" |
| `[FEEDBACK_SYSTEM_1]` | Specify the feedback system 1 | "[specify value]" |
| `[FEEDBACK_SYSTEM_2]` | Specify the feedback system 2 | "[specify value]" |
| `[FINAL_DIAGNOSIS]` | Specify the final diagnosis | "[specify value]" |
| `[URGENT_TREATMENT_1]` | Specify the urgent treatment 1 | "[specify value]" |
| `[URGENT_TREATMENT_2]` | Specify the urgent treatment 2 | "[specify value]" |
| `[MONITORING_PARAMETER_1]` | Specify the monitoring parameter 1 | "[specify value]" |
| `[MONITORING_PARAMETER_2]` | Specify the monitoring parameter 2 | "[specify value]" |
| `[SAFETY_CONCERN_1]` | Specify the safety concern 1 | "[specify value]" |
| `[SAFETY_CONCERN_2]` | Specify the safety concern 2 | "[specify value]" |
| `[PRIMARY_TREATMENT_OPTION]` | Specify the primary treatment option | "[specify value]" |
| `[EXPECTED_RESPONSE_TIME]` | Specify the expected response time | "[specify value]" |
| `[ALTERNATIVE_TREATMENT_1]` | Specify the alternative treatment 1 | "[specify value]" |
| `[ALTERNATIVE_TREATMENT_2]` | Specify the alternative treatment 2 | "[specify value]" |
| `[TREATMENT_CONTRAINDICATION_1]` | Specify the treatment contraindication 1 | "[specify value]" |
| `[TREATMENT_CONTRAINDICATION_2]` | Specify the treatment contraindication 2 | "[specify value]" |
| `[SHORT_TERM_PROGNOSIS]` | Specify the short term prognosis | "[specify value]" |
| `[LONG_TERM_PROGNOSIS]` | Specify the long term prognosis | "[specify value]" |
| `[PROGNOSTIC_FACTOR_1]` | Specify the prognostic factor 1 | "[specify value]" |
| `[PROGNOSTIC_FACTOR_2]` | Specify the prognostic factor 2 | "[specify value]" |
| `[FOLLOW_UP_TIMEFRAME]` | Specify the follow up timeframe | "[specify value]" |
| `[MONITORING_SCHEDULE]` | Specify the monitoring schedule | "[specify value]" |
| `[RESPONSE_CRITERIA]` | Specify the response criteria | "[specify value]" |
| `[WARNING_SIGNS_LIST]` | Specify the warning signs list | "[specify value]" |
| `[LITERACY_ASSESSMENT]` | Specify the literacy assessment | "[specify value]" |
| `[COMMUNICATION_PREFERENCE]` | Specify the communication preference | "[specify value]" |
| `[LANGUAGE_ACCOMMODATION]` | Specify the language accommodation | "[specify value]" |
| `[CULTURAL_CONSIDERATIONS]` | Specify the cultural considerations | "[specify value]" |
| `[DIAGNOSIS_IN_LAYMAN_TERMS]` | Specify the diagnosis in layman terms | "[specify value]" |
| `[CONDITION_EXPLANATION]` | Specify the condition explanation | "[specify value]" |
| `[CAUSATION_EXPLANATION]` | Specify the causation explanation | "[specify value]" |
| `[EXPECTATION_SETTING]` | Specify the expectation setting | "[specify value]" |
| `[TREATMENT_RATIONALE]` | Specify the treatment rationale | "[specify value]" |
| `[ABSOLUTE_RISK_PERCENTAGE]` | Specify the absolute risk percentage | "25%" |
| `[RELATIVE_RISK_COMPARISON]` | Specify the relative risk comparison | "[specify value]" |
| `[NNT_VALUE]` | Specify the nnt value | "[specify value]" |
| `[RISK_COMMUNICATION_TOOLS]` | Specify the risk communication tools | "[specify value]" |
| `[OPTION_1]` | Specify the option 1 | "[specify value]" |
| `[OPTION_2]` | Specify the option 2 | "[specify value]" |
| `[OPTION_3]` | Specify the option 3 | "[specify value]" |
| `[PATIENT_VALUES_1]` | Specify the patient values 1 | "[specify value]" |
| `[PATIENT_VALUES_2]` | Specify the patient values 2 | "[specify value]" |
| `[PATIENT_PREFERENCE]` | Specify the patient preference | "[specify value]" |
| `[DECISION_AID_USED]` | Specify the decision aid used | "[specify value]" |
| `[AGREED_TREATMENT_PLAN]` | Specify the agreed treatment plan | "[specify value]" |
| `[DOCUMENTED_CHIEF_COMPLAINT]` | Specify the documented chief complaint | "[specify value]" |
| `[HISTORY_DOCUMENTATION_COMPLETENESS]` | Specify the history documentation completeness | "[specify value]" |
| `[PHYSICAL_EXAM_THOROUGHNESS]` | Specify the physical exam thoroughness | "[specify value]" |
| `[CLINICAL_ASSESSMENT_CLARITY]` | Specify the clinical assessment clarity | "[specify value]" |
| `[TREATMENT_PLAN_SPECIFICITY]` | Specify the treatment plan specificity | "[specify value]" |
| `[DOCUMENTED_DIFFERENTIALS]` | Specify the documented differentials | "[specify value]" |
| `[TEST_JUSTIFICATION]` | Specify the test justification | "[specify value]" |
| `[INTERPRETATION_DOCUMENTATION]` | Specify the interpretation documentation | "[specify value]" |
| `[CORRELATION_EXPLANATION]` | Specify the correlation explanation | "[specify value]" |
| `[CONSENT_DOCUMENTATION]` | Specify the consent documentation | "[specify value]" |
| `[RISK_COMMUNICATION_RECORD]` | Specify the risk communication record | "[specify value]" |
| `[COMPREHENSION_VERIFICATION]` | Specify the comprehension verification | "[specify value]" |
| `[SECOND_OPINION_DOCUMENTATION]` | Specify the second opinion documentation | "[specify value]" |
| `[STANDARD_COMPLIANCE]` | Specify the standard compliance | "[specify value]" |
| `[REVIEW_CRITERIA_MET]` | Specify the review criteria met | "[specify value]" |
| `[OUTCOME_MONITORING_PLAN]` | Specify the outcome monitoring plan | "[specify value]" |
| `[IMPROVEMENT_OPPORTUNITIES]` | Specify the improvement opportunities | "[specify value]" |
| `[SAFETY_EVENT_DOCUMENTATION]` | Specify the safety event documentation | "[specify value]" |

### 2. Physical Examination and Clinical Assessment

**Systematic Physical Examination Protocol:**
```
Vital Signs: Temperature [TEMPERATURE_VALUE]°F, Blood Pressure [SYSTOLIC_BP]/[DIASTOLIC_BP] mmHg, Heart Rate [HEART_RATE_VALUE] BPM, Respiratory Rate [RESPIRATORY_RATE_VALUE], Oxygen Saturation [O2_SAT_VALUE]% on [OXYGEN_DELIVERY_METHOD], Height [HEIGHT_MEASUREMENT], Weight [WEIGHT_MEASUREMENT], BMI [BMI_CALCULATION].

General Appearance: Patient appears [OVERALL_APPEARANCE], [DISTRESS_LEVEL], [NUTRITIONAL_STATUS], [HYDRATION_STATUS], [MENTAL_STATUS_DESCRIPTION].

Head, Eyes, Ears, Nose, Throat: [HEAD_EXAMINATION_FINDINGS], [EYE_EXAMINATION_DETAILS], [PUPIL_EXAMINATION], [FUNDOSCOPIC_FINDINGS], [EAR_EXAMINATION_RESULTS], [NASAL_EXAMINATION], [THROAT_EXAMINATION], [NECK_EXAMINATION], [LYMPH_NODE_ASSESSMENT].

Cardiovascular: [HEART_SOUNDS_DESCRIPTION], [MURMUR_PRESENCE], [PERIPHERAL_PULSES_ASSESSMENT], [CAPILLARY_REFILL_TIME], [JUGULAR_VENOUS_DISTENSION], [EDEMA_ASSESSMENT], [EXTREMITY_EXAMINATION].

Pulmonary: [CHEST_WALL_INSPECTION], [PERCUSSION_FINDINGS], [AUSCULTATION_RESULTS], [BREATH_SOUNDS_QUALITY], [ADVENTITIOUS_SOUNDS], [RESPIRATORY_EFFORT_DESCRIPTION].

Abdominal: [INSPECTION_FINDINGS], [AUSCULTATION_BOWEL_SOUNDS], [PERCUSSION_RESULTS], [PALPATION_FINDINGS], [ORGAN_ENLARGEMENT], [TENDERNESS_LOCATION], [GUARDING_REBOUND], [SPECIAL_MANEUVERS].

Musculoskeletal: [JOINT_EXAMINATION], [RANGE_OF_MOTION_ASSESSMENT], [MUSCLE_STRENGTH_TESTING], [DEFORMITY_PRESENCE], [SPINE_EXAMINATION], [GAIT_ASSESSMENT].

Neurological: [MENTAL_STATUS_EXAM], [CRANIAL_NERVE_ASSESSMENT], [MOTOR_EXAMINATION], [SENSORY_EXAMINATION], [REFLEX_TESTING], [CEREBELLAR_FUNCTION], [COORDINATION_TESTING].

Dermatological: [SKIN_COLOR_TEXTURE], [LESION_DESCRIPTION], [RASH_CHARACTERISTICS], [NAIL_EXAMINATION], [HAIR_ASSESSMENT].
```

### 3. Differential Diagnosis Development

**Clinical Reasoning and Hypothesis Generation:**
```
Based on the presentation of [CHIEF_COMPLAINT] in [PATIENT_DEMOGRAPHIC] with [KEY_RISK_FACTORS], the differential diagnosis includes:

### Primary Diagnostic Considerations
1. [MOST_LIKELY_DIAGNOSIS] - Probability: [LIKELIHOOD_PERCENTAGE]%
   Supporting Evidence: [SUPPORTING_SYMPTOM_1], [SUPPORTING_SIGN_1], [SUPPORTING_HISTORY_1]
   Contradicting Evidence: [CONTRADICTING_FACTOR_1]

2. [SECOND_LIKELY_DIAGNOSIS] - Probability: [LIKELIHOOD_PERCENTAGE_2]%
   Supporting Evidence: [SUPPORTING_SYMPTOM_2], [SUPPORTING_SIGN_2], [SUPPORTING_HISTORY_2]
   Contradicting Evidence: [CONTRADICTING_FACTOR_2]

3. [THIRD_LIKELY_DIAGNOSIS] - Probability: [LIKELIHOOD_PERCENTAGE_3]%
   Supporting Evidence: [SUPPORTING_SYMPTOM_3], [SUPPORTING_SIGN_3], [SUPPORTING_HISTORY_3]
   Contradicting Evidence: [CONTRADICTING_FACTOR_3]

### Secondary Considerations
- [ALTERNATIVE_DIAGNOSIS_1] - Consider due to [REASONING_1]
- [ALTERNATIVE_DIAGNOSIS_2] - Consider due to [REASONING_2]
- [ALTERNATIVE_DIAGNOSIS_3] - Consider due to [REASONING_3]

Must-Rule-Out Conditions (Life-Threatening):
- [EMERGENCY_CONDITION_1] - Rule out with [URGENT_TEST_1]
- [EMERGENCY_CONDITION_2] - Rule out with [URGENT_TEST_2]
- [EMERGENCY_CONDITION_3] - Rule out with [URGENT_TEST_3]

Red Flag Symptoms Present: [RED_FLAG_SYMPTOM_1], [RED_FLAG_SYMPTOM_2], [RED_FLAG_SYMPTOM_3]
Clinical Decision Rules Applied: [DECISION_RULE_1] with score [SCORE_1], [DECISION_RULE_2] with result [RESULT_2].
```

### 4. Diagnostic Testing Strategy

**Evidence-Based Investigation Protocol:**
```
### Initial Laboratory Studies
- [LAB_TEST_1]: Expected result [EXPECTED_RANGE_1], Clinical significance [SIGNIFICANCE_1]
- [LAB_TEST_2]: Expected result [EXPECTED_RANGE_2], Clinical significance [SIGNIFICANCE_2]
- [LAB_TEST_3]: Expected result [EXPECTED_RANGE_3], Clinical significance [SIGNIFICANCE_3]
- [SPECIAL_LAB_TEST]: Specific for [CONDITION_TESTED], Sensitivity [SENSITIVITY_PERCENTAGE]%, Specificity [SPECIFICITY_PERCENTAGE]%

Imaging Studies:
- [IMAGING_MODALITY_1]: Indication [INDICATION_1], Expected findings [EXPECTED_FINDINGS_1]
- [IMAGING_MODALITY_2]: Indication [INDICATION_2], Expected findings [EXPECTED_FINDINGS_2]
- [CONTRAST_STUDY]: Contraindications checked [CONTRAST_CONTRAINDICATIONS], Pre-medication [PRE_MEDICATION_PROTOCOL]

### Specialized Testing
- [FUNCTIONAL_TEST_1]: Purpose [TEST_PURPOSE_1], Preparation required [PATIENT_PREPARATION_1]
- [BIOPSY_PROCEDURE]: Location [BIOPSY_SITE], Technique [BIOPSY_METHOD], Pathology focus [PATHOLOGY_FOCUS]
- [CARDIAC_TESTING]: Type [CARDIAC_TEST_TYPE], Indication [CARDIAC_INDICATION], Contraindications [CARDIAC_CONTRAINDICATIONS]

### Microbiological Studies
- [CULTURE_TYPE_1]: Source [SPECIMEN_SOURCE_1], Expected organisms [EXPECTED_ORGANISMS_1]
- [MOLECULAR_TEST]: Target [TARGET_PATHOGEN], Turnaround time [RESULT_TIMEFRAME]
- [SEROLOGY_TEST]: Antibody/Antigen [SEROLOGY_TARGET], Interpretation [RESULT_INTERPRETATION]

Point-of-Care Testing:
- [POC_TEST_1]: Immediate result [IMMEDIATE_RESULT_1], Clinical action [CLINICAL_ACTION_1]
- [BEDSIDE_ULTRASOUND]: Target organ [ULTRASOUND_TARGET], Key findings [ULTRASOUND_FINDINGS]

Test Prioritization: [STAT_TESTS] for immediate results, [URGENT_TESTS] within [URGENT_TIMEFRAME], [ROUTINE_TESTS] for comprehensive evaluation.
```

### 5. Clinical Correlation and Interpretation

**Results Integration and Analysis:**
```
### Laboratory Results Analysis
- [LAB_RESULT_1]: Value [ACTUAL_VALUE_1] (Reference: [REFERENCE_RANGE_1]) - Interpretation: [CLINICAL_INTERPRETATION_1]
- [LAB_RESULT_2]: Value [ACTUAL_VALUE_2] (Reference: [REFERENCE_RANGE_2]) - Interpretation: [CLINICAL_INTERPRETATION_2]
- [CRITICAL_VALUE_ALERT]: [CRITICAL_LAB_VALUE] requires [IMMEDIATE_ACTION_REQUIRED]

Imaging Interpretation:
- [IMAGING_FINDING_1] on [IMAGING_STUDY_1] consistent with [PATHOLOGY_SUGGESTED_1]
- [IMAGING_FINDING_2] shows [ABNORMALITY_DESCRIPTION] measuring [MEASUREMENT_VALUE]
- [INCIDENTAL_FINDING]: [FINDING_DESCRIPTION] requiring [FOLLOW_UP_RECOMMENDATION]

### Clinical Correlation Matrix
History + Physical + Labs + Imaging = [DIAGNOSTIC_CONFIDENCE_LEVEL]%
Supporting factors: [SUPPORTING_EVIDENCE_WEIGHT]
Conflicting data: [CONFLICTING_INFORMATION_ANALYSIS]
Additional testing needed: [ADDITIONAL_TESTS_RATIONALE]

### Diagnostic Certainty Scale
- Definitive Diagnosis (>95%): [DEFINITIVE_DIAGNOSIS_CRITERIA]
- Highly Probable (85-95%): [PROBABLE_DIAGNOSIS_FEATURES]
- Possible (50-85%): [POSSIBLE_DIAGNOSIS_UNCERTAINTY]
- Unlikely (<50%): [ALTERNATIVE_EXPLANATIONS_NEEDED]
```

### 6. Collaborative Consultation and Second Opinions

**Multidisciplinary Diagnostic Approach:**
```
### Consultation Strategy
Primary Consultant: [SPECIALIST_TYPE_1] for [CONSULTATION_PURPOSE_1]
- Specific question: [CLINICAL_QUESTION_1]
- Urgency level: [CONSULTATION_URGENCY_1]
- Expected contribution: [SPECIALIST_EXPERTISE_1]

Secondary Consultant: [SPECIALIST_TYPE_2] for [CONSULTATION_PURPOSE_2]
- Specific question: [CLINICAL_QUESTION_2]
- Urgency level: [CONSULTATION_URGENCY_2]
- Expected contribution: [SPECIALIST_EXPERTISE_2]

### Multidisciplinary Team Meeting
Participants: [TEAM_MEMBER_1], [TEAM_MEMBER_2], [TEAM_MEMBER_3], [TEAM_MEMBER_4]
Case presentation focus: [PRESENTATION_FOCUS_AREAS]
Consensus building approach: [CONSENSUS_METHOD]
Documentation of decisions: [DECISION_DOCUMENTATION_PROCESS]

### Second Opinion Considerations
- Complex/Rare condition: [COMPLEXITY_ASSESSMENT]
- High-stakes diagnosis: [CONSEQUENCE_ANALYSIS]
- Patient/Family request: [PATIENT_PREFERENCE_CONSIDERATION]
- Institutional policy: [POLICY_REQUIREMENTS]

### Telemedicine Consultation
Platform: [TELEHEALTH_PLATFORM]
Technical requirements: [TECHNICAL_SETUP]
Information sharing: [DATA_SHARING_PROTOCOL]
Documentation: [TELEMEDICINE_DOCUMENTATION]
```

### 7. Diagnostic Accuracy and Quality Assurance

**Evidence-Based Validation Framework:**
```
### Test Performance Characteristics
- [DIAGNOSTIC_TEST_1]: Sensitivity [SENSITIVITY_VALUE_1]%, Specificity [SPECIFICITY_VALUE_1]%, PPV [PPV_VALUE_1]%, NPV [NPV_VALUE_1]%
- [DIAGNOSTIC_TEST_2]: Sensitivity [SENSITIVITY_VALUE_2]%, Specificity [SPECIFICITY_VALUE_2]%, PPV [PPV_VALUE_2]%, NPV [NPV_VALUE_2]%
- Pre-test probability: [PRETEST_PROBABILITY]%
- Post-test probability: [POSTTEST_PROBABILITY]%

Clinical Prediction Rules:
- [PREDICTION_RULE_1]: Score [RULE_SCORE_1], Risk category [RISK_CATEGORY_1]
- [PREDICTION_RULE_2]: Criteria met [CRITERIA_MET_2], Recommendation [RULE_RECOMMENDATION_2]
- Validation status: [RULE_VALIDATION_STATUS]

### Quality Metrics
- Time to diagnosis: [DIAGNOSIS_TIME_HOURS] hours
- Number of tests ordered: [TOTAL_TESTS_ORDERED]
- Cost-effectiveness: [DIAGNOSTIC_COST] per [OUTCOME_MEASURE]
- Patient satisfaction: [SATISFACTION_SCORE]/10
- Diagnostic accuracy rate: [ACCURACY_PERCENTAGE]%

### Error Prevention
Cognitive bias awareness: [BIAS_TYPE_1], [BIAS_TYPE_2], [BIAS_TYPE_3]
Safety nets: [SAFETY_MECHANISM_1], [SAFETY_MECHANISM_2]
Feedback loops: [FEEDBACK_SYSTEM_1], [FEEDBACK_SYSTEM_2]
```

### 8. Treatment Implications and Management Planning

**Diagnosis-to-Treatment Pathway:**
```
Confirmed Diagnosis: [FINAL_DIAGNOSIS] with [DIAGNOSTIC_CONFIDENCE_LEVEL]% certainty

### Immediate Management Requirements
- Urgent interventions: [URGENT_TREATMENT_1], [URGENT_TREATMENT_2]
- Monitoring needs: [MONITORING_PARAMETER_1], [MONITORING_PARAMETER_2]
- Safety considerations: [SAFETY_CONCERN_1], [SAFETY_CONCERN_2]

Treatment Planning:
- First-line therapy: [PRIMARY_TREATMENT_OPTION] with [EXPECTED_RESPONSE_TIME]
- Alternative options: [ALTERNATIVE_TREATMENT_1], [ALTERNATIVE_TREATMENT_2]
- Contraindications: [TREATMENT_CONTRAINDICATION_1], [TREATMENT_CONTRAINDICATION_2]

### Prognosis Assessment
- Short-term outlook: [SHORT_TERM_PROGNOSIS]
- Long-term prognosis: [LONG_TERM_PROGNOSIS]
- Factors affecting prognosis: [PROGNOSTIC_FACTOR_1], [PROGNOSTIC_FACTOR_2]

Follow-up Strategy:
- Next appointment: [FOLLOW_UP_TIMEFRAME]
- Monitoring schedule: [MONITORING_SCHEDULE]
- Response assessment: [RESPONSE_CRITERIA]
- Red flags for return: [WARNING_SIGNS_LIST]
```

### 9. Patient Communication and Shared Decision Making

**Diagnostic Disclosure and Education:**
```
### Communication Approach
Patient health literacy level: [LITERACY_ASSESSMENT]
Communication preferences: [COMMUNICATION_PREFERENCE]
Language considerations: [LANGUAGE_ACCOMMODATION]
Cultural factors: [CULTURAL_CONSIDERATIONS]

Diagnostic Explanation:
Diagnosis name: [DIAGNOSIS_IN_LAYMAN_TERMS]
What it means: [CONDITION_EXPLANATION]
Why it occurred: [CAUSATION_EXPLANATION]
What to expect: [EXPECTATION_SETTING]
Treatment necessity: [TREATMENT_RATIONALE]

### Risk Communication
Absolute risk: [ABSOLUTE_RISK_PERCENTAGE]%
Relative risk: [RELATIVE_RISK_COMPARISON]
Number needed to treat: [NNT_VALUE]
Visual aids used: [RISK_COMMUNICATION_TOOLS]

### Shared Decision Making
Treatment options presented: [OPTION_1], [OPTION_2], [OPTION_3]
Patient values explored: [PATIENT_VALUES_1], [PATIENT_VALUES_2]
Preference assessment: [PATIENT_PREFERENCE]
Decision support tools: [DECISION_AID_USED]
Final decision: [AGREED_TREATMENT_PLAN]
```

### 10. Documentation and Legal Considerations

**Comprehensive Record Keeping:**
```
### Medical Record Documentation
Chief complaint: [DOCUMENTED_CHIEF_COMPLAINT]
History details: [HISTORY_DOCUMENTATION_COMPLETENESS]
Physical exam: [PHYSICAL_EXAM_THOROUGHNESS]
Assessment: [CLINICAL_ASSESSMENT_CLARITY]
Plan: [TREATMENT_PLAN_SPECIFICITY]

Diagnostic Reasoning Documentation:
Differential diagnosis list: [DOCUMENTED_DIFFERENTIALS]
Rationale for testing: [TEST_JUSTIFICATION]
Results interpretation: [INTERPRETATION_DOCUMENTATION]
Clinical correlation: [CORRELATION_EXPLANATION]

### Legal and Regulatory Compliance
Informed consent: [CONSENT_DOCUMENTATION]
Risk disclosure: [RISK_COMMUNICATION_RECORD]
Patient understanding: [COMPREHENSION_VERIFICATION]
Second opinion offered: [SECOND_OPINION_DOCUMENTATION]
Standard of care adherence: [STANDARD_COMPLIANCE]

### Quality Assurance
Peer review eligibility: [REVIEW_CRITERIA_MET]
Outcome tracking: [OUTCOME_MONITORING_PLAN]
Continuous improvement: [IMPROVEMENT_OPPORTUNITIES]
Patient safety reporting: [SAFETY_EVENT_DOCUMENTATION]
```

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
### Example 1: Acute Chest Pain Evaluation
```
As a Emergency Medicine Physician with Emergency Medicine specialization working in Emergency Department with 10 years of experience, I am evaluating 55-year-old Male Caucasian presenting with chief complaint of Severe chest pain lasting 2 hours.

History of Present Illness: The Severe chest pain started Suddenly while climbing stairs and is characterized as Crushing, squeezing quality, 9/10 severity, Substernal location, with Radiating to left arm and jaw. The symptom is Worsened by Physical exertion and Not relieved by Rest or nitroglycerin.

Associated symptoms include Diaphoresis, Nausea, Shortness of breath, Lightheadedness, and Palpitations. Patient denies Fever, Cough, Recent trauma.

Based on the presentation of Severe chest pain in Middle-aged male with Diabetes, hypertension, smoking history, the differential diagnosis includes:

Primary Diagnostic Considerations:
1. ST-Elevation Myocardial Infarction - Probability: 85%
2. Non-ST-Elevation Myocardial Infarction - Probability: 10%
3. Unstable Angina - Probability: 5%
```

### Example 2: Pediatric Fever Investigation
```
As a Pediatrician with Pediatric Medicine specialization working in Pediatric Clinic with 8 years of experience, I am evaluating 3-year-old Female Hispanic presenting with chief complaint of High fever lasting 3 days.

History of Present Illness: The High fever started Gradually after daycare exposure and is characterized as Intermittent pattern, 103.2°F maximum, Generalized, with No specific radiation. The symptom is Worsened by Activity and Partially improved by Acetaminophen.

Associated symptoms include Decreased appetite, Fussiness, Runny nose, Cough, and Pulling at ears. Patient denies Vomiting, Diarrhea, Rash.

Based on the presentation of High fever in Toddler with Upper respiratory symptoms, daycare exposure, the differential diagnosis includes:

Primary Diagnostic Considerations:
1. Viral Upper Respiratory Infection - Probability: 60%
2. Acute Otitis Media - Probability: 25%
3. Bacterial Pneumonia - Probability: 10%
```

### Example 3: Chronic Abdominal Pain Workup
```
As a Gastroenterologist with Gastroenterology specialization working in Specialty Clinic with 15 years of experience, I am evaluating 42-year-old Female Asian presenting with chief complaint of Recurrent abdominal pain lasting 6 months.

History of Present Illness: The Recurrent abdominal pain started Insidiously without clear trigger and is characterized as Cramping, aching quality, 6/10 severity, Right lower quadrant, with No radiation. The symptom is Worsened by Fatty meals, stress and Improved by Bowel movements.

Associated symptoms include Alternating diarrhea and constipation, Bloating, Gas, Mucus in stool, and Fatigue. Patient denies Weight loss, Blood in stool, Fever.

Based on the presentation of Recurrent abdominal pain in Middle-aged female with Bowel habit changes, stress triggers, the differential diagnosis includes:

Primary Diagnostic Considerations:
1. Irritable Bowel Syndrome - Probability: 70%
2. Inflammatory Bowel Disease - Probability: 15%
3. Small Intestinal Bacterial Overgrowth - Probability: 10%
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Telemedicine Platform Design](telemedicine-platform-design.md)** - Complementary approaches and methodologies
- **[Patient Care Pathway](patient-care-pathway.md)** - Complementary approaches and methodologies
- **[Clinical Trials Management](clinical-trials-management.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Medical Diagnosis Template)
2. Use [Telemedicine Platform Design](telemedicine-platform-design.md) for deeper analysis
3. Apply [Patient Care Pathway](patient-care-pathway.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[healthcare/Medical & Clinical](../../healthcare/Medical & Clinical/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **General application**: Combine this template with related analytics and strategy frameworks
- **Professional use**: Combine this template with related analytics and strategy frameworks
- **Project implementation**: Combine this template with related analytics and strategy frameworks

## Customization Options

### 1. Specialty-Specific Adaptations
- **Emergency Medicine**: Emphasize rapid diagnosis, triage protocols, and life-threatening condition identification
- **Primary Care**: Focus on common conditions, preventive screening, and longitudinal care considerations
- **Internal Medicine**: Incorporate complex medical conditions, multiple comorbidities, and medication interactions
- **Pediatrics**: Include age-appropriate examination techniques, developmental considerations, and family dynamics
- **Geriatrics**: Address multiple comorbidities, medication complexity, and functional assessment integration

### 2. Clinical Setting Modifications
- **Inpatient Hospital**: Acute care focus, consultant availability, and resource-intensive diagnostics
- **Outpatient Clinics**: Cost-effective approaches, staged workups, and follow-up planning
- **Urgent Care Centers**: Limited resource availability, common condition focus, and referral protocols
- **Telemedicine Platforms**: Remote assessment techniques, technology limitations, and safety protocols
- **Rural Healthcare**: Limited specialist access, resource constraints, and transport considerations

### 3. Diagnostic Complexity Levels
- **Straightforward Diagnoses**: Streamlined approach for common, well-defined conditions
- **Complex Multi-system**: Comprehensive evaluation for conditions affecting multiple organ systems
- **Rare Diseases**: Literature review integration, expert consultation, and genetic considerations
- **Psychiatric Comorbidity**: Mental health screening integration and collaborative care approaches
- **Emergency Presentations**: Time-sensitive protocols and critical decision-making frameworks

### 4. Technology Integration Options
- **Basic Clinical Tools**: Standard examination techniques and traditional diagnostic approaches
- **Advanced Imaging**: CT, MRI, nuclear medicine, and interventional radiology integration
- **Point-of-Care Testing**: Bedside diagnostics, rapid tests, and immediate result interpretation
- **Artificial Intelligence**: Clinical decision support systems, pattern recognition, and predictive analytics
- **Genomic Medicine**: Genetic testing integration, hereditary condition evaluation, and personalized medicine approaches

### 5. Quality and Safety Enhancements
- **Patient Safety Focus**: Error prevention strategies, safety checklist integration, and adverse event prevention
- **Quality Metrics**: Performance measurement, outcome tracking, and continuous improvement integration
- **Evidence-Based Practice**: Literature integration, guideline adherence, and research application
- **Cultural Competency**: Diverse population considerations, language services, and cultural sensitivity
- **Legal Risk Management**: Documentation standards, informed consent protocols, and liability consideration

---

*This template provides a systematic approach to medical diagnosis that integrates clinical expertise with evidence-based medicine. The 400+ variables ensure comprehensive customization for diverse patient presentations, clinical settings, and diagnostic challenges while maintaining high standards of care quality and patient safety.*