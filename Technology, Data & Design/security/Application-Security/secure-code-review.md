---
category: security
title: Secure Code Review Framework
tags:
- security
- secure-code-review
- sast
- owasp
use_cases:
- Conducting security-focused code reviews identifying SQL injection, XSS, authentication bypass, CSRF, cryptographic failures with OWASP Top 10 and CWE Top 25 validation
- Implementing secure coding practices in development workflows with SAST integration (SonarQube/Checkmarx/Semgrep), pre-commit hooks, security gates
- Training development teams on secure coding with hands-on code review exercises, vulnerability remediation workshops, CERT/OWASP guidelines
- Automating security checks in CI/CD pipelines with SAST/SCA/secrets detection, blocking critical vulnerabilities before deployment
related_templates:
- security/Cybersecurity/security-audit.md
- technology/Software-Development/code-review.md
industries:
- finance
- government
- healthcare
- manufacturing
- technology
type: framework
difficulty: intermediate
slug: secure-code-review
---

# Secure Code Review Framework

## Purpose
Comprehensive framework for conducting security-focused code reviews, identifying vulnerabilities (OWASP Top 10, CWE Top 25), implementing secure coding practices, and integrating security checks into development workflows to prevent security issues before deployment.

## 🚀 Quick Secure Code Review Prompt

> Review **{LANGUAGE/FRAMEWORK}** code for security vulnerabilities. Focus: authentication/session management, input validation, SQL/command injection, XSS, CSRF, cryptography usage, secrets handling, access control. Check against **OWASP Top 10** and **CWE Top 25**. Provide: findings with severity (Critical/High/Medium/Low), vulnerable code snippets, remediation code examples, CI/CD security gate recommendations.

---

## Template

Review {LANGUAGE} codebase ({LOC} lines) for {APPLICATION_TYPE} application with {AUTHENTICATION_METHOD} authentication handling {DATA_SENSITIVITY} data under {COMPLIANCE_REQUIREMENTS} compliance.

**SECURITY REVIEW AREAS**

Authentication/Authorization—Check password hashing (bcrypt/Argon2 with salt), session management (HTTPOnly/Secure flags, CSRF tokens, timeout enforcement), authorization on sensitive operations (RBAC/ABAC enforcement), JWT validation (signature verification, expiration checks, secure algorithms RS256/ES256), MFA for privileged accounts, authentication bypass risks (logic flaws, SQL injection in login).

Input Validation/Sanitization—Server-side validation for all user input (never trust client-side), parameterized queries (prevent SQL injection), output encoding for context (HTML entity encoding, JavaScript escaping, URL encoding), command injection prevention (avoid shell execution, use safer APIs), path traversal checks (canonicalize paths, validate against allowlist), file upload validation (MIME type, magic bytes, size limits, virus scanning), XML/JSON injection prevention (schema validation, disable external entities).

Cryptographic Controls—Algorithm strength (AES-256, RSA-2048+, reject MD5/SHA1/DES), TLS 1.2+ enforcement (disable SSLv3/TLS1.0), secure random generation (cryptographic PRNG not Math.random()), key management (vault storage, rotation policies, no hardcoded keys), certificate validation (hostname verification, CA chain validation, OCSP/CRL checking), sensitive data encryption at rest and in transit.

API Security—Authentication on all endpoints (no unauthenticated by default), rate limiting per user/IP (prevent brute force, DoS), input validation with schema (OpenAPI validation), error messages sanitized (no stack traces, internal details), CORS properly configured (specific origins not wildcard in production), GraphQL query complexity limits (depth, cost analysis), REST authorization checks (not just authentication).

Data Protection—Sensitive data identification (PII, PHI, credentials, tokens), encryption at rest (database-level, file-level), no sensitive data in logs (mask passwords, tokens, SSNs), secure data retention/disposal, database connection encryption (TLS for PostgreSQL/MySQL), backup encryption, data access logging for audit trails.

Error Handling/Logging—Generic error messages to users (no technical details), security event logging (login failures, access denials, permission escalations), log injection prevention (sanitize user input in logs), no sensitive data in logs (passwords, tokens, credit cards), centralized logging with integrity protection, log retention policies.

Dependencies/Supply Chain—SCA scanning (Snyk, OWASP Dependency-Check, npm audit), outdated libraries flagged (critical vulnerabilities patched), dependency pinning (lock files, hash verification), integrity checks (subresource integrity, package signatures), license compliance, minimal dependencies (reduce attack surface).

Configuration/Secrets—No hardcoded credentials (scan with TruffleHog, GitGuardian), secrets in vault (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault), environment-specific configs separated (dev/staging/prod), debug mode disabled in production (no verbose errors, profiling), default credentials changed, security headers enabled (CSP, HSTS, X-Frame-Options).

Business Logic—Race conditions in critical operations (use transactions, locks), integer overflow checks (financial calculations, array indexing), privilege escalation paths (vertical/horizontal), price manipulation prevention (server-side validation), account enumeration prevention (consistent error messages, rate limiting), workflow bypasses (state machine validation).

**OWASP TOP 10 VALIDATION**

A01 Broken Access Control—Verify authorization checks on every sensitive operation (not just authentication), horizontal privilege checks (user can't access other users' data), vertical privilege checks (regular users can't admin functions), direct object reference protection (UUIDs or access validation), missing function level access control.

A02 Cryptographic Failures—Strong algorithms only (AES-256, RSA-2048+), TLS 1.2+ for transit, encryption at rest for sensitive data, secure key management (rotation, vault storage), no weak hashing (MD5, SHA1), proper random generation.

A03 Injection—Parameterized queries for SQL (no string concatenation), output encoding for XSS (context-aware), command injection prevention (avoid shell calls), LDAP/XML/NoSQL injection checks, ORM usage validation (still vulnerable if misused).

A04 Insecure Design—Threat modeling evidence, security requirements defined, defense in depth layers, failure modes analyzed (fail securely), business logic security, rate limiting on sensitive workflows.

A05 Security Misconfiguration—Secure defaults, unnecessary features disabled (directory listing, debug endpoints), security headers configured (CSP, HSTS, X-Frame-Options), dependencies updated, cloud storage properly secured (S3 buckets not public), error handling doesn't leak info.

A06 Vulnerable Components—All dependencies scanned (SCA tools), critical CVEs patched within SLA (7 days critical, 30 days high), no end-of-life libraries, dependency versions pinned, integrity verification.

A07 Authentication Failures—Strong password policies, MFA for sensitive accounts, account lockout after failed attempts (5-10 tries), session timeout enforcement, credential stuffing prevention (rate limiting), secure password reset (token-based, not security questions).

A08 Software/Data Integrity—Code signing, secure CI/CD pipelines, dependency integrity checks (lock files, SRI), no auto-update without verification, deserialization of untrusted data prevented.

A09 Logging/Monitoring Failures—Security events logged (authentication, authorization, input validation failures), logs protected from tampering, alerting on suspicious activity, log retention compliance, no sensitive data in logs.

A10 SSRF—URL validation (allowlist domains), disable unnecessary protocols (file://, gopher://), network segmentation (API servers isolated), DNS rebinding protection, cloud metadata endpoint protection (169.254.169.254).

Deliver secure code review as:

1. **EXECUTIVE SUMMARY** - Overall security posture, critical/high vulnerability count, risk rating
2. **FINDINGS BY SEVERITY** - Critical/High/Medium/Low with code snippets, OWASP/CWE classification, exploitability
3. **REMEDIATION EXAMPLES** - Before/after code, specific fixes, library upgrades, configuration changes
4. **PRIORITY ROADMAP** - Fix order, estimated effort, dependencies, timeline
5. **PREVENTIVE MEASURES** - Developer training topics, SAST tool integration, secure coding standards

---

## Usage Examples

### Example 1: Node.js Authentication Module Review
**Prompt:** Review Node.js authentication module (auth/login.js, auth/register.js, middleware/auth.js, ~1200 LOC) for web app with JWT authentication, PostgreSQL, handling PII under GDPR/SOC2.

**Output:** Authentication Issues—Password hashing using bcrypt rounds=10 (adequate), but missing pepper (add server-side secret), password reset tokens expire in 24 hours (reduce to 1 hour), JWT signed with HS256 symmetric key (upgrade to RS256 asymmetric for key rotation), refresh tokens not rotated on use (implement rotation to limit replay window). Session Management—HTTPOnly/Secure flags set correctly, SameSite=Strict prevents CSRF, session timeout 15 minutes (good), but no absolute timeout (add 8-hour max session age). Authorization—Middleware validates JWT signature and expiration, but doesn't verify user still exists (add user lookup), role checks missing on admin endpoints (add RBAC middleware to /admin/*). SQL Injection—All queries use parameterized statements via pg library (good), but one instance of string concatenation in search (line 247: `SELECT * FROM users WHERE name LIKE '%${req.query.q}%'`—change to parameterized). Input Validation—Email validation uses regex (acceptable), password complexity enforced client-side only (add server-side zxcvbn strength check), no rate limiting on login endpoint (add express-rate-limit: 5 attempts/15 min). Secrets—JWT secret in .env file (good), but .env.example includes placeholder secret (remove, add .env to .gitignore verification). Dependencies—jsonwebtoken 8.5.1 has moderate severity CVE (upgrade to 9.0.0), bcrypt 5.0.1 current, express 4.17.1 has info-level advisory (upgrade to 4.18.2). Remediation Priority—Critical: Parameterize search query (1 hour), High: Upgrade to RS256 JWT (4 hours), implement rate limiting (2 hours), Medium: Add server-side password strength (3 hours), rotate refresh tokens (5 hours). Tools—Integrate Snyk for dependency scanning, Semgrep for SAST (detect SQL injection patterns), pre-commit hook blocks hardcoded secrets.

### Example 2: Python API Security Review (FastAPI)
**Prompt:** Review Python FastAPI application (18 endpoints, ~2400 LOC) handling healthcare PHI with OAuth 2.0, MongoDB, HIPAA compliance.

**Output:** OAuth Implementation—Authorization code flow with PKCE correctly implemented, token expiration 15 minutes (good), refresh tokens stored hashed in MongoDB (excellent), but revocation endpoint missing (add /oauth/revoke per RFC 7009). Authorization—Scopes validated on endpoints (read:patients, write:prescriptions), but one admin endpoint missing scope check (line 512: @router.get("/admin/users") lacks dependency=Security(has_scope, scopes=["admin:users"])). NoSQL Injection—MongoDB queries use parameterized filters (good), but aggregation pipeline in analytics endpoint accepts raw user input (line 892: db.aggregate(json.loads(req.body))—validate against schema, reject $where operators). Data Exposure—PHI fields (diagnosis, medications) returned in list endpoints (violate minimum necessary principle—implement sparse fieldsets, exclude PHI unless explicitly requested). Logging—All PHI access logged with patient_id, user_id, timestamp, IP (excellent HIPAA compliance), but one error handler logs full request body (line 156: logger.error(f"Error: {request.body}")—mask PHI fields). Encryption—TLS 1.3 enforced, MongoDB connections use TLS (good), but patient records not encrypted at rest (enable MongoDB encryption at rest or field-level encryption for PHI fields). Dependencies—FastAPI 0.95.1 current, Pydantic 1.10.2 has CVE-2022-4135 (upgrade to 2.x for validation bypass fix), cryptography 38.0.1 has high severity CVE (upgrade to 41.0.0). Configuration—JWT secret from environment variable (good), MongoDB credentials from AWS Secrets Manager (excellent), but debug mode enabled in production Dockerfile (ENV DEBUG=1—remove). Testing—Unit tests for auth flows exist, but no security-specific tests (add: expired token rejection, scope validation, injection attempts, rate limit enforcement). Remediation—Critical: Disable debug mode (immediate), upgrade cryptography library (2 hours), High: Implement sparse fieldsets for PHI (8 hours), add OAuth revocation (4 hours), Medium: NoSQL injection validation (6 hours), security test suite (12 hours). BAA—Ensure BAA signed with MongoDB Atlas, AWS (hosting), log retention 7 years, breach notification procedures documented.

### Example 3: Java Microservices Security Review (Spring Boot)
**Prompt:** Review Spring Boot microservices (12 services, ~15K LOC) with mTLS, Kafka messaging, PostgreSQL, financial transactions, SOX compliance.

**Output:** mTLS Configuration—Service mesh (Istio) enforces mTLS for all service-to-service (good), certificate rotation every 90 days (good), but one service has allowPermissiveMode enabled (payment-service—enforce STRICT mode). Service Authorization—Istio AuthorizationPolicy defines allowed service pairs (good), but catch-all rule allows all internal traffic in namespace (remove default allow, explicit deny by default). API Security—All REST endpoints require JWT from API gateway (good), GraphQL endpoint in reporting-service has introspection enabled (disable in production), rate limiting at gateway (Kong) but not at service level (add resilience4j rate limiter for defense in depth). SQL Injection—JPA/Hibernate used for all queries (good), but one native query in ledger-service uses string formatting (line 2,341: `entityManager.createNativeQuery("SELECT * FROM transactions WHERE account_id = " + accountId)`—use setParameter). Kafka Security—SASL_SSL authentication enabled (good), ACLs restrict topic access (good), but messages not encrypted at application level (add encryption for PII in transit even with TLS). Transaction Integrity—Financial calculations use BigDecimal (good), atomic transactions via @Transactional (good), but one race condition in concurrent fund transfer (lines 1,523-1,547—implement optimistic locking with @Version). Logging—All financial transactions logged (transaction_id, amount, accounts, timestamp, service) to Splunk (good), 7-year retention (SOX compliant), but one service logs full Kafka message including account numbers (reporting-service line 892—mask account numbers). Dependencies—Spring Boot 2.7.14 (upgrade to 3.x for extended support), Log4j 2.17.1 (current, post-Log4Shell), PostgreSQL JDBC 42.5.1 has moderate CVE (upgrade to 42.6.0). Secrets Management—All secrets from HashiCorp Vault (excellent), dynamic database credentials (good), but API keys for third-party service hardcoded in config map (move to Vault, rotate immediately). Testing—Integration tests cover happy paths, but security tests missing (add: SQL injection attempts, authorization bypass, concurrent transaction conflicts, circuit breaker validation). SOX Controls—Access logging (good), segregation of duties (payment-service can't call admin-service, enforced by Istio), change management (all deployments via GitOps with ArgoCD, audit trail). Remediation—Critical: Remove hardcoded API key (immediate), fix SQL injection (2 hours), enforce mTLS STRICT (1 hour), High: Add optimistic locking (6 hours), disable GraphQL introspection (30 min), Medium: Upgrade Spring Boot (16 hours testing), add message encryption (8 hours). SAST Integration—Checkmarx scan weekly, Snyk in CI/CD blocks critical/high, SonarQube quality gates (80% coverage, 0 blocker issues).

---

## Cross-References

- [Security Audit](../Cybersecurity/security-audit.md) - Comprehensive security assessment beyond code review
- [Code Review](../../technology/Software-Development/code-review.md) - General code review practices
