---
title: "DevSecOps Implementation Framework"
category: security
tags: [security, devsecops, ci-cd, automation, shift-left, development]
description: "Comprehensive framework for integrating security into DevOps pipelines with automated testing, secure CI/CD, infrastructure as code security, and security-as-code practices."
related_templates:
  - ../Application-Security/web-application-security.md
  - ../Application-Security/secure-code-review.md
  - ../Cloud-Security/cloud-security-architecture.md
  - ../Cloud-Security/container-security.md
  - ../Security-Operations/vulnerability-management.md
version: 2.0
last_updated: 2025-11-12
---

# DevSecOps Implementation Framework

## Purpose
This framework provides a comprehensive approach to integrating security into DevOps practices and CI/CD pipelines. It covers shift-left security, automated security testing (SAST, DAST, SCA), secure pipeline design, infrastructure as code (IaC) security, container security, secrets management, and security-as-code practices to enable secure, rapid software delivery.

## Quick Start

1. **Shift Left Security**: Integrate security early in development with IDE plugins, pre-commit hooks, and developer security training
2. **Automate Security Testing**: Implement SAST, SCA, and secrets scanning in CI pipeline; DAST in deployment pipeline
3. **Secure CI/CD Pipeline**: Harden build systems, implement pipeline security controls, enforce approval gates
4. **Infrastructure as Code Security**: Scan IaC templates (Terraform, CloudFormation) for misconfigurations
5. **Monitor & Respond**: Deploy runtime security monitoring, logging, and automated incident response

---

## Minimal Example

**SCENARIO**: A development team building a web application needs to integrate security into their CI/CD pipeline without slowing down releases.

**DevSecOps Implementation**:

**Developer Environment** (Shift-Left):
- IDE security plugins (Snyk, SonarLint) for real-time feedback
- Pre-commit hooks: Git secrets scanning, basic linting
- Security training: OWASP Top 10, secure coding practices

**CI Pipeline** (Automated Security):
```yaml
# GitHub Actions CI Pipeline
name: CI with Security

on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      # SAST - Static Application Security Testing
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: p/security-audit

      # SCA - Software Composition Analysis
      - name: Run Snyk Dependency Scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

      # Secrets Scanning
      - name: Run TruffleHog
        uses: trufflesecurity/trufflehog@main

      # Container Scanning (if applicable)
      - name: Run Trivy Container Scan
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'myapp:${{ github.sha }}'
          severity: 'CRITICAL,HIGH'

      # Fail build on critical vulnerabilities
      - name: Check Security Results
        run: |
          if [ "$CRITICAL_VULNS" -gt 0 ]; then
            echo "Critical vulnerabilities found"
            exit 1
          fi
```

**CD Pipeline** (Deployment Security):
- DAST scanning on staging environment
- Infrastructure as Code (IaC) scanning
- Security approval gate for production
- Runtime security monitoring enabled

**Results**:
- Security integrated without blocking developers
- Vulnerabilities caught pre-production (90%+ reduction in production issues)
- 5-minute security scan time (minimal impact on build time)
- Developer security awareness increased

---

## Comprehensive Framework

### PHASE 1: Shift-Left Security (Development)

#### 1.1 Developer Security Environment

**IDE Security Plugins**:

| IDE | Security Plugins | Features |
|-----|------------------|----------|
| **VS Code** | Snyk, SonarLint, GitGuardian | Real-time vulnerability detection, secure code suggestions |
| **IntelliJ** | Snyk, SonarLint, CheckStyle | SAST, dependency scanning, code quality |
| **Eclipse** | SpotBugs, SonarLint | Static analysis, bug detection |

**Example: VS Code Security Setup**:
```json
// .vscode/settings.json
{
  "snyk.enable": true,
  "snyk.severity": "high",
  "sonarlint.enable": true,
  "sonarlint.rules": {
    "security:*": true
  },
  "gitguardian.enable": true
}
```

**Pre-Commit Hooks**:
```bash
# .git/hooks/pre-commit
#!/bin/bash

# Secrets scanning
echo "Scanning for secrets..."
if ! git secrets --scan; then
    echo "❌ Secrets detected! Commit blocked."
    exit 1
fi

# SAST quick scan
echo "Running quick security scan..."
if ! semgrep --config auto --error --quiet .; then
    echo "❌ Security issues detected! Commit blocked."
    exit 1
fi

# Dependency check
echo "Checking dependencies..."
if ! snyk test --severity-threshold=high; then
    echo "⚠️  High severity vulnerabilities in dependencies"
    # Warning only, don't block commit
fi

echo "✅ Pre-commit security checks passed"
```

**Security Linting Rules**:
```yaml
# .semgrep.yml - Security rules for pre-commit
rules:
  - id: hardcoded-secret
    pattern: |
      password = "..."
    message: Hardcoded password detected
    severity: ERROR

  - id: sql-injection
    pattern: |
      execute($SQL)
    message: Possible SQL injection
    severity: ERROR

  - id: xss-vulnerability
    pattern: |
      innerHTML = $USER_INPUT
    message: Possible XSS vulnerability
    severity: ERROR
```

#### 1.2 Security Training for Developers

**Training Program**:
- **Onboarding**: OWASP Top 10, secure coding fundamentals
- **Ongoing**: Monthly security topics (e.g., authentication, cryptography)
- **Hands-On**: Capture the Flag (CTF) exercises, vulnerable app practice
- **Certification**: OWASP, SANS secure coding courses

**Secure Coding Guidelines**:
```markdown
# Secure Coding Checklist

## Input Validation
- [ ] Validate all user input (whitelist approach)
- [ ] Use parameterized queries (no string concatenation)
- [ ] Sanitize output (context-aware encoding)

## Authentication & Authorization
- [ ] Never trust client-side data
- [ ] Check authorization on every request
- [ ] Use strong password hashing (bcrypt, Argon2)
- [ ] Implement MFA for sensitive operations

## Cryptography
- [ ] Use strong algorithms (AES-256, RSA-2048+)
- [ ] Never hardcode secrets (use environment variables/vault)
- [ ] Use TLS 1.2+ for all connections

## Error Handling
- [ ] Log errors securely (no sensitive data in logs)
- [ ] Generic error messages to users
- [ ] Implement proper exception handling
```

**Security Champions Program**:
- Identify security champions in each team
- Champions receive advanced security training
- Act as security liaisons between dev team and security team
- Review security findings and mentor team members

#### 1.3 Secure Development Workflow

**Branch Protection Rules**:
```yaml
# GitHub branch protection configuration
main:
  required_status_checks:
    - security-scan
    - dependency-check
    - code-review
  required_reviewers: 2
  require_code_owner_review: true
  dismiss_stale_reviews: true
  enforce_admins: true
```

**Security Code Review Checklist**:
- [ ] No hardcoded secrets or credentials
- [ ] Input validation on all user inputs
- [ ] Authorization checks present
- [ ] Parameterized queries (no SQL injection)
- [ ] Output encoding (no XSS)
- [ ] Secure error handling (no information disclosure)
- [ ] Dependencies up to date (no known vulnerabilities)

---

### PHASE 2: CI/CD Pipeline Security

#### 2.1 Secure CI/CD Architecture

**Pipeline Security Principles**:
1. **Least Privilege**: CI/CD systems have minimum necessary permissions
2. **Segregation**: Development, staging, production pipelines segregated
3. **Immutable Artifacts**: Build once, deploy many times
4. **Audit Logging**: All pipeline actions logged
5. **Secrets Management**: No secrets in code or pipeline definitions

**Secure Pipeline Architecture**:
```
Developer → Git Push → Webhook
                ↓
        CI/CD System (GitLab CI, GitHub Actions)
                ↓
        Security Scanning (SAST, SCA, Secrets)
                ↓
        Build & Package (Immutable Artifact)
                ↓
        Artifact Repository (Signed, Hashed)
                ↓
        Deploy to Staging → DAST Scan → Security Approval
                ↓
        Deploy to Production → Runtime Monitoring
```

**CI/CD Security Controls**:
```yaml
# GitLab CI with security controls
stages:
  - build
  - test
  - security
  - deploy

# SAST - Static Application Security Testing
sast:
  stage: security
  image: returntocorp/semgrep
  script:
    - semgrep --config=p/security-audit --config=p/owasp-top-ten --json -o sast-report.json .
  artifacts:
    reports:
      sast: sast-report.json
  allow_failure: false  # Block pipeline on findings

# SCA - Software Composition Analysis
dependency-scan:
  stage: security
  image: snyk/snyk:node
  script:
    - snyk test --severity-threshold=high --json > sca-report.json
  artifacts:
    reports:
      dependency_scanning: sca-report.json
  allow_failure: false

# Secrets Scanning
secrets-scan:
  stage: security
  image: trufflesecurity/trufflehog:latest
  script:
    - trufflehog filesystem . --json > secrets-report.json
    - if [ -s secrets-report.json ]; then exit 1; fi
  allow_failure: false

# Container Scanning
container-scan:
  stage: security
  image: aquasec/trivy
  script:
    - trivy image --severity HIGH,CRITICAL --exit-code 1 $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  allow_failure: false

# IaC Scanning
iac-scan:
  stage: security
  image: bridgecrew/checkov
  script:
    - checkov -d terraform/ --output json > iac-report.json
  allow_failure: false

# Build with security hardening
build:
  stage: build
  script:
    - docker build --no-cache -t $IMAGE_NAME .
    - docker scan $IMAGE_NAME
  artifacts:
    paths:
      - $IMAGE_NAME

# Sign artifacts
sign-artifacts:
  stage: build
  script:
    - cosign sign --key $SIGNING_KEY $IMAGE_NAME
    - cosign verify --key $PUBLIC_KEY $IMAGE_NAME
```

#### 2.2 Security Testing Automation

**Testing Types in CI/CD**:

| Test Type | Tool Examples | When to Run | What It Finds |
|-----------|---------------|-------------|---------------|
| **SAST** | Semgrep, SonarQube, Checkmarx | Every commit | Code vulnerabilities (SQL injection, XSS) |
| **SCA** | Snyk, Dependabot, WhiteSource | Every commit | Vulnerable dependencies |
| **Secrets** | TruffleHog, GitGuardian, Gitleaks | Every commit | Hardcoded secrets, credentials |
| **Container** | Trivy, Clair, Anchore | After build | Container image vulnerabilities |
| **IaC** | Checkov, tfsec, Terrascan | Before deploy | Infrastructure misconfigurations |
| **DAST** | OWASP ZAP, Burp Suite | After deploy (staging) | Runtime vulnerabilities |
| **IAST** | Contrast, Seeker | During testing | Runtime analysis with instrumentation |

**SAST Implementation**:
```yaml
# Comprehensive SAST configuration
sast:
  tools:
    - name: Semgrep
      rules:
        - p/security-audit
        - p/owasp-top-ten
        - p/ci
      config: |
        rules:
          - id: custom-rule-1
            pattern: eval($X)
            message: "Dangerous eval() usage"
            severity: ERROR

    - name: SonarQube
      quality_gate: true
      thresholds:
        blocker: 0
        critical: 0
        security_hotspots: 0

  fail_conditions:
    - critical_count > 0
    - high_count > 5
    - security_hotspot_rating < B
```

**SCA Implementation**:
```javascript
// package.json - Dependency security
{
  "scripts": {
    "audit": "npm audit --audit-level=moderate",
    "audit:fix": "npm audit fix",
    "snyk:test": "snyk test --severity-threshold=high",
    "snyk:monitor": "snyk monitor"
  },
  "devDependencies": {
    "snyk": "^1.1000.0"
  }
}
```

**Secrets Scanning**:
```python
# Pre-commit config for secrets detection
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/trufflesecurity/trufflehog
    rev: v3.63.0
    hooks:
      - id: trufflehog
        name: TruffleHog
        entry: trufflehog filesystem .
        language: system

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

**Container Security Scanning**:
```dockerfile
# Multi-stage build for smaller, more secure images
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine
# Run as non-root user
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
USER nodejs
WORKDIR /app
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --chown=nodejs:nodejs . .
EXPOSE 3000
CMD ["node", "server.js"]
```

```bash
# Scan container with Trivy
trivy image \
  --severity HIGH,CRITICAL \
  --exit-code 1 \
  --no-progress \
  myapp:latest

# Scan with Grype
grype myapp:latest \
  --fail-on high \
  --output json > grype-report.json
```

#### 2.3 CI/CD Pipeline Hardening

**Pipeline Security Controls**:

**1. Pipeline Access Control**:
```yaml
# GitLab CI - Protect pipeline variables
variables:
  DATABASE_PASSWORD:
    value: $DB_PASSWORD
    protected: true      # Only available in protected branches
    masked: true         # Masked in logs
    environment_scope: production

# Restrict who can run pipelines
permissions:
  pipelines:
    run: [maintainers, developers]
    approve: [maintainers only]
```

**2. Artifact Integrity**:
```bash
# Sign artifacts with cosign
cosign sign --key cosign.key myapp:v1.0.0

# Verify signature before deployment
cosign verify --key cosign.pub myapp:v1.0.0

# Generate SBOM (Software Bill of Materials)
syft packages myapp:v1.0.0 -o spdx-json > sbom.json

# Attest SBOM
cosign attest --predicate sbom.json --key cosign.key myapp:v1.0.0
```

**3. Secrets Management**:
```yaml
# Never store secrets in pipeline YAML
# ❌ BAD
deploy:
  script:
    - kubectl create secret generic db-password --from-literal=password=supersecret

# ✅ GOOD - Use CI/CD secrets management
deploy:
  script:
    - kubectl create secret generic db-password --from-literal=password=$DB_PASSWORD
  secrets:
    DB_PASSWORD:
      vault: production/db/password
      engine: kv-v2
```

**4. Network Isolation**:
- CI/CD runners in isolated network
- Outbound traffic restricted (whitelist)
- No direct internet access from build agents
- Private artifact registries

**5. Audit Logging**:
```json
// Pipeline audit log
{
  "timestamp": "2025-01-15T10:30:00Z",
  "pipeline_id": "12345",
  "triggered_by": "john.doe@company.com",
  "branch": "main",
  "commit": "abc123",
  "stages": [
    {"stage": "security", "status": "passed", "duration": "45s"},
    {"stage": "build", "status": "passed", "duration": "120s"},
    {"stage": "deploy", "status": "manual", "approver": "jane.smith@company.com"}
  ],
  "security_findings": {
    "sast": {"high": 0, "medium": 2},
    "sca": {"high": 0, "medium": 1},
    "secrets": {"high": 0}
  }
}
```

---

### PHASE 3: Infrastructure as Code (IaC) Security

#### 3.1 IaC Security Scanning

**IaC Scanning Tools**:
- **Checkov**: Multi-cloud IaC scanner (Terraform, CloudFormation, Kubernetes)
- **tfsec**: Terraform-specific security scanner
- **Terrascan**: Policy-based IaC scanner
- **Snyk IaC**: Vulnerability scanner for IaC

**Example: Terraform Security Scanning**:
```bash
# Scan Terraform with checkov
checkov -d terraform/ \
  --framework terraform \
  --output json \
  --output-file checkov-report.json \
  --soft-fail-on MEDIUM \
  --hard-fail-on HIGH

# Scan with tfsec
tfsec terraform/ \
  --format json \
  --out tfsec-report.json \
  --minimum-severity HIGH

# Scan with Terrascan
terrascan scan -d terraform/ \
  --iac-type terraform \
  --policy-type aws \
  --severity high \
  --output json > terrascan-report.json
```

**Common IaC Misconfigurations**:

```hcl
# ❌ BAD: Unencrypted S3 bucket
resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
  # No encryption configuration
}

# ✅ GOOD: Encrypted S3 bucket
resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# ❌ BAD: Security group allowing all traffic
resource "aws_security_group" "app" {
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  # Open to internet
  }
}

# ✅ GOOD: Restricted security group
resource "aws_security_group" "app" {
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]  # Internal only
  }
}

# ❌ BAD: IAM user with admin access
resource "aws_iam_user_policy_attachment" "admin" {
  user       = aws_iam_user.developer.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

# ✅ GOOD: Least privilege IAM policy
resource "aws_iam_policy" "app_access" {
  name = "app-access"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Resource = "arn:aws:s3:::my-app-bucket/*"
      }
    ]
  })
}
```

#### 3.2 IaC Security Best Practices

**Terraform Security Module**:
```hcl
# modules/secure-s3/main.tf
resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name

  tags = var.tags
}

# Enable versioning
resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Enable encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
  bucket = aws_s3_bucket.this.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = var.kms_key_id
    }
  }
}

# Block public access
resource "aws_s3_bucket_public_access_block" "this" {
  bucket = aws_s3_bucket.this.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Enable logging
resource "aws_s3_bucket_logging" "this" {
  bucket = aws_s3_bucket.this.id

  target_bucket = var.logging_bucket
  target_prefix = "s3-access-logs/${var.bucket_name}/"
}
```

**Policy as Code**:
```rego
# Open Policy Agent (OPA) policy for Terraform
package terraform.policies

deny[msg] {
  resource := input.resource.aws_s3_bucket[name]
  not resource.server_side_encryption_configuration
  msg := sprintf("S3 bucket '%s' does not have encryption enabled", [name])
}

deny[msg] {
  resource := input.resource.aws_security_group[name]
  rule := resource.ingress[_]
  rule.cidr_blocks[_] == "0.0.0.0/0"
  msg := sprintf("Security group '%s' allows access from 0.0.0.0/0", [name])
}

deny[msg] {
  resource := input.resource.aws_iam_policy[name]
  statement := resource.policy.Statement[_]
  statement.Effect == "Allow"
  statement.Action[_] == "*"
  statement.Resource == "*"
  msg := sprintf("IAM policy '%s' grants overly permissive access", [name])
}
```

---

### PHASE 4: Container & Kubernetes Security

#### 4.1 Container Security

**Container Image Best Practices**:
```dockerfile
# Secure Dockerfile example
# Use specific version (not 'latest')
FROM node:18.17.0-alpine3.18 AS builder

# Run as non-root user
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001

# Set working directory
WORKDIR /app

# Copy dependency files first (layer caching)
COPY --chown=nodejs:nodejs package*.json ./

# Install dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy application code
COPY --chown=nodejs:nodejs . .

# Build application
RUN npm run build

# Production image
FROM node:18.17.0-alpine3.18

# Install security updates
RUN apk --no-cache upgrade

# Create non-root user
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001

# Set working directory
WORKDIR /app

# Copy from builder
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist

# Drop to non-root user
USER nodejs

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node healthcheck.js || exit 1

# Run application
CMD ["node", "dist/server.js"]
```

**Container Runtime Security**:
```yaml
# Kubernetes Pod Security Standards
apiVersion: v1
kind: Pod
metadata:
  name: secure-app
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1001
    fsGroup: 1001
    seccompProfile:
      type: RuntimeDefault

  containers:
  - name: app
    image: myapp:v1.0.0
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
          - ALL
      readOnlyRootFilesystem: true

    resources:
      limits:
        cpu: "1"
        memory: "512Mi"
      requests:
        cpu: "0.5"
        memory: "256Mi"

    volumeMounts:
    - name: tmp
      mountPath: /tmp
    - name: cache
      mountPath: /app/cache

  volumes:
  - name: tmp
    emptyDir: {}
  - name: cache
    emptyDir: {}
```

#### 4.2 Kubernetes Security

**Kubernetes Security Controls**:
```yaml
# NetworkPolicy - Restrict pod-to-pod communication
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-network-policy
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432

---
# PodSecurityPolicy (deprecated, use Pod Security Standards)
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: restricted
spec:
  privileged: false
  allowPrivilegeEscalation: false
  requiredDropCapabilities:
    - ALL
  volumes:
    - 'configMap'
    - 'emptyDir'
    - 'secret'
  runAsUser:
    rule: 'MustRunAsNonRoot'
  seLinux:
    rule: 'RunAsAny'
  fsGroup:
    rule: 'RunAsAny'
  readOnlyRootFilesystem: true
```

**Kubernetes Secret Management**:
```yaml
# External Secrets Operator - Sync secrets from vault
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
spec:
  secretStoreRef:
    name: vault
    kind: SecretStore
  target:
    name: app-secrets
    creationPolicy: Owner
  data:
  - secretKey: database-password
    remoteRef:
      key: secret/data/database
      property: password
```

---

### PHASE 5: Security Monitoring & Response

#### 5.1 Runtime Security Monitoring

**Application Security Monitoring**:
```yaml
# Falco rules for runtime security
- rule: Unauthorized Process in Container
  desc: Detect unexpected processes running in container
  condition: >
    spawned_process and container and
    not proc.name in (node, npm, sh)
  output: >
    Unauthorized process in container
    (user=%user.name command=%proc.cmdline container=%container.name)
  priority: WARNING

- rule: Sensitive File Access
  desc: Detect access to sensitive files
  condition: >
    open_read and container and
    fd.name in (/etc/shadow, /etc/passwd, /root/.ssh/id_rsa)
  output: >
    Sensitive file accessed
    (user=%user.name file=%fd.name container=%container.name)
  priority: CRITICAL
```

**Security Metrics & Dashboards**:
```yaml
# Prometheus metrics for security monitoring
metrics:
  - name: security_vulnerabilities_total
    type: gauge
    labels: [severity, source]
    description: "Total number of vulnerabilities by severity"

  - name: security_scan_duration_seconds
    type: histogram
    labels: [scanner_type]
    description: "Duration of security scans"

  - name: failed_authentication_attempts_total
    type: counter
    labels: [service, user]
    description: "Failed authentication attempts"

  - name: suspicious_activity_total
    type: counter
    labels: [activity_type, severity]
    description: "Suspicious activities detected"
```

#### 5.2 Incident Response Automation

**Automated Response Actions**:
```python
# Security incident automation
class SecurityIncidentHandler:
    def handle_critical_vulnerability(self, vulnerability):
        """Automated response to critical vulnerability detection"""
        # 1. Create incident ticket
        incident = self.create_jira_ticket(
            summary=f"Critical vulnerability: {vulnerability.cve}",
            severity="CRITICAL",
            component=vulnerability.component
        )

        # 2. Notify security team
        self.send_slack_alert(
            channel="#security-alerts",
            message=f"🚨 Critical vulnerability detected: {vulnerability.cve}\n"
                    f"Component: {vulnerability.component}\n"
                    f"Ticket: {incident.key}"
        )

        # 3. Block deployment (if in pipeline)
        if vulnerability.in_pipeline:
            self.block_deployment(vulnerability.pipeline_id)

        # 4. Create remediation PR (if patch available)
        if vulnerability.has_patch:
            self.create_remediation_pr(vulnerability)

    def handle_secrets_exposure(self, secret_finding):
        """Automated response to exposed secrets"""
        # 1. Revoke compromised secret immediately
        self.revoke_secret(secret_finding.secret_id)

        # 2. Alert security team
        self.send_pagerduty_alert(
            title="Secret exposed in code",
            details=secret_finding,
            urgency="high"
        )

        # 3. Block commit/PR
        self.block_commit(secret_finding.commit_sha)

        # 4. Rotate secret
        new_secret = self.rotate_secret(secret_finding.secret_id)

        # 5. Update applications
        self.update_secret_in_vault(secret_finding.secret_id, new_secret)
```

---

## Variables Table

| Variable | Description | Example Values | Notes |
|----------|-------------|----------------|-------|
| `{SAST_TOOL}` | Static analysis tool | Semgrep, SonarQube, Checkmarx | Choose based on language |
| `{SCA_TOOL}` | Dependency scanner | Snyk, Dependabot, WhiteSource | SaaS vs self-hosted |
| `{DAST_TOOL}` | Dynamic scanner | OWASP ZAP, Burp Suite, Acunetix | For staging/pre-prod |
| `{CONTAINER_SCANNER}` | Container image scanner | Trivy, Clair, Anchore, Grype | Open source vs commercial |
| `{IAC_SCANNER}` | IaC security scanner | Checkov, tfsec, Terrascan | Multi-cloud support |
| `{SECRETS_SCANNER}` | Secrets detection | TruffleHog, GitGuardian, Gitleaks | Real-time vs batch |
| `{CI_CD_PLATFORM}` | CI/CD system | GitHub Actions, GitLab CI, Jenkins | Pipeline definition varies |
| `{SEVERITY_THRESHOLD}` | Block threshold | CRITICAL, HIGH, MEDIUM | Risk tolerance |
| `{SCAN_FREQUENCY}` | How often to scan | Every commit, Daily, Weekly | Balance speed vs thoroughness |
| `{APPROVAL_REQUIRED}` | Manual approval gate | Production only, All envs, None | Risk-based |
| `{SECRETS_MANAGER}` | Secret storage | AWS Secrets Manager, Vault, Azure Key Vault | Cloud vs on-prem |
| `{RUNTIME_SECURITY}` | Runtime monitoring | Falco, Aqua, Prisma Cloud | Container/K8s specific |

---

## Usage Examples

### Example 1: Startup DevSecOps (GitHub Actions + Open Source Tools)

**Context**: Small startup (10 developers) building SaaS application, needs DevSecOps on limited budget.

**DevSecOps Stack** (All Open Source):
- **Source Control**: GitHub
- **CI/CD**: GitHub Actions (free tier)
- **SAST**: Semgrep (free)
- **SCA**: Snyk (free tier), Dependabot (free)
- **Secrets**: TruffleHog (free)
- **Container**: Trivy (free)
- **DAST**: OWASP ZAP (free)

**GitHub Actions Workflow**:
```yaml
name: Security CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      # SAST with Semgrep
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/security-audit
            p/owasp-top-ten
            p/typescript

      # SCA with Snyk
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      # Secrets scanning
      - name: TruffleHog Scan
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD

  build-and-scan:
    needs: security-scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      # Build Docker image
      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .

      # Scan with Trivy
      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'

      # Upload to GitHub Security tab
      - name: Upload Trivy results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  deploy-staging:
    needs: build-and-scan
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        run: |
          # Deploy logic here
          echo "Deploying to staging..."

      # DAST with OWASP ZAP
      - name: OWASP ZAP Scan
        uses: zaproxy/action-full-scan@v0.4.0
        with:
          target: 'https://staging.myapp.com'
          rules_file_name: '.zap/rules.tsv'
          cmd_options: '-a'
```

**Developer Workflow**:
```bash
# Developer commits code
git add .
git commit -m "Add new feature"

# Pre-commit hooks run automatically
# - Secrets scanning (TruffleHog)
# - Quick SAST (Semgrep)

git push origin feature-branch

# GitHub Actions triggers:
# 1. SAST (Semgrep) - 2 minutes
# 2. SCA (Snyk) - 1 minute
# 3. Secrets (TruffleHog) - 30 seconds
# 4. Build + Container scan (Trivy) - 3 minutes
# Total: ~7 minutes
```

**Results**:
- Zero-cost DevSecOps implementation
- 90% of vulnerabilities caught pre-production
- <10 minute security scan time
- Developer adoption: 95% (minimal friction)

### Example 2: Enterprise DevSecOps (Full Stack)

**Context**: Enterprise (500+ developers), highly regulated industry (financial services), requires comprehensive DevSecOps.

**DevSecOps Stack**:
- **Source Control**: GitLab Self-Hosted
- **CI/CD**: GitLab CI
- **SAST**: SonarQube Enterprise, Checkmarx
- **SCA**: WhiteSource (Mend), JFrog Xray
- **Secrets**: GitGuardian Enterprise
- **Container**: Aqua Security, Twistlock
- **DAST**: Burp Suite Enterprise, Veracode
- **IAST**: Contrast Security
- **RASP**: Imperva RASP
- **SIEM**: Splunk Enterprise

**Multi-Stage Pipeline**:
```yaml
# .gitlab-ci.yml - Enterprise pipeline
stages:
  - security-shift-left
  - build
  - security-scan
  - test
  - security-test
  - deploy-staging
  - security-approval
  - deploy-production

# Pre-commit security
pre-commit-security:
  stage: security-shift-left
  script:
    - gitguardian scan --all-policies .
    - semgrep --config=auto --error .
  allow_failure: false

# SAST with SonarQube
sonarqube-scan:
  stage: security-scan
  image: sonarsource/sonar-scanner-cli
  script:
    - sonar-scanner
      -Dsonar.projectKey=$CI_PROJECT_NAME
      -Dsonar.sources=.
      -Dsonar.host.url=$SONAR_HOST_URL
      -Dsonar.login=$SONAR_TOKEN
      -Dsonar.qualitygate.wait=true
  allow_failure: false

# SAST with Checkmarx
checkmarx-scan:
  stage: security-scan
  script:
    - /opt/checkmarx/runCxConsole.sh scan create
      -ProjectName "$CI_PROJECT_NAME"
      -LocationPath .
      -Preset "High and Medium"
  artifacts:
    reports:
      sast: checkmarx-report.json
  allow_failure: false

# SCA with WhiteSource
whitesource-scan:
  stage: security-scan
  script:
    - java -jar /opt/whitesource/wss-unified-agent.jar
      -c whitesource.config
      -project "$CI_PROJECT_NAME"
  allow_failure: false

# Container scanning with Aqua
aqua-scan:
  stage: security-scan
  script:
    - aquasec scan
      --registry $CI_REGISTRY
      --image $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
      --fail-on high
  allow_failure: false

# Build and sign artifacts
build:
  stage: build
  script:
    - docker build -t $IMAGE .
    - cosign sign --key $SIGNING_KEY $IMAGE
    - syft packages $IMAGE -o spdx-json > sbom.json
    - cosign attest --predicate sbom.json --key $SIGNING_KEY $IMAGE
  artifacts:
    paths:
      - sbom.json

# IAST with Contrast Security
integration-test:
  stage: test
  script:
    - contrast-agent start
    - npm run test:integration
    - contrast-agent report
  allow_failure: false

# DAST with Burp Suite Enterprise
burp-dast:
  stage: security-test
  script:
    - burp-cli scan
      --url https://staging.company.com
      --config burp-config.json
      --report-output burp-report.html
  artifacts:
    paths:
      - burp-report.html
  allow_failure: false

# Security approval gate
security-approval:
  stage: security-approval
  script:
    - echo "Security review required"
  when: manual
  only:
    - main
  environment:
    name: production

# Production deployment
deploy-production:
  stage: deploy-production
  script:
    - kubectl apply -f k8s/
  only:
    - main
  environment:
    name: production
```

**Security Governance**:
- **Security Gates**: No critical/high vulnerabilities allowed in production
- **Approval Process**: Security team approval required for production deploys
- **Compliance**: SOC 2, PCI-DSS, SOX compliance automation
- **Audit Trail**: Complete audit trail of all deployments and security findings
- **Metrics**: Security dashboard with KPIs (MTTR, vulnerability trends, coverage)

**Results**:
- 95% reduction in production security incidents
- 80% reduction in security review time (automation)
- SOC 2 Type II + PCI-DSS compliance maintained
- <30 minute pipeline time (parallelization)
- Developer productivity maintained (security integrated, not bolted on)

### Example 3: Kubernetes Platform DevSecOps

**Context**: Cloud-native company running microservices on Kubernetes, 100+ services deployed daily.

**K8s Security Stack**:
- **Policy Enforcement**: OPA Gatekeeper, Kyverno
- **Runtime Security**: Falco, Aqua Security
- **Network Security**: Cilium Network Policies
- **Secrets**: External Secrets Operator + Vault
- **Admission Control**: Custom admission webhooks
- **Image Scanning**: Harbor + Trivy
- **Service Mesh Security**: Istio mTLS

**Security Policies as Code**:
```yaml
# Kyverno policy - Enforce security standards
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-security-standards
spec:
  validationFailureAction: enforce
  background: true
  rules:
    - name: require-non-root
      match:
        resources:
          kinds:
            - Pod
      validate:
        message: "Running as root is not allowed"
        pattern:
          spec:
            containers:
              - securityContext:
                  runAsNonRoot: true

    - name: require-drop-all-capabilities
      match:
        resources:
          kinds:
            - Pod
      validate:
        message: "All capabilities must be dropped"
        pattern:
          spec:
            containers:
              - securityContext:
                  capabilities:
                    drop:
                      - ALL

    - name: require-read-only-root-fs
      match:
        resources:
          kinds:
            - Pod
      validate:
        message: "Root filesystem must be read-only"
        pattern:
          spec:
            containers:
              - securityContext:
                  readOnlyRootFilesystem: true
```

**Automated Security Scanning Pipeline**:
```yaml
# ArgoCD ApplicationSet with security scanning
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: microservices
spec:
  generators:
    - git:
        repoURL: https://github.com/company/services
        revision: HEAD
        directories:
          - path: services/*
  template:
    metadata:
      name: '{{path.basename}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/company/services
        targetRevision: HEAD
        path: '{{path}}'
      destination:
        server: https://kubernetes.default.svc
        namespace: '{{path.basename}}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
        syncOptions:
          - CreateNamespace=true
      # Security pre-sync hooks
      hooks:
        - name: security-scan
          type: PreSync
          manifest: |
            apiVersion: batch/v1
            kind: Job
            metadata:
              name: security-scan
            spec:
              template:
                spec:
                  containers:
                    - name: trivy
                      image: aquasec/trivy
                      command: ["trivy", "image", "--exit-code", "1", "--severity", "HIGH,CRITICAL", "{{image}}"]
                  restartPolicy: Never
```

**Results**:
- 100+ microservices secured consistently
- Policy violations blocked at admission (99.9% enforcement)
- Runtime threats detected and alerted (Falco)
- Zero trust networking (mTLS everywhere)
- Automated compliance reporting (PCI-DSS, SOC 2)

---

## Best Practices

### Shift-Left Security
- **Start Early**: Integrate security from day 1, not as afterthought
- **Developer Training**: Invest in security training for all developers
- **Fast Feedback**: Security feedback in <5 minutes (IDE, pre-commit, CI)
- **Fix Forward**: Focus on fixing issues, not blaming developers
- **Security Champions**: Embed security expertise in development teams

### Automation
- **Automate Everything**: SAST, SCA, secrets scanning, container scanning, IaC scanning
- **Fail Fast**: Fail builds early on critical vulnerabilities
- **Parallel Scans**: Run security scans in parallel to minimize pipeline time
- **Smart Thresholds**: Block on critical/high, alert on medium/low
- **Continuous Monitoring**: Security doesn't end at deployment

### Pipeline Security
- **Least Privilege**: CI/CD systems have minimum necessary permissions
- **Immutable Artifacts**: Build once, deploy everywhere
- **Sign & Verify**: Sign artifacts, verify signatures before deployment
- **Secrets Management**: Never hardcode secrets, use vault/KMS
- **Audit Everything**: Comprehensive audit logging of all pipeline actions

### Continuous Improvement
- **Measure**: Track security metrics (vulnerabilities found, MTTR, coverage)
- **Learn**: Post-incident reviews, lessons learned
- **Iterate**: Continuously improve processes and tools
- **Feedback Loop**: Developer feedback shapes security tooling
- **Stay Current**: Keep security tools and practices up to date

---

## Common Pitfalls

### Implementation Pitfalls
- **Too Many Tools**: Tool sprawl creates noise and alert fatigue
- **No Prioritization**: Treating all findings equally overwhelms teams
- **Slow Pipelines**: Security adding 30+ minutes kills adoption
- **No False Positive Management**: Unmanaged false positives ignored
- **Bolt-On Security**: Adding security at the end instead of integrating early

### Process Pitfalls
- **No Developer Buy-In**: Forcing tools without developer input
- **Security Silos**: Security team separate from development
- **Manual Processes**: Manual security reviews don't scale
- **No Exception Process**: Rigid policies with no exception handling
- **Compliance Checkbox**: Compliance over actual security

### Technical Pitfalls
- **Secrets in Code**: Hardcoded credentials, API keys
- **Weak Pipeline Security**: Compromised CI/CD = compromised production
- **No Runtime Security**: Focus only on pre-deployment, ignore runtime
- **Ignoring Dependencies**: Focus on first-party code, ignore third-party
- **Configuration Drift**: IaC defines infra, but manual changes create drift

---

## Related Templates

- **../Application-Security/web-application-security.md**: Application security fundamentals
- **../Application-Security/secure-code-review.md**: Manual security code review
- **../Cloud-Security/cloud-security-architecture.md**: Cloud security architecture
- **../Cloud-Security/container-security.md**: Container and Kubernetes security
- **../Security-Operations/vulnerability-management.md**: Vulnerability lifecycle management

---

## Additional Resources

**DevSecOps Frameworks**:
- OWASP DevSecOps Guideline
- NIST DevSecOps Practices
- SANS DevSecOps Survey

**Tools & Platforms**:
- SAST: Semgrep, SonarQube, Checkmarx, Veracode
- SCA: Snyk, WhiteSource, Black Duck, Dependabot
- DAST: OWASP ZAP, Burp Suite, Acunetix
- Container: Trivy, Clair, Aqua, Prisma Cloud
- IaC: Checkov, tfsec, Terrascan, Snyk IaC
- Secrets: TruffleHog, GitGuardian, AWS Secrets Manager, Vault

**Training & Certification**:
- DevSecOps Foundation (DOF)
- Certified DevSecOps Professional (CDP)
- SANS DevSecOps courses
- Cloud provider DevSecOps training

**Community**:
- DevSecOps Days conferences
- OWASP DevSecOps projects
- Cloud Native Security Working Group

---

*This framework provides comprehensive guidance for DevSecOps implementation. DevSecOps is a cultural shift as much as a technical one - success requires people, processes, and technology aligned. Start small, automate incrementally, and continuously improve based on developer feedback and security outcomes.*
