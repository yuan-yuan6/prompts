---
title: Data Governance Standards Template
category: data-analytics/Analytics Engineering
tags: [compliance, data-analytics, data-quality, governance, standards, template]
use_cases:
  - Establishing data governance standards and policies including quality standards, compliance requirements, data stewardship, and governance frameworks for enterprise data management.
  - Data governance
  - Quality standards
related_templates:
  - analytics-data-quality-overview.md
  - data-quality-assessment.md
  - analytics-documentation.md
last_updated: 2025-11-09
---

# Data Governance Standards Template

## Purpose
Establish comprehensive data governance standards and policies including quality standards, compliance requirements, data stewardship roles, and governance frameworks for enterprise data management.

## Template

```
You are a data governance specialist. Define governance standards for [ORGANIZATION] covering [GOVERNANCE_SCOPE] with [COMPLIANCE_REQUIREMENTS] enforced through [GOVERNANCE_MECHANISMS].

### GOVERNANCE FRAMEWORK

```
Data Quality Standards:

1. Data Accuracy Standard
   - Definition: Data must correctly represent real-world values
   - Target: ≥ [ACCURACY_TARGET]% accuracy
   - Measurement: Validation against authoritative sources
   - Compliance: Mandatory for [CRITICAL_DATA_CLASSES]

2. Data Completeness Standard
   - Definition: All required data elements must be populated
   - Target: ≥ [COMPLETENESS_TARGET]% completeness
   - Measurement: Null value analysis
   - Compliance: Required fields defined in data dictionary

3. Data Consistency Standard
   - Definition: Data must be uniform across systems
   - Target: ≥ [CONSISTENCY_TARGET]% consistency
   - Measurement: Cross-system reconciliation
   - Compliance: Master data management compliance

4. Data Timeliness Standard
   - Definition: Data must be available when needed
   - Target: Data latency < [TIMELINESS_TARGET] hours
   - Measurement: Timestamp analysis
   - Compliance: SLA adherence monitoring
```

### DATA STEWARDSHIP

```
Roles and Responsibilities:

Data Owner:
- Accountable for data quality
- Approves data definitions
- Sets quality requirements
- Funds quality initiatives

Data Steward:
- Manages day-to-day quality
- Implements quality rules
- Monitors quality metrics
- Coordinates remediation

Data Quality Analyst:
- Performs quality assessments
- Analyzes quality trends
- Reports quality status
- Recommends improvements

Data Engineer:
- Implements quality controls
- Builds quality pipelines
- Automates quality checks
- Maintains quality tools
```

### COMPLIANCE REQUIREMENTS

```
Regulatory Compliance:

GDPR (if applicable):
- Data accuracy maintained
- Data minimization enforced
- Right to rectification supported
- Data quality documented

SOX (if applicable):
- Financial data accuracy
- Control documentation
- Audit trail maintenance
- Quality attestation

Industry Standards:
- [INDUSTRY_STANDARD_1]: [REQUIREMENTS]
- [INDUSTRY_STANDARD_2]: [REQUIREMENTS]
```

OUTPUT: Governance policies, standards documentation, compliance framework, stewardship model
```

## Variables
- [ORGANIZATION] - Organization name
- [GOVERNANCE_SCOPE] - Scope of governance
- [COMPLIANCE_REQUIREMENTS] - Required compliance
- [GOVERNANCE_MECHANISMS] - Enforcement mechanisms

## Best Practices
1. **Establish clear ownership** - Define roles and responsibilities
2. **Document standards** - Written policies and procedures
3. **Enforce consistently** - Apply standards uniformly
4. **Monitor compliance** - Track adherence to standards
