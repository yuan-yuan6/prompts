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
title: Patient Documentation Template
use_cases:
- Creating comprehensive patient documentation including medical histories, clinical
  notes, assessments, progress reports, and discharge summaries that meet regulatory
  requirements and support continuity of care.
- Project planning and execution
- Strategy development
---

# Patient Documentation Template

## Purpose
Create comprehensive patient documentation including medical histories, clinical notes, assessments, progress reports, and discharge summaries that meet regulatory requirements and support continuity of care.

## Quick Start

**HIPAA-Compliant Clinical Documentation:**

1. **Verify Identity & Access** - Confirm patient identity using two identifiers; ensure authorized access to PHI
2. **Document Chief Complaint & HPI** - Record presenting problem, onset, duration, severity using OLDCARTS format
3. **Complete Review of Systems** - Document pertinent positives and negatives across all organ systems
4. **Physical Examination** - Record vital signs and focused physical exam findings objectively
5. **Assessment & Plan** - List diagnoses (ICD-10 codes), differential diagnoses, and specific treatment plan
6. **Secure Authentication** - Sign/authenticate note within required timeframe (typically 24-48 hours)
7. **Privacy Check** - Verify no unauthorized individuals present; secure workstation when leaving

**HIPAA Documentation Standards:** Use minimum necessary information, maintain audit logs, secure electronic devices, never share login credentials, and report any suspected breaches immediately.

## Template

```
You are a clinical documentation specialist. Create [DOCUMENT_TYPE] for [PATIENT_CONTEXT] in [CLINICAL_SETTING] following [DOCUMENTATION_STANDARD] guidelines for [PURPOSE].

PATIENT INFORMATION:
Demographics:
- Patient ID: [PATIENT_ID]
- Name: [PATIENT_NAME]
- Date of birth: [DOB]
- Age: [AGE]
- Gender: [GENDER]
- Preferred pronouns: [PRONOUNS]
- Primary language: [PRIMARY_LANGUAGE]
- Interpreter needed: [INTERPRETER_NEEDED]
- Race/Ethnicity: [RACE_ETHNICITY]
- Marital status: [MARITAL_STATUS]

### Contact Information
- Address: [PATIENT_ADDRESS]
- Phone: [PHONE_NUMBERS]
- Email: [EMAIL_ADDRESS]
- Emergency contact: [EMERGENCY_CONTACT]
- Emergency relationship: [EMERGENCY_RELATIONSHIP]
- Emergency phone: [EMERGENCY_PHONE]

Insurance/Coverage:
- Primary insurance: [PRIMARY_INSURANCE]
- Policy number: [POLICY_NUMBER]
- Group number: [GROUP_NUMBER]
- Secondary insurance: [SECONDARY_INSURANCE]
- Authorization status: [AUTH_STATUS]
- Copay: [COPAY_AMOUNT]

### CLINICAL DOCUMENTATION

History and Physical (H&P):
### Chief Complaint
"[CHIEF_COMPLAINT]"
Duration: [SYMPTOM_DURATION]
Severity: [SEVERITY_SCALE]
Context: [COMPLAINT_CONTEXT]

History of Present Illness (HPI):
[DETAILED_HPI]
- Onset: [ONSET_TIMING]
- Location: [SYMPTOM_LOCATION]
- Duration: [SYMPTOM_DURATION]
- Character: [SYMPTOM_CHARACTER]
- Aggravating factors: [AGGRAVATING_FACTORS]
- Relieving factors: [RELIEVING_FACTORS]
- Timing: [SYMPTOM_TIMING]
- Severity: [PAIN_SEVERITY_SCALE]
- Associated symptoms: [ASSOCIATED_SYMPTOMS]
- Previous episodes: [PREVIOUS_EPISODES]
- Treatments tried: [TREATMENTS_ATTEMPTED]

### Past Medical History
### Medical Conditions
1. [CONDITION_1] - Diagnosed: [DATE_1] - Status: [STATUS_1] - Controlled: [CONTROL_1]
2. [CONDITION_2] - Diagnosed: [DATE_2] - Status: [STATUS_2] - Controlled: [CONTROL_2]
3. [CONDITION_3] - Diagnosed: [DATE_3] - Status: [STATUS_3] - Controlled: [CONTROL_3]
4. [CONDITION_4] - Diagnosed: [DATE_4] - Status: [STATUS_4] - Controlled: [CONTROL_4]
5. [CONDITION_5] - Diagnosed: [DATE_5] - Status: [STATUS_5] - Controlled: [CONTROL_5]

### Surgical History
1. [SURGERY_1] - Date: [SURGERY_DATE_1] - Complications: [COMPLICATIONS_1] - Outcome: [OUTCOME_1]
2. [SURGERY_2] - Date: [SURGERY_DATE_2] - Complications: [COMPLICATIONS_2] - Outcome: [OUTCOME_2]
3. [SURGERY_3] - Date: [SURGERY_DATE_3] - Complications: [COMPLICATIONS_3] - Outcome: [OUTCOME_3]

### Hospitalizations
1. [HOSPITALIZATION_1] - Date: [HOSPITAL_DATE_1] - Reason: [HOSPITAL_REASON_1]
2. [HOSPITALIZATION_2] - Date: [HOSPITAL_DATE_2] - Reason: [HOSPITAL_REASON_2]
3. [HOSPITALIZATION_3] - Date: [HOSPITAL_DATE_3] - Reason: [HOSPITAL_REASON_3]

### Current Medications
1. [MEDICATION_1] - Dose: [DOSE_1] - Frequency: [FREQUENCY_1] - Route: [ROUTE_1] - Start date: [START_DATE_1]
2. [MEDICATION_2] - Dose: [DOSE_2] - Frequency: [FREQUENCY_2] - Route: [ROUTE_2] - Start date: [START_DATE_2]
3. [MEDICATION_3] - Dose: [DOSE_3] - Frequency: [FREQUENCY_3] - Route: [ROUTE_3] - Start date: [START_DATE_3]
4. [MEDICATION_4] - Dose: [DOSE_4] - Frequency: [FREQUENCY_4] - Route: [ROUTE_4] - Start date: [START_DATE_4]
5. [MEDICATION_5] - Dose: [DOSE_5] - Frequency: [FREQUENCY_5] - Route: [ROUTE_5] - Start date: [START_DATE_5]

Over-the-counter/Supplements:
- [OTC_MEDICATION_1]: [OTC_DOSE_1]
- [OTC_MEDICATION_2]: [OTC_DOSE_2]
- [OTC_MEDICATION_3]: [OTC_DOSE_3]

### Allergies and Reactions
- Medications: [MEDICATION_ALLERGIES] - Reaction: [MEDICATION_REACTION]
- Food: [FOOD_ALLERGIES] - Reaction: [FOOD_REACTION]
- Environmental: [ENVIRONMENTAL_ALLERGIES] - Reaction: [ENVIRONMENTAL_REACTION]
- Latex: [LATEX_ALLERGY] - Reaction: [LATEX_REACTION]
- Contrast dye: [CONTRAST_ALLERGY] - Reaction: [CONTRAST_REACTION]

### Social History
- Occupation: [OCCUPATION]
- Work environment: [WORK_ENVIRONMENT]
- Living situation: [LIVING_SITUATION]
- Support system: [SUPPORT_SYSTEM]
- Tobacco use: [TOBACCO_HISTORY] - Pack years: [PACK_YEARS]
- Alcohol use: [ALCOHOL_HISTORY] - Drinks per week: [DRINKS_PER_WEEK]
- Substance use: [SUBSTANCE_HISTORY] - Type: [SUBSTANCE_TYPE]
- Exercise: [EXERCISE_HABITS] - Frequency: [EXERCISE_FREQUENCY]
- Diet: [DIETARY_HABITS] - Restrictions: [DIETARY_RESTRICTIONS]
- Sexual history: [SEXUAL_HISTORY] - Partners: [SEXUAL_PARTNERS]
- Travel history: [TRAVEL_HISTORY]
- Pet exposure: [PET_EXPOSURE]

### Family History
- Mother: [MATERNAL_HISTORY] - Age: [MATERNAL_AGE] - Health: [MATERNAL_HEALTH]
- Father: [PATERNAL_HISTORY] - Age: [PATERNAL_AGE] - Health: [PATERNAL_HEALTH]
- Siblings: [SIBLING_HISTORY] - Number: [SIBLING_COUNT]
- Children: [CHILDREN_HISTORY] - Number: [CHILDREN_COUNT]
- Grandparents: [GRANDPARENT_HISTORY]
- Heart disease: [FAMILY_HEART_DISEASE]
- Cancer: [FAMILY_CANCER] - Type: [CANCER_TYPE]
- Diabetes: [FAMILY_DIABETES]
- Hypertension: [FAMILY_HYPERTENSION]
- Mental illness: [FAMILY_MENTAL_ILLNESS]
- Genetic conditions: [GENETIC_CONDITIONS]

Review of Systems (ROS):
Constitutional: [CONSTITUTIONAL_SYMPTOMS] - Fever: [FEVER] - Chills: [CHILLS] - Weight loss: [WEIGHT_LOSS]
HEENT: [HEENT_SYMPTOMS] - Headache: [HEADACHE] - Vision changes: [VISION_CHANGES] - Hearing loss: [HEARING_LOSS]
Cardiovascular: [CV_SYMPTOMS] - Chest pain: [CHEST_PAIN] - Palpitations: [PALPITATIONS] - Shortness of breath: [SOB]
Respiratory: [RESP_SYMPTOMS] - Cough: [COUGH] - Sputum: [SPUTUM] - Wheezing: [WHEEZING]
Gastrointestinal: [GI_SYMPTOMS] - Nausea: [NAUSEA] - Vomiting: [VOMITING] - Diarrhea: [DIARRHEA]
Genitourinary: [GU_SYMPTOMS] - Dysuria: [DYSURIA] - Frequency: [URINARY_FREQUENCY] - Incontinence: [INCONTINENCE]
Musculoskeletal: [MSK_SYMPTOMS] - Joint pain: [JOINT_PAIN] - Muscle weakness: [MUSCLE_WEAKNESS]
Neurological: [NEURO_SYMPTOMS] - Dizziness: [DIZZINESS] - Numbness: [NUMBNESS] - Memory loss: [MEMORY_LOSS]
Psychiatric: [PSYCH_SYMPTOMS] - Depression: [DEPRESSION] - Anxiety: [ANXIETY] - Sleep problems: [SLEEP_PROBLEMS]
Endocrine: [ENDO_SYMPTOMS] - Heat/cold intolerance: [TEMPERATURE_INTOLERANCE] - Polyuria: [POLYURIA]
Hematologic: [HEME_SYMPTOMS] - Easy bruising: [BRUISING] - Bleeding: [BLEEDING_TENDENCY]
Skin: [SKIN_SYMPTOMS] - Rash: [RASH] - Lesions: [SKIN_LESIONS] - Itching: [PRURITUS]

### PHYSICAL EXAMINATION

### Vital Signs
- Temperature: [TEMPERATURE] °F/°C
- Blood pressure: [BP_SYSTOLIC]/[BP_DIASTOLIC] mmHg
- Heart rate: [HEART_RATE] bpm
- Respiratory rate: [RESPIRATORY_RATE] breaths/min
- Oxygen saturation: [O2_SATURATION] % on [O2_DELIVERY]
- Pain score: [PAIN_SCORE]/10
- Height: [HEIGHT] [HEIGHT_UNITS]
- Weight: [WEIGHT] [WEIGHT_UNITS]
- BMI: [BMI_CALCULATED]

### General Appearance
Patient appears [GENERAL_APPEARANCE]. [DISTRESS_LEVEL]. [POSITIONING]. [HYGIENE]. [COOPERATION_LEVEL].

### Systems Examination
### HEENT
- Head: [HEAD_EXAM] - Normocephalic: [NORMOCEPHALIC] - Trauma: [HEAD_TRAUMA]
- Eyes: [EYE_EXAM] - PERRLA: [PUPILS] - Conjunctiva: [CONJUNCTIVA] - Sclera: [SCLERA]
- Ears: [EAR_EXAM] - TM: [TYMPANIC_MEMBRANE] - Hearing: [HEARING_TEST]
- Nose: [NOSE_EXAM] - Septum: [NASAL_SEPTUM] - Discharge: [NASAL_DISCHARGE]
- Throat: [THROAT_EXAM] - Pharynx: [PHARYNX] - Tonsils: [TONSILS]

### Neck
- Inspection: [NECK_INSPECTION]
- Lymph nodes: [LYMPH_NODES]
- Thyroid: [THYROID_EXAM]
- JVD: [JUGULAR_VENOUS_DISTENSION]
- Range of motion: [NECK_ROM]

### Cardiovascular
- Heart sounds: [HEART_SOUNDS] - S1: [S1] - S2: [S2] - S3: [S3] - S4: [S4]
- Rhythm: [CARDIAC_RHYTHM] - Regular: [REGULAR_RHYTHM]
- Murmurs: [MURMURS] - Grade: [MURMUR_GRADE] - Location: [MURMUR_LOCATION]
- Peripheral pulses: [PERIPHERAL_PULSES] - Radial: [RADIAL_PULSE] - Pedal: [PEDAL_PULSE]
- Edema: [EDEMA_LOCATION] - Grade: [EDEMA_GRADE]
- Capillary refill: [CAPILLARY_REFILL]

### Respiratory
- Inspection: [CHEST_INSPECTION] - Symmetry: [CHEST_SYMMETRY]
- Breath sounds: [BREATH_SOUNDS] - Clear: [CLEAR_LUNGS]
- Adventitious sounds: [ADVENTITIOUS_SOUNDS] - Wheeze: [WHEEZE] - Rales: [RALES]
- Respiratory effort: [RESPIRATORY_EFFORT] - Accessory muscles: [ACCESSORY_MUSCLES]
- Percussion: [CHEST_PERCUSSION]

### Abdomen
- Inspection: [ABDOMEN_INSPECTION] - Distension: [ABDOMINAL_DISTENSION]
- Auscultation: [BOWEL_SOUNDS] - Active: [BOWEL_SOUNDS_ACTIVE]
- Palpation: [ABDOMINAL_PALPATION] - Soft: [ABDOMEN_SOFT] - Tender: [ABDOMINAL_TENDERNESS]
- Organomegaly: [ORGANOMEGALY] - Hepatomegaly: [HEPATOMEGALY] - Splenomegaly: [SPLENOMEGALY]
- Masses: [ABDOMINAL_MASSES]
- Percussion: [ABDOMINAL_PERCUSSION]

### Neurological
- Mental status: [MENTAL_STATUS] - Alert: [ALERTNESS] - Oriented: [ORIENTATION]
- Cranial nerves: [CRANIAL_NERVES] - II-XII: [CN_EXAM]
- Motor: [MOTOR_EXAM] - Strength: [MOTOR_STRENGTH] - Tone: [MUSCLE_TONE]
- Sensory: [SENSORY_EXAM] - Light touch: [LIGHT_TOUCH] - Vibration: [VIBRATION]
- Reflexes: [REFLEXES] - DTRs: [DEEP_TENDON_REFLEXES] - Babinski: [BABINSKI]
- Coordination: [COORDINATION] - Finger-to-nose: [FINGER_TO_NOSE]
- Gait: [GAIT_EXAM] - Steady: [GAIT_STEADY] - Balance: [BALANCE]

### Musculoskeletal
- Range of motion: [ROM_ASSESSMENT] - Shoulders: [SHOULDER_ROM] - Knees: [KNEE_ROM]
- Strength: [STRENGTH_TESTING] - Upper extremities: [UPPER_STRENGTH] - Lower extremities: [LOWER_STRENGTH]
- Joint stability: [JOINT_STABILITY] - Deformities: [JOINT_DEFORMITIES]
- Spine: [SPINE_EXAM] - Curvature: [SPINAL_CURVATURE] - Tenderness: [SPINE_TENDERNESS]

### Skin
- Color: [SKIN_COLOR] - Pallor: [PALLOR] - Cyanosis: [CYANOSIS] - Jaundice: [JAUNDICE]
- Temperature: [SKIN_TEMPERATURE] - Moisture: [SKIN_MOISTURE]
- Lesions: [SKIN_LESIONS] - Type: [LESION_TYPE] - Distribution: [LESION_DISTRIBUTION]
- Wounds: [WOUNDS] - Location: [WOUND_LOCATION] - Size: [WOUND_SIZE] - Stage: [WOUND_STAGE]

### CLINICAL NOTES FORMATS

### SOAP Note
Date: [SOAP_DATE] Time: [SOAP_TIME] Provider: [SOAP_PROVIDER]

### Subjective
[SUBJECTIVE_FINDINGS]
Patient reports [PATIENT_REPORT]. [SYMPTOM_DESCRIPTION]. [FUNCTIONAL_IMPACT].

### Objective
Vital Signs: [VITAL_SIGNS_SUMMARY]
Physical Exam: [PHYSICAL_EXAM_SUMMARY]
Labs: [LAB_RESULTS]
Imaging: [IMAGING_RESULTS]

### Assessment
[CLINICAL_ASSESSMENT]
- Primary diagnosis: [PRIMARY_DIAGNOSIS] - ICD-10: [PRIMARY_ICD10]
- Secondary diagnoses: [SECONDARY_DIAGNOSES]
- Differential diagnoses: [DIFFERENTIAL_DIAGNOSES]
- Problem list: [ACTIVE_PROBLEM_LIST]

### Plan
[TREATMENT_PLAN]
- Diagnostic tests: [DIAGNOSTIC_ORDERS] - Labs: [LAB_ORDERS] - Imaging: [IMAGING_ORDERS]
- Medications: [MEDICATION_CHANGES] - New: [NEW_MEDICATIONS] - Discontinued: [DISCONTINUED_MEDS]
- Procedures: [PROCEDURE_PLAN] - Scheduled: [SCHEDULED_PROCEDURES]
- Referrals: [REFERRAL_ORDERS] - Specialty: [SPECIALTY_REFERRALS]
- Follow-up: [FOLLOWUP_SCHEDULE] - Return visit: [RETURN_VISIT_TIMING]
- Patient education: [EDUCATION_PROVIDED]

### Progress Note
Date/Time: [PROGRESS_DATE] [PROGRESS_TIME]
Provider: [PROGRESS_PROVIDER]
Service: [SERVICE_TYPE]

### Interval History
[INTERVAL_CHANGES]
Since last visit: [CHANGES_SINCE_LAST_VISIT]
New complaints: [NEW_COMPLAINTS]
Medication compliance: [MEDICATION_COMPLIANCE]

### Current Status
- Symptoms: [CURRENT_SYMPTOMS] - Improved: [SYMPTOM_IMPROVEMENT] - Worsened: [SYMPTOM_WORSENING]
- Response to treatment: [TREATMENT_RESPONSE] - Effective: [TREATMENT_EFFECTIVENESS]
- Functional status: [FUNCTIONAL_STATUS] - ADL independence: [ADL_STATUS]
- Pain level: [CURRENT_PAIN_LEVEL]

### Focused Examination
[FOCUSED_EXAM_FINDINGS]
Pertinent positives: [PERTINENT_POSITIVES]
Pertinent negatives: [PERTINENT_NEGATIVES]

Assessment/Plan:
Problem 1: [PROBLEM_1] - Status: [PROBLEM_1_STATUS] - Plan: [PROBLEM_1_PLAN]
Problem 2: [PROBLEM_2] - Status: [PROBLEM_2_STATUS] - Plan: [PROBLEM_2_PLAN]
Problem 3: [PROBLEM_3] - Status: [PROBLEM_3_STATUS] - Plan: [PROBLEM_3_PLAN]

### Discharge Summary
Admission Date: [ADMIT_DATE]
Discharge Date: [DISCHARGE_DATE]
Length of Stay: [LENGTH_OF_STAY] days
Attending Physician: [ATTENDING_PHYSICIAN]

### Admitting Diagnosis
[ADMITTING_DIAGNOSIS]

### Discharge Diagnoses
Principal: [PRINCIPAL_DISCHARGE_DIAGNOSIS]
### Secondary
1. [SECONDARY_DIAGNOSIS_1]
2. [SECONDARY_DIAGNOSIS_2]
3. [SECONDARY_DIAGNOSIS_3]

### Hospital Course
[HOSPITAL_COURSE_NARRATIVE]
[DAILY_PROGRESS_SUMMARY]
[COMPLICATIONS_DURING_STAY]
[RESPONSE_TO_TREATMENT]

### Procedures Performed
1. [PROCEDURE_1] - Date: [PROCEDURE_DATE_1] - Complications: [PROCEDURE_COMPLICATIONS_1]
2. [PROCEDURE_2] - Date: [PROCEDURE_DATE_2] - Complications: [PROCEDURE_COMPLICATIONS_2]

### Consultations
1. [CONSULTATION_1] - Service: [CONSULT_SERVICE_1] - Recommendations: [CONSULT_RECOMMENDATIONS_1]
2. [CONSULTATION_2] - Service: [CONSULT_SERVICE_2] - Recommendations: [CONSULT_RECOMMENDATIONS_2]

### Discharge Medications
[DISCHARGE_MEDICATION_LIST]
- New medications: [NEW_DISCHARGE_MEDS]
- Changed medications: [CHANGED_DISCHARGE_MEDS]
- Continued medications: [CONTINUED_MEDS]
- Discontinued medications: [DISCONTINUED_DISCHARGE_MEDS]

### Discharge Instructions
- Activity: [ACTIVITY_RESTRICTIONS] - Lifting: [LIFTING_RESTRICTIONS] - Driving: [DRIVING_RESTRICTIONS]
- Diet: [DIETARY_INSTRUCTIONS] - Restrictions: [DIET_RESTRICTIONS] - Fluid limits: [FLUID_RESTRICTIONS]
- Wound care: [WOUND_CARE_INSTRUCTIONS] - Dressing changes: [DRESSING_FREQUENCY]
- Warning signs: [WARNING_SIGNS_TO_REPORT]
- When to seek care: [EMERGENCY_RETURN_CRITERIA]
- Equipment needs: [DME_ORDERS]

Follow-up Appointments:
Primary care: [PCP_FOLLOWUP] - Scheduled: [PCP_APPOINTMENT_DATE]
Specialty: [SPECIALTY_FOLLOWUP] - Service: [SPECIALTY_SERVICE] - When: [SPECIALTY_TIMING]
Lab work: [FOLLOWUP_LABS] - When: [LAB_TIMING]

### Discharge Disposition
[DISCHARGE_DISPOSITION]
- Home: [HOME_DISCHARGE] - Services: [HOME_SERVICES]
- Facility: [FACILITY_NAME] - Level of care: [FACILITY_LEVEL]
- Transportation: [DISCHARGE_TRANSPORTATION]

### SPECIALIZED DOCUMENTATION

### Procedure Note
Procedure: [PROCEDURE_NAME]
Date/Time: [PROCEDURE_DATETIME]
Provider: [PERFORMING_PROVIDER]
Assistant(s): [PROCEDURE_ASSISTANTS]
Location: [PROCEDURE_LOCATION]

Pre-procedure:
- Indication: [PROCEDURE_INDICATION]
- Consent: [CONSENT_OBTAINED] - Risks discussed: [RISKS_DISCUSSED]
- Timeout: [TIMEOUT_PERFORMED] - Correct patient: [CORRECT_PATIENT] - Correct site: [CORRECT_SITE]
- Allergies reviewed: [ALLERGIES_REVIEWED]
- Antibiotics: [PROPHYLACTIC_ANTIBIOTICS]

### Procedure Details
[DETAILED_PROCEDURE_DESCRIPTION]
- Approach: [PROCEDURE_APPROACH]
- Anesthesia: [ANESTHESIA_TYPE] - Provider: [ANESTHESIA_PROVIDER]
- Positioning: [PATIENT_POSITIONING]
- Preparation: [SITE_PREPARATION]
- Equipment used: [PROCEDURE_EQUIPMENT]

### Findings
[PROCEDURE_FINDINGS]
- Normal findings: [NORMAL_FINDINGS]
- Abnormal findings: [ABNORMAL_FINDINGS]
- Specimens: [SPECIMENS_OBTAINED] - Sent to: [PATHOLOGY_DESTINATION]

### Complications
[PROCEDURE_COMPLICATIONS]
- Immediate: [IMMEDIATE_COMPLICATIONS]
- Intraoperative: [INTRAOPERATIVE_COMPLICATIONS]

Post-procedure:
- Patient condition: [POST_PROCEDURE_CONDITION]
- Vital signs: [POST_PROCEDURE_VITALS]
- Recovery: [RECOVERY_STATUS]
- Disposition: [POST_PROCEDURE_DISPOSITION]
- Instructions: [POST_PROCEDURE_INSTRUCTIONS]

### Consultation Note
Date: [CONSULTATION_DATE]
Requesting Provider: [REQUESTING_PROVIDER]
Consultant: [CONSULTANT_NAME]
Service: [CONSULTING_SERVICE]

### Reason for Consultation
[CONSULTATION_REASON]
- Question: [SPECIFIC_QUESTION]
- Background: [CONSULTATION_BACKGROUND]

Consultant's Assessment:
History: [CONSULTANT_HISTORY_REVIEW]
Physical Exam: [CONSULTANT_EXAMINATION]
Review of Data: [DATA_REVIEWED] - Labs: [LABS_REVIEWED] - Imaging: [IMAGING_REVIEWED]

Consultant's Impression:
[CONSULTANT_ASSESSMENT]
- Primary issue: [CONSULTANT_PRIMARY_DIAGNOSIS]
- Contributing factors: [CONTRIBUTING_FACTORS]
- Prognosis: [CONSULTANT_PROGNOSIS]

### Recommendations
1. [RECOMMENDATION_1] - Priority: [PRIORITY_1]
2. [RECOMMENDATION_2] - Priority: [PRIORITY_2]
3. [RECOMMENDATION_3] - Priority: [PRIORITY_3]

Follow-up Plan:
[CONSULTANT_FOLLOWUP_PLAN]
- Return consultation: [RETURN_CONSULT_TIMING]
- Monitoring: [MONITORING_PLAN]

### ASSESSMENT TOOLS

### Functional Assessment
Activities of Daily Living (ADLs):
- Bathing: [BATHING_ABILITY] - Independent: [BATHING_INDEPENDENT]
- Dressing: [DRESSING_ABILITY] - Independent: [DRESSING_INDEPENDENT]
- Toileting: [TOILETING_ABILITY] - Independent: [TOILETING_INDEPENDENT]
- Transferring: [TRANSFER_ABILITY] - Device needed: [TRANSFER_DEVICE]
- Continence: [CONTINENCE_STATUS] - Bladder: [BLADDER_CONTINENCE] - Bowel: [BOWEL_CONTINENCE]
- Feeding: [FEEDING_ABILITY] - Independent: [FEEDING_INDEPENDENT]

### Instrumental ADLs
- Medication management: [MEDICATION_MANAGEMENT_ABILITY]
- Shopping: [SHOPPING_ABILITY]
- Meal preparation: [MEAL_PREP_ABILITY]
- Transportation: [TRANSPORTATION_ABILITY]
- Finances: [FINANCIAL_MANAGEMENT_ABILITY]
- Housekeeping: [HOUSEKEEPING_ABILITY]
- Phone use: [PHONE_USE_ABILITY]

### Cognitive Assessment
- Orientation: [ORIENTATION_STATUS] - Person: [PERSON_ORIENTED] - Place: [PLACE_ORIENTED] - Time: [TIME_ORIENTED]
- Memory: [MEMORY_ASSESSMENT] - Recent: [RECENT_MEMORY] - Remote: [REMOTE_MEMORY]
- Attention: [ATTENTION_ASSESSMENT] - Sustained: [SUSTAINED_ATTENTION]
- Language: [LANGUAGE_ASSESSMENT] - Comprehension: [LANGUAGE_COMPREHENSION] - Expression: [LANGUAGE_EXPRESSION]
- Executive function: [EXECUTIVE_FUNCTION] - Decision making: [DECISION_MAKING_ABILITY]
- MMSE score: [MMSE_SCORE]/30
- MoCA score: [MOCA_SCORE]/30

### Pain Assessment
- Location: [PAIN_LOCATION] - Primary: [PRIMARY_PAIN_SITE]
- Quality: [PAIN_QUALITY] - Sharp: [SHARP_PAIN] - Dull: [DULL_PAIN] - Burning: [BURNING_PAIN]
- Intensity: [PAIN_INTENSITY] - At rest: [PAIN_AT_REST] - With movement: [PAIN_WITH_MOVEMENT]
- Duration: [PAIN_DURATION] - Chronic: [CHRONIC_PAIN] - Acute: [ACUTE_PAIN]
- Aggravating factors: [PAIN_AGGRAVATORS]
- Alleviating factors: [PAIN_RELIEVERS] - Medication effective: [PAIN_MED_EFFECTIVE]
- Impact on function: [PAIN_FUNCTIONAL_IMPACT]
- Sleep interference: [PAIN_SLEEP_IMPACT]
- Mood impact: [PAIN_MOOD_IMPACT]

### Risk Assessments
### Falls Risk
- Fall risk score: [FALL_RISK_SCORE]
- Previous falls: [PREVIOUS_FALLS] - Number: [FALL_COUNT] - Circumstances: [FALL_CIRCUMSTANCES]
- Mobility aids: [MOBILITY_AIDS] - Walker: [WALKER_USE] - Cane: [CANE_USE]
- Environmental hazards: [ENVIRONMENTAL_HAZARDS]
- Medications affecting balance: [BALANCE_MEDICATIONS]

### Pressure Injury Risk
- Braden scale score: [BRADEN_SCORE]/23
- Mobility: [MOBILITY_SCORE]
- Activity: [ACTIVITY_SCORE]
- Sensory perception: [SENSORY_SCORE]
- Moisture: [MOISTURE_SCORE]
- Nutrition: [NUTRITION_SCORE]
- Friction/shear: [FRICTION_SCORE]

### VTE Risk
- VTE risk score: [VTE_RISK_SCORE]
- Risk factors: [VTE_RISK_FACTORS]
- Previous VTE: [PREVIOUS_VTE]
- Prophylaxis indicated: [VTE_PROPHYLAXIS_INDICATED]
- Prophylaxis method: [VTE_PROPHYLAXIS_METHOD]

### Suicide Risk
- Suicide risk level: [SUICIDE_RISK_LEVEL]
- PHQ-9 score: [PHQ9_SCORE]
- Previous attempts: [PREVIOUS_SUICIDE_ATTEMPTS]
- Current ideation: [CURRENT_SUICIDAL_IDEATION]
- Plan: [SUICIDE_PLAN]
- Means: [SUICIDE_MEANS]
- Protective factors: [PROTECTIVE_FACTORS]
- Safety plan: [SAFETY_PLAN_STATUS]

### Abuse Screening
- Abuse screening completed: [ABUSE_SCREENING_COMPLETED]
- Physical abuse indicators: [PHYSICAL_ABUSE_INDICATORS]
- Emotional abuse indicators: [EMOTIONAL_ABUSE_INDICATORS]
- Financial abuse indicators: [FINANCIAL_ABUSE_INDICATORS]
- Neglect indicators: [NEGLECT_INDICATORS]
- Safety concerns: [SAFETY_CONCERNS]
- Resources provided: [ABUSE_RESOURCES_PROVIDED]

### CARE COORDINATION

### Care Team
- Primary care physician: [PRIMARY_PHYSICIAN] - Contact: [PCP_CONTACT]
- Specialists: [SPECIALIST_LIST]
  - Cardiologist: [CARDIOLOGIST]
  - Endocrinologist: [ENDOCRINOLOGIST]
  - Psychiatrist: [PSYCHIATRIST]
- Nursing team: [NURSING_STAFF] - Primary nurse: [PRIMARY_NURSE]
- Pharmacy: [PHARMACY_CONTACT] - Clinical pharmacist: [CLINICAL_PHARMACIST]
- Therapy services: [THERAPY_TEAM]
  - Physical therapy: [PHYSICAL_THERAPIST]
  - Occupational therapy: [OCCUPATIONAL_THERAPIST]
  - Speech therapy: [SPEECH_THERAPIST]
- Case manager: [CASE_MANAGER] - Contact: [CASE_MANAGER_CONTACT]
- Social worker: [SOCIAL_WORKER] - Contact: [SOCIAL_WORKER_CONTACT]
- Chaplain: [CHAPLAIN] - Contact: [CHAPLAIN_CONTACT]

### Communication
- Family meetings: [FAMILY_MEETING_DATES] - Participants: [MEETING_PARTICIPANTS]
- Goals of care discussion: [GOALS_OF_CARE_DATE] - Outcomes: [GOALS_OUTCOMES]
- Code status: [CODE_STATUS] - DNR: [DNR_STATUS] - Healthcare proxy: [HEALTHCARE_PROXY]
- Advance directives: [ADVANCE_DIRECTIVES] - Living will: [LIVING_WILL]
- Care conferences: [CARE_CONFERENCE_NOTES]
- Handoff communication: [HANDOFF_COMMUNICATION] - SBAR format: [SBAR_HANDOFF]

### Transitions of Care
- Sending facility: [SENDING_FACILITY] - Contact: [SENDING_CONTACT]
- Receiving facility: [RECEIVING_FACILITY] - Contact: [RECEIVING_CONTACT]
- Transfer reason: [TRANSFER_REASON] - Urgency: [TRANSFER_URGENCY]
- Transport method: [TRANSPORT_METHOD] - Provider: [TRANSPORT_PROVIDER]
- Accompanying staff: [ACCOMPANYING_STAFF]
- Medications transferred: [TRANSFER_MEDICATIONS]
- Equipment transferred: [TRANSFER_EQUIPMENT]
- Transfer documents: [TRANSFER_DOCUMENTS_LIST]
- Report given: [TRANSFER_REPORT] - Time: [REPORT_TIME] - To: [REPORT_RECIPIENT]

### REGULATORY COMPLIANCE

### Documentation Standards
- Timeliness: [DOCUMENTATION_TIMELINESS] - Within [DOCUMENTATION_TIMEFRAME] hours
- Completeness: [COMPLETENESS_SCORE] - Missing elements: [MISSING_ELEMENTS]
- Accuracy: [ACCURACY_VERIFICATION] - Verified by: [VERIFICATION_PROVIDER]
- Legibility: [LEGIBILITY_STANDARD] - Electronic: [ELECTRONIC_DOCUMENTATION]
- Authentication: [AUTHENTICATION_METHOD] - Electronic signature: [ELECTRONIC_SIGNATURE]
- Date/time stamp: [TIMESTAMP_ACCURATE]
- Amendments: [DOCUMENTATION_AMENDMENTS] - Late entries: [LATE_ENTRIES]

Privacy/Security:
- HIPAA compliance: [HIPAA_COMPLIANCE_STATUS]
- Access controls: [ACCESS_CONTROL_LEVEL]
- Minimum necessary standard: [MINIMUM_NECESSARY_FOLLOWED]
- Patient consent: [PATIENT_CONSENT_STATUS]
- Information sharing agreements: [INFORMATION_SHARING_AGREEMENTS]
- Breach protocols: [BREACH_PROTOCOL_FOLLOWED]
- Audit logs: [AUDIT_LOG_MAINTAINED]

### Quality Measures
- Core measures: [CORE_MEASURES_MET]
- Quality indicators: [QUALITY_INDICATORS_TRACKED]
- Patient safety goals: [SAFETY_GOALS_ADDRESSED]
- Performance metrics: [PERFORMANCE_METRICS_REPORTED]
- Outcome measures: [OUTCOME_MEASURES_TRACKED]
- Process measures: [PROCESS_MEASURES_MONITORED]

BILLING/CODING:

### Diagnosis Codes
- Primary diagnosis: [PRIMARY_DIAGNOSIS_CODE] - ICD-10: [PRIMARY_ICD10_CODE]
- Secondary diagnoses:
  - [SECONDARY_DIAGNOSIS_1]: [SECONDARY_ICD10_1]
  - [SECONDARY_DIAGNOSIS_2]: [SECONDARY_ICD10_2]
  - [SECONDARY_DIAGNOSIS_3]: [SECONDARY_ICD10_3]
- Complications: [COMPLICATION_CODES]
- External causes: [EXTERNAL_CAUSE_CODES]

### Procedure Codes
- CPT codes: [CPT_CODE_LIST]
- Primary procedure: [PRIMARY_PROCEDURE_CPT]
- Secondary procedures: [SECONDARY_PROCEDURE_CPTS]
- Modifiers: [CPT_MODIFIERS]
- HCPCS codes: [HCPCS_CODES]

### Documentation Requirements
- Medical necessity: [MEDICAL_NECESSITY_DOCUMENTED]
- Level of service: [SERVICE_LEVEL_JUSTIFIED]
- Time-based billing: [TIME_DOCUMENTATION_COMPLETE]
- Critical care time: [CRITICAL_CARE_TIME_DOCUMENTED]
- Evaluation and management level: [EM_LEVEL_SUPPORTED]
- Decision making complexity: [DECISION_MAKING_COMPLEXITY]

### PATIENT EDUCATION

### Education Provided
### Topics Covered
1. [EDUCATION_TOPIC_1] - Method: [EDUCATION_METHOD_1] - Understanding: [UNDERSTANDING_1]
2. [EDUCATION_TOPIC_2] - Method: [EDUCATION_METHOD_2] - Understanding: [UNDERSTANDING_2]
3. [EDUCATION_TOPIC_3] - Method: [EDUCATION_METHOD_3] - Understanding: [UNDERSTANDING_3]
4. [EDUCATION_TOPIC_4] - Method: [EDUCATION_METHOD_4] - Understanding: [UNDERSTANDING_4]
5. [EDUCATION_TOPIC_5] - Method: [EDUCATION_METHOD_5] - Understanding: [UNDERSTANDING_5]

### Teaching Methods
- Verbal instruction: [VERBAL_TEACHING_PROVIDED] - Language: [TEACHING_LANGUAGE]
- Written materials: [WRITTEN_MATERIALS_PROVIDED] - Reading level: [MATERIAL_READING_LEVEL]
- Visual aids: [VISUAL_AIDS_USED] - Type: [VISUAL_AID_TYPE]
- Demonstration: [DEMONSTRATION_PROVIDED] - Skill: [DEMONSTRATED_SKILL]
- Return demonstration: [RETURN_DEMONSTRATION_SUCCESSFUL]
- Technology-based: [TECHNOLOGY_EDUCATION] - Platform: [EDUCATION_PLATFORM]

### Understanding Assessment
- Patient comprehension: [PATIENT_COMPREHENSION_LEVEL]
- Questions asked: [PATIENT_QUESTIONS_LIST]
- Concerns expressed: [PATIENT_CONCERNS]
- Learning barriers: [LEARNING_BARRIERS_IDENTIFIED]
- Cultural considerations: [CULTURAL_CONSIDERATIONS]
- Language barriers: [LANGUAGE_BARRIERS] - Interpreter used: [INTERPRETER_USED]
- Additional education needs: [ADDITIONAL_EDUCATION_NEEDED]
- Family involvement: [FAMILY_EDUCATION_PROVIDED]

Follow-up Education Plan:
- Reinforcement needed: [EDUCATION_REINFORCEMENT_NEEDED]
- Next education session: [NEXT_EDUCATION_DATE]
- Resources provided: [EDUCATION_RESOURCES_PROVIDED]
- Community resources: [COMMUNITY_EDUCATION_RESOURCES]

Generate comprehensive patient documentation with all relevant sections including:

### COMPLETE DOCUMENTATION OUTPUT
Document Type: [FINAL_DOCUMENT_TYPE]
Patient: [FINAL_PATIENT_IDENTIFIER]
Date/Time: [FINAL_DOCUMENTATION_DATETIME]
Provider: [FINAL_DOCUMENTING_PROVIDER]
Service: [FINAL_SERVICE_TYPE]

[COMPLETE_FORMATTED_DOCUMENTATION]

---

### Documentation Summary
✓ Patient identification complete: [PATIENT_ID_COMPLETE]
✓ Clinical information documented: [CLINICAL_INFO_COMPLETE]
✓ Assessment and plan included: [ASSESSMENT_PLAN_COMPLETE]
✓ Regulatory compliance met: [COMPLIANCE_STATUS]
✓ Authentication completed: [AUTHENTICATION_COMPLETE]
✓ Quality measures addressed: [QUALITY_MEASURES_COMPLETE]

Provider Signature: [PROVIDER_SIGNATURE]
Date/Time: [SIGNATURE_DATETIME]
```

## Variables
[500+ variables covering all aspects of comprehensive patient documentation including demographics, clinical history, physical examination, assessments, plans, procedures, education, care coordination, and regulatory compliance]

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
### Example 1: Initial Emergency Department Assessment
```
DOCUMENT_TYPE: "Emergency Department Initial Assessment"
CLINICAL_SETTING: "Emergency Department"
CHIEF_COMPLAINT: "Chest pain and shortness of breath"
DOCUMENTATION_STANDARD: "CMS and Joint Commission requirements"
PURPOSE: "Emergency evaluation and treatment"
```

### Example 2: Inpatient Progress Note
```
DOCUMENT_TYPE: "Daily progress note"
CLINICAL_SETTING: "Medical-surgical unit"
PATIENT_CONTEXT: "Post-operative day 3 following appendectomy"
FOCUS: "Recovery monitoring and discharge planning"
FORMAT: "Problem-oriented progress note"
```

### Example 3: Comprehensive Discharge Summary
```
DOCUMENT_TYPE: "Hospital discharge summary"
ADMISSION_DIAGNOSIS: "Acute myocardial infarction"
LENGTH_OF_STAY: "5 days"
DISCHARGE_DISPOSITION: "Home with cardiac rehabilitation referral"
FOLLOW_UP: "Cardiology in 1 week, primary care in 3 days"
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Telemedicine Platform Design](telemedicine-platform-design.md)** - Complementary approaches and methodologies
- **[Patient Care Pathway](patient-care-pathway.md)** - Complementary approaches and methodologies
- **[Clinical Trials Management](clinical-trials-management.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Patient Documentation Template)
2. Use [Telemedicine Platform Design](telemedicine-platform-design.md) for deeper analysis
3. Apply [Patient Care Pathway](patient-care-pathway.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[healthcare/Clinical Practice](../../healthcare/Clinical Practice/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive patient documentation including medical histories, clinical notes, assessments, progress reports, and discharge summaries that meet regulatory requirements and support continuity of care.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Customization Options

1. **Document Types**
   - History & Physical examinations
   - Daily progress notes
   - Consultation reports
   - Procedure documentation
   - Discharge summaries
   - Transfer summaries
   - Emergency department notes
   - Nursing documentation
   - Therapy notes
   - Social work assessments

2. **Clinical Settings**
   - Emergency department
   - Medical-surgical units
   - Intensive care units
   - Operating rooms
   - Outpatient clinics
   - Specialty clinics
   - Rehabilitation units
   - Long-term care facilities
   - Home health settings

3. **Medical Specialties**
   - Internal medicine
   - Family medicine
   - Emergency medicine
   - Surgery (all specialties)
   - Pediatrics
   - Obstetrics/Gynecology
   - Psychiatry
   - Neurology
   - Cardiology
   - Oncology

4. **Documentation Formats**
   - SOAP notes
   - Problem-oriented records
   - Systems-based documentation
   - Narrative notes
   - Structured templates
   - Voice-to-text documentation
   - Electronic health records

5. **Regulatory Standards**
   - CMS requirements
   - Joint Commission standards
   - State licensing requirements
   - Specialty board standards
   - Insurance documentation requirements
   - Legal documentation standards