---
title: Security Assessment Template
category: security
tags:
- security
- security-assessment
- vulnerability-scanning
- risk-analysis
use_cases:
- Creating comprehensive security assessment including vulnerability scanning, penetration
  testing, security audits, risk analysis, and remediation planning for enterprise
  systems and applications.
- Project planning and execution
- Strategy development
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
last_updated: 2025-11-22
industries:
- government
- retail
- technology
type: template
difficulty: intermediate
slug: security-assessment
---

# Security Assessment Template

## Purpose
Comprehensive security assessment including vulnerability scanning, penetration testing, security audits, risk analysis, and remediation planning for enterprise systems and applications.

## Quick Security Assessment Prompt
Conduct security assessment for [system/application] covering [scope: infrastructure/web app/API/cloud]. Methodology: [NIST/OWASP/CIS]. Perform: asset inventory, threat modeling, vulnerability scanning (Nessus/Qualys), penetration testing (OWASP Top 10), control review. Prioritize findings by CVSS + business impact. Deliver: executive summary, detailed findings, and remediation roadmap with timeline.

## Quick Start

**Basic Usage:**
```
Conduct comprehensive security assessment for [SYSTEM_NAME] covering [ASSESSMENT_SCOPE] using [METHODOLOGY] framework.
```

**Example:**
```
Conduct comprehensive security assessment for EcommercePlatform web application covering OWASP Top 10 vulnerabilities using NIST framework methodology.
```

**Key Steps:**
1. Define assessment scope, timeline, and target systems
2. Identify assets, threat actors, and attack vectors through threat modeling
3. Perform vulnerability scanning with tools like Burp Suite, OWASP ZAP, Nessus
4. Conduct penetration testing following defined rules of engagement
5. Review security controls across administrative, technical, and physical domains
6. Prioritize findings by CVSS scoring and business impact
7. Create remediation roadmap with timeline and compensating controls

## Template Structure

### Assessment Overview
- **Assessment Name**: [ASSESSMENT_NAME]
- **Assessment Type**: [ASSESSMENT_TYPE]
- **Scope**: [ASSESSMENT_SCOPE]
- **Target Systems**: [TARGET_SYSTEMS]
- **Assessment Methodology**: [ASSESSMENT_METHODOLOGY]
- **Timeline**: [ASSESSMENT_TIMELINE]
- **Team**: [ASSESSMENT_TEAM]
- **Stakeholders**: [STAKEHOLDERS]
- **Business Context**: [BUSINESS_CONTEXT]
- **Compliance Requirements**: [COMPLIANCE_REQUIREMENTS]

### Threat Modeling
- **Asset Identification**: [ASSET_IDENTIFICATION]
- **Threat Actors**: [THREAT_ACTORS]
- **Attack Vectors**: [ATTACK_VECTORS]
- **Threat Scenarios**: [THREAT_SCENARIOS]
- **Impact Analysis**: [IMPACT_ANALYSIS]
- **Likelihood Assessment**: [LIKELIHOOD_ASSESSMENT]
- **Risk Rating**: [RISK_RATING]
- **Threat Intelligence**: [THREAT_INTELLIGENCE]
- **Attack Surface**: [ATTACK_SURFACE]
- **Trust Boundaries**: [TRUST_BOUNDARIES]

### Vulnerability Assessment
- **Scanning Tools**: [SCANNING_TOOLS]
- **Scanning Scope**: [SCANNING_SCOPE]
- **Vulnerability Categories**: [VULNERABILITY_CATEGORIES]
- **CVSS Scoring**: [CVSS_SCORING]
- **False Positive Analysis**: [FALSE_POSITIVE_ANALYSIS]
- **Vulnerability Prioritization**: [VULNERABILITY_PRIORITIZATION]
- **Remediation Timeline**: [REMEDIATION_TIMELINE]
- **Compensating Controls**: [COMPENSATING_CONTROLS]
- **Vulnerability Tracking**: [VULNERABILITY_TRACKING]
- **Reporting Format**: [VULNERABILITY_REPORTING]

### Penetration Testing
- **Testing Methodology**: [TESTING_METHODOLOGY]
- **Testing Scope**: [PENETRATION_SCOPE]
- **Rules of Engagement**: [RULES_OF_ENGAGEMENT]
- **Testing Tools**: [PENETRATION_TOOLS]
- **Attack Scenarios**: [ATTACK_SCENARIOS]
- **Exploitation Techniques**: [EXPLOITATION_TECHNIQUES]
- **Privilege Escalation**: [PRIVILEGE_ESCALATION]
- **Lateral Movement**: [LATERAL_MOVEMENT]
- **Data Exfiltration**: [DATA_EXFILTRATION]
- **Persistence Methods**: [PERSISTENCE_METHODS]

### Security Controls Review
- **Control Framework**: [CONTROL_FRAMEWORK]
- **Administrative Controls**: [ADMINISTRATIVE_CONTROLS]
- **Technical Controls**: [TECHNICAL_CONTROLS]
- **Physical Controls**: [PHYSICAL_CONTROLS]
- **Preventive Controls**: [PREVENTIVE_CONTROLS]
- **Detective Controls**: [DETECTIVE_CONTROLS]
- **Corrective Controls**: [CORRECTIVE_CONTROLS]
- **Control Effectiveness**: [CONTROL_EFFECTIVENESS]
- **Control Gaps**: [CONTROL_GAPS]
- **Control Recommendations**: [CONTROL_RECOMMENDATIONS]

Please provide detailed assessment procedures, testing methodologies, risk analysis frameworks, and remediation roadmaps.

## Usage Examples

### Web Application Security Assessment
```
Conduct comprehensive security assessment for EcommercePlatform web application covering OWASP Top 10 vulnerabilities using NIST framework methodology.

Assessment Overview:
- Web application security assessment type for customer-facing e-commerce platform
- Cover authentication, authorization, data validation assessment scope
- Target React frontend, Node.js backend, PostgreSQL database systems
- Apply OWASP WSTG assessment methodology over 4-week timeline
- Ensure PCI DSS, GDPR compliance requirements

Vulnerability Assessment:
- Use Burp Suite, OWASP ZAP, Nessus scanning tools
- Scan all public endpoints, admin interfaces scanning scope
- Focus on injection, authentication, access control vulnerability categories
- Apply CVSS v3.1 scoring with business impact analysis
- Prioritize by exploitability and business impact vulnerability prioritization

### Penetration Testing
- Apply OWASP WSTG testing methodology
- Test all user roles and privilege levels penetration scope
- Define authorized testing scope rules of engagement
- Use Metasploit, custom scripts, manual testing tools
- Test SQL injection, XSS, broken authentication attack scenarios
```

## Variables

### Assessment Overview

| Variable | Description | Example |
|----------|-------------|----------|
| `[ASSESSMENT_NAME]` | Descriptive name for the assessment | "Q4 2025 Web Application Security Assessment", "Annual PCI-DSS Compliance Audit" |
| `[ASSESSMENT_TYPE]` | Category of security assessment | "Vulnerability Assessment", "Penetration Test", "Red Team", "Compliance Audit" |
| `[ASSESSMENT_SCOPE]` | What is included in the assessment | "All customer-facing web applications", "AWS infrastructure + on-prem network" |
| `[TARGET_SYSTEMS]` | Specific systems being assessed | "app.example.com, api.example.com, 10.0.0.0/24 internal network" |
| `[ASSESSMENT_METHODOLOGY]` | Framework guiding the assessment | "OWASP Testing Guide v4.2", "PTES", "NIST SP 800-115", "OSSTMM" |
| `[ASSESSMENT_TIMELINE]` | Duration and schedule | "2 weeks (Jan 15-29)", "5 business days active testing" |
| `[ASSESSMENT_TEAM]` | Personnel conducting assessment | "2 senior pentesters, 1 web app specialist, project manager" |
| `[STAKEHOLDERS]` | Key stakeholders and decision makers | "CISO, VP Engineering, Compliance Officer, Legal (for breach scenarios)" |
| `[COMPLIANCE_REQUIREMENTS]` | Regulatory drivers | "PCI-DSS 4.0 Req 11.4", "SOC 2 CC6.1", "HIPAA Security Rule" |

### Threat Modeling

| Variable | Description | Example |
|----------|-------------|----------|
| `[ASSET_IDENTIFICATION]` | Critical assets in scope | "Customer PII database, payment processing API, admin portal credentials" |
| `[THREAT_ACTORS]` | Who might attack | "Financially motivated cybercriminals, nation-state APT, disgruntled employees" |
| `[ATTACK_VECTORS]` | How attacks might occur | "Internet-facing apps, phishing emails, supply chain compromise, insider access" |
| `[THREAT_SCENARIOS]` | Specific attack scenarios | "Ransomware via RDP, SQL injection for data theft, credential stuffing" |
| `[RISK_RATING]` | Risk scoring methodology | "CVSS 3.1 for technical, FAIR for business impact quantification" |
| `[ATTACK_SURFACE]` | Exposed entry points | "15 web apps, 3 APIs, VPN endpoint, email gateway, public cloud (AWS)" |
| `[TRUST_BOUNDARIES]` | Security zone transitions | "Internet → DMZ → Internal → PCI zone → Database tier" |

### Vulnerability Assessment

| Variable | Description | Example |
|----------|-------------|----------|
| `[SCANNING_TOOLS]` | Tools used for scanning | "Nessus Professional, Qualys VMDR, Burp Suite Pro, Nuclei" |
| `[SCANNING_SCOPE]` | What gets scanned | "All TCP ports on external hosts, authenticated scans on internal systems" |
| `[VULNERABILITY_CATEGORIES]` | Types of vulnerabilities sought | "OWASP Top 10, CWE/SANS Top 25, CISA Known Exploited Vulnerabilities" |
| `[CVSS_SCORING]` | How vulnerabilities are scored | "CVSS 3.1 base score + environmental adjustments for business context" |
| `[VULNERABILITY_PRIORITIZATION]` | How findings are prioritized | "Critical+exploitable+external = P1, Critical+internal = P2, High = P3" |
| `[REMEDIATION_TIMELINE]` | Expected fix timeline by severity | "Critical: 24-48 hours, High: 7 days, Medium: 30 days, Low: 90 days" |
| `[COMPENSATING_CONTROLS]` | Interim mitigations | "WAF rules, network segmentation, enhanced monitoring until patched" |

### Penetration Testing

| Variable | Description | Example |
|----------|-------------|----------|
| `[TESTING_METHODOLOGY]` | Pentest approach | "Black-box external, gray-box internal with limited credentials" |
| `[PENETRATION_SCOPE]` | What can be tested | "All production systems except database writes, no DoS testing" |
| `[RULES_OF_ENGAGEMENT]` | Engagement boundaries | "No social engineering without approval, stop on confirmed breach, notify within 1hr" |
| `[PENETRATION_TOOLS]` | Tools for active testing | "Metasploit, Cobalt Strike, Impacket, BloodHound, custom exploits" |
| `[EXPLOITATION_TECHNIQUES]` | Attack techniques used | "SQL injection, SSRF, deserialization, Kerberoasting, LLMNR poisoning" |
| `[PRIVILEGE_ESCALATION]` | Escalation paths tested | "Service account abuse, misconfigurations, kernel exploits, AD delegation" |
| `[LATERAL_MOVEMENT]` | Movement techniques | "Pass-the-hash, token impersonation, RDP pivoting, WMI execution" |

### Security Controls Review

| Variable | Description | Example |
|----------|-------------|----------|
| `[CONTROL_FRAMEWORK]` | Control framework used | "NIST CSF", "CIS Controls v8", "ISO 27001 Annex A" |
| `[ADMINISTRATIVE_CONTROLS]` | Policy/process controls | "Security policies, background checks, security awareness training" |
| `[TECHNICAL_CONTROLS]` | Technology controls | "Firewalls, IDS/IPS, encryption, MFA, DLP, SIEM, EDR" |
| `[PHYSICAL_CONTROLS]` | Physical security measures | "Badge access, CCTV, server room locks, visitor logs" |
| `[CONTROL_EFFECTIVENESS]` | How effective controls are | "MFA: 95% adoption, EDR: 100% coverage, Patching: 85% compliant" |
| `[CONTROL_GAPS]` | Identified control weaknesses | "No network segmentation between zones, shared admin accounts" |
| `[CONTROL_RECOMMENDATIONS]` | Recommended improvements | "Implement microsegmentation, deploy PAM solution, enable audit logging" |

## Best Practices

1. **Define clear scope and rules of engagement**
2. **Use multiple assessment methodologies and tools**
3. **Prioritize findings based on business impact**
4. **Provide actionable remediation guidance**
5. **Track remediation progress and validate fixes**