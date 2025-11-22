---
category: security/Cybersecurity
last_updated: 2025-11-11
title: Threat Modeling Framework
tags:
- security
- design
- risk-assessment
use_cases:
- Identifying security threats in system design
- Proactive security risk assessment
- Security architecture review
- DevSecOps threat analysis
related_templates:
- security/Cybersecurity/security-architecture.md
- security/Application-Security/secure-code-review.md
- technology/Software-Development/architecture-design.md
industries:
- finance
- government
- technology
type: template
difficulty: intermediate
slug: threat-modeling
---

# Threat Modeling Framework

## Purpose
Systematic framework for identifying, analyzing, and mitigating security threats in system design using STRIDE, PASTA, or LINDDUN methodologies for applications, infrastructure, and data flows.

## Quick Start

**Need to model threats quickly?** Use this minimal example:

### Minimal Example
```
Perform threat modeling for our new cloud-based payment processing system using STRIDE methodology. Identify threats to authentication, data flow between web app, API gateway, payment processor, and database. Provide threat scenarios and mitigation strategies.
```

### When to Use This
- Designing new systems or features
- Security architecture review
- Pre-production security validation
- Incident root cause analysis
- Compliance requirements

### Basic 3-Step Workflow
1. **Model the System** - Create architecture diagrams, data flows (1-2 hours)
2. **Identify Threats** - Apply STRIDE or other methodology (2-4 hours)
3. **Mitigate & Validate** - Design countermeasures, validate (2-4 hours)

**Time to complete**: 1-2 days for comprehensive threat model

---

## Template

```markdown
I need to perform threat modeling for my system. Please provide comprehensive threat identification and mitigation guidance.

## SYSTEM CONTEXT

### System Overview
- System name and purpose: [DESCRIPTION]
- System type: [WEB_APP_MOBILE_API_CLOUD_SERVICE_IOT_INFRASTRUCTURE]
- Architecture: [MONOLITH_MICROSERVICES_SERVERLESS_HYBRID]
- Users: [INTERNAL_EXTERNAL_AUTHENTICATED_ANONYMOUS]
- Data sensitivity: [PUBLIC_INTERNAL_CONFIDENTIAL_PII_PHI_PCI]
- Deployment: [CLOUD_ON_PREM_HYBRID]

### Components
- Frontend: [WEB_MOBILE_DESKTOP]
- Backend: [LANGUAGES_FRAMEWORKS]
- APIs: [REST_GRAPHQL_GRPC]
- Databases: [TYPES_PRODUCTS]
- External services: [THIRD_PARTY_INTEGRATIONS]
- Infrastructure: [CLOUD_PROVIDER_SERVICES]

### Data Flows
- User authentication flow
- Data input and processing
- Data storage and retrieval
- External API calls
- Admin operations
- Background jobs

## THREAT MODELING METHODOLOGY

### STRIDE Analysis

For each component, identify:

**Spoofing (Authentication):**
- Can attacker impersonate legitimate user?
- Weak authentication mechanisms
- Missing MFA
- Session hijacking vulnerabilities

**Tampering (Integrity):**
- Can data be modified unauthorized?
- Man-in-the-middle attacks
- Database injection
- API parameter manipulation

**Repudiation (Non-repudiation):**
- Can users deny actions?
- Insufficient logging
- Missing audit trails
- Weak transaction tracking

**Information Disclosure (Confidentiality):**
- Can sensitive data be exposed?
- Data leaks in logs or errors
- Insecure storage
- Unencrypted transmission

**Denial of Service (Availability):**
- Can system be made unavailable?
- Resource exhaustion
- Amplification attacks
- Missing rate limiting

**Elevation of Privilege (Authorization):**
- Can user gain unauthorized access?
- Broken access controls
- Privilege escalation
- Insecure direct object references

### Threat Prioritization

For each threat, rate:
- **Likelihood:** Low / Medium / High
- **Impact:** Low / Medium / High
- **Risk:** Likelihood × Impact
- **Priority:** Critical / High / Medium / Low

## MITIGATION STRATEGIES

For each identified threat, provide:
1. Threat description
2. Attack scenarios
3. Existing controls
4. Recommended mitigations
5. Residual risk
6. Validation methods

## OUTPUT REQUIREMENTS

Provide:
1. System architecture diagram with trust boundaries
2. Data flow diagrams
3. Threat matrix (all threats identified)
4. Risk-prioritized threat list
5. Mitigation recommendations
6. Implementation roadmap
```
