---
title: Incident Response Template
category: technology/Cybersecurity
tags: [communication, data-science, design, management, research, security, strategy, technology]
use_cases:
  - Creating comprehensive incident response planning including detection, analysis, containment, eradication, recovery, and lessons learned for effective cybersecurity incident management.

  - Project planning and execution
  - Strategy development
related_templates:
  - cloud-architecture-framework.md
  - site-reliability-engineering.md
  - cloud-migration-strategy.md
last_updated: 2025-11-09
---

# Incident Response Template

## Purpose
Comprehensive incident response planning including detection, analysis, containment, eradication, recovery, and lessons learned for effective cybersecurity incident management.

## Quick Start

**Set Your Foundation (5 minutes):**
1. Define incident types and severity levels: critical, high, medium, low
2. Establish incident response team: commander, security, IT ops, legal, communications
3. Set up incident communication channels and contact lists

**Configure Key Parameters (10 minutes):**
4. Create incident classification matrix based on impact and scope
5. Define escalation paths and authority levels for decision-making
6. Establish evidence collection and chain of custody procedures

**Implement & Deploy (Ongoing):**
7. Deploy SIEM for detection and correlation (Splunk, Elastic, or QRadar)
8. Create incident response playbooks for common scenarios (ransomware, phishing, DDoS)
9. Set up forensic toolkit with memory capture, disk imaging, and analysis tools
10. Conduct tabletop exercises quarterly to test response procedures

**Pro Tips:** Follow NIST SP 800-61 framework, maintain offline incident response kit, document everything during incidents, use MITRE ATT&CK for attack mapping, and conduct post-incident reviews within 72 hours for lessons learned.

## Template Structure

### Incident Overview
- **Incident ID**: [INCIDENT_ID]
- **Incident Type**: [INCIDENT_TYPE]
- **Severity Level**: [SEVERITY_LEVEL]
- **Affected Systems**: [AFFECTED_SYSTEMS]
- **Discovery Method**: [DISCOVERY_METHOD]
- **Discovery Time**: [DISCOVERY_TIME]
- **Reporting Time**: [REPORTING_TIME]
- **Initial Reporter**: [INITIAL_REPORTER]
- **Business Impact**: [BUSINESS_IMPACT]
- **Estimated Loss**: [ESTIMATED_LOSS]

### Response Team
- **Incident Commander**: [INCIDENT_COMMANDER]
- **Security Team**: [SECURITY_TEAM]
- **IT Operations**: [IT_OPERATIONS]
- **Legal Team**: [LEGAL_TEAM]
- **Communications**: [COMMUNICATIONS_TEAM]
- **External Resources**: [EXTERNAL_RESOURCES]
- **Escalation Path**: [ESCALATION_PATH]
- **Contact Information**: [CONTACT_INFORMATION]
- **Roles and Responsibilities**: [ROLES_RESPONSIBILITIES]
- **Authority Levels**: [AUTHORITY_LEVELS]

### Detection and Analysis
- **Detection Sources**: [DETECTION_SOURCES]
- **Alert Correlation**: [ALERT_CORRELATION]
- **Evidence Collection**: [EVIDENCE_COLLECTION]
- **Forensic Analysis**: [FORENSIC_ANALYSIS]
- **IOC Identification**: [IOC_IDENTIFICATION]
- **Attack Timeline**: [ATTACK_TIMELINE]
- **Attribution Analysis**: [ATTRIBUTION_ANALYSIS]
- **Scope Assessment**: [SCOPE_ASSESSMENT]
- **Impact Analysis**: [IMPACT_ANALYSIS]
- **Root Cause Analysis**: [ROOT_CAUSE_ANALYSIS]

### Containment Strategy
- **Short-term Containment**: [SHORT_TERM_CONTAINMENT]
- **Long-term Containment**: [LONG_TERM_CONTAINMENT]
- **System Isolation**: [SYSTEM_ISOLATION]
- **Network Segmentation**: [NETWORK_SEGMENTATION]
- **Access Restrictions**: [ACCESS_RESTRICTIONS]
- **Service Disruption**: [SERVICE_DISRUPTION]
- **Business Continuity**: [BUSINESS_CONTINUITY]
- **Communication Plan**: [CONTAINMENT_COMMUNICATION]
- **Monitoring Enhancement**: [MONITORING_ENHANCEMENT]
- **Evidence Preservation**: [EVIDENCE_PRESERVATION]

### Eradication and Recovery
- **Threat Elimination**: [THREAT_ELIMINATION]
- **System Hardening**: [SYSTEM_HARDENING]
- **Patch Management**: [PATCH_MANAGEMENT]
- **Configuration Changes**: [CONFIGURATION_CHANGES]
- **Recovery Planning**: [RECOVERY_PLANNING]
- **Data Restoration**: [DATA_RESTORATION]
- **Service Restoration**: [SERVICE_RESTORATION]
- **Monitoring Restoration**: [MONITORING_RESTORATION]
- **Validation Testing**: [VALIDATION_TESTING]
- **Return to Operations**: [RETURN_TO_OPERATIONS]

### Communication and Reporting
- **Internal Communications**: [INTERNAL_COMMUNICATIONS]
- **External Communications**: [EXTERNAL_COMMUNICATIONS]
- **Regulatory Reporting**: [REGULATORY_REPORTING]
- **Customer Notifications**: [CUSTOMER_NOTIFICATIONS]
- **Media Relations**: [MEDIA_RELATIONS]
- **Legal Notifications**: [LEGAL_NOTIFICATIONS]
- **Stakeholder Updates**: [STAKEHOLDER_UPDATES]
- **Status Reports**: [STATUS_REPORTS]
- **Final Report**: [FINAL_REPORT]
- **Documentation**: [INCIDENT_DOCUMENTATION]

Please provide detailed response procedures, communication templates, forensic workflows, and recovery plans.

## Usage Examples

### Ransomware Incident Response
```
Execute incident response for CryptoLocker ransomware affecting 500+ workstations with critical severity level using NIST framework.

Incident Overview:
- Ransomware attack incident type with critical severity level
- Affect Windows workstations, file servers affected systems
- Discover via EDR alerts discovery method at 2AM discovery time
- Impact payroll, customer service business functions
- Estimate $500K operational impact estimated loss

Detection and Analysis:
- Correlate EDR, SIEM, network monitoring detection sources
- Collect memory dumps, disk images, network logs evidence collection
- Analyze malware samples, encryption methods forensic analysis
- Identify C2 domains, file extensions IOC identification
- Map attack progression over 48hrs attack timeline

### Containment Strategy
- Isolate infected systems system isolation within 30 minutes
- Segment network to prevent spread network segmentation
- Disable file sharing, remote access access restrictions
- Maintain critical services with backup systems business continuity
- Deploy additional monitoring on network boundaries monitoring enhancement

### Communication and Reporting
- Brief executive team, board internal communications
- Notify cyber insurance, legal counsel external communications
- File FBI IC3, state AG regulatory reporting
- Send customer data breach notifications customer notifications
- Prepare holding statements for media inquiries media relations
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[INCIDENT_ID]` | Specify the incident id | "[specify value]" |
| `[INCIDENT_TYPE]` | Specify the incident type | "Standard" |
| `[SEVERITY_LEVEL]` | Specify the severity level | "[specify value]" |
| `[AFFECTED_SYSTEMS]` | Specify the affected systems | "[specify value]" |
| `[DISCOVERY_METHOD]` | Specify the discovery method | "[specify value]" |
| `[DISCOVERY_TIME]` | Specify the discovery time | "[specify value]" |
| `[REPORTING_TIME]` | Specify the reporting time | "[specify value]" |
| `[INITIAL_REPORTER]` | Specify the initial reporter | "[specify value]" |
| `[BUSINESS_IMPACT]` | Specify the business impact | "[specify value]" |
| `[ESTIMATED_LOSS]` | Specify the estimated loss | "[specify value]" |
| `[INCIDENT_COMMANDER]` | Specify the incident commander | "[specify value]" |
| `[SECURITY_TEAM]` | Specify the security team | "[specify value]" |
| `[IT_OPERATIONS]` | Specify the it operations | "[specify value]" |
| `[LEGAL_TEAM]` | Specify the legal team | "[specify value]" |
| `[COMMUNICATIONS_TEAM]` | Specify the communications team | "[specify value]" |
| `[EXTERNAL_RESOURCES]` | Specify the external resources | "[specify value]" |
| `[ESCALATION_PATH]` | Specify the escalation path | "[specify value]" |
| `[CONTACT_INFORMATION]` | Specify the contact information | "[specify value]" |
| `[ROLES_RESPONSIBILITIES]` | Specify the roles responsibilities | "[specify value]" |
| `[AUTHORITY_LEVELS]` | Specify the authority levels | "[specify value]" |
| `[DETECTION_SOURCES]` | Specify the detection sources | "[specify value]" |
| `[ALERT_CORRELATION]` | Specify the alert correlation | "[specify value]" |
| `[EVIDENCE_COLLECTION]` | Specify the evidence collection | "[specify value]" |
| `[FORENSIC_ANALYSIS]` | Specify the forensic analysis | "[specify value]" |
| `[IOC_IDENTIFICATION]` | Specify the ioc identification | "[specify value]" |
| `[ATTACK_TIMELINE]` | Specify the attack timeline | "6 months" |
| `[ATTRIBUTION_ANALYSIS]` | Specify the attribution analysis | "[specify value]" |
| `[SCOPE_ASSESSMENT]` | Specify the scope assessment | "[specify value]" |
| `[IMPACT_ANALYSIS]` | Specify the impact analysis | "[specify value]" |
| `[ROOT_CAUSE_ANALYSIS]` | Specify the root cause analysis | "[specify value]" |
| `[SHORT_TERM_CONTAINMENT]` | Specify the short term containment | "[specify value]" |
| `[LONG_TERM_CONTAINMENT]` | Specify the long term containment | "[specify value]" |
| `[SYSTEM_ISOLATION]` | Specify the system isolation | "[specify value]" |
| `[NETWORK_SEGMENTATION]` | Specify the network segmentation | "[specify value]" |
| `[ACCESS_RESTRICTIONS]` | Specify the access restrictions | "[specify value]" |
| `[SERVICE_DISRUPTION]` | Specify the service disruption | "[specify value]" |
| `[BUSINESS_CONTINUITY]` | Specify the business continuity | "[specify value]" |
| `[CONTAINMENT_COMMUNICATION]` | Specify the containment communication | "[specify value]" |
| `[MONITORING_ENHANCEMENT]` | Specify the monitoring enhancement | "[specify value]" |
| `[EVIDENCE_PRESERVATION]` | Specify the evidence preservation | "[specify value]" |
| `[THREAT_ELIMINATION]` | Specify the threat elimination | "[specify value]" |
| `[SYSTEM_HARDENING]` | Specify the system hardening | "[specify value]" |
| `[PATCH_MANAGEMENT]` | Specify the patch management | "[specify value]" |
| `[CONFIGURATION_CHANGES]` | Specify the configuration changes | "[specify value]" |
| `[RECOVERY_PLANNING]` | Specify the recovery planning | "[specify value]" |
| `[DATA_RESTORATION]` | Specify the data restoration | "[specify value]" |
| `[SERVICE_RESTORATION]` | Specify the service restoration | "[specify value]" |
| `[MONITORING_RESTORATION]` | Specify the monitoring restoration | "[specify value]" |
| `[VALIDATION_TESTING]` | Specify the validation testing | "[specify value]" |
| `[RETURN_TO_OPERATIONS]` | Specify the return to operations | "[specify value]" |
| `[INTERNAL_COMMUNICATIONS]` | Specify the internal communications | "[specify value]" |
| `[EXTERNAL_COMMUNICATIONS]` | Specify the external communications | "[specify value]" |
| `[REGULATORY_REPORTING]` | Specify the regulatory reporting | "[specify value]" |
| `[CUSTOMER_NOTIFICATIONS]` | Specify the customer notifications | "[specify value]" |
| `[MEDIA_RELATIONS]` | Specify the media relations | "[specify value]" |
| `[LEGAL_NOTIFICATIONS]` | Specify the legal notifications | "[specify value]" |
| `[STAKEHOLDER_UPDATES]` | Specify the stakeholder updates | "2025-01-15" |
| `[STATUS_REPORTS]` | Specify the status reports | "In Progress" |
| `[FINAL_REPORT]` | Specify the final report | "[specify value]" |
| `[INCIDENT_DOCUMENTATION]` | Specify the incident documentation | "[specify value]" |



## Best Practices

1. **Prepare and practice response procedures regularly**
2. **Maintain updated contact lists and escalation paths**
3. **Document everything during incident response**
4. **Preserve evidence while containing threats**
5. **Conduct thorough post-incident reviews**