---
category: security
last_updated: 2025-11-11
title: Secure Code Review Framework
tags:
- security
- development
- testing
- automation
use_cases:
- Conducting security-focused code reviews to identify vulnerabilities
- Implementing secure coding practices in development workflows
- Training development teams on security best practices
- Automating security checks in CI/CD pipelines
related_templates:
- security/Cybersecurity/security-audit.md
- technology/Software-Development/code-review.md
industries:
- finance
- government
- healthcare
- manufacturing
- technology
type: template
difficulty: intermediate
slug: secure-code-review
---

# Secure Code Review Framework

## Purpose
Comprehensive framework for conducting security-focused code reviews, identifying vulnerabilities, implementing secure coding practices, and integrating security checks into development workflows to prevent security issues before deployment.

## Quick Start

**Need to review code for security vulnerabilities quickly?** Use this minimal example:

### Minimal Example
```
Review a new authentication module in our web application for security vulnerabilities, focusing on common issues like SQL injection, XSS, authentication bypass, and insecure session management. The module handles user login, password reset, and session management using JWT tokens.
```

### When to Use This
- Reviewing code changes before merging to production
- Conducting security audits of existing codebases
- Training developers on secure coding practices
- Implementing security gates in CI/CD pipelines

### Basic 3-Step Workflow
1. **Identify Risk Areas** - Focus on authentication, authorization, data validation, cryptography, and external integrations (15-30 min)
2. **Review Against Standards** - Check code against OWASP Top 10, CWE Top 25, and language-specific security guidelines (30-60 min)
3. **Document and Remediate** - Create actionable remediation plan with severity ratings and fix timelines (20-40 min)

**Time to complete**: 1-2 hours for focused review, 4-8 hours for comprehensive audit

---

## Template

```markdown
I need to conduct a comprehensive secure code review. Please provide detailed security analysis and recommendations.

## CODE REVIEW CONTEXT

### Application Information
- Application type: [WEB_APP_MOBILE_API_MICROSERVICE_DESKTOP_IOT]
- Technology stack: [LANGUAGES_FRAMEWORKS_LIBRARIES]
- Authentication method: [JWT_SESSION_OAUTH_SAML_API_KEY_NONE]
- Database: [POSTGRESQL_MYSQL_MONGODB_DYNAMODB_OTHER]
- Deployment environment: [CLOUD_ON_PREM_HYBRID_CONTAINER_SERVERLESS]
- User base: [INTERNAL_EXTERNAL_PUBLIC_B2B_B2C]
- Data sensitivity: [PUBLIC_INTERNAL_CONFIDENTIAL_HIGHLY_SENSITIVE_PII_PHI]
- Compliance requirements: [PCI_DSS_HIPAA_GDPR_SOC2_NONE]

### Code Scope
- Files/modules under review: [SPECIFIC_FILES_OR_MODULES]
- Lines of code: [APPROXIMATE_LOC]
- Review type: [PRE_COMMIT_MERGE_REQUEST_FULL_AUDIT_TARGETED_REVIEW]
- Focus areas: [AUTH_DATA_VALIDATION_CRYPTO_API_DATABASE_FILE_HANDLING]
- Recent changes: [NEW_FEATURE_BUG_FIX_REFACTOR_MIGRATION]
- Known issues: [EXISTING_VULNERABILITIES_TECHNICAL_DEBT]

### Security Context
- Previous security findings: [NONE_MINOR_MODERATE_CRITICAL]
- Last security review: [DATE_OR_NEVER]
- Static analysis tools used: [SONARQUBE_CHECKMARX_SEMGREP_SNYK_NONE]
- Security training level: [NOVICE_INTERMEDIATE_ADVANCED_SECURITY_CERTIFIED]
- Threat model exists: [YES_NO_IN_PROGRESS]
- Security requirements defined: [YES_NO_PARTIAL]

## SECURITY REVIEW AREAS

### 1. Authentication & Authorization
Please review for:
- Authentication mechanisms (login, password reset, MFA, SSO)
- Password storage and handling (hashing, salting, complexity)
- Session management (creation, validation, expiration, invalidation)
- Authorization controls (RBAC, ABAC, permission checks)
- Token handling (JWT validation, refresh tokens, API keys)
- Authentication bypass vulnerabilities

Key questions:
- Are passwords properly hashed with strong algorithms (bcrypt, Argon2)?
- Is session management secure (HTTPOnly, Secure flags, CSRF protection)?
- Are authorization checks performed on every sensitive operation?
- Is MFA implemented for privileged accounts?

### 2. Input Validation & Data Sanitization
Please review for:
- User input validation (client and server-side)
- SQL injection prevention (parameterized queries, ORM usage)
- XSS prevention (output encoding, CSP headers)
- Command injection prevention
- Path traversal prevention
- XML/JSON injection prevention
- File upload validation (type, size, content)

Key questions:
- Is all user input validated before processing?
- Are parameterized queries used for all database operations?
- Is output properly encoded for the context (HTML, JavaScript, URL)?
- Are file uploads restricted by type, size, and content validation?

### 3. Cryptographic Controls
Please review for:
- Encryption algorithms and key lengths
- Secure random number generation
- Certificate validation (SSL/TLS)
- Sensitive data encryption (at rest and in transit)
- Key management practices
- Cryptographic library usage

Key questions:
- Are modern, secure algorithms used (AES-256, RSA-2048+)?
- Is TLS 1.2+ enforced for all network communications?
- Are encryption keys properly managed and rotated?
- Is cryptographic randomness properly generated?

### 4. API Security
Please review for:
- API authentication and authorization
- Rate limiting and throttling
- Input validation on API endpoints
- Error handling and information disclosure
- CORS configuration
- API versioning and deprecation
- GraphQL/REST security best practices

Key questions:
- Are all API endpoints authenticated and authorized?
- Is rate limiting implemented to prevent abuse?
- Are error messages sanitized to prevent information disclosure?
- Is CORS properly configured?

### 5. Data Protection
Please review for:
- Sensitive data identification and classification
- Data encryption (in transit and at rest)
- Logging of sensitive information
- Data retention and disposal
- Personally Identifiable Information (PII) handling
- Database security configuration
- Backup security

Key questions:
- Is sensitive data encrypted at rest and in transit?
- Are logs free of passwords, tokens, and PII?
- Is data access logged and monitored?
- Are database connections encrypted?

### 6. Error Handling & Logging
Please review for:
- Exception handling completeness
- Error message information disclosure
- Stack trace exposure
- Logging of security events
- Log injection prevention
- Sensitive data in logs

Key questions:
- Are generic error messages returned to users?
- Are security events (login failures, access denials) logged?
- Are logs protected from unauthorized access?
- Is log injection prevented through sanitization?

### 7. Dependencies & Third-Party Code
Please review for:
- Vulnerable dependencies (SCA scanning)
- Outdated libraries and frameworks
- Dependency pinning and integrity checks
- Supply chain security
- License compliance

Key questions:
- Are all dependencies up to date with security patches?
- Are dependency versions pinned to prevent supply chain attacks?
- Are integrity checks (checksums, signatures) verified?
- Are vulnerable dependencies identified and remediated?

### 8. Configuration & Secrets Management
Please review for:
- Hardcoded credentials and secrets
- Configuration file security
- Environment variable usage
- Secrets management (vault, key management)
- Default configurations
- Debug mode in production

Key questions:
- Are secrets stored in secure vaults, not in code?
- Are environment-specific configurations properly separated?
- Is debug mode disabled in production?
- Are default credentials changed?

### 9. Business Logic Vulnerabilities
Please review for:
- Race conditions and TOCTOU issues
- Integer overflow/underflow
- Logic flaws in workflows
- Privilege escalation opportunities
- Price manipulation
- Account enumeration

Key questions:
- Are critical operations atomic and thread-safe?
- Are numerical operations checked for overflow?
- Can users manipulate workflows to gain unauthorized access?
- Are financial calculations secure from manipulation?

### 10. OWASP Top 10 Coverage
Please specifically review against:
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

## SECURE CODING STANDARDS

### Code Quality Requirements
- Follow language-specific secure coding guidelines (CERT, OWASP)
- Use security-focused linters and static analysis
- Implement defense in depth
- Apply principle of least privilege
- Fail securely and safely

### Testing Requirements
- Unit tests for security controls
- Integration tests for authentication/authorization
- Security-specific test cases
- Negative testing (invalid inputs, boundary conditions)
- Automated security tests in CI/CD

## REMEDIATION GUIDANCE

For each vulnerability identified, please provide:

1. **Vulnerability Description**
   - Technical explanation of the issue
   - OWASP/CWE classification
   - Affected code location (file, line numbers)

2. **Risk Assessment**
   - Severity: [CRITICAL_HIGH_MEDIUM_LOW_INFO]
   - Exploitability: [EASY_MODERATE_DIFFICULT]
   - Impact: [HIGH_MEDIUM_LOW]
   - CVSS score (if applicable)

3. **Proof of Concept**
   - How the vulnerability can be exploited
   - Example attack scenario

4. **Remediation Steps**
   - Specific code changes required
   - Secure coding examples
   - Configuration changes
   - Library upgrades

5. **Prevention**
   - How to prevent similar issues in future
   - Developer training recommendations
   - Tool recommendations

## OUTPUT REQUIREMENTS

Please provide:

1. **Executive Summary**
   - Overview of security posture
   - Critical/High vulnerabilities count
   - Overall risk rating

2. **Detailed Findings**
   - Each vulnerability with full details
   - Organized by severity
   - Code snippets showing issues
   - Remediation code examples

3. **Secure Code Examples**
   - Before/After comparisons
   - Best practice implementations
   - Language-specific recommendations

4. **Remediation Roadmap**
   - Prioritized action items
   - Estimated fix effort
   - Dependencies between fixes
   - Timeline recommendations

5. **Security Hardening Checklist**
   - Additional security improvements
   - Security controls to implement
   - Configuration hardening steps

6. **Developer Training Recommendations**
   - Topics for security training
   - Common mistakes observed
   - Resources and references

## Additional Context
[Add any specific concerns, previous vulnerabilities, or areas requiring special attention]
```

---

## Example: Web Application Authentication Review

```markdown
I need to conduct a comprehensive secure code review.

## CODE REVIEW CONTEXT

### Application Information
- Application type: WEB_APP
- Technology stack: Node.js, Express, React, PostgreSQL
- Authentication method: JWT with refresh tokens
- Database: POSTGRESQL
- Deployment environment: AWS ECS containers
- User base: EXTERNAL (B2C)
- Data sensitivity: CONFIDENTIAL (includes PII)
- Compliance requirements: GDPR, SOC2

### Code Scope
- Files/modules under review: auth/login.js, auth/register.js, auth/passwordReset.js, middleware/auth.js
- Lines of code: ~1200 LOC
- Review type: MERGE_REQUEST
- Focus areas: AUTH, DATA_VALIDATION, CRYPTO, DATABASE
- Recent changes: NEW_FEATURE (added OAuth integration)
- Known issues: None reported

### Security Context
- Previous security findings: MINOR (XSS in error messages - fixed)
- Last security review: 2025-09-15
- Static analysis tools used: SNYK, ESLint security plugin
- Security training level: INTERMEDIATE
- Threat model exists: YES
- Security requirements defined: YES

[Rest of template filled in...]
```

---

## Best Practices

### Before Review
1. Understand application architecture and data flows
2. Review threat model and security requirements
3. Set up development environment for testing
4. Gather previous security findings
5. Configure security analysis tools

### During Review
1. Focus on high-risk areas first (auth, crypto, data handling)
2. Use multiple review methods (manual + automated)
3. Test hypotheses with proof-of-concept code
4. Document findings as you discover them
5. Ask questions when unclear about intent

### After Review
1. Prioritize findings by risk and impact
2. Provide actionable remediation guidance
3. Create tickets for each finding
4. Schedule follow-up review for fixes
5. Update threat model with new findings

### Tools Integration
- **SAST:** SonarQube, Checkmarx, Semgrep, Snyk Code
- **Dependency Scanning:** Snyk, OWASP Dependency-Check, npm audit
- **Secrets Detection:** GitGuardian, TruffleHog, detect-secrets
- **IDE Plugins:** Security linters, vulnerability scanners

---

## Related Resources

- [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/)
- [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/)
- [SANS Secure Coding Guidelines](https://www.sans.org/secure-coding/)
- security/Cybersecurity/security-audit.md
- security/Application-Security/owasp-security-testing.md
- technology/Software-Development/code-review.md
