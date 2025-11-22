---
category: security
last_updated: 2025-11-22
title: API Security Framework & Testing
tags:
- security
- development
- testing
- api
use_cases:
- Securing REST, GraphQL, and SOAP APIs
- Implementing API authentication and authorization
- API threat detection and prevention
- API security testing and validation
related_templates:
- security/Application-Security/secure-code-review.md
- technology/Software-Development/architecture-design.md
industries:
- government
- healthcare
- technology
type: template
difficulty: intermediate
slug: api-security-framework
---

# API Security Framework & Testing

## Purpose
Comprehensive framework for securing APIs (REST, GraphQL, SOAP), implementing authentication/authorization, rate limiting, input validation, preventing OWASP API Security Top 10 vulnerabilities, and conducting security testing.

## Quick Start

**Need to secure APIs quickly?** Use this minimal example:

### Minimal Example
```
Secure our REST API with 50+ endpoints handling customer data, implementing OAuth 2.0 authentication, rate limiting, input validation, and protection against injection attacks, broken authentication, and excessive data exposure.
```

### When to Use This
- Designing new API security architecture
- Securing existing APIs before production
- Conducting API security assessments
- Implementing API gateway security controls

### Basic 3-Step Workflow
1. **Identify API Assets** - Document all endpoints, data flows, authentication (30-60 min)
2. **Implement Security Controls** - Auth, rate limiting, validation, encryption (2-4 hours)
3. **Test & Monitor** - Security testing, vulnerability scanning, runtime monitoring (1-2 hours)

**Time to complete**: 4-8 hours for comprehensive API security implementation

---

## Template

```markdown
I need to implement comprehensive API security. Please provide detailed API security design and implementation guidance.

## API CONTEXT

### API Information
- API type: [REST_GRAPHQL_SOAP_GRPC_WEBSOCKET]
- Number of endpoints: [COUNT]
- Authentication method: [OAUTH2_JWT_API_KEY_BASIC_MUTUAL_TLS]
- API consumers: [INTERNAL_EXTERNAL_PARTNER_PUBLIC]
- Data sensitivity: [PUBLIC_INTERNAL_CONFIDENTIAL_PII_PHI]
- Traffic volume: [REQUESTS_PER_SECOND]
- Compliance: [PCI_DSS_HIPAA_GDPR_SOC2]

### Current Security
- Existing controls: [LIST_CURRENT_MEASURES]
- Known vulnerabilities: [IDENTIFIED_ISSUES]
- Security testing: [LAST_ASSESSMENT_DATE]
- API gateway: [YES_NO_VENDOR]
- WAF protection: [YES_NO_VENDOR]

## OWASP API SECURITY TOP 10

Address these critical vulnerabilities:

### API1: Broken Object Level Authorization
- Implement object-level permission checks
- Validate user authorization for specific resources
- Use UUIDs instead of sequential IDs
- Test authorization at object level, not just endpoint

### API2: Broken Authentication
- Strong authentication mechanisms
- MFA for sensitive operations
- Secure credential storage
- Token expiration and rotation
- Protection against brute force attacks

### API3: Broken Object Property Level Authorization
- Validate which properties user can read/write
- Implement schema-based validation
- Prevent mass assignment vulnerabilities
- Use allowlists for accessible properties

### API4: Unrestricted Resource Consumption
- Rate limiting per user/IP/API key
- Resource allocation limits
- Request size limits
- Query complexity limits (GraphQL)
- Timeout enforcement

### API5: Broken Function Level Authorization
- Validate user roles for all functions
- Enforce least privilege
- Separate admin functions
- Test authorization bypass attempts

### API6: Unrestricted Access to Sensitive Business Flows
- Identify sensitive workflows
- Implement business logic rate limiting
- Bot detection and prevention
- Transaction monitoring and alerting

### API7: Server Side Request Forgery (SSRF)
- Validate and sanitize URLs
- Use allowlists for external resources
- Disable unnecessary URL schemas
- Network segmentation

### API8: Security Misconfiguration
- Secure default configurations
- Remove unnecessary endpoints
- Disable debug modes in production
- Keep dependencies updated
- Implement security headers

### API9: Improper Inventory Management
- Maintain API documentation
- Retire old API versions securely
- Monitor for shadow APIs
- Document all endpoints and versions

### API10: Unsafe Consumption of APIs
- Validate third-party API responses
- Encrypt API communications
- Implement circuit breakers
- Monitor third-party API security

## AUTHENTICATION & AUTHORIZATION

### Authentication Methods
**OAuth 2.0:**
- Authorization code flow
- Client credentials flow
- Resource owner password (avoid)
- PKCE for mobile/SPA
- Token introspection and revocation

**JWT Tokens:**
- Strong signing algorithms (RS256, ES256)
- Short expiration times
- Secure key management
- Refresh token rotation
- Token validation on every request

**API Keys:**
- Secure generation and storage
- Rotation policies
- Key-per-environment
- Rate limiting by key
- Revocation mechanisms

**Mutual TLS:**
- Client certificate authentication
- Certificate validation
- CA trust management
- Certificate revocation checks

### Authorization Controls
- Role-based access control (RBAC)
- Attribute-based access control (ABAC)
- Scope-based permissions
- Resource-level authorization
- Dynamic policy evaluation

## SECURITY CONTROLS

### Input Validation
- Schema validation (JSON Schema, OpenAPI)
- Type checking and sanitization
- Length and range validation
- Format validation (email, URL, etc.)
- Reject unexpected parameters
- SQL/NoSQL injection prevention
- XSS prevention in responses

### Output Encoding
- Proper content-type headers
- JSON encoding
- Error message sanitization
- Remove sensitive data from responses
- Pagination to limit data exposure

### Rate Limiting & Throttling
- Per-endpoint rate limits
- User/IP-based throttling
- Sliding window algorithms
- Distributed rate limiting (Redis)
- Custom limits for premium users
- 429 response handling

### Encryption
- TLS 1.2+ for all communications
- Perfect forward secrecy
- Certificate pinning for mobile
- Encrypted payload for sensitive data
- Secure key exchange

### Logging & Monitoring
- Log all authentication attempts
- Log authorization failures
- Rate limit violations
- Suspicious patterns
- Avoid logging sensitive data
- Real-time alerting

## API GATEWAY SECURITY

Implement at gateway level:
- Centralized authentication
- Rate limiting and quota management
- Request/response transformation
- Schema validation
- Threat detection
- API analytics and monitoring
- Circuit breaker patterns
- IP whitelisting/blacklisting

## SECURITY TESTING

### Automated Testing
- OWASP ZAP API scanning
- Postman security tests
- Burp Suite Professional
- API fuzzing tools
- Dependency scanning

### Manual Testing
- Authorization bypass testing
- Authentication testing
- Input validation testing
- Business logic testing
- Rate limit testing

### Test Cases
- Test authentication bypass
- Test authorization at object level
- Test mass assignment
- Test injection attacks
- Test excessive data exposure
- Test lack of resource limits
- Test SSRF vulnerabilities

## GRAPHQL-SPECIFIC SECURITY

- Query depth limiting
- Query complexity analysis
- Disable introspection in production
- Field-level authorization
- Persistent query allowlists
- Rate limiting by query cost

## IMPLEMENTATION CHECKLIST

- [ ] Strong authentication implemented
- [ ] Authorization checks on all endpoints
- [ ] Input validation for all parameters
- [ ] Rate limiting configured
- [ ] HTTPS enforced
- [ ] Security headers configured
- [ ] Error messages sanitized
- [ ] Logging and monitoring active
- [ ] API documentation up-to-date
- [ ] Security testing completed
- [ ] Penetration test passed
- [ ] Incident response plan ready

## OUTPUT REQUIREMENTS

Provide:
1. API security architecture diagram
2. Authentication/authorization implementation
3. Rate limiting configuration
4. Input validation rules
5. Security testing report
6. Monitoring and alerting setup
7. Remediation recommendations
```

---

## Usage Examples

### Example 1: E-commerce REST API

**Context:** Customer-facing REST API for e-commerce platform with 200+ endpoints

```
Secure our e-commerce REST API handling customer data and payment processing with
PCI-DSS compliance requirements.

API CONTEXT:
- API type: REST (JSON over HTTPS)
- Endpoints: 215 endpoints across products, orders, users, payments
- Authentication: OAuth 2.0 with JWT access tokens
- Consumers: Mobile apps (iOS/Android), web SPA, partner integrations
- Data sensitivity: PII, payment tokens (no raw card data)
- Traffic: Peak 5,000 requests/second during sales
- Compliance: PCI-DSS 4.0, GDPR

Current Security:
- Basic JWT validation in place
- No rate limiting implemented
- API gateway: Kong (self-hosted)
- WAF: AWS WAF (basic rules)

Key Focus Areas:
- Implement BOLA protection for order/user resources
- Add rate limiting (per user: 100/min, per endpoint: 1000/min)
- Harden payment endpoints with additional validation
- Add request signing for partner API integrations
```

**Expected Output:**
- BOLA protection: UUID for order IDs, ownership validation middleware
- OAuth scopes: read:orders, write:orders, admin:users
- Rate limiting: Redis-based sliding window, 429 responses with retry-after
- Payment endpoints: Additional MFA challenge, request signing
- WAF rules: OWASP Core Rule Set + custom rules for business logic

### Example 2: GraphQL API for Mobile App

**Context:** GraphQL API powering a healthcare mobile application

```
Secure our GraphQL API serving patient health data to iOS and Android apps with
HIPAA compliance requirements.

API CONTEXT:
- API type: GraphQL (Apollo Server)
- Schema: 45 types, 120 queries/mutations
- Authentication: OAuth 2.0 + refresh tokens
- Consumers: Native mobile apps only
- Data sensitivity: PHI (patient records, prescriptions, appointments)
- Traffic: 500 requests/second average
- Compliance: HIPAA, HITECH

Current Security:
- JWT tokens (1-hour expiration)
- Basic field-level authorization
- Introspection enabled (needs to disable)
- No query complexity limits

Key Focus Areas:
- Disable introspection in production
- Implement query depth and complexity limits
- Add field-level authorization for PHI fields
- Certificate pinning for mobile apps
- Audit logging for all PHI access
```

**Expected Output:**
- Query limits: max depth 7, max complexity 500
- Persisted queries only (disable arbitrary queries in production)
- Field authorization: @auth directive on PHI fields
- Certificate pinning: Pin to leaf certificate + backup
- Audit logging: Patient ID, accessed fields, timestamp, user ID

### Example 3: Internal Microservices API

**Context:** Internal APIs for microservices communication in financial services

```
Secure internal microservices APIs handling financial transactions with
zero-trust architecture requirements.

API CONTEXT:
- API type: gRPC + REST (internal)
- Services: 35 microservices, ~500 endpoints total
- Authentication: mTLS + JWT for service identity
- Consumers: Internal services only (no external access)
- Data sensitivity: Financial transactions, account balances
- Traffic: 50,000 requests/second internal
- Compliance: SOX, internal security policy

Current Security:
- Network segmentation (services in private subnet)
- Basic service mesh (Istio) with mTLS
- No service-to-service authorization
- Limited logging

Key Focus Areas:
- Implement service-to-service authorization (SPIFFE/SPIRE)
- Add authorization policies in Istio
- Implement request tracing with correlation IDs
- Add circuit breakers for resilience
- Comprehensive audit logging for SOX
```

**Expected Output:**
- SPIFFE identities for all services
- Istio AuthorizationPolicy: explicit allow rules per service pair
- Distributed tracing: Jaeger with correlation ID propagation
- Circuit breakers: Istio DestinationRule with outlier detection
- Audit logging: All transactions to Splunk with SOX-required fields

## Best Practices

- **Never Trust Input** - Validate everything
- **Fail Securely** - Default deny, fail closed
- **Defense in Depth** - Multiple security layers
- **Least Privilege** - Minimal permissions needed
- **Audit Everything** - Log security-relevant events
- **Keep It Simple** - Complex security is fragile security

---

## Related Resources

- [OWASP API Security Project](https://owasp.org/www-project-api-security/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- security/Application-Security/secure-code-review.md
- technology/Software-Development/testing-qa.md
