---
category: security
last_updated: 2025-11-22
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- security
- incident-response
- playbooks
- containment
title: Incident Response Template
use_cases:
- Creating comprehensive incident response planning including detection, analysis,
  containment, eradication, recovery, and lessons learned for effective cybersecurity
  incident management.
- Project planning and execution
- Strategy development
industries:
- technology
type: template
difficulty: intermediate
slug: incident-response
---

# Incident Response Template

## Purpose
Comprehensive incident response planning including detection, analysis, containment, eradication, recovery, and lessons learned for effective cybersecurity incident management.

## Quick IR Planning Prompt
Develop incident response capability for [organization]. Define: incident classification matrix (severity P1-P4), response team roles (commander, security, IT ops, legal, comms), escalation paths, and communication templates. Create playbooks for: [ransomware, phishing, data breach, DDoS]. Deploy: SIEM detection rules, forensic toolkit, evidence handling procedures. Schedule quarterly tabletop exercises.

## Quick Start

**Set Your Foundation:**
1. Define incident types and severity levels: critical, high, medium, low
2. Establish incident response team: commander, security, IT ops, legal, communications
3. Set up incident communication channels and contact lists

**Configure Key Parameters:**
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

### Incident Identification

| Variable | Description | Example |
|----------|-------------|----------|
| `[INCIDENT_ID]` | Unique identifier for tracking | "INC-2025-0142", "SEC-20250122-001" |
| `[INCIDENT_TYPE]` | Category of security incident | "Ransomware", "Data Breach", "Phishing", "DDoS", "Insider Threat", "Malware" |
| `[SEVERITY_LEVEL]` | Impact severity classification | "Critical (P1)", "High (P2)", "Medium (P3)", "Low (P4)" |
| `[AFFECTED_SYSTEMS]` | Systems impacted by the incident | "500 Windows workstations, 3 file servers", "Customer database, payment system" |
| `[DISCOVERY_METHOD]` | How the incident was detected | "EDR alert", "SIEM correlation", "User report", "External notification" |
| `[DISCOVERY_TIME]` | When incident was first detected | "2025-01-22 02:15 UTC", "Monday 2AM during overnight monitoring" |
| `[REPORTING_TIME]` | When incident was formally reported | "15 minutes after discovery", "2025-01-22 02:30 UTC" |
| `[INITIAL_REPORTER]` | Person/system that reported | "SOC Analyst John Smith", "CrowdStrike automated alert", "Help desk ticket #4521" |
| `[BUSINESS_IMPACT]` | Business functions affected | "Customer service down, payroll processing delayed, e-commerce unavailable" |
| `[ESTIMATED_LOSS]` | Projected financial impact | "$500K operational loss", "$2M potential regulatory fines", "$50K/hour downtime" |

### Response Team

| Variable | Description | Example |
|----------|-------------|----------|
| `[INCIDENT_COMMANDER]` | Lead person directing response | "CISO Jane Doe", "Security Operations Manager", "On-call incident commander" |
| `[SECURITY_TEAM]` | Security personnel assigned | "3 SOC analysts, 2 threat hunters, 1 forensics specialist" |
| `[IT_OPERATIONS]` | IT ops support team | "Network admin, 2 system administrators, DBA on standby" |
| `[LEGAL_TEAM]` | Legal counsel involvement | "General Counsel + outside cybersecurity counsel (firm on retainer)" |
| `[COMMUNICATIONS_TEAM]` | PR/comms personnel | "VP Communications, Social media manager, Customer success lead" |
| `[EXTERNAL_RESOURCES]` | Third-party support | "CrowdStrike IR services, Kroll forensics, FBI cyber liaison" |
| `[ESCALATION_PATH]` | Chain of escalation | "Analyst → Team Lead → SOC Manager → CISO → CEO (for critical)" |
| `[AUTHORITY_LEVELS]` | Decision-making authority | "CISO can approve system shutdown, CEO required for ransom decisions" |

### Detection and Analysis

| Variable | Description | Example |
|----------|-------------|----------|
| `[DETECTION_SOURCES]` | Systems that detected activity | "CrowdStrike EDR, Splunk SIEM, Darktrace NDR, firewall logs" |
| `[ALERT_CORRELATION]` | How alerts were correlated | "MITRE ATT&CK mapping, timeline correlation, IOC enrichment" |
| `[EVIDENCE_COLLECTION]` | Evidence gathered | "Memory dumps, disk images, network PCAPs, log exports, screenshots" |
| `[FORENSIC_ANALYSIS]` | Forensic investigation approach | "Volatile data first, disk imaging with FTK, malware analysis sandbox" |
| `[IOC_IDENTIFICATION]` | Indicators of compromise found | "C2 domains, malicious IP addresses, file hashes, registry keys" |
| `[ATTACK_TIMELINE]` | Chronological attack progression | "Initial access 01/15, lateral movement 01/18, data exfil 01/20-01/22" |
| `[ROOT_CAUSE_ANALYSIS]` | Underlying cause determination | "Phishing email with weaponized attachment, unpatched VPN vulnerability" |

### Containment Strategy

| Variable | Description | Example |
|----------|-------------|----------|
| `[SHORT_TERM_CONTAINMENT]` | Immediate containment actions | "Isolate affected hosts via EDR, block C2 IPs at firewall" |
| `[LONG_TERM_CONTAINMENT]` | Sustained containment measures | "Segment network, rebuild compromised systems, reset all credentials" |
| `[SYSTEM_ISOLATION]` | How systems are isolated | "EDR network isolation, VLAN quarantine, physical disconnect for critical" |
| `[NETWORK_SEGMENTATION]` | Network isolation approach | "Block lateral movement paths, isolate affected VLAN, ACL restrictions" |
| `[ACCESS_RESTRICTIONS]` | Access control changes | "Disable compromised accounts, force MFA reset, revoke VPN access" |
| `[EVIDENCE_PRESERVATION]` | Evidence protection measures | "Hash all collected evidence, maintain chain of custody, secure storage" |

### Eradication and Recovery

| Variable | Description | Example |
|----------|-------------|----------|
| `[THREAT_ELIMINATION]` | Threat removal approach | "AV scan all systems, remove persistence mechanisms, clean registry" |
| `[SYSTEM_HARDENING]` | Post-incident hardening | "Patch vulnerabilities, disable unnecessary services, update firewall rules" |
| `[PATCH_MANAGEMENT]` | Patching activities | "Emergency patch for exploited CVE, update all endpoints within 24 hours" |
| `[DATA_RESTORATION]` | Data recovery process | "Restore from verified clean backup, validate data integrity" |
| `[SERVICE_RESTORATION]` | Service recovery order | "1: Auth systems, 2: Email, 3: Core apps, 4: User workstations" |
| `[VALIDATION_TESTING]` | Post-recovery validation | "Vulnerability scan, penetration test, functionality testing, user acceptance" |

### Communication

| Variable | Description | Example |
|----------|-------------|----------|
| `[INTERNAL_COMMUNICATIONS]` | Employee communication plan | "All-hands email, manager briefings, intranet updates every 4 hours" |
| `[EXTERNAL_COMMUNICATIONS]` | External stakeholder comms | "Customer notification email, vendor alerts, partner briefings" |
| `[REGULATORY_REPORTING]` | Required regulatory notices | "72-hour GDPR notification, state AG breach notification, SEC 8-K if material" |
| `[CUSTOMER_NOTIFICATIONS]` | Customer notification approach | "Direct email to affected, status page updates, support hotline" |
| `[MEDIA_RELATIONS]` | Press/media handling | "Prepared statement only, no interviews during active incident" |
| `[FINAL_REPORT]` | Post-incident documentation | "Executive summary, technical details, lessons learned, remediation status" |



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Incident Response Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Cybersecurity](../../technology/Cybersecurity/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive incident response planning including detection, analysis, containment, eradication, recovery, and lessons learned for effective cybersecurity incident management.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Prepare and practice response procedures regularly**
2. **Maintain updated contact lists and escalation paths**
3. **Document everything during incident response**
4. **Preserve evidence while containing threats**
5. **Conduct thorough post-incident reviews**