---
title: Incident Response Template
category: technology/Cybersecurity
tags: [communication, data-science, design, management, research, security, strategy, technology]
use_cases:
  - Implementing comprehensive incident response planning including detection, analysis, containm...
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

## Template Structure

### Incident Overview
- **Incident ID**: {incident_id}
- **Incident Type**: {incident_type}
- **Severity Level**: {severity_level}
- **Affected Systems**: {affected_systems}
- **Discovery Method**: {discovery_method}
- **Discovery Time**: {discovery_time}
- **Reporting Time**: {reporting_time}
- **Initial Reporter**: {initial_reporter}
- **Business Impact**: {business_impact}
- **Estimated Loss**: {estimated_loss}

### Response Team
- **Incident Commander**: {incident_commander}
- **Security Team**: {security_team}
- **IT Operations**: {it_operations}
- **Legal Team**: {legal_team}
- **Communications**: {communications_team}
- **External Resources**: {external_resources}
- **Escalation Path**: {escalation_path}
- **Contact Information**: {contact_information}
- **Roles and Responsibilities**: {roles_responsibilities}
- **Authority Levels**: {authority_levels}

### Detection and Analysis
- **Detection Sources**: {detection_sources}
- **Alert Correlation**: {alert_correlation}
- **Evidence Collection**: {evidence_collection}
- **Forensic Analysis**: {forensic_analysis}
- **IOC Identification**: {ioc_identification}
- **Attack Timeline**: {attack_timeline}
- **Attribution Analysis**: {attribution_analysis}
- **Scope Assessment**: {scope_assessment}
- **Impact Analysis**: {impact_analysis}
- **Root Cause Analysis**: {root_cause_analysis}

### Containment Strategy
- **Short-term Containment**: {short_term_containment}
- **Long-term Containment**: {long_term_containment}
- **System Isolation**: {system_isolation}
- **Network Segmentation**: {network_segmentation}
- **Access Restrictions**: {access_restrictions}
- **Service Disruption**: {service_disruption}
- **Business Continuity**: {business_continuity}
- **Communication Plan**: {containment_communication}
- **Monitoring Enhancement**: {monitoring_enhancement}
- **Evidence Preservation**: {evidence_preservation}

### Eradication and Recovery
- **Threat Elimination**: {threat_elimination}
- **System Hardening**: {system_hardening}
- **Patch Management**: {patch_management}
- **Configuration Changes**: {configuration_changes}
- **Recovery Planning**: {recovery_planning}
- **Data Restoration**: {data_restoration}
- **Service Restoration**: {service_restoration}
- **Monitoring Restoration**: {monitoring_restoration}
- **Validation Testing**: {validation_testing}
- **Return to Operations**: {return_to_operations}

### Communication and Reporting
- **Internal Communications**: {internal_communications}
- **External Communications**: {external_communications}
- **Regulatory Reporting**: {regulatory_reporting}
- **Customer Notifications**: {customer_notifications}
- **Media Relations**: {media_relations}
- **Legal Notifications**: {legal_notifications}
- **Stakeholder Updates**: {stakeholder_updates}
- **Status Reports**: {status_reports}
- **Final Report**: {final_report}
- **Documentation**: {incident_documentation}

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

Containment Strategy:
- Isolate infected systems system isolation within 30 minutes
- Segment network to prevent spread network segmentation
- Disable file sharing, remote access access restrictions
- Maintain critical services with backup systems business continuity
- Deploy additional monitoring on network boundaries monitoring enhancement

Communication and Reporting:
- Brief executive team, board internal communications
- Notify cyber insurance, legal counsel external communications
- File FBI IC3, state AG regulatory reporting
- Send customer data breach notifications customer notifications
- Prepare holding statements for media inquiries media relations
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `{incident_id}` | Specify the incident id | "[specify value]" |
| `{incident_type}` | Specify the incident type | "Standard" |
| `{severity_level}` | Specify the severity level | "[specify value]" |
| `{affected_systems}` | Specify the affected systems | "[specify value]" |
| `{discovery_method}` | Specify the discovery method | "[specify value]" |
| `{discovery_time}` | Specify the discovery time | "[specify value]" |
| `{reporting_time}` | Specify the reporting time | "[specify value]" |
| `{initial_reporter}` | Specify the initial reporter | "[specify value]" |
| `{business_impact}` | Specify the business impact | "[specify value]" |
| `{estimated_loss}` | Specify the estimated loss | "[specify value]" |
| `{incident_commander}` | Specify the incident commander | "[specify value]" |
| `{security_team}` | Specify the security team | "[specify value]" |
| `{it_operations}` | Specify the it operations | "[specify value]" |
| `{legal_team}` | Specify the legal team | "[specify value]" |
| `{communications_team}` | Specify the communications team | "[specify value]" |
| `{external_resources}` | Specify the external resources | "[specify value]" |
| `{escalation_path}` | Specify the escalation path | "[specify value]" |
| `{contact_information}` | Specify the contact information | "[specify value]" |
| `{roles_responsibilities}` | Specify the roles responsibilities | "[specify value]" |
| `{authority_levels}` | Specify the authority levels | "[specify value]" |
| `{detection_sources}` | Specify the detection sources | "[specify value]" |
| `{alert_correlation}` | Specify the alert correlation | "[specify value]" |
| `{evidence_collection}` | Specify the evidence collection | "[specify value]" |
| `{forensic_analysis}` | Specify the forensic analysis | "[specify value]" |
| `{ioc_identification}` | Specify the ioc identification | "[specify value]" |
| `{attack_timeline}` | Specify the attack timeline | "6 months" |
| `{attribution_analysis}` | Specify the attribution analysis | "[specify value]" |
| `{scope_assessment}` | Specify the scope assessment | "[specify value]" |
| `{impact_analysis}` | Specify the impact analysis | "[specify value]" |
| `{root_cause_analysis}` | Specify the root cause analysis | "[specify value]" |
| `{short_term_containment}` | Specify the short term containment | "[specify value]" |
| `{long_term_containment}` | Specify the long term containment | "[specify value]" |
| `{system_isolation}` | Specify the system isolation | "[specify value]" |
| `{network_segmentation}` | Specify the network segmentation | "[specify value]" |
| `{access_restrictions}` | Specify the access restrictions | "[specify value]" |
| `{service_disruption}` | Specify the service disruption | "[specify value]" |
| `{business_continuity}` | Specify the business continuity | "[specify value]" |
| `{containment_communication}` | Specify the containment communication | "[specify value]" |
| `{monitoring_enhancement}` | Specify the monitoring enhancement | "[specify value]" |
| `{evidence_preservation}` | Specify the evidence preservation | "[specify value]" |
| `{threat_elimination}` | Specify the threat elimination | "[specify value]" |
| `{system_hardening}` | Specify the system hardening | "[specify value]" |
| `{patch_management}` | Specify the patch management | "[specify value]" |
| `{configuration_changes}` | Specify the configuration changes | "[specify value]" |
| `{recovery_planning}` | Specify the recovery planning | "[specify value]" |
| `{data_restoration}` | Specify the data restoration | "[specify value]" |
| `{service_restoration}` | Specify the service restoration | "[specify value]" |
| `{monitoring_restoration}` | Specify the monitoring restoration | "[specify value]" |
| `{validation_testing}` | Specify the validation testing | "[specify value]" |
| `{return_to_operations}` | Specify the return to operations | "[specify value]" |
| `{internal_communications}` | Specify the internal communications | "[specify value]" |
| `{external_communications}` | Specify the external communications | "[specify value]" |
| `{regulatory_reporting}` | Specify the regulatory reporting | "[specify value]" |
| `{customer_notifications}` | Specify the customer notifications | "[specify value]" |
| `{media_relations}` | Specify the media relations | "[specify value]" |
| `{legal_notifications}` | Specify the legal notifications | "[specify value]" |
| `{stakeholder_updates}` | Specify the stakeholder updates | "2025-01-15" |
| `{status_reports}` | Specify the status reports | "In Progress" |
| `{final_report}` | Specify the final report | "[specify value]" |
| `{incident_documentation}` | Specify the incident documentation | "[specify value]" |



## Best Practices

1. **Prepare and practice response procedures regularly**
2. **Maintain updated contact lists and escalation paths**
3. **Document everything during incident response**
4. **Preserve evidence while containing threats**
5. **Conduct thorough post-incident reviews**