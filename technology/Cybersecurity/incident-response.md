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

## Best Practices

1. **Prepare and practice response procedures regularly**
2. **Maintain updated contact lists and escalation paths**
3. **Document everything during incident response**
4. **Preserve evidence while containing threats**
5. **Conduct thorough post-incident reviews**