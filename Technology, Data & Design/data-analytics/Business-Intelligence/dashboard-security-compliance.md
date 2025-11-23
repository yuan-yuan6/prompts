---
category: data-analytics
last_updated: 2025-11-22
related_templates:
- data-analytics/Business-Intelligence/dashboard-technical-implementation.md
- data-analytics/Business-Intelligence/dashboard-data-architecture.md
- data-analytics/Business-Intelligence/dashboard-design-overview.md
tags:
- data-analytics
- security
- compliance
title: Dashboard Security, Governance & Compliance
use_cases:
- Security architecture design
- Compliance framework implementation
- Access control configuration
industries:
- finance
- government
- healthcare
- technology
type: template
difficulty: intermediate
slug: dashboard-security-compliance
---

# Dashboard Security, Governance & Compliance

## Overview
Implement robust security measures, access controls, and compliance frameworks for dashboard solutions. This prompt guides security architecture design, data governance, and regulatory compliance implementation.

---

## Purpose
Use this prompt to:
- Design comprehensive security architecture
- Implement role-based access controls
- Ensure regulatory compliance
- Establish data governance framework

---

## Quick Start

**Security Setup Checklist (2 Hours):**
1. **Enable SSO with MFA** - Integrate with existing identity provider (Okta, Azure AD), require MFA for all users
2. **Define 3-5 roles** - Map users to roles (Executive → all data aggregated, Manager → department only, Analyst → detailed access)
3. **Implement row-level security** - Filter data by user attributes (e.g., WHERE region = user.region, WHERE department = user.department)
4. **Mask sensitive data** - Hide PII/PHI (SSN, DOB) except for authorized roles, use data masking for financial data
5. **Enable audit logging** - Log all access to sensitive dashboards, track data exports, set up alerts for unusual activity

**Key Decision:** For HIPAA/SOX compliance, enable encryption at rest (AES-256), in transit (TLS 1.2+), and implement full audit trails.

---

## Prompt

I need to design a comprehensive security and compliance framework for a dashboard solution with the following requirements:

### Security Context
**Organizational Requirements:**
- Organization type: [ORG_TYPE] (Public company/Private/Healthcare/Financial services/Government/Other)
- Industry regulations: [REGULATIONS] (GDPR/HIPAA/SOX/PCI-DSS/CCPA/Other/None)
- Data sensitivity level: [DATA_SENSITIVITY] (Public/Internal/Confidential/Highly confidential)
- Security maturity: [SECURITY_MATURITY] (Basic/Intermediate/Advanced)
- Compliance requirements: [COMPLIANCE_REQUIREMENTS]

**User Access:**
- Total users: [USER_COUNT]
- User types: [USER_TYPES] (Internal employees/External partners/Customers)
- Geographic distribution: [GEOGRAPHIC_DISTRIBUTION]
- Access patterns: [ACCESS_PATTERNS] (On-premises/Remote/Mixed)
- BYOD policy: [BYOD_POLICY] (Allowed/Restricted/Prohibited)

### Authentication & Authorization
**Authentication:**
- Authentication method: [AUTH_METHOD] (SSO/LDAP/OAuth/SAML/Multi-factor/Mixed)
- Identity provider: [IDENTITY_PROVIDER] (Okta/Azure AD/Google/AWS IAM/Other)
- MFA requirements: [MFA_REQUIREMENTS] (Required/Optional/Role-based)
- Session management: [SESSION_MANAGEMENT] (Timeout period, concurrent sessions)
- Password policy: [PASSWORD_POLICY]

**Authorization:**
- Access control model: [ACCESS_MODEL] (RBAC/ABAC/MAC/DAC)
- Role hierarchy: [ROLE_HIERARCHY]
- Permission levels: [PERMISSION_LEVELS]
- Row-level security: [ROW_LEVEL_SECURITY] (Required/Not required)
- Column-level security: [COLUMN_LEVEL_SECURITY] (Required/Not required)
- Dynamic data masking: [DATA_MASKING] (Required for PII/PHI/Financial data/Not required)

### Data Security
**Encryption:**
- Data at rest: [ENCRYPTION_AT_REST] (AES-256/Other/Not required)
- Data in transit: [ENCRYPTION_IN_TRANSIT] (TLS 1.2+/TLS 1.3/Other)
- Key management: [KEY_MANAGEMENT] (AWS KMS/Azure Key Vault/HashiCorp Vault/Other)
- Encryption scope: [ENCRYPTION_SCOPE] (Full database/Sensitive columns only)

**Data Protection:**
- PII handling: [PII_HANDLING]
- PHI requirements: [PHI_REQUIREMENTS] (HIPAA compliance if applicable)
- Data classification: [DATA_CLASSIFICATION] (Classification levels and handling)
- Data retention: [DATA_RETENTION] (Retention policies by data type)
- Data deletion: [DATA_DELETION] (Right to be forgotten implementation)
- Backup encryption: [BACKUP_ENCRYPTION]

### Network Security
**Network Controls:**
- Network architecture: [NETWORK_ARCHITECTURE] (VPN/Private link/Public internet)
- IP whitelisting: [IP_WHITELISTING] (Required/Not required)
- Firewall rules: [FIREWALL_RULES]
- DMZ requirements: [DMZ_REQUIREMENTS]
- API security: [API_SECURITY] (Rate limiting/Token validation/API keys)

**Infrastructure Security:**
- Cloud security groups: [SECURITY_GROUPS]
- Network segmentation: [NETWORK_SEGMENTATION]
- DDoS protection: [DDOS_PROTECTION]
- Web Application Firewall: [WAF_REQUIREMENTS]
- Intrusion detection: [IDS_IPS]

### Audit & Compliance
**Audit Requirements:**
- Audit logging scope: [AUDIT_SCOPE] (All access/Changes only/Admin actions)
- Log retention: [LOG_RETENTION] (Duration and storage)
- Audit trail requirements: [AUDIT_TRAIL]
- User activity monitoring: [ACTIVITY_MONITORING]
- Compliance reporting: [COMPLIANCE_REPORTING]

**Governance Framework:**
- Data ownership: [DATA_OWNERSHIP]
- Data stewardship: [DATA_STEWARDSHIP]
- Change management: [CHANGE_MANAGEMENT]
- Access review frequency: [ACCESS_REVIEW] (Quarterly/Semi-annual/Annual)
- Security assessment schedule: [SECURITY_ASSESSMENT]

### Compliance Requirements
**Regulatory Compliance:**
- GDPR requirements: [GDPR_REQUIREMENTS] (If applicable)
- HIPAA requirements: [HIPAA_REQUIREMENTS] (If applicable)
- SOX requirements: [SOX_REQUIREMENTS] (If applicable)
- PCI-DSS requirements: [PCI_REQUIREMENTS] (If applicable)
- Industry-specific regulations: [INDUSTRY_REGULATIONS]

**Privacy & Consent:**
- Privacy policy requirements: [PRIVACY_POLICY]
- Consent management: [CONSENT_MANAGEMENT]
- Data subject rights: [DATA_SUBJECT_RIGHTS] (Access/Rectification/Erasure/Portability)
- Cross-border data transfer: [DATA_TRANSFER] (Adequacy decisions/SCCs/BCRs)

### Incident Response
**Security Incident Management:**
- Incident response plan: [INCIDENT_RESPONSE_PLAN]
- Breach notification requirements: [BREACH_NOTIFICATION]
- Incident escalation: [INCIDENT_ESCALATION]
- Recovery time objective: [RTO]
- Recovery point objective: [RPO]

---

## Deliverables

Please provide:

1. **Security Architecture Design**
   - Security architecture diagram
   - Network security topology
   - Authentication and authorization flows
   - Data protection strategy
   - Security controls matrix

2. **Access Control Framework**
   - Role definition and hierarchy
   - Permission matrix by role
   - Row-level security rules
   - Column-level security specifications
   - Data masking rules
   - Access request and approval workflow

3. **Compliance Framework**
   - Regulatory requirements mapping
   - Compliance controls checklist
   - Privacy impact assessment
   - Data processing inventory
   - Compliance monitoring approach
   - Audit reporting templates

4. **Security Policies & Procedures**
   - Authentication and authorization policies
   - Data classification policy
   - Encryption policy
   - Access management procedures
   - Incident response procedures
   - Security awareness guidelines

5. **Audit & Monitoring Setup**
   - Audit logging configuration
   - Security monitoring dashboard design
   - Alert rules and thresholds
   - Log analysis approach
   - Compliance reporting framework

6. **Implementation Roadmap**
   - Security implementation phases
   - Compliance milestone timeline
   - Testing and validation plan
   - User training requirements
   - Ongoing maintenance schedule

---

## Example Usage

### Example: Healthcare Analytics Platform (HIPAA)

```
Organization type: Healthcare provider
Industry regulations: HIPAA, state privacy laws
Data sensitivity level: Highly confidential (PHI)
Security maturity: Advanced
Compliance requirements: HIPAA Privacy Rule, Security Rule, Breach Notification Rule

Total users: 200 (100 clinical staff, 75 administrative, 25 executives)
User types: Internal employees only
Geographic distribution: 5 hospital locations across 3 states
Access patterns: Mixed (on-premises and remote)
BYOD policy: Restricted - only approved devices with MDM

Authentication method: SSO with MFA
Identity provider: Azure AD
MFA requirements: Required for all users
Session management: 30-minute timeout, single session per user
Password policy: 12 characters, complexity required, 90-day expiration

Access control model: RBAC with row-level security
Role hierarchy: Physician > Nurse > Administrative > Executive (separate hierarchy)
Permission levels: Read, Read-Write, Admin
Row-level security: Required - users see only their department/location data
Column-level security: Required - hide SSN, financial data by role
Data masking: Required for SSN, date of birth, diagnosis codes (except for authorized roles)

Data at rest: AES-256 encryption
Data in transit: TLS 1.3
Key management: Azure Key Vault with HSM
Encryption scope: Full database encryption

PII handling: All PHI encrypted, access logged, minimum necessary principle
PHI requirements: Full HIPAA compliance - encryption, access controls, audit trails
Data classification: Public, Internal, PHI, Sensitive PHI
Data retention: Patient data 7 years, audit logs 6 years
Data deletion: Secure deletion process, logged and verified
Backup encryption: All backups encrypted, stored separately

Network architecture: Private VPN connections only
IP whitelisting: Required - only known hospital IPs
Firewall rules: Deny all, explicit allow for approved IPs
DMZ requirements: Not applicable (private network)
API security: JWT tokens, rate limiting, IP restrictions

Cloud security groups: Restrictive - only required ports
Network segmentation: Separate VPCs for prod/non-prod
DDoS protection: AWS Shield Standard
WAF requirements: AWS WAF with OWASP rules
IDS/IPS: AWS GuardDuty enabled

Audit logging scope: All access to PHI, all changes, all admin actions
Log retention: 6 years minimum
Audit trail requirements: Immutable logs, tamper-proof
User activity monitoring: Real-time monitoring, alerts on unusual patterns
Compliance reporting: Quarterly compliance reports, annual risk assessment

Data ownership: Clinical data - CMO, Financial data - CFO
Data stewardship: Each department has data steward
Change management: CAB approval for all changes
Access review frequency: Quarterly access reviews
Security assessment: Annual penetration testing, quarterly vulnerability scans

HIPAA requirements: Full compliance required
  - Privacy Rule: Minimum necessary, patient rights
  - Security Rule: Administrative, physical, technical safeguards
  - Breach Notification: 60-day notification process

Privacy policy: HIPAA Notice of Privacy Practices
Consent management: Track patient consent for data use
Data subject rights: Access, amendment, accounting of disclosures
Cross-border data transfer: Not applicable (US only)

Incident response plan: HIPAA-compliant IR plan with breach notification
Breach notification: <60 days to HHS and patients if >500 records
Incident escalation: Security team → Privacy officer → Legal → Executive
RTO: 4 hours for critical systems
RPO: 1 hour maximum data loss
```

---

## Usage Examples

### Example 1: Financial Services SOX Compliance

**Context:** Investment firm needs SOX-compliant dashboard security for financial reporting

**Copy-paste this prompt:**

```
I need to design a comprehensive security and compliance framework for a dashboard solution with the following requirements:

### Security Context
**Organizational Requirements:**
- Organization type: Public company (SEC registered investment advisor)
- Industry regulations: SOX, SEC Rule 17a-4, FINRA regulations
- Data sensitivity level: Highly confidential (financial data, client portfolios)
- Security maturity: Advanced (existing SOC 2 Type II certified)
- Compliance requirements: SOX 302/404, SEC Recordkeeping, FINRA 4511

**User Access:**
- Total users: 150 (50 portfolio managers, 75 analysts, 25 executives/compliance)
- User types: Internal employees only
- Geographic distribution: US offices (NYC, Chicago, SF)
- Access patterns: On-premises during trading hours, VPN for remote
- BYOD policy: Prohibited for trading systems

### Authentication & Authorization
**Authentication:**
- Authentication method: SSO with MFA (hardware token required for trading dashboards)
- Identity provider: Okta
- MFA requirements: Required for all users, hardware token for portfolio access
- Session management: 15-minute timeout for trading, 30-minute for reporting
- Password policy: 16 characters, complexity, 60-day rotation

**Authorization:**
- Access control model: RBAC with attribute-based restrictions
- Role hierarchy: Chief Investment Officer > Portfolio Manager > Analyst > Compliance (separate)
- Permission levels: View Aggregated, View Detailed, View + Export, Admin
- Row-level security: Required - users see only their assigned portfolios/clients
- Column-level security: Required - hide client PII except for authorized roles
- Dynamic data masking: Required for SSN, account numbers, detailed holdings (role-based)

### Data Security
**Encryption:**
- Data at rest: AES-256 encryption (all financial data)
- Data in transit: TLS 1.3 only
- Key management: AWS KMS with HSM, key rotation every 90 days
- Encryption scope: Full database encryption, separate keys per data classification

**Data Protection:**
- PII handling: Client SSN, DOB masked in dashboards, full access only for operations
- PHI requirements: N/A
- Data classification: Public, Internal, Confidential, Highly Confidential (trading data)
- Data retention: 7 years (SEC/FINRA requirement), trading data indefinite
- Backup encryption: All backups encrypted, stored in separate AWS region

### Audit & Compliance
**Audit Requirements:**
- Audit logging scope: All access to financial data, all exports, all admin actions
- Log retention: 7 years (regulatory requirement)
- Audit trail requirements: Immutable, tamper-evident, write-once storage (S3 Object Lock)
- User activity monitoring: Real-time monitoring, alerts on unusual access patterns
- Compliance reporting: Monthly SOX control reports, quarterly FINRA reports

**Governance Framework:**
- Data ownership: CIO owns investment data, CFO owns financial reporting, CCO owns compliance
- Change management: CAB approval required, change freeze during trading hours
- Access review frequency: Quarterly (SOX requirement), monthly for privileged access
- Security assessment: Annual SOC 2 Type II audit, quarterly penetration testing

Please provide:
1. SOX control framework mapped to dashboard security controls
2. Segregation of duties matrix for financial dashboard access
3. Audit logging specification for SEC recordkeeping compliance
4. Change management process for SOX-compliant dashboard updates
5. Evidence collection approach for annual SOX audit
```

**Expected Output:**
- SOX IT General Controls (ITGC) mapping for dashboard environment
- Segregation of duties: Portfolio managers can't approve their own trades, compliance has read-only
- Audit logging: Who accessed what data, when, from where, what they exported
- Change management: Dual approval, testing, documented rollback procedures

---

### Example 2: Retail GDPR and CCPA Compliance

**Context:** E-commerce company needs privacy-compliant customer analytics dashboards

**Copy-paste this prompt:**

```
I need to design a comprehensive security and compliance framework for a dashboard solution with the following requirements:

### Security Context
**Organizational Requirements:**
- Organization type: Private company (e-commerce retailer)
- Industry regulations: GDPR (EU customers), CCPA (California customers), PCI-DSS (payment data)
- Data sensitivity level: Confidential (customer PII, purchase history)
- Security maturity: Intermediate (growing data privacy program)
- Compliance requirements: GDPR Articles 5, 6, 17, 32; CCPA 1798.100-199

**User Access:**
- Total users: 75 (25 marketing, 30 operations, 15 customer service, 5 executives)
- User types: Internal employees, 5 external agency partners (marketing only)
- Geographic distribution: US headquarters, EU subsidiary (UK, Germany offices)
- Access patterns: Remote-first, VPN for sensitive data access
- BYOD policy: Allowed with MDM for corporate data

### Authentication & Authorization
**Authentication:**
- Authentication method: SSO with MFA
- Identity provider: Azure AD
- MFA requirements: Required for all users accessing customer data
- Session management: 60-minute timeout, single concurrent session
- Password policy: 12 characters, complexity, 90-day rotation

**Authorization:**
- Access control model: RBAC
- Role hierarchy: Executive > Marketing Manager > Marketing Analyst > Agency Partner (limited)
- Permission levels: No PII, Aggregated Only, PII Access (justified), Admin
- Row-level security: Required - regional teams see only their region (EU, US)
- Column-level security: Required - hide email, phone, address by default
- Dynamic data masking: Required for all PII fields, unmasked only with data access justification

### Data Security
**Encryption:**
- Data at rest: AES-256
- Data in transit: TLS 1.2+
- Key management: Azure Key Vault
- Encryption scope: All customer data encrypted

**Data Protection:**
- PII handling: Pseudonymization for analytics, full PII only for customer service with justification
- Data classification: Public, Internal, Personal Data, Sensitive Personal Data
- Data retention: 3 years for marketing analytics, 7 years for order history (legal requirement)
- Data deletion: Automated deletion workflows for GDPR Article 17 requests
- Right to erasure: Dashboard must exclude deleted customer data within 30 days

### Privacy & Consent
- Consent management: Track customer consent preferences, filter dashboards by consent status
- Data subject rights: Access request workflow, rectification, erasure, portability
- Cross-border data transfer: SCCs for EU→US transfer, UK Addendum for UK data
- Purpose limitation: Marketing dashboards only show customers who consented to marketing

### Audit & Compliance
**Audit Requirements:**
- Audit logging scope: All PII access logged with business justification
- Log retention: 2 years for access logs
- User activity monitoring: Alerts on bulk PII access or export
- Compliance reporting: Monthly GDPR compliance report, CCPA request tracking

Please provide:
1. GDPR Article 32 technical controls mapping for dashboard security
2. Data subject rights implementation in dashboards (right to access, erasure)
3. Consent-aware row-level security (filter data by consent status)
4. Cross-border data transfer compliance for EU customer data
5. Data minimization approach for marketing analytics
```

**Expected Output:**
- GDPR Article 32 controls: Encryption, access controls, pseudonymization, audit logging
- Data subject rights: Customer lookup dashboard for access requests, exclusion lists for erasure
- Consent filtering: WHERE consent_marketing = true in all marketing dashboards
- Privacy by design: Aggregate-first dashboards, drill-down to PII requires justification

---

### Example 3: Government Security (FedRAMP/FISMA)

**Context:** Government contractor needs FedRAMP-compliant analytics platform

**Copy-paste this prompt:**

```
I need to design a comprehensive security and compliance framework for a dashboard solution with the following requirements:

### Security Context
**Organizational Requirements:**
- Organization type: Government contractor (federal agency contract)
- Industry regulations: FedRAMP Moderate, FISMA, NIST 800-53, FIPS 140-2
- Data sensitivity level: Controlled Unclassified Information (CUI)
- Security maturity: Advanced (FedRAMP authorized cloud environment)
- Compliance requirements: FedRAMP Moderate baseline (325 controls), agency-specific ATOs

**User Access:**
- Total users: 500 (300 government users, 200 contractor users)
- User types: Federal employees, contractors with public trust clearance
- Geographic distribution: CONUS only, government network access
- Access patterns: Government workstations, CAC/PIV authentication required
- BYOD policy: Prohibited

### Authentication & Authorization
**Authentication:**
- Authentication method: CAC/PIV smart card + PIN (two-factor)
- Identity provider: Agency's identity management system (ICAM)
- MFA requirements: Required - CAC/PIV mandatory for all CUI access
- Session management: 15-minute inactivity timeout, re-authentication required
- Password policy: N/A - certificate-based authentication

**Authorization:**
- Access control model: RBAC with mandatory access control (MAC) for CUI
- Role hierarchy: Federal Program Manager > Contracting Officer > Contractor PM > Analyst
- Permission levels: Unclassified, CUI-Basic, CUI-Specified (need-to-know)
- Row-level security: Required - users see only their program/contract data
- Column-level security: Required - CUI marked fields require CUI access role
- Dynamic data masking: Required for SSN, contract values (role-based unmasking)

### Data Security
**Encryption:**
- Data at rest: AES-256 (FIPS 140-2 validated modules)
- Data in transit: TLS 1.2 or TLS 1.3 with FIPS-validated algorithms
- Key management: FIPS 140-2 Level 3 HSM, agency-owned keys
- Encryption scope: All CUI data encrypted, validated cryptographic modules only

**Data Protection:**
- CUI handling: CUI banners on all dashboards containing CUI, handling instructions
- Data classification: Unclassified, CUI-Basic, CUI-Specified, classified (out of scope)
- Data retention: Per agency records schedule, minimum 3 years after contract close
- Data deletion: Sanitization per NIST 800-88, verification required
- Backup encryption: FIPS-validated encryption, geographically redundant within CONUS

### Network Security
**Network Controls:**
- Network architecture: Agency's TIC (Trusted Internet Connection) only
- IP whitelisting: Required - only agency-approved IP ranges
- Firewall rules: Deny all, explicit allow per FISMA system boundary
- FedRAMP boundary: Separate authorization boundary from other systems
- API security: API gateway with mTLS, rate limiting, SIEM integration

### Audit & Compliance
**Audit Requirements:**
- Audit logging scope: All access, all changes, all admin actions (AU-2 events)
- Log retention: 1 year online, 6 years archive (per agency policy)
- Audit trail requirements: Tamper-evident, centralized SIEM, real-time correlation
- User activity monitoring: Continuous monitoring per FedRAMP ConMon
- Compliance reporting: Monthly vulnerability scans, annual 3PAO assessment

**Incident Response:**
- Incident response plan: FedRAMP-compliant IR plan, 1-hour notification to agency
- Breach notification: US-CERT notification within 1 hour of confirmed breach
- Recovery time objective: 4 hours for critical systems
- Recovery point objective: 1 hour maximum data loss

Please provide:
1. FedRAMP Moderate control mapping for dashboard access controls
2. CUI handling requirements for dashboard display and export
3. CAC/PIV authentication integration architecture
4. Continuous monitoring (ConMon) dashboard for FedRAMP compliance
5. System Security Plan (SSP) section template for dashboard component
```

**Expected Output:**
- FedRAMP control mapping: AC-2 Account Management, AU-2 Audit Events, SC-13 Cryptographic Protection
- CUI handling: Banners on all CUI dashboards, export restrictions, printing controls
- CAC/PIV integration: SAML with certificate-based authentication, PIN verification
- ConMon dashboard: POA&M status, vulnerability scan results, control assessment status

---

## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Dashboard Technical Implementation](dashboard-technical-implementation.md)** - Complementary approaches and methodologies
- **[Dashboard Data Architecture](dashboard-data-architecture.md)** - Leverage data analysis to drive informed decisions
- **[Dashboard Design Overview](dashboard-design-overview.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Dashboard Security, Governance & Compliance)
2. Use [Dashboard Technical Implementation](dashboard-technical-implementation.md) for deeper analysis
3. Apply [Dashboard Data Architecture](dashboard-data-architecture.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Business Intelligence](../../data-analytics/Business Intelligence/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Security architecture design**: Combine this template with related analytics and strategy frameworks
- **Compliance framework implementation**: Combine this template with related analytics and strategy frameworks
- **Access control configuration**: Combine this template with related analytics and strategy frameworks

## Best Practices

### Authentication & Access Control
1. **Implement SSO** - Single sign-on improves security and user experience
2. **Require MFA for sensitive data** - Especially for remote access
3. **Follow least privilege** - Grant minimum access needed
4. **Use role-based access** - Easier to manage than individual permissions
5. **Review access regularly** - Quarterly reviews to remove unnecessary access

### Data Security
6. **Encrypt everything** - Data at rest and in transit
7. **Use strong encryption** - AES-256 for data at rest, TLS 1.2+ for transit
8. **Manage keys properly** - Use dedicated key management service
9. **Implement data masking** - Protect PII/PHI even from authorized users
10. **Apply row-level security** - Users see only their data

### Compliance
11. **Document everything** - Compliance requires documentation
12. **Map controls to requirements** - Show how you meet each regulation
13. **Automate compliance reporting** - Reduce manual effort and errors
14. **Conduct regular assessments** - Don't wait for audits
15. **Train users on compliance** - Security is everyone's responsibility

### Audit & Monitoring
16. **Log all access to sensitive data** - Who accessed what and when
17. **Monitor for anomalies** - Unusual access patterns indicate issues
18. **Retain logs appropriately** - Meet regulatory requirements
19. **Protect audit logs** - Prevent tampering
20. **Regular log review** - Don't just collect, analyze

---

## Role-Based Access Control Examples

### Example: Financial Services Dashboard

| Role | Revenue | Profit | Customer Data | Admin Functions | Row-Level Filter |
|------|---------|--------|---------------|-----------------|------------------|
| CEO | Full | Full | Full (masked PII) | No | All regions |
| CFO | Full | Full | Aggregated only | No | All regions |
| Regional VP | Read | Read | Regional only (masked) | No | Own region |
| Analyst | Read | No | Aggregated only | No | Own region |
| Admin | No | No | No | Full | N/A |

### Example: Healthcare Dashboard

| Role | Patient Data | Diagnosis | Financial | Clinical Notes | Row-Level Filter |
|------|--------------|-----------|-----------|----------------|------------------|
| Physician | Full | Full | No | Full | Own patients |
| Nurse | Limited | Read | No | Read | Own department |
| Billing | Demographics (masked) | Codes only | Full | No | Own location |
| Executive | Aggregated only | Statistics | Aggregated | No | All locations |
| Privacy Officer | Full (audit) | Full (audit) | No | Full (audit) | All |

---

## Compliance Requirements Checklist

### GDPR Compliance

- [ ] Lawful basis for processing documented
- [ ] Data subject consent obtained and tracked
- [ ] Privacy notice provided and accessible
- [ ] Data subject rights implemented (Access, Rectification, Erasure, Portability)
- [ ] Data Protection Impact Assessment (DPIA) completed
- [ ] Data Processing Agreement (DPA) with vendors
- [ ] Cross-border data transfer mechanisms in place
- [ ] Breach notification process (<72 hours)
- [ ] Data retention policy defined and enforced
- [ ] Privacy by design implemented

### HIPAA Compliance

- [ ] Privacy Rule compliance (minimum necessary)
- [ ] Security Rule administrative safeguards
- [ ] Security Rule physical safeguards
- [ ] Security Rule technical safeguards
- [ ] Encryption implemented (at rest and in transit)
- [ ] Access controls and audit trails
- [ ] Business Associate Agreements (BAAs) signed
- [ ] Breach notification process (<60 days)
- [ ] Security risk assessment completed
- [ ] Workforce training completed

### SOX Compliance (Financial Reporting)

- [ ] Access controls for financial data
- [ ] Segregation of duties
- [ ] Change management process
- [ ] Audit trail for all changes
- [ ] Data integrity controls
- [ ] IT general controls (ITGC)
- [ ] User access reviews
- [ ] SOC 2 reports from vendors
- [ ] Documentation of controls
- [ ] Annual control testing

---

## Common Security Pitfalls

- Overly permissive access (too many admins)
- No row-level security (users see all data)
- Weak or missing data masking
- Insufficient audit logging
- No regular access reviews
- Poor password policies
- Missing MFA for remote access
- Unencrypted backups
- No incident response plan
- Inadequate user training

---

## Security Monitoring Metrics

| Metric | Target | Alert Threshold | Action |
|--------|--------|-----------------|--------|
| Failed login attempts | <1% of logins | >5 failures in 10 min | Lock account |
| Unusual access patterns | 0 | Access outside normal hours/location | Alert security team |
| Privileged access usage | Logged | Any admin action | Review weekly |
| Data export volume | Baseline + 20% | 2x baseline | Investigate |
| API call rate | Normal pattern | 5x normal | Rate limit/investigate |
| Concurrent sessions | 1 per user | >1 session | Terminate oldest |

---

## Variables Quick Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `[ORG_TYPE]` | Organization type | "Healthcare provider" |
| `[REGULATIONS]` | Applicable regulations | "HIPAA, state privacy laws" |
| `[DATA_SENSITIVITY]` | Data sensitivity level | "Highly confidential (PHI)" |
| `[AUTH_METHOD]` | Authentication approach | "SSO with MFA" |
| `[ACCESS_MODEL]` | Access control type | "RBAC with row-level security" |
| `[ENCRYPTION_AT_REST]` | Encryption method | "AES-256" |
| `[AUDIT_SCOPE]` | What to audit | "All PHI access, changes, admin" |
| `[COMPLIANCE_REQUIREMENTS]` | Regulations to meet | "HIPAA Privacy, Security Rules" |
| `[RTO]` | Recovery time | "4 hours" |
| `[RPO]` | Recovery point | "1 hour max data loss" |
