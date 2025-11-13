---
title: "Web Application Security Framework"
category: security
tags: [security, application-security, web-security, owasp, vulnerability-management, development]
description: "Comprehensive framework for securing web applications covering OWASP Top 10, secure development lifecycle, vulnerability assessment, and defense-in-depth strategies."
related_templates:
  - api-security-framework.md
  - secure-code-review.md
  - ../Cybersecurity/threat-modeling.md
  - ../Security-Operations/penetration-testing.md
  - ../Security-Operations/vulnerability-management.md
version: 2.0
last_updated: 2025-11-12
---

# Web Application Security Framework

## Purpose
This framework provides a comprehensive approach to securing web applications throughout their lifecycle. It covers threat modeling, secure design patterns, OWASP Top 10 vulnerabilities, secure coding practices, security testing, and deployment security. Applicable to modern web applications including SPAs, APIs, microservices, and traditional web apps.

## Quick Start

1. **Threat Model Your Application**: Identify assets, threats, attack vectors, and security requirements using STRIDE or similar methodology
2. **Implement Security Controls**: Apply defense-in-depth with input validation, authentication, authorization, encryption, and secure configuration
3. **Address OWASP Top 10**: Systematically mitigate the most critical web application security risks
4. **Integrate Security Testing**: Implement SAST, DAST, SCA, and manual security testing in your SDLC
5. **Monitor & Respond**: Deploy security monitoring, logging, and incident response capabilities

---

## Minimal Example

**SCENARIO**: A SaaS application with user authentication, payment processing, and sensitive customer data needs comprehensive security implementation.

**Threat Model** (Key threats):
- SQL Injection, XSS in user inputs
- Authentication bypass, session hijacking
- Authorization failures (horizontal/vertical privilege escalation)
- Sensitive data exposure (PCI-DSS, GDPR concerns)
- API abuse and rate limiting

**Security Controls Implemented**:
- **Input Validation**: Whitelist validation, parameterized queries, HTML encoding
- **Authentication**: Multi-factor authentication, secure password policy, session management
- **Authorization**: Role-based access control (RBAC), principle of least privilege
- **Encryption**: TLS 1.3, data-at-rest encryption, secure key management
- **API Security**: Rate limiting, API authentication (OAuth 2.0), input validation

**OWASP Top 10 Mitigations**:
- A01: Broken Access Control → RBAC implementation, authorization checks on every request
- A02: Cryptographic Failures → TLS enforcement, encrypted database fields, secure key storage
- A03: Injection → Parameterized queries, input validation, ORM usage
- A04: Insecure Design → Threat modeling, security requirements, secure architecture review
- A07: Identification & Authentication Failures → MFA, secure session management, password policies

**Security Testing**:
- SAST: Integrated in CI/CD (Semgrep, SonarQube)
- DAST: Weekly automated scans (OWASP ZAP)
- Manual testing: Quarterly penetration tests
- Dependency scanning: Daily SCA scans (Snyk, Dependabot)

**Result**: Secure application with multiple layers of defense, regular security testing, and compliance with security standards.

---

## Comprehensive Framework

### PHASE 1: Security Requirements & Threat Modeling

#### 1.1 Define Security Requirements

**Functional Security Requirements**:
- **Authentication**: How will users authenticate? (passwords, MFA, SSO, OAuth)
- **Authorization**: What access control model? (RBAC, ABAC, ACL)
- **Data Protection**: What data must be encrypted? (in-transit, at-rest)
- **Audit/Logging**: What security events must be logged?
- **Session Management**: Session timeout, concurrent sessions, secure cookies

**Non-Functional Security Requirements**:
- **Performance**: Security controls impact on performance
- **Availability**: DDoS protection, rate limiting requirements
- **Scalability**: Security controls must scale with application
- **Compliance**: Regulatory requirements (PCI-DSS, GDPR, HIPAA, SOC 2)

**Security Objectives**:
- **Confidentiality**: Protect sensitive data from unauthorized access
- **Integrity**: Prevent unauthorized modification of data
- **Availability**: Ensure application remains available to legitimate users
- **Non-repudiation**: Audit trails and accountability
- **Privacy**: Comply with data privacy regulations

#### 1.2 Threat Modeling

**STRIDE Threat Model**:

| Threat Type | Description | Examples | Mitigations |
|-------------|-------------|----------|-------------|
| **Spoofing** | Pretending to be someone else | Authentication bypass, session hijacking | Strong authentication, MFA, secure sessions |
| **Tampering** | Modifying data or code | SQL injection, XSS, CSRF | Input validation, parameterized queries, CSRF tokens |
| **Repudiation** | Denying actions | User denies transaction | Audit logging, digital signatures, non-repudiation |
| **Information Disclosure** | Exposing information | Sensitive data in logs, error messages, unencrypted data | Encryption, secure error handling, data classification |
| **Denial of Service** | Disrupting availability | DDoS attacks, resource exhaustion | Rate limiting, input validation, resource limits |
| **Elevation of Privilege** | Gaining unauthorized access | Privilege escalation, authorization bypass | Least privilege, authorization checks, secure defaults |

**Attack Surface Analysis**:
- **Entry Points**: Login forms, APIs, file uploads, search functions, admin panels
- **Assets**: User credentials, PII, payment data, business logic, source code
- **Trust Boundaries**: Client ↔ Web server, Web server ↔ Database, Internal ↔ External APIs
- **Data Flows**: User input → Processing → Storage → Output

**Threat Scenarios**:
1. **Attacker attempts SQL injection** through search functionality
2. **Attacker exploits XSS** to steal session cookies
3. **Insider threat** attempts to access unauthorized customer data
4. **Attacker brute forces** user passwords
5. **Attacker exploits API** without rate limiting to scrape data

#### 1.3 Security Architecture & Design

**Defense in Depth Layers**:

**Layer 1: Network Security**
- WAF (Web Application Firewall) for common attack patterns
- DDoS protection (CloudFlare, AWS Shield)
- Network segmentation (DMZ, internal networks)

**Layer 2: Application Security**
- Input validation (whitelist approach)
- Output encoding (context-aware encoding)
- Authentication & authorization
- Secure session management

**Layer 3: Data Security**
- Encryption in transit (TLS 1.3)
- Encryption at rest (AES-256)
- Secure key management (HSM, KMS)
- Data masking, tokenization for sensitive data

**Layer 4: Infrastructure Security**
- Hardened servers, secure configuration
- Patch management, vulnerability scanning
- Container security (if applicable)
- Secrets management (Vault, AWS Secrets Manager)

**Secure Design Patterns**:
- **Least Privilege**: Users/processes have minimum necessary permissions
- **Fail Secure**: Security failures default to secure state (deny access)
- **Complete Mediation**: Every access checked, no assumptions about previous checks
- **Separation of Duties**: No single user has complete control
- **Secure Defaults**: Out-of-the-box configuration is secure
- **Economy of Mechanism**: Keep security mechanisms simple

---

### PHASE 2: OWASP Top 10 Mitigation

#### 2.1 A01:2021 – Broken Access Control

**Vulnerability**: Users can access resources/functions they shouldn't have access to.

**Common Scenarios**:
- **Insecure Direct Object References (IDOR)**: `GET /api/user/1234/profile` (change ID to access other users)
- **Missing Function Level Access Control**: Regular user accessing admin functions
- **Vertical Privilege Escalation**: User elevates to admin privileges
- **Horizontal Privilege Escalation**: User A accesses User B's data
- **Forced Browsing**: Accessing URLs not linked in application

**Mitigation Strategies**:

**1. Implement Robust Authorization**:
```python
# BAD: Only checking authentication
@app.route('/api/user/<user_id>/profile')
@login_required
def get_profile(user_id):
    profile = User.query.get(user_id)
    return jsonify(profile)

# GOOD: Checking both authentication AND authorization
@app.route('/api/user/<user_id>/profile')
@login_required
def get_profile(user_id):
    if current_user.id != user_id and not current_user.is_admin:
        abort(403, "Unauthorized access")
    profile = User.query.get(user_id)
    return jsonify(profile)
```

**2. Use Indirect References**:
- Use session-specific references instead of direct database IDs
- Map user session to allowed resources server-side

**3. Deny by Default**:
- Default to deny access unless explicitly allowed
- Enforce access control checks on every request

**4. Implement RBAC (Role-Based Access Control)**:
- Define roles (Admin, User, Guest)
- Assign permissions to roles
- Assign roles to users
- Check role permissions on every request

**Testing**:
- Test with different user roles
- Attempt to access other users' resources
- Try to access admin functions as regular user
- Forced browsing to hidden URLs

#### 2.2 A02:2021 – Cryptographic Failures

**Vulnerability**: Sensitive data exposed due to weak or missing encryption.

**Common Scenarios**:
- Sensitive data transmitted over HTTP (not HTTPS)
- Weak encryption algorithms (DES, MD5, SHA1)
- Hardcoded encryption keys in source code
- Sensitive data stored in plaintext (passwords, credit cards)
- Weak TLS configuration (SSLv3, TLS 1.0, weak ciphers)

**Mitigation Strategies**:

**1. Encrypt Data in Transit**:
- **Enforce HTTPS**: Use HSTS (HTTP Strict Transport Security)
- **TLS 1.3**: Use modern TLS versions (1.2 minimum, 1.3 preferred)
- **Strong Ciphers**: Disable weak ciphers (RC4, DES, 3DES)
- **Certificate Management**: Valid certificates, automated renewal

```nginx
# NGINX TLS Configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256';
ssl_prefer_server_ciphers on;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

**2. Encrypt Data at Rest**:
- **Sensitive Fields**: Encrypt PII, payment data, sensitive business data
- **Full Disk Encryption**: For database servers, file storage
- **Database Encryption**: Transparent Data Encryption (TDE) for databases
- **Field-Level Encryption**: Encrypt specific sensitive columns

**3. Secure Key Management**:
- **Never Hardcode Keys**: Use environment variables or key management services
- **Key Rotation**: Regular key rotation policy
- **HSM/KMS**: Use hardware security modules or cloud KMS (AWS KMS, Azure Key Vault)
- **Separate Keys**: Different keys for different purposes

**4. Strong Password Hashing**:
```python
# BAD: Weak hashing
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()

# GOOD: Strong adaptive hashing
import bcrypt
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
```
- Use bcrypt, scrypt, or Argon2 (not MD5, SHA1, or plain SHA256)
- Use salt (automatically handled by bcrypt/scrypt)
- Use sufficient work factor (bcrypt rounds: 12-15)

**Testing**:
- SSL Labs scan for TLS configuration
- Check for sensitive data in logs, error messages
- Verify encryption at rest for sensitive data
- Code review for hardcoded secrets

#### 2.3 A03:2021 – Injection

**Vulnerability**: Untrusted data sent to interpreter as part of command or query.

**Injection Types**:
- **SQL Injection**: Malicious SQL code in database queries
- **NoSQL Injection**: Attacks on NoSQL databases (MongoDB, etc.)
- **OS Command Injection**: Execute arbitrary OS commands
- **LDAP Injection**: Attacks on LDAP queries
- **XPath Injection**: Attacks on XML queries

**SQL Injection Example**:
```python
# VULNERABLE CODE
username = request.form['username']
password = request.form['password']
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
user = db.execute(query)

# ATTACK INPUT
# username: admin' OR '1'='1' --
# Resulting query: SELECT * FROM users WHERE username='admin' OR '1'='1' --' AND password=''
# Returns all users, bypasses authentication
```

**Mitigation Strategies**:

**1. Use Parameterized Queries / Prepared Statements**:
```python
# GOOD: Parameterized query
username = request.form['username']
password = request.form['password']
query = "SELECT * FROM users WHERE username=? AND password=?"
user = db.execute(query, (username, password_hash))
```

**2. Use ORM (Object-Relational Mapping)**:
```python
# Using SQLAlchemy ORM
user = User.query.filter_by(username=username, password=password_hash).first()
```

**3. Input Validation (Whitelist Approach)**:
```python
import re

# Validate username: alphanumeric only, 3-20 characters
if not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
    raise ValueError("Invalid username format")
```

**4. Escape Special Characters** (Last resort, parameterization preferred):
```python
# If dynamic query absolutely necessary
username = db.escape_string(username)
```

**5. Least Privilege Database Access**:
- Application database user should have minimal permissions
- No DROP, CREATE, or ADMIN privileges for application user
- Use stored procedures with restricted permissions

**Testing**:
- SAST tools to detect SQL injection vulnerabilities
- DAST tools with SQL injection payloads
- Manual testing with common injection patterns
- Code review for dynamic query construction

#### 2.4 A04:2021 – Insecure Design

**Vulnerability**: Missing or ineffective security controls due to design flaws.

**Common Design Flaws**:
- No threat modeling performed
- Security requirements not defined
- Missing security controls in architecture
- Business logic flaws
- Lack of security principles (least privilege, defense in depth)

**Mitigation Strategies**:

**1. Threat Modeling**: Conduct threat modeling in design phase (STRIDE, PASTA)

**2. Secure Design Principles**:
- **Defense in Depth**: Multiple layers of security
- **Least Privilege**: Minimum necessary access
- **Fail Secure**: Failures default to secure state
- **Separation of Duties**: No single point of control
- **Zero Trust**: Never trust, always verify

**3. Security Requirements**: Define security requirements early

**4. Security Architecture Review**: Review architecture with security team

**5. Secure Design Patterns**: Use proven secure patterns
- Anti-CSRF tokens for state-changing operations
- Secure session management patterns
- Rate limiting for API endpoints
- Secure password reset flows

**Example: Secure Password Reset Flow**:
```
1. User requests password reset (provide email/username)
2. System generates random token (cryptographically secure)
3. Token stored in database with expiration (15-60 minutes)
4. Email sent with reset link containing token
5. User clicks link, token validated (not expired, matches user)
6. User sets new password
7. Token invalidated after use
8. All sessions terminated, user must re-login
```

**Testing**:
- Architecture review by security team
- Threat modeling workshops
- Business logic testing
- Abuse case testing

#### 2.5 A05:2021 – Security Misconfiguration

**Vulnerability**: Insecure default configurations, incomplete setups, verbose error messages.

**Common Misconfigurations**:
- Default credentials not changed
- Unnecessary features enabled
- Directory listing enabled
- Detailed error messages exposing stack traces
- Security headers missing
- Outdated software versions

**Mitigation Strategies**:

**1. Secure Configuration Management**:
- Infrastructure as Code (Terraform, CloudFormation)
- Configuration management tools (Ansible, Puppet)
- Automated security baseline enforcement
- Regular configuration audits

**2. Hardening Checklist**:
- Change default credentials immediately
- Disable unnecessary features, services, ports
- Remove default accounts and sample applications
- Disable directory listing
- Implement security headers
- Configure error handling (don't expose stack traces)

**3. Security Headers**:
```
# Essential Security Headers
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'
Referrer-Policy: no-referrer
Permissions-Policy: geolocation=(), microphone=(), camera=()
```

**4. Error Handling**:
```python
# BAD: Verbose error messages
try:
    user = User.query.get(user_id)
except Exception as e:
    return jsonify({"error": str(e)}), 500  # Exposes stack trace

# GOOD: Generic error messages
try:
    user = User.query.get(user_id)
except Exception as e:
    logger.error(f"Error fetching user {user_id}: {str(e)}")
    return jsonify({"error": "An error occurred"}), 500
```

**5. Regular Patching**: Automated patch management, vulnerability scanning

**Testing**:
- Configuration scanners (Nessus, OpenVAS)
- Security header validation
- Default credential testing
- Error message testing

#### 2.6 A06:2021 – Vulnerable and Outdated Components

**Vulnerability**: Using components with known vulnerabilities.

**Common Scenarios**:
- Outdated frameworks, libraries, dependencies
- Unused dependencies with vulnerabilities
- Transitive dependencies with vulnerabilities
- Unpatched operating systems, web servers, databases

**Mitigation Strategies**:

**1. Software Composition Analysis (SCA)**:
- **Tools**: Snyk, WhiteSource, Black Duck, OWASP Dependency-Check, GitHub Dependabot
- **Frequency**: Daily scans in CI/CD
- **Action**: Automated PRs for dependency updates

**2. Dependency Management**:
```json
// package.json with specific versions
{
  "dependencies": {
    "express": "4.18.2",  // Specific version, not ^4.18.2
    "bcrypt": "5.1.0"
  }
}
```

**3. Remove Unused Dependencies**:
- Regular audits to identify unused packages
- Remove to reduce attack surface

**4. Automated Updates**:
- Dependabot, Renovate Bot for automated dependency PRs
- Review and test before merging

**5. Vulnerability Management Process**:
```
1. Daily SCA scans detect vulnerability
2. Automated ticket created with severity
3. Critical/High: Patch within 24-48 hours
4. Medium: Patch within 1 week
5. Low: Patch in next release cycle
6. Test patches in staging before production
```

**Testing**:
- SCA tool integration in CI/CD
- Regular dependency audits
- Vulnerability scanner for infrastructure

#### 2.7 A07:2021 – Identification and Authentication Failures

**Vulnerability**: Weak authentication allowing attackers to compromise accounts.

**Common Scenarios**:
- Weak password policies
- Credential stuffing, brute force attacks
- Session ID in URL, not invalidated properly
- Session fixation attacks
- Missing or weak MFA

**Mitigation Strategies**:

**1. Strong Password Policy**:
- Minimum 12 characters (not just 8)
- No common passwords (check against Have I Been Pwned)
- Password complexity (uppercase, lowercase, numbers, symbols)
- No password reuse across systems
- Password expiration (90-180 days) for high-security systems

**2. Multi-Factor Authentication (MFA)**:
- Require MFA for all users (especially admin accounts)
- Support TOTP (Google Authenticator, Authy)
- Support WebAuthn/FIDO2 (hardware keys)
- Backup codes for account recovery

**3. Brute Force Protection**:
```python
# Rate limiting for login attempts
from flask_limiter import Limiter

limiter = Limiter(key_func=get_remote_address)

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")  # Max 5 attempts per minute
def login():
    # Login logic
    pass
```

**4. Secure Session Management**:
```python
# Secure session configuration
app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Not accessible via JavaScript
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # CSRF protection
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)  # 2-hour timeout
```

**5. Account Lockout**:
- Lock account after X failed attempts (5-10)
- Temporary lockout (15-30 minutes) or require password reset
- CAPTCHA after failed attempts

**6. Secure Password Reset**:
- Use secure tokens (cryptographically random)
- Short expiration (15-60 minutes)
- Invalidate after use
- Terminate all sessions after password reset

**Testing**:
- Brute force testing
- Session management testing
- Password policy testing
- MFA bypass testing

#### 2.8 A08:2021 – Software and Data Integrity Failures

**Vulnerability**: Code and infrastructure relying on unverified updates.

**Common Scenarios**:
- Insecure CI/CD pipeline allowing code injection
- Auto-updates without integrity verification
- Insecure deserialization
- Unsigned artifacts
- Compromised dependencies (supply chain attacks)

**Mitigation Strategies**:

**1. Secure CI/CD Pipeline**:
- Code signing for artifacts
- Immutable build artifacts
- Access control for CI/CD systems
- Audit logs for all deployments
- Secrets management (not hardcoded in pipeline)

**2. Dependency Integrity**:
```bash
# Verify package integrity using checksums
npm install --integrity

# Use package lock files
npm ci  # Install from package-lock.json
```

**3. Digital Signatures**:
- Sign software releases
- Verify signatures before installation
- Code signing certificates for binaries

**4. Secure Deserialization**:
```python
# BAD: Insecure deserialization
import pickle
data = pickle.loads(user_input)  # Can execute arbitrary code

# GOOD: Use safe serialization formats
import json
data = json.loads(user_input)  # Safe, limited to data structures
```

**5. Subresource Integrity (SRI)**:
```html
<!-- Verify integrity of CDN resources -->
<script src="https://cdn.example.com/lib.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/ux..."
        crossorigin="anonymous"></script>
```

**Testing**:
- CI/CD security audits
- Deserialization vulnerability testing
- Supply chain security analysis

#### 2.9 A09:2021 – Security Logging and Monitoring Failures

**Vulnerability**: Insufficient logging allowing attackers to persist undetected.

**Common Scenarios**:
- Login failures, authentication events not logged
- No alerts for suspicious activities
- Logs not centralized or monitored
- Log tampering possible
- Insufficient log retention

**Mitigation Strategies**:

**1. Comprehensive Logging**:
```python
import logging

# Log security events
logger.info(f"Successful login: user={username}, ip={request.remote_addr}")
logger.warning(f"Failed login attempt: user={username}, ip={request.remote_addr}")
logger.error(f"Authorization failure: user={username}, resource={resource_id}")
```

**Security Events to Log**:
- Authentication (success, failure, logout)
- Authorization failures
- Input validation failures
- Application errors
- Configuration changes
- Admin actions
- Privileged account usage

**2. Centralized Logging**:
- SIEM (Splunk, ELK Stack, Datadog)
- Cloud logging (CloudWatch, Azure Monitor, GCP Cloud Logging)
- Log aggregation for correlation

**3. Alerting**:
```
Critical Alerts:
- Multiple failed login attempts (brute force)
- Privilege escalation attempts
- Data exfiltration patterns
- Malware detection
- Infrastructure changes

Medium Alerts:
- Unusual access patterns
- Configuration changes
- New admin accounts created
```

**4. Log Protection**:
- Append-only logs (prevent tampering)
- Encrypted log transmission
- Access control for logs (principle of least privilege)
- Log retention policy (compliance requirements)

**5. Security Monitoring**:
- Real-time monitoring dashboards
- Automated anomaly detection
- Behavioral analytics (user/entity behavior)
- Threat intelligence integration

**Testing**:
- Verify security events are logged
- Test alerting mechanisms
- Log injection testing (ensure logs can't be manipulated)
- Log retention verification

#### 2.10 A10:2021 – Server-Side Request Forgery (SSRF)

**Vulnerability**: Application fetches remote resource without validating URL.

**Common Scenarios**:
- Webhooks without URL validation
- PDF generators fetching external resources
- Image processing from user-provided URLs
- API integration without URL validation

**Attack Example**:
```python
# VULNERABLE CODE
@app.route('/fetch-image')
def fetch_image():
    url = request.args.get('url')
    response = requests.get(url)  # No validation
    return response.content

# ATTACK: ?url=http://169.254.169.254/latest/meta-data/
# Accesses AWS metadata service, potentially exposing credentials
```

**Mitigation Strategies**:

**1. URL Validation Whitelist**:
```python
from urllib.parse import urlparse

ALLOWED_DOMAINS = ['example.com', 'cdn.example.com']

@app.route('/fetch-image')
def fetch_image():
    url = request.args.get('url')
    parsed = urlparse(url)

    if parsed.hostname not in ALLOWED_DOMAINS:
        abort(400, "Domain not allowed")

    response = requests.get(url, timeout=5)
    return response.content
```

**2. Deny List for Internal IPs**:
```python
import ipaddress

DENIED_NETWORKS = [
    ipaddress.ip_network('10.0.0.0/8'),      # Private
    ipaddress.ip_network('172.16.0.0/12'),   # Private
    ipaddress.ip_network('192.168.0.0/16'),  # Private
    ipaddress.ip_network('127.0.0.0/8'),     # Loopback
    ipaddress.ip_network('169.254.0.0/16'),  # Link-local (AWS metadata)
]

def is_internal_ip(hostname):
    try:
        ip = ipaddress.ip_address(hostname)
        return any(ip in network for network in DENIED_NETWORKS)
    except ValueError:
        return False
```

**3. Disable Redirects**:
```python
response = requests.get(url, allow_redirects=False, timeout=5)
```

**4. Network Segmentation**:
- Application servers in DMZ with restricted outbound access
- Firewall rules preventing access to internal services

**5. Use Dedicated Services**:
- For webhooks, use dedicated webhook service with validation
- For image processing, use sandboxed workers

**Testing**:
- SSRF vulnerability scanning
- Test with internal IP addresses
- Test URL redirect chains
- Cloud metadata endpoint testing

---

### PHASE 3: Secure Development Practices

#### 3.1 Secure Coding Standards

**Input Validation**:
```python
# Whitelist validation (preferred)
def validate_username(username):
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Invalid username")
    return username

# Sanitization
from html import escape
safe_output = escape(user_input)  # Escape HTML special characters
```

**Output Encoding** (Context-aware):
- **HTML Context**: HTML entity encoding
- **JavaScript Context**: JavaScript encoding
- **URL Context**: URL encoding
- **SQL Context**: Use parameterized queries (don't encode)

**Error Handling**:
```python
# Secure error handling
try:
    # Application logic
    process_payment(amount, card)
except PaymentProcessingError:
    logger.error(f"Payment failed for user {user_id}", exc_info=True)
    return jsonify({"error": "Payment processing failed"}), 500
except Exception as e:
    logger.critical(f"Unexpected error: {str(e)}", exc_info=True)
    return jsonify({"error": "An unexpected error occurred"}), 500
```

**Secrets Management**:
```python
# BAD: Hardcoded secrets
API_KEY = "sk_live_abcdef123456"

# GOOD: Environment variables or secrets manager
import os
API_KEY = os.environ.get('API_KEY')

# BETTER: Secrets manager
from aws_secretsmanager import get_secret
API_KEY = get_secret('prod/api/key')
```

#### 3.2 Security Testing in SDLC

**Testing Types**:

| Test Type | Tool Examples | Frequency | Coverage |
|-----------|---------------|-----------|----------|
| **SAST** (Static) | SonarQube, Semgrep, Checkmarx | Every commit | Code vulnerabilities |
| **DAST** (Dynamic) | OWASP ZAP, Burp Suite | Weekly/On-demand | Running application |
| **SCA** (Dependencies) | Snyk, Dependabot, WhiteSource | Daily | Vulnerable dependencies |
| **IAST** (Interactive) | Contrast, Seeker | During testing | Runtime analysis |
| **Manual Testing** | Penetration testing | Quarterly | Complex logic, business vulnerabilities |

**CI/CD Security Integration**:
```yaml
# Example GitHub Actions workflow
name: Security Scanning
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      # SAST - Static code analysis
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1

      # SCA - Dependency scanning
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

      # Secrets scanning
      - name: Run TruffleHog
        uses: trufflesecurity/trufflehog@main

      # Fail build on high/critical vulnerabilities
      - name: Check results
        run: |
          if [ "$VULNS_HIGH" -gt 0 ]; then
            echo "High severity vulnerabilities found"
            exit 1
          fi
```

**Security Testing Phases**:

**1. Development** (Shift-Left):
- IDE security plugins (real-time feedback)
- Pre-commit hooks (secrets scanning, linting)
- SAST on every commit

**2. Build**:
- SAST comprehensive scan
- SCA dependency analysis
- Container image scanning (if applicable)

**3. Testing**:
- DAST on test environment
- IAST during integration tests
- Security regression tests

**4. Pre-Production**:
- Penetration testing
- Security acceptance testing
- Configuration validation

**5. Production**:
- Runtime application self-protection (RASP)
- Security monitoring
- Continuous vulnerability scanning

#### 3.3 Code Review for Security

**Security Code Review Checklist**:

**Authentication & Authorization**:
- [ ] Authentication required for protected resources?
- [ ] Authorization checks on every request?
- [ ] No hardcoded credentials?
- [ ] Secure session management?

**Input Validation**:
- [ ] All user input validated?
- [ ] Whitelist validation used?
- [ ] Parameterized queries for database?
- [ ] File upload restrictions (type, size)?

**Cryptography**:
- [ ] Strong algorithms used (bcrypt, AES-256)?
- [ ] No hardcoded keys?
- [ ] Secure random number generation?
- [ ] TLS enforced?

**Error Handling**:
- [ ] Generic error messages to users?
- [ ] Detailed errors logged securely?
- [ ] No stack traces exposed?

**Sensitive Data**:
- [ ] Sensitive data encrypted?
- [ ] No sensitive data in logs?
- [ ] Secure data transmission?

**Business Logic**:
- [ ] Race conditions handled?
- [ ] Abuse cases considered?
- [ ] Rate limiting implemented?

---

### PHASE 4: Deployment & Operations Security

#### 4.1 Secure Deployment

**Deployment Checklist**:
- [ ] Security headers configured
- [ ] TLS/HTTPS enforced
- [ ] Secrets injected via secure mechanism (not in code/config)
- [ ] Default credentials changed
- [ ] Unnecessary services disabled
- [ ] Firewall rules configured (least privilege)
- [ ] Security monitoring enabled
- [ ] Backup and recovery tested

**Infrastructure as Code Security**:
```terraform
# Secure S3 bucket configuration
resource "aws_s3_bucket" "secure_bucket" {
  bucket = "my-secure-bucket"

  # Encryption
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  # Block public access
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

  # Versioning
  versioning {
    enabled = true
  }

  # Logging
  logging {
    target_bucket = aws_s3_bucket.logs.id
    target_prefix = "s3-access-logs/"
  }
}
```

#### 4.2 Security Monitoring

**Application-Level Monitoring**:
- Failed authentication attempts
- Authorization failures
- Input validation failures
- Unusual traffic patterns
- Error rate spikes

**Infrastructure Monitoring**:
- Unauthorized access attempts
- Configuration changes
- Patch status
- Vulnerability scan results

**Security Metrics**:
- Time to detect (TTD)
- Time to respond (TTR)
- Mean time to remediate (MTTR)
- Vulnerability counts by severity
- Patch compliance rate

#### 4.3 Incident Response

**Incident Response Plan**:
```
1. Detection & Analysis
   - Identify security incident
   - Assess severity and scope
   - Activate incident response team

2. Containment
   - Short-term: Isolate affected systems
   - Long-term: Patch vulnerabilities

3. Eradication
   - Remove malware, backdoors
   - Patch vulnerabilities
   - Improve security controls

4. Recovery
   - Restore systems from clean backups
   - Verify system integrity
   - Resume normal operations

5. Post-Incident
   - Lessons learned
   - Update incident response plan
   - Implement preventive measures
```

---

## Variables Table

| Variable | Description | Example Values | Notes |
|----------|-------------|----------------|-------|
| `{AUTHENTICATION_METHOD}` | How users authenticate | Password+MFA, OAuth, SSO, Certificate | MFA strongly recommended |
| `{AUTHORIZATION_MODEL}` | Access control model | RBAC, ABAC, ACL | RBAC most common |
| `{ENCRYPTION_STANDARD}` | Encryption algorithms | AES-256, TLS 1.3, bcrypt | Avoid MD5, DES, SHA1 |
| `{INPUT_VALIDATION_STRATEGY}` | Validation approach | Whitelist, Regex, Type checking | Whitelist preferred |
| `{SESSION_TIMEOUT}` | Session expiration | 15 min, 2 hours, 8 hours | Balance security vs usability |
| `{PASSWORD_POLICY}` | Password requirements | 12+ chars, complexity, no reuse | 12+ chars minimum |
| `{LOGGING_DESTINATION}` | Where logs are sent | SIEM, CloudWatch, Splunk | Centralized logging |
| `{VULNERABILITY_SLA}` | Time to patch | Critical: 24h, High: 7d, Medium: 30d | Based on severity |
| `{SECURITY_TESTING_FREQUENCY}` | How often to test | SAST: every commit, DAST: weekly, Pentest: quarterly | Continuous testing |
| `{RATE_LIMIT}` | API rate limiting | 100 req/min, 1000 req/hour | Prevent abuse |
| `{DATA_CLASSIFICATION}` | Sensitivity levels | Public, Internal, Confidential, Restricted | Determines controls |
| `{COMPLIANCE_REQUIREMENTS}` | Regulatory requirements | PCI-DSS, GDPR, HIPAA, SOC 2 | Drives security controls |

---

## Usage Examples

### Example 1: E-Commerce Platform Security

**Context**: E-commerce platform handling payment cards, customer PII, requiring PCI-DSS compliance.

**Security Implementation**:

**Threat Model** (Key threats):
- Payment card data theft
- Account takeover (credential stuffing)
- SQL injection on product search
- XSS in product reviews
- CSRF on checkout process

**OWASP Top 10 Mitigations**:

**A01 - Broken Access Control**:
- RBAC implementation (Customer, Merchant, Admin roles)
- Authorization checks on every API endpoint
- User can only access own orders: `if order.user_id != current_user.id: abort(403)`

**A02 - Cryptographic Failures**:
- TLS 1.3 enforcement with HSTS
- PCI-DSS compliance: Tokenization of payment cards (no storage of full PANs)
- Payment processing via Stripe (PCI-DSS compliant processor)
- Passwords hashed with bcrypt (rounds=12)

**A03 - Injection**:
- Parameterized queries for all database operations
- ORM usage (SQLAlchemy) to prevent SQL injection
- Input validation on product search (whitelist alphanumeric + spaces)

**A04 - Insecure Design**:
- Threat modeling conducted in design phase
- Rate limiting on API endpoints (100 req/min per IP)
- Secure checkout flow with CSRF protection

**A07 - Authentication Failures**:
- Password policy: 12+ characters, complexity requirements
- MFA optional for customers, required for merchants/admins
- Account lockout after 5 failed attempts
- Rate limiting on login endpoint (5 attempts/min)

**Security Testing**:
- **SAST**: SonarQube integrated in GitLab CI (every commit)
- **SCA**: Snyk scanning dependencies (daily)
- **DAST**: OWASP ZAP scans (weekly on staging)
- **Manual**: Quarterly penetration testing
- **PCI-DSS**: Annual PCI-DSS assessment by QSA

**Security Monitoring**:
- Failed login attempts (alert on 10+ failures in 5 minutes)
- Payment processing failures (alert on spike)
- Unusual access patterns (user accessing 100+ products/min)
- Infrastructure changes (unauthorized SSH access)

**Results**:
- PCI-DSS Level 1 compliance achieved
- Zero data breaches in 2 years
- <0.1% fraud rate on transactions
- 99.9% uptime with DDoS protection

### Example 2: SaaS Application Security (Multi-Tenant)

**Context**: B2B SaaS application with multi-tenant architecture, storing sensitive customer data.

**Security Implementation**:

**Multi-Tenant Isolation**:
- Tenant ID in every database query
- Row-level security in database
- Separate encryption keys per tenant
- Tenant-specific security policies

**Data Security**:
- Encryption at rest: AES-256 for database
- Encryption in transit: TLS 1.3
- Field-level encryption for PII
- Database backups encrypted

**Authentication & Authorization**:
- SSO integration (SAML 2.0, OIDC)
- MFA enforced for all users
- RBAC with custom roles per tenant
- API authentication via OAuth 2.0

**API Security**:
- OAuth 2.0 for API access
- API rate limiting (1000 req/hour per user)
- API request/response logging
- API security testing in CI/CD

**Security Testing**:
```yaml
# CI/CD Security Pipeline
stages:
  - sast: Semgrep scanning
  - sca: Snyk dependency scanning
  - secrets: TruffleHog secrets detection
  - dast: OWASP ZAP API scan (staging)
  - compliance: SOC 2 control validation
```

**Compliance**:
- SOC 2 Type II certified
- GDPR compliant (EU data residency)
- ISO 27001 certified
- Regular third-party audits

**Monitoring**:
- SIEM: Splunk for centralized logging
- Alerts: Failed authentication, privilege escalation attempts, data exfiltration patterns
- Anomaly detection: User behavior analytics (UBA)
- Vulnerability management: Weekly scans, <7 day patch SLA for high/critical

**Incident Response**:
- 24/7 security operations center (SOC)
- Incident response plan tested quarterly
- Breach notification procedures (GDPR 72-hour requirement)
- Cyber insurance coverage

**Results**:
- SOC 2 Type II and ISO 27001 certifications
- Zero security breaches in 3 years
- 99.95% uptime SLA met
- Customer security questionnaires streamlined (compliance certifications)

### Example 3: Healthcare Application Security (HIPAA)

**Context**: Healthcare application storing electronic protected health information (ePHI), requiring HIPAA compliance.

**Security Implementation**:

**HIPAA Security Rule Compliance**:

**Administrative Safeguards**:
- Security management process (risk assessments, risk management)
- Assigned security responsibility (CISO designated)
- Workforce security (background checks, access controls)
- Security awareness training (annual HIPAA training)

**Physical Safeguards**:
- Facility access controls (badge access)
- Workstation security (screen locks, encryption)
- Device and media controls (secure disposal, encryption)

**Technical Safeguards**:
- Access controls (unique user IDs, automatic logoff, encryption)
- Audit controls (comprehensive logging)
- Integrity controls (data integrity verification)
- Transmission security (encryption in transit)

**ePHI Protection**:
- Encryption at rest: AES-256
- Encryption in transit: TLS 1.3
- Data masking for non-privileged users
- Audit logging of all ePHI access

**Access Controls**:
- Role-based access control (Physician, Nurse, Administrator, Patient)
- Minimum necessary access (principle of least privilege)
- Break-glass access for emergencies (logged and reviewed)
- Automatic logoff after 15 minutes of inactivity

**Audit Logging**:
- All ePHI access logged (who, what, when, where)
- Audit logs reviewed monthly
- Audit logs retained for 6 years (HIPAA requirement)
- Tamper-proof audit logs (append-only)

**Business Associate Agreements (BAA)**:
- BAAs with all vendors handling ePHI
- Regular vendor security assessments
- Vendor breach notification obligations

**Breach Notification**:
- Breach detection and analysis procedures
- Notification to patients within 60 days
- Notification to HHS (if >500 patients affected)
- Media notification (if >500 patients in jurisdiction)

**Security Testing**:
- Annual HIPAA security risk assessment
- Quarterly penetration testing
- Continuous vulnerability scanning
- Third-party security audits

**Results**:
- HIPAA compliance maintained for 5 years
- HITRUST CSF certification achieved
- Zero reportable breaches
- Annual security risk assessments completed

---

## Best Practices

### Design & Architecture
- **Threat Model Early**: Conduct threat modeling in design phase, not after development
- **Defense in Depth**: Multiple layers of security controls
- **Least Privilege**: Users/processes have minimum necessary permissions
- **Fail Secure**: Security failures default to deny access
- **Zero Trust**: Never trust, always verify

### Development
- **Secure by Default**: Default configuration is secure
- **Input Validation**: Validate all input (whitelist approach)
- **Output Encoding**: Context-aware encoding (HTML, JS, URL, SQL)
- **Parameterized Queries**: Always use for database queries
- **Secrets Management**: Never hardcode secrets

### Testing
- **Shift Left**: Integrate security testing early (SAST on every commit)
- **Automate Testing**: SAST, SCA, DAST in CI/CD pipeline
- **Test Regularly**: Continuous testing, not just pre-release
- **Manual Testing**: Quarterly penetration tests for complex logic
- **Test Like Attacker**: Use attacker mindset, test abuse cases

### Operations
- **Monitor Continuously**: Real-time security monitoring
- **Patch Quickly**: Critical vulnerabilities patched within 24-48 hours
- **Least Privilege**: Infrastructure access controls
- **Backup & Recovery**: Regular backups, tested recovery procedures
- **Incident Response**: Tested incident response plan

---

## Common Pitfalls

### Design Pitfalls
- **No Threat Modeling**: Building without understanding threats
- **Single Layer Defense**: Relying on one security control
- **Insecure Defaults**: Default configuration is insecure
- **Ignoring Business Logic**: Focus on technical vulns, ignore business logic flaws

### Development Pitfalls
- **Trusting User Input**: Not validating/sanitizing input
- **Blacklist Validation**: Using blacklist instead of whitelist
- **Weak Cryptography**: Using MD5, SHA1, DES
- **Hardcoded Secrets**: API keys, passwords in source code
- **Verbose Errors**: Exposing stack traces to users

### Testing Pitfalls
- **Testing Too Late**: Security testing only at the end
- **No Automation**: Manual testing only (doesn't scale)
- **Ignoring Dependencies**: Not scanning third-party libraries
- **False Sense of Security**: Tools find some issues, not all
- **No Manual Testing**: Relying only on automated tools

### Operations Pitfalls
- **No Monitoring**: Not monitoring for security events
- **Slow Patching**: Taking weeks to patch critical vulnerabilities
- **No Incident Response**: No plan for when breach occurs
- **Ignoring Logs**: Logs not reviewed or alerted on
- **Configuration Drift**: Security configuration not maintained

---

## Related Templates

- **api-security-framework.md**: API-specific security controls
- **secure-code-review.md**: Code review for security vulnerabilities
- **../Cybersecurity/threat-modeling.md**: Detailed threat modeling methodologies
- **../Security-Operations/penetration-testing.md**: Manual security testing
- **../Security-Operations/vulnerability-management.md**: Vulnerability lifecycle management
- **../Identity-Access-Management/zero-trust-architecture.md**: Zero trust security model

---

## Additional Resources

**OWASP Resources**:
- OWASP Top 10 (2021)
- OWASP ASVS (Application Security Verification Standard)
- OWASP Testing Guide
- OWASP Cheat Sheet Series

**Standards & Frameworks**:
- NIST Cybersecurity Framework
- CIS Controls
- ISO 27001/27002
- PCI-DSS, HIPAA, GDPR (compliance specific)

**Tools**:
- SAST: SonarQube, Semgrep, Checkmarx, Veracode
- DAST: OWASP ZAP, Burp Suite, Acunetix
- SCA: Snyk, WhiteSource, Black Duck, Dependabot
- SIEM: Splunk, ELK Stack, Datadog

**Training**:
- OWASP Web Security Testing Guide
- PortSwigger Web Security Academy (free)
- SANS Secure Coding courses
- Cybersecurity certifications (CISSP, CEH, OSCP, OSWE)

---

*This framework provides comprehensive guidance for web application security. Security is not a one-time activity but an ongoing process throughout the application lifecycle. Adapt this framework to your specific application architecture, threat model, and compliance requirements. Remember: security is a journey, not a destination.*
