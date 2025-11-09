---
title: Security Assessment Template
category: technology/Cybersecurity
tags: [data-science, design, machine-learning, research, security, strategy, technology, template]
use_cases:
  - Implementing comprehensive security assessment including vulnerability scanning, penetration ...
  - Project planning and execution
  - Strategy development
related_templates:
  - cloud-architecture-framework.md
  - site-reliability-engineering.md
  - cloud-migration-strategy.md
last_updated: 2025-11-09
---

# Security Assessment Template

## Purpose
Comprehensive security assessment including vulnerability scanning, penetration testing, security audits, risk analysis, and remediation planning for enterprise systems and applications.

## Template Structure

### Assessment Overview
- **Assessment Name**: {assessment_name}
- **Assessment Type**: {assessment_type}
- **Scope**: {assessment_scope}
- **Target Systems**: {target_systems}
- **Assessment Methodology**: {assessment_methodology}
- **Timeline**: {assessment_timeline}
- **Team**: {assessment_team}
- **Stakeholders**: {stakeholders}
- **Business Context**: {business_context}
- **Compliance Requirements**: {compliance_requirements}

### Threat Modeling
- **Asset Identification**: {asset_identification}
- **Threat Actors**: {threat_actors}
- **Attack Vectors**: {attack_vectors}
- **Threat Scenarios**: {threat_scenarios}
- **Impact Analysis**: {impact_analysis}
- **Likelihood Assessment**: {likelihood_assessment}
- **Risk Rating**: {risk_rating}
- **Threat Intelligence**: {threat_intelligence}
- **Attack Surface**: {attack_surface}
- **Trust Boundaries**: {trust_boundaries}

### Vulnerability Assessment
- **Scanning Tools**: {scanning_tools}
- **Scanning Scope**: {scanning_scope}
- **Vulnerability Categories**: {vulnerability_categories}
- **CVSS Scoring**: {cvss_scoring}
- **False Positive Analysis**: {false_positive_analysis}
- **Vulnerability Prioritization**: {vulnerability_prioritization}
- **Remediation Timeline**: {remediation_timeline}
- **Compensating Controls**: {compensating_controls}
- **Vulnerability Tracking**: {vulnerability_tracking}
- **Reporting Format**: {vulnerability_reporting}

### Penetration Testing
- **Testing Methodology**: {testing_methodology}
- **Testing Scope**: {penetration_scope}
- **Rules of Engagement**: {rules_of_engagement}
- **Testing Tools**: {penetration_tools}
- **Attack Scenarios**: {attack_scenarios}
- **Exploitation Techniques**: {exploitation_techniques}
- **Privilege Escalation**: {privilege_escalation}
- **Lateral Movement**: {lateral_movement}
- **Data Exfiltration**: {data_exfiltration}
- **Persistence Methods**: {persistence_methods}

### Security Controls Review
- **Control Framework**: {control_framework}
- **Administrative Controls**: {administrative_controls}
- **Technical Controls**: {technical_controls}
- **Physical Controls**: {physical_controls}
- **Preventive Controls**: {preventive_controls}
- **Detective Controls**: {detective_controls}
- **Corrective Controls**: {corrective_controls}
- **Control Effectiveness**: {control_effectiveness}
- **Control Gaps**: {control_gaps}
- **Control Recommendations**: {control_recommendations}

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
| `{assessment_name}` | Specify the assessment name | "John Smith" |
| `{assessment_type}` | Specify the assessment type | "Standard" |
| `{assessment_scope}` | Specify the assessment scope | "[specify value]" |
| `{target_systems}` | Specify the target systems | "[specify value]" |
| `{assessment_methodology}` | Specify the assessment methodology | "[specify value]" |
| `{assessment_timeline}` | Specify the assessment timeline | "6 months" |
| `{assessment_team}` | Specify the assessment team | "[specify value]" |
| `{stakeholders}` | Specify the stakeholders | "[specify value]" |
| `{business_context}` | Specify the business context | "[specify value]" |
| `{compliance_requirements}` | Specify the compliance requirements | "[specify value]" |
| `{asset_identification}` | Specify the asset identification | "[specify value]" |
| `{threat_actors}` | Specify the threat actors | "[specify value]" |
| `{attack_vectors}` | Specify the attack vectors | "[specify value]" |
| `{threat_scenarios}` | Specify the threat scenarios | "[specify value]" |
| `{impact_analysis}` | Specify the impact analysis | "[specify value]" |
| `{likelihood_assessment}` | Specify the likelihood assessment | "[specify value]" |
| `{risk_rating}` | Specify the risk rating | "[specify value]" |
| `{threat_intelligence}` | Specify the threat intelligence | "[specify value]" |
| `{attack_surface}` | Specify the attack surface | "[specify value]" |
| `{trust_boundaries}` | Specify the trust boundaries | "[specify value]" |
| `{scanning_tools}` | Specify the scanning tools | "[specify value]" |
| `{scanning_scope}` | Specify the scanning scope | "[specify value]" |
| `{vulnerability_categories}` | Specify the vulnerability categories | "[specify value]" |
| `{cvss_scoring}` | Specify the cvss scoring | "[specify value]" |
| `{false_positive_analysis}` | Specify the false positive analysis | "[specify value]" |
| `{vulnerability_prioritization}` | Specify the vulnerability prioritization | "[specify value]" |
| `{remediation_timeline}` | Specify the remediation timeline | "6 months" |
| `{compensating_controls}` | Specify the compensating controls | "[specify value]" |
| `{vulnerability_tracking}` | Specify the vulnerability tracking | "[specify value]" |
| `{vulnerability_reporting}` | Specify the vulnerability reporting | "[specify value]" |
| `{testing_methodology}` | Specify the testing methodology | "[specify value]" |
| `{penetration_scope}` | Specify the penetration scope | "[specify value]" |
| `{rules_of_engagement}` | Specify the rules of engagement | "[specify value]" |
| `{penetration_tools}` | Specify the penetration tools | "[specify value]" |
| `{attack_scenarios}` | Specify the attack scenarios | "[specify value]" |
| `{exploitation_techniques}` | Specify the exploitation techniques | "[specify value]" |
| `{privilege_escalation}` | Specify the privilege escalation | "[specify value]" |
| `{lateral_movement}` | Specify the lateral movement | "[specify value]" |
| `{data_exfiltration}` | Specify the data exfiltration | "[specify value]" |
| `{persistence_methods}` | Specify the persistence methods | "[specify value]" |
| `{control_framework}` | Specify the control framework | "[specify value]" |
| `{administrative_controls}` | Specify the administrative controls | "[specify value]" |
| `{technical_controls}` | Specify the technical controls | "[specify value]" |
| `{physical_controls}` | Specify the physical controls | "[specify value]" |
| `{preventive_controls}` | Specify the preventive controls | "[specify value]" |
| `{detective_controls}` | Specify the detective controls | "[specify value]" |
| `{corrective_controls}` | Specify the corrective controls | "[specify value]" |
| `{control_effectiveness}` | Specify the control effectiveness | "[specify value]" |
| `{control_gaps}` | Specify the control gaps | "[specify value]" |
| `{control_recommendations}` | Specify the control recommendations | "[specify value]" |



## Best Practices

1. **Define clear scope and rules of engagement**
2. **Use multiple assessment methodologies and tools**
3. **Prioritize findings based on business impact**
4. **Provide actionable remediation guidance**
5. **Track remediation progress and validate fixes**