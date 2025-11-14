---
title: "Threat Hunting Framework"
category: security
tags: [security, threat-hunting, detection, siem, threat-intelligence, security-operations]
description: "Comprehensive framework for proactive threat hunting including hypothesis-driven hunting, IOC-based detection, behavioral analysis, threat intelligence integration, and hunt methodology."
related_templates:
  - siem-security-monitoring.md
  - ../Cybersecurity/threat-intelligence.md
  - ../Cybersecurity/incident-response.md
  - vulnerability-management.md
  - ../Cybersecurity/threat-modeling.md
version: 2.0
last_updated: 2025-11-12
---

# Threat Hunting Framework

## Purpose
This framework provides a systematic approach to proactive threat hunting - actively searching for threats that evade existing security controls. It covers hunt methodologies, hypothesis development, data sources, hunting techniques, threat intelligence integration, and hunt operations management for identifying advanced threats before they cause damage.

## Quick Start

1. **Establish Hunt Foundation**: Define scope, identify data sources (SIEM, EDR, network), baseline normal behavior
2. **Develop Hunt Hypotheses**: Create testable hypotheses based on threat intelligence, attack frameworks (MITRE ATT&CK), and organizational risks
3. **Execute Hunt**: Query data sources, analyze anomalies, pivot on findings, document evidence
4. **Validate Findings**: Triage alerts, confirm true positives, escalate incidents, create detection rules
5. **Improve Defenses**: Create automated detections, update security controls, share intelligence, iterate

---

## Minimal Example

**SCENARIO**: A security team wants to start threat hunting to find threats that bypassed existing defenses.

**Hunt Hypothesis**: "Attackers may be using living-off-the-land binaries (LOLBins) like PowerShell to evade AV detection."

**Hunt Process**:
```
1. Data Source: Windows Event Logs (EventID 4104 - PowerShell Script Block Logging)

2. Hunt Query (Splunk):
   index=windows EventCode=4104
   | search ScriptBlockText="*DownloadString*" OR ScriptBlockText="*IEX*" OR ScriptBlockText="*Invoke-Expression*"
   | stats count by ComputerName, User, ScriptBlockText
   | where count > 5

3. Findings:
   - 3 workstations running obfuscated PowerShell commands
   - Commands downloading files from suspicious external IPs
   - Execution happening outside business hours

4. Validation:
   - TRUE POSITIVE: Credential harvesting malware
   - Incident escalated to IR team

5. Detection Rule Created:
   - SIEM alert for suspicious PowerShell usage
   - EDR behavior rule for encoded PowerShell commands

6. Result: Prevented data exfiltration, created automated detection
```

**Outcome**: Found threat that evaded AV, created detection rule, prevented broader compromise.

---

## Comprehensive Framework

### PHASE 1: Threat Hunt Foundation

#### 1.1 Hunt Team Structure

**Roles & Responsibilities**:
```yaml
hunt_team:
  hunt_lead:
    - responsibilities: [hypothesis_development, hunt_planning, stakeholder_communication]
    - skills: [threat_intelligence, attack_frameworks, data_analysis]
    - experience: senior_security_analyst_5plus_years

  threat_hunters:
    - responsibilities: [query_development, data_analysis, investigation]
    - skills: [siem_queries, log_analysis, network_analysis, malware_analysis]
    - experience: security_analyst_2plus_years
    - team_size: 2-5_hunters

  detection_engineer:
    - responsibilities: [detection_rule_creation, tuning, automation]
    - skills: [siem_rules, yara, sigma, automation]
    - experience: 3plus_years

  threat_intelligence_analyst:
    - responsibilities: [threat_intel_feeds, ioc_management, ttp_analysis]
    - skills: [threat_intel_platforms, osint, adversary_tracking]
    - experience: 2plus_years
```

#### 1.2 Data Sources

**Essential Data Sources**:

| Source | Data Type | Hunt Value | Retention |
|--------|-----------|------------|-----------|
| **SIEM** | Aggregated logs | High - Central repository | 90 days - 1 year |
| **EDR** | Endpoint telemetry | Critical - Process, network, file events | 30-90 days |
| **Network (NSM)** | PCAP, NetFlow | High - Network behavior, C2 detection | 7-30 days |
| **DNS Logs** | DNS queries | High - C2, exfiltration, malware | 90 days |
| **Firewall** | Traffic logs | Medium - Perimeter activity | 90 days |
| **Proxy** | Web traffic | Medium - Web-based attacks | 90 days |
| **Cloud Logs** | AWS CloudTrail, Azure Activity | High - Cloud security events | 90 days - 1 year |
| **Email Gateway** | Email metadata, attachments | Medium - Phishing detection | 30-90 days |

**Data Ingestion**:
```python
# Example: Ingest data sources into hunt platform
hunt_data_sources = {
    'siem': {
        'platform': 'Splunk',
        'indices': ['windows', 'linux', 'network', 'cloud'],
        'retention': '1 year'
    },
    'edr': {
        'platform': 'CrowdStrike Falcon',
        'api': 'https://api.crowdstrike.com',
        'data_types': ['processes', 'network_connections', 'file_writes', 'registry']
    },
    'network': {
        'platform': 'Zeek (NSM)',
        'data_types': ['conn.log', 'dns.log', 'http.log', 'ssl.log', 'files.log']
    },
    'threat_intel': {
        'feeds': ['abuse.ch', 'alienvault_otx', 'misp', 'commercial_feed'],
        'ioc_types': ['ip', 'domain', 'hash', 'url']
    }
}
```

#### 1.3 Baseline Normal Behavior

**Establish Baselines**:
```sql
-- Example: Baseline normal authentication patterns
SELECT
    user,
    COUNT(DISTINCT computer) as unique_computers,
    COUNT(*) as total_logins,
    HOUR(timestamp) as hour_of_day
FROM windows_security_logs
WHERE event_id = 4624  -- Successful login
    AND timestamp >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY user, HOUR(timestamp)

-- Identify outliers (users logging in from unusual locations/times)
-- Hunt for anomalies: logins from 10+ unique computers, logins at 3 AM, etc.
```

**Normal Behavior Profiles**:
- Typical login times (8 AM - 6 PM for most users)
- Standard software execution (Office apps, browsers)
- Network traffic patterns (internal vs. external)
- Administrative activity (patching windows, scheduled tasks)
- Data transfer volumes (baseline file share access)

---

### PHASE 2: Hunt Methodologies

#### 2.1 Hypothesis-Driven Hunting

**Hunt Hypothesis Framework**:
```
Hypothesis Template:
"Given [threat intelligence/attack technique],
adversaries may be [specific activity],
which would appear as [observable indicators],
in [data sources]."

Example:
"Given recent APT29 campaigns targeting government organizations,
adversaries may be using WMI for persistence and lateral movement,
which would appear as unusual WMI process creation and network connections,
in Windows Event Logs (EventID 5857, 5860, 5861) and EDR process telemetry."
```

**Hypothesis Sources**:
1. **Threat Intelligence**: Recent campaigns, TTPs, IOCs from threat reports
2. **MITRE ATT&CK**: Specific techniques (T1055 Process Injection, T1059 Command and Scripting)
3. **Incident Trends**: Patterns from recent incidents in your org or industry
4. **Red Team Findings**: Techniques used successfully by your red team
5. **Security Gaps**: Known blind spots in detection coverage

**Example Hypotheses**:
```yaml
hunt_hypotheses:
  - hypothesis_id: H001
    title: "PowerShell-based credential dumping"
    description: "Attackers using Mimikatz via PowerShell to dump credentials"
    mitre_technique: T1003.001
    data_sources: [windows_event_logs, edr, powershell_logs]
    expected_indicators:
      - powershell.exe spawning unusual child processes
      - access to lsass.exe memory
      - suspicious module loads (sekurlsa, kerberos)

  - hypothesis_id: H002
    title: "DNS tunneling for C2"
    description: "Adversaries using DNS queries for command and control"
    mitre_technique: T1071.004
    data_sources: [dns_logs, network_traffic]
    expected_indicators:
      - high volume of DNS queries to single domain
      - unusually long DNS query strings
      - queries to newly registered domains

  - hypothesis_id: H003
    title: "Living-off-the-land lateral movement"
    description: "Using PsExec, WMI, or RDP for lateral movement"
    mitre_technique: T1021
    data_sources: [windows_event_logs, network_logs, edr]
    expected_indicators:
      - service creation on remote systems
      - WMI process creation from network connections
      - RDP connections between workstations
```

#### 2.2 IOC-Based Hunting

**Indicator of Compromise (IOC) Hunt**:
```python
# Example: Hunt for known malicious IPs from threat intel feed
malicious_ips = [
    '192.0.2.1',
    '198.51.100.5',
    '203.0.113.10'
]

# Splunk query
splunk_query = f'''
index=firewall OR index=proxy OR index=dns
| search dest_ip IN ({",".join(malicious_ips)})
| stats count by src_ip, dest_ip, dest_port, action
| where count > 0
'''

# Expected findings: Any connection attempts to malicious IPs
# Action: Investigate source systems, check for compromise
```

**IOC Types**:
- **IP Addresses**: Known C2 servers, malicious infrastructure
- **Domains**: Malware download sites, phishing domains
- **File Hashes**: Malware samples (MD5, SHA1, SHA256)
- **URLs**: Phishing URLs, exploit kit landing pages
- **YARA Rules**: Malware signatures based on code patterns
- **Email Addresses**: Phishing sender addresses

**Threat Intelligence Platforms**:
```yaml
threat_intel_sources:
  free:
    - abuse_ch: "https://abuse.ch (Malware hashes, IPs, URLs)"
    - alienvault_otx: "Open Threat Exchange"
    - misp: "Malware Information Sharing Platform"
    - threatfox: "IOC database"

  commercial:
    - recorded_future: "Comprehensive threat intel"
    - anomali: "ThreatStream platform"
    - crowdstrike_intel: "Adversary intelligence"
    - mandiant_intel: "APT tracking"

  integration:
    - siem_feeds: "Ingest IOCs into SIEM for automated hunting"
    - edr_feeds: "Push IOCs to EDR for behavioral detection"
    - firewall_feeds: "Block malicious IPs at perimeter"
```

#### 2.3 Behavioral Analytics Hunting

**Anomaly Detection**:
```python
# Example: Detect unusual process execution
# Query: Processes that are rarely executed company-wide

import pandas as pd
from scipy import stats

# Get process execution frequency
process_freq = df.groupby('process_name').size()

# Calculate z-scores (identify rare processes)
z_scores = stats.zscore(process_freq)

# Flag processes with z-score < -2 (significantly rare)
rare_processes = process_freq[z_scores < -2]

# Hunt for these rare processes
for process in rare_processes.index:
    print(f"Rare process: {process}")
    # Investigate: Is this legitimate? Malware? LOLBin abuse?
```

**Behavioral Hunt Patterns**:
```yaml
behavioral_hunts:
  - pattern: "Unusual network beaconing"
    technique: "C2 communication detection"
    query: |
      # Regular, consistent network connections (beaconing behavior)
      SELECT src_ip, dest_ip, dest_port,
             COUNT(*) as connection_count,
             STDDEV(TIMESTAMPDIFF(SECOND, @prev_timestamp, timestamp)) as time_variance
      FROM network_connections
      GROUP BY src_ip, dest_ip, dest_port
      HAVING connection_count > 100 AND time_variance < 5  # Consistent timing

  - pattern: "Data staging"
    technique: "Pre-exfiltration activity"
    query: |
      # Unusual data aggregation (copying many files to single location)
      SELECT user, dest_folder, COUNT(*) as files_copied, SUM(file_size) as total_size
      FROM file_operations
      WHERE operation = 'copy' OR operation = 'move'
      GROUP BY user, dest_folder
      HAVING files_copied > 1000 OR total_size > 10GB

  - pattern: "Privilege escalation attempts"
    technique: "Detect elevation attempts"
    query: |
      # Failed privilege escalation followed by success
      SELECT user, computer, COUNT(*) as failed_attempts
      FROM security_logs
      WHERE event_id = 4673  # Privilege use failure
      GROUP BY user, computer
      HAVING failed_attempts > 5
```

---

### PHASE 3: Hunt Execution

#### 3.1 Hunt Process

**Hunt Workflow**:
```
1. SELECT HYPOTHESIS
   ↓
2. IDENTIFY DATA SOURCES
   ↓
3. DEVELOP QUERIES
   ↓
4. EXECUTE HUNT
   ↓
5. ANALYZE RESULTS
   ↓
6. PIVOT & INVESTIGATE
   ↓
7. VALIDATE FINDINGS
   ↓
8. CREATE DETECTIONS
   ↓
9. DOCUMENT & SHARE
```

**Hunt Execution Example** (PowerShell Credential Dumping):
```markdown
## Hunt: PowerShell Credential Dumping

### Hypothesis:
Attackers may be using PowerShell to execute Mimikatz for credential dumping.

### MITRE ATT&CK:
- T1003.001: OS Credential Dumping (LSASS Memory)
- T1059.001: PowerShell

### Data Sources:
- Windows Event Logs (PowerShell Script Block Logging - EventID 4104)
- EDR process telemetry
- Memory dumps (if available)

### Hunt Queries:

**Query 1: Suspicious PowerShell keywords**
```splunk
index=windows EventCode=4104
| search ScriptBlockText="*mimikatz*" OR ScriptBlockText="*sekurlsa*" OR ScriptBlockText="*lsadump*"
| table _time, ComputerName, User, ScriptBlockText
```

**Query 2: PowerShell accessing LSASS**
```splunk
index=edr process_name="powershell.exe"
| search target_process="lsass.exe" AND access_type="read_memory"
| table _time, computer, user, command_line, parent_process
```

**Query 3: Encoded PowerShell commands**
```splunk
index=windows EventCode=4104
| regex ScriptBlockText="(?i)-enc(oded)?command"
| eval decoded_command=base64decode(ScriptBlockText)
| table _time, ComputerName, User, decoded_command
```

### Results:
- Found 2 instances of encoded PowerShell commands
- Both executed "Invoke-Mimikatz" module
- Targeted domain controllers (high-value targets)

### Pivot Investigations:
- Check user account used: "svc-backup" (service account)
- Investigate process parent: "explorer.exe" (unusual, should be from scheduled task)
- Network connections: Outbound SMB to file server (exfiltration?)
- Timeline: Executed at 2:47 AM (outside business hours)

### Validation:
✅ TRUE POSITIVE - Credential dumping attack
- Escalate to incident response team
- Isolate affected systems
- Reset compromised credentials

### Detection Rule Created:
```yaml
rule:
  name: "PowerShell Credential Dumping"
  severity: CRITICAL
  condition: |
    EventCode=4104 AND
    (ScriptBlockText contains "mimikatz" OR
     ScriptBlockText contains "sekurlsa" OR
     ScriptBlockText contains "lsadump" OR
     process accesses lsass.exe memory)
  action: alert_and_isolate
```
```

#### 3.2 Hunting Tools & Platforms

**Hunt Platforms**:
```yaml
hunt_tools:
  siem:
    - splunk: "Market leader, powerful SPL query language"
    - elastic_ecs: "Open source, flexible"
    - azure_sentinel: "Cloud-native, integrated with Microsoft"

  edr:
    - crowdstrike_falcon: "Excellent hunt capabilities, API access"
    - microsoft_defender: "Integrated with Windows, KQL queries"
    - sentinelone: "Deep visibility, automated response"

  network:
    - zeek: "Open source network security monitor"
    - suricata: "IDS/IPS with lua scripting"
    - moloch: "PCAP capture and search"

  threat_hunting_specific:
    - velociraptor: "Endpoint visibility, fast collection"
    - osquery: "SQL-based endpoint queries"
    - graylog: "Log management and hunting"

  automation:
    - jupyter_notebooks: "Document hunts, share queries"
    - soar_platforms: "Automate hunt workflows"
    - custom_scripts: "Python, PowerShell for automation"
```

**Example: Velociraptor Hunt**:
```sql
-- Hunt for unusual scheduled tasks across all endpoints
SELECT * FROM Artifact.Windows.System.TaskScheduler()
WHERE
  -- Exclude known good tasks
  Name NOT IN ('Microsoft\\Windows\\UpdateOrchestrator', 'GoogleUpdateTaskMachine')
  AND
  -- Look for suspicious characteristics
  (Command LIKE '%powershell%' OR
   Command LIKE '%wscript%' OR
   Command LIKE '%cscript%' OR
   UserAccount = 'SYSTEM')
ORDER BY CreationTime DESC
```

#### 3.3 Hunt Documentation

**Hunt Report Template**:
```markdown
# Threat Hunt Report

## Hunt Metadata
- **Hunt ID**: TH-2025-001
- **Date**: 2025-01-15
- **Hunter**: John Doe
- **Status**: Completed

## Hypothesis
Adversaries may be using WMI for lateral movement and persistence.

## MITRE ATT&CK Mapping
- T1047: Windows Management Instrumentation
- T1021: Remote Services

## Data Sources
- Windows Event Logs (WMI Activity - EventID 5857, 5860, 5861)
- EDR process telemetry
- Network traffic logs

## Hunt Queries
[Include all queries used]

## Findings
- **Total Events Analyzed**: 1,234,567
- **Anomalies Identified**: 45
- **True Positives**: 2
- **False Positives**: 43

### True Positive Details:
1. **TP-001**: WMI-based persistence on DC01
   - Attacker created WMI event subscription
   - Executed malicious PowerShell script every 30 minutes
   - Escalated to incident response

2. **TP-002**: Lateral movement via WMI
   - Attacker used WMI to execute commands on 5 workstations
   - Credential harvesting detected
   - Escalated to incident response

## Detection Rules Created
- Rule-001: WMI Event Subscription Creation
- Rule-002: WMI Process Execution from Network

## Recommendations
1. Enable WMI logging on all systems
2. Restrict WMI access to privileged users only
3. Monitor WMI event subscriptions regularly

## Lessons Learned
- WMI logging was incomplete on some systems
- Need better baseline of legitimate WMI usage
- Consider blocking WMI lateral movement via firewall rules

## Next Hunt
Investigate potential use of BITS for persistence (similar technique)
```

---

### PHASE 4: Detection Engineering

#### 4.1 From Hunt to Detection

**Detection Rule Development**:
```yaml
# Sigma rule example (universal detection format)
title: Suspicious PowerShell Credential Access
id: 12345678-1234-1234-1234-123456789012
status: experimental
description: Detects PowerShell commands attempting to access credentials
references:
  - https://attack.mitre.org/techniques/T1003/
author: Threat Hunt Team
date: 2025/01/15
logsource:
  product: windows
  service: powershell
  definition: 'Requires PowerShell Script Block Logging (Event ID 4104)'
detection:
  selection:
    EventID: 4104
  keywords:
    - '*mimikatz*'
    - '*Invoke-Mimikatz*'
    - '*sekurlsa*'
    - '*lsadump*'
    - '*DumpCreds*'
  condition: selection and keywords
falsepositives:
  - Legitimate penetration testing (if authorized)
  - Security tools testing
level: critical
tags:
  - attack.credential_access
  - attack.t1003.001
```

**YARA Rule for Malware Hunt**:
```yara
rule APT_Mimikatz_PowerShell
{
    meta:
        description = "Detects PowerShell Mimikatz in memory or scripts"
        author = "Threat Hunt Team"
        date = "2025-01-15"
        reference = "Hunt TH-2025-001"

    strings:
        $str1 = "Invoke-Mimikatz" ascii wide
        $str2 = "sekurlsa::logonpasswords" ascii wide
        $str3 = "lsadump::sam" ascii wide
        $str4 = "kerberos::golden" ascii wide

    condition:
        any of ($str*)
}
```

#### 4.2 Detection Tuning

**Reduce False Positives**:
```python
# Example: Tune detection for unusual authentication patterns
# Initial rule: Alert on any login from unusual location

# Tuning approach:
# 1. Collect data for 30 days
# 2. Build whitelist of legitimate unusual locations (VPN, remote offices)
# 3. Adjust threshold (require multiple failed attempts before alert)

tuned_detection = {
    'rule': 'Unusual Authentication Location',
    'original': {
        'condition': 'login from IP not in last 90 days',
        'false_positive_rate': '15%'
    },
    'tuned': {
        'condition': '''
            login from IP not in last 90 days AND
            IP not in whitelist (VPN ranges, known offices) AND
            (failed_attempts > 3 OR successful_after_failures)
        ''',
        'false_positive_rate': '2%'
    },
    'whitelist': [
        '10.0.0.0/8',      # Internal network
        '203.0.113.0/24',  # VPN range
        '198.51.100.0/24'  # Remote office
    ]
}
```

---

### PHASE 5: Hunt Operations

#### 5.1 Hunt Cadence

**Hunt Schedule**:
```yaml
hunt_calendar:
  daily:
    - ioc_sweeps: "Check new threat intel IOCs against historical data"
    - anomaly_review: "Review SIEM/EDR anomaly alerts"

  weekly:
    - hypothesis_hunt: "Execute 1-2 hypothesis-driven hunts"
    - detection_tuning: "Review and tune existing detection rules"

  monthly:
    - comprehensive_hunt: "Deep dive hunt (APT techniques, insider threats)"
    - metrics_review: "Review hunt metrics, adjust priorities"

  quarterly:
    - red_team_debrief: "Hunt for red team TTPs that succeeded"
    - threat_landscape_review: "Update hunt priorities based on threat intel"

  annually:
    - program_assessment: "Assess hunt program effectiveness"
    - training_update: "Update hunter training, new tools/techniques"
```

#### 5.2 Hunt Metrics

**Key Performance Indicators**:
```yaml
hunt_kpis:
  effectiveness:
    - true_positives_found: "Number of real threats discovered"
    - mean_time_to_detect: "How long threats went undetected"
    - detection_coverage: "% of MITRE ATT&CK techniques covered"

  efficiency:
    - hunts_per_week: "Hunt velocity"
    - time_per_hunt: "Average hunt duration"
    - false_positive_rate: "% of findings that are false positives"

  impact:
    - detection_rules_created: "New automated detections from hunts"
    - incidents_prevented: "Threats stopped before impact"
    - security_gaps_identified: "Blind spots discovered"

  maturity:
    - hunt_hypothesis_sources: "Diversity of hunt ideas"
    - data_source_coverage: "% of environment with visibility"
    - hunter_skill_development: "Training, certifications"
```

**Hunt Effectiveness Dashboard**:
```
Monthly Hunt Metrics (January 2025)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hunts Executed:           12
True Positives Found:      3
False Positives:          18
Detection Rules Created:   4
MITRE Coverage:           45% (65/144 techniques)
Mean Time to Detect:      12 days (↓ from 18 days)
Hunt Time (avg):          4.5 hours

Top Hunt Findings:
1. Credential dumping (2 instances)
2. DNS tunneling C2 (1 instance)

Gaps Identified:
- Low visibility into MacOS endpoints
- No monitoring of cloud API calls
```

---

## Variables Table

| Variable | Description | Example Values | Notes |
|----------|-------------|----------------|-------|
| `{HUNT_FREQUENCY}` | How often to hunt | Daily, Weekly, Monthly | Based on team size |
| `{DATA_SOURCE}` | Primary hunt data | SIEM, EDR, Network, Cloud | More sources = better |
| `{HUNT_HYPOTHESIS}` | Hunt focus | PowerShell abuse, DNS tunneling, Lateral movement | MITRE ATT&CK based |
| `{THREAT_INTEL_FEED}` | IOC source | AlienVault OTX, MISP, Commercial | Free vs paid |
| `{HUNT_PLATFORM}` | Hunt tool | Splunk, Elastic, Sentinel, Velociraptor | Based on budget |
| `{MITRE_TECHNIQUE}` | ATT&CK technique | T1003, T1059, T1021 | Prioritize common |
| `{HUNT_DURATION}` | Time per hunt | 2-8 hours | Complexity dependent |
| `{DETECTION_RULE_FORMAT}` | Rule type | Sigma, YARA, Snort, Custom | Platform specific |
| `{FALSE_POSITIVE_THRESHOLD}` | Acceptable FP rate | <5%, <10%, <20% | Balance coverage vs noise |
| `{RETENTION}` | Data retention | 30 days, 90 days, 1 year | Cost vs visibility |
| `{HUNT_TEAM_SIZE}` | Number of hunters | 1-2, 3-5, 6-10 | Org size dependent |
| `{AUTOMATION_LEVEL}` | Hunt automation | Manual, Semi-automated, Fully automated | Maturity level |

---

## Usage Examples

### Example 1: Small Company (1 Hunter, Limited Budget)

**Context**: 200-employee company, 1 security analyst, limited tools (free/low-cost).

**Hunt Setup**:
```yaml
tools:
  - siem: elastic_stack (free)
  - edr: microsoft_defender (included_in_m365)
  - threat_intel: abuse_ch, alienvault_otx (free)
  - hunt_automation: python_scripts, jupyter_notebooks (free)

data_sources:
  - windows_event_logs
  - microsoft_defender_alerts
  - firewall_logs
  - dns_logs

hunt_cadence:
  weekly: 1_hypothesis_hunt (4_hours)
  daily: ioc_sweep (30_minutes)
```

**Weekly Hunt Example**:
```markdown
Hunt: Unusual PowerShell Activity
Time: 4 hours

1. Hypothesis: Attackers using PowerShell for malware delivery
2. Query (KQL in Microsoft Defender):
   DeviceProcessEvents
   | where FileName == "powershell.exe"
   | where ProcessCommandLine has_any ("DownloadString", "IEX", "-enc")
   | summarize count() by DeviceName, AccountName, ProcessCommandLine

3. Results: 2 suspicious instances found
4. Investigation: 1 false positive (admin script), 1 true positive (malware)
5. Response: Isolate infected device, incident response
6. Detection: Created alert for encoded PowerShell commands
```

**Results**:
- 1 threat found per month (average)
- 4 detection rules created (first quarter)
- Prevented ransomware attack (caught during delivery phase)

### Example 2: Enterprise SOC (Dedicated Hunt Team)

**Context**: Enterprise with 10,000 employees, dedicated 5-person hunt team, full tooling.

**Hunt Team**:
```yaml
team_structure:
  hunt_lead: 1
  senior_hunters: 2
  junior_hunters: 2
  detection_engineer: 1 (shared with SOC)

tools:
  - siem: splunk_enterprise
  - edr: crowdstrike_falcon
  - network: zeek, suricata
  - threat_intel: recorded_future, misp
  - hunt_platform: jupyter_enterprise_gateway
  - automation: soar_platform (phantom)

budget: $500k_annually
```

**Hunt Program**:
```yaml
hunt_types:
  hypothesis_driven:
    frequency: 3-5_per_week
    duration: 4-8_hours_each
    source: mitre_attack, threat_intel, red_team

  ioc_based:
    frequency: daily
    duration: automated_with_review
    source: threat_intel_feeds

  behavioral:
    frequency: 2_per_month
    duration: 2-3_days_each
    technique: ml_anomaly_detection, behavioral_analytics

  campaign_focused:
    frequency: as_needed
    trigger: new_apt_campaign, critical_vulnerability
    duration: multi-day_intensive_hunt
```

**Advanced Hunt Example** (APT Campaign):
```markdown
Hunt: APT29 (Nobelium) TTPs in Environment

Duration: 3 days
Team: 3 hunters + threat intel analyst

Day 1: Intelligence Gathering
- Reviewed Microsoft, FireEye, CrowdStrike reports on APT29
- Mapped TTPs to MITRE ATT&CK
- Identified 15 techniques to hunt for

Day 2: Execution
- Hunt 1: Malicious OAuth applications (T1528)
  - Query: Azure AD app consent grants
  - Found: 2 suspicious applications (delegated permissions)

- Hunt 2: SAML token abuse (T1606.002)
  - Query: Azure AD SAML token issuance
  - Found: 1 anomalous token for external user

- Hunt 3: Mailbox rule forwarding (T1114.003)
  - Query: Exchange mailbox rules with external forwards
  - Found: 3 rules forwarding to external addresses

Day 3: Investigation & Response
- Validated findings: 2 true positives (compromised OAuth apps)
- Incident response: Revoked apps, reset user credentials
- Detection: Created SIEM rules for OAuth abuse

Results:
- Discovered active APT29 compromise (early stage)
- Prevented data exfiltration
- 6 detection rules created
- Shared IOCs with ISAC
```

**Program Results** (Annually):
- 200+ hunts executed
- 25 true positive threats found
- 150+ detection rules created
- 75% MITRE ATT&CK coverage
- Mean time to detect: 8 days (industry avg: 24 days)

### Example 3: Financial Services (Highly Regulated)

**Context**: Bank with strict compliance requirements, insider threat focus.

**Hunt Focus Areas**:
```yaml
compliance_driven_hunts:
  - insider_threats: "Malicious insiders, data exfiltration"
  - fraud: "Account takeover, wire fraud"
  - aml: "Money laundering detection"
  - pci_dss: "Cardholder data access monitoring"

hunt_triggers:
  - employee_termination: "Hunt for data staging before exit"
  - privileged_access_change: "Hunt for privilege abuse"
  - large_transactions: "Hunt for fraud indicators"
  - failed_audits: "Hunt for evidence of non-compliance"
```

**Insider Threat Hunt Example**:
```markdown
Hunt: Departing Employee Data Exfiltration

Trigger: VP of Sales resigned (2-week notice)

Hunt Activities:
1. Baseline normal behavior:
   - Typical file access: 50 files/day
   - Data transfer: 100 MB/day
   - Work hours: 8 AM - 6 PM

2. Monitor for anomalies:
   - File access spiked to 500 files/day
   - Data copied to USB drive (DLP alert)
   - Activity at 11 PM (outside normal hours)

3. Findings:
   - Employee copied customer list to personal USB
   - Uploaded files to personal cloud storage
   - Accessed competitor's website (likely next employer)

4. Response:
   - Disabled account immediately
   - Retrieved USB drive (HR/Legal)
   - Notified legal team (potential theft of trade secrets)
   - Forensic image of laptop

5. Outcome:
   - Legal action initiated
   - Customer list recovered
   - Enhanced DLP policies implemented
```

**Compliance Value**:
- Demonstrated proactive monitoring (regulators, auditors)
- Protected customer data (PCI-DSS, GDPR)
- Evidence for legal proceedings
- Improved insider threat program

---

## Best Practices

### Hunt Methodology
- **Hypothesis-Driven**: Start with specific, testable hypotheses
- **MITRE ATT&CK**: Use framework to guide hunts and measure coverage
- **Document Everything**: Detailed hunt documentation enables knowledge sharing
- **Iterate**: Failed hunts are learning opportunities, refine and retry
- **Think Like Adversary**: Understand attacker TTPs, motivations

### Data & Tools
- **Visibility First**: Can't hunt what you can't see - prioritize data collection
- **Log Retention**: Longer retention = ability to hunt historical compromises
- **Baseline Normal**: Understanding normal behavior is critical to finding anomalies
- **Automate**: Automate repetitive hunts, focus hunters on complex investigations
- **Use Right Tool**: SIEM for broad searches, EDR for endpoint detail, NSM for network

### Team & Operations
- **Continuous Learning**: Hunters must stay current on threats, tools, techniques
- **Threat Intel**: Integrate threat intelligence to focus hunts
- **Collaboration**: Share findings with SOC, IR, Threat Intel teams
- **Create Detections**: Every hunt should result in automated detection
- **Measure Impact**: Track metrics to demonstrate value

### Detection Engineering
- **Hunt → Detect → Automate**: Transform successful hunts into automated detections
- **Tune Relentlessly**: Low false positive rate is critical for SOC adoption
- **Use Standards**: Sigma, YARA for portable, shareable detection rules
- **Test Detections**: Red team validation of new detection rules
- **Continuous Improvement**: Regularly review and update detection logic

---

## Common Pitfalls

### Methodology Errors
- **Fishing Expeditions**: Hunting without hypothesis wastes time
- **Confirmation Bias**: Looking only for expected results, missing actual threats
- **Analysis Paralysis**: Over-analyzing data without taking action
- **Poor Documentation**: Can't reproduce hunt or share findings
- **No Follow-Through**: Finding threats but not creating detections

### Technical Mistakes
- **Insufficient Data**: Limited visibility prevents effective hunting
- **Wrong Tool**: Using SIEM when EDR would be better (or vice versa)
- **Query Errors**: Poorly written queries miss threats or generate too many results
- **No Baseline**: Don't know normal, can't identify abnormal
- **Ignoring Context**: Raw data without context leads to false conclusions

### Operational Issues
- **Inconsistent Hunting**: Ad hoc hunting vs. systematic program
- **No Prioritization**: Hunting low-risk areas instead of high-value targets
- **Siloed Operations**: Hunt team not integrated with SOC/IR
- **Alert Fatigue**: Creating too many detections, SOC overwhelmed
- **No Metrics**: Can't demonstrate value without measuring results

### Team Challenges
- **Skill Gaps**: Hunters without necessary technical skills
- **Burnout**: Hunting is intensive, need rotation and breaks
- **No Training**: Not investing in hunter skill development
- **Communication Gaps**: Not sharing findings effectively
- **Tool Dependency**: Over-reliance on tools vs. critical thinking

---

## Related Templates

- **siem-security-monitoring.md**: SIEM implementation and monitoring
- **../Cybersecurity/threat-intelligence.md**: Threat intelligence program
- **../Cybersecurity/incident-response.md**: Incident response procedures
- **vulnerability-management.md**: Vulnerability management lifecycle
- **../Cybersecurity/threat-modeling.md**: Threat modeling methodologies

---

## Additional Resources

**Threat Hunting Resources**:
- MITRE ATT&CK: https://attack.mitre.org/
- Cyber Kill Chain: Lockheed Martin framework
- Diamond Model: Threat intelligence analysis
- TaHiTI (Threat Hunting Methodology): https://www.betaalvereniging.nl/tahiti/

**Training & Certifications**:
- SANS SEC555: SIEM with Tactical Analytics
- SANS FOR508: Advanced Incident Response
- GIAC GCFA: Forensic Analyst
- eLearnSecurity eCTHP: Certified Threat Hunting Professional

**Tools & Platforms**:
- Velociraptor: https://docs.velociraptor.app/
- OSQuery: https://osquery.io/
- Zeek (Bro): https://zeek.org/
- Sigma: https://github.com/SigmaHQ/sigma

**Threat Intelligence**:
- AlienVault OTX: https://otx.alienvault.com/
- MISP Project: https://www.misp-project.org/
- Abuse.ch: https://abuse.ch/
- VirusTotal: https://www.virustotal.com/

**Community**:
- ThreatHunter-Playbook: https://github.com/OTRF/ThreatHunter-Playbook
- Awesome Threat Intelligence: https://github.com/hslatman/awesome-threat-intelligence
- Hunting with Splunk: Splunk Boss of the SOC datasets

---

*This framework provides comprehensive guidance for building and operating a threat hunting program. Threat hunting is proactive defense - finding threats that evaded existing controls before they cause damage. Success requires visibility (data), methodology (hypothesis-driven hunting), and skills (trained hunters). Remember: You can't hunt what you can't see - prioritize visibility and data collection first.*
