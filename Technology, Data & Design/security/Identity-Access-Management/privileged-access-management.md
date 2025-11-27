---
category: security
last_updated: 2025-11-23
title: Privileged Access Management (PAM)
tags:
- security
- pam
- privileged-access
- credential-vault
use_cases:
- Securing privileged accounts and credentials
- Implementing just-in-time access
- Session monitoring and recording
- Compliance with least privilege principle
related_templates:
- security/Identity-Access-Management/zero-trust-architecture.md
- security/Compliance-Governance/security-compliance-framework.md
industries:
- technology
type: template
difficulty: intermediate
slug: privileged-access-management
---

# Privileged Access Management (PAM)

## Purpose
Comprehensive framework for securing privileged accounts, implementing just-in-time access, session monitoring, credential vaulting, and compliance with least privilege principles.

## Quick PAM Prompt
Implement PAM for [X] privileged accounts across [Windows/Linux/databases/cloud]. Solution: [CyberArk/BeyondTrust/Delinea]. Implement: credential vaulting with auto-rotation, just-in-time access workflows, session recording for audit, break-glass procedures. Cover: admin accounts, service accounts, third-party access. Compliance: [SOX/PCI-DSS/HIPAA]. Deliver: architecture, access policies, and operational procedures.

## Quick Start

**Need to implement PAM?** Use this minimal example:

```
Implement PAM solution (CyberArk/BeyondTrust/Delinea) for 500 privileged accounts across Windows, Linux, databases, cloud platforms. Implement credential vaulting, session recording, just-in-time access, and automated password rotation.
```

### When to Use This
- Implementing enterprise PAM for regulatory compliance (SOX, PCI-DSS, HIPAA)
- Securing privileged access after a security incident or audit finding
- Moving to zero trust architecture requiring privileged access controls
- Managing third-party/contractor privileged access
- Consolidating disparate privileged credential management

### Basic 3-Step Workflow
1. **Discover Privileged Accounts** - Inventory all privileged accounts
2. **Vault & Rotate** - Secure credentials, automate rotation
3. **Monitor & Audit** - Session recording, access reviews

---

## Template

```markdown
I need to implement privileged access management. Please provide comprehensive PAM implementation guidance.

## ENVIRONMENT CONTEXT

### Privileged Accounts
- Admin accounts: [WINDOWS_LINUX_MAC_DATABASES_CLOUD]
- Service accounts: [APPLICATIONS_SERVICES_AUTOMATION]
- Privileged users: [ADMINS_DBAs_DEVOPS_CONTRACTORS]
- Target systems: [SERVERS_NETWORK_CLOUD_APPLICATIONS]

## PAM CAPABILITIES

### 1. Credential Vaulting
- Secure password storage
- Encrypted vaults
- Access controls
- Check-in/check-out workflow
- Dual control/approval workflows

### 2. Password Management
- Automated password rotation
- Strong password generation
- Password history
- Emergency access procedures
- Password discovery

### 3. Session Management
- Session recording
- Real-time monitoring
- Session isolation
- Kill session capability
- Activity logging

### 4. Just-in-Time (JIT) Access
- Temporary access elevation
- Time-bound permissions
- Workflow approvals
- Access removal
- Audit trails

### 5. Privileged Behavior Analytics
- Baseline normal behavior
- Anomaly detection
- Risk scoring
- Automated response
- Threat hunting

### 6. Integration
- SIEM integration
- Ticketing integration
- MFA integration
- Directory services
- Cloud platforms

## OUTPUT REQUIREMENTS

Provide:
1. PAM architecture
2. Implementation roadmap
3. Credential vaulting strategy
4. Access workflows
5. Monitoring and alerting
6. Compliance reporting
```

## Variables

### PAM_PLATFORM
The privileged access management solution being implemented.
- Examples: "CyberArk Privileged Access Security", "BeyondTrust Password Safe", "Delinea Secret Server", "HashiCorp Vault Enterprise", "AWS Secrets Manager + IAM"

### PRIVILEGED_ACCOUNT_TYPES
Categories of privileged accounts to be managed.
- Examples: "Domain Admins", "Local Administrators", "Root accounts", "Database DBAs", "Service accounts", "Cloud IAM roles", "Application service IDs"

### TARGET_SYSTEMS
Systems containing privileged accounts to be vaulted.
- Examples: "Windows Server 2019/2022", "RHEL/Ubuntu Linux", "Oracle/SQL Server databases", "AWS/Azure/GCP consoles", "Network devices (Cisco, Palo Alto)", "VMware vSphere"

### ACCESS_WORKFLOW
The privileged access request and approval workflow.
- Examples: "Manager approval + security review", "Self-service with time-based auto-expiry", "Dual control (two approvers required)", "Emergency break-glass procedure"

### SESSION_RECORDING_SCOPE
Scope of privileged session recording.
- Examples: "All sessions to production systems", "Database admin sessions only", "Keystroke logging for high-risk accounts", "Video recording for compliance"

### ROTATION_FREQUENCY
Password rotation schedule for privileged accounts.
- Examples: "Every 30 days for service accounts", "After each use for shared accounts", "90 days for admin accounts", "Immediate rotation on check-in"

---

## Usage Examples

### Example 1: Financial Services SOX Compliance
```
PAM_PLATFORM: CyberArk Privileged Access Security
PRIVILEGED_ACCOUNT_TYPES: 200 Windows domain admins, 150 Linux root, 50 Oracle DBAs
TARGET_SYSTEMS: 500 Windows servers, 300 Linux servers, 25 Oracle databases
ACCESS_WORKFLOW: Manager + security approval, 4-hour maximum session
SESSION_RECORDING_SCOPE: Full session recording with keystroke logging
ROTATION_FREQUENCY: Every use for shared accounts, 30 days for service accounts

Key Implementations:
- Vault: CyberArk Enterprise Password Vault with HSM
- Discovery: Automated weekly scans for new privileged accounts
- JIT Access: Time-bound elevation via ServiceNow integration
- Session Management: PSM with video recording for SOX evidence
- Compliance: Automated attestation reports for auditors
- Emergency Access: Break-glass with dual control and SMS alerts
```

### Example 2: Healthcare HIPAA Environment
```
PAM_PLATFORM: BeyondTrust Password Safe + Privilege Management
PRIVILEGED_ACCOUNT_TYPES: EHR system admins, medical device service accounts
TARGET_SYSTEMS: Epic EHR, medical imaging systems, HL7 integration servers
ACCESS_WORKFLOW: Security team approval with ticket reference required
SESSION_RECORDING_SCOPE: All PHI system access recorded and retained 7 years
ROTATION_FREQUENCY: 24 hours for medical device accounts, 90 days for admin

Key Implementations:
- Vault: BeyondTrust with FIPS 140-2 encryption
- Discovery: Medical device credential inventory (IoT/OT)
- JIT Access: 2-hour access windows for system maintenance
- Session Management: Recording retained for HIPAA audit trail
- Compliance: PHI access reports for privacy officer review
- Integration: Epic MyChart SSO with privileged session proxy
```

### Example 3: Multi-Cloud DevOps Environment
```
PAM_PLATFORM: HashiCorp Vault Enterprise + CyberArk Conjur
PRIVILEGED_ACCOUNT_TYPES: Cloud IAM roles, Kubernetes service accounts, CI/CD secrets
TARGET_SYSTEMS: AWS (50 accounts), Azure (20 subscriptions), GCP (10 projects), Kubernetes clusters
ACCESS_WORKFLOW: GitOps-driven with pull request approval
SESSION_RECORDING_SCOPE: Cloud console access via AWS Session Manager
ROTATION_FREQUENCY: Dynamic secrets with TTL-based expiration

Key Implementations:
- Vault: HashiCorp Vault with auto-unseal (AWS KMS)
- Discovery: Cloud IAM role enumeration via API scanning
- JIT Access: Dynamic AWS credentials (15-minute TTL)
- Session Management: AWS Session Manager for EC2 access
- Secrets Injection: Kubernetes External Secrets Operator
- CI/CD: Vault Agent sidecar for pipeline secrets
- Zero Standing Privileges: No persistent cloud admin access
```

---

## Best Practices

1. **Discover before you vault** - Complete privileged account discovery before implementing vaulting to ensure no orphan accounts
2. **Start with service accounts** - They're less disruptive than user accounts and provide quick wins
3. **Implement break-glass procedures** - Define emergency access before locking down production access
4. **Session recording for compliance** - Record all privileged sessions for high-risk systems
5. **Integrate with ITSM** - Require ticket references for privileged access requests
6. **Automate password rotation** - Eliminate manual password changes and shared spreadsheets
7. **Monitor for anomalies** - Use behavioral analytics to detect unusual privileged access patterns
8. **Regular attestation** - Quarterly reviews of privileged access entitlements
9. **Least privilege always** - Grant minimum necessary access for the specific task
10. **API-first for DevOps** - Provide programmatic access to secrets for automation

## Common Pitfalls

❌ **Big bang rollout** - Trying to vault all accounts at once
✅ Instead: Phased approach starting with highest-risk accounts

❌ **Ignoring service accounts** - Focusing only on human privileged users
✅ Instead: Include service accounts, scripts, and automation credentials

❌ **No break-glass procedure** - Locking out access without emergency alternatives
✅ Instead: Define and test break-glass access before go-live

❌ **Complex approval workflows** - Multi-level approvals causing operational delays
✅ Instead: Risk-based workflows (simple for low-risk, strict for high-risk)

❌ **Password-only protection** - Relying solely on password vaulting
✅ Instead: Combine with MFA, session monitoring, and behavioral analytics
