---
category: security
title: Kubernetes Security Framework
tags:
- security
- kubernetes-security
- container-security
- rbac
use_cases:
- Securing Kubernetes clusters implementing RBAC least-privilege, network policies deny-by-default, Pod Security Standards achieving CIS benchmark compliance
- Implementing container security with image scanning, admission controllers (OPA/Kyverno), runtime detection (Falco) for regulated industries (PCI-DSS, HIPAA)
- Multi-tenant Kubernetes security with namespace isolation, resource quotas, tenant-specific network policies for SaaS platforms
related_templates:
- security/Cloud-Security/cloud-security-architecture.md
- technology/DevOps-Cloud/container-orchestration.md
industries:
- technology
- financial-services
- healthcare
- government
type: framework
difficulty: intermediate
slug: kubernetes-security
---

# Kubernetes Security Framework

## Purpose
Secure Kubernetes clusters covering control plane hardening, RBAC, network policies, Pod Security Standards, secrets management, admission control, runtime security, and compliance achieving defense-in-depth for containerized workloads.

## Template

Secure Kubernetes cluster {K8S_DISTRIBUTION} running {WORKLOAD_COUNT} workloads achieving {COMPLIANCE_REQUIREMENTS} compliance with {SECURITY_POSTURE} stance.

**CONTROL PLANE SECURITY**

Harden Kubernetes control plane components. API server security: enable authentication (OIDC, client certificates, service account tokens), authorization via RBAC (disable ABAC, Node, AlwaysAllow), admission controllers (NodeRestriction, PodSecurity, ValidatingAdmissionWebhook, MutatingAdmissionWebhook), enable audit logging (comprehensive level capturing metadata and request/response bodies for sensitive operations), TLS encryption for all API communication. etcd security: encryption at rest for secrets (EncryptionConfiguration with KMS provider or aescbc), restrict etcd access to control plane only (firewall rules, network policies), enable etcd TLS peer and client authentication, regular etcd backups with encrypted storage.

Cloud-managed considerations: EKS (enable envelope encryption with AWS KMS, private endpoint for API server, EKS Pod Identity for workload IAM), GKE (enable Workload Identity, Binary Authorization, private cluster with authorized networks), AKS (enable Azure AD integration, managed identity for kubelet, private cluster). Audit logging: enable API server audit logs capturing all requests, retention per compliance (7 years for SOX, 6 years for HIPAA), ship to centralized SIEM (CloudWatch, Stackdriver, Azure Monitor), alert on sensitive operations (secrets access, RBAC changes, exec into pods).

**RBAC AND IDENTITY**

Implement least-privilege access control. Service account design: create dedicated service accounts per workload (not default), disable automountServiceAccountToken unless explicitly needed, bind minimal RBAC permissions (read ConfigMaps only, not cluster-admin). Role design: namespace-scoped Roles for application teams (not ClusterRoles), grant specific API resources and verbs (get pods, not * on *), use RoleBindings for team assignments, avoid ClusterRoleBindings except for cluster-wide services.

Cloud identity integration: EKS Pod Identity (AWS IAM roles for service accounts), GKE Workload Identity (Google Cloud service accounts), AKS Pod Identity (Azure managed identities). Human access: integrate with corporate identity (OIDC with Okta/Azure AD), group-based RBAC (map AD groups to Kubernetes groups), namespace admin roles for development teams (admin within namespace, view-only cluster-wide), require MFA for kubectl access. RBAC auditing: use rbac-tool or kubectl who-can to audit permissions, identify overly permissive bindings (cluster-admin to users, wildcard permissions), quarterly RBAC review and cleanup.

**NETWORK SECURITY**

Implement defense-in-depth network controls. Network policies: default deny all ingress and egress per namespace, explicit allow policies for required communication (frontend → backend, backend → database), label-based selectors for policy application, test policies in staging before production. Policy examples: deny-all baseline (empty podSelector, no ingress/egress), allow DNS (egress to kube-dns on port 53), allow within namespace (podSelector matches namespace label), allow specific cross-namespace (namespaceSelector for shared services).

Service mesh security: Istio/Linkerd for automatic mTLS between services (eliminates plaintext pod-to-pod), authorization policies (L7 policy based on service identity), traffic encryption without application changes. Ingress security: TLS termination with valid certificates (cert-manager for automation), WAF integration (AWS WAF with ALB, ModSecurity with NGINX), rate limiting and DDoS protection, authentication at ingress (OAuth2 proxy, Istio RequestAuthentication). Network segmentation: separate node pools for sensitive workloads (PCI, PHI), VPC/subnet isolation for clusters, private clusters (no public API server endpoint).

**POD SECURITY**

Enforce secure pod configurations. Pod Security Standards: enforce Restricted profile for production namespaces (no privileged, no hostPath, runAsNonRoot, drop ALL capabilities), Baseline for development namespaces (allows some privilege with review), Privileged only for system namespaces (kube-system, monitoring). Security context settings: runAsNonRoot:true, runAsUser >1000, readOnlyRootFilesystem:true (with emptyDir for /tmp), allowPrivilegeEscalation:false, drop all capabilities then add only required (NET_BIND_SERVICE for port 80).

Resource limits: memory/CPU limits prevent DoS, requests for bin packing, LimitRanges for namespace defaults, ResourceQuotas for team boundaries. Host isolation: disallow hostNetwork, hostPID, hostIPC (breaks container isolation), disallow hostPath volumes (except for CSI drivers, monitoring), AppArmor/SELinux profiles for mandatory access control. Pod Security Admission: configure per-namespace labels (pod-security.kubernetes.io/enforce: restricted), warning mode before enforcing for testing, exemptions for specific system pods.

**IMAGE SECURITY**

Secure container supply chain. Image scanning: scan in CI/CD pipeline (Trivy, Snyk, Aqua), block critical vulnerabilities from deployment, continuous scanning of running images (new CVEs discovered daily), policy-based exceptions for accepted risk. Base image hardening: use minimal base images (distroless, alpine, scratch), avoid latest tags (use SHA256 digests), private registries (ECR, GCR, ACR, Harbor), vulnerability scanning on registry (ECR/GCR native, Harbor with Trivy).

Image signing and verification: sign images with Cosign/Notary, admission controller verifies signatures (Kyverno, OPA Gatekeeper), Binary Authorization (GKE) or Image Trust (Docker), cryptographic verification before pod starts. SBOM (Software Bill of Materials): generate SBOM during build (Syft, Trivy), store SBOM with image, audit dependencies for known vulnerabilities, compliance evidence (Executive Order 14028). Admission policies: only allow images from approved registries, require image scanning results attached, enforce signature verification, block privileged images.

**SECRETS MANAGEMENT**

Secure sensitive data handling. External secrets: HashiCorp Vault (Vault Agent injector, CSI driver), cloud-native (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager), External Secrets Operator (syncs external secrets to K8s), avoid native K8s secrets in Git (encrypted at rest but plaintext in etcd). Secrets encryption: enable EncryptionConfiguration with KMS provider (AWS KMS, GCP Cloud KMS, Azure Key Vault), rotate encryption keys regularly, verify encryption with etcdctl read.

Secrets rotation: automate rotation with external secrets operator, workload restart on secret update, credential lifetime limits (short-lived tokens preferred). Access control: RBAC restricts secret access (deny by default), service accounts with minimal secret permissions, audit secret access in API logs. Best practices: never commit secrets to Git (use .gitignore, pre-commit hooks), never log secrets (sanitize logs), never expose in environment variables (mount as files instead), use init containers for secret retrieval.

**ADMISSION CONTROL**

Enforce policies before pod admission. Admission controllers: OPA Gatekeeper (Rego policies, audit mode, template library), Kyverno (Kubernetes-native YAML policies, validate/mutate/generate), Pod Security Admission (built-in, replaces PodSecurityPolicy). Policy examples: require resource limits/requests, enforce label standards (app, owner, environment), disallow latest image tags, require readOnlyRootFilesystem, block privileged containers, enforce image signature verification.

Policy enforcement: audit mode first (report violations without blocking), warning mode (allow but notify), enforce mode (reject non-compliant pods), exemptions for system namespaces, policy versioning in Git. Validation vs mutation: validation rejects non-compliant manifests, mutation automatically fixes (add labels, inject sidecars, set defaults), prefer validation for security (explicit over implicit). Policy testing: unit test policies (Conftest for OPA, Kyverno CLI), integration tests in staging, progressive rollout (audit → warn → enforce).

**RUNTIME SECURITY**

Detect threats in running containers. Runtime detection: Falco (kernel-level syscall monitoring, ruleset for suspicious activity), Sysdig Secure (Falco + commercial features), Aqua/Prisma Cloud (commercial solutions). Falco rules: detect shell spawned in container, suspicious network activity, privilege escalation attempts, file access violations, crypto mining indicators. Alert integration: Falco → SIEM (Splunk, Sentinel), webhook to Slack/PagerDuty, SOAR for automated response (kill pod, isolate node).

Behavioral monitoring: baseline normal container behavior (typical processes, network connections), alert on deviations (new process, unexpected outbound connection), machine learning for anomaly detection. Incident response: automated pod termination on critical threats, node isolation (cordon, drain), forensics (capture pod logs, memory dump, network traffic), post-incident analysis. Audit and compliance: runtime security evidence for compliance (SOC 2, PCI), regular reviews of security events, tune false positives.

**MONITORING AND COMPLIANCE**

Track security posture and compliance. Security monitoring: API audit logs (sensitive operations, failed auth, RBAC changes), admission controller audit (policy violations, approved exceptions), runtime security alerts (Falco events), vulnerability scan results, network policy violations. Metrics: pod security standard compliance %, RBAC permissions creep, vulnerabilities per severity, time to patch critical CVEs, admission policy violations.

CIS Kubernetes Benchmark: run kube-bench regularly (monthly), remediate failed checks, document accepted risks for impractical controls, track compliance score over time. Compliance frameworks: PCI-DSS (network segmentation, encryption, access logs), HIPAA (encryption, audit logs, access controls), SOC 2 (change management, monitoring, access reviews). Dashboards: security posture overview, vulnerability trends, policy compliance, audit log highlights. Reporting: executive security summary, compliance evidence for auditors, security metrics trending.

Deliver Kubernetes security implementation as:

1. **CLUSTER HARDENING** - Control plane configuration, etcd encryption, audit logging, cloud-specific hardening

2. **RBAC POLICIES** - Service accounts, Roles/ClusterRoles, RoleBindings, cloud identity integration

3. **NETWORK POLICIES** - Default deny baselines, namespace isolation, ingress/egress rules, service mesh configuration

4. **POD SECURITY** - Pod Security Standards, security contexts, resource limits, admission policies

5. **IMAGE SECURITY** - Scanning pipeline, admission policies, signing/verification, SBOM generation

6. **SECRETS MANAGEMENT** - External secrets configuration, encryption at rest, rotation automation

7. **ADMISSION CONTROL** - OPA/Kyverno policies, enforcement strategy, testing procedures

8. **RUNTIME SECURITY** - Falco rules, alert integration, incident response playbooks

9. **MONITORING SETUP** - Security dashboards, CIS benchmark tracking, compliance reporting

---

## Usage Examples

### Example 1: Financial Services EKS Cluster
**Prompt:** Secure Amazon EKS 1.28 cluster with 150 microservices, 10 StatefulSets achieving PCI-DSS compliance with CIS benchmark hardening.

**Expected Output:** Control plane: EKS with envelope encryption (AWS KMS), private API endpoint, CloudWatch audit logs (7-year retention for SOC/PCI). RBAC: 5 namespace-scoped Roles for development teams (dev-team-1 → namespace:payments, dev-team-2 → namespace:orders), EKS Pod Identity for AWS IAM (pods assume IAM roles for S3, DynamoDB access), human access via OIDC with Okta (MFA required). Network: Calico network policies with default deny, frontend → backend (port 8080), backend → RDS (port 5432), all pods → kube-dns (port 53), AWS VPC CNI for pod networking. Pod security: Restricted standard for production namespaces (runAsNonRoot, readOnlyRootFilesystem, drop ALL capabilities), LimitRanges (default 100Mi memory, 100m CPU), ResourceQuotas per team. Image security: ECR with scan-on-push, Trivy in CI/CD (fail on critical CVEs), OPA Gatekeeper policies (only ECR images, require scan results, no latest tags). Secrets: Vault with Kubernetes auth (Vault Agent injector for sidecar), secrets mounted as files, 30-day credential rotation. Admission: OPA Gatekeeper with policies (require labels, resource limits, pod security restricted, signed images), audit mode first (2 weeks) then enforce. Runtime: Falco with CloudWatch Events integration, rules (shell in container, privilege escalation, sensitive file access), alerts → SNS → PagerDuty. Monitoring: kube-bench weekly (CIS compliance 92%), audit logs → S3 → Splunk, security dashboard (vulnerability count, pod security violations, Falco alerts). Cost: EKS ($0.10/hour cluster), Vault ($400/month), Falco (open-source), OPA (open-source).

### Example 2: Healthcare GKE Cluster
**Prompt:** Secure Google GKE 1.27 cluster for HIPAA-compliant patient data processing with Binary Authorization and Workload Identity.

**Expected Output:** Control plane: GKE Autopilot (Google-managed hardening), private cluster (no public IPs), Workload Identity enabled, customer-managed encryption keys (CMEK) for etcd, Cloud Audit Logs (10-year retention for HIPAA). RBAC: Workload Identity binding (K8s SA → Google Cloud SA), namespace isolation for PHI workloads, least-privilege cloud IAM roles (storage.objectViewer, not storage.admin). Network: VPC-native cluster, Istio service mesh with mTLS (automatic encryption), AuthorizationPolicies (L7 access control), GKE Dataplane V2 (eBPF networking), Cloud Armor (DDoS protection). Pod security: GKE Pod Security Standards enforced (Restricted for PHI namespaces), Shielded GKE Nodes (Secure Boot, vTPM, integrity monitoring), no hostPath mounts. Image security: Artifact Registry with vulnerability scanning, Binary Authorization (only signed images from approved Artifact Registry), Kritis Signer for attestation, SLSA provenance. Secrets: GCP Secret Manager with Workload Identity (no static keys), Secrets Store CSI Driver mounts secrets as volumes, automatic rotation (30 days). Admission: Kyverno for policy enforcement (require encryption labels, disallow latest tags, enforce resource limits), Binary Authorization for provenance verification. Runtime: Sysdig Secure (Falco + managed service), GKE Security Posture dashboard, runtime threat detection with ML. Monitoring: Cloud Operations for Kubernetes (audit logs, security insights), GKE Security Posture API, compliance reports for HIPAA audit. Compliance: HIPAA technical safeguards (encryption at rest/in transit, access controls, audit logs), BAA with Google Cloud, HITRUST certification alignment.

### Example 3: Multi-Tenant SaaS on AKS
**Prompt:** Secure Azure AKS cluster for multi-tenant SaaS with 50 customer namespaces requiring tenant isolation and Azure AD integration.

**Expected Output:** Control plane: AKS with Azure AD integration (RBAC assignments via AD groups), private cluster, Azure Key Vault encryption for etcd, Azure Policy for Kubernetes (governance at scale). RBAC: tenant-specific namespaces (tenant-acme, tenant-contoso), namespace admin roles for customers (admin within tenant namespace only), Azure AD Pod Identity (deprecated) → Workload Identity Federation (pods access Azure resources with federated identity). Network: Azure CNI for pod networking, Calico for network policies, deny-all baseline + tenant isolation (no cross-namespace traffic), Azure Firewall for egress filtering, per-tenant ingress with SNI routing. Pod security: Pod Security Admission (Restricted for tenant namespaces, exemptions for monitoring), hierarchical namespaces for tenant sub-namespaces, ResourceQuotas per tenant (prevent noisy neighbor), LimitRanges for defaults. Image security: Azure Container Registry with Defender for Containers (vulnerability scanning), admission webhook blocks unscanned images, Azure Policy requiring ACR images only. Secrets: Azure Key Vault with CSI driver (akv2k8s), per-tenant Key Vault instances (tenant isolation), Workload Identity for secret access, automatic rotation. Admission: Kyverno + Pod Security Admission (dual enforcement), policies (tenant resource quotas, require cost center labels, disallow privileged), tenant-specific policy exceptions. Runtime: Prisma Cloud (commercial), tenant activity monitoring, anomaly detection per tenant, isolation breach detection. Monitoring: Azure Monitor for containers, per-tenant cost allocation, security dashboards (tenant violations, vulnerabilities), Azure Defender for Kubernetes alerts. Tenant isolation: network policies (pod-to-pod blocked across tenants), separate node pools for premium tiers, RBAC prevents cross-tenant access, audit logs per tenant for SOC 2.

---

## Cross-References

- [Cloud Security Architecture](cloud-security-architecture.md) - Broader cloud security context
- [Container Orchestration](../../technology/DevOps-Cloud/container-orchestration.md) - Kubernetes deployment patterns
- [Zero Trust Architecture](../Identity-Access-Management/zero-trust-architecture.md) - Zero trust principles for containers
