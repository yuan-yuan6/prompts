---
category: security
last_updated: 2025-11-23
title: SIEM & Security Monitoring Framework
tags:
- security
- siem
- soc
- log-analysis
use_cases:
- Implementing SIEM for threat detection
- Security event monitoring and analysis
- SOC operations and incident response
- Compliance logging and reporting
related_templates:
- security/Cybersecurity/security-operations.md
- security/Cybersecurity/incident-response.md
- security/Cybersecurity/threat-intelligence.md
industries:
- technology
type: template
difficulty: intermediate
slug: siem-security-monitoring
---

# SIEM & Security Monitoring Framework

## Purpose
Comprehensive framework for implementing SIEM platforms, security monitoring, log management, threat detection, incident response, and SOC operations.

## Quick SIEM Prompt
Implement SIEM for [organization] using [Splunk/Sentinel/Elastic/QRadar]. Log sources: [X endpoints], [Y servers], [firewalls], [cloud: AWS/Azure/GCP], [applications]. Configure: detection use cases (brute force, lateral movement, data exfiltration), correlation rules, alert thresholds, compliance dashboards. SOC operations: triage procedures, escalation matrix, 24x7 coverage model. Target: [X] EPS, [Y] day retention.

## Quick Start

**Need to implement SIEM?** Use this minimal example:

```
Implement SIEM solution (Splunk/Sentinel/Elastic) for enterprise collecting logs from 5000 endpoints, 200 servers, firewalls, cloud environments. Configure use cases for threat detection, compliance monitoring, and incident response with 24x7 SOC operations.
```

### When to Use This
- Building or maturing a Security Operations Center (SOC)
- Implementing centralized security monitoring for compliance
- Migrating from legacy SIEM to modern platform
- Developing threat detection use cases and playbooks
- Integrating cloud workloads into security monitoring

### Basic 3-Step Workflow
1. **Deploy & Integrate** - SIEM platform, log sources
2. **Configure Use Cases** - Detection rules, dashboards
3. **Operate & Optimize** - SOC operations, tuning

---

## Template

```markdown
I need to implement SIEM and security monitoring. Please provide comprehensive SIEM deployment and operations guidance.

## ENVIRONMENT CONTEXT

### Infrastructure
- Log sources: [ENDPOINTS_SERVERS_NETWORK_CLOUD_APPLICATIONS]
- Log volume: [EVENTS_PER_SECOND_OR_TB_PER_DAY]
- Retention requirements: [DAYS_MONTHS_YEARS]
- Compliance: [PCI_DSS_HIPAA_SOC2_GDPR]

### Current State
- Existing tools: [SIEM_LOG_MANAGEMENT_MONITORING]
- SOC maturity: [NONE_INITIAL_MANAGED_OPTIMIZED]
- Staff: [ANALYSTS_ENGINEERS_MANAGER]

## SIEM IMPLEMENTATION

### 1. Platform Selection
- Splunk Enterprise Security
- Microsoft Sentinel
- Elastic Security
- IBM QRadar
- LogRhythm
- Sumo Logic

### 2. Log Collection
- Syslog collection
- Agent-based collection
- API integration
- Cloud service logs
- Application logs
- Database audit logs

### 3. Use Case Development
- Authentication monitoring
- Privilege escalation detection
- Malware detection
- Data exfiltration
- Insider threat detection
- Compliance monitoring

### 4. Detection Rules
- Correlation rules
- Threat intelligence
- Behavioral analytics
- Machine learning models
- Custom detection logic

### 5. Incident Response Integration
- Alert routing and triage
- Case management
- SOAR integration
- Playbook automation
- Forensics and investigation

### 6. Dashboards & Reporting
- Executive dashboards
- SOC operational dashboards
- Compliance reports
- Threat intelligence
- KPIs and metrics

## SOC OPERATIONS

### Tier 1: Monitoring & Triage
- Alert monitoring
- Initial triage
- False positive filtering
- Escalation to Tier 2

### Tier 2: Investigation & Response
- Deep dive analysis
- Threat hunting
- Incident response
- Remediation coordination

### Tier 3: Advanced Analysis
- Malware analysis
- Threat intelligence
- Detection engineering
- Process improvement

## OUTPUT REQUIREMENTS

Provide:
1. SIEM architecture design
2. Log collection strategy
3. Use case library
4. Detection rule examples
5. SOC playbooks
6. Dashboard designs
7. KPIs and metrics
```

## Variables

### SIEM_PLATFORM
The SIEM solution being implemented.
- Examples: "Splunk Enterprise Security", "Microsoft Sentinel", "Elastic Security", "IBM QRadar", "LogRhythm NextGen SIEM", "Google Chronicle", "Sumo Logic Cloud SIEM"

### LOG_SOURCES
Categories of log sources to integrate.
- Examples: "Windows Event Logs", "Linux syslog/auditd", "Firewall logs (Palo Alto, Cisco)", "AWS CloudTrail/GuardDuty", "Azure Activity Logs", "Okta/Azure AD", "EDR (CrowdStrike, Defender)", "Email gateway", "Proxy logs"

### LOG_VOLUME
Expected log ingestion volume.
- Examples: "50 GB/day", "500 GB/day", "5 TB/day", "10,000 EPS (events per second)", "100,000 EPS"

### RETENTION_REQUIREMENTS
Log retention periods for compliance.
- Examples: "Hot: 30 days, Warm: 90 days, Cold: 1 year", "7 years for SOX", "6 years for HIPAA", "1 year online, 7 years archive"

### SOC_MODEL
Security operations center staffing model.
- Examples: "In-house 24x7 SOC", "Hybrid (in-house + MSSP)", "Fully managed MSSP", "Business hours only with on-call", "Follow-the-sun global SOC"

### SOAR_PLATFORM
Security orchestration and automated response solution.
- Examples: "Splunk SOAR (Phantom)", "Microsoft Sentinel Playbooks", "Palo Alto XSOAR", "Swimlane", "Tines", "TheHive + Cortex"

---

## Usage Examples

### Example 1: Enterprise Splunk Deployment
```
SIEM_PLATFORM: Splunk Enterprise Security with Premium Solutions
LOG_SOURCES: 8,000 Windows endpoints, 500 Linux servers, Palo Alto firewalls, AWS (50 accounts), Okta, CrowdStrike
LOG_VOLUME: 2 TB/day ingestion
RETENTION_REQUIREMENTS: 90 days hot, 1 year warm, 7 years cold (S3)
SOC_MODEL: In-house 24x7 SOC with 15 analysts (5 per shift)
SOAR_PLATFORM: Splunk SOAR (Phantom)

Key Implementations:
- Architecture: Distributed indexer cluster (10 nodes) + search head cluster
- Log Collection: Universal Forwarders for Windows, HTTP Event Collector for cloud
- Use Cases: 150+ correlation searches covering MITRE ATT&CK
- Dashboards: Executive summary, SOC operations, compliance (PCI, SOX)
- Alerting: Risk-based alerting with asset/identity enrichment
- Automation: 50+ SOAR playbooks for tier-1 automation
- Threat Intel: Splunk ES with Recorded Future integration
- Compliance: PCI-DSS daily reports, SOX evidence collection
```

### Example 2: Microsoft Sentinel Cloud-Native
```
SIEM_PLATFORM: Microsoft Sentinel (Azure-native)
LOG_SOURCES: Azure resources, M365, Azure AD, Defender for Endpoint, AWS (via connector)
LOG_VOLUME: 500 GB/day with Sentinel analytics tier pricing
RETENTION_REQUIREMENTS: 90 days analytics, 2 years basic logs (archive tier)
SOC_MODEL: Hybrid - 5 internal analysts + Microsoft Managed XDR
SOAR_PLATFORM: Sentinel Playbooks (Logic Apps)

Key Implementations:
- Architecture: Multi-workspace for data residency (US, EU)
- Log Collection: Azure Monitor Agent, Sentinel connectors, CEF/Syslog
- Use Cases: Microsoft-provided analytics rules + 50 custom KQL rules
- Dashboards: Workbooks for M365 security, identity threats, cloud posture
- Alerting: Fusion ML detection for advanced attacks
- Automation: Playbooks for auto-enrichment, ticket creation, blocking
- Threat Intel: MDTI (Microsoft Defender Threat Intelligence)
- Cost Optimization: Commitment tiers, basic logs for high-volume sources
```

### Example 3: Elastic Security Open Platform
```
SIEM_PLATFORM: Elastic Security (self-managed on Kubernetes)
LOG_SOURCES: Kubernetes clusters, Linux servers, network devices, cloud (multi-cloud)
LOG_VOLUME: 1.5 TB/day, 50,000 EPS peak
RETENTION_REQUIREMENTS: 30 days hot, 90 days warm (ILM policies)
SOC_MODEL: DevSecOps model - 3 detection engineers, developers on-call
SOAR_PLATFORM: TheHive + Cortex + Shuffle

Key Implementations:
- Architecture: Elastic Cloud on Kubernetes (ECK) with autoscaling
- Log Collection: Elastic Agent (Fleet-managed), Filebeat, Metricbeat
- Use Cases: Detection rules aligned to MITRE ATT&CK for containers/cloud
- Dashboards: Kibana dashboards for Kubernetes security, cloud posture
- Alerting: Elastic detection rules with risk scoring
- Automation: TheHive cases with Cortex analyzers for enrichment
- Threat Hunting: Osquery integration for live endpoint queries
- Cost: Open-source core with Elastic subscription for ML/alerting
```

---

## Best Practices

1. **Start with critical log sources** - Prioritize authentication, firewall, endpoint, and cloud audit logs before expanding
2. **Normalize data early** - Use Common Information Model (CIM) or ECS for consistent field naming
3. **Tune before scaling** - Address false positives before adding more use cases
4. **Risk-based alerting** - Aggregate related events into risk scores rather than individual alerts
5. **Automate tier-1 tasks** - Use SOAR for enrichment, ticket creation, and common response actions
6. **Map to MITRE ATT&CK** - Align detection coverage to framework for gap analysis
7. **Retention tiers** - Use hot/warm/cold storage tiers to manage costs
8. **Regular detection reviews** - Monthly review of detection efficacy and false positive rates
9. **Threat hunting program** - Proactive hypothesis-driven hunts, not just alert response
10. **Measure SOC metrics** - Track MTTD, MTTR, alert volume, and analyst workload

## Common Pitfalls

❌ **Alert fatigue** - Too many alerts overwhelming analysts
✅ Instead: Risk-based alerting, aggressive tuning, and automation

❌ **Missing log sources** - Critical systems not sending logs to SIEM
✅ Instead: Log source inventory with coverage mapping to use cases

❌ **No normalization** - Inconsistent field names across sources
✅ Instead: Enforce data model (CIM/ECS) at ingestion

❌ **Detection without response** - Alerts with no playbook or action
✅ Instead: Every detection rule needs a documented response procedure

❌ **Cost overruns** - Unexpected SIEM licensing costs from log volume
✅ Instead: Volume forecasting, tiered retention, filtering low-value logs

## SOC Metrics to Track

| Metric | Target | Description |
|--------|--------|-------------|
| MTTD (Mean Time to Detect) | < 24 hours | Time from attack start to detection |
| MTTR (Mean Time to Respond) | < 4 hours | Time from detection to containment |
| Alert Volume | < 50/analyst/day | Sustainable workload for analysts |
| False Positive Rate | < 20% | Percentage of alerts that are benign |
| Detection Coverage | > 80% ATT&CK | Percentage of MITRE techniques covered |
| Automation Rate | > 60% tier-1 | Percentage of tier-1 tasks automated |
