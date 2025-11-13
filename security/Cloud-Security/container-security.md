---
title: "Container Security Framework"
category: security
tags: [security, containers, docker, kubernetes, cloud-security, devsecops]
description: "Comprehensive framework for securing containerized applications covering image security, runtime protection, Kubernetes security, supply chain security, and container orchestration best practices."
related_templates:
  - ../Cybersecurity/devsecops-implementation.md
  - cloud-security-architecture.md
  - kubernetes-security.md
  - ../Application-Security/web-application-security.md
  - ../Security-Operations/vulnerability-management.md
version: 2.0
last_updated: 2025-11-12
---

# Container Security Framework

## Purpose
This framework provides comprehensive security guidance for containerized applications and orchestration platforms. It covers container image security, build-time and runtime protection, Kubernetes security hardening, supply chain security, network policies, secrets management, and compliance for containerized environments.

## Quick Start

1. **Secure Container Images**: Use minimal base images, scan for vulnerabilities, run as non-root, implement multi-stage builds
2. **Harden Container Runtime**: Enable security profiles (AppArmor/SELinux), drop capabilities, use read-only filesystems
3. **Secure Kubernetes**: Implement RBAC, network policies, pod security standards, enable audit logging
4. **Supply Chain Security**: Sign images, generate SBOMs, verify signatures, use private registries
5. **Monitor & Respond**: Deploy runtime security (Falco), monitor for anomalies, automate incident response

---

## Minimal Example

**SCENARIO**: A team deploying microservices on Kubernetes needs to implement container security without disrupting development velocity.

**Secure Dockerfile**:
```dockerfile
# Multi-stage build with security best practices
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine
# Install security updates
RUN apk --no-cache upgrade

# Create non-root user
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001

WORKDIR /app
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --chown=nodejs:nodejs . .

# Drop to non-root
USER nodejs

EXPOSE 3000
CMD ["node", "server.js"]
```

**Kubernetes Pod Security**:
```yaml
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
        drop: [ALL]
      readOnlyRootFilesystem: true
    resources:
      limits:
        cpu: "1"
        memory: "512Mi"
```

**Security Scanning**:
```bash
# Scan image with Trivy
trivy image --severity HIGH,CRITICAL myapp:v1.0.0

# Scan with Grype
grype myapp:v1.0.0 --fail-on high
```

**Result**: Secure containerized application with minimal attack surface, vulnerability scanning, and runtime protection.

---

## Comprehensive Framework

### PHASE 1: Container Image Security

#### 1.1 Secure Base Images

**Base Image Selection**:

| Base Image Type | Use Case | Size | Security Posture |
|-----------------|----------|------|------------------|
| **Distroless** | Production apps | Minimal (~2MB) | Excellent (no shell, no package manager) |
| **Alpine** | General purpose | Small (~5MB) | Good (minimal packages) |
| **Debian Slim** | Compatibility needed | Medium (~30MB) | Good (trimmed Debian) |
| **Ubuntu** | Full compatibility | Large (~70MB) | Fair (more attack surface) |
| **Scratch** | Static binaries | Minimal (<1MB) | Excellent (empty base) |

**Distroless Example** (Recommended for Production):
```dockerfile
# Multi-stage build with distroless
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /app/server

# Distroless base (no shell, no package manager)
FROM gcr.io/distroless/static-debian11
COPY --from=builder /app/server /server
USER nonroot:nonroot
ENTRYPOINT ["/server"]
```

**Alpine Example** (Good Balance):
```dockerfile
FROM node:18-alpine
# Install security updates
RUN apk --no-cache upgrade && \
    apk --no-cache add dumb-init

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

USER nodejs
WORKDIR /app
COPY --chown=nodejs:nodejs . .

ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "server.js"]
```

**Scratch Example** (Minimal):
```dockerfile
# For static Go binaries
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -ldflags="-w -s" -o server

FROM scratch
COPY --from=builder /app/server /server
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
USER 65534:65534
ENTRYPOINT ["/server"]
```

#### 1.2 Dockerfile Security Best Practices

**Multi-Stage Builds**:
```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Test stage (optional, run tests in CI)
FROM builder AS tester
RUN npm run test

# Production stage
FROM node:18-alpine
RUN apk --no-cache upgrade
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
WORKDIR /app
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
USER nodejs
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s CMD node healthcheck.js || exit 1
CMD ["node", "dist/server.js"]
```

**Security Anti-Patterns to Avoid**:
```dockerfile
# ❌ BAD PRACTICES

# Running as root
USER root

# Installing unnecessary packages
RUN apt-get install -y vim curl wget netcat

# Using latest tag
FROM node:latest

# Exposing unnecessary ports
EXPOSE 22 3306 5432

# Hardcoded secrets
ENV DATABASE_PASSWORD=supersecret

# Copying entire filesystem
COPY / /app

# ✅ GOOD PRACTICES

# Run as non-root
USER 1001

# Minimal packages only
RUN apk add --no-cache ca-certificates

# Specific version tags
FROM node:18.17.0-alpine3.18

# Only necessary ports
EXPOSE 3000

# Secrets via environment/volume
ENV DATABASE_PASSWORD_FILE=/run/secrets/db_password

# Copy only needed files
COPY package*.json ./
COPY src/ ./src/
```

**Layer Optimization**:
```dockerfile
# Optimize layer caching
FROM node:18-alpine

# 1. Install system dependencies (changes rarely)
RUN apk --no-cache add dumb-init

# 2. Create user (changes rarely)
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001

# 3. Set working directory
WORKDIR /app

# 4. Copy dependency files first (changes moderately)
COPY --chown=nodejs:nodejs package*.json ./

# 5. Install dependencies (expensive, cache when possible)
RUN npm ci --only=production && npm cache clean --force

# 6. Copy application code (changes frequently)
COPY --chown=nodejs:nodejs . .

USER nodejs
CMD ["dumb-init", "node", "server.js"]
```

#### 1.3 Container Image Scanning

**Scanning Tools**:

| Tool | Type | Strengths | Integration |
|------|------|-----------|-------------|
| **Trivy** | Open Source | Fast, comprehensive, easy to use | CLI, CI/CD, Kubernetes |
| **Grype** | Open Source | Accurate, SBOM support | CLI, CI/CD |
| **Clair** | Open Source | Continuous monitoring | Quay registry |
| **Snyk** | Commercial | Developer-friendly, fix guidance | IDE, CI/CD, registry |
| **Aqua** | Commercial | Enterprise features, runtime protection | Full platform |
| **Prisma Cloud** | Commercial | Multi-cloud, compliance | Full platform |

**Trivy Scanning**:
```bash
# Basic scan
trivy image myapp:v1.0.0

# Scan with severity threshold
trivy image --severity HIGH,CRITICAL myapp:v1.0.0

# Exit with error on findings
trivy image --exit-code 1 --severity CRITICAL myapp:v1.0.0

# Output formats
trivy image --format json -o report.json myapp:v1.0.0
trivy image --format sarif -o report.sarif myapp:v1.0.0

# Scan specific vulnerabilities
trivy image --vuln-type os,library myapp:v1.0.0

# Ignore unfixed vulnerabilities
trivy image --ignore-unfixed myapp:v1.0.0

# Scan Dockerfile
trivy config Dockerfile
```

**CI/CD Integration**:
```yaml
# GitHub Actions
- name: Run Trivy vulnerability scanner
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'myapp:${{ github.sha }}'
    format: 'sarif'
    output: 'trivy-results.sarif'
    severity: 'CRITICAL,HIGH'
    exit-code: '1'

- name: Upload Trivy results to GitHub Security
  uses: github/codeql-action/upload-sarif@v2
  if: always()
  with:
    sarif_file: 'trivy-results.sarif'
```

**Vulnerability Management**:
```yaml
# trivy.yaml - Scanning policy
scan:
  severity: [CRITICAL, HIGH, MEDIUM]
  ignore-unfixed: false
  timeout: 5m

  # Fail build on findings
  fail-on:
    - severity: CRITICAL
      count: 0
    - severity: HIGH
      count: 5

  # Suppression list (with justification)
  suppressions:
    - id: CVE-2023-12345
      reason: "False positive - not using affected code path"
      expires: 2025-03-01
    - id: CVE-2023-67890
      reason: "Fix not available, mitigated by network controls"
      expires: 2025-02-01
```

---

### PHASE 2: Container Runtime Security

#### 2.1 Container Runtime Configuration

**Security Contexts**:
```yaml
# Pod-level security context
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    # Run as non-root
    runAsNonRoot: true
    runAsUser: 1001
    runAsGroup: 1001
    fsGroup: 1001

    # Seccomp profile
    seccompProfile:
      type: RuntimeDefault

    # SELinux options
    seLinuxOptions:
      level: "s0:c123,c456"

  containers:
  - name: app
    image: myapp:v1.0.0

    # Container-level security context
    securityContext:
      # Prevent privilege escalation
      allowPrivilegeEscalation: false

      # Drop all capabilities
      capabilities:
        drop:
          - ALL
        add:
          - NET_BIND_SERVICE  # Only if needed

      # Read-only root filesystem
      readOnlyRootFilesystem: true

      # Run as specific user
      runAsUser: 1001
      runAsNonRoot: true

    # Resource limits
    resources:
      limits:
        cpu: "1"
        memory: "512Mi"
      requests:
        cpu: "100m"
        memory: "128Mi"

    # Volume mounts for writable areas
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

**AppArmor Profile**:
```yaml
# Pod with AppArmor profile
apiVersion: v1
kind: Pod
metadata:
  name: apparmor-pod
  annotations:
    container.apparmor.security.beta.kubernetes.io/app: runtime/default
spec:
  containers:
  - name: app
    image: myapp:v1.0.0
```

**Seccomp Profile**:
```json
// seccomp-profile.json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64"],
  "syscalls": [
    {
      "names": [
        "accept4", "access", "arch_prctl", "bind", "brk",
        "chmod", "chown", "clock_gettime", "clone", "close",
        "connect", "dup", "dup2", "epoll_create1", "epoll_ctl",
        "epoll_wait", "exit", "exit_group", "fchmod", "fchown",
        "fcntl", "fstat", "fstatfs", "futex", "getcwd",
        "getdents64", "getegid", "geteuid", "getgid", "getpeername",
        "getpid", "getppid", "getrandom", "getsockname", "getsockopt",
        "getuid", "listen", "lseek", "madvise", "mmap",
        "mprotect", "munmap", "nanosleep", "newfstatat", "open",
        "openat", "pipe", "pipe2", "poll", "prctl",
        "pread64", "pwrite64", "read", "readlink", "readlinkat",
        "recvfrom", "recvmsg", "rt_sigaction", "rt_sigprocmask", "rt_sigreturn",
        "sched_getaffinity", "sched_yield", "sendmsg", "sendto", "set_robust_list",
        "set_tid_address", "setgid", "setgroups", "setsockopt", "setuid",
        "shutdown", "sigaltstack", "socket", "stat", "statfs",
        "tgkill", "uname", "unlink", "wait4", "write"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

#### 2.2 Linux Capabilities

**Understanding Capabilities**:
```yaml
# Default Docker capabilities (DO NOT USE IN PRODUCTION)
capabilities:
  - CHOWN
  - DAC_OVERRIDE
  - FSETID
  - FOWNER
  - MKNOD
  - NET_RAW
  - SETGID
  - SETUID
  - SETFCAP
  - SETPCAP
  - NET_BIND_SERVICE
  - SYS_CHROOT
  - KILL
  - AUDIT_WRITE

# Secure: Drop all, add only necessary
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: app
    securityContext:
      capabilities:
        drop:
          - ALL
        add:
          - NET_BIND_SERVICE  # To bind to port <1024
          # Add others only if absolutely necessary
```

**Common Capability Use Cases**:
```yaml
# Web server binding to port 80/443
capabilities:
  drop: [ALL]
  add: [NET_BIND_SERVICE]

# Application performing chown operations
capabilities:
  drop: [ALL]
  add: [CHOWN, FOWNER]

# Network diagnostic tools (ping, traceroute)
capabilities:
  drop: [ALL]
  add: [NET_RAW, NET_ADMIN]

# Time synchronization
capabilities:
  drop: [ALL]
  add: [SYS_TIME]
```

#### 2.3 Runtime Security Monitoring

**Falco Rules**:
```yaml
# Falco rules for container security
- rule: Unauthorized Process in Container
  desc: Detect unexpected processes in container
  condition: >
    spawned_process and container and
    not proc.name in (node, python, java, nginx) and
    not proc.pname in (node, python, java, nginx, sh, bash)
  output: >
    Unexpected process started in container
    (user=%user.name command=%proc.cmdline container=%container.name image=%container.image.repository)
  priority: WARNING
  tags: [container, process]

- rule: Write to Non-Writable Directory
  desc: Detect writes to read-only filesystem
  condition: >
    open_write and container and
    fd.name startswith /etc and
    not fd.name in (/etc/resolv.conf, /etc/hosts, /etc/hostname)
  output: >
    Write attempt to read-only directory
    (file=%fd.name container=%container.name command=%proc.cmdline)
  priority: ERROR
  tags: [container, filesystem]

- rule: Container Privilege Escalation
  desc: Detect privilege escalation attempts
  condition: >
    spawned_process and container and
    proc.name in (sudo, su, setuid, setgid, capsh) and
    not user.name=root
  output: >
    Privilege escalation attempt
    (user=%user.name command=%proc.cmdline container=%container.name)
  priority: CRITICAL
  tags: [container, privilege_escalation]

- rule: Sensitive File Access in Container
  desc: Detect access to sensitive files
  condition: >
    open_read and container and
    fd.name in (/etc/shadow, /etc/sudoers, /root/.ssh/id_rsa, /root/.aws/credentials)
  output: >
    Sensitive file accessed
    (file=%fd.name user=%user.name container=%container.name)
  priority: CRITICAL
  tags: [container, sensitive_data]

- rule: Unexpected Network Connection
  desc: Detect unexpected outbound connections
  condition: >
    outbound and container and
    not fd.sip in (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) and
    not fd.sport in (80, 443, 53)
  output: >
    Unexpected outbound connection
    (connection=%fd.name container=%container.name)
  priority: WARNING
  tags: [container, network]
```

**Deploying Falco**:
```yaml
# Falco DaemonSet
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: falco
  namespace: falco
spec:
  selector:
    matchLabels:
      app: falco
  template:
    metadata:
      labels:
        app: falco
    spec:
      serviceAccountName: falco
      hostNetwork: true
      hostPID: true
      containers:
      - name: falco
        image: falcosecurity/falco:latest
        securityContext:
          privileged: true
        volumeMounts:
        - name: docker-socket
          mountPath: /host/var/run/docker.sock
        - name: dev
          mountPath: /host/dev
        - name: proc
          mountPath: /host/proc
          readOnly: true
        - name: boot
          mountPath: /host/boot
          readOnly: true
        - name: lib-modules
          mountPath: /host/lib/modules
          readOnly: true
        - name: falco-config
          mountPath: /etc/falco
      volumes:
      - name: docker-socket
        hostPath:
          path: /var/run/docker.sock
      - name: dev
        hostPath:
          path: /dev
      - name: proc
        hostPath:
          path: /proc
      - name: boot
        hostPath:
          path: /boot
      - name: lib-modules
        hostPath:
          path: /lib/modules
      - name: falco-config
        configMap:
          name: falco-config
```

---

### PHASE 3: Kubernetes Security

#### 3.1 Pod Security Standards

**Pod Security Levels**:

**Privileged** (Unrestricted, avoid in production):
- No restrictions
- Allows privileged containers
- Root user allowed

**Baseline** (Minimally restrictive):
- Prevents known privilege escalations
- Blocks privileged containers
- Restricts host namespaces

**Restricted** (Heavily restricted, recommended):
- Enforces hardening best practices
- Non-root user required
- Read-only root filesystem
- All capabilities dropped

**Pod Security Admission**:
```yaml
# Namespace-level Pod Security Standards
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

**Policy Enforcement with Kyverno**:
```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-restricted-pod-security
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
            securityContext:
              runAsNonRoot: true
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

    - name: disallow-privilege-escalation
      match:
        resources:
          kinds:
            - Pod
      validate:
        message: "Privilege escalation is not allowed"
        pattern:
          spec:
            containers:
              - securityContext:
                  allowPrivilegeEscalation: false
```

#### 3.2 RBAC & Access Control

**Principle of Least Privilege RBAC**:
```yaml
# ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  namespace: production

---
# Role (namespace-scoped)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-role
  namespace: production
rules:
  # Read-only access to ConfigMaps
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list"]
    resourceNames: ["app-config"]  # Specific ConfigMap only

  # Read-only access to Secrets
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get"]
    resourceNames: ["app-secret"]  # Specific Secret only

  # Pod logs access
  - apiGroups: [""]
    resources: ["pods/log"]
    verbs: ["get"]

---
# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-rolebinding
  namespace: production
subjects:
  - kind: ServiceAccount
    name: app-sa
    namespace: production
roleRef:
  kind: Role
  name: app-role
  apiGroup: rbac.authorization.k8s.io

---
# Pod using ServiceAccount
apiVersion: v1
kind: Pod
metadata:
  name: app
  namespace: production
spec:
  serviceAccountName: app-sa
  automountServiceAccountToken: true  # Set to false if not needed
  containers:
  - name: app
    image: myapp:v1.0.0
```

**ClusterRole for Multi-Namespace Access**:
```yaml
# ClusterRole for monitoring system
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: pod-reader
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["pods/log"]
    verbs: ["get"]

---
# ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: monitoring-pod-reader
subjects:
  - kind: ServiceAccount
    name: monitoring-sa
    namespace: monitoring
roleRef:
  kind: ClusterRole
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

#### 3.3 Network Policies

**Default Deny Network Policy**:
```yaml
# Deny all ingress and egress by default
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
```

**Allow Specific Traffic**:
```yaml
# Allow ingress from frontend to backend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080

---
# Allow egress to database
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-backend-to-database
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Egress
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - protocol: TCP
          port: 5432

---
# Allow DNS resolution
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Egress
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              name: kube-system
        - podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
```

#### 3.4 Secrets Management

**External Secrets Operator**:
```yaml
# SecretStore pointing to AWS Secrets Manager
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secrets-manager
  namespace: production
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
      auth:
        jwt:
          serviceAccountRef:
            name: external-secrets-sa

---
# ExternalSecret syncing from AWS
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: SecretStore
  target:
    name: app-secrets
    creationPolicy: Owner
  data:
    - secretKey: database-password
      remoteRef:
        key: prod/app/database
        property: password

    - secretKey: api-key
      remoteRef:
        key: prod/app/api
        property: key
```

**Sealed Secrets** (GitOps-friendly):
```bash
# Install Sealed Secrets controller
kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.24.0/controller.yaml

# Encrypt secret
echo -n 'supersecret' | kubectl create secret generic app-secret \
  --dry-run=client \
  --from-file=password=/dev/stdin \
  -o yaml | \
  kubeseal -o yaml > sealed-secret.yaml

# Commit sealed-secret.yaml to Git (safe, encrypted)
git add sealed-secret.yaml
git commit -m "Add sealed secret"
```

```yaml
# SealedSecret (safe to commit to Git)
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: app-secret
  namespace: production
spec:
  encryptedData:
    password: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq...
  template:
    metadata:
      name: app-secret
      namespace: production
```

---

### PHASE 4: Container Supply Chain Security

#### 4.1 Image Signing & Verification

**Cosign Image Signing**:
```bash
# Generate key pair
cosign generate-key-pair

# Sign image
cosign sign --key cosign.key myregistry.io/myapp:v1.0.0

# Verify signature
cosign verify --key cosign.pub myregistry.io/myapp:v1.0.0

# Sign with keyless (OIDC)
cosign sign myregistry.io/myapp:v1.0.0

# Verify keyless signature
cosign verify \
  --certificate-identity=user@company.com \
  --certificate-oidc-issuer=https://accounts.google.com \
  myregistry.io/myapp:v1.0.0
```

**Policy Enforcement with Kyverno**:
```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-image-signatures
spec:
  validationFailureAction: enforce
  background: false
  webhookTimeoutSeconds: 30
  rules:
    - name: verify-signature
      match:
        resources:
          kinds:
            - Pod
      verifyImages:
        - imageReferences:
            - "myregistry.io/myapp:*"
          attestors:
            - entries:
                - keys:
                    publicKeys: |-
                      -----BEGIN PUBLIC KEY-----
                      MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE...
                      -----END PUBLIC KEY-----
```

#### 4.2 Software Bill of Materials (SBOM)

**Generate SBOM**:
```bash
# Syft - Generate SBOM
syft packages myapp:v1.0.0 -o spdx-json > sbom.spdx.json
syft packages myapp:v1.0.0 -o cyclonedx-json > sbom.cyclonedx.json

# Attach SBOM to image
cosign attest --predicate sbom.spdx.json --key cosign.key myapp:v1.0.0

# Verify SBOM attestation
cosign verify-attestation --key cosign.pub myapp:v1.0.0
```

**SBOM Analysis**:
```bash
# Grype - Scan SBOM for vulnerabilities
grype sbom:./sbom.spdx.json

# OSS Review Toolkit - License compliance
ort analyze -i sbom.spdx.json
```

#### 4.3 Private Container Registry

**Harbor Configuration**:
```yaml
# Harbor with security features
harbor:
  # Enable vulnerability scanning
  core:
    scanner:
      enabled: true
      replicas: 1

  # Content trust (Notary)
  notary:
    enabled: true

  # Image replication
  replication:
    enabled: true

  # RBAC
  rbac:
    enabled: true

  # Audit logging
  audit:
    enabled: true

  # Retention policy
  retention:
    enabled: true
    policy:
      - tagRetention: 10
        daysRetention: 30
```

**Registry Security**:
```bash
# Pull image only from trusted registry
docker pull myregistry.io/myapp:v1.0.0

# Verify registry TLS certificate
docker pull --disable-content-trust=false myregistry.io/myapp:v1.0.0

# Use image pull secrets in Kubernetes
kubectl create secret docker-registry regcred \
  --docker-server=myregistry.io \
  --docker-username=user \
  --docker-password=pass \
  --docker-email=user@company.com
```

```yaml
# Pod with imagePullSecrets
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  imagePullSecrets:
    - name: regcred
  containers:
  - name: app
    image: myregistry.io/myapp:v1.0.0
```

---

### PHASE 5: Compliance & Governance

#### 5.1 Compliance Frameworks

**CIS Benchmarks**:
```bash
# Docker Bench Security
docker run --rm --net host --pid host --userns host --cap-add audit_control \
  -v /etc:/etc:ro \
  -v /usr/bin/containerd:/usr/bin/containerd:ro \
  -v /usr/bin/runc:/usr/bin/runc:ro \
  -v /usr/lib/systemd:/usr/lib/systemd:ro \
  -v /var/lib:/var/lib:ro \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  docker/docker-bench-security

# Kube-bench
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job.yaml
kubectl logs job/kube-bench
```

**Policy-as-Code with OPA**:
```rego
package kubernetes.admission

# Deny privileged containers
deny[msg] {
  input.request.kind.kind == "Pod"
  container := input.request.object.spec.containers[_]
  container.securityContext.privileged == true
  msg := sprintf("Privileged container not allowed: %v", [container.name])
}

# Require resource limits
deny[msg] {
  input.request.kind.kind == "Pod"
  container := input.request.object.spec.containers[_]
  not container.resources.limits
  msg := sprintf("Container must have resource limits: %v", [container.name])
}

# Enforce non-root user
deny[msg] {
  input.request.kind.kind == "Pod"
  not input.request.object.spec.securityContext.runAsNonRoot
  msg := "Pod must run as non-root user"
}
```

#### 5.2 Audit Logging

**Kubernetes Audit Policy**:
```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  # Log all pod creation/deletion
  - level: RequestResponse
    verbs: ["create", "delete", "patch"]
    resources:
      - group: ""
        resources: ["pods"]

  # Log secret access
  - level: Metadata
    verbs: ["get", "list", "watch"]
    resources:
      - group: ""
        resources: ["secrets"]

  # Log RBAC changes
  - level: RequestResponse
    verbs: ["create", "delete", "patch"]
    resources:
      - group: "rbac.authorization.k8s.io"
        resources: ["roles", "rolebindings", "clusterroles", "clusterrolebindings"]

  # Don't log health checks
  - level: None
    users: ["system:kube-proxy"]
    verbs: ["watch"]
    resources:
      - group: ""
        resources: ["endpoints", "services"]
```

---

## Variables Table

| Variable | Description | Example Values | Notes |
|----------|-------------|----------------|-------|
| `{BASE_IMAGE}` | Container base image | alpine, distroless, scratch | Distroless for prod |
| `{IMAGE_SCANNER}` | Vulnerability scanner | Trivy, Grype, Snyk, Aqua | Trivy open source |
| `{RUNTIME_SECURITY}` | Runtime monitoring | Falco, Aqua, Sysdig | Falco open source |
| `{POD_SECURITY_LEVEL}` | K8s security level | Privileged, Baseline, Restricted | Restricted for prod |
| `{SECRETS_MANAGER}` | Secrets storage | Vault, AWS Secrets, External Secrets | Based on cloud |
| `{REGISTRY}` | Container registry | Docker Hub, Harbor, ECR, GCR | Private for prod |
| `{SIGNING_TOOL}` | Image signing | Cosign, Notary | Cosign recommended |
| `{POLICY_ENGINE}` | Policy enforcement | Kyverno, OPA, Admission Controller | Kyverno easier |
| `{SERVICE_MESH}` | Service mesh | Istio, Linkerd, Consul | For mTLS |
| `{SCAN_THRESHOLD}` | Vulnerability threshold | CRITICAL, HIGH, MEDIUM | Block on CRITICAL |
| `{USER_ID}` | Non-root user ID | 1001, 65534 | >1000 recommended |
| `{RESOURCE_LIMITS}` | Pod resource limits | cpu: "1", memory: "512Mi" | Always set limits |

---

## Usage Examples

### Example 1: Microservices Startup (Cost-Conscious)

**Context**: Startup with 5 microservices, limited budget, deploying to managed Kubernetes (EKS).

**Container Security Stack** (Open Source):
- **Base Images**: Alpine Linux (balance of size and compatibility)
- **Scanner**: Trivy (open source, comprehensive)
- **Runtime Security**: Falco (open source, standard)
- **Policy Enforcement**: Kyverno (easier than OPA for K8s)
- **Secrets**: External Secrets Operator + AWS Secrets Manager
- **Registry**: Amazon ECR (managed, integrated)

**Secure Dockerfile Template**:
```dockerfile
FROM node:18-alpine
RUN apk --no-cache upgrade && apk add --no-cache dumb-init
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
WORKDIR /app
COPY --chown=nodejs:nodejs package*.json ./
RUN npm ci --only=production && npm cache clean --force
COPY --chown=nodejs:nodejs . .
USER nodejs
EXPOSE 3000
ENTRYPOINT ["dumb-init", "--"]
CMD ["node", "server.js"]
```

**CI/CD Pipeline** (GitHub Actions):
```yaml
name: Build and Deploy

on: [push]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          exit-code: '1'
          severity: 'CRITICAL,HIGH'

      - name: Push to ECR
        run: |
          aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
          docker tag myapp:${{ github.sha }} $ECR_REGISTRY/myapp:${{ github.sha }}
          docker push $ECR_REGISTRY/myapp:${{ github.sha }}
```

**Kubernetes Deployment** (Secure Defaults):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      serviceAccountName: myapp-sa
      securityContext:
        runAsNonRoot: true
        runAsUser: 1001
        fsGroup: 1001
        seccompProfile:
          type: RuntimeDefault

      containers:
      - name: app
        image: $ECR_REGISTRY/myapp:${{ github.sha }}
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: [ALL]
          readOnlyRootFilesystem: true

        resources:
          limits:
            cpu: "500m"
            memory: "256Mi"
          requests:
            cpu: "100m"
            memory: "128Mi"

        volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: cache
          mountPath: /app/cache

        env:
        - name: DATABASE_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-password

      volumes:
      - name: tmp
        emptyDir: {}
      - name: cache
        emptyDir: {}
```

**Kyverno Policies**:
```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: security-baseline
spec:
  validationFailureAction: enforce
  rules:
    - name: require-non-root
      match:
        resources:
          kinds: [Pod]
      validate:
        message: "Running as root not allowed"
        pattern:
          spec:
            securityContext:
              runAsNonRoot: true

    - name: require-drop-all-caps
      match:
        resources:
          kinds: [Pod]
      validate:
        message: "Must drop all capabilities"
        pattern:
          spec:
            containers:
            - securityContext:
                capabilities:
                  drop: [ALL]
```

**Network Policies**:
```yaml
# Default deny
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress

---
# Allow app to database
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-to-database
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
  - Egress
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
  - to:
    - namespaceSelector:
        matchLabels:
          name: kube-system
    - podSelector:
        matchLabels:
          k8s-app: kube-dns
    ports:
    - protocol: UDP
      port: 53
```

**Results**:
- Zero-cost security tools (all open source)
- <10 minute pipeline time (including security scans)
- Pod Security Standards enforced (Restricted level)
- Network segmentation with NetworkPolicies
- Secrets managed externally (AWS Secrets Manager)
- Runtime monitoring with Falco
- 95%+ reduction in security vulnerabilities

### Example 2: Enterprise Financial Services (Highly Regulated)

**Context**: Financial services company, PCI-DSS compliance required, 100+ microservices on Kubernetes.

**Container Security Stack** (Enterprise):
- **Base Images**: Google Distroless (minimal attack surface)
- **Scanner**: Aqua Security + Twistlock (commercial, comprehensive)
- **Runtime Security**: Aqua CNDR + Falco
- **Policy Enforcement**: OPA Gatekeeper (enterprise features)
- **Secrets**: HashiCorp Vault Enterprise
- **Registry**: Harbor Enterprise (on-premise)
- **Service Mesh**: Istio (mTLS everywhere)
- **Compliance**: Prisma Cloud (multi-cloud compliance)

**Ultra-Secure Dockerfile**:
```dockerfile
# Multi-stage build with distroless
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.* ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags="-w -s" -o server .

# Distroless base (no shell, no package manager)
FROM gcr.io/distroless/static-debian11:nonroot
COPY --from=builder /app/server /server
USER nonroot:nonroot
ENTRYPOINT ["/server"]
```

**Admission Control**:
```rego
# OPA policy for PCI-DSS compliance
package kubernetes.admission

# Deny privileged containers (PCI-DSS)
deny[msg] {
  input.request.kind.kind == "Pod"
  container := input.request.object.spec.containers[_]
  container.securityContext.privileged == true
  msg := sprintf("PCI-DSS: Privileged containers not allowed: %v", [container.name])
}

# Require signed images (PCI-DSS)
deny[msg] {
  input.request.kind.kind == "Pod"
  image := input.request.object.spec.containers[_].image
  not is_signed_image(image)
  msg := sprintf("PCI-DSS: Image must be signed: %v", [image])
}

# Require resource limits (PCI-DSS)
deny[msg] {
  input.request.kind.kind == "Pod"
  container := input.request.object.spec.containers[_]
  not container.resources.limits.cpu
  not container.resources.limits.memory
  msg := sprintf("PCI-DSS: Resource limits required: %v", [container.name])
}

# Enforce network segmentation (PCI-DSS)
deny[msg] {
  input.request.kind.kind == "Pod"
  namespace := input.request.namespace
  cardholder_namespace(namespace)
  not has_network_policy(namespace)
  msg := sprintf("PCI-DSS: NetworkPolicy required for cardholder data: %v", [namespace])
}
```

**Istio mTLS Enforcement**:
```yaml
# Require mTLS for all services
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT

---
# Authorization policy for cardholder data
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: cardholder-data-access
  namespace: payment
spec:
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/payment/sa/payment-processor"]
    to:
    - operation:
        methods: ["GET", "POST"]
        paths: ["/api/v1/payment"]
```

**Comprehensive Audit Logging**:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: audit-policy
  namespace: kube-system
data:
  audit-policy.yaml: |
    apiVersion: audit.k8s.io/v1
    kind: Policy
    rules:
      # Log all changes to cardholder data namespace
      - level: RequestResponse
        namespaces: ["payment", "cardholder-data"]
        verbs: ["create", "update", "patch", "delete"]

      # Log all secret access
      - level: Metadata
        resources:
        - group: ""
          resources: ["secrets"]
        verbs: ["get", "list", "watch"]

      # Log all RBAC changes
      - level: RequestResponse
        resources:
        - group: "rbac.authorization.k8s.io"
        verbs: ["create", "update", "patch", "delete"]
```

**Results**:
- PCI-DSS Level 1 compliance maintained
- SOC 2 Type II certified
- Zero critical vulnerabilities in production
- 100% mTLS coverage (service-to-service)
- Complete audit trail (7-year retention)
- Quarterly penetration testing passed
- <15 minute deployment pipeline with full security scanning

---

## Best Practices

### Image Security
- **Use Minimal Base Images**: Distroless or Alpine for production
- **Multi-Stage Builds**: Separate build and runtime dependencies
- **Specific Tags**: Never use `latest`, use specific version tags
- **Scan Everything**: Scan all images before deployment
- **Non-Root User**: Always run as non-root user

### Runtime Security
- **Drop All Capabilities**: Start with none, add only necessary ones
- **Read-Only Root FS**: Prevent runtime modifications
- **Seccomp/AppArmor**: Enable security profiles
- **Resource Limits**: Set CPU and memory limits
- **Runtime Monitoring**: Deploy Falco or equivalent

### Kubernetes Security
- **Pod Security Standards**: Enforce Restricted level
- **Network Policies**: Default deny, explicit allow
- **RBAC**: Least privilege for all service accounts
- **Secrets Management**: External secrets, never in ConfigMaps
- **Audit Logging**: Comprehensive audit trails

### Supply Chain
- **Sign Images**: Use Cosign for image signing
- **Generate SBOMs**: Track dependencies with SBOM
- **Verify Signatures**: Enforce signature verification
- **Private Registry**: Use private registry for production
- **Vulnerability Management**: Automated scanning and patching

---

## Common Pitfalls

### Image Pitfalls
- **Using `latest` Tag**: Breaks reproducibility and security
- **Running as Root**: Massive privilege escalation risk
- **Large Images**: More attack surface, slower deployments
- **Hardcoded Secrets**: Credentials in Dockerfile or image layers
- **No Multi-Stage**: Build tools and dependencies in production image

### Runtime Pitfalls
- **Privileged Containers**: Breaks container isolation
- **Host Path Mounts**: Access to host filesystem
- **No Resource Limits**: Resource exhaustion attacks
- **Excessive Capabilities**: More privileges than needed
- **No Security Contexts**: Missing security hardening

### Kubernetes Pitfalls
- **Default ServiceAccount**: Using default SA with cluster access
- **No Network Policies**: Unrestricted pod-to-pod communication
- **Secrets in ConfigMaps**: Secrets stored as plain text
- **No Pod Security**: Missing Pod Security Standards
- **Overly Permissive RBAC**: Too many permissions granted

### Supply Chain Pitfalls
- **Unsigned Images**: Can't verify image provenance
- **No SBOM**: Can't track dependencies for vulnerabilities
- **Public Registries**: Pulling from untrusted sources
- **No Image Scanning**: Deploying vulnerable images
- **Manual Processes**: Security checks not automated

---

## Related Templates

- **../Cybersecurity/devsecops-implementation.md**: DevSecOps pipeline integration
- **cloud-security-architecture.md**: Cloud-native security architecture
- **kubernetes-security.md**: Kubernetes security deep dive
- **../Application-Security/web-application-security.md**: Application security
- **../Security-Operations/vulnerability-management.md**: Vulnerability management

---

## Additional Resources

**Container Security**:
- CIS Docker Benchmark
- CIS Kubernetes Benchmark
- NIST Application Container Security Guide
- Docker Security Best Practices

**Tools**:
- Scanning: Trivy, Grype, Clair, Snyk, Aqua
- Runtime: Falco, Aqua, Sysdig, Prisma Cloud
- Policy: Kyverno, OPA Gatekeeper
- Signing: Cosign, Notary
- SBOM: Syft, CycloneDX

**Kubernetes Security**:
- Kubernetes Security Documentation
- Pod Security Standards
- RBAC Best Practices
- Network Policies Guide

**Training**:
- Certified Kubernetes Security Specialist (CKS)
- Docker Security Course (Udemy, Pluralsight)
- Kubernetes Security (A Cloud Guru)

---

*This framework provides comprehensive container security guidance. Container security is a shared responsibility across development, operations, and security teams. Implement security controls at every layer - from base images to runtime monitoring - and automate security checks in your CI/CD pipeline. Remember: secure by default, defense in depth.*
