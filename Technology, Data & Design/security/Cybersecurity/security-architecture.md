---
category: security
last_updated: 2025-11-22
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- design
- ai-ml
- management
- security
- strategy
title: Security Architecture Template
use_cases:
- Creating design comprehensive security architecture including security design principles,
  defensive strategies, implementation patterns, and governance frameworks for enterprise
  security systems.
- Project planning and execution
- Strategy development
industries:
- government
- technology
type: template
difficulty: intermediate
slug: security-architecture
---

# Security Architecture Template

## Purpose
Design comprehensive security architecture including security design principles, defensive strategies, implementation patterns, and governance frameworks for enterprise security systems.

## Quick Security Architecture Prompt
Design security architecture for [enterprise/application] with [X users], [Y systems]. Apply principles: zero trust, defense-in-depth, least privilege. Define: identity strategy (SSO, MFA, PAM), network segmentation, data protection (encryption, DLP), endpoint security (EDR), and monitoring (SIEM, SOAR). Use [SABSA/TOGAF] framework. Deliver: architecture diagrams, control matrix, and implementation roadmap.

## Quick Start

**Set Your Foundation:**
1. Define security objectives aligned with business goals and risk tolerance
2. Identify threat landscape: external threats, insider risks, supply chain vulnerabilities
3. Determine regulatory requirements and compliance mandates

**Configure Key Parameters:**
4. Select core security principles: zero trust, defense in depth, least privilege
5. Define identity strategy: SSO, MFA, PAM implementation approach
6. Choose technology stack: SIEM, EDR, firewall, WAF, DLP solutions

**Implement & Deploy (Ongoing):**
7. Implement network segmentation with micro-segmentation for critical assets
8. Deploy zero trust architecture with continuous verification and least privilege access
9. Establish security monitoring with SIEM, SOAR, and threat intelligence integration
10. Create security governance framework with policies, standards, and procedures

**Pro Tips:** Use SABSA or TOGAF for architecture framework, implement security by design in SDLC, automate security controls where possible, and maintain architecture documentation with regular updates. Start with identity-centric security model for zero trust.

## Template Structure

### Security Architecture Overview
- **Architecture Name**: [ARCHITECTURE_NAME]
- **Security Objectives**: [SECURITY_OBJECTIVES]
- **Business Context**: [BUSINESS_CONTEXT]
- **Threat Landscape**: [THREAT_LANDSCAPE]
- **Regulatory Requirements**: [REGULATORY_REQUIREMENTS]
- **Risk Profile**: [RISK_PROFILE]
- **Architecture Scope**: [ARCHITECTURE_SCOPE]
- **Technology Stack**: [SECURITY_TECHNOLOGY_STACK]
- **Budget**: [ARCHITECTURE_BUDGET]
- **Timeline**: [ARCHITECTURE_TIMELINE]

### Security Principles
- **Defense in Depth**: [DEFENSE_IN_DEPTH]
- **Zero Trust**: [ZERO_TRUST]
- **Least Privilege**: [LEAST_PRIVILEGE]
- **Fail Secure**: [FAIL_SECURE]
- **Security by Design**: [SECURITY_BY_DESIGN]
- **Separation of Duties**: [SEPARATION_OF_DUTIES]
- **Complete Mediation**: [COMPLETE_MEDIATION]
- **Open Design**: [OPEN_DESIGN]
- **Psychological Acceptability**: [PSYCHOLOGICAL_ACCEPTABILITY]
- **Work Factor**: [WORK_FACTOR]

### Identity and Access Management
- **Identity Strategy**: [IDENTITY_STRATEGY]
- **Authentication Methods**: [AUTHENTICATION_METHODS]
- **Authorization Model**: [AUTHORIZATION_MODEL]
- **Identity Providers**: [IDENTITY_PROVIDERS]
- **Single Sign-On**: [SINGLE_SIGN_ON]
- **Multi-Factor Authentication**: [MULTI_FACTOR_AUTHENTICATION]
- **Privileged Access Management**: [PRIVILEGED_ACCESS_MANAGEMENT]
- **Identity Governance**: [IDENTITY_GOVERNANCE]
- **Access Reviews**: [ACCESS_REVIEWS]
- **Identity Federation**: [IDENTITY_FEDERATION]

### Network Security Architecture
- **Network Segmentation**: [NETWORK_SEGMENTATION]
- **Perimeter Defense**: [PERIMETER_DEFENSE]
- **Internal Network Security**: [INTERNAL_NETWORK_SECURITY]
- **Remote Access**: [REMOTE_ACCESS]
- **Wireless Security**: [WIRELESS_SECURITY]
- **Network Monitoring**: [NETWORK_MONITORING]
- **Intrusion Detection**: [INTRUSION_DETECTION]
- **Intrusion Prevention**: [INTRUSION_PREVENTION]
- **Network Access Control**: [NETWORK_ACCESS_CONTROL]
- **DDoS Protection**: [DDOS_PROTECTION]

### Application Security Architecture
- **Secure Development**: [SECURE_DEVELOPMENT]
- **Application Security Testing**: [APPLICATION_SECURITY_TESTING]
- **Runtime Protection**: [RUNTIME_PROTECTION]
- **API Security**: [API_SECURITY]
- **Web Application Firewall**: [WEB_APPLICATION_FIREWALL]
- **Code Analysis**: [CODE_ANALYSIS]
- **Dependency Management**: [DEPENDENCY_MANAGEMENT]
- **Container Security**: [CONTAINER_SECURITY]
- **Serverless Security**: [SERVERLESS_SECURITY]
- **Mobile Application Security**: [MOBILE_APPLICATION_SECURITY]

### Data Security Architecture
- **Data Classification**: [DATA_CLASSIFICATION]
- **Data Protection**: [DATA_PROTECTION]
- **Encryption Strategy**: [ENCRYPTION_STRATEGY]
- **Key Management**: [KEY_MANAGEMENT]
- **Data Loss Prevention**: [DATA_LOSS_PREVENTION]
- **Database Security**: [DATABASE_SECURITY]
- **Backup Security**: [BACKUP_SECURITY]
- **Data Masking**: [DATA_MASKING]
- **Data Retention**: [DATA_RETENTION]
- **Data Governance**: [SECURITY_DATA_GOVERNANCE]

Please provide detailed architecture diagrams, security controls mapping, implementation guides, and governance frameworks.

## Usage Examples

### Cloud Security Architecture
```
Design comprehensive security architecture for CloudFirst multi-cloud environment supporting zero trust security objectives with hybrid workforce business context.

Security Architecture Overview:
- Multi-cloud security architecture for AWS, Azure, GCP platforms
- Implement zero trust, defense in depth security objectives
- Support remote workforce, cloud migration business context
- Address APT, ransomware, insider threat landscape
- Ensure SOC2, ISO27001 regulatory requirements

Zero Trust Implementation:
- Never trust, always verify zero trust principles
- Implement continuous verification, least privilege access
- Use identity-centric security model identity strategy
- Deploy SAML, OAuth 2.0, certificate authentication methods
- Apply RBAC, ABAC authorization model with dynamic policies

### Network Security Architecture
- Implement micro-segmentation network segmentation
- Deploy cloud WAF, DDoS protection perimeter defense
- Use VPC flow logs, SIEM network monitoring
- Implement cloud CASB, SWG for remote access
- Deploy NIDS/NIPS intrusion detection systems

### Data Security Architecture
- Classify data as public, internal, confidential, restricted
- Encrypt data at rest with AES-256, in transit with TLS 1.3
- Implement FIPS 140-2 Level 3 HSM key management
- Deploy cloud DLP data loss prevention across SaaS/IaaS
- Apply tokenization, format-preserving encryption data masking
```

## Variables

### Core Architecture Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ARCHITECTURE_NAME]` | Descriptive name for the security architecture | "Enterprise Zero Trust Architecture", "Cloud-First Security Framework" |
| `[SECURITY_OBJECTIVES]` | Primary goals the architecture aims to achieve | "Protect customer data, achieve SOC 2 compliance, enable secure remote work" |
| `[BUSINESS_CONTEXT]` | Business drivers and constraints shaping security decisions | "Hybrid workforce, cloud migration, M&A integration, rapid growth" |
| `[THREAT_LANDSCAPE]` | Key threats the organization faces | "Ransomware, nation-state APT, insider threats, supply chain attacks" |
| `[REGULATORY_REQUIREMENTS]` | Compliance frameworks that must be addressed | "SOC 2 Type II, GDPR, HIPAA, PCI-DSS, ISO 27001" |
| `[RISK_PROFILE]` | Organization's risk tolerance and exposure level | "Low tolerance (financial services)", "Medium (tech startup)", "High (research)" |
| `[ARCHITECTURE_SCOPE]` | What systems and environments are covered | "All production systems, cloud infrastructure, remote endpoints" |
| `[SECURITY_TECHNOLOGY_STACK]` | Core security tools and platforms | "CrowdStrike EDR, Splunk SIEM, Okta IAM, Palo Alto firewalls" |
| `[ARCHITECTURE_BUDGET]` | Total investment allocated for implementation | "$2M initial, $500K annual", "$50K for startup" |
| `[ARCHITECTURE_TIMELINE]` | Implementation schedule | "18 months phased rollout", "6-month MVP" |

### Security Principles

| Variable | Description | Example |
|----------|-------------|----------|
| `[DEFENSE_IN_DEPTH]` | Layered security controls approach | "7 layers: perimeter, network, endpoint, application, data, identity, physical" |
| `[ZERO_TRUST]` | Never trust, always verify implementation | "Verify every access request regardless of source, continuous authentication" |
| `[LEAST_PRIVILEGE]` | Minimum necessary access approach | "Role-based access with just-in-time elevation, 90-day access reviews" |
| `[FAIL_SECURE]` | Behavior when controls fail | "Default deny on firewall failure, lock accounts on suspicious activity" |
| `[SECURITY_BY_DESIGN]` | How security is built into systems | "Threat modeling in design phase, security gates in SDLC, secure defaults" |
| `[SEPARATION_OF_DUTIES]` | Role separation requirements | "No single admin can deploy to production, 4-eyes principle for privileged ops" |

### Identity and Access Management

| Variable | Description | Example |
|----------|-------------|----------|
| `[IDENTITY_STRATEGY]` | Overall approach to identity management | "Identity-centric security model, single source of truth in Okta" |
| `[AUTHENTICATION_METHODS]` | Supported authentication approaches | "SAML 2.0, OAuth 2.0, FIDO2/WebAuthn, certificate-based" |
| `[AUTHORIZATION_MODEL]` | Access control methodology | "RBAC for standard access, ABAC for dynamic policies, PBAC for sensitive data" |
| `[IDENTITY_PROVIDERS]` | Systems managing identities | "Okta (workforce), Azure AD B2C (customers), AWS IAM (cloud)" |
| `[MULTI_FACTOR_AUTHENTICATION]` | MFA implementation details | "Mandatory for all users, hardware keys for admins, push notifications" |
| `[PRIVILEGED_ACCESS_MANAGEMENT]` | Admin access controls | "CyberArk for credential vaulting, session recording, just-in-time access" |

### Network Security

| Variable | Description | Example |
|----------|-------------|----------|
| `[NETWORK_SEGMENTATION]` | How networks are divided | "Micro-segmentation with VMware NSX, separate VLANs for PCI scope" |
| `[PERIMETER_DEFENSE]` | Edge protection mechanisms | "Next-gen firewall, WAF, DDoS protection, geo-blocking" |
| `[REMOTE_ACCESS]` | Secure connectivity for remote users | "ZTNA via Zscaler, no traditional VPN, device posture checks" |
| `[INTRUSION_DETECTION]` | Threat detection capabilities | "Network IDS at all egress points, behavioral analytics, honeypots" |
| `[DDOS_PROTECTION]` | Volumetric attack mitigation | "Cloudflare for edge protection, rate limiting, traffic scrubbing" |

### Application Security

| Variable | Description | Example |
|----------|-------------|----------|
| `[SECURE_DEVELOPMENT]` | Secure coding practices | "OWASP guidelines, security training for devs, peer code review" |
| `[APPLICATION_SECURITY_TESTING]` | Testing methodologies | "SAST in CI/CD, weekly DAST scans, annual penetration testing" |
| `[API_SECURITY]` | API protection measures | "API gateway with rate limiting, OAuth 2.0, schema validation" |
| `[WEB_APPLICATION_FIREWALL]` | Web application protection | "AWS WAF with OWASP Core Rule Set, custom rules for business logic" |
| `[CONTAINER_SECURITY]` | Container and orchestration security | "Image scanning, runtime protection, network policies in Kubernetes" |

### Data Security

| Variable | Description | Example |
|----------|-------------|----------|
| `[DATA_CLASSIFICATION]` | How data is categorized | "4 tiers: Public, Internal, Confidential, Restricted (auto-classification)" |
| `[ENCRYPTION_STRATEGY]` | Cryptographic approach | "AES-256 at rest, TLS 1.3 in transit, HSM for key storage" |
| `[KEY_MANAGEMENT]` | Cryptographic key handling | "AWS KMS for cloud, on-prem HSM, annual key rotation" |
| `[DATA_LOSS_PREVENTION]` | Data exfiltration prevention | "Microsoft DLP for endpoints, network DLP at egress, CASB for cloud" |
| `[DATA_RETENTION]` | Data lifecycle management | "7-year retention for financial, 90-day logs, GDPR deletion compliance" |



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Security Architecture Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Cybersecurity](../../technology/Cybersecurity/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating design comprehensive security architecture including security design principles, defensive strategies, implementation patterns, and governance frameworks for enterprise security systems.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Align security architecture with business objectives**
2. **Apply defense in depth and zero trust principles**
3. **Design for scalability and adaptability**
4. **Integrate security controls throughout the architecture**
5. **Maintain architecture documentation and governance**