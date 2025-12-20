---
category: security
title: API Security Framework
tags:
- security
- api-security
- oauth
- owasp-api
use_cases:
- Securing REST/GraphQL/gRPC APIs with OAuth 2.0, rate limiting, input validation preventing OWASP API Top 10 vulnerabilities
- Implementing API gateway security (Kong/Apigee/AWS) with authentication, authorization, threat detection, monitoring
- API security testing with OWASP ZAP, Burp Suite, Postman validating auth, injection, BOLA, rate limiting
related_templates:
- security/Application-Security/secure-code-review.md
- technology/Software-Development/architecture-design.md
industries:
- government
- healthcare
- technology
type: framework
difficulty: intermediate
slug: api-security-framework
---

# API Security Framework

## Purpose
Secure APIs (REST, GraphQL, gRPC, SOAP) implementing authentication/authorization (OAuth 2.0, JWT, mTLS), rate limiting, input validation, encryption preventing OWASP API Top 10 vulnerabilities achieving secure-by-design APIs.

## Template

Secure {API_TYPE} API with {ENDPOINT_COUNT} endpoints handling {DATA_SENSITIVITY} data achieving {COMPLIANCE_REQUIREMENTS} compliance with {TRAFFIC_VOLUME} request load.

**OWASP API SECURITY TOP 10 PROTECTION**

API1 Broken Object Level Authorization (BOLA): Use UUIDs not sequential IDs (prevents enumeration), validate user owns requested resource (not just endpoint access), test with different user credentials attempting access to others' objects, implement resource-level authorization middleware.

API2 Broken Authentication: OAuth 2.0 authorization code flow with PKCE (mobile/SPA), JWT with RS256/ES256 signing (not HS256 symmetric), short token expiration (15 min access, rotate refresh), MFA for sensitive operations, rate limit authentication endpoints (5 failed attempts = account lock).

API3 Broken Object Property Level Authorization: Validate which properties user can read/write (not just object access), schema-based validation (JSON Schema, OpenAPI), prevent mass assignment (explicit field allowlists), separate read/write DTOs.

API4 Unrestricted Resource Consumption: Rate limiting per user/IP/API key (100 req/min standard, 1000/min premium), request size limits (10MB max), timeout enforcement (30 sec), GraphQL query complexity limits (depth <7, complexity <500), circuit breakers prevent cascade failures.

API5 Broken Function Level Authorization: Validate user role for every function (not just authentication), enforce least privilege (read vs write vs admin scopes), separate admin endpoints (/admin/*), test with lower-privilege users attempting admin functions.

API6 Unrestricted Access to Sensitive Business Flows: Identify sensitive workflows (password reset, fund transfer, purchase), business logic rate limiting (3 password resets/hour, 10 purchases/minute), bot detection (CAPTCHA, behavioral analysis), transaction monitoring alerts on anomalies.

API7 Server Side Request Forgery (SSRF): Validate and sanitize URLs (allowlist domains), disable unnecessary protocols (file://, gopher://), network segmentation (API servers can't access internal management), DNS rebinding protection.

API8 Security Misconfiguration: Secure defaults (fail closed), remove debug endpoints in production (/debug, /test), disable directory listing, keep dependencies updated (Dependabot, Snyk), security headers (HSTS, X-Content-Type-Options, CSP).

API9 Improper Inventory Management: Maintain OpenAPI/Swagger documentation, retire old versions securely (v1 sunset after v2 GA + 6 months), monitor for shadow APIs (undocumented endpoints), version in URL (/api/v2) or header.

API10 Unsafe Consumption of APIs: Validate third-party API responses (don't trust external data), encrypt communications (TLS 1.3, certificate pinning), circuit breakers for external API failures, monitor third-party API security advisories.

**AUTHENTICATION AND AUTHORIZATION**

OAuth 2.0 implementation: Authorization code flow (web apps with backend), client credentials flow (service-to-service), PKCE extension (mobile/SPA prevents auth code intercept), token introspection (validate at resource server), revocation endpoint (logout, security incident). JWT best practices: RS256 or ES256 asymmetric signing (public key verification), short expiration (15 min access tokens), refresh token rotation (new refresh on each use), validate issuer and audience claims, store signing keys securely (KMS, Vault).

API keys (for less sensitive use): Secure generation (cryptographically random, 32+ chars), environment separation (dev/staging/prod keys), rotation policy (90 days, immediate on compromise), rate limiting by key (prevent abuse), revocation mechanism (instant invalidation), don't log keys (mask in logs). Mutual TLS (high security): Client certificate authentication, validate certificate chain to trusted CA, check certificate revocation (OCSP), short certificate lifetime (90 days), automated cert management (cert-manager, Vault).

Scope-based authorization: OAuth scopes define permissions (read:orders, write:orders, admin:users), validate required scope on every request, granular scopes (not admin:* but specific permissions), scope inheritance hierarchy, request minimum scopes needed (least privilege).

**API GATEWAY SECURITY**

Centralized security enforcement: Authentication before reaching backend (JWT validation, OAuth introspection), request transformation (sanitize headers, normalize input), schema validation (reject malformed requests), rate limiting and quotas (prevent abuse, DDoS mitigation), IP allowlisting/blocklisting (geofencing, known bad actors). Gateway platforms: Kong (open-source, plugin ecosystem, Kubernetes-native), Apigee (Google Cloud, advanced analytics, monetization), AWS API Gateway (serverless, AWS integration, consumption pricing), Azure API Management (Azure-native, developer portal), Tyk (open-source alternative, GraphQL support).

Threat detection: Anomaly detection (unusual traffic patterns, geographic anomalies), bot detection (behavioral analysis, CAPTCHAs), SQL injection detection (WAF integration), credential stuffing prevention (rate limiting, CAPTCHA escalation), data exfiltration detection (large response sizes, unusual endpoints).

**SECURITY TESTING**

Automated testing: OWASP ZAP API scan (automated vulnerability detection, OpenAPI import), Burp Suite Professional (advanced testing, extensions for APIs), Postman security tests (assertion-based validation, CI/CD integration), API fuzzing (Fuzzapi, RESTler generate invalid inputs), SAST for API code (Checkmarx, SonarQube).

Manual testing scenarios: Authorization bypass (access with different user, without token, with expired token, with tampered JWT), BOLA testing (enumerate IDs, access other users' objects), injection testing (SQL, NoSQL, command injection in all parameters), business logic flaws (negative prices, quantity overflow), rate limit validation (exceed limits, verify 429 responses).

Deliver API security as:

1. **SECURITY ARCHITECTURE** - Auth flow diagrams, API gateway configuration, defense-in-depth layers
2. **OWASP TOP 10 CONTROLS** - Mitigation for each vulnerability, implementation guides, test cases
3. **AUTHENTICATION/AUTHORIZATION** - OAuth 2.0 setup, JWT validation, scope definitions, mTLS config
4. **RATE LIMITING RULES** - Per-endpoint limits, user/IP quotas, sliding window configuration
5. **MONITORING & ALERTS** - Security event logging, anomaly detection, incident response integration

---

## Usage Examples

### Example 1: E-Commerce REST API (PCI-DSS)
**Prompt:** Secure e-commerce REST API (215 endpoints, peak 5K req/sec, PCI-DSS, customer PII + payment tokens).

**Output:** Auth—OAuth 2.0 authorization code for web/mobile, JWT RS256 15-min expiration, scopes (read:products, write:cart, checkout:payment). BOLA—UUIDs for order/cart IDs, middleware validates user ownership before data access. Rate limiting—100/min per user, 1000/min per endpoint, 10/min payment endpoints (stricter), Redis sliding window, 429 with Retry-After header. Payment API hardening—additional MFA step via SMS, request signing with HMAC-SHA256, network isolation (payment services private subnet). Input validation—JSON Schema for all request bodies, whitelist allowed parameters, SQLi prevention via parameterized queries, XSS prevention in product reviews. Gateway—Kong with OAuth 2.0 plugin, rate-limiting plugin, request-transformer, AWS WAF with OWASP CRS + custom rules. Testing—weekly OWASP ZAP automated scan, quarterly manual pentest, BOLA tests with cross-user credentials. Monitoring—Splunk ingestion of all auth failures, rate limit violations, payment anomalies, real-time PagerDuty alerts. Compliance—PCI-DSS Requirement 6.5 (API security), annual QSA validation, no card data storage (tokenization via Stripe).

### Example 2: Healthcare GraphQL API (HIPAA)
**Prompt:** Secure GraphQL API (45 types, 120 queries, HIPAA PHI, mobile apps, 500 req/sec).

**Output:** GraphQL hardening—disable introspection in production (prevents schema discovery), persisted queries only (allowlist approved queries, reject ad-hoc), query depth limit 7, complexity limit 500, timeout 30 sec. Field-level auth—@auth directive on PHI fields (Patient.diagnoses, Prescription.medications), resolver validates user permission per field, deny by default. Mobile security—certificate pinning to leaf cert + backup, PKCE flow for OAuth, biometric authentication, refresh token rotation. Audit logging—every PHI access logged (patient_id, fields_accessed, user_id, timestamp, IP), log retention 7 years (HIPAA), integration with Epic audit trail. Rate limiting—50/min per user, 5/min for sensitive mutations (createPrescription), cost-based limits (complex queries consume more quota). Testing—GraphQL-specific tools (InQL, GraphQL Cop), authorization matrix (user roles × PHI fields), HIPAA Security Rule validation. Compliance—BAA with AWS (hosting), encryption at rest (RDS, S3) and in transit (TLS 1.3), breach notification procedures (<60 days to HHS if >500 patients).

### Example 3: Microservices gRPC (Financial/SOX)
**Prompt:** Secure internal gRPC microservices (35 services, 500 endpoints, mTLS, 50K req/sec, SOX compliance).

**Output:** Zero trust—mTLS for all service-to-service (Istio service mesh), SPIFFE/SPIRE for workload identity, no network-level trust. Service authorization—Istio AuthorizationPolicy explicit allow rules (payment-service can call account-service, ledger-service can call both), deny by default, least privilege. Distributed tracing—Jaeger with correlation IDs (trace requests across services), latency analysis, security event correlation. Circuit breakers—Istio DestinationRule outlier detection (5 consecutive failures = circuit open), prevent cascade failures, graceful degradation. Audit logging—all financial transactions logged (transaction_id, amount, from_account, to_account, timestamp, service_identity), centralized Splunk, 7-year retention (SOX). Testing—service mesh policy testing (verify payment-service can't call admin-service), chaos engineering (failure injection validates circuit breakers), penetration testing of service mesh. Compliance—SOX controls (access logging, segregation of duties, change management), audit evidence (Istio policies as code in Git, log retention proof).

---

## Cross-References

- [Secure Code Review](secure-code-review.md) - Code-level API security validation
- [Architecture Design](../../technology/Software-Development/architecture-design.md) - API architecture patterns
