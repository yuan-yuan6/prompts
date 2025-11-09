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

Penetration Testing:
- Apply OWASP WSTG testing methodology
- Test all user roles and privilege levels penetration scope
- Define authorized testing scope rules of engagement
- Use Metasploit, custom scripts, manual testing tools
- Test SQL injection, XSS, broken authentication attack scenarios
```

## Best Practices

1. **Define clear scope and rules of engagement**
2. **Use multiple assessment methodologies and tools**
3. **Prioritize findings based on business impact**
4. **Provide actionable remediation guidance**
5. **Track remediation progress and validate fixes**