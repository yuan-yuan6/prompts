---
title: CDS Rules, Algorithms & Diagnostic Support
category: healthcare
tags: [design, healthcare, machine-learning]
use_cases:
  - Developing CDS rules, algorithms, diagnostic support, medication management, and risk prediction systems
  - Project planning and execution
last_updated: 2025-11-09
related_templates:
  - clinical-decision-support-overview.md
---

# CDS Rules, Algorithms & Diagnostic Support

## Purpose
Design comprehensive CDS rules and algorithms covering diagnostic support, medication management, risk prediction, and clinical pathways.

## Template

```
You are a clinical decision support algorithm specialist. Create detailed CDS rules based on:

Clinical Context:
- Clinical Focus: [PRIMARY_CLINICAL_CONDITIONS]
- Decision Types: [DIAGNOSIS_TREATMENT_SAFETY]
- Risk Categories: [PATIENT_RISK_FACTORS]
- AI Capabilities: [MACHINE_LEARNING_INFRASTRUCTURE]

Generate comprehensive CDS rules and algorithms covering:

## 2. DIAGNOSTIC DECISION SUPPORT SYSTEMS

### 2.1 Differential Diagnosis Support
- Symptom-based diagnostic assistance
- Clinical presentation analysis
- Diagnostic probability calculation
- Medical imaging AI analysis
- Laboratory data interpretation
- Pattern recognition and clustering
- Evidence-based diagnostic pathways
- Diagnostic accuracy metrics

### 2.2 Clinical Pathway Guidance
- Disease-specific care pathways
- Standardized care protocols
- Personalized care planning
- Treatment option comparison
- Care transition management
- Discharge planning optimization
- Prognosis and outcome prediction
- Quality of life assessment

### 2.3 Risk Stratification and Prediction
- Validated risk scoring systems
- Cardiovascular risk calculation
- Surgical risk assessment
- Infection risk prediction
- Falls and pressure ulcer risk
- Population risk management
- Predictive modeling applications
- Early warning systems

## 3. MEDICATION MANAGEMENT AND SAFETY

### 3.1 Drug Interaction and Safety Checking
- Drug-drug interaction screening
- Severity assessment and classification
- Drug-allergy checking and contraindications
- Alternative medication recommendations
- Dose adjustment requirements
- Patient counseling and education
- Provider communication protocols
- Emergency response planning

### 3.2 Prescription Decision Support
- Evidence-based prescribing guidance
- First-line therapy recommendations
- Personalized medicine integration
- Pharmacogenomic testing and interpretation
- Therapeutic drug monitoring
- Adverse drug event prevention
- Medication optimization
- Quality assurance processes
```

## Variables
- `[PRIMARY_CLINICAL_CONDITIONS]`: Clinical focus
- `[DIAGNOSIS_TREATMENT_SAFETY]`: Decision types
- `[PATIENT_RISK_FACTORS]`: Risk categories
- `[MACHINE_LEARNING_INFRASTRUCTURE]`: AI capabilities

## Best Practices
1. **Validate algorithms** - Test with clinical data
2. **Prioritize alerts** - Avoid alert fatigue
3. **Provide alternatives** - Suggest actionable options
4. **Explain recommendations** - Show evidence and reasoning
5. **Monitor outcomes** - Track clinical effectiveness
