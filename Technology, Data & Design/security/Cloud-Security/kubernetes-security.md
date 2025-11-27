---
category: security
last_updated: 2025-11-23
title: Kubernetes Security Framework
tags:
- security
- kubernetes-security
- container-security
- rbac
use_cases:
- Securing Kubernetes clusters and workloads
- Implementing K8s RBAC and network policies
- Container security and image scanning
- K8s compliance (CIS benchmarks, NSA guidelines)
related_templates:
- security/Cloud-Security/cloud-security-architecture.md
- technology/DevOps-Cloud/container-orchestration.md
industries:
- government
- technology
type: template
difficulty: intermediate
slug: kubernetes-security
---

# Kubernetes Security Framework

## Purpose
Comprehensive framework for securing Kubernetes clusters including RBAC, network policies, pod security, secrets management, admission control, and runtime security monitoring.

## Quick K8s Security Prompt
Secure [EKS/GKE/AKS/self-managed] Kubernetes cluster running [X] workloads. Implement: RBAC policies, network policies (deny-by-default), pod security standards (restricted), secrets management (Vault/sealed-secrets), image scanning in CI/CD, admission controllers (OPA/Kyverno), and runtime monitoring (Falco). Assess against CIS Kubernetes Benchmark. Deliver: security policies, deployment templates, and monitoring dashboards.

## Quick Start

**Need to secure Kubernetes quickly?** Use this minimal example:

```
Secure production Kubernetes cluster with 100 microservices. Implement RBAC, network policies, pod security standards, image scanning, secrets management with Vault, and runtime threat detection with Falco.
```

### When to Use This
- Setting up a new production Kubernetes cluster
- Hardening existing K8s deployments for compliance audits
- Implementing container security for regulated industries
- Migrating from traditional VMs to containerized workloads
- Preparing for CIS Kubernetes benchmark assessments

### Basic 3-Step Workflow
1. **Secure Control Plane** - API server, etcd, RBAC
2. **Secure Workloads** - Pod security, network policies, secrets
3. **Monitor & Respond** - Runtime security, audit logs

---

## Template

```markdown
I need to secure my Kubernetes environment. Please provide comprehensive K8s security implementation guidance.

## CLUSTER CONTEXT

### Cluster Information
- K8s distribution: [EKS_GKE_AKS_SELF_MANAGED_OPENSHIFT]
- Version: [VERSION]
- Node count: [NUMBER]
- Namespaces: [NUMBER_AND_PURPOSE]
- Workload types: [STATELESS_STATEFUL_BATCH_DAEMON_SETS]
- Ingress: [NGINX_TRAEFIK_ISTIO_AWS_ALB]

## SECURITY AREAS

### 1. Control Plane Security
- API server authentication and authorization
- etcd encryption at rest
- Audit logging configuration
- API server admission controllers
- Control plane network isolation

### 2. RBAC (Role-Based Access Control)
- Service account management
- Role and ClusterRole design
- RoleBinding least privilege
- Pod service account binding
- External user authentication

### 3. Network Security
- Network policies (ingress/egress)
- Service mesh security (mTLS)
- Ingress controller security
- Network segmentation
- DNS security

### 4. Pod Security
- Pod Security Standards (Baseline, Restricted)
- Security contexts (runAsNonRoot, readOnlyRootFilesystem)
- Resource limits
- Privileged containers restriction
- Host namespace isolation

### 5. Image Security
- Image scanning for vulnerabilities
- Private registry security
- Image signing and verification
- Base image hardening
- Distroless containers

### 6. Secrets Management
- External secrets (Vault, AWS Secrets Manager)
- Encryption at rest
- Secrets rotation
- RBAC for secret access
- Avoiding secrets in environment variables

### 7. Runtime Security
- Runtime threat detection (Falco, Sysdig)
- Behavioral monitoring
- Anomaly detection
- Incident response
- Forensics and investigation

### 8. Supply Chain Security
- Admission controllers (OPA, Kyverno)
- Pod Security admission
- Image policy enforcement
- SBOM generation
- Dependency scanning

### 9. Monitoring & Logging
- Audit log collection
- Security event monitoring
- SIEM integration
- Metrics and alerting
- Compliance reporting

## CIS KUBERNETES BENCHMARK

Implement CIS recommendations:
- Control Plane (Master) hardening
- etcd hardening
- Control Plane Configuration
- Worker Node hardening
- Policies (Pod Security, Network, RBAC)

## OUTPUT REQUIREMENTS

Provide:
1. Cluster hardening checklist
2. RBAC policy examples
3. Network policy manifests
4. Pod security policy/standards
5. Admission controller policies
6. Monitoring and alerting setup
7. Incident response procedures
```

## Variables

### K8S_DISTRIBUTION
The Kubernetes distribution or managed service being used.
- Examples: "Amazon EKS 1.28", "Google GKE Autopilot", "Azure AKS", "OpenShift 4.14", "Rancher RKE2", "Self-managed kubeadm"

### WORKLOAD_TYPES
Types of Kubernetes workloads running in the cluster.
- Examples: "Stateless microservices (Deployments)", "Stateful databases (StatefulSets)", "Batch processing (Jobs/CronJobs)", "System daemons (DaemonSets)"

### INGRESS_CONTROLLER
The ingress solution handling external traffic.
- Examples: "NGINX Ingress Controller", "Istio Gateway", "AWS ALB Ingress", "Traefik", "Kong", "HAProxy"

### SECRETS_BACKEND
External secrets management solution.
- Examples: "HashiCorp Vault", "AWS Secrets Manager", "Azure Key Vault", "GCP Secret Manager", "Kubernetes native secrets with encryption"

### RUNTIME_SECURITY_TOOL
Runtime threat detection and monitoring solution.
- Examples: "Falco", "Sysdig Secure", "Aqua Security", "Prisma Cloud", "StackRox"

### ADMISSION_CONTROLLER
Policy enforcement admission controller.
- Examples: "OPA Gatekeeper", "Kyverno", "Pod Security Admission", "Datree", "Kubewarden"

---

## Usage Examples

### Example 1: Financial Services EKS Cluster
```
K8S_DISTRIBUTION: Amazon EKS 1.28
WORKLOAD_TYPES: 150 stateless microservices, 10 StatefulSets for databases
INGRESS_CONTROLLER: AWS ALB Ingress with WAF integration
SECRETS_BACKEND: HashiCorp Vault with Kubernetes auth
RUNTIME_SECURITY_TOOL: Falco with CloudWatch integration
ADMISSION_CONTROLLER: OPA Gatekeeper

Key Security Implementations:
- RBAC: Namespace-scoped roles for 5 development teams
- Network Policies: Default deny with explicit allow lists
- Pod Security: Restricted standard for all namespaces
- Image Security: ECR scanning + Trivy in CI/CD
- Audit Logging: API server logs to S3 for 7-year retention
- Compliance: PCI-DSS controls mapped to CIS benchmarks
```

### Example 2: Healthcare GKE Cluster
```
K8S_DISTRIBUTION: Google GKE 1.27 with Workload Identity
WORKLOAD_TYPES: HIPAA-compliant patient data processing
INGRESS_CONTROLLER: Istio service mesh with mTLS
SECRETS_BACKEND: GCP Secret Manager with Workload Identity
RUNTIME_SECURITY_TOOL: Sysdig Secure
ADMISSION_CONTROLLER: Kyverno for policy enforcement

Key Security Implementations:
- Binary Authorization for image provenance
- VPC-native cluster with private nodes
- Shielded GKE nodes with Secure Boot
- Customer-managed encryption keys (CMEK)
- Anthos Config Management for GitOps security
- HIPAA audit logging to BigQuery
```

### Example 3: Multi-tenant SaaS Platform
```
K8S_DISTRIBUTION: Azure AKS with Azure AD integration
WORKLOAD_TYPES: Multi-tenant SaaS with 50 customer namespaces
INGRESS_CONTROLLER: NGINX with per-tenant TLS certificates
SECRETS_BACKEND: Azure Key Vault with CSI driver
RUNTIME_SECURITY_TOOL: Prisma Cloud
ADMISSION_CONTROLLER: Pod Security Admission + Kyverno

Key Security Implementations:
- Tenant isolation: Network policies + ResourceQuotas
- Azure AD Pod Identity for Azure resource access
- Hierarchical namespaces for tenant management
- OPA policies for tenant resource boundaries
- Azure Defender for Kubernetes
- Tenant-specific audit log filtering
```

---

## Best Practices

1. **Least privilege by default** - Start with deny-all network policies and minimal RBAC, then add permissions as needed
2. **Immutable infrastructure** - Use read-only root filesystems and avoid privileged containers
3. **Defense in depth** - Combine admission control, runtime security, and network policies
4. **Secrets rotation** - Automate credential rotation with external secrets operators
5. **Image provenance** - Verify image signatures and use admission controllers to enforce trusted registries
6. **Audit everything** - Enable API server audit logs and retain for compliance requirements
7. **Regular scanning** - Continuously scan running images for new CVEs, not just at build time
8. **Namespace isolation** - Use network policies to prevent cross-namespace communication by default
9. **Service account hygiene** - Disable automounting of service account tokens unless explicitly needed
10. **CIS benchmarking** - Run kube-bench regularly and remediate findings

## Common Pitfalls

❌ **Default service accounts** - Using default SA with excessive permissions
✅ Instead: Create dedicated service accounts with minimal RBAC

❌ **Privileged containers** - Running containers as root or with privileged: true
✅ Instead: Use Pod Security Standards (Restricted) and securityContext

❌ **No network policies** - All pods can communicate freely
✅ Instead: Implement default-deny policies with explicit allow rules

❌ **Secrets in ConfigMaps** - Storing sensitive data in plain ConfigMaps
✅ Instead: Use external secrets management with encryption at rest

❌ **Ignoring runtime threats** - No visibility into container behavior
✅ Instead: Deploy Falco or similar runtime security monitoring
