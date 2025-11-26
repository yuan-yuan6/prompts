---
title: Data Governance Framework & Management Strategy
category: data-analytics
tags:
- data-analytics
- ai-ml
- design
- framework
- management
- research
- security
use_cases:
- Creating comprehensive data governance framework covering data strategy, quality
  management, privacy compliance, security protocols, lifecycle management, and organizational
  governance to ensure trusted, compliant, and valuable data assets across the enterprise.
- Project planning and execution
- Strategy development
last_updated: 2025-11-09
industries:
- finance
- government
- healthcare
- manufacturing
- retail
- technology
type: template
difficulty: intermediate
slug: data-governance-framework
---

# Data Governance Framework & Management Strategy

## Purpose
Comprehensive data governance framework covering data strategy, quality management, privacy compliance, security protocols, lifecycle management, and organizational governance to ensure trusted, compliant, and valuable data assets across the enterprise.

## Quick Governance Prompt
> Create a data governance framework for [company type] with [data volume] across [number] systems. Key regulations: [GDPR/CCPA/HIPAA/SOX]. Current maturity: [1-5]. Target quality: [%]. Priority areas: [quality/security/privacy/MDM]. Include: (1) Governance organization and roles, (2) Data quality rules and monitoring, (3) Compliance requirements checklist, (4) Implementation timeline and milestones.

## Quick Start

### For Data Engineers
Establish data governance in 3 steps:

1. **Assess Current State**
   - Evaluate governance maturity across 8 domains: Strategy, Quality, Privacy, Security, MDM, Architecture, Lifecycle, Literacy
   - Rate each domain 1-5 (Initial→Optimizing) and identify critical gaps
   - Document compliance requirements: GDPR, CCPA, HIPAA, SOX, industry regulations (Section 3, lines 47-56)
   - Example: `QUALITY_CURRENT: "2/5"`, `QUALITY_TARGET: "4/5"`, `QUALITY_GAP: "Critical data profiling missing"`

2. **Implement Core Controls**
   - **Data Quality**: Set up monitoring for completeness, accuracy, consistency with automated alerts (Section 2, lines 35-46)
   - **Security**: Implement classification (Public/Internal/Confidential/Restricted), access controls, encryption, audit logging (Section 4, lines 58-68)
   - **Master Data**: Define golden records for Customer, Product, Vendor with stewardship model (Section 5, lines 70-79)
   - Configure quality thresholds: `DATA_QUALITY_TARGET: "95%"`, `COMPLIANCE_TARGET: "100%"`

3. **Establish Governance Organization**
   - Define roles: Chief Data Officer, Data Governance Council, Data Stewards, Data Owners, Custodians (Section 8, lines 103-113)
   - Set up data lifecycle policies: Creation→Active Use→Archival→Destruction with retention rules (Section 7, lines 92-101)
   - Create performance metrics: Quality score, compliance rate, accessibility, incident response time (Section 10, lines 125-136)
   - Implement governance workflows for data access requests, classification, and exception handling

**Key Sections**: Maturity assessment (23-33), Quality management (35-46), Compliance (47-57), Security (58-69), Lifecycle (92-102), Organization (103-114)

## Template

Implement data governance for [COMPANY_NAME] managing [DATA_VOLUME] of data across [SYSTEM_COUNT] systems with [GOVERNANCE_BUDGET] budget over [TIMELINE] to achieve [DATA_QUALITY_TARGET]% data quality, [COMPLIANCE_TARGET]% regulatory compliance, and [DATA_VALUE_TARGET] in measurable data value.

### 1. Data Governance Assessment & Maturity

| **Governance Domain** | **Current Maturity** | **Target Maturity** | **Gap Analysis** | **Critical Issues** | **Investment Priority** | **Timeline** |
|----------------------|---------------------|-------------------|------------------|-------------------|----------------------|-------------|
| Data Strategy & Vision | [STRATEGY_CURRENT]/5 | [STRATEGY_TARGET]/5 | [STRATEGY_GAP] | [STRATEGY_ISSUES] | [STRATEGY_PRIORITY] | [STRATEGY_TIMELINE] |
| Data Quality Management | [QUALITY_CURRENT]/5 | [QUALITY_TARGET]/5 | [QUALITY_GAP] | [QUALITY_ISSUES] | [QUALITY_PRIORITY] | [QUALITY_TIMELINE] |
| Data Privacy & Ethics | [PRIVACY_CURRENT]/5 | [PRIVACY_TARGET]/5 | [PRIVACY_GAP] | [PRIVACY_ISSUES] | [PRIVACY_PRIORITY] | [PRIVACY_TIMELINE] |
| Data Security | [SECURITY_CURRENT]/5 | [SECURITY_TARGET]/5 | [SECURITY_GAP] | [SECURITY_ISSUES] | [SECURITY_PRIORITY] | [SECURITY_TIMELINE] |
| Master Data Management | [MDM_CURRENT]/5 | [MDM_TARGET]/5 | [MDM_GAP] | [MDM_ISSUES] | [MDM_PRIORITY] | [MDM_TIMELINE] |
| Data Architecture | [ARCH_CURRENT]/5 | [ARCH_TARGET]/5 | [ARCH_GAP] | [ARCH_ISSUES] | [ARCH_PRIORITY] | [ARCH_TIMELINE] |
| Data Lifecycle Management | [LIFECYCLE_CURRENT]/5 | [LIFECYCLE_TARGET]/5 | [LIFECYCLE_GAP] | [LIFECYCLE_ISSUES] | [LIFECYCLE_PRIORITY] | [LIFECYCLE_TIMELINE] |
| Data Literacy & Culture | [LITERACY_CURRENT]/5 | [LITERACY_TARGET]/5 | [LITERACY_GAP] | [LITERACY_ISSUES] | [LITERACY_PRIORITY] | [LITERACY_TIMELINE] |

### 2. Data Quality Management Framework

| **Data Domain** | **Quality Dimensions** | **Current Score** | **Target Score** | **Quality Rules** | **Monitoring Method** | **Remediation Process** |
|----------------|----------------------|------------------|------------------|------------------|---------------------|------------------------|
| Customer Data | [CUST_DIMENSIONS] | [CUST_CURRENT]% | [CUST_TARGET]% | [CUST_RULES] | [CUST_MONITORING] | [CUST_REMEDIATION] |
| Product Data | [PROD_DIMENSIONS] | [PROD_CURRENT]% | [PROD_TARGET]% | [PROD_RULES] | [PROD_MONITORING] | [PROD_REMEDIATION] |
| Financial Data | [FIN_DIMENSIONS] | [FIN_CURRENT]% | [FIN_TARGET]% | [FIN_RULES] | [FIN_MONITORING] | [FIN_REMEDIATION] |
| Operational Data | [OPS_DIMENSIONS] | [OPS_CURRENT]% | [OPS_TARGET]% | [OPS_RULES] | [OPS_MONITORING] | [OPS_REMEDIATION] |
| Employee Data | [EMP_DIMENSIONS] | [EMP_CURRENT]% | [EMP_TARGET]% | [EMP_RULES] | [EMP_MONITORING] | [EMP_REMEDIATION] |
| Vendor/Supplier Data | [VENDOR_DIMENSIONS] | [VENDOR_CURRENT]% | [VENDOR_TARGET]% | [VENDOR_RULES] | [VENDOR_MONITORING] | [VENDOR_REMEDIATION] |
| Reference Data | [REF_DIMENSIONS] | [REF_CURRENT]% | [REF_TARGET]% | [REF_RULES] | [REF_MONITORING] | [REF_REMEDIATION] |

### 3. Data Privacy & Compliance Management

| **Privacy Regulation** | **Compliance Scope** | **Current Status** | **Requirements** | **Implementation Plan** | **Risk Level** | **Completion Timeline** |
|-----------------------|----------------------|-------------------|------------------|------------------------|----------------|------------------------|
| GDPR | [GDPR_SCOPE] | [GDPR_STATUS] | [GDPR_REQUIREMENTS] | [GDPR_PLAN] | [GDPR_RISK] | [GDPR_TIMELINE] |
| CCPA | [CCPA_SCOPE] | [CCPA_STATUS] | [CCPA_REQUIREMENTS] | [CCPA_PLAN] | [CCPA_RISK] | [CCPA_TIMELINE] |
| HIPAA | [HIPAA_SCOPE] | [HIPAA_STATUS] | [HIPAA_REQUIREMENTS] | [HIPAA_PLAN] | [HIPAA_RISK] | [HIPAA_TIMELINE] |
| SOX | [SOX_SCOPE] | [SOX_STATUS] | [SOX_REQUIREMENTS] | [SOX_PLAN] | [SOX_RISK] | [SOX_TIMELINE] |
| Industry Regulations | [INDUSTRY_SCOPE] | [INDUSTRY_STATUS] | [INDUSTRY_REQUIREMENTS] | [INDUSTRY_PLAN] | [INDUSTRY_RISK] | [INDUSTRY_TIMELINE] |
| International Standards | [INTL_SCOPE] | [INTL_STATUS] | [INTL_REQUIREMENTS] | [INTL_PLAN] | [INTL_RISK] | [INTL_TIMELINE] |

### 4. Data Security & Access Management

| **Security Layer** | **Current Controls** | **Target Controls** | **Implementation** | **Monitoring** | **Incident Response** | **Compliance Validation** |
|-------------------|--------------------|--------------------|-------------------|----------------|----------------------|--------------------------|
| Data Classification | [CLASS_CURRENT] | [CLASS_TARGET] | [CLASS_IMPLEMENTATION] | [CLASS_MONITORING] | [CLASS_INCIDENT] | [CLASS_COMPLIANCE] |
| Access Controls | [ACCESS_CURRENT] | [ACCESS_TARGET] | [ACCESS_IMPLEMENTATION] | [ACCESS_MONITORING] | [ACCESS_INCIDENT] | [ACCESS_COMPLIANCE] |
| Encryption | [ENCRYPT_CURRENT] | [ENCRYPT_TARGET] | [ENCRYPT_IMPLEMENTATION] | [ENCRYPT_MONITORING] | [ENCRYPT_INCIDENT] | [ENCRYPT_COMPLIANCE] |
| Data Masking | [MASK_CURRENT] | [MASK_TARGET] | [MASK_IMPLEMENTATION] | [MASK_MONITORING] | [MASK_INCIDENT] | [MASK_COMPLIANCE] |
| Audit Logging | [AUDIT_CURRENT] | [AUDIT_TARGET] | [AUDIT_IMPLEMENTATION] | [AUDIT_MONITORING] | [AUDIT_INCIDENT] | [AUDIT_COMPLIANCE] |
| Data Loss Prevention | [DLP_CURRENT] | [DLP_TARGET] | [DLP_IMPLEMENTATION] | [DLP_MONITORING] | [DLP_INCIDENT] | [DLP_COMPLIANCE] |
| Backup & Recovery | [BACKUP_CURRENT] | [BACKUP_TARGET] | [BACKUP_IMPLEMENTATION] | [BACKUP_MONITORING] | [BACKUP_INCIDENT] | [BACKUP_COMPLIANCE] |

### 5. Master Data Management Strategy

| **Master Data Entity** | **Current State** | **Target State** | **Data Sources** | **Golden Record Definition** | **Stewardship Model** | **Success Metrics** |
|-----------------------|------------------|-----------------|-----------------|----------------------------|----------------------|-------------------|
| Customer Master | [CUST_MDM_CURRENT] | [CUST_MDM_TARGET] | [CUST_MDM_SOURCES] | [CUST_MDM_GOLDEN] | [CUST_MDM_STEWARD] | [CUST_MDM_METRICS] |
| Product Master | [PROD_MDM_CURRENT] | [PROD_MDM_TARGET] | [PROD_MDM_SOURCES] | [PROD_MDM_GOLDEN] | [PROD_MDM_STEWARD] | [PROD_MDM_METRICS] |
| Vendor Master | [VENDOR_MDM_CURRENT] | [VENDOR_MDM_TARGET] | [VENDOR_MDM_SOURCES] | [VENDOR_MDM_GOLDEN] | [VENDOR_MDM_STEWARD] | [VENDOR_MDM_METRICS] |
| Employee Master | [EMP_MDM_CURRENT] | [EMP_MDM_TARGET] | [EMP_MDM_SOURCES] | [EMP_MDM_GOLDEN] | [EMP_MDM_STEWARD] | [EMP_MDM_METRICS] |
| Location Master | [LOC_MDM_CURRENT] | [LOC_MDM_TARGET] | [LOC_MDM_SOURCES] | [LOC_MDM_GOLDEN] | [LOC_MDM_STEWARD] | [LOC_MDM_METRICS] |
| Asset Master | [ASSET_MDM_CURRENT] | [ASSET_MDM_TARGET] | [ASSET_MDM_SOURCES] | [ASSET_MDM_GOLDEN] | [ASSET_MDM_STEWARD] | [ASSET_MDM_METRICS] |

### 6. Data Architecture & Integration Framework

| **Architecture Component** | **Current Architecture** | **Target Architecture** | **Integration Pattern** | **Technology Stack** | **Performance Requirements** | **Scalability Plan** |
|----------------------------|--------------------------|----------------------|----------------------|--------------------|-----------------------------|---------------------|
| Data Warehouse | [DW_CURRENT] | [DW_TARGET] | [DW_INTEGRATION] | [DW_TECH] | [DW_PERFORMANCE] | [DW_SCALABILITY] |
| Data Lake | [DL_CURRENT] | [DL_TARGET] | [DL_INTEGRATION] | [DL_TECH] | [DL_PERFORMANCE] | [DL_SCALABILITY] |
| Data Mart | [DM_CURRENT] | [DM_TARGET] | [DM_INTEGRATION] | [DM_TECH] | [DM_PERFORMANCE] | [DM_SCALABILITY] |
| Real-time Analytics | [RT_CURRENT] | [RT_TARGET] | [RT_INTEGRATION] | [RT_TECH] | [RT_PERFORMANCE] | [RT_SCALABILITY] |
| API Layer | [API_CURRENT] | [API_TARGET] | [API_INTEGRATION] | [API_TECH] | [API_PERFORMANCE] | [API_SCALABILITY] |
| Data Catalog | [CAT_CURRENT] | [CAT_TARGET] | [CAT_INTEGRATION] | [CAT_TECH] | [CAT_PERFORMANCE] | [CAT_SCALABILITY] |

### 7. Data Lifecycle Management

| **Lifecycle Stage** | **Policies** | **Retention Rules** | **Storage Tier** | **Access Controls** | **Disposal Process** | **Compliance Requirements** |
|---------------------|-------------|-------------------|-----------------|-------------------|--------------------|-----------------------------|
| Data Creation | [CREATE_POLICIES] | [CREATE_RETENTION] | [CREATE_STORAGE] | [CREATE_ACCESS] | [CREATE_DISPOSAL] | [CREATE_COMPLIANCE] |
| Active Use | [ACTIVE_POLICIES] | [ACTIVE_RETENTION] | [ACTIVE_STORAGE] | [ACTIVE_ACCESS] | [ACTIVE_DISPOSAL] | [ACTIVE_COMPLIANCE] |
| Archival | [ARCHIVE_POLICIES] | [ARCHIVE_RETENTION] | [ARCHIVE_STORAGE] | [ARCHIVE_ACCESS] | [ARCHIVE_DISPOSAL] | [ARCHIVE_COMPLIANCE] |
| Long-term Storage | [LONGTERM_POLICIES] | [LONGTERM_RETENTION] | [LONGTERM_STORAGE] | [LONGTERM_ACCESS] | [LONGTERM_DISPOSAL] | [LONGTERM_COMPLIANCE] |
| Data Destruction | [DESTROY_POLICIES] | [DESTROY_RETENTION] | [DESTROY_STORAGE] | [DESTROY_ACCESS] | [DESTROY_DISPOSAL] | [DESTROY_COMPLIANCE] |
| Legal Hold | [LEGAL_POLICIES] | [LEGAL_RETENTION] | [LEGAL_STORAGE] | [LEGAL_ACCESS] | [LEGAL_DISPOSAL] | [LEGAL_COMPLIANCE] |

### 8. Data Governance Organization & Roles

| **Governance Role** | **Responsibilities** | **Authority Level** | **Key Stakeholders** | **Success Metrics** | **Training Requirements** | **Performance Measures** |
|--------------------|---------------------|-------------------|----------------------|-------------------|--------------------------|-------------------------|
| Chief Data Officer | [CDO_RESPONSIBILITIES] | [CDO_AUTHORITY] | [CDO_STAKEHOLDERS] | [CDO_METRICS] | [CDO_TRAINING] | [CDO_PERFORMANCE] |
| Data Governance Council | [DGC_RESPONSIBILITIES] | [DGC_AUTHORITY] | [DGC_STAKEHOLDERS] | [DGC_METRICS] | [DGC_TRAINING] | [DGC_PERFORMANCE] |
| Data Stewards | [STEWARD_RESPONSIBILITIES] | [STEWARD_AUTHORITY] | [STEWARD_STAKEHOLDERS] | [STEWARD_METRICS] | [STEWARD_TRAINING] | [STEWARD_PERFORMANCE] |
| Data Custodians | [CUSTODIAN_RESPONSIBILITIES] | [CUSTODIAN_AUTHORITY] | [CUSTODIAN_STAKEHOLDERS] | [CUSTODIAN_METRICS] | [CUSTODIAN_TRAINING] | [CUSTODIAN_PERFORMANCE] |
| Data Owners | [OWNER_RESPONSIBILITIES] | [OWNER_AUTHORITY] | [OWNER_STAKEHOLDERS] | [OWNER_METRICS] | [OWNER_TRAINING] | [OWNER_PERFORMANCE] |
| Privacy Officer | [PRIVACY_RESPONSIBILITIES] | [PRIVACY_AUTHORITY] | [PRIVACY_STAKEHOLDERS] | [PRIVACY_METRICS] | [PRIVACY_TRAINING] | [PRIVACY_PERFORMANCE] |

### 9. Data Analytics & Value Creation

| **Analytics Domain** | **Use Cases** | **Data Requirements** | **Technology Platform** | **Skill Requirements** | **Value Metrics** | **ROI Targets** |
|---------------------|---------------|----------------------|------------------------|-------------------|--------------------|----------------|
| Descriptive Analytics | [DESC_USE_CASES] | [DESC_DATA_REQ] | [DESC_PLATFORM] | [DESC_SKILLS] | [DESC_VALUE] | [DESC_ROI] |
| Diagnostic Analytics | [DIAG_USE_CASES] | [DIAG_DATA_REQ] | [DIAG_PLATFORM] | [DIAG_SKILLS] | [DIAG_VALUE] | [DIAG_ROI] |
| Predictive Analytics | [PRED_USE_CASES] | [PRED_DATA_REQ] | [PRED_PLATFORM] | [PRED_SKILLS] | [PRED_VALUE] | [PRED_ROI] |
| Prescriptive Analytics | [PRESC_USE_CASES] | [PRESC_DATA_REQ] | [PRESC_PLATFORM] | [PRESC_SKILLS] | [PRESC_VALUE] | [PRESC_ROI] |
| Real-time Analytics | [RT_ANAL_USE_CASES] | [RT_ANAL_DATA_REQ] | [RT_ANAL_PLATFORM] | [RT_ANAL_SKILLS] | [RT_ANAL_VALUE] | [RT_ANAL_ROI] |
| AI/ML Applications | [AI_USE_CASES] | [AI_DATA_REQ] | [AI_PLATFORM] | [AI_SKILLS] | [AI_VALUE] | [AI_ROI] |

### 10. Performance Measurement & Continuous Improvement

| **Governance Metric** | **Definition** | **Target Value** | **Current Value** | **Measurement Method** | **Reporting Frequency** | **Improvement Actions** |
|----------------------|----------------|------------------|-------------------|----------------------|------------------------|------------------------|
| Data Quality Score | [DQ_DEFINITION] | [DQ_TARGET]% | [DQ_CURRENT]% | [DQ_METHOD] | [DQ_FREQUENCY] | [DQ_ACTIONS] |
| Data Compliance Rate | [COMPLIANCE_DEFINITION] | [COMPLIANCE_TARGET]% | [COMPLIANCE_CURRENT]% | [COMPLIANCE_METHOD] | [COMPLIANCE_FREQUENCY] | [COMPLIANCE_ACTIONS] |
| Data Accessibility | [ACCESS_DEFINITION] | [ACCESS_TARGET]% | [ACCESS_CURRENT]% | [ACCESS_METHOD] | [ACCESS_FREQUENCY] | [ACCESS_ACTIONS] |
| Data Literacy Score | [LITERACY_DEFINITION] | [LITERACY_TARGET]% | [LITERACY_CURRENT]% | [LITERACY_METHOD] | [LITERACY_FREQUENCY] | [LITERACY_ACTIONS] |
| Data Value Realization | [VALUE_DEFINITION] | $[VALUE_TARGET] | $[VALUE_CURRENT] | [VALUE_METHOD] | [VALUE_FREQUENCY] | [VALUE_ACTIONS] |
| Incident Response Time | [INCIDENT_DEFINITION] | [INCIDENT_TARGET] hrs | [INCIDENT_CURRENT] hrs | [INCIDENT_METHOD] | [INCIDENT_FREQUENCY] | [INCIDENT_ACTIONS] |
| Data Catalog Coverage | [CATALOG_DEFINITION] | [CATALOG_TARGET]% | [CATALOG_CURRENT]% | [CATALOG_METHOD] | [CATALOG_FREQUENCY] | [CATALOG_ACTIONS] |

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
### Example 1: Financial Services Data Governance
```
Company: Regional bank with $50B assets
Data Volume: 500TB across 150 systems
Compliance: GDPR, SOX, Basel III
Budget: $15M over 3 years
Focus: Risk management, regulatory reporting
Target: 95% data quality, 100% compliance
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[COMPANY_NAME]` | Name of the company | "Acme Corporation", "Global Financial Services", "HealthTech Solutions" |
| `[DATA_VOLUME]` | Total volume of enterprise data | "500TB", "2PB", "100TB", "5PB across all systems" |
| `[SYSTEM_COUNT]` | Number of data source systems | "50 systems", "150 applications", "25 databases", "200+ data sources" |
| `[GOVERNANCE_BUDGET]` | Budget allocation for governance | "$500,000", "$2M annual", "$15M over 3 years", "$5M/year" |
| `[TIMELINE]` | Timeline or schedule for implementation | "6 months", "18 months", "3-year roadmap", "Q1-Q4 2025" |
| `[DATA_QUALITY_TARGET]` | Target data quality percentage | "95%", "99%", "98% for critical data", "95% completeness, 99% accuracy" |
| `[COMPLIANCE_TARGET]` | Target regulatory compliance rate | "100%", "99.9%", "100% for GDPR/CCPA", "Full SOX compliance" |
| `[DATA_VALUE_TARGET]` | Target measurable data value | "$10M annual ROI", "$50M cost savings", "20% revenue increase", "$5M analytics value" |
| `[STRATEGY_CURRENT]` | Current maturity score (1-5 scale) | "2", "1 (Initial)", "3 (Defined)", "2.5 average across domains" |
| `[STRATEGY_TARGET]` | Target maturity score (1-5 scale) | "4", "5 (Optimizing)", "4 (Managed)", "4.5 enterprise-wide" |
| `[STRATEGY_GAP]` | Gap analysis for strategy domain | "No formal data strategy documented", "Strategy exists but not executed", "Siloed departmental strategies" |
| `[STRATEGY_ISSUES]` | Critical issues in strategy domain | "Lack of executive sponsorship", "No data strategy alignment with business", "Unclear data ownership" |
| `[STRATEGY_PRIORITY]` | Strategy or approach for priority | "High" |
| `[STRATEGY_TIMELINE]` | Strategy or approach for timeline | "6 months" |
| `[QUALITY_CURRENT]` | Current data quality maturity score | "2", "1 (Ad-hoc profiling only)", "3 (Basic rules in place)", "2.5" |
| `[QUALITY_TARGET]` | Target data quality maturity | "4", "5 (Automated quality monitoring)", "4 (Proactive remediation)" |
| `[QUALITY_GAP]` | Gap in data quality capabilities | "No automated profiling", "Manual quality checks only", "Missing data lineage" |
| `[QUALITY_ISSUES]` | Critical data quality issues | "30% duplicate customer records", "Inconsistent product codes", "Missing validation rules" |
| `[QUALITY_PRIORITY]` | Priority level for quality initiatives | "Critical", "High", "Medium", "P1 - Customer data" |
| `[QUALITY_TIMELINE]` | Timeline for quality improvements | "Q1-Q2 2025", "6 months", "12 months phased", "90 days for critical" |
| `[PRIVACY_CURRENT]` | Current privacy maturity score | "2", "3 (GDPR-compliant)", "1 (Minimal controls)", "2.5" |
| `[PRIVACY_TARGET]` | Target privacy maturity | "4", "5 (Privacy by design)", "4 (Automated consent management)" |
| `[PRIVACY_GAP]` | Gap in privacy capabilities | "No consent management system", "Manual DSR processing", "Incomplete data mapping" |
| `[PRIVACY_ISSUES]` | Critical privacy issues | "GDPR compliance gaps", "No data subject request workflow", "Missing privacy impact assessments" |
| `[PRIVACY_PRIORITY]` | Priority level for privacy initiatives | "Critical (regulatory)", "High", "P1 - GDPR deadline" |
| `[PRIVACY_TIMELINE]` | Timeline for privacy improvements | "Q1 2025", "6 months", "Before audit deadline", "Immediate" |
| `[SECURITY_CURRENT]` | Current security maturity score | "3", "2 (Basic access controls)", "4 (Encryption in place)", "2.5" |
| `[SECURITY_TARGET]` | Target security maturity | "5", "4 (Zero-trust architecture)", "5 (Automated threat detection)" |
| `[SECURITY_GAP]` | Gap in security capabilities | "No data classification", "Missing encryption at rest", "Incomplete access auditing" |
| `[SECURITY_ISSUES]` | Critical security issues | "Overprivileged access", "Unencrypted PII", "No DLP solution", "Weak audit trails" |
| `[SECURITY_PRIORITY]` | Priority level for security | "Critical", "High", "P1 - PCI compliance", "Immediate for PII" |
| `[SECURITY_TIMELINE]` | Timeline for security improvements | "Q1 2025", "90 days", "6 months phased", "30 days for critical" |
| `[MDM_CURRENT]` | Current MDM maturity score | "1", "2 (Siloed masters)", "3 (Partial integration)", "1.5" |
| `[MDM_TARGET]` | Target MDM maturity | "4", "5 (Golden record automation)", "4 (Real-time synchronization)" |
| `[MDM_GAP]` | Gap in MDM capabilities | "No single customer view", "Multiple product catalogs", "No golden record definition" |
| `[MDM_ISSUES]` | Critical MDM issues | "5 conflicting customer databases", "No vendor deduplication", "Orphaned master records" |
| `[MDM_PRIORITY]` | Priority level for MDM | "High", "Critical for customer 360", "P1 - M&A integration" |
| `[MDM_TIMELINE]` | Timeline for MDM implementation | "12 months", "18 months phased", "Q1-Q4 2025", "2-year roadmap" |
| `[ARCH_CURRENT]` | Current architecture maturity score | "2", "3 (Hybrid cloud)", "1 (Legacy only)", "2.5" |
| `[ARCH_TARGET]` | Target architecture maturity | "4", "5 (Modern data mesh)", "4 (Cloud-native lakehouse)" |
| `[ARCH_GAP]` | Gap in architecture capabilities | "No data lake", "Siloed data warehouses", "Missing real-time layer" |
| `[ARCH_ISSUES]` | Critical architecture issues | "Technical debt in ETL", "Scalability limits", "No self-service capabilities" |
| `[ARCH_PRIORITY]` | Priority level for architecture | "High", "Medium", "P2 - After MDM", "Critical for analytics" |
| `[ARCH_TIMELINE]` | Timeline for architecture modernization | "2 years", "18 months", "Q2-Q4 2025", "3-year transformation" |
| `[LIFECYCLE_CURRENT]` | Current lifecycle management maturity | "1", "2 (Basic retention)", "3 (Policies defined)", "1.5" |
| `[LIFECYCLE_TARGET]` | Target lifecycle maturity | "4", "5 (Automated lifecycle)", "4 (Policy-driven archival)" |
| `[LIFECYCLE_GAP]` | Gap in lifecycle capabilities | "No retention policies", "Manual archival process", "Missing disposal procedures" |
| `[LIFECYCLE_ISSUES]` | Critical lifecycle issues | "Unlimited data retention", "No legal hold process", "Storage cost growth 40%/year" |
| `[LIFECYCLE_PRIORITY]` | Priority level for lifecycle | "Medium", "High (cost control)", "P2", "Critical for compliance" |
| `[LIFECYCLE_TIMELINE]` | Timeline for lifecycle implementation | "6 months", "Q2 2025", "12 months", "90 days for legal hold" |
| `[LITERACY_CURRENT]` | Current data literacy maturity | "2", "1 (Limited training)", "3 (Some self-service)", "2" |
| `[LITERACY_TARGET]` | Target data literacy maturity | "4", "5 (Data-driven culture)", "4 (Widespread self-service)" |
| `[LITERACY_GAP]` | Gap in data literacy | "No formal training program", "Limited analytics adoption", "Tribal knowledge only" |
| `[LITERACY_ISSUES]` | Critical literacy issues | "20% tool adoption rate", "Shadow IT analytics", "No data steward community" |
| `[LITERACY_PRIORITY]` | Priority level for literacy | "Medium", "High", "P2 - After governance foundation" |
| `[LITERACY_TIMELINE]` | Timeline for literacy program | "12 months", "Ongoing", "Q1-Q4 2025", "6-month pilot" |
| `[CUST_DIMENSIONS]` | Quality dimensions for customer data | "Completeness, Accuracy, Uniqueness, Timeliness", "Name/Address validation, Email format, Duplicate detection" |
| `[CUST_CURRENT]` | Current customer data quality score | "72%", "85%", "68% (duplicates issue)", "78% composite score" |
| `[CUST_TARGET]` | Target customer data quality score | "95%", "98%", "99% for golden records", "95% minimum threshold" |
| `[CUST_RULES]` | Quality rules for customer data | "Email regex validation", "Address standardization", "Phone format check", "Duplicate matching >85% confidence" |
| `[CUST_MONITORING]` | Monitoring method for customer data | "Daily profiling via Great Expectations", "Real-time validation", "Weekly quality dashboards", "Automated alerts on threshold breach" |
| `[CUST_REMEDIATION]` | Remediation process for customer data | "Auto-correction for formatting", "Manual review queue for duplicates", "Source system notification", "Data steward escalation" |
| `[PROD_DIMENSIONS]` | Quality dimensions for product data | "Completeness, Consistency, Validity", "SKU format, Price validation, Category hierarchy" |
| `[PROD_CURRENT]` | Current product data quality score | "82%", "75%", "88%", "80% (missing attributes)" |
| `[PROD_TARGET]` | Target product data quality score | "98%", "95%", "99% for catalog", "97% minimum" |
| `[PROD_RULES]` | Quality rules for product data | "SKU format validation", "Price range checks", "Required attribute completeness", "Category code lookup" |
| `[PROD_MONITORING]` | Monitoring method for product data | "Daily catalog scans", "Real-time PIM validation", "Weekly completeness reports", "Change detection alerts" |
| `[PROD_REMEDIATION]` | Remediation process for product data | "PIM workflow for missing data", "Supplier notification for discrepancies", "Automated enrichment", "Manual category assignment" |
| `[FIN_DIMENSIONS]` | Quality dimensions for financial data | "Accuracy, Completeness, Timeliness, Auditability", "Balance reconciliation, Transaction integrity" |
| `[FIN_CURRENT]` | Current financial data quality score | "94%", "91%", "96%", "92% (timing issues)" |
| `[FIN_TARGET]` | Target financial data quality score | "99.9%", "99.5%", "100% for audit", "99% minimum" |
| `[FIN_RULES]` | Quality rules for financial data | "Double-entry balance checks", "Transaction amount validation", "GL code validation", "Period close completeness" |
| `[FIN_MONITORING]` | Monitoring method for financial data | "Real-time reconciliation", "Daily balance validation", "Monthly audit checks", "SOX control monitoring" |
| `[FIN_REMEDIATION]` | Remediation process for financial data | "Immediate escalation to finance", "Automated variance alerts", "Audit trail preservation", "Controller review process" |
| `[OPS_DIMENSIONS]` | Quality dimensions for operational data | "Timeliness, Accuracy, Completeness", "Sensor validation, Event sequencing, Throughput metrics" |
| `[OPS_CURRENT]` | Current operational data quality score | "78%", "82%", "75%", "80% (latency issues)" |
| `[OPS_TARGET]` | Target operational data quality score | "95%", "98%", "99% for real-time", "95% minimum" |
| `[OPS_RULES]` | Quality rules for operational data | "Timestamp validation", "Sensor range checks", "Event sequence validation", "Throughput threshold monitoring" |
| `[OPS_MONITORING]` | Monitoring method for operational data | "Real-time streaming validation", "Hourly aggregation checks", "Anomaly detection", "SLA monitoring dashboards" |
| `[OPS_REMEDIATION]` | Remediation process for operational data | "Automated sensor recalibration alerts", "Missing data interpolation", "Operator notification", "Maintenance ticket creation" |
| `[EMP_DIMENSIONS]` | Quality dimensions for employee data | "Completeness, Currency, Accuracy", "Identity validation, Role hierarchy, Compliance attributes" |
| `[EMP_CURRENT]` | Current employee data quality score | "85%", "88%", "82%", "86% (termination lag)" |
| `[EMP_TARGET]` | Target employee data quality score | "99%", "98%", "100% for compliance", "98% minimum" |
| `[EMP_RULES]` | Quality rules for employee data | "SSN/ID validation", "Manager hierarchy check", "Required training completeness", "Active directory sync validation" |
| `[EMP_MONITORING]` | Monitoring method for employee data | "Daily HRIS sync validation", "Weekly org hierarchy audit", "Monthly compliance check", "Real-time termination alerts" |
| `[EMP_REMEDIATION]` | Remediation process for employee data | "HR ticket for discrepancies", "Automated access revocation", "Manager notification for updates", "Compliance escalation" |
| `[VENDOR_DIMENSIONS]` | Quality dimensions for vendor data | "Completeness, Validity, Currency", "Tax ID validation, Banking details, Contract status" |
| `[VENDOR_CURRENT]` | Current vendor data quality score | "76%", "80%", "72%", "78% (onboarding backlog)" |
| `[VENDOR_TARGET]` | Target vendor data quality score | "95%", "98%", "99% for payments", "95% minimum" |
| `[VENDOR_RULES]` | Quality rules for vendor data | "Tax ID format validation", "Bank account verification", "Contract expiration alerts", "Compliance certification check" |
| `[VENDOR_MONITORING]` | Monitoring method for vendor data | "Monthly vendor file audit", "Payment validation pre-check", "Contract expiration monitoring", "Compliance certification tracking" |
| `[VENDOR_REMEDIATION]` | Remediation process for vendor data | "Procurement team notification", "Payment hold for invalid data", "Vendor portal update request", "Re-onboarding workflow" |
| `[REF_DIMENSIONS]` | Quality dimensions for reference data | "Consistency, Validity, Synchronization", "Code standardization, Cross-system alignment" |
| `[REF_CURRENT]` | Current reference data quality score | "88%", "90%", "85%", "87% (version drift)" |
| `[REF_TARGET]` | Target reference data quality score | "99%", "100%", "99.9% for lookups", "99% minimum" |
| `[REF_RULES]` | Quality rules for reference data | "Code format validation", "Cross-reference integrity", "Version synchronization", "Hierarchy validation" |
| `[REF_MONITORING]` | Monitoring method for reference data | "Real-time sync monitoring", "Daily cross-system reconciliation", "Version drift detection", "Usage pattern analysis" |
| `[REF_REMEDIATION]` | Remediation process for reference data | "Automated sync correction", "MDM team escalation", "Source system notification", "Emergency code freeze" |
| `[GDPR_SCOPE]` | Scope of GDPR compliance | "EU customer data processing", "All EEA personal data", "EU employees and customers", "Cross-border data transfers" |
| `[GDPR_STATUS]` | Current GDPR compliance status | "Compliant", "In Progress (70%)", "Remediation Required", "Annual certification pending" |
| `[GDPR_REQUIREMENTS]` | Key GDPR requirements | "Consent management, DSR workflow, DPIAs, Breach notification, Data mapping, Lawful basis documentation" |
| `[GDPR_PLAN]` | GDPR implementation plan | "Phase 1: Data mapping; Phase 2: Consent platform; Phase 3: DSR automation; Phase 4: Annual audit" |
| `[GDPR_RISK]` | GDPR compliance risk level | "High (pending DSR automation)", "Medium", "Low (fully compliant)", "Critical (consent gaps)" |
| `[GDPR_TIMELINE]` | Timeline for GDPR compliance | "Q1 2025 full compliance", "6 months", "Ongoing maintenance", "90 days for gaps" |
| `[CCPA_SCOPE]` | Scope of CCPA compliance | "California resident data", "US consumer PII", "California employees", "B2C customer records" |
| `[CCPA_STATUS]` | Current CCPA compliance status | "Compliant", "In Progress (80%)", "Opt-out mechanism pending", "Annual disclosure updated" |
| `[CCPA_REQUIREMENTS]` | Key CCPA requirements | "Right to know, Right to delete, Right to opt-out, Non-discrimination, Privacy notice updates" |
| `[CCPA_PLAN]` | CCPA implementation plan | "Phase 1: Privacy notice update; Phase 2: Opt-out mechanism; Phase 3: Data deletion workflow" |
| `[CCPA_RISK]` | CCPA compliance risk level | "Medium", "Low (mostly compliant)", "High (sale of data unclear)", "Medium (verification process)" |
| `[CCPA_TIMELINE]` | Timeline for CCPA compliance | "Q2 2025", "3 months", "Annual review cycle", "60 days for updates" |
| `[HIPAA_SCOPE]` | Scope of HIPAA compliance | "PHI in all systems", "Patient records", "Healthcare claims data", "Employee health records" |
| `[HIPAA_STATUS]` | Current HIPAA compliance status | "Compliant with annual audit", "In Progress", "BAAs current", "Risk assessment completed" |
| `[HIPAA_REQUIREMENTS]` | Key HIPAA requirements | "PHI encryption, Access controls, Audit logs, BAAs with vendors, Breach notification, Employee training" |
| `[HIPAA_PLAN]` | HIPAA implementation plan | "Phase 1: Risk assessment; Phase 2: Technical safeguards; Phase 3: Administrative policies; Phase 4: Training" |
| `[HIPAA_RISK]` | HIPAA compliance risk level | "High (encryption gaps)", "Medium", "Low (mature controls)", "Critical (BAA missing for vendor)" |
| `[HIPAA_TIMELINE]` | Timeline for HIPAA compliance | "Ongoing", "Q1 2025 audit prep", "6 months remediation", "Annual certification" |
| `[SOX_SCOPE]` | Scope of SOX compliance | "Financial reporting systems", "GL and sub-ledger data", "IT general controls", "Material accounts" |
| `[SOX_STATUS]` | Current SOX compliance status | "Compliant (no material weaknesses)", "In Progress", "Control deficiencies identified", "Year-end audit ready" |
| `[SOX_REQUIREMENTS]` | Key SOX requirements | "ITGC controls, Segregation of duties, Access reviews, Change management, Reconciliation controls" |
| `[SOX_PLAN]` | SOX implementation plan | "Q1: Control testing; Q2: Remediation; Q3: Management testing; Q4: External audit support" |
| `[SOX_RISK]` | SOX compliance risk level | "Medium (access review gaps)", "Low", "High (new system implementation)", "Material weakness risk" |
| `[SOX_TIMELINE]` | Timeline for SOX compliance | "Fiscal year-end", "Ongoing quarterly", "Annual audit cycle", "Q4 remediation deadline" |
| `[INDUSTRY_SCOPE]` | Scope of industry-specific regulations | "PCI-DSS for payment data", "FINRA for trading", "FDA for clinical data", "FedRAMP for government" |
| `[INDUSTRY_STATUS]` | Industry regulation compliance status | "PCI Level 1 certified", "FINRA audit passed", "FDA 21 CFR Part 11 compliant", "FedRAMP Moderate ATO" |
| `[INDUSTRY_REQUIREMENTS]` | Industry-specific requirements | "PCI: Cardholder data protection; FINRA: Records retention; FDA: Validation protocols; FedRAMP: Security controls" |
| `[INDUSTRY_PLAN]` | Industry compliance implementation plan | "Annual certification cycle", "Quarterly control testing", "Continuous monitoring program", "Gap remediation roadmap" |
| `[INDUSTRY_RISK]` | Industry-specific compliance risk | "Medium (PCI scope creep)", "Low", "High (new product launch)", "Critical (certification expiring)" |
| `[INDUSTRY_TIMELINE]` | Timeline for industry compliance | "Annual recertification", "Q2 2025 audit", "6 months for new requirements", "Ongoing monitoring" |
| `[INTL_SCOPE]` | Scope of international standards | "ISO 27001 certification", "SOC 2 Type II", "ISO 27701 privacy", "Cross-border data transfers" |
| `[INTL_STATUS]` | International standards compliance status | "ISO 27001 certified", "SOC 2 Type II annual", "ISO 27701 in progress", "SCCs implemented" |
| `[INTL_REQUIREMENTS]` | International standards requirements | "ISO 27001: ISMS controls; SOC 2: Trust principles; ISO 27701: Privacy controls; SCCs: Transfer mechanisms" |
| `[INTL_PLAN]` | International standards implementation plan | "Phase 1: Gap assessment; Phase 2: Control implementation; Phase 3: Internal audit; Phase 4: Certification" |
| `[INTL_RISK]` | International standards compliance risk | "Low (mature program)", "Medium (new geography)", "High (Brexit transfer impacts)", "Certification lapse risk" |
| `[INTL_TIMELINE]` | Timeline for international compliance | "Annual surveillance audit", "3-year recertification", "6 months for new standards", "Q3 2025 ISO 27701" |
| `[CLASS_CURRENT]` | Current data classification controls | "Manual classification only", "Public/Internal labels", "No formal classification", "Basic 3-tier system" |
| `[CLASS_TARGET]` | Target data classification controls | "Automated classification with ML", "4-tier: Public/Internal/Confidential/Restricted", "Policy-driven auto-labeling" |
| `[CLASS_IMPLEMENTATION]` | Classification implementation plan | "Deploy Microsoft Purview", "Implement sensitivity labels", "Train ML classifier", "Integrate with DLP" |
| `[CLASS_MONITORING]` | Classification monitoring approach | "Weekly label accuracy review", "Monthly coverage reports", "Real-time misclassification alerts", "Quarterly policy audit" |
| `[CLASS_INCIDENT]` | Classification incident response | "Immediate reclassification workflow", "Data owner notification", "Access restriction pending review", "Compliance team escalation" |
| `[CLASS_COMPLIANCE]` | Classification compliance validation | "Annual classification audit", "Spot check sampling", "Policy compliance scoring", "External audit ready" |
| `[ACCESS_CURRENT]` | Current access control state | "Basic RBAC", "Manual access requests", "No periodic review", "Local admin accounts exist" |
| `[ACCESS_TARGET]` | Target access control state | "Attribute-based access (ABAC)", "Zero-trust architecture", "Just-in-time access", "Automated provisioning/deprovisioning" |
| `[ACCESS_IMPLEMENTATION]` | Access control implementation plan | "Deploy identity governance (SailPoint/Saviynt)", "Implement PAM for privileged access", "SCIM integration", "Birthright access policies" |
| `[ACCESS_MONITORING]` | Access control monitoring approach | "Real-time access analytics", "Weekly privilege review", "Anomaly detection for unusual access", "Monthly orphan account cleanup" |
| `[ACCESS_INCIDENT]` | Access control incident response | "Immediate suspension of compromised accounts", "Forensic log preservation", "Access revocation workflow", "SOC escalation" |
| `[ACCESS_COMPLIANCE]` | Access control compliance validation | "Quarterly access certification", "SOX segregation of duties testing", "Annual penetration test", "Compliance dashboard" |
| `[ENCRYPT_CURRENT]` | Current encryption state | "TLS 1.2 in transit", "No encryption at rest", "Database TDE only", "Some systems unencrypted" |
| `[ENCRYPT_TARGET]` | Target encryption state | "TLS 1.3 everywhere", "AES-256 at rest for all PII", "End-to-end encryption", "HSM key management" |
| `[ENCRYPT_IMPLEMENTATION]` | Encryption implementation plan | "Deploy AWS KMS/Azure Key Vault", "Enable TDE on all databases", "Certificate management automation", "Field-level encryption for PII" |
| `[ENCRYPT_MONITORING]` | Encryption monitoring approach | "Certificate expiration monitoring", "Key rotation compliance tracking", "Encryption coverage dashboard", "TLS version monitoring" |
| `[ENCRYPT_INCIDENT]` | Encryption incident response | "Key compromise rotation procedure", "Certificate revocation workflow", "Data exposure assessment", "Forensic decryption for investigations" |
| `[ENCRYPT_COMPLIANCE]` | Encryption compliance validation | "Annual key management audit", "PCI encryption requirements testing", "HIPAA encryption validation", "Quarterly configuration review" |
| `[MASK_CURRENT]` | Current data masking state | "Manual masking for reports", "No dynamic masking", "Development uses production data", "Inconsistent masking rules" |
| `[MASK_TARGET]` | Target data masking state | "Dynamic masking in production", "Automated test data generation", "Format-preserving encryption", "Consistent masking policies" |
| `[MASK_IMPLEMENTATION]` | Data masking implementation plan | "Deploy Delphix/Informatica masking", "Define masking rules by data class", "Integrate with CI/CD for test environments", "Tokenization for payment data" |
| `[MASK_MONITORING]` | Data masking monitoring approach | "Masking coverage reports", "Unmasked data detection", "Test environment audits", "Real-time masking validation" |
| `[MASK_INCIDENT]` | Data masking incident response | "Immediate data recall for unmasked exposure", "Environment isolation", "Root cause analysis", "Re-masking workflow" |
| `[MASK_COMPLIANCE]` | Data masking compliance validation | "Non-production environment audits", "PCI masking validation", "GDPR pseudonymization checks", "Annual masking policy review" |
| `[AUDIT_CURRENT]` | Current audit logging state | "Basic application logs", "No centralized SIEM", "30-day retention only", "Incomplete audit trail" |
| `[AUDIT_TARGET]` | Target audit logging state | "Centralized SIEM (Splunk/Sentinel)", "7-year retention for compliance", "Real-time alerting", "Complete audit trail" |
| `[AUDIT_IMPLEMENTATION]` | Audit logging implementation plan | "Deploy Splunk Enterprise", "Standardize log format (CEF/OCSF)", "Enable all system audit logs", "Configure retention policies" |
| `[AUDIT_MONITORING]` | Audit logging monitoring approach | "Real-time log analysis", "Daily log integrity checks", "Anomaly detection rules", "Weekly security review" |
| `[AUDIT_INCIDENT]` | Audit logging incident response | "Log preservation for forensics", "Chain of custody documentation", "eDiscovery support", "Incident timeline reconstruction" |
| `[AUDIT_COMPLIANCE]` | Audit logging compliance validation | "SOX audit log review", "PCI log monitoring requirements", "HIPAA audit trail validation", "Annual log retention audit" |
| `[DLP_CURRENT]` | Current DLP state | "No DLP solution", "Email gateway only", "Limited endpoint protection", "No cloud DLP" |
| `[DLP_TARGET]` | Target DLP state | "Comprehensive DLP (endpoint, network, cloud)", "Integrated with classification", "Automated policy enforcement", "User coaching" |
| `[DLP_IMPLEMENTATION]` | DLP implementation plan | "Deploy Microsoft Purview DLP", "Define DLP policies by data class", "Enable cloud app monitoring", "User behavior analytics" |
| `[DLP_MONITORING]` | DLP monitoring approach | "Real-time incident dashboard", "Weekly policy violation reports", "False positive tuning", "Trend analysis" |
| `[DLP_INCIDENT]` | DLP incident response | "Automatic block for high-risk", "User notification and coaching", "Manager escalation workflow", "Compliance team review" |
| `[DLP_COMPLIANCE]` | DLP compliance validation | "Monthly policy effectiveness review", "Incident response testing", "Annual DLP audit", "Regulatory requirement mapping" |
| `[BACKUP_CURRENT]` | Current backup state | "Daily incremental backups", "Weekly full backups", "On-site storage only", "Manual recovery testing" |
| `[BACKUP_TARGET]` | Target backup state | "Continuous replication", "Immutable backups", "Geo-redundant storage", "Automated recovery testing" |
| `[BACKUP_IMPLEMENTATION]` | Backup implementation plan | "Deploy Veeam/Commvault", "Implement 3-2-1 rule", "Air-gapped backup copies", "Automated DR orchestration" |
| `[BACKUP_MONITORING]` | Backup monitoring approach | "Real-time backup success monitoring", "Daily backup verification", "Capacity forecasting", "RTO/RPO tracking" |
| `[BACKUP_INCIDENT]` | Backup incident response | "Ransomware isolation procedure", "Clean room recovery", "Backup integrity verification", "Business continuity activation" |
| `[BACKUP_COMPLIANCE]` | Backup compliance validation | "Annual DR test", "Quarterly recovery testing", "Backup encryption verification", "Retention policy audit" |
| `[CUST_MDM_CURRENT]` | Current customer MDM state | "5 siloed customer databases", "Partial CRM integration", "No single customer view", "Manual deduplication" |
| `[CUST_MDM_TARGET]` | Target customer MDM state | "Single Customer 360 view", "Real-time cross-channel sync", "Automated match/merge", "Self-service customer lookup" |
| `[CUST_MDM_SOURCES]` | Customer MDM source systems | "CRM (Salesforce), ERP (SAP), eCommerce, Support (ServiceNow), Marketing (Marketo)" |
| `[CUST_MDM_GOLDEN]` | Customer golden record definition | "Name + Email + Phone + Address, Match confidence >85%, CRM as system of record, Survivorship rules defined" |
| `[CUST_MDM_STEWARD]` | Customer MDM stewardship model | "Sales Operations owns customer master, Regional data stewards, Weekly exception review, Automated alerts" |
| `[CUST_MDM_METRICS]` | Customer MDM success metrics | "Duplicate rate <2%", "Match accuracy >95%", "Time to resolve <24hrs", "Customer completeness >98%" |
| `[PROD_MDM_CURRENT]` | Current product MDM state | "Multiple product catalogs", "Inconsistent SKUs", "Manual attribute management", "No PIM system" |
| `[PROD_MDM_TARGET]` | Target product MDM state | "Unified product catalog", "Single SKU hierarchy", "Automated attribute enrichment", "PIM-driven syndication" |
| `[PROD_MDM_SOURCES]` | Product MDM source systems | "ERP (SAP), PIM (Akeneo), eCommerce (Magento), PLM, Supplier portals" |
| `[PROD_MDM_GOLDEN]` | Product golden record definition | "SKU + GTIN + Description + Category, PIM as system of record, Supplier data merge rules" |
| `[PROD_MDM_STEWARD]` | Product MDM stewardship model | "Product Management owns master, Category managers as stewards, Supplier data validation workflow" |
| `[PROD_MDM_METRICS]` | Product MDM success metrics | "Attribute completeness >95%", "Image coverage 100%", "Syndication errors <1%", "Time to market <48hrs" |
| `[VENDOR_MDM_CURRENT]` | Current vendor MDM state | "Scattered vendor files", "Duplicate supplier records", "Manual onboarding", "Inconsistent banking data" |
| `[VENDOR_MDM_TARGET]` | Target vendor MDM state | "Centralized vendor master", "Automated onboarding portal", "Real-time compliance validation", "Single payment view" |
| `[VENDOR_MDM_SOURCES]` | Vendor MDM source systems | "ERP (SAP), Procurement (Ariba), AP system, Vendor portal, Compliance databases" |
| `[VENDOR_MDM_GOLDEN]` | Vendor golden record definition | "Tax ID + Name + Banking details, Procurement as system of record, Annual re-verification required" |
| `[VENDOR_MDM_STEWARD]` | Vendor MDM stewardship model | "Procurement owns vendor master, AP validates banking, Compliance team certifications, Category managers" |
| `[VENDOR_MDM_METRICS]` | Vendor MDM success metrics | "Duplicate rate <1%", "Onboarding time <5 days", "Banking accuracy 100%", "Compliance coverage 100%" |
| `[EMP_MDM_CURRENT]` | Current employee MDM state | "HRIS + AD disconnected", "Manual provisioning", "Delayed terminations", "Inconsistent org hierarchy" |
| `[EMP_MDM_TARGET]` | Target employee MDM state | "Unified employee identity", "Real-time HR-AD sync", "Automated lifecycle management", "Single org hierarchy" |
| `[EMP_MDM_SOURCES]` | Employee MDM source systems | "HRIS (Workday/SAP HCM), Active Directory, Badge system, Learning management, Payroll" |
| `[EMP_MDM_GOLDEN]` | Employee golden record definition | "Employee ID + Name + Department + Manager, HRIS as system of record, 24hr sync SLA" |
| `[EMP_MDM_STEWARD]` | Employee MDM stewardship model | "HR Operations owns master, IT owns technical identity, Managers validate reports, Automated sync" |
| `[EMP_MDM_METRICS]` | Employee MDM success metrics | "Sync accuracy 100%", "Termination processing <4hrs", "Org accuracy 100%", "Identity match 100%" |
| `[LOC_MDM_CURRENT]` | Current location MDM state | "Inconsistent address formats", "Multiple location codes", "No geocoding", "Regional variations" |
| `[LOC_MDM_TARGET]` | Target location MDM state | "Standardized addresses (USPS/CASS)", "Unified location hierarchy", "Geocoded locations", "Real-time validation" |
| `[LOC_MDM_SOURCES]` | Location MDM source systems | "ERP facility records, Real estate system, Store locator, Logistics, Tax jurisdictions" |
| `[LOC_MDM_GOLDEN]` | Location golden record definition | "Address + Geo coordinates + Type + Status, Real estate as system of record, USPS standardization" |
| `[LOC_MDM_STEWARD]` | Location MDM stewardship model | "Real Estate owns facility master, Finance owns cost centers, Operations owns operational status" |
| `[LOC_MDM_METRICS]` | Location MDM success metrics | "Address validation 100%", "Geocode accuracy >99%", "Hierarchy completeness 100%", "Tax jurisdiction accuracy 100%" |
| `[ASSET_MDM_CURRENT]` | Current asset MDM state | "Spreadsheet-based tracking", "Incomplete asset register", "No depreciation sync", "Manual audits" |
| `[ASSET_MDM_TARGET]` | Target asset MDM state | "Centralized asset repository", "Real-time tracking", "Automated depreciation", "Integrated maintenance" |
| `[ASSET_MDM_SOURCES]` | Asset MDM source systems | "Fixed asset system (SAP), IT asset management (ServiceNow), Maintenance (Maximo), Facilities" |
| `[ASSET_MDM_GOLDEN]` | Asset golden record definition | "Asset ID + Serial + Location + Owner + Value, Finance owns fixed assets, IT owns technology assets" |
| `[ASSET_MDM_STEWARD]` | Asset MDM stewardship model | "Finance owns fixed asset master, IT owns technology assets, Facilities owns building assets, Annual audit" |
| `[ASSET_MDM_METRICS]` | Asset MDM success metrics | "Asset accuracy >99%", "Audit variance <1%", "Depreciation sync 100%", "Location accuracy >98%" |
| `[DW_CURRENT]` | Current data warehouse state | "On-prem Oracle DW", "Legacy SQL Server", "Teradata at capacity", "Snowflake pilot" |
| `[DW_TARGET]` | Target data warehouse state | "Cloud DW (Snowflake/BigQuery)", "Serverless scaling", "Near-real-time refresh", "Self-service access" |
| `[DW_INTEGRATION]` | Data warehouse integration pattern | "ELT with dbt", "Batch ETL (Informatica)", "CDC streaming", "API-based ingestion" |
| `[DW_TECH]` | Data warehouse technology stack | "Snowflake + dbt + Fivetran", "BigQuery + Dataform", "Databricks SQL + Delta Lake", "Synapse Analytics" |
| `[DW_PERFORMANCE]` | Data warehouse performance requirements | "Query response <5s for 90%", "Concurrent users >500", "Daily load <4hrs", "99.9% availability" |
| `[DW_SCALABILITY]` | Data warehouse scalability plan | "Auto-scaling compute", "Multi-cluster warehouse", "Elastic capacity", "5x growth in 3 years" |
| `[DL_CURRENT]` | Current data lake state | "No data lake", "HDFS cluster", "S3 raw data dump", "Unstructured landing zone" |
| `[DL_TARGET]` | Target data lake state | "Governed lakehouse", "Delta Lake/Iceberg format", "Multi-zone architecture", "Self-service discovery" |
| `[DL_INTEGRATION]` | Data lake integration pattern | "Streaming ingestion (Kafka)", "Batch landing (Airflow)", "CDC replication", "API connectors" |
| `[DL_TECH]` | Data lake technology stack | "Databricks Lakehouse", "AWS Lake Formation + Glue", "Azure Data Lake Gen2 + Synapse", "GCP Dataplex" |
| `[DL_PERFORMANCE]` | Data lake performance requirements | "Ingestion latency <1hr", "Query federation <30s", "Petabyte-scale storage", "99.9% durability" |
| `[DL_SCALABILITY]` | Data lake scalability plan | "Object storage auto-scale", "Compute separation", "Zone-based partitioning", "10PB capacity plan" |
| `[DM_CURRENT]` | Current data mart state | "Siloed departmental marts", "Manual refresh", "Inconsistent metrics", "Excel extracts" |
| `[DM_TARGET]` | Target data mart state | "Governed semantic layer", "Self-service marts", "Consistent KPI definitions", "Automated refresh" |
| `[DM_INTEGRATION]` | Data mart integration pattern | "Push from DW", "Virtual marts (views)", "Materialized aggregations", "dbt models" |
| `[DM_TECH]` | Data mart technology stack | "dbt + Snowflake schemas", "Looker semantic layer", "Power BI datasets", "Tableau extracts" |
| `[DM_PERFORMANCE]` | Data mart performance requirements | "Dashboard load <3s", "Ad-hoc queries <10s", "Refresh frequency hourly", "99.5% availability" |
| `[DM_SCALABILITY]` | Data mart scalability plan | "Pre-aggregated cubes", "User-based scaling", "Query caching", "20 new marts/year" |
| `[RT_CURRENT]` | Current real-time analytics state | "No real-time capability", "Batch only (T+1)", "Limited streaming", "Manual dashboards" |
| `[RT_TARGET]` | Target real-time analytics state | "Sub-second streaming", "Real-time dashboards", "Event-driven alerts", "Operational analytics" |
| `[RT_INTEGRATION]` | Real-time integration pattern | "Kafka streaming", "Change data capture", "Event sourcing", "WebSocket feeds" |
| `[RT_TECH]` | Real-time technology stack | "Kafka + Flink + ksqlDB", "Spark Structured Streaming", "AWS Kinesis + Lambda", "Azure Stream Analytics" |
| `[RT_PERFORMANCE]` | Real-time performance requirements | "End-to-end latency <1s", "Event throughput 100K/s", "99.99% delivery", "Zero data loss" |
| `[RT_SCALABILITY]` | Real-time scalability plan | "Horizontal partition scaling", "Auto-scaling consumers", "Multi-region replication", "10x throughput headroom" |
| `[API_CURRENT]` | Current data API state | "No data APIs", "Point-to-point integrations", "Manual file transfers", "FTP-based" |
| `[API_TARGET]` | Target data API state | "RESTful data APIs", "GraphQL for complex queries", "Self-service API portal", "Rate-limited access" |
| `[API_INTEGRATION]` | Data API integration pattern | "API gateway (Kong/Apigee)", "OAuth 2.0 authentication", "OpenAPI specs", "Versioned endpoints" |
| `[API_TECH]` | Data API technology stack | "Kong + FastAPI", "Apigee + Spring Boot", "AWS API Gateway + Lambda", "GraphQL (Hasura/Apollo)" |
| `[API_PERFORMANCE]` | Data API performance requirements | "Response time <200ms", "99.9% uptime SLA", "1000 requests/sec", "Auto-scaling" |
| `[API_SCALABILITY]` | Data API scalability plan | "Horizontal scaling", "CDN caching", "Read replicas", "Multi-region deployment" |
| `[CAT_CURRENT]` | Current data catalog state | "No catalog", "Spreadsheet inventory", "Tribal knowledge", "Basic metadata" |
| `[CAT_TARGET]` | Target data catalog state | "Enterprise catalog (Alation/Collibra)", "Automated discovery", "Business glossary", "Data lineage" |
| `[CAT_INTEGRATION]` | Data catalog integration pattern | "Automated scanning", "Metadata harvesting", "Lineage extraction", "BI tool integration" |
| `[CAT_TECH]` | Data catalog technology stack | "Alation + Monte Carlo", "Collibra + Atlan", "DataHub + Great Expectations", "Azure Purview" |
| `[CAT_PERFORMANCE]` | Data catalog performance requirements | "Search response <2s", "Daily metadata refresh", "Full lineage depth", "99.9% availability" |
| `[CAT_SCALABILITY]` | Data catalog scalability plan | "100K+ assets", "1000+ users", "Automated tagging ML", "Federated catalogs" |
| `[CREATE_POLICIES]` | Data creation stage policies | "Classification at creation", "Metadata tagging required", "Quality validation on entry", "Source documentation" |
| `[CREATE_RETENTION]` | Data creation retention rules | "Initial classification determines retention", "Temporary data: 30 days", "Transaction data: 7 years", "PII: Policy-defined" |
| `[CREATE_STORAGE]` | Data creation storage tier | "Hot storage (SSD)", "Primary database tier", "High-performance storage", "Replicated for availability" |
| `[CREATE_ACCESS]` | Data creation access controls | "Creator has full access", "Team access by default", "Classification-based sharing", "Audit logging enabled" |
| `[CREATE_DISPOSAL]` | Data creation disposal process | "N/A for creation stage", "Validation failure: Reject", "Duplicate detection: Merge/reject", "Quality gate enforcement" |
| `[CREATE_COMPLIANCE]` | Data creation compliance requirements | "GDPR: Lawful basis documented", "Purpose limitation enforced", "Consent recorded", "Privacy notice provided" |
| `[ACTIVE_POLICIES]` | Active use stage policies | "Regular quality monitoring", "Access recertification", "Usage tracking", "Performance optimization" |
| `[ACTIVE_RETENTION]` | Active use retention rules | "Operational data: Active use period", "Transaction data: 1-3 years active", "Reference data: Indefinite active", "Logs: 90 days active" |
| `[ACTIVE_STORAGE]` | Active use storage tier | "Hot storage (SSD/NVMe)", "In-memory caching", "Replicated databases", "High-IOPS storage" |
| `[ACTIVE_ACCESS]` | Active use access controls | "Role-based access", "Need-to-know principle", "Quarterly access review", "Privileged access monitoring" |
| `[ACTIVE_DISPOSAL]` | Active use disposal process | "Transition to archive criteria", "Inactivity threshold: 12 months", "Business relevance review", "Migration validation" |
| `[ACTIVE_COMPLIANCE]` | Active use compliance requirements | "SOX: Active control monitoring", "HIPAA: Access audit logs", "GDPR: Purpose limitation", "PCI: Cardholder data minimization" |
| `[ARCHIVE_POLICIES]` | Archive stage policies | "Compressed storage", "Reduced access frequency", "Metadata preservation", "Searchable index" |
| `[ARCHIVE_RETENTION]` | Archive retention rules | "Financial records: 7 years", "HR records: 7 years post-employment", "Contracts: 10 years post-expiry", "Customer data: Per consent" |
| `[ARCHIVE_STORAGE]` | Archive storage tier | "Cool storage (HDD/Object)", "S3 Infrequent Access", "Azure Cool Blob", "Tape for large volumes" |
| `[ARCHIVE_ACCESS]` | Archive access controls | "Restricted access (approval required)", "Data steward authorization", "Audit all retrievals", "Time-limited access grants" |
| `[ARCHIVE_DISPOSAL]` | Archive disposal process | "Scheduled retention review", "Business approval for extension", "Regulatory hold check", "Disposal queue management" |
| `[ARCHIVE_COMPLIANCE]` | Archive compliance requirements | "eDiscovery readiness", "Regulatory retention periods", "Chain of custody", "Integrity verification" |
| `[LONGTERM_POLICIES]` | Long-term storage policies | "Immutable storage", "Encryption required", "Periodic integrity checks", "Format migration planning" |
| `[LONGTERM_RETENTION]` | Long-term retention rules | "Permanent records: Indefinite", "Legal requirements: Per regulation", "Historical data: Business decision", "Minimum 7-10 years typical" |
| `[LONGTERM_STORAGE]` | Long-term storage tier | "Glacier/Archive tier", "Tape libraries", "WORM storage", "Geo-redundant cold storage" |
| `[LONGTERM_ACCESS]` | Long-term access controls | "Executive approval required", "Legal/Compliance authorization", "48-72hr retrieval SLA", "Full audit trail" |
| `[LONGTERM_DISPOSAL]` | Long-term disposal process | "Regulatory approval required", "Legal review mandatory", "Documented destruction", "Certificate of destruction" |
| `[LONGTERM_COMPLIANCE]` | Long-term compliance requirements | "SEC Rule 17a-4", "IRS retention requirements", "Industry-specific mandates", "Cross-border transfer rules" |
| `[DESTROY_POLICIES]` | Data destruction policies | "Secure deletion methods", "Multi-pass overwrite", "Cryptographic erasure", "Physical destruction for media" |
| `[DESTROY_RETENTION]` | Data destruction retention rules | "Destruction records: 10 years", "Certificate retention: Permanent", "Audit logs: 7 years", "Approval records: 10 years" |
| `[DESTROY_STORAGE]` | Data destruction storage tier | "N/A - Data removed", "Destruction queue staging", "Verification environment", "Certificate storage" |
| `[DESTROY_ACCESS]` | Data destruction access controls | "Destruction team only", "Dual authorization required", "Segregation of duties", "Witnessed destruction" |
| `[DESTROY_DISPOSAL]` | Data destruction disposal process | "NIST SP 800-88 compliant", "DoD 5220.22-M for sensitive", "Verified destruction", "Certificate generation" |
| `[DESTROY_COMPLIANCE]` | Data destruction compliance requirements | "GDPR: Right to erasure fulfilled", "Documented destruction proof", "Regulatory notification if required", "Third-party destruction verification" |
| `[LEGAL_POLICIES]` | Legal hold policies | "Immediate preservation on notice", "Litigation hold procedures", "Custodian notification", "Collection protocols" |
| `[LEGAL_RETENTION]` | Legal hold retention rules | "Indefinite until hold released", "Override normal retention", "Preserve all relevant data", "No destruction during hold" |
| `[LEGAL_STORAGE]` | Legal hold storage tier | "Immutable preservation", "Chain of custody storage", "Forensic copy maintained", "Segregated hold repository" |
| `[LEGAL_ACCESS]` | Legal hold access controls | "Legal team access only", "eDiscovery platform access", "Custodian limited access", "Full audit logging" |
| `[LEGAL_DISPOSAL]` | Legal hold disposal process | "Hold release authorization required", "Legal sign-off mandatory", "Return to normal lifecycle", "Post-hold review" |
| `[LEGAL_COMPLIANCE]` | Legal hold compliance requirements | "FRCP compliance", "Spoliation prevention", "Defensible collection", "Proportionality assessment" |
| `[CDO_RESPONSIBILITIES]` | Chief Data Officer responsibilities | "Enterprise data strategy", "Governance program leadership", "Data-driven culture champion", "Executive stakeholder management", "Budget/resource allocation" |
| `[CDO_AUTHORITY]` | Chief Data Officer authority level | "C-suite executive", "Board reporting", "Cross-functional authority", "Policy approval", "Vendor selection authority" |
| `[CDO_STAKEHOLDERS]` | CDO key stakeholders | "CEO, CFO, CIO, CISO", "Business unit leaders", "Board of Directors", "Regulatory bodies", "External auditors" |
| `[CDO_METRICS]` | CDO success metrics | "Data ROI realized", "Governance maturity score", "Compliance rate", "Data quality improvement", "Analytics adoption rate" |
| `[CDO_TRAINING]` | CDO training requirements | "Executive data leadership", "Regulatory compliance updates", "Industry conferences", "Peer networking", "Board presentation skills" |
| `[CDO_PERFORMANCE]` | CDO performance measures | "Strategic objectives achieved", "Budget management", "Team development", "Stakeholder satisfaction", "Program milestone delivery" |
| `[DGC_RESPONSIBILITIES]` | Data Governance Council responsibilities | "Policy approval", "Cross-domain coordination", "Issue resolution", "Priority setting", "Resource allocation recommendations" |
| `[DGC_AUTHORITY]` | Data Governance Council authority | "Policy ratification", "Escalation resolution", "Initiative prioritization", "Standards approval", "Exception handling" |
| `[DGC_STAKEHOLDERS]` | Data Governance Council stakeholders | "CDO (Chair)", "Business domain leaders", "IT leadership", "Legal/Compliance", "Finance representative" |
| `[DGC_METRICS]` | Data Governance Council metrics | "Policies approved/quarter", "Issues resolved", "Meeting attendance", "Decision cycle time", "Initiative success rate" |
| `[DGC_TRAINING]` | Data Governance Council training | "Governance framework overview", "Policy development", "Decision-making processes", "Industry best practices", "Regulatory updates" |
| `[DGC_PERFORMANCE]` | Data Governance Council performance | "Decision effectiveness", "Policy adoption rate", "Stakeholder engagement", "Initiative delivery", "Conflict resolution time" |
| `[STEWARD_RESPONSIBILITIES]` | Data Steward responsibilities | "Data quality ownership", "Metadata management", "Issue investigation", "Policy enforcement", "User support and training" |
| `[STEWARD_AUTHORITY]` | Data Steward authority level | "Domain data decisions", "Quality rule definition", "Exception approval (limited)", "Issue escalation", "Access recommendations" |
| `[STEWARD_STAKEHOLDERS]` | Data Steward stakeholders | "Data owners", "Business analysts", "IT/Data engineers", "End users", "Compliance team" |
| `[STEWARD_METRICS]` | Data Steward success metrics | "Data quality score improvement", "Issue resolution time", "User satisfaction", "Metadata completeness", "Policy compliance rate" |
| `[STEWARD_TRAINING]` | Data Steward training requirements | "Data governance fundamentals", "Quality management tools", "Domain-specific training", "Communication skills", "Conflict resolution" |
| `[STEWARD_PERFORMANCE]` | Data Steward performance measures | "Quality KPIs met", "Issues resolved on time", "Stakeholder feedback", "Documentation currency", "Training completion" |
| `[CUSTODIAN_RESPONSIBILITIES]` | Data Custodian responsibilities | "Technical data management", "Security controls implementation", "Backup/recovery execution", "Performance optimization", "Infrastructure maintenance" |
| `[CUSTODIAN_AUTHORITY]` | Data Custodian authority level | "Technical implementation decisions", "Security configuration", "Storage allocation", "Performance tuning", "Incident response" |
| `[CUSTODIAN_STAKEHOLDERS]` | Data Custodian stakeholders | "Data owners", "Data stewards", "Security team", "Infrastructure team", "Application developers" |
| `[CUSTODIAN_METRICS]` | Data Custodian success metrics | "System availability", "Backup success rate", "Recovery time objectives met", "Security compliance", "Performance SLAs" |
| `[CUSTODIAN_TRAINING]` | Data Custodian training requirements | "Database administration", "Security certifications", "Cloud platform training", "Disaster recovery procedures", "Vendor-specific training" |
| `[CUSTODIAN_PERFORMANCE]` | Data Custodian performance measures | "Uptime percentage", "Incident response time", "Backup/recovery success", "Security audit results", "Capacity management" |
| `[OWNER_RESPONSIBILITIES]` | Data Owner responsibilities | "Accountability for data assets", "Access authorization", "Quality standards definition", "Business value realization", "Risk acceptance" |
| `[OWNER_AUTHORITY]` | Data Owner authority level | "Data access approval/denial", "Quality threshold setting", "Usage policy decisions", "Retention period approval", "Classification determination" |
| `[OWNER_STAKEHOLDERS]` | Data Owner stakeholders | "Executive sponsors", "Data stewards", "Business users", "Compliance/Legal", "IT partners" |
| `[OWNER_METRICS]` | Data Owner success metrics | "Data asset utilization", "Business value generated", "Compliance status", "User satisfaction", "Cost efficiency" |
| `[OWNER_TRAINING]` | Data Owner training requirements | "Data ownership principles", "Regulatory requirements", "Risk management", "Governance framework", "Value measurement" |
| `[OWNER_PERFORMANCE]` | Data Owner performance measures | "Asset value delivered", "Compliance achieved", "Access governance", "Quality oversight", "Strategic alignment" |
| `[PRIVACY_RESPONSIBILITIES]` | Privacy Officer responsibilities | "Privacy program management", "DPIA oversight", "Regulatory compliance", "Breach response coordination", "Privacy by design guidance" |
| `[PRIVACY_AUTHORITY]` | Privacy Officer authority level | "Privacy policy approval", "Processing activity review", "Breach notification decision", "Vendor assessment sign-off", "Regulatory liaison" |
| `[PRIVACY_STAKEHOLDERS]` | Privacy Officer stakeholders | "CDO", "Legal counsel", "CISO", "Business unit leaders", "Regulatory authorities", "Data subjects" |
| `[PRIVACY_METRICS]` | Privacy Officer success metrics | "DSR response time", "Breach count/severity", "DPIA completion rate", "Training completion", "Regulatory audit results" |
| `[PRIVACY_TRAINING]` | Privacy Officer training requirements | "CIPP/CIPM certification", "Regulatory updates (GDPR, CCPA)", "Privacy engineering", "Incident response", "Legal developments" |
| `[PRIVACY_PERFORMANCE]` | Privacy Officer performance measures | "Compliance audit results", "DSR SLA achievement", "Breach prevention", "Policy effectiveness", "Stakeholder confidence" |
| `[DESC_USE_CASES]` | Descriptive analytics use cases | "Executive dashboards", "KPI reporting", "Historical trend analysis", "Operational metrics", "Financial reporting" |
| `[DESC_DATA_REQ]` | Descriptive analytics data requirements | "Clean historical data", "Consistent metrics definitions", "Aggregated summaries", "Time-series data", "Dimensional hierarchies" |
| `[DESC_PLATFORM]` | Descriptive analytics platform | "Power BI", "Tableau", "Looker", "Qlik Sense", "AWS QuickSight" |
| `[DESC_SKILLS]` | Descriptive analytics skills required | "SQL proficiency", "Data visualization", "Business domain knowledge", "Dashboard design", "Stakeholder communication" |
| `[DESC_VALUE]` | Descriptive analytics value delivered | "Operational visibility", "Performance monitoring", "Compliance reporting", "Executive decision support", "Self-service insights" |
| `[DESC_ROI]` | Descriptive analytics ROI target | "20% reduction in reporting time", "$500K saved in manual reporting", "100+ self-service users", "5x dashboard adoption" |
| `[DIAG_USE_CASES]` | Diagnostic analytics use cases | "Root cause analysis", "Variance investigation", "Drill-down analysis", "Anomaly explanation", "Performance diagnostics" |
| `[DIAG_DATA_REQ]` | Diagnostic analytics data requirements | "Granular transaction data", "Event logs", "Contextual metadata", "Time-stamped records", "Correlated datasets" |
| `[DIAG_PLATFORM]` | Diagnostic analytics platform | "Power BI + DAX", "Tableau + Prep", "Looker + LookML", "Custom SQL + Python", "Splunk for logs" |
| `[DIAG_SKILLS]` | Diagnostic analytics skills required | "Advanced SQL", "Statistical analysis", "Root cause methodologies", "Data investigation", "Hypothesis testing" |
| `[DIAG_VALUE]` | Diagnostic analytics value delivered | "Faster issue resolution", "Process improvement insights", "Cost reduction opportunities", "Quality issue identification" |
| `[DIAG_ROI]` | Diagnostic analytics ROI target | "50% faster root cause identification", "$1M in identified savings", "30% reduction in issue recurrence" |
| `[PRED_USE_CASES]` | Predictive analytics use cases | "Demand forecasting", "Churn prediction", "Risk scoring", "Maintenance prediction", "Sales forecasting" |
| `[PRED_DATA_REQ]` | Predictive analytics data requirements | "Historical outcome data", "Feature engineering inputs", "Training/test datasets", "Real-time scoring data", "Labeled examples" |
| `[PRED_PLATFORM]` | Predictive analytics platform | "Azure ML", "AWS SageMaker", "Databricks ML", "Google Vertex AI", "DataRobot" |
| `[PRED_SKILLS]` | Predictive analytics skills required | "Machine learning", "Python/R programming", "Feature engineering", "Model validation", "MLOps practices" |
| `[PRED_VALUE]` | Predictive analytics value delivered | "Proactive decision-making", "Risk reduction", "Revenue optimization", "Resource planning", "Customer retention" |
| `[PRED_ROI]` | Predictive analytics ROI target | "15% churn reduction ($2M)", "20% forecast accuracy improvement", "$5M in predictive maintenance savings" |
| `[PRESC_USE_CASES]` | Prescriptive analytics use cases | "Price optimization", "Route optimization", "Resource allocation", "Treatment recommendations", "Next-best-action" |
| `[PRESC_DATA_REQ]` | Prescriptive analytics data requirements | "Constraint parameters", "Optimization objectives", "Real-time decision data", "Outcome feedback loops", "Simulation inputs" |
| `[PRESC_PLATFORM]` | Prescriptive analytics platform | "IBM Decision Optimization", "Gurobi/CPLEX", "AWS Personalize", "Google OR-Tools", "Custom optimization engines" |
| `[PRESC_SKILLS]` | Prescriptive analytics skills required | "Operations research", "Optimization algorithms", "Simulation modeling", "Decision science", "Business modeling" |
| `[PRESC_VALUE]` | Prescriptive analytics value delivered | "Optimized outcomes", "Automated decision-making", "Resource efficiency", "Personalized recommendations" |
| `[PRESC_ROI]` | Prescriptive analytics ROI target | "10% margin improvement", "$10M in optimization savings", "25% efficiency gains", "2x conversion improvement" |
| `[RT_ANAL_USE_CASES]` | Real-time analytics use cases | "Fraud detection", "Real-time personalization", "Operational monitoring", "IoT analytics", "Live dashboards" |
| `[RT_ANAL_DATA_REQ]` | Real-time analytics data requirements | "Streaming data feeds", "Sub-second latency", "Event-driven architecture", "In-memory processing", "Real-time enrichment" |
| `[RT_ANAL_PLATFORM]` | Real-time analytics platform | "Apache Kafka + Flink", "AWS Kinesis", "Azure Stream Analytics", "Google Dataflow", "Spark Structured Streaming" |
| `[RT_ANAL_SKILLS]` | Real-time analytics skills required | "Stream processing", "Event-driven architecture", "Real-time ML", "Performance optimization", "Distributed systems" |
| `[RT_ANAL_VALUE]` | Real-time analytics value delivered | "Immediate response to events", "Fraud prevention", "Customer engagement", "Operational excellence", "Competitive advantage" |
| `[RT_ANAL_ROI]` | Real-time analytics ROI target | "$5M fraud prevented annually", "30% engagement improvement", "99.9% event processing SLA", "Sub-second decision latency" |
| `[AI_USE_CASES]` | AI/ML application use cases | "NLP document processing", "Computer vision QA", "Recommendation engines", "Chatbots/Virtual assistants", "Generative AI" |
| `[AI_DATA_REQ]` | AI/ML data requirements | "Large labeled datasets", "Unstructured data processing", "Training infrastructure", "Model versioning", "Feature stores" |
| `[AI_PLATFORM]` | AI/ML platform | "Azure OpenAI + Cognitive Services", "AWS Bedrock + SageMaker", "Google Vertex AI", "Databricks ML", "Hugging Face" |
| `[AI_SKILLS]` | AI/ML skills required | "Deep learning", "NLP/Computer vision", "MLOps/LLMOps", "Prompt engineering", "Responsible AI", "Model governance" |
| `[AI_VALUE]` | AI/ML value delivered | "Process automation", "Enhanced customer experience", "New product capabilities", "Competitive differentiation", "Cost reduction" |
| `[AI_ROI]` | AI/ML ROI target | "50% process automation", "$20M in new revenue", "80% reduction in manual tasks", "NPS improvement +15 points" |
| `[DQ_DEFINITION]` | Data quality score definition | "Composite score of completeness, accuracy, consistency, timeliness, uniqueness weighted by business criticality" |
| `[DQ_TARGET]` | Data quality target percentage | "95%", "98% for critical data", "99% for financial data", "90% baseline" |
| `[DQ_CURRENT]` | Current data quality score | "78%", "82%", "85%", "72% (baseline assessment)" |
| `[DQ_METHOD]` | Data quality measurement method | "Automated profiling (Great Expectations)", "Rule-based validation", "Statistical sampling", "Continuous monitoring" |
| `[DQ_FREQUENCY]` | Data quality measurement frequency | "Real-time for critical", "Daily batch profiling", "Weekly scorecards", "Monthly executive reports" |
| `[DQ_ACTIONS]` | Data quality improvement actions | "Automated remediation rules", "Source system fixes", "Data steward workflows", "Root cause analysis", "Prevention controls" |
| `[COMPLIANCE_DEFINITION]` | Compliance rate definition | "Percentage of data assets meeting all applicable regulatory requirements and internal policies" |
| `[COMPLIANCE_CURRENT]` | Current compliance rate | "85%", "92%", "78%", "88% (last audit)" |
| `[COMPLIANCE_METHOD]` | Compliance measurement method | "Automated policy scans", "Audit sampling", "Control testing", "Self-assessment surveys" |
| `[COMPLIANCE_FREQUENCY]` | Compliance measurement frequency | "Continuous monitoring", "Quarterly control testing", "Annual audit", "Event-triggered reviews" |
| `[COMPLIANCE_ACTIONS]` | Compliance improvement actions | "Gap remediation plans", "Policy updates", "Training programs", "Control enhancements", "Tool implementations" |
| `[ACCESS_DEFINITION]` | Data accessibility definition | "Percentage of authorized users able to access required data within SLA, measured by request fulfillment rate" |
| `[ACCESS_METHOD]` | Accessibility measurement method | "User satisfaction surveys", "Access request fulfillment tracking", "Self-service adoption metrics", "SLA monitoring" |
| `[ACCESS_FREQUENCY]` | Accessibility measurement frequency | "Monthly user surveys", "Weekly request metrics", "Daily SLA tracking", "Quarterly reviews" |
| `[ACCESS_ACTIONS]` | Accessibility improvement actions | "Self-service enablement", "Access request automation", "Documentation improvement", "Training sessions", "Catalog enhancements" |
| `[LITERACY_DEFINITION]` | Data literacy score definition | "Organization-wide assessment of data comprehension, interpretation, and application skills across roles" |
| `[LITERACY_METHOD]` | Data literacy measurement method | "Skills assessments", "Certification completion", "Tool adoption rates", "Self-service usage metrics" |
| `[LITERACY_FREQUENCY]` | Data literacy measurement frequency | "Annual skills assessment", "Quarterly training metrics", "Monthly adoption tracking", "Continuous course completion" |
| `[LITERACY_ACTIONS]` | Data literacy improvement actions | "Training curriculum development", "Certification programs", "Champions network", "Lunch-and-learns", "Embedded coaching" |
| `[VALUE_DEFINITION]` | Data value realization definition | "Measurable business value generated from data assets including revenue, cost savings, and efficiency gains" |
| `[VALUE_TARGET]` | Data value target | "$10M annual", "$50M cumulative", "10x data investment ROI", "$5M/quarter" |
| `[VALUE_CURRENT]` | Current data value realized | "$3M", "$8M YTD", "4x ROI", "$2M/quarter" |
| `[VALUE_METHOD]` | Data value measurement method | "Use case value tracking", "Cost avoidance calculation", "Revenue attribution", "Efficiency measurement" |
| `[VALUE_FREQUENCY]` | Data value measurement frequency | "Quarterly business reviews", "Monthly use case tracking", "Annual ROI calculation", "Per-project post-mortems" |
| `[VALUE_ACTIONS]` | Data value improvement actions | "High-value use case prioritization", "Analytics enablement", "Data product development", "Monetization exploration" |
| `[INCIDENT_DEFINITION]` | Incident response time definition | "Average time from data incident detection to resolution, measured in hours across severity levels" |
| `[INCIDENT_TARGET]` | Incident response time target | "4 hrs (Critical)", "24 hrs (High)", "72 hrs (Medium)", "7 days (Low)" |
| `[INCIDENT_CURRENT]` | Current incident response time | "8 hrs", "36 hrs", "5 days", "12 hrs average" |
| `[INCIDENT_METHOD]` | Incident measurement method | "ServiceNow ticket tracking", "MTTR calculation", "SLA compliance reporting", "Incident categorization" |
| `[INCIDENT_FREQUENCY]` | Incident measurement frequency | "Real-time dashboards", "Daily standups", "Weekly incident reviews", "Monthly trend analysis" |
| `[INCIDENT_ACTIONS]` | Incident response improvement actions | "Runbook development", "On-call rotation", "Automated alerting", "Post-incident reviews", "Prevention investments" |
| `[CATALOG_DEFINITION]` | Data catalog coverage definition | "Percentage of enterprise data assets documented in the data catalog with complete metadata and lineage" |
| `[CATALOG_TARGET]` | Data catalog coverage target | "90%", "95% for production data", "100% for critical assets", "80% Year 1" |
| `[CATALOG_CURRENT]` | Current data catalog coverage | "45%", "60%", "35%", "52% documented" |
| `[CATALOG_METHOD]` | Catalog coverage measurement method | "Automated asset discovery", "Metadata completeness scoring", "Lineage depth tracking", "User tagging metrics" |
| `[CATALOG_FREQUENCY]` | Catalog coverage measurement frequency | "Weekly discovery runs", "Monthly completeness reports", "Quarterly coverage reviews", "Continuous auto-cataloging" |
| `[CATALOG_ACTIONS]` | Catalog improvement actions | "Automated scanning expansion", "Steward documentation campaigns", "Crowdsourced tagging", "Integration with source systems" |

### Example 2: Healthcare Data Governance
```
Company: Health system with 20 hospitals
Data Volume: 2PB patient and operational data
Compliance: HIPAA, FDA, state regulations
Budget: $25M over 4 years
Focus: Patient safety, research enablement
Target: 99% privacy compliance, analytics ROI
```

### Example 3: Manufacturing Data Governance
```
Company: Global manufacturer, 50 plants
Data Volume: 1PB IoT and operational data
Compliance: ISO standards, environmental
Budget: $20M over 3 years
Focus: Operational efficiency, sustainability
Target: Real-time analytics, 40% cost reduction
```

## Customization Options

### 1. Industry Vertical
- Financial services/Banking
- Healthcare/Life sciences
- Manufacturing/Industrial
- Retail/Consumer goods
- Technology/Software
- Government/Public sector
- Energy/Utilities

### 2. Regulatory Environment
- Highly regulated industries
- Moderate compliance requirements
- Emerging regulatory landscape
- International/Multi-jurisdiction
- Industry-specific standards
- Privacy-focused regulations

### 3. Data Maturity Level
- Data governance beginners
- Intermediate data management
- Advanced analytics organizations
- Data-driven enterprises
- Digital transformation companies
- Legacy system modernization

### 4. Organization Size
- Small/Medium enterprises
- Large corporations
- Multi-national companies
- Government agencies
- Non-profit organizations
- Startups/Growth companies

### 5. Technology Landscape
- Cloud-first organizations
- Hybrid cloud environments
- Legacy system environments
- Modern data stack
- Real-time/Streaming data
- AI/ML-heavy organizations

### 6. Data Strategy Focus
- Operational efficiency
- Customer analytics
- Risk management
- Innovation enablement
- Regulatory compliance
- Revenue generation
- Cost optimization

### 7. Implementation Approach
- Centralized governance
- Federated model
- Domain-driven approach
- Agile implementation
- Waterfall methodology
- Continuous improvement focus