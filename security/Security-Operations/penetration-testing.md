---
category: security/Security-Operations
last_updated: 2025-11-11
title: Penetration Testing Framework
tags:
- security
- testing
- assessment
use_cases:
- Planning and executing penetration tests
- Internal and external security assessments
- Red team exercises and attack simulations
- Vulnerability validation and exploitation testing
related_templates:
- security/Cybersecurity/security-assessment.md
- security/Application-Security/secure-code-review.md
- security/Security-Operations/vulnerability-management.md
industries:
- finance
- government
- healthcare
- technology
---

# Penetration Testing Framework

## Purpose
Comprehensive framework for planning, executing, and reporting penetration tests including scope definition, methodology selection, testing execution, vulnerability exploitation, and remediation guidance.

## Quick Start

**Need to conduct a penetration test?** Use this minimal example:

### Minimal Example
```
Execute external penetration test for our e-commerce web application (www.example.com) including infrastructure, web application, APIs, and authentication mechanisms. Test for OWASP Top 10, injection attacks, authentication bypass, and privilege escalation. Provide exploit proof-of-concepts and remediation guidance.
```

### When to Use This
- Quarterly/annual security assessments
- Pre-production security validation
- Compliance requirements (PCI-DSS, HIPAA)
- Post-incident security validation
- Red team exercises

### Basic 3-Step Workflow
1. **Planning & Reconnaissance** - Define scope, gather intelligence (2-4 hours)
2. **Exploitation & Testing** - Identify and exploit vulnerabilities (8-40 hours)
3. **Reporting & Remediation** - Document findings, provide fixes (4-8 hours)

**Time to complete**: 1-2 weeks for comprehensive assessment

---

## Template

```markdown
I need to plan and execute a penetration test. Please provide comprehensive penetration testing guidance and methodology.

## ENGAGEMENT CONTEXT

### Scope Definition
- Test type: [EXTERNAL_INTERNAL_WEB_APP_MOBILE_API_CLOUD_WIRELESS]
- Target systems: [IP_RANGES_DOMAINS_APPLICATIONS]
- Testing window: [DATES_AND_TIMES]
- Authorized testers: [TEAM_MEMBERS]
- Out of scope: [EXCLUDED_SYSTEMS]
- Rules of engagement: [RESTRICTIONS_CONSTRAINTS]

### Objectives
- Primary goals: [FIND_VULNERABILITIES_TEST_CONTROLS_SIMULATE_ATTACK]
- Threat scenarios: [EXTERNAL_ATTACKER_INSIDER_THREAT_ADVANCED_PERSISTENT_THREAT]
- Success criteria: [SPECIFIC_TARGETS_OR_GOALS]
- Compliance requirements: [PCI_DSS_HIPAA_ISO27001_SOC2]

### Environment Details
- Infrastructure: [ON_PREM_CLOUD_HYBRID]
- Applications: [WEB_MOBILE_API_DESKTOP]
- Network architecture: [PERIMETER_SEGMENTED_ZERO_TRUST]
- Security controls: [WAF_IDS_IPS_EDR_SIEM]
- Authentication: [SSO_MFA_LDAP_OAUTH]

## PENETRATION TESTING METHODOLOGY

### Phase 1: Planning & Reconnaissance
**Passive Information Gathering:**
- OSINT collection (domain, employees, technologies)
- DNS enumeration and subdomain discovery
- Social media reconnaissance
- Public database searches
- Leaked credential searches

**Active Information Gathering:**
- Port scanning and service detection
- OS fingerprinting
- Web technology identification
- SSL/TLS analysis
- Email server enumeration

### Phase 2: Vulnerability Discovery
**Automated Scanning:**
- Nessus, Qualys, OpenVAS vulnerability scans
- Web application scanning (Burp Suite, OWASP ZAP)
- Database vulnerability scanning
- Configuration assessment tools

**Manual Testing:**
- Authentication mechanism testing
- Session management analysis
- Input validation testing
- Business logic flaws
- Access control testing
- Cryptographic implementation review

### Phase 3: Exploitation
**Exploitation Techniques:**
- SQL injection attacks
- Cross-site scripting (XSS)
- Remote code execution (RCE)
- Local file inclusion (LFI)
- Authentication bypass
- Privilege escalation
- Command injection
- Server-side request forgery (SSRF)

**Tools:**
- Metasploit Framework
- SQLmap
- Burp Suite Professional
- Custom exploit scripts
- Social engineering toolkit

### Phase 4: Post-Exploitation
**Objectives:**
- Maintain access and persistence
- Privilege escalation to admin/root
- Lateral movement testing
- Data exfiltration simulation
- Domain compromise (if applicable)
- Pivoting to other systems

### Phase 5: Reporting
**Report Sections:**
1. Executive summary
2. Methodology and scope
3. Findings by severity
4. Technical details and proof-of-concepts
5. Risk ratings (CVSS scores)
6. Remediation recommendations
7. Strategic security improvements

## TESTING AREAS

### Network Penetration Testing
- External network testing
- Internal network testing
- Wireless network testing
- Firewall and IDS/IPS bypass
- Man-in-the-middle attacks
- Network segmentation validation

### Web Application Testing
- OWASP Top 10 vulnerabilities
- Authentication and session management
- Input validation and injection
- Business logic flaws
- API security testing
- Client-side security

### Mobile Application Testing
- Android and iOS testing
- Mobile API testing
- Insecure data storage
- Weak cryptography
- Insecure communication
- Code tampering

### Cloud Penetration Testing
- AWS, Azure, GCP security
- IAM misconfigurations
- Storage bucket security
- Serverless function testing
- Container security
- API gateway testing

### Social Engineering
- Phishing campaigns
- Vishing (voice phishing)
- Physical security testing
- Tailgating and unauthorized access
- USB drop testing

## VULNERABILITY SEVERITY RATING

**Critical:**
- Remote code execution
- Authentication bypass
- SQL injection with data access
- Complete system compromise

**High:**
- Privilege escalation
- Stored XSS
- Sensitive data exposure
- Insecure deserialization

**Medium:**
- Reflected XSS
- CSRF on important functions
- Information disclosure
- Security misconfiguration

**Low:**
- Information disclosure (minimal impact)
- Missing security headers
- Self-XSS
- Open redirects

## COMPLIANCE-SPECIFIC TESTING

### PCI-DSS Testing
- Quarterly external scans
- Annual penetration testing
- Segmentation testing
- Wireless testing if applicable

### HIPAA Testing
- Technical safeguards validation
- Access control testing
- Audit control testing
- Transmission security

### SOC 2 Testing
- Security control validation
- Access control testing
- Monitoring and logging
- Change management testing

## REMEDIATION GUIDANCE

For each finding provide:
- Vulnerability description
- Business impact
- Technical details
- Proof-of-concept
- CVSS score
- Remediation steps
- Code examples (where applicable)
- Testing validation steps
- References (CWE, OWASP, CVE)

## OUTPUT REQUIREMENTS

Provide:
1. **Executive Report** - High-level summary for management
2. **Technical Report** - Detailed findings for IT/security teams
3. **Remediation Matrix** - Prioritized action items
4. **Proof-of-Concepts** - Exploits and screenshots
5. **Retest Report** - Validation of fixes

## Best Practices

- Get written authorization before testing
- Follow rules of engagement strictly
- Document everything
- Validate exploits in controlled environment
- Handle sensitive data with care
- Provide actionable remediation guidance
- Offer retest to validate fixes
```

---

## Related Resources

- [PTES: Penetration Testing Execution Standard](http://www.pentest-standard.org/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- security/Cybersecurity/security-assessment.md
- security/Security-Operations/vulnerability-management.md
