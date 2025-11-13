---
title: "Ransomware Defense & Recovery Framework"
category: security
tags: [security, ransomware, incident-response, backup-recovery, threat-prevention, cybersecurity]
description: "Comprehensive framework for preventing, detecting, and recovering from ransomware attacks including defense-in-depth strategies, backup systems, incident response, and business continuity planning."
related_templates:
  - ../Cybersecurity/incident-response.md
  - ../Cybersecurity/security-architecture.md
  - ../Security-Operations/siem-security-monitoring.md
  - ../Compliance-Governance/data-security-strategy.md
  - ../Application-Security/web-application-security.md
version: 2.0
last_updated: 2025-11-12
---

# Ransomware Defense & Recovery Framework

## Purpose
This framework provides comprehensive guidance for defending against and recovering from ransomware attacks. It covers prevention strategies, detection mechanisms, backup and recovery systems, incident response procedures, and business continuity planning to minimize impact and enable rapid recovery from ransomware incidents.

## Quick Start

1. **Implement Defense-in-Depth**: Deploy multiple layers of security (email security, endpoint protection, network segmentation, access controls)
2. **Establish Robust Backups**: Implement 3-2-1 backup strategy with immutable/offline backups, test recovery regularly
3. **Deploy Detection Systems**: Enable EDR/XDR, SIEM alerting, behavioral analysis for early ransomware detection
4. **Prepare Incident Response**: Document ransomware-specific response procedures, define decision criteria (pay vs. recover)
5. **Test & Train**: Conduct ransomware simulations, train employees on phishing, test backup recovery quarterly

---

## Minimal Example

**SCENARIO**: A mid-size company needs basic ransomware protection without a large security budget.

**Prevention (Defense Layers)**:
- **Email Security**: Microsoft Defender or Proofpoint (block malicious attachments, phishing links)
- **Endpoint Protection**: Windows Defender or CrowdStrike (signature + behavioral detection)
- **Patch Management**: Automated patching for OS and applications (monthly cycle)
- **Access Controls**: MFA for all users, least privilege, disable RDP from internet
- **Network Segmentation**: Separate production from corporate network

**Backup Strategy (3-2-1 Rule)**:
- **3 copies**: Primary data + 2 backups
- **2 media types**: Local NAS + Cloud (AWS S3)
- **1 offsite**: Cloud backup geographically separate
- **Immutability**: S3 Object Lock (cannot be deleted for 30 days)
- **Testing**: Monthly restore tests of critical systems

**Detection**:
- **EDR**: CrowdStrike Falcon or Microsoft Defender for Endpoint
- **SIEM**: Splunk or ELK Stack for centralized logging
- **Alerts**: File encryption activity, mass file deletions, suspicious processes

**Incident Response Plan**:
```
1. Detect: EDR alert on encryption activity
2. Isolate: Disconnect infected systems from network immediately
3. Assess: Determine scope (how many systems affected?)
4. Recover: Restore from immutable backups (don't pay ransom)
5. Investigate: Root cause analysis, patch vulnerabilities
```

**Result**: Multi-layered defense with tested recovery capability, <4 hour RTO for critical systems.

---

## Comprehensive Framework

### PHASE 1: Ransomware Prevention

#### 1.1 Email Security (Primary Attack Vector)

**Email Gateway Security**:
- **Spam Filtering**: Block known malicious senders and domains
- **Attachment Filtering**: Block executables (.exe, .scr, .vbs, .js, .bat, .cmd)
- **Link Protection**: Sandbox/rewrite URLs, check against threat intelligence
- **Impersonation Protection**: Detect CEO fraud, domain spoofing (DMARC/DKIM/SPF)
- **Attachment Sandboxing**: Detonate suspicious files in sandbox before delivery

**Email Security Solutions**:
| Solution | Type | Strengths | Cost |
|----------|------|-----------|------|
| **Microsoft Defender for Office 365** | Cloud | Integrated with M365, good protection | Included in E5 |
| **Proofpoint** | Cloud | Best-in-class threat intel, targeted attack protection | $$$ |
| **Mimecast** | Cloud | Email security + archiving + continuity | $$ |
| **Barracuda** | Cloud/On-prem | Good value, comprehensive features | $ |

**Email Security Configuration**:
```powershell
# Microsoft 365 - Block dangerous attachments
Set-SafeAttachmentPolicy -Identity "Default" `
  -Action Block `
  -BlockedFileTypes @("exe","scr","vbs","js","bat","cmd","com","pif","msi","reg") `
  -Enable $true

# Enable Safe Links
Set-SafeLinksPolicy -Identity "Default" `
  -IsEnabled $true `
  -ScanUrls $true `
  -DeliverMessageAfterScan $true `
  -EnableForInternalSenders $true
```

#### 1.2 Endpoint Protection

**Endpoint Detection & Response (EDR)**:
- **Next-Gen Antivirus**: Signature + behavioral + machine learning detection
- **Ransomware Behavior Detection**: Monitor for mass file encryption, shadow copy deletion
- **Rollback Capability**: Restore files encrypted during attack (CrowdStrike, SentinelOne)
- **Network Containment**: Automatically isolate infected endpoints

**EDR Solutions**:
| Solution | Detection | Response | Rollback | Cost |
|----------|-----------|----------|----------|------|
| **CrowdStrike Falcon** | Excellent | Automated | Yes | $$$ |
| **SentinelOne** | Excellent | Automated | Yes | $$$ |
| **Microsoft Defender for Endpoint** | Very Good | Manual/Automated | Limited | Included in E5 |
| **Carbon Black** | Very Good | Automated | Yes | $$ |

**Key EDR Features for Ransomware**:
```yaml
# EDR Configuration Requirements
detection:
  - file_encryption_activity: true
  - shadow_copy_deletion: true
  - volume_shadow_service_disabled: true
  - backup_deletion: true
  - suspicious_powershell: true
  - lateral_movement: true

response:
  - network_isolation: automatic
  - process_termination: automatic
  - file_quarantine: automatic
  - alert_security_team: immediate

rollback:
  - automatic_file_restoration: true
  - retention_period: 30_days
```

**Windows Security Hardening**:
```powershell
# Enable Windows Defender features
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -DisableBehaviorMonitoring $false
Set-MpPreference -DisableBlockAtFirstSeen $false
Set-MpPreference -DisableIOAVProtection $false
Set-MpPreference -DisableScriptScanning $false

# Enable Controlled Folder Access (ransomware protection)
Set-MpPreference -EnableControlledFolderAccess Enabled

# Add protected folders
Add-MpPreference -ControlledFolderAccessProtectedFolders "C:\Users\*\Documents"
Add-MpPreference -ControlledFolderAccessProtectedFolders "C:\Users\*\Pictures"

# Enable Attack Surface Reduction rules
Add-MpPreference -AttackSurfaceReductionRules_Ids `
  "BE9BA2D9-53EA-4CDC-84E5-9B1EEEE46550" `  # Block executable content from email
  "D4F940AB-401B-4EFC-AADC-AD5F3C50688A" `  # Block Office from creating child processes
  "3B576869-A4EC-4529-8536-B80A7769E899" `  # Block Office from creating executable content
  "75668C1F-73B5-4CF0-BB93-3ECF5CB7CC84" `  # Block Office from injecting code
  "26190899-1602-49E8-8B27-EB1D0A1CE869" `  # Block Office communication apps from creating child processes
  "E6DB77E5-3DF2-4CF1-B95A-636979351E5B"    # Block persistence through WMI

# Disable macros from untrusted sources
# (Configure via Group Policy)
```

#### 1.3 Vulnerability & Patch Management

**Exploited Vulnerabilities in Ransomware Attacks**:
- **VPN Vulnerabilities**: Pulse Secure, Fortinet, Citrix (common entry points)
- **RDP Exploits**: BlueKeep (CVE-2019-0708), other RDP vulnerabilities
- **Microsoft Exchange**: ProxyShell, ProxyLogon exploits
- **Unpatched OS**: EternalBlue (WannaCry), SMBGhost
- **Third-Party Software**: Adobe, Java, browsers (drive-by downloads)

**Patch Management Strategy**:
```yaml
# Patching Priorities & Timelines
critical_patches:
  - zero_day_exploits: 24_hours
  - actively_exploited: 48_hours
  - critical_with_exploit_code: 7_days

high_patches:
  - high_severity: 30_days

routine_patches:
  - medium_severity: 60_days
  - low_severity: 90_days

patch_testing:
  - test_environment_first: required
  - pilot_group: 5-10% of devices
  - full_rollout: after_48h_pilot

exclusions:
  - business_critical_systems: change_control_required
  - legacy_systems: risk_accepted_documented
```

**Automated Patch Management**:
```powershell
# Windows Update for Business (Group Policy)
# Path: Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Update

# Configure Automatic Updates
Enabled: "4 - Auto download and schedule the install"

# Configure deadline for feature updates: 7 days
# Configure deadline for quality updates: 2 days

# Enable automatic restart after deadline
Enabled: "Yes"
```

#### 1.4 Access Controls & Network Segmentation

**Zero Trust Principles**:
- **Never Trust, Always Verify**: Authenticate and authorize every access
- **Least Privilege**: Minimum necessary access for users and applications
- **Micro-Segmentation**: Isolate workloads, limit lateral movement
- **Continuous Verification**: Monitor and verify all sessions

**MFA Enforcement**:
```yaml
# MFA Requirements
users:
  - all_users: mfa_required
  - privileged_accounts: phishing_resistant_mfa  # FIDO2, smart cards
  - service_accounts: certificate_based_auth

applications:
  - vpn: mfa_required
  - email: mfa_required
  - admin_portals: mfa_required
  - file_shares: mfa_for_external_access

mfa_methods:
  - preferred: [fido2_hardware_keys, microsoft_authenticator_push]
  - allowed: [authenticator_app_totp]
  - blocked: [sms, phone_call]  # Vulnerable to SIM swapping
```

**Network Segmentation**:
```
Internet
    ↓ Firewall
DMZ (Web servers, email gateway)
    ↓ Firewall
Corporate Network (Workstations, general servers)
    ↓ Firewall
Production Network (Application servers, databases)
    ↓ Firewall
Management Network (Backups, domain controllers, admin systems)
    ↓ Firewall
Critical Systems (Backup repositories, air-gapped backups)
```

**RDP Hardening** (Major Ransomware Entry Point):
```powershell
# Disable RDP if not needed
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 1

# If RDP needed, harden configuration:
# 1. Network Level Authentication (NLA) required
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name "UserAuthentication" -Value 1

# 2. Change default port (security through obscurity, not primary defense)
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name "PortNumber" -Value 33890

# 3. Limit RDP access to specific IPs (firewall rule)
New-NetFirewallRule -DisplayName "RDP from Admin IPs Only" `
  -Direction Inbound -Protocol TCP -LocalPort 3389 `
  -RemoteAddress 10.0.0.0/24 -Action Allow

# 4. Enable RDP logging
auditpol /set /subcategory:"Logon" /success:enable /failure:enable

# 5. Use RDP Gateway instead of direct RDP
# (Configure via Remote Desktop Gateway role)
```

#### 1.5 Privileged Access Management (PAM)

**Privileged Account Controls**:
- **Separate Admin Accounts**: Different accounts for admin vs. regular use
- **Just-in-Time (JIT) Access**: Temporary elevation only when needed
- **Privileged Access Workstations (PAW)**: Dedicated, hardened workstations for admin tasks
- **Password Vaulting**: Store privileged credentials in vault (CyberArk, Thycotic)
- **Session Recording**: Record all privileged sessions

**PAM Solutions**:
- **CyberArk**: Enterprise-grade, comprehensive features
- **Thycotic/Delinea**: Mid-market, good features
- **BeyondTrust**: Privileged remote access + password vaulting
- **Azure AD Privileged Identity Management**: Cloud-native, integrated with Microsoft

**Local Admin Password Solution (LAPS)**:
```powershell
# Deploy Microsoft LAPS (Local Administrator Password Solution)
# Randomizes local admin passwords on each workstation

# Install LAPS
Install-Module -Name AdmPwd.PS -Force

# Configure LAPS policy via GPO
Set-AdmPwdComputerSelfPermission -Identity "Workstations-OU"
Set-AdmPwdReadPasswordPermission -Identity "Workstations-OU" -AllowedPrincipals "IT-Admins"

# Password complexity: 14 characters, 30-day rotation
```

---

### PHASE 2: Backup & Recovery

#### 2.1 Backup Strategy (3-2-1-1-0 Rule)

**3-2-1-1-0 Backup Rule**:
- **3** copies of data: 1 primary + 2 backups
- **2** different media types: Disk + Tape/Cloud
- **1** offsite backup: Geographic separation
- **1** immutable/offline backup: Cannot be encrypted by ransomware
- **0** errors: Verify backups, test restores

**Backup Architecture**:
```
Primary Data (Production)
    ↓
Backup Copy 1: Local NAS (Fast recovery)
    ↓
Backup Copy 2: Cloud Object Storage (Offsite, immutable)
    ↓
Backup Copy 3: Tape/Air-Gapped Storage (Offline, ultimate protection)
```

#### 2.2 Immutable Backups

**Immutability Options**:

**Cloud Object Storage (AWS S3 Example)**:
```bash
# Enable S3 Object Lock (immutability)
aws s3api put-object-lock-configuration \
  --bucket ransomware-backups \
  --object-lock-configuration '{
    "ObjectLockEnabled": "Enabled",
    "Rule": {
      "DefaultRetention": {
        "Mode": "GOVERNANCE",
        "Days": 30
      }
    }
  }'

# Versioning enables point-in-time recovery
aws s3api put-bucket-versioning \
  --bucket ransomware-backups \
  --versioning-configuration Status=Enabled

# MFA Delete protection (even root can't delete without MFA)
aws s3api put-bucket-versioning \
  --bucket ransomware-backups \
  --versioning-configuration Status=Enabled,MFADelete=Enabled \
  --mfa "arn:aws:iam::123456789012:mfa/root-account-mfa-device 123456"
```

**Azure Blob Immutability**:
```bash
# Enable immutable storage
az storage container immutability-policy create \
  --account-name backupstorage \
  --container-name ransomware-backups \
  --period 30 \
  --resource-group backup-rg
```

**Backup Appliance (Veeam, Commvault)**:
```yaml
# Veeam Immutability Configuration
immutable_backup:
  enabled: true
  immutability_period: 14_days  # Cannot be deleted/modified for 14 days
  repository_type: object_storage  # S3, Azure Blob, or Linux hardened repo
  hardened_repository:
    os: linux_immutable
    ssh_keys_only: true
    sudo_disabled_for_backup_user: true
    backup_user_cannot_delete: true
```

**Air-Gapped Backup**:
```yaml
# Tape library or removable media strategy
air_gapped_backup:
  media: lto8_tape  # Or removable drives
  schedule:
    - full_backup: weekly
    - incremental: daily
    - offsite_rotation: weekly

  process:
    - backup_to_tape: automated
    - eject_tape: automated
    - physically_remove: manual  # Critical: Physically disconnect
    - store_offsite: within_24h

  retention:
    - weekly: 4_weeks
    - monthly: 12_months
    - yearly: 7_years

  testing:
    - restore_test: quarterly
    - full_disaster_recovery_test: annually
```

#### 2.3 Backup Monitoring & Testing

**Backup Verification**:
```python
# Automated backup verification script
import boto3
from datetime import datetime, timedelta

def verify_backups():
    s3 = boto3.client('s3')
    bucket = 'ransomware-backups'

    # Check backups exist for last 7 days
    for days_ago in range(7):
        date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
        prefix = f'backups/{date}/'

        response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

        if 'Contents' not in response:
            alert(f"❌ Backup missing for {date}")
            return False

        # Verify backup size (should be within reasonable range)
        total_size = sum(obj['Size'] for obj in response['Contents'])
        if total_size < MIN_BACKUP_SIZE:
            alert(f"⚠️ Backup for {date} suspiciously small: {total_size} bytes")
            return False

        print(f"✅ Backup verified for {date}: {total_size / 1024 / 1024:.2f} MB")

    return True

def test_restore():
    """Automated restore test"""
    try:
        # Restore random sample to test environment
        restore_random_files(count=10, target='test-restore-env')
        verify_restored_files()
        print("✅ Restore test successful")
        return True
    except Exception as e:
        alert(f"❌ Restore test failed: {str(e)}")
        return False

# Run daily
if __name__ == "__main__":
    if not verify_backups():
        sys.exit(1)

    # Restore test weekly (on Sundays)
    if datetime.now().weekday() == 6:
        if not test_restore():
            sys.exit(1)
```

**Recovery Time Objective (RTO) & Recovery Point Objective (RPO)**:
```yaml
# Define RTO/RPO by system criticality
tier_1_critical:
  - systems: [domain_controllers, email, financial_systems]
  - rto: 4_hours
  - rpo: 1_hour
  - backup_frequency: hourly
  - recovery_priority: 1

tier_2_important:
  - systems: [file_servers, databases, web_applications]
  - rto: 24_hours
  - rpo: 4_hours
  - backup_frequency: every_4_hours
  - recovery_priority: 2

tier_3_normal:
  - systems: [dev_environments, test_systems, archives]
  - rto: 72_hours
  - rpo: 24_hours
  - backup_frequency: daily
  - recovery_priority: 3
```

---

### PHASE 3: Detection & Response

#### 3.1 Ransomware Detection

**Behavioral Indicators**:
```yaml
# SIEM detection rules for ransomware
detection_rules:
  - rule_name: "Mass File Encryption"
    condition: |
      file_modifications > 100 in 60_seconds AND
      file_extensions changed to [.encrypted, .locked, .crypto, .cerber, etc.]
    severity: CRITICAL
    response: isolate_system

  - rule_name: "Shadow Copy Deletion"
    condition: |
      process: vssadmin.exe AND
      command_line contains "delete shadows"
    severity: CRITICAL
    response: terminate_process_and_alert

  - rule_name: "Backup Service Stopped"
    condition: |
      event_id: 7036 AND
      service_name in [VSS, Windows Backup, SQL Server Agent] AND
      state changed to "stopped"
    severity: HIGH
    response: alert_security_team

  - rule_name: "Suspicious PowerShell"
    condition: |
      process: powershell.exe AND
      command_line contains ["Invoke-WebRequest", "DownloadString", "IEX", "-enc"]
    severity: HIGH
    response: log_and_alert

  - rule_name: "Ransomware Note Creation"
    condition: |
      file_created AND
      filename matches ["README.txt", "HOW_TO_DECRYPT.txt", "*_DECRYPT_*"]
    severity: CRITICAL
    response: isolate_system_immediately
```

**Splunk SPL Queries**:
```spl
# Detect mass file encryption
index=windows source="WinEventLog:Security"
| stats count by ComputerName, User, TargetFilename
| where count > 100
| eval time_window=relative_time(now(), "-1m")
| where _time > time_window
| table ComputerName, User, count

# Detect shadow copy deletion
index=windows EventCode=1
Image="*vssadmin.exe"
CommandLine="*delete shadows*"
| table _time, ComputerName, User, CommandLine

# Detect ransomware processes
index=windows EventCode=1
| rex field=CommandLine "(?<encoded_command>-enc\s+[A-Za-z0-9+/=]+)"
| where isnotnull(encoded_command)
| eval decoded_command=base64decode(encoded_command)
| table _time, ComputerName, User, decoded_command
```

#### 3.2 Incident Response Playbook

**Ransomware Incident Response**:

**Phase 1: Detection & Triage** (Minutes 0-15)
```markdown
1. **Alert Received**: EDR/SIEM alert on ransomware indicators
2. **Verify Incident**: Confirm ransomware (not false positive)
   - Check for ransom note
   - Verify file encryption activity
   - Check multiple systems for spread
3. **Activate Incident Response Team**:
   - Incident Commander
   - IT Operations
   - Security Team
   - Communications Lead
   - Legal Counsel
4. **Document**: Start incident timeline, preserve evidence
```

**Phase 2: Containment** (Minutes 15-60)
```markdown
1. **Isolate Infected Systems**:
   - Disconnect from network (pull cable, disable WiFi)
   - DO NOT shut down (preserves memory for forensics)
   - Identify patient zero

2. **Prevent Spread**:
   - Disable user accounts of affected users
   - Block malicious IPs/domains at firewall
   - Isolate network segments
   - Disable RDP if attack vector

3. **Assess Scope**:
   - How many systems infected?
   - What data encrypted?
   - Are backups affected?

4. **Preserve Evidence**:
   - Memory dumps of infected systems
   - Network traffic captures
   - Logs from EDR, firewalls, proxies
```

**Phase 3: Eradication** (Hours 1-4)
```markdown
1. **Identify Attack Vector**:
   - Phishing email?
   - Exploited vulnerability?
   - Compromised credentials?
   - Supply chain attack?

2. **Remove Threat**:
   - Kill ransomware processes (if still running)
   - Remove persistence mechanisms
   - Patch exploited vulnerabilities
   - Reset compromised credentials

3. **Clean Affected Systems**:
   - Reimage infected systems (preferred)
   - Or: Scan with multiple AV tools, manual verification
```

**Phase 4: Recovery** (Hours 4-48)
```markdown
1. **Restore from Backups**:
   - Verify backups not encrypted
   - Restore in order of priority (Tier 1 first)
   - Restore to clean, patched systems

2. **Verify Recovery**:
   - Check restored data integrity
   - Test critical business functions
   - Scan restored systems for malware

3. **Resume Operations**:
   - Gradual return to production
   - Enhanced monitoring
   - User communication
```

**Phase 5: Post-Incident** (Days 1-7)
```markdown
1. **Root Cause Analysis**:
   - Timeline reconstruction
   - Attack path analysis
   - Identify security gaps

2. **Lessons Learned**:
   - What worked well?
   - What could improve?
   - Update incident response plan

3. **Implement Improvements**:
   - Patch identified vulnerabilities
   - Update security controls
   - Additional training if needed

4. **Reporting**:
   - Executive briefing
   - Board notification (if material)
   - Regulatory reporting (if required)
   - Cyber insurance claim
```

#### 3.3 Ransom Payment Decision Framework

**To Pay or Not to Pay?**

**Arguments Against Payment**:
- ❌ No guarantee of decryption (30% of victims who pay don't get data back)
- ❌ Funds criminal enterprise
- ❌ Makes you a target for future attacks
- ❌ Legal/regulatory issues (paying sanctioned entities)
- ❌ Potential criminal prosecution (some jurisdictions)
- ❌ Reputational damage

**Arguments For Payment** (Desperate Scenarios):
- ✅ No viable backups available
- ✅ Critical life-safety systems affected (hospitals)
- ✅ Business extinction without data
- ✅ Decryption proven possible (negotiator verified)

**Decision Tree**:
```
Can we recover from backups?
  └─ YES → Do not pay, recover from backups
  └─ NO → ↓

Is the data business-critical?
  └─ NO → Do not pay, recreate data
  └─ YES → ↓

Have we verified decryption works? (via negotiator)
  └─ NO → Do not pay, likely scam
  └─ YES → ↓

Is payment legal? (not sanctioned entity)
  └─ NO → Do not pay, illegal
  └─ YES → ↓

Board/Executive Decision:
  - Consider business impact
  - Legal review
  - Cyber insurance guidance
  - Final decision: Pay or not
```

**If Payment Decided** (last resort):
```yaml
payment_process:
  1_engage_negotiator:
    - specialized_ransomware_negotiator
    - negotiate_down_ransom (often 20-50% reduction)
    - verify_decryption (test file decryption)

  2_legal_review:
    - verify_not_sanctioned_entity
    - consider_regulatory_reporting
    - document_business_justification

  3_payment:
    - use_cryptocurrency (Bitcoin, Monero)
    - go_through_exchange_licensed_in_us
    - document_for_tax_purposes

  4_decryption:
    - receive_decryption_tool
    - test_on_non_critical_system_first
    - decrypt_in_priority_order
    - verify_no_backdoors_in_tool

  5_post_payment:
    - report_to_law_enforcement (FBI IC3)
    - report_to_cyber_insurance
    - share_IOCs_with_community
```

**Recommendation**: **DO NOT PAY**. Focus on robust backups and prevention instead.

---

### PHASE 4: Business Continuity & Disaster Recovery

#### 4.1 Business Continuity Planning (BCP)

**Ransomware-Specific BCP Considerations**:
```yaml
business_continuity:
  scenario: "Complete ransomware encryption of production systems"

  critical_business_functions:
    - function: "Process customer orders"
      rto: 4_hours
      workaround: "Manual order processing, paper forms"
      dependencies: [order_system, payment_gateway, inventory]

    - function: "Manufacturing operations"
      rto: 8_hours
      workaround: "Manual production scheduling, paper travelers"
      dependencies: [mes_system, erp, plc_controllers]

    - function: "Customer support"
      rto: 2_hours
      workaround: "Phone support only, no CRM access"
      dependencies: [crm_system, phone_system, knowledge_base]

  communication_plan:
    internal:
      - employees: "Company-wide email + Microsoft Teams"
      - executives: "Emergency conference call line"
      - it_team: "Dedicated Slack channel"

    external:
      - customers: "Website banner + email notification"
      - vendors: "Account managers notify key vendors"
      - media: "Prepared statement (only if public)"
      - regulators: "Legal team handles notifications"

  alternate_work_locations:
    - primary: "Work from home (if corporate network affected)"
    - secondary: "Partner office space (pre-arranged)"
```

#### 4.2 Disaster Recovery Testing

**Tabletop Exercises**:
```yaml
tabletop_exercise:
  frequency: quarterly
  duration: 2_hours
  participants: [IT, Security, Executives, Legal, Communications]

  scenario: |
    "It's Monday 8 AM. Multiple users report they cannot access files.
    IT discovers ransomware note on several servers. Approximately 30%
    of file servers encrypted. Email system still operational. Backups
    status unknown."

  discussion_questions:
    - "Who is incident commander?"
    - "What are first 3 actions?"
    - "How do we assess scope?"
    - "When do we notify executives/board?"
    - "How do we communicate with employees?"
    - "What's our backup recovery plan?"
    - "Do we pay the ransom?"

  outcomes:
    - identified_gaps: [unclear_ic_designation, backup_status_unknown, no_communication_template]
    - action_items: [update_ir_plan, document_backup_locations, create_comm_templates]
```

**Full DR Tests**:
```yaml
disaster_recovery_test:
  frequency: annually
  duration: 1_day
  scope: "Full recovery of Tier 1 systems from immutable backups"

  test_steps:
    1_simulate_attack:
      - encrypt_test_environment_data
      - disable_access_to_production_backups

    2_invoke_dr_plan:
      - activate_incident_response_team
      - follow_documented_procedures

    3_recovery:
      - restore_from_immutable_backups
      - verify_data_integrity
      - test_critical_business_functions

    4_measure:
      - actual_rto_vs_target
      - actual_rpo_vs_target
      - issues_encountered

    5_report:
      - executive_summary
      - lessons_learned
      - improvement_actions

  success_criteria:
    - all_tier1_systems_restored: within_rto
    - data_integrity: 100%
    - critical_functions: operational
    - documentation: complete_and_accurate
```

---

### PHASE 5: Insurance & Legal

#### 5.1 Cyber Insurance

**Cyber Insurance Coverage** (for Ransomware):
```yaml
cyber_insurance_policy:
  coverage:
    first_party:
      - business_interruption: "Loss of income during downtime"
      - data_restoration: "Cost to restore from backups"
      - extortion_payment: "Ransom payment (if paid)"
      - forensic_investigation: "Digital forensics costs"
      - legal_fees: "Attorney fees for incident response"
      - notification_costs: "Notifying affected parties"
      - credit_monitoring: "For affected individuals"
      - pr_crisis_management: "Reputation management"

    third_party:
      - liability: "Lawsuits from affected parties"
      - regulatory_fines: "GDPR, CCPA, HIPAA fines"
      - defense_costs: "Legal defense in lawsuits"

  policy_limits:
    - per_incident: $5_million
    - aggregate_annual: $10_million
    - extortion_payment_sublimit: $1_million

  deductible:
    - self_insured_retention: $100_000

  requirements:
    - security_controls: [mfa, edr, siem, backups, patching]
    - security_assessment: annual_third_party_audit
    - incident_response_plan: documented_and_tested
    - backup_testing: quarterly_restore_tests
```

**Making a Claim**:
```markdown
1. **Immediate Notification**: Notify insurer within 24-48 hours of discovery
2. **Breach Coach**: Insurer provides attorney (breach coach)
3. **Approved Vendors**: Use insurer's approved forensics/IR vendors
4. **Documentation**: Detailed documentation of incident and costs
5. **Coverage Determination**: Insurer reviews and approves coverage
6. **Reimbursement**: Submit invoices for covered costs
```

#### 5.2 Legal & Regulatory Obligations

**Notification Requirements** (if PII affected):
```yaml
notification_requirements:
  gdpr_eu:
    - regulator: data_protection_authority
    - timeline: within_72_hours
    - threshold: likely_risk_to_rights_and_freedoms
    - individuals: if_high_risk

  ccpa_california:
    - regulator: california_attorney_general
    - timeline: without_unreasonable_delay
    - threshold: unauthorized_access_or_disclosure
    - individuals: required

  hipaa_healthcare:
    - regulator: hhs_office_for_civil_rights
    - timeline: within_60_days
    - threshold: unsecured_phi_affected
    - individuals: required_if_500_or_more
    - media: required_if_500_or_more

  state_laws_us:
    - varies_by_state: 50_different_laws
    - timeline: generally_without_unreasonable_delay
    - threshold: varies (some all_breaches, some only_sensitive_data)
```

**Law Enforcement Reporting**:
```markdown
- **FBI Internet Crime Complaint Center (IC3)**: https://www.ic3.gov/
- **Secret Service Cyber Investigations**: For financial crimes
- **CISA**: Report via CISA's reporting portal
- **Local Law Enforcement**: File police report

Benefits of Reporting:
- Assists law enforcement in tracking threat actors
- May receive threat intelligence in return
- May be required for cyber insurance claim
- Demonstrates good faith to regulators
```

---

## Variables Table

| Variable | Description | Example Values | Notes |
|----------|-------------|----------------|-------|
| `{EDR_SOLUTION}` | Endpoint detection tool | CrowdStrike, SentinelOne, Defender | Behavioral detection critical |
| `{BACKUP_TYPE}` | Backup immutability | S3 Object Lock, Azure Immutable, Tape | Must be immutable |
| `{RTO}` | Recovery time objective | 4 hours, 24 hours, 72 hours | By system criticality |
| `{RPO}` | Recovery point objective | 1 hour, 4 hours, 24 hours | How much data loss acceptable |
| `{BACKUP_FREQUENCY}` | How often backups run | Hourly, Daily, Weekly | Based on RPO |
| `{RANSOM_DECISION}` | Pay or not | Never, Only_if_life_safety, Board_decision | Strongly recommend never |
| `{INSURANCE_LIMIT}` | Cyber insurance coverage | $1M, $5M, $10M | Based on company size/risk |
| `{SEGMENTATION_LEVEL}` | Network isolation | Flat, Basic_zones, Micro-segmentation | More isolation = less spread |
| `{MFA_REQUIREMENT}` | MFA scope | All_users, Admins_only, VPN_only | Recommend all users |
| `{PATCH_SLA}` | Patch timeline | 24h_critical, 7d_high, 30d_medium | Based on severity |
| `{RESTORE_TESTING}` | Test frequency | Weekly, Monthly, Quarterly | Monthly minimum |
| `{AIR_GAP_MEDIA}` | Offline backup type | Tape, Removable_drives, None | Ultimate protection |

---

## Usage Examples

### Example 1: Healthcare Organization (HIPAA Compliance)

**Context**: 300-bed hospital, HIPAA-regulated, previous ransomware scare, implementing comprehensive defense.

**Prevention Stack**:
- **Email Security**: Proofpoint (healthcare-focused threat intel)
- **Endpoint**: CrowdStrike Falcon (EDR with rollback)
- **Network Segmentation**:
  - Medical devices on isolated VLAN
  - EMR systems on protected segment
  - Corporate network separate
  - Guest WiFi completely isolated

**Backup Strategy**:
```yaml
backup_strategy:
  tier_1_critical:
    - systems: [emr, pacs, pharmacy, lab]
    - rto: 2_hours
    - rpo: 15_minutes
    - backup_frequency: every_15_minutes
    - backup_locations:
      - primary: on_premise_nas (instant recovery)
      - secondary: aws_s3_immutable (30_day_lock)
      - tertiary: tape_air_gapped (weekly)

  tier_2_important:
    - systems: [billing, scheduling, hr]
    - rto: 8_hours
    - rpo: 1_hour
    - backup_frequency: hourly

  testing:
    - restore_test: weekly_automated
    - full_dr_test: quarterly
    - tabletop_exercise: monthly
```

**Incident Response**:
```markdown
## Ransomware IR Plan (Healthcare-Specific)

### Immediate Actions (Minutes 0-15):
1. Activate incident response team + Hospital Incident Command
2. Assess impact to patient care
3. If critical systems affected: Activate downtime procedures
4. Isolate affected systems (preserve patient safety systems)

### Patient Safety Priority:
- Life-safety systems (ventilators, monitors) are air-gapped and separate
- EMR downtime procedures: Paper charts, manual medication administration
- Lab/Radiology: Manual requisitions, courier for critical results
- Surgery: Postpone elective procedures if systems unavailable

### Communication:
- Staff: Overhead page + emergency notification system
- Patients: Direct communication, posted signage
- Regulators: HHS notification within 60 days if ePHI affected
- Law enforcement: FBI, local police

### Recovery Priority:
1. EMR system (patient care critical)
2. Pharmacy system (medication safety)
3. Lab/Radiology (diagnostics)
4. Scheduling/registration
5. Billing (can delay)
```

**Results**:
- Zero patient safety incidents during ransomware tests
- <2 hour RTO for critical systems
- Full DR test passed (recovered all Tier 1 systems in 1.5 hours)
- HIPAA audit: No findings on ransomware preparedness

### Example 2: Manufacturing Company (Operational Technology)

**Context**: Manufacturing plant with OT/ICS systems, potential ransomware impact to production line.

**OT-Specific Challenges**:
- Legacy systems (Windows XP, unpatched)
- Cannot install EDR on PLCs
- Cannot reboot production systems
- Air-gapped network (theoretically)

**Defense Strategy**:
```yaml
ot_security:
  network_segmentation:
    - level_4_5: "IT network (firewall separated from OT)"
    - level_3: "SCADA, HMI, Engineering workstations"
    - level_2: "PLCs, DCS, industrial controllers"
    - level_1_0: "Physical processes, sensors, actuators"

    firewall_rules:
      - default: deny_all
      - level3_to_level2: allow_specific_protocols [modbus, opc_ua]
      - level4_to_level3: read_only_access [historians, reporting]
      - no_internet_access_from_level0-2: enforced

  endpoint_protection:
    - engineering_workstations: crowdstrike_edr
    - legacy_plc_controllers: unidirectional_gateways
    - hmi_displays: application_whitelisting

  backup_strategy:
    - plc_ladder_logic: daily_export_to_isolated_storage
    - scada_configuration: weekly_backup_to_tape
    - engineering_workstation_images: monthly_golden_images
    - production_data: hourly_replication_to_it_network
```

**Incident Response** (OT-Specific):
```markdown
## Ransomware in OT Environment

### DO NOT:
- Do not shut down running production equipment (safety risk)
- Do not isolate Level 0-2 networks mid-production (halt production only if safe)

### If Ransomware Reaches OT Network:
1. **Assess**: Which level affected? (Workstation vs. controller)
2. **Contain**: Isolate affected level at firewall
3. **Safety First**: If controllers affected, perform safe shutdown
4. **Forensics**: Image affected engineering workstations
5. **Rebuild**: Restore controllers from backup ladder logic
6. **Verify**: Test all safety interlocks before resuming production

### Prevention Priority:
- Engineering workstations are primary risk (Windows-based, network access)
- Keep OT network truly air-gapped (USB is common infection vector)
- Whitelist applications on HMI/SCADA systems
- Train engineers on USB hygiene (scan before plugging in)
```

**Results**:
- Engineering workstation infected in simulation
- Production line not affected (Level 2 isolated)
- Restored workstation from golden image in 30 minutes
- Zero production downtime during incident

### Example 3: Financial Services (Highly Regulated)

**Context**: Regional bank, PCI-DSS + SOX compliance, high ransomware target.

**Comprehensive Defense**:
```yaml
defense_in_depth:
  layer_1_perimeter:
    - email_security: proofpoint_tap
    - web_proxy: zscaler_with_dlp
    - vpn: palo_alto_global_protect_with_mfa

  layer_2_network:
    - firewall: palo_alto_next_gen
    - ids_ips: suricata
    - network_segmentation: zero_trust_micro_segmentation

  layer_3_endpoint:
    - edr: crowdstrike_falcon_enterprise
    - application_whitelisting: applocker
    - disk_encryption: bitlocker_with_tpm

  layer_4_identity:
    - mfa: yubikey_fido2_for_all_users
    - pam: cyberark_for_privileged_access
    - zero_trust: okta_with_device_trust

  layer_5_data:
    - dlp: symantec_dlp
    - database_encryption: tde_sql_server
    - file_encryption: microsoft_purview_aip

  layer_6_application:
    - waf: akamai
    - api_security: apigee
    - code_security: veracode_sast_dast
```

**Backup & Recovery** (Financial Services):
```yaml
backup_requirements:
  regulatory_compliance:
    - sox: 7_year_retention
    - pci_dss: secure_deletion_after_retention
    - finra: audit_trail_integrity

  architecture:
    - production: active_active_data_center
    - backup_tier1: netapp_snapshots_every_15min
    - backup_tier2: veeam_to_s3_immutable_daily
    - backup_tier3: iron_mountain_tape_weekly

  recovery_capabilities:
    - instant_recovery: from_netapp_snapshots (<1_hour)
    - full_recovery: from_s3_immutable (<4_hours)
    - disaster_recovery: from_tape (<24_hours)

  testing:
    - automated_restore_test: daily
    - partial_dr_test: monthly
    - full_dr_test: quarterly
    - regulator_witnessed_test: annually
```

**Results**:
- No ransomware incidents in 3 years
- SOX audit: No findings on backup/recovery
- PCI-DSS: Compliant for 5 consecutive years
- DR test: Passed 100% success rate
- Cyber insurance premium reduced 30% (due to strong controls)

---

## Best Practices

### Prevention
- **Defense in Depth**: Multiple layers of security (email, endpoint, network, identity)
- **Patch Aggressively**: Prioritize critical and high-severity patches (7-day SLA)
- **MFA Everywhere**: All users, all systems, phishing-resistant preferred
- **Network Segmentation**: Limit lateral movement, separate critical systems
- **Least Privilege**: Minimum necessary access, just-in-time elevation

### Backup & Recovery
- **3-2-1-1-0 Rule**: 3 copies, 2 media, 1 offsite, 1 immutable, 0 errors
- **Immutable Backups**: Cannot be encrypted or deleted (S3 Object Lock, tape)
- **Offline/Air-Gapped**: Physical separation is ultimate protection
- **Test Regularly**: Monthly automated restore tests, quarterly full DR tests
- **Document RTO/RPO**: Define recovery objectives, test against them

### Detection & Response
- **Behavioral Detection**: EDR/XDR with behavioral analytics (not just signatures)
- **SIEM Alerts**: Mass file encryption, shadow copy deletion, suspicious processes
- **Incident Response Plan**: Documented, tested (tabletop quarterly)
- **Isolate Quickly**: Disconnect infected systems within minutes
- **Do Not Pay**: Recover from backups instead of paying ransom

### Business Continuity
- **Tabletop Exercises**: Quarterly exercises to practice response
- **Communication Plans**: Internal and external communication templates
- **Alternate Processes**: Manual workarounds for critical functions
- **Cyber Insurance**: Adequate coverage for ransomware incidents
- **Legal Preparedness**: Breach coach, notification templates ready

---

## Common Pitfalls

### Backup Failures
- **Backups Not Immutable**: Ransomware encrypts backups too
- **No Offline Backups**: All backups connected to network, all encrypted
- **Untested Backups**: Discover backups don't work during actual incident
- **Backup Credentials Compromised**: Attackers delete backups before encryption
- **RPO Too Long**: Lose too much data even with successful recovery

### Prevention Gaps
- **No MFA**: Compromised credentials = network access
- **Flat Network**: Ransomware spreads unchecked
- **Unpatched Systems**: Exploited vulnerabilities (EternalBlue, ProxyLogon)
- **RDP Exposed**: Direct RDP from internet is primary entry point
- **No Email Security**: Phishing emails deliver ransomware

### Response Errors
- **Slow Isolation**: Delay in isolating infected systems allows spread
- **Shutting Down**: Powering off destroys forensics evidence (memory)
- **Paying Ransom**: No guarantee of decryption, funds criminals
- **Poor Communication**: Employees, customers, regulators not notified properly
- **No DR Plan**: Ad hoc response instead of practiced procedures

### Detection Failures
- **Signature-Only**: Modern ransomware evades signature detection
- **No EDR**: No behavioral detection of encryption activity
- **Alert Fatigue**: Too many false positives, real alert missed
- **No Monitoring**: Attacks occur outside business hours, not detected until Monday
- **Insufficient Logging**: Cannot reconstruct attack timeline

---

## Related Templates

- **../Cybersecurity/incident-response.md**: General incident response framework
- **../Cybersecurity/security-architecture.md**: Defense-in-depth architecture
- **../Security-Operations/siem-security-monitoring.md**: SIEM and monitoring
- **../Compliance-Governance/data-security-strategy.md**: Data backup and encryption
- **../Application-Security/web-application-security.md**: Application security

---

## Additional Resources

**Ransomware Resources**:
- CISA Ransomware Guide: https://www.cisa.gov/stopransomware
- FBI Ransomware Reporting: https://www.ic3.gov/
- No More Ransom Project: https://www.nomoreransom.org/
- Ransomware Task Force: https://securityandtechnology.org/ransomwaretaskforce/

**Incident Response**:
- NIST Cybersecurity Framework
- SANS Incident Response
- MITRE ATT&CK (Ransomware tactics)

**Backup Solutions**:
- Veeam Backup & Replication
- Commvault
- Rubrik (immutable backups)
- AWS Backup, Azure Backup

**Training**:
- SANS Ransomware Summit
- KnowBe4 Security Awareness Training
- Ransomware simulation exercises

**Threat Intelligence**:
- Ransomware.live (tracking current campaigns)
- ID Ransomware (identify ransomware variant)
- Bleeping Computer Ransomware forum

---

*This framework provides comprehensive ransomware defense and recovery guidance. Ransomware is not a matter of "if" but "when" - organizations must prepare with robust prevention, detection, and recovery capabilities. The best defense is strong backups with offline/immutable copies combined with defense-in-depth security controls. Remember: Never pay the ransom if avoidable - it funds criminal enterprises and doesn't guarantee data recovery.*
