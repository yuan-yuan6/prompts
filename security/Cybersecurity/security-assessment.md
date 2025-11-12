---
title: Security Assessment Template
category: security/Cybersecurity
tags:
- ai-ml
- design
- research
- security
- strategy
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
last_updated: 2025-11-09
industries:
- government
- retail
- technology
---

# Security Assessment Template

## Purpose
Comprehensive security assessment including vulnerability scanning, penetration testing, security audits, risk analysis, and remediation planning for enterprise systems and applications.

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

| Variable | Description | Example |
|----------|-------------|----------|
| `[ASSESSMENT_NAME]` | Specify the assessment name | "John Smith" |
| `[ASSESSMENT_TYPE]` | Specify the assessment type | "Standard" |
| `[ASSESSMENT_SCOPE]` | Specify the assessment scope | "[specify value]" |
| `[TARGET_SYSTEMS]` | Specify the target systems | "[specify value]" |
| `[ASSESSMENT_METHODOLOGY]` | Specify the assessment methodology | "[specify value]" |
| `[ASSESSMENT_TIMELINE]` | Specify the assessment timeline | "6 months" |
| `[ASSESSMENT_TEAM]` | Specify the assessment team | "[specify value]" |
| `[STAKEHOLDERS]` | Specify the stakeholders | "[specify value]" |
| `[BUSINESS_CONTEXT]` | Specify the business context | "[specify value]" |
| `[COMPLIANCE_REQUIREMENTS]` | Specify the compliance requirements | "[specify value]" |
| `[ASSET_IDENTIFICATION]` | Specify the asset identification | "[specify value]" |
| `[THREAT_ACTORS]` | Specify the threat actors | "[specify value]" |
| `[ATTACK_VECTORS]` | Specify the attack vectors | "[specify value]" |
| `[THREAT_SCENARIOS]` | Specify the threat scenarios | "[specify value]" |
| `[IMPACT_ANALYSIS]` | Specify the impact analysis | "[specify value]" |
| `[LIKELIHOOD_ASSESSMENT]` | Specify the likelihood assessment | "[specify value]" |
| `[RISK_RATING]` | Specify the risk rating | "[specify value]" |
| `[THREAT_INTELLIGENCE]` | Specify the threat intelligence | "[specify value]" |
| `[ATTACK_SURFACE]` | Specify the attack surface | "[specify value]" |
| `[TRUST_BOUNDARIES]` | Specify the trust boundaries | "[specify value]" |
| `[SCANNING_TOOLS]` | Specify the scanning tools | "[specify value]" |
| `[SCANNING_SCOPE]` | Specify the scanning scope | "[specify value]" |
| `[VULNERABILITY_CATEGORIES]` | Specify the vulnerability categories | "[specify value]" |
| `[CVSS_SCORING]` | Specify the cvss scoring | "[specify value]" |
| `[FALSE_POSITIVE_ANALYSIS]` | Specify the false positive analysis | "[specify value]" |
| `[VULNERABILITY_PRIORITIZATION]` | Specify the vulnerability prioritization | "[specify value]" |
| `[REMEDIATION_TIMELINE]` | Specify the remediation timeline | "6 months" |
| `[COMPENSATING_CONTROLS]` | Specify the compensating controls | "[specify value]" |
| `[VULNERABILITY_TRACKING]` | Specify the vulnerability tracking | "[specify value]" |
| `[VULNERABILITY_REPORTING]` | Specify the vulnerability reporting | "[specify value]" |
| `[TESTING_METHODOLOGY]` | Specify the testing methodology | "[specify value]" |
| `[PENETRATION_SCOPE]` | Specify the penetration scope | "[specify value]" |
| `[RULES_OF_ENGAGEMENT]` | Specify the rules of engagement | "[specify value]" |
| `[PENETRATION_TOOLS]` | Specify the penetration tools | "[specify value]" |
| `[ATTACK_SCENARIOS]` | Specify the attack scenarios | "[specify value]" |
| `[EXPLOITATION_TECHNIQUES]` | Specify the exploitation techniques | "[specify value]" |
| `[PRIVILEGE_ESCALATION]` | Specify the privilege escalation | "[specify value]" |
| `[LATERAL_MOVEMENT]` | Specify the lateral movement | "[specify value]" |
| `[DATA_EXFILTRATION]` | Specify the data exfiltration | "[specify value]" |
| `[PERSISTENCE_METHODS]` | Specify the persistence methods | "[specify value]" |
| `[CONTROL_FRAMEWORK]` | Specify the control framework | "[specify value]" |
| `[ADMINISTRATIVE_CONTROLS]` | Specify the administrative controls | "[specify value]" |
| `[TECHNICAL_CONTROLS]` | Specify the technical controls | "[specify value]" |
| `[PHYSICAL_CONTROLS]` | Specify the physical controls | "[specify value]" |
| `[PREVENTIVE_CONTROLS]` | Specify the preventive controls | "[specify value]" |
| `[DETECTIVE_CONTROLS]` | Specify the detective controls | "[specify value]" |
| `[CORRECTIVE_CONTROLS]` | Specify the corrective controls | "[specify value]" |
| `[CONTROL_EFFECTIVENESS]` | Specify the control effectiveness | "[specify value]" |
| `[CONTROL_GAPS]` | Specify the control gaps | "[specify value]" |
| `[CONTROL_RECOMMENDATIONS]` | Specify the control recommendations | "[specify value]" |

## Best Practices

1. **Define clear scope and rules of engagement**
2. **Use multiple assessment methodologies and tools**
3. **Prioritize findings based on business impact**
4. **Provide actionable remediation guidance**
5. **Track remediation progress and validate fixes**