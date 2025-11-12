---
category: security/Identity-Access-Management
last_updated: 2025-11-11
title: Privileged Access Management (PAM)
tags:
- security
- compliance
- access-control
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
---

# Privileged Access Management (PAM)

## Purpose
Comprehensive framework for securing privileged accounts, implementing just-in-time access, session monitoring, credential vaulting, and compliance with least privilege principles.

## Quick Start

**Need to implement PAM?** Use this minimal example:

```
Implement PAM solution (CyberArk/BeyondTrust/Delinea) for 500 privileged accounts across Windows, Linux, databases, cloud platforms. Implement credential vaulting, session recording, just-in-time access, and automated password rotation.
```

### Basic 3-Step Workflow
1. **Discover Privileged Accounts** - Inventory all privileged accounts (1-2 weeks)
2. **Vault & Rotate** - Secure credentials, automate rotation (2-4 weeks)
3. **Monitor & Audit** - Session recording, access reviews (ongoing)

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
