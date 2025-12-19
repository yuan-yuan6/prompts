---
category: security
title: SIEM & Security Monitoring Framework
tags:
- security
- siem
- soc
- log-analysis
use_cases:
- Implementing SIEM platform with log collection from endpoints, servers, network devices, cloud achieving 24x7 threat detection and compliance reporting
- Building SOC operations with tiered analyst model (L1 triage, L2 investigation, L3 threat hunting) achieving MTTD <24h, MTTR <4h
- Developing detection use cases mapped to MITRE ATT&CK covering authentication attacks, lateral movement, data exfiltration with SOAR automation
related_templates:
- security/Cybersecurity/security-operations.md
- security/Cybersecurity/incident-response.md
- security/Cybersecurity/threat-intelligence.md
industries:
- technology
- financial-services
- healthcare
- government
type: framework
difficulty: intermediate
slug: siem-security-monitoring
---

# SIEM & Security Monitoring Framework

## Purpose
Implement SIEM platform covering log collection, normalization, threat detection, correlation, SOC operations, incident response integration, and compliance reporting achieving comprehensive security visibility and rapid threat detection.

## 🚀 Quick SIEM Prompt

> Implement SIEM using **[PLATFORM]** (Splunk/Sentinel/Elastic/QRadar) for **[ORGANIZATION]**. Log sources: **[ENDPOINTS]** endpoints, **[SERVERS]** servers, **[NETWORK]** devices, **[CLOUD]** (AWS/Azure/GCP), **[APPS]**. Volume: **[X_TB/day]** or **[Y_EPS]**. Retention: **[HOT/WARM/COLD]** tiers. Use cases: **[MITRE_ATT&CK_COVERAGE]**. SOC: **[24x7/BUSINESS_HOURS]**, **[TIERS]**. SOAR: **[PLATFORM]** for automation. Compliance: **[PCI/HIPAA/SOC2]**.

---

## Template

Implement SIEM solution for {ORGANIZATION} with {LOG_VOLUME} ingestion from {LOG_SOURCES} achieving {COMPLIANCE_REQUIREMENTS} compliance with {SOC_MODEL} operations.

**PLATFORM SELECTION AND ARCHITECTURE**

Choose SIEM platform matching scale and requirements. Platform options: Splunk Enterprise Security (comprehensive detection, mature ecosystem, highest cost), Microsoft Sentinel (Azure-native, cloud-first, consumption pricing), Elastic Security (open-source core, Kubernetes-friendly, cost-effective), IBM QRadar (flow-based, strong compliance, complex deployment), Chronicle (Google-scale, unlimited retention, less mature). Architecture design: distributed for scale (indexers, search heads, forwarders for Splunk), cloud-native (serverless ingestion for Sentinel), hybrid (on-prem sensitive data, cloud for scale). Sizing: calculate based on EPS (events per second) and retention requirements, plan for 30% growth, consider hot/warm/cold tiers for cost optimization.

**LOG COLLECTION STRATEGY**

Prioritize critical log sources for security visibility. Essential sources: authentication logs (Windows Event Logs, Azure AD sign-ins, Okta, VPN), endpoint security (EDR telemetry from CrowdStrike/Defender, antivirus alerts), network security (firewall accepts/denies, IDS/IPS alerts, VPN connections), cloud audit (AWS CloudTrail/GuardDuty, Azure Activity/Defender, GCP Cloud Logging), application logs (web server access/error, database audit, critical business applications). Collection methods: agent-based for endpoints (Splunk Universal Forwarder, Azure Monitor Agent, Elastic Agent), syslog for network devices, API integration for cloud services (AWS EventBridge, Azure Event Hub), HTTP Event Collector for applications.

Data normalization: implement Common Information Model (CIM for Splunk) or Elastic Common Schema (ECS), normalize field names at ingestion (source_ip vs src_ip → consistent naming), enrich with asset/identity context (criticality, owner, location), tag by compliance scope (PCI CDE, HIPAA PHI systems). Log filtering: filter low-value logs before ingestion (debug logs, health checks), sample high-volume sources (HTTP 200s) while keeping security events, use tiered retention (hot 30 days, warm 90 days, cold 1+ years).

**USE CASE DEVELOPMENT**

Build detection library covering threat landscape. Use case categories: authentication attacks (brute force, credential stuffing, impossible travel), privilege escalation (admin account creation, privilege changes, sudo usage), lateral movement (SMB/RDP from unusual sources, pass-the-hash, service account abuse), data exfiltration (large uploads, database exports, cloud storage access), malware (EDR detections, command-line anomalies, persistence mechanisms), insider threat (after-hours access, data downloads, policy violations), cloud security (IAM changes, public S3 buckets, security group modifications).

Detection methodology: signature-based for known threats (failed login thresholds, known-bad IOCs), behavioral analytics for anomalies (baseline normal then detect deviations), correlation for attack chains (initial access → privilege escalation → lateral movement), machine learning for zero-days (Sentinel Fusion, Splunk UBA, Elastic ML jobs). MITRE ATT&CK mapping: map each detection to technique (T1078: Valid Accounts, T1021: Remote Services), identify coverage gaps through heatmap, prioritize development for uncovered high-risk techniques.

**DETECTION ENGINEERING**

Write effective correlation rules and analytics. Rule structure: define data sources required, establish baseline behavior (e.g., typical login times per user), set thresholds avoiding false positives (5 failed logins in 10 minutes, not 3 in 1 minute), include exclusions for known-good (service accounts, monitoring systems). Rule examples: failed authentication (EventCode 4625 Windows, status code 50126 Azure AD) exceeding threshold from single source, privilege escalation (user added to Administrators/Domain Admins), lateral movement (RDP/SMB from workstation to workstation, not server), data exfiltration (outbound network volume exceeding baseline by 10x).

Risk-based alerting: aggregate related events into risk scores rather than individual alerts, assign risk score per event (critical finding = +100, suspicious = +25), trigger incident when user/asset risk exceeds threshold (>100 = incident), reset risk scores after investigation period. Alert enrichment: add user context (title, department, manager, recent HR actions), asset context (criticality tier, data classification, owner), threat intelligence (IP reputation, domain age, known-bad indicator), historical context (user's first time doing this action? seen before?).

**SOC OPERATIONS MODEL**

Structure analyst tiers for efficient operations. Tier 1 (Monitoring & Triage): monitor alert queue, perform initial triage (true positive vs false positive), gather basic evidence (screenshot, log snippets), escalate confirmed incidents to Tier 2, document triage decisions. Tier 2 (Investigation & Response): deep-dive investigation (timeline reconstruction, scope assessment), coordinate response actions (isolate endpoint, disable account, block IP), engage stakeholders (IT, management, legal), document investigation findings. Tier 3 (Threat Hunting & Engineering): proactive threat hunting (hypothesis-driven searches), detection engineering (develop new rules, tune existing), malware analysis and reverse engineering, threat intelligence integration and correlation.

Staffing models: in-house 24x7 SOC (15+ analysts, 5 per shift across 3 shifts), hybrid (in-house business hours + MSSP after-hours), follow-the-sun (global SOC sites handing off coverage), business hours only (suitable for low-risk environments with on-call escalation). Shift structure: 12-hour shifts with 2-2-3 schedule, weekly shift lead rotation, monthly analyst rotation between tiers for skill development.

**SOAR INTEGRATION**

Automate repetitive analyst tasks. Automation candidates: alert enrichment (query threat intel, lookup user/asset, geolocation lookup), tier-1 triage (collect standard evidence, run predefined queries, check against whitelist), response actions (isolate endpoint via EDR API, disable user account in AD/Azure AD, block IP in firewall), ticket creation (auto-create ServiceNow ticket with evidence, assign to appropriate team).

Platform selection: Splunk SOAR (Phantom) for Splunk shops, Sentinel Playbooks (Logic Apps) for Azure-native, Palo Alto XSOAR for multi-vendor, Tines/Shuffle for cost-conscious, TheHive+Cortex for open-source. Playbook examples: phishing response (extract URLs/attachments → analyze in sandbox → block malicious indicators → notify users), failed login response (check if account locked → verify user travel → check for credential compromise → alert user if suspicious), malware detection (isolate endpoint → collect forensic triage → submit sample to sandbox → remediate based on findings).

Automation philosophy: automate tier-1 decisions (>60% of repetitive tasks), human-in-the-loop for tier-2 response (playbook suggests action, analyst approves), keep human judgment for complex investigations. Success metrics: automation rate (% of tier-1 tasks automated), analyst time saved (hours per week), MTTR reduction (faster response through automation).

**DASHBOARDS AND REPORTING**

Build visualizations for different audiences. Executive dashboards: security posture overview (open incidents by severity, trending risk), MTTD and MTTR trends, compliance status (PCI scans, HIPAA audit logs), top threats and attack vectors. SOC operational dashboards: alert queue (by priority, age, assignment), analyst workload (alerts per analyst, queue depth), detection coverage (MITRE ATT&CK heatmap), infrastructure health (ingestion rates, parsing errors, search performance).

Compliance reporting: PCI-DSS (quarterly vulnerability scan results, access to CDE logs, firewall rule changes), HIPAA (ePHI access logs, breach notification evidence, audit trail), SOC 2 (security monitoring evidence, incident response documentation, access reviews). Threat intelligence: IOC tracking (malicious IPs/domains blocked), threat actor tracking (APT groups targeting industry), vulnerability management (exploited CVEs, time-to-patch).

**METRICS AND CONTINUOUS IMPROVEMENT**

Track SOC effectiveness. Key metrics: mean time to detect (MTTD <24 hours from initial compromise to alert), mean time to respond (MTTR <4 hours from alert to containment), alert volume (50-100 alerts per analyst per day sustainable), false positive rate (<20% of alerts are false positives), detection coverage (>80% of MITRE ATT&CK techniques covered), automation rate (>60% of tier-1 tasks automated).

Quality metrics: incident classification accuracy (% correctly triaged), escalation rate (% of tier-1 escalated to tier-2), repeat incidents (same root cause recurring), detection efficacy (% of true incidents detected vs missed). Improvement process: monthly detection review (which rules firing? false positives? gaps?), quarterly threat hunt (proactive search for undetected threats), annual purple team exercise (red team attack, measure detection), continuous tuning (adjust thresholds, add exclusions, retire ineffective rules).

Deliver SIEM implementation as:

1. **ARCHITECTURE DESIGN** - Platform selection, sizing, distributed architecture, retention tiers

2. **LOG COLLECTION PLAN** - Prioritized sources, collection methods, normalization strategy, filtering rules

3. **USE CASE LIBRARY** - Detection rules mapped to MITRE ATT&CK, correlation logic, thresholds, exclusions

4. **SOC PLAYBOOKS** - Response procedures per incident type, escalation criteria, stakeholder contacts

5. **SOAR AUTOMATION** - Playbook library, integration architecture, automation candidates

6. **DASHBOARD CATALOG** - Executive, operational, compliance, and threat intel dashboards

7. **METRICS FRAMEWORK** - KPI definitions, data sources, reporting cadence, improvement triggers

---

## Usage Examples

### Example 1: Enterprise Splunk Deployment
**Prompt:** Implement Splunk Enterprise Security for GlobalCorp with 8,000 endpoints, 500 servers, multi-cloud (AWS, Azure) achieving PCI-DSS and SOX compliance with 24x7 SOC.

**Expected Output:** Platform: Splunk Enterprise Security 7.2 with Premium Solutions (UBA, ITSI). Architecture: distributed—10 indexers (hot tier, 90 days), 3 search heads (clustered), 2 heavy forwarders (cloud log aggregation), SmartStore with S3 (warm/cold tiers 1 year/7 years). Sizing: 2 TB/day ingestion (60K EPS peak), 90 days hot retention on-prem, warm (1 year) and cold (7 years) in S3. Log sources: Windows Event Logs (8K endpoints via Universal Forwarder), Linux auditd/syslog (500 servers), Palo Alto firewalls (10 devices via syslog), AWS CloudTrail (50 accounts via EventBridge → HEC), Azure AD/Activity Logs (Sentinel connector), Okta (API), CrowdStrike Falcon (Event Stream API). Normalization: CIM compliance enforced (Authentication, Network Traffic, Endpoint data models), asset/identity enrichment from ServiceNow CMDB. Use cases: 150+ correlation searches including: failed authentication (>5 in 10 min), admin account creation, lateral movement (workstation-to-workstation SMB/RDP), AWS IAM privilege escalation, data exfiltration (upload >1GB in 5 min). MITRE coverage: 82% of techniques (mapped via Splunk Security Essentials). SOC: 15 analysts (5 per shift, 3 shifts 24x7), Tier 1 (alert triage), Tier 2 (investigation/response), Tier 3 (2 threat hunters). SOAR: Splunk SOAR (Phantom) with 50+ playbooks (phishing response, malware containment, user account lockout). Dashboards: executive (security posture, trends), SOC ops (alert queue, analyst workload), PCI/SOX compliance. Metrics: MTTD target <12h, MTTR <2h, automation rate 65% tier-1 tasks. Cost: $800K annual (licensing + infrastructure + S3 storage).

### Example 2: Microsoft Sentinel Cloud-Native
**Prompt:** Implement Microsoft Sentinel for CloudFirst with Azure/M365 workloads, hybrid AD, AWS integration achieving SOC 2 compliance with hybrid SOC (in-house + managed XDR).

**Expected Output:** Platform: Microsoft Sentinel (Azure-native SIEM) with Microsoft 365 Defender XDR integration. Architecture: two workspaces for data residency (US-East, EU-West), Sentinel analytics tier pricing, basic logs for high-volume low-value (Exchange audit). Sizing: 500 GB/day analytics tier, 90-day retention (analytics), 2-year basic logs (archive tier for compliance). Log sources: Azure resources (Activity Logs, NSG Flow, Key Vault), M365 (Exchange, SharePoint, Teams), Azure AD (sign-ins, audit), Defender for Endpoint (alerts, advanced hunting), AWS (CloudTrail via S3 connector), on-prem syslog (firewall, Linux servers via Log Analytics agent). Normalization: ASIM (Advanced Security Information Model) for consistent querying across sources. Use cases: 80+ analytics rules (Microsoft-provided + 50 custom KQL), including: impossible travel (Azure AD sign-in from geographically distant IPs within 4h), privilege escalation (PIM elevation, role assignment), ransomware behavior (Defender file extension changes + encryption), cloud data exfiltration (SharePoint mass download). Detection: Fusion ML engine (multi-stage attack detection), UEBA (user/entity behavior analytics). SOC: hybrid model—5 in-house analysts (business hours) + Microsoft Defender Experts (24x7 managed XDR for critical alerts). SOAR: Sentinel Playbooks (Logic Apps) with automation: IP enrichment (VirusTotal, AbuseIPDB), automatic incident assignment (based on Sentinel watchlist of asset owners), user response (prompt via Teams adaptive card—"was this you?"), automated containment (isolate device via Defender API, disable user via Azure AD). Dashboards: M365 security (phishing, malware, DLP), Azure workload security, identity threats (risky sign-ins, privilege escalation). Cost optimization: commitment tier ($100/day), basic logs for verbose sources (Exchange mailbox audit), filtering low-value events. Metrics: MTTD <18h, MTTR <3h (improved by XDR automation). Compliance: SOC 2 evidence collection (automated queries for access logs, change management).

### Example 3: Elastic Security for DevSecOps
**Prompt:** Implement Elastic Security for TechStartup with Kubernetes workloads, multi-cloud infrastructure achieving cost-effective security monitoring with DevSecOps integration.

**Expected Output:** Platform: Elastic Security 8.x (self-managed on Kubernetes via ECK operator). Architecture: 3-node Elasticsearch cluster (hot tier), ILM (Index Lifecycle Management) for tiering (30 days hot SSD, 90 days warm HDD), autoscaling based on ingestion load. Sizing: 1.5 TB/day, 50K EPS peak, 30-day hot retention, 90-day warm. Log sources: Kubernetes (audit logs, pod logs via Filebeat), Linux servers (auditd, syslog), cloud (AWS CloudTrail via Filebeat, GCP Cloud Logging), applications (structured JSON logs), network (Suricata IDS via Filebeat). Normalization: Elastic Common Schema (ECS) enforced at ingestion (ecs.version, @timestamp, host.name, user.name). Use cases: 60+ detection rules aligned to MITRE ATT&CK for cloud/containers including: privileged container execution (securityContext.privileged:true), container escape (mount /var/run/docker.sock), Kubernetes RBAC abuse (ClusterRoleBinding to cluster-admin), cloud credential access (AWS AssumeRole from unusual IP), lateral movement (kubectl exec into pods). Detection: Elastic detection engine with risk scoring, osquery integration (live endpoint queries for investigation), machine learning jobs (rare process execution, unusual network activity). SOC: DevSecOps model—3 detection engineers (develop/tune rules), on-call rotation (developers respond to their service alerts), security champions (embedded in dev teams). SOAR: TheHive (case management) + Cortex (analyzers for enrichment—VirusTotal, MISP) + Shuffle (workflow automation). Dashboards: Kibana dashboards for Kubernetes security (pod security policies, RBAC, network policies), cloud posture (IAM, public resources), application security (OWASP Top 10). Automation: Shuffle workflows—suspicious container → collect pod logs/network connections → submit to sandbox → create TheHive case → Slack notification. Cost: open-source core + Elastic Basic (free) + Elastic subscription ($50K/year for ML/detection rules). Metrics: MTTD <24h, MTTR <6h (developer self-service), detection coverage 70% of cloud-native ATT&CK matrix. Philosophy: shift-left security (developers see alerts in CI/CD), security as code (detection rules in Git).

---

## Cross-References

- [Security Operations](../Cybersecurity/security-operations.md) - SOC operational context and maturity
- [Incident Response](../Cybersecurity/incident-response.md) - Integration with IR processes
- [Threat Intelligence](../Cybersecurity/threat-intelligence.md) - Threat intel enrichment for detections
