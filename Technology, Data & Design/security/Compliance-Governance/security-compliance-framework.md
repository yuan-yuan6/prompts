---
category: security
last_updated: 2025-11-11
title: Security Compliance Framework (SOC 2, ISO 27001, HIPAA, PCI-DSS)
tags:
- security
- compliance
- framework
use_cases:
- Achieving SOC 2, ISO 27001, HIPAA, or PCI-DSS compliance
- Building security compliance program from scratch
- Preparing for security audits and assessments
- Maintaining continuous compliance posture
related_templates:
- security/Cybersecurity/security-audit.md
- security/Cloud-Security/cloud-security-architecture.md
industries:
- finance
- government
- healthcare
- technology
type: template
difficulty: intermediate
slug: security-compliance-framework
---

# Security Compliance Framework

## Purpose
Comprehensive framework for achieving and maintaining security compliance (SOC 2, ISO 27001, HIPAA, PCI-DSS) including control implementation, evidence collection, audit preparation, and continuous compliance monitoring.

## Quick Compliance Prompt
Achieve [SOC 2/ISO 27001/HIPAA/PCI-DSS] compliance for [organization type] with [X employees], [Y systems]. Perform gap analysis against [framework] requirements. Create: control implementation roadmap, policy templates (security, access control, incident response), evidence collection procedures, audit preparation checklist, and continuous compliance monitoring plan. Timeline: [X months] to certification.

## Quick Start

**Need to achieve compliance quickly?** Use this minimal example:

### Minimal Example
```
Guide us through SOC 2 Type II compliance for our SaaS platform, implementing required security controls for Trust Services Criteria (Security, Availability, Confidentiality), establishing evidence collection processes, and preparing for auditor assessment.
```

### When to Use This
- Starting compliance journey from zero
- Preparing for first compliance audit
- Maintaining ongoing compliance
- Responding to customer security questionnaires
- Meeting contractual security requirements

### Basic 3-Step Workflow
1. **Gap Analysis** - Assess current state against requirements (1-2 weeks)
2. **Implement Controls** - Deploy required security controls (2-6 months)
3. **Audit & Certification** - Evidence collection and auditor review (1-3 months)

**Time to complete**: 6-12 months for initial certification, ongoing maintenance

---

## Template

```markdown
I need to achieve security compliance. Please provide comprehensive compliance implementation guidance.

## COMPLIANCE CONTEXT

### Target Framework
- Framework: [SOC2_TYPE_I_TYPE_II_ISO27001_HIPAA_PCI_DSS_NIST_CSF_GDPR]
- Trust Services Criteria: [SECURITY_AVAILABILITY_PROCESSING_INTEGRITY_CONFIDENTIALITY_PRIVACY]
- Timeline: [TARGET_COMPLETION_DATE]
- Business drivers: [CUSTOMER_REQUIREMENT_SALES_ENABLER_RISK_REDUCTION]

### Organization Profile
- Industry: [SAAS_HEALTHCARE_FINTECH_ECOMMERCE_ENTERPRISE_SOFTWARE]
- Company size: [EMPLOYEES_CUSTOMERS_REVENUE]
- Data handled: [PII_PHI_PCI_FINANCIAL_PROPRIETARY]
- Geographic scope: [US_EU_GLOBAL]
- Existing certifications: [NONE_OR_LIST]

### Current State
- Security maturity: [INITIAL_MANAGED_DEFINED_OPTIMIZED]
- Existing controls: [DESCRIBE_CURRENT_CONTROLS]
- Documentation: [POLICIES_PROCEDURES_EVIDENCE]
- Previous audits: [NONE_OR_RESULTS]
- Gaps identified: [KNOWN_DEFICIENCIES]

## FRAMEWORK-SPECIFIC GUIDANCE

### SOC 2 Compliance

**Trust Services Criteria:**

**CC1: Control Environment**
- Demonstrates commitment to integrity and ethical values
- Board oversight of risk and compliance
- Organizational structure and assignment of authority
- Commitment to competence
- Accountability mechanisms

**CC2: Communication & Information**
- Internal communication processes
- External communication processes
- Quality of information for control activities

**CC3: Risk Assessment**
- Risk identification and analysis
- Assessment of fraud risk
- Changes that could impact controls

**CC4: Monitoring Activities**
- Ongoing and periodic evaluations
- Remediation of deficiencies

**CC5: Control Activities**
- Selection and development of controls
- Technology controls
- Policies and procedures deployment

**CC6: Logical & Physical Access**
- Logical access controls
- Physical access controls
- Access removal process

**CC7: System Operations**
- Change management
- Configuration management
- Incident management
- Backup and recovery

**CC8: Change Management**
- System changes authorization
- Infrastructure and software maintenance

**CC9: Risk Mitigation**
- Risk mitigation activities
- Vendor management
- Business continuity

**Additional Criteria:**

**Availability (A1):**
- System availability monitoring
- Incident response
- Disaster recovery
- Service level agreements

**Confidentiality (C1):**
- Data classification
- Encryption
- Data retention
- Secure disposal

**Implementation Requirements:**
- Documented policies and procedures
- Control implementation evidence
- Testing evidence (screenshots, logs, reports)
- 3-12 month operating history (Type II)
- Management assertions
- Auditor testing results

### ISO 27001 Compliance

**Annex A Controls (93 controls across 14 domains):**

**A.5: Organizational Controls**
- Information security policies
- Roles and responsibilities
- Segregation of duties
- Management responsibilities
- Contact with authorities

**A.6: People Controls**
- Screening
- Terms and conditions of employment
- Information security awareness
- Disciplinary process

**A.7: Physical Controls**
- Physical security perimeter
- Physical entry controls
- Securing offices and facilities
- Protecting against threats
- Equipment security

**A.8: Technological Controls**
- User endpoint devices
- Privileged access rights
- Information access restriction
- Access to source code
- Secure authentication
- Capacity management
- Protection against malware
- Backup
- Logging and monitoring
- Cryptography
- Secure development
- Security testing
- Network security

**Implementation Requirements:**
- Information Security Management System (ISMS)
- Risk assessment and treatment
- Statement of Applicability (SoA)
- Security objectives and plans
- Internal audits
- Management review
- Continuous improvement

### HIPAA Compliance

**Administrative Safeguards:**
- Security Management Process
- Workforce Security
- Information Access Management
- Security Awareness and Training
- Security Incident Procedures
- Contingency Plan
- Business Associate Agreements

**Physical Safeguards:**
- Facility Access Controls
- Workstation Use and Security
- Device and Media Controls

**Technical Safeguards:**
- Access Control
- Audit Controls
- Integrity Controls
- Transmission Security

**Implementation Requirements:**
- Risk analysis and management
- Policies and procedures
- Encryption of ePHI
- Audit logs
- Breach notification process
- Business associate management

### PCI-DSS Compliance

**12 Requirements:**

1. Install and maintain firewall configuration
2. Do not use vendor-supplied defaults
3. Protect stored cardholder data
4. Encrypt transmission of cardholder data
5. Use and update anti-virus software
6. Develop and maintain secure systems
7. Restrict access to cardholder data
8. Assign unique ID to each person with computer access
9. Restrict physical access to cardholder data
10. Track and monitor access to network resources
11. Regularly test security systems
12. Maintain information security policy

**Implementation Requirements:**
- Network segmentation
- Cardholder Data Environment (CDE) definition
- Quarterly vulnerability scans (ASV)
- Annual penetration testing
- Quarterly compliance reports (AOC)
- Compensating controls documentation

## COMPLIANCE IMPLEMENTATION ROADMAP

### Phase 1: Planning & Gap Analysis (4-6 weeks)
- Select framework and scope
- Conduct gap assessment
- Define control objectives
- Assign responsibilities
- Create project plan

### Phase 2: Policy & Procedure Development (6-8 weeks)
- Write required policies
- Develop procedures and standards
- Create templates and forms
- Review and approval process
- Communication and training

### Phase 3: Control Implementation (3-6 months)
- Deploy technical controls
- Implement process controls
- Configure monitoring and logging
- Establish incident response
- Vendor management program

### Phase 4: Evidence Collection (3-12 months)
- Establish evidence repository
- Automate evidence collection
- Document control execution
- Maintain audit trail
- Regular control testing

### Phase 5: Audit Preparation (4-8 weeks)
- Internal readiness assessment
- Remediate identified gaps
- Organize evidence packages
- Conduct mock audit
- Select auditor

### Phase 6: Audit Execution (2-4 weeks)
- Opening meeting
- Document review
- Control testing
- Interviews
- Closing meeting

### Phase 7: Continuous Compliance (Ongoing)
- Quarterly control reviews
- Annual risk assessments
- Policy updates
- Training refreshers
- Continuous monitoring

## EVIDENCE COLLECTION

### Required Evidence Types:

**Policies & Procedures:**
- Information security policy
- Access control policy
- Incident response plan
- Business continuity plan
- Vendor management policy
- Change management policy

**Technical Evidence:**
- Configuration screenshots
- Security tool reports
- Log samples
- Vulnerability scan reports
- Penetration test results
- Backup verification

**Operational Evidence:**
- Access reviews
- Training records
- Incident tickets
- Change tickets
- Vendor assessments
- Risk assessment documents

**Organizational Evidence:**
- Organizational charts
- Role descriptions
- Board minutes
- Management approvals
- Contracts and agreements

## CONTROL MAPPING

Cross-framework control mapping for efficiency:

| Control Area | SOC 2 | ISO 27001 | HIPAA | PCI-DSS |
|--------------|-------|-----------|-------|---------|
| Access Control | CC6 | A.9 | 164.312(a) | 7,8 |
| Encryption | CC6 | A.10 | 164.312(a)(2) | 3,4 |
| Incident Response | CC7 | A.16 | 164.308(a)(6) | 12.10 |
| Risk Assessment | CC3 | A.5 | 164.308(a)(1) | 12.2 |
| Change Management | CC8 | A.14 | 164.308(a)(8) | 6 |
| Monitoring | CC7 | A.12 | 164.312(b) | 10 |

## OUTPUT REQUIREMENTS

Provide:
1. **Gap Assessment Report** - Current state vs requirements
2. **Implementation Roadmap** - Phased approach with timelines
3. **Control Matrix** - All controls mapped to requirements
4. **Policy Templates** - All required policies and procedures
5. **Evidence Collection Plan** - What, when, who, where
6. **Audit Preparation Checklist** - Readiness assessment
7. **Training Plan** - Employee awareness and compliance training
```
