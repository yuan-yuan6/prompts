---
title: Surgical Treatment Plan
category: healthcare/Clinical-Practice
tags:
- healthcare
use_cases:
- Developing comprehensive surgical treatment plans
- Creating perioperative care protocols
- Managing pre-operative assessment and post-operative care
related_templates:
- healthcare/Clinical Practice/acute-care-treatment-plan.md
- healthcare/Clinical Practice/chronic-disease-management-plan.md
- healthcare/patient-care-pathway.md
last_updated: 2025-11-09
industries:
- education
- healthcare
- manufacturing
---

# Surgical Treatment Plan

## Purpose
Develop comprehensive surgical treatment plans that integrate pre-operative assessment, intraoperative planning, and post-operative care to ensure optimal surgical outcomes and patient safety throughout the perioperative period.

## Quick Start

### For Elective Surgery Planning
1. Complete risk stratification: `ASA_CLASS: "II"`, calculate RCRI score
2. Obtain necessary clearances: Cardiology, pulmonary as indicated by risk
3. Set VTE prophylaxis: Choose mechanical + pharmacologic based on Caprini score
4. Plan antibiotic prophylaxis: Select agent, timing (within 60 min of incision)
5. Document informed consent: Include procedure-specific risks and alternatives

### For Urgent/Emergency Surgery
1. Expedite pre-op assessment: Focus on critical labs, ECG, imaging
2. Implement rapid optimization: Correct coagulopathy, fluid resuscitation
3. Activate surgical team: Confirm OR availability, anesthesia readiness
4. Communicate urgency: Specify timeframe (STAT/within 6 hours/within 24 hours)
5. Brief family: Provide realistic expectations given urgency and risk

### HIPAA Compliance in Surgical Planning
- Secure all consent forms and surgical paperwork in locked/encrypted systems
- Limit case discussions to care team members only (no hallway conversations)
- De-identify cases for teaching or quality review presentations
- Obtain specific authorization for surgical photography/video
- Ensure OR schedule displays use patient identifiers appropriately

### Perioperative Safety Checklist
- Pre-op: H&P complete, consent signed, site marked, NPO confirmed
- Timeout: Correct patient, site, procedure verified by entire team
- Post-op: Pain management plan, VTE prophylaxis ordered, discharge criteria defined

## Template

```
You are a surgical planning specialist. Create [SURGICAL_PLAN_TYPE] for [SURGICAL_INDICATION] in [SURGICAL_SETTING] following [SURGICAL_GUIDELINES] with [URGENCY_CLASSIFICATION].

PRE-OPERATIVE ASSESSMENT:

Patient Demographics:
- Patient ID: [PATIENT_ID]
- Name: [PATIENT_NAME]
- Age: [PATIENT_AGE]
- Gender: [PATIENT_GENDER]
- BMI: [BMI] - Weight: [WEIGHT] - Height: [HEIGHT]

Surgical Indication:
- Primary diagnosis: [SURGICAL_DIAGNOSIS]
- Indication for surgery: [SURGICAL_INDICATION]
- Alternative treatments considered: [ALTERNATIVE_TREATMENTS]
- Rationale for surgical approach: [SURGICAL_RATIONALE]
- Urgency: [SURGICAL_URGENCY] - Timing: [SURGICAL_TIMING]
- Failed conservative management: [FAILED_CONSERVATIVE_TX]

Medical History:
- Relevant medical history: [RELEVANT_MEDICAL_HISTORY]
- Cardiac history: [CARDIAC_HISTORY] - Risk factors: [CARDIAC_RISK]
- Pulmonary history: [PULMONARY_HISTORY] - FEV1: [FEV1_VALUE]
- Renal function: [RENAL_FUNCTION] - eGFR: [EGFR]
- Hepatic function: [HEPATIC_FUNCTION] - LFTs: [LFT_VALUES]
- Diabetes: [DIABETES_STATUS] - HbA1c: [HBA1C]
- Bleeding disorders: [BLEEDING_DISORDERS]
- Previous surgeries: [SURGICAL_HISTORY]
- Anesthesia history: [ANESTHESIA_HISTORY] - Complications: [ANESTHESIA_COMPLICATIONS]

Risk Stratification:
- ASA classification: [ASA_CLASS] - Rationale: [ASA_RATIONALE]
- Cardiac risk score: [CARDIAC_RISK_SCORE] - Tool: [RISK_SCORE_TOOL]
- VTE risk: [VTE_RISK] - Caprini score: [CAPRINI_SCORE]
- Surgical site infection risk: [SSI_RISK]
- Overall surgical risk: [OVERALL_RISK] - High/moderate/low: [RISK_LEVEL]

Medications Review:
- Current medications: [CURRENT_MEDICATIONS]
- Anticoagulants: [ANTICOAGULANTS] - Hold before surgery: [ANTICOAG_HOLD_TIME]
- Antiplatelets: [ANTIPLATELETS] - Hold before surgery: [ANTIPLATELET_HOLD_TIME]
- Medications to continue: [CONTINUE_MEDS]
- Medications to hold: [HOLD_MEDS] - Hold timing: [HOLD_TIMING]
- Allergies: [ALLERGIES] - Reactions: [ALLERGY_REACTIONS]

SURGICAL PLAN:

Procedure Details:
- Primary procedure: [PRIMARY_PROCEDURE]
- CPT code: [CPT_CODE]
- Surgical approach: [SURGICAL_APPROACH] - Open/laparoscopic/robotic: [APPROACH_TYPE]
- Estimated duration: [PROCEDURE_DURATION]
- Estimated blood loss: [ESTIMATED_EBL]
- Additional procedures planned: [ADDITIONAL_PROCEDURES]

Surgical Team:
- Primary surgeon: [PRIMARY_SURGEON] - Credentials: [SURGEON_CREDENTIALS]
- Assistant surgeon: [ASSISTANT_SURGEON]
- Anesthesiologist: [ANESTHESIOLOGIST]
- Surgical nurse: [SURGICAL_NURSE]
- Anesthesia type: [ANESTHESIA_TYPE] - General/regional/local: [ANESTHESIA_DETAIL]

Operative Planning:
- Patient positioning: [PATIENT_POSITIONING]
- Special equipment needed: [SPECIAL_EQUIPMENT]
- Instrumentation: [INSTRUMENTATION]
- Implants/devices: [IMPLANTS] - Size/type: [IMPLANT_DETAILS]
- Blood products: [BLOOD_PRODUCTS] - Type and screen: [TYPE_SCREEN]
- Imaging guidance: [IMAGING_GUIDANCE] - Fluoroscopy/navigation: [IMAGING_TYPE]

PRE-OPERATIVE OPTIMIZATION:

Medical Optimization:
- Cardiac optimization: [CARDIAC_OPTIMIZATION]
  - Beta-blocker management: [BETA_BLOCKER_PLAN]
  - BP control target: [BP_TARGET]
- Pulmonary optimization: [PULMONARY_OPTIMIZATION]
  - Incentive spirometry: [SPIROMETRY_PLAN]
  - Smoking cessation: [SMOKING_CESSATION] - Timeframe: [CESSATION_TIMEFRAME]
- Glycemic control: [GLYCEMIC_OPTIMIZATION] - Target HbA1c: [HBA1C_TARGET]
- Nutritional status: [NUTRITIONAL_STATUS] - Optimization: [NUTRITION_OPTIMIZATION]
- Anemia management: [ANEMIA_MANAGEMENT] - Hgb target: [HGB_TARGET]

Pre-operative Testing:
- Laboratory tests: [PREOP_LABS]
  - CBC: [CBC_REQUIRED] - Results: [CBC_RESULTS]
  - BMP: [BMP_REQUIRED] - Results: [BMP_RESULTS]
  - Coagulation panel: [COAG_REQUIRED] - Results: [COAG_RESULTS]
  - Type and screen: [TYPE_SCREEN_REQUIRED]
- Imaging: [PREOP_IMAGING] - Studies: [IMAGING_STUDIES]
- ECG: [ECG_REQUIRED] - Results: [ECG_RESULTS]
- Chest X-ray: [CXR_REQUIRED] - Results: [CXR_RESULTS]
- Additional tests: [ADDITIONAL_TESTS]

Pre-operative Clearances:
- Cardiology clearance: [CARDIOLOGY_CLEARANCE] - Status: [CARDIO_CLEARANCE_STATUS]
- Pulmonary clearance: [PULMONARY_CLEARANCE] - Status: [PULM_CLEARANCE_STATUS]
- Other specialty clearances: [OTHER_CLEARANCES]
- Anesthesia pre-op evaluation: [ANESTHESIA_EVAL] - Date: [ANESTHESIA_EVAL_DATE]

PROPHYLAXIS PROTOCOLS:

VTE Prophylaxis:
- VTE risk assessment: [VTE_RISK_ASSESSMENT]
- Mechanical prophylaxis: [MECHANICAL_PROPHYLAXIS] - SCDs/TED stockings: [MECHANICAL_TYPE]
- Pharmacologic prophylaxis: [PHARMACOLOGIC_PROPHYLAXIS]
  - Agent: [VTE_AGENT] - Dose: [VTE_DOSE] - Timing: [VTE_TIMING]
  - Duration: [VTE_DURATION]
- Contraindications: [VTE_CONTRAINDICATIONS]

Antibiotic Prophylaxis:
- SSI risk category: [SSI_CATEGORY] - Clean/clean-contaminated/contaminated: [WOUND_CLASS]
- Antibiotic choice: [PROPHYLACTIC_ANTIBIOTIC] - Dose: [ANTIBIOTIC_DOSE]
- Timing: [ANTIBIOTIC_TIMING] - Within 60 minutes of incision
- Redosing required: [REDOSING_REQUIRED] - Interval: [REDOSING_INTERVAL]
- Discontinuation: [ANTIBIOTIC_DISCONTINUATION] - Typically 24 hours post-op

Additional Prophylaxis:
- Aspiration prophylaxis: [ASPIRATION_PROPHYLAXIS]
- Glycemic control: [PERIOP_GLUCOSE_CONTROL] - Target: [GLUCOSE_TARGET]
- Hypothermia prevention: [HYPOTHERMIA_PREVENTION]
- Pressure ulcer prevention: [PRESSURE_ULCER_PREVENTION]

INFORMED CONSENT:

Consent Discussion:
- Procedure explained: [PROCEDURE_EXPLANATION]
- Benefits discussed: [PROCEDURE_BENEFITS]
- Risks discussed: [PROCEDURE_RISKS]
  - Common risks: [COMMON_RISKS]
  - Serious risks: [SERIOUS_RISKS]
  - Anesthesia risks: [ANESTHESIA_RISKS]
- Alternatives presented: [ALTERNATIVES_PRESENTED]
- Questions addressed: [QUESTIONS_ADDRESSED]
- Patient understanding confirmed: [UNDERSTANDING_CONFIRMED]

Specific Risks:
- Bleeding: [BLEEDING_RISK_PERCENTAGE]
- Infection: [INFECTION_RISK_PERCENTAGE]
- Organ injury: [ORGAN_INJURY_RISK] - Specific organs: [AT_RISK_ORGANS]
- Nerve damage: [NERVE_DAMAGE_RISK]
- Conversion (if minimally invasive): [CONVERSION_RISK]
- Need for transfusion: [TRANSFUSION_RISK]
- Death: [MORTALITY_RISK]

Consent Documentation:
- Consent form signed: [CONSENT_SIGNED] - Date: [CONSENT_DATE]
- Witness present: [WITNESS] - Name: [WITNESS_NAME]

PRE-OPERATIVE INSTRUCTIONS:

Patient Preparation:
- NPO status: [NPO_INSTRUCTIONS] - Clear liquids until: [CLEAR_LIQUID_TIME]
- Bowel preparation: [BOWEL_PREP] - Regimen: [BOWEL_PREP_REGIMEN]
- Skin preparation: [SKIN_PREP] - Chlorhexidine shower: [CHG_SHOWER_INSTRUCTIONS]
- Medication instructions: [PREOP_MED_INSTRUCTIONS]
  - Morning of surgery: [MORNING_MEDS]
  - Hold these medications: [HOLD_MEDS_LIST]
- Arrival time: [ARRIVAL_TIME] - Surgery scheduled: [SURGERY_TIME]

Day of Surgery:
- Check-in location: [CHECKIN_LOCATION]
- Items to bring: [ITEMS_TO_BRING]
- Contact person: [EMERGENCY_CONTACT] - Phone: [EMERGENCY_PHONE]
- Transportation plan: [TRANSPORTATION] - Driver required: [DRIVER_REQUIRED]
- Expected hospital stay: [EXPECTED_LOS] - Inpatient/outpatient: [ADMISSION_STATUS]

INTRAOPERATIVE PLAN:

Surgical Steps:
1. [SURGICAL_STEP_1] - Critical considerations: [STEP_1_CONSIDERATIONS]
2. [SURGICAL_STEP_2] - Critical considerations: [STEP_2_CONSIDERATIONS]
3. [SURGICAL_STEP_3] - Critical considerations: [STEP_3_CONSIDERATIONS]
4. [SURGICAL_STEP_4] - Critical considerations: [STEP_4_CONSIDERATIONS]

Safety Checklist:
- Time-out performed: [TIMEOUT_CONFIRMED]
- Correct patient: [PATIENT_CONFIRMED]
- Correct site: [SITE_CONFIRMED] - Site marking: [SITE_MARKING]
- Correct procedure: [PROCEDURE_CONFIRMED]
- Consent verified: [CONSENT_VERIFIED]
- Antibiotic given: [ANTIBIOTIC_CONFIRMED]

Monitoring:
- Standard monitoring: [STANDARD_MONITORING]
- Arterial line: [ARTERIAL_LINE_NEEDED]
- Central line: [CENTRAL_LINE_NEEDED]
- Foley catheter: [FOLEY_NEEDED]
- Temperature monitoring: [TEMP_MONITORING]

POST-OPERATIVE CARE PLAN:

Immediate Post-operative (PACU):
- Recovery location: [RECOVERY_LOCATION]
- Pain management: [PACU_PAIN_MGMT]
  - IV medications: [IV_PAIN_MEDS]
  - PCA: [PCA_NEEDED] - Medication: [PCA_MED]
- PONV prophylaxis: [PONV_PROPHYLAXIS] - Agents: [PONV_AGENTS]
- Vital signs frequency: [PACU_VS_FREQUENCY]
- Discharge criteria from PACU: [PACU_DISCHARGE_CRITERIA]

Post-operative Orders:
- Admission location: [ADMISSION_UNIT] - Level of care: [CARE_LEVEL]
- Activity: [ACTIVITY_ORDERS] - Ambulation: [AMBULATION_PLAN]
- Diet: [DIET_ORDERS] - Advancement: [DIET_ADVANCEMENT]
- IV fluids: [IV_FLUID_ORDERS] - Rate: [IV_RATE]
- Drain management: [DRAIN_ORDERS] - Type: [DRAIN_TYPE]
- Wound care: [WOUND_CARE_ORDERS] - Dressing changes: [DRESSING_CHANGE_FREQUENCY]

Pain Management Protocol:
- Multimodal approach: [MULTIMODAL_PAIN_MGMT]
- Oral medications: [ORAL_PAIN_MEDS]
  - [PAIN_MED_1]: Dose [PAIN_DOSE_1] - Frequency [PAIN_FREQ_1]
  - [PAIN_MED_2]: Dose [PAIN_DOSE_2] - Frequency [PAIN_FREQ_2]
- PRN medications: [PRN_PAIN_MEDS]
- Pain assessment frequency: [PAIN_ASSESSMENT_FREQ]
- Pain goal: [PAIN_GOAL]

Post-operative Monitoring:
- Vital signs: [POSTOP_VS_FREQUENCY]
- Drain output: [DRAIN_MONITORING] - Alert criteria: [DRAIN_ALERT]
- Surgical site checks: [SITE_CHECK_FREQUENCY]
- Lab monitoring: [POSTOP_LAB_MONITORING]
  - [POSTOP_LAB_1]: Frequency [POSTOP_LAB_FREQ_1]
  - [POSTOP_LAB_2]: Frequency [POSTOP_LAB_FREQ_2]
- Imaging: [POSTOP_IMAGING] - Timing: [POSTOP_IMAGING_TIMING]

COMPLICATIONS MANAGEMENT:

Potential Complications:
- [COMPLICATION_1]: Risk [COMPLICATION_1_RISK] - Prevention: [PREVENTION_1] - Management: [MGMT_1]
- [COMPLICATION_2]: Risk [COMPLICATION_2_RISK] - Prevention: [PREVENTION_2] - Management: [MGMT_2]
- [COMPLICATION_3]: Risk [COMPLICATION_3_RISK] - Prevention: [PREVENTION_3] - Management: [MGMT_3]

Early Warning Signs:
- [WARNING_SIGN_1]: Action [ACTION_1]
- [WARNING_SIGN_2]: Action [ACTION_2]
- [WARNING_SIGN_3]: Action [ACTION_3]

Emergency Protocols:
- Hemorrhage protocol: [HEMORRHAGE_PROTOCOL]
- Anastomotic leak protocol: [LEAK_PROTOCOL]
- Respiratory distress: [RESPIRATORY_PROTOCOL]
- Hemodynamic instability: [HEMODYNAMIC_PROTOCOL]

DISCHARGE PLANNING:

Discharge Criteria:
- Pain controlled on oral meds: [PAIN_CONTROL_ACHIEVED]
- Tolerating diet: [DIET_TOLERANCE]
- Ambulating independently: [AMBULATION_ACHIEVED]
- No signs of complications: [COMPLICATIONS_RULED_OUT]
- Patient education completed: [EDUCATION_COMPLETED]
- Follow-up arranged: [FOLLOWUP_ARRANGED]

Discharge Instructions:
- Activity restrictions: [ACTIVITY_RESTRICTIONS] - Duration: [RESTRICTION_DURATION]
- Return to work: [RETURN_TO_WORK_TIMELINE]
- Driving restrictions: [DRIVING_RESTRICTIONS]
- Lifting restrictions: [LIFTING_RESTRICTIONS]
- Wound care: [HOME_WOUND_CARE] - Shower instructions: [SHOWER_INSTRUCTIONS]
- Drain care: [HOME_DRAIN_CARE] - Removal plan: [DRAIN_REMOVAL_PLAN]

Discharge Medications:
- Pain medications: [DISCHARGE_PAIN_MEDS] - Duration: [PAIN_MED_DURATION]
- Antibiotics: [DISCHARGE_ANTIBIOTICS] - Duration: [ANTIBIOTIC_DURATION]
- VTE prophylaxis: [DISCHARGE_VTE_PROPHYLAXIS] - Duration: [VTE_PROPHYLAXIS_DURATION]
- Other medications: [OTHER_DISCHARGE_MEDS]

Warning Signs to Report:
- Fever >101.5°F (38.6°C)
- Increased pain not relieved by medications
- Redness, swelling, or drainage from incision
- Shortness of breath or chest pain
- Leg swelling or pain
- Inability to tolerate food or fluids
- [PROCEDURE_SPECIFIC_WARNING_SIGNS]

Follow-up Plan:
- Post-op appointment: [FOLLOWUP_DATE] - Provider: [FOLLOWUP_PROVIDER]
- Wound check: [WOUND_CHECK_DATE]
- Drain removal: [DRAIN_REMOVAL_DATE]
- Suture/staple removal: [SUTURE_REMOVAL_DATE]
- Imaging: [FOLLOWUP_IMAGING] - Timing: [IMAGING_FOLLOWUP_TIMING]
- Contact information: [SURGEON_CONTACT] - After hours: [AFTER_HOURS_CONTACT]

SURGICAL TREATMENT PLAN SUMMARY:

Patient: [SURGICAL_PATIENT_ID]
Procedure: [PROCEDURE_NAME]
Surgeon: [SURGEON_NAME]
Scheduled date: [SURGERY_DATE]
ASA class: [ASA_CLASSIFICATION]

Pre-operative Checklist:
✓ Medical optimization completed: [OPTIMIZATION_STATUS]
✓ Pre-operative testing complete: [TESTING_STATUS]
✓ Clearances obtained: [CLEARANCE_STATUS]
✓ Consent signed: [CONSENT_STATUS]
✓ Prophylaxis planned: [PROPHYLAXIS_STATUS]

Intraoperative Plan:
- Approach: [APPROACH_SUMMARY]
- Duration: [DURATION_ESTIMATE]
- Team: [TEAM_SUMMARY]

Post-operative Plan:
- Admission: [ADMISSION_PLAN]
- Expected LOS: [EXPECTED_STAY]
- Pain management: [PAIN_MGMT_SUMMARY]
- Discharge planning: [DISCHARGE_PLAN_SUMMARY]

Surgeon signature: [SURGEON_SIGNATURE]
Date: [PLAN_DATE]

---

Perioperative Safety Checklist:
✓ Risk assessment completed: [RISK_ASSESSMENT_STATUS]
✓ VTE prophylaxis ordered: [VTE_PROPHYLAXIS_STATUS]
✓ Antibiotic prophylaxis planned: [ANTIBIOTIC_STATUS]
✓ Informed consent obtained: [INFORMED_CONSENT_STATUS]
✓ Pre-op instructions provided: [INSTRUCTIONS_STATUS]
✓ Post-op plan established: [POSTOP_PLAN_STATUS]
✓ Discharge criteria defined: [DISCHARGE_CRITERIA_STATUS]

Next action: [NEXT_ACTION_ITEM]
```

## Variables
Surgical-specific variables covering: pre-operative assessment, risk stratification, surgical planning, optimization, prophylaxis, informed consent, intraoperative details, post-operative care, complication management, and discharge planning.

## Usage Examples

### Example 1: Laparoscopic Cholecystectomy
```
SURGICAL_PLAN_TYPE: "Elective laparoscopic cholecystectomy plan"
SURGICAL_INDICATION: "Symptomatic cholelithiasis"
SURGICAL_SETTING: "Ambulatory surgery center"
SURGICAL_GUIDELINES: "SAGES guidelines"
URGENCY_CLASSIFICATION: "Elective"
```

### Example 2: Total Knee Replacement
```
SURGICAL_PLAN_TYPE: "Total knee arthroplasty protocol"
SURGICAL_INDICATION: "Severe osteoarthritis right knee"
SURGICAL_SETTING: "Hospital operating room"
SURGICAL_GUIDELINES: "AAOS guidelines"
URGENCY_CLASSIFICATION: "Elective"
```

### Example 3: Emergency Appendectomy
```
SURGICAL_PLAN_TYPE: "Emergency appendectomy plan"
SURGICAL_INDICATION: "Acute appendicitis"
SURGICAL_SETTING: "Hospital OR"
SURGICAL_GUIDELINES: "WSES guidelines"
URGENCY_CLASSIFICATION: "Urgent - within 24 hours"
```

### Example 4: Oncologic Surgery
```
SURGICAL_PLAN_TYPE: "Oncologic resection protocol"
SURGICAL_INDICATION: "Resectable pancreatic adenocarcinoma"
SURGICAL_SETTING: "Tertiary care center"
SURGICAL_GUIDELINES: "NCCN surgical guidelines"
URGENCY_CLASSIFICATION: "Scheduled - within 4-6 weeks"
```

## Best Practices

1. **Comprehensive pre-operative assessment** - Identify and optimize all risk factors
2. **Multidisciplinary approach** - Involve anesthesia, nursing, and specialty consultants early
3. **Evidence-based prophylaxis** - Follow guidelines for VTE and SSI prevention
4. **Clear communication** - Ensure patient understanding through teach-back
5. **Standardized protocols** - Use checklists and bundles to reduce variability
6. **Appropriate testing** - Order tests based on clinical indication, not routine
7. **Risk stratification** - Use validated tools (ASA, RCRI, Caprini)
8. **Enhanced recovery pathways** - Implement ERAS protocols when applicable
9. **Shared decision-making** - Involve patients in treatment decisions
10. **Complication preparedness** - Anticipate and plan for potential complications

## Tips for Success

- Schedule pre-operative clinic visit 1-2 weeks before surgery
- Optimize modifiable risk factors (smoking, glucose, nutrition)
- Minimize NPO time (clear liquids up to 2 hours, solids 6-8 hours)
- Use multimodal pain management to reduce opioid use
- Implement early mobilization protocols
- Provide written discharge instructions with contact information
- Ensure 24-hour post-discharge phone call for outpatient procedures
- Use care pathways and order sets to standardize care
- Document clearly for medicolegal protection
- Debrief after complex cases for continuous improvement
