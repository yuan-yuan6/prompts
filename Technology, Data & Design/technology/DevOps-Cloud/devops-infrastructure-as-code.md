---
category: technology
related_templates:
- technology/DevOps-Cloud/cloud-architecture.md
- technology/DevOps-Cloud/ci-cd-pipelines.md
- technology/DevOps-Cloud/container-orchestration.md
tags:
- devops
- infrastructure-as-code
- terraform
- cloud-provisioning
title: Infrastructure as Code (IaC)
use_cases:
- Designing modular Terraform/Pulumi infrastructure for multi-environment deployments with remote state, locking, and CI/CD integration
- Implementing policy-as-code with OPA/Sentinel enforcing security baselines, cost controls, and compliance requirements
- Building reusable infrastructure modules with testing, versioning, and private registry distribution for platform teams
industries:
- technology
- financial-services
- healthcare
- government
type: framework
difficulty: intermediate
slug: devops-infrastructure-as-code
---

# Infrastructure as Code (IaC)

## Purpose
Design and implement infrastructure as code using Terraform, Pulumi, or CloudFormation covering module architecture, state management, CI/CD integration, security scanning, and policy enforcement achieving reproducible, auditable infrastructure deployments across environments.

## Template

Create infrastructure as code for {CLOUD_PROVIDER} using {IAC_TOOL} managing {INFRASTRUCTURE_SCOPE} across {ENVIRONMENTS} with {STATE_BACKEND} backend and {CICD_PLATFORM} integration.

**TOOL SELECTION AND ARCHITECTURE**

Choose IaC tool matching team expertise and requirements. Terraform: industry standard, provider ecosystem (3000+ providers), HCL declarative syntax, state management requires planning. Pulumi: general-purpose languages (TypeScript, Python, Go), familiar programming paradigms, better for complex logic. AWS CDK/CDKTF: TypeScript/Python generating CloudFormation/Terraform, type safety, IDE support. CloudFormation: AWS-native, deep integration, no state management (AWS manages), slower iteration.

Design repository structure for maintainability. Monorepo: single repository with environment directories, easier cross-cutting changes, atomic updates across modules. Multi-repo: separate repositories per module/component, clearer ownership, independent versioning. Hybrid: shared modules repo + environment-specific repos referencing modules. Directory structure: environments/ (dev/staging/prod), modules/ (reusable components), shared/ (providers, backend config), docs/ (architecture, runbooks).

Organize modules for reusability and composition. Module granularity: one module per logical component (VPC, EKS cluster, RDS instance), avoid monolithic modules. Input variables: required (no default), optional (sensible defaults), validated (type constraints, custom validation rules). Outputs: expose all IDs, ARNs, endpoints needed by dependent modules. Documentation: README.md with usage examples, terraform-docs for auto-generated variable/output documentation.

**STATE MANAGEMENT**

Configure remote state for team collaboration. S3 backend (AWS): bucket with versioning enabled, server-side encryption (SSE-S3 or KMS), DynamoDB table for state locking. Azure Storage: storage account with blob container, SAS token or managed identity authentication. GCS: bucket with versioning, object lock for compliance, IAM for access control. Terraform Cloud: managed state with built-in locking, run history, cost estimation.

Implement state locking preventing concurrent modifications. DynamoDB locking (AWS): single table for all states, partition key = LockID, auto-created by Terraform. Consul locking: distributed locking for on-premises or multi-cloud. Terraform Cloud: automatic locking with run queue. Lock timeout: 5-10 minutes default, increase for large infrastructures.

Structure state files for operational efficiency. State per environment: separate state files for dev/staging/prod, independent deployments, blast radius isolation. State per component: networking, compute, data separated, independent lifecycle management. State naming: {project}-{environment}-{component}.tfstate for clarity. State migration: terraform state mv for refactoring, careful planning required, test in non-production first.

**MODULE DEVELOPMENT**

Create reusable modules with consistent patterns. Module interface: clear inputs with descriptions and validation, comprehensive outputs, no hardcoded values. Resource naming: include environment, region, component in names ({env}-{region}-{component}-{resource}). Tagging: mandatory tags (Environment, Owner, CostCenter, Application) passed through variables. Dependencies: explicit depends_on only when necessary, prefer implicit through resource references.

Implement module versioning and distribution. Semantic versioning: major.minor.patch (1.0.0), major for breaking changes, minor for features, patch for fixes. Version constraints: ~> 1.0 allows 1.x but not 2.0, exact version for production stability. Distribution: Terraform Registry (public), private registry (Terraform Cloud, Artifactory, S3), Git tags. Changelog: maintain CHANGELOG.md documenting all changes, breaking changes highlighted.

Test modules before release. Unit testing: Terratest (Go), pytest-terraform (Python), validate module logic. Integration testing: deploy to test environment, verify resources created correctly, destroy after test. Policy testing: Conftest for OPA policies, ensure module output complies with standards. Pre-commit hooks: terraform fmt, terraform validate, tflint, documentation generation.

**CI/CD INTEGRATION**

Design pipeline for safe infrastructure changes. Plan on PR: terraform plan output as PR comment, reviewers see exact changes before approval. Apply on merge: terraform apply after PR merge to protected branch, automated deployment. Environment promotion: dev (auto-apply) → staging (auto-apply after dev success) → prod (manual approval). Separate pipelines: network changes require additional approval, database changes have extended review.

Configure pipeline security and controls. Credentials: OIDC federation (GitHub Actions → AWS IAM), no long-lived credentials in CI. Least privilege: CI role can only modify resources in target environment, read-only for plan. Approval gates: required reviewers for production, change advisory board for critical infrastructure. Audit trail: all applies logged with user, timestamp, plan output, commit hash.

Implement automated validation in pipeline. Syntax validation: terraform validate, terraform fmt --check (fail if unformatted). Security scanning: tfsec/checkov/Snyk IaC (block on critical/high findings). Cost estimation: Infracost PR comments showing cost impact of changes. Policy check: OPA/Sentinel policies (resource limits, required tags, approved regions). Plan review: automated checks for destructive changes (resource deletion warnings).

**SECURITY AND COMPLIANCE**

Implement security scanning in development workflow. Pre-commit: tfsec/checkov local scanning before commit, fast feedback. CI pipeline: full security scan with all rules, block PR on critical findings. Tools comparison: tfsec (Terraform-specific, fast), Checkov (multi-framework, comprehensive), Snyk IaC (vulnerability database, fix suggestions). Custom rules: organization-specific policies (approved instance types, required encryption).

Configure policy-as-code enforcement. OPA/Conftest: Rego policies evaluated against Terraform plan JSON, flexible and powerful. Sentinel (Terraform Cloud/Enterprise): native integration, policy sets per workspace, soft/hard mandatory. AWS SCP: preventive controls at organization level, complement IaC policies. Azure Policy: built-in compliance, audit or deny non-compliant resources. Policy examples: no public S3 buckets, encryption required on all storage, approved regions only.

Manage secrets securely in IaC. Never in code: no secrets in .tf files, variables, or tfvars committed to Git. Secret injection: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault accessed at apply time. Sensitive variables: mark sensitive = true, redacted in logs and plan output. State security: state files contain secrets, encrypt backend, restrict access to state bucket.

**ENVIRONMENT MANAGEMENT**

Structure environments for consistency and isolation. Workspace-based: terraform workspace for environment switching, single codebase, variable files per environment. Directory-based: separate directories per environment, explicit isolation, some duplication. Terragrunt: DRY configuration across environments, dependency management, generate blocks. Variable hierarchy: defaults → environment-specific → deployment-specific overrides.

Implement environment promotion patterns. Infrastructure version: tag infrastructure releases (infra-v1.2.3), promote same version through environments. Configuration parity: same module versions dev/staging/prod, only size/count parameters differ. Blue-green infrastructure: parallel environments for zero-downtime infrastructure changes. Drift detection: scheduled terraform plan comparing actual vs desired state, alert on drift.

Manage environment-specific configuration. Variable files: terraform.tfvars per environment, checked into repository. Parameter stores: AWS SSM Parameter Store, Azure App Configuration for dynamic values. Environment detection: workspace name or variable for conditional logic (count = var.environment == "prod" ? 3 : 1). Resource sizing: variable maps for instance types, replica counts, storage sizes per environment.

**OPERATIONAL PRACTICES**

Implement GitOps workflow for infrastructure. Pull request workflow: all changes via PR, no direct applies, code review required. Atlantis/Terraform Cloud: automated plan on PR, apply via PR comment or merge. ArgoCD for Kubernetes: GitOps for Kubernetes resources, sync from Git repository. Drift reconciliation: periodic terraform apply to correct manual changes, or alert for investigation.

Document infrastructure comprehensively. Architecture diagrams: C4 model or similar, show relationships between components. Module documentation: terraform-docs generates variable/output tables automatically. Runbooks: common operations (scaling, failover, recovery), step-by-step procedures. Decision records: ADRs for significant choices (why Terraform over Pulumi, why this state structure).

Monitor and maintain infrastructure code. Technical debt tracking: track TODOs, deprecated resources, upgrade needs. Dependency updates: Dependabot/Renovate for provider and module version updates. Provider upgrades: test in dev first, review changelog for breaking changes, staged rollout. Terraform upgrades: test new Terraform versions in CI, upgrade state format carefully.

Deliver infrastructure as code as:

1. **REPOSITORY STRUCTURE** - Directory layout, module organization, environment separation, naming conventions

2. **MODULE LIBRARY** - Reusable modules with inputs, outputs, documentation, versioning strategy

3. **STATE CONFIGURATION** - Backend setup, locking mechanism, state file organization, access controls

4. **CI/CD PIPELINE** - Plan/apply workflow, approval gates, security scanning, cost estimation

5. **SECURITY CONTROLS** - Policy-as-code, security scanning, secret management, compliance checks

6. **OPERATIONAL DOCS** - Runbooks, architecture diagrams, ADRs, troubleshooting guides

---

## Usage Examples

### Example 1: Multi-Environment AWS Platform
**Prompt:** Create IaC for AWS using Terraform managing VPC, EKS, RDS, and S3 across dev/staging/prod in us-east-1 and eu-west-1 with S3+DynamoDB state and GitHub Actions CI/CD.

**Expected Output:** Repository structure: monorepo with environments/{dev,staging,prod}/{us-east-1,eu-west-1}/, modules/{vpc,eks,rds,s3}/. Modules: VPC (3 AZs, public/private/data subnets, NAT Gateway), EKS (managed node groups, IRSA, cluster autoscaler), RDS (Aurora PostgreSQL, Multi-AZ, automated backups), S3 (encryption, versioning, lifecycle policies). State: s3://{org}-terraform-state/{env}/{region}/terraform.tfstate, DynamoDB terraform-locks table. CI/CD: GitHub Actions with OIDC to AWS, plan on PR with Atlantis-style comments, apply on merge to main, environment-specific branch protection. Security: tfsec + Checkov in CI, Infracost for cost estimation, OPA policies (no public subnets without justification, encryption required). Environment sizing: dev (t3.medium nodes, db.t3.medium), staging (t3.large, db.r5.large), prod (m5.xlarge, db.r5.xlarge with read replica). Cost: dev ~$800/month, staging ~$2,500/month, prod ~$8,000/month per region.

### Example 2: Azure Landing Zone with Governance
**Prompt:** Create IaC for Azure using Terraform implementing CAF landing zone with management groups, policy assignments, and hub-spoke networking for enterprise with SOC2 compliance.

**Expected Output:** Repository structure: azure-landing-zone/ with platform/ (management groups, policies, connectivity) and workloads/ (subscription vending). Module hierarchy: management-groups (org structure), policy-definitions (custom policies), policy-assignments (compliance enforcement), hub-network (firewall, VPN gateway, Bastion), spoke-network (peered VNets). State: Azure Storage account with private endpoint, managed identity authentication, container per environment. Governance: Azure Policy for SOC2 (required encryption, logging, network controls), deny public IPs, audit NSG rules. Hub-spoke: central hub with Azure Firewall, spoke VNets peered to hub, UDR forcing traffic through firewall. Identity: Azure AD integration, Privileged Identity Management for JIT access, service principals with federated credentials. CI/CD: Azure DevOps pipelines, plan on PR, apply with approval gate, policy compliance check before apply. Cost: hub ~$3,000/month (firewall dominant), spoke ~$500/month base plus workload costs.

### Example 3: Multi-Cloud Kubernetes Platform
**Prompt:** Create IaC for multi-cloud (AWS EKS + GCP GKE) using Pulumi (TypeScript) with centralized state and GitOps deployment for disaster recovery architecture.

**Expected Output:** Repository structure: Pulumi project with stacks per environment per cloud (aws-prod, gcp-dr). Pulumi components: KubernetesCluster (abstraction over EKS/GKE), NetworkFoundation (VPC/VPC creation), DatabaseCluster (Aurora/Cloud SQL). State: Pulumi Cloud for state management, encrypted, team access controls. Cross-cloud: shared Kubernetes manifests deployed via Flux CD, DNS failover via Cloudflare. EKS configuration: managed node groups, Karpenter for scaling, ALB controller, external-dns. GKE configuration: Autopilot mode for DR (reduced management), Cloud NAT, GKE Ingress. GitOps: Flux CD on both clusters, single Git repo for Kubernetes manifests, automatic sync. DR strategy: active-passive, GKE cluster scaled down (1 node per pool), scale-up automation on failover. CI/CD: GitHub Actions, pulumi preview on PR, pulumi up with approval, drift detection cron job. Monitoring: Pulumi Cloud shows resource graph, CloudWatch/Cloud Monitoring for cloud-native metrics.

---

## Cross-References

- [Cloud Architecture](cloud-architecture.md) - Cloud infrastructure patterns implemented via IaC
- [CI/CD Pipelines](ci-cd-pipelines.md) - Pipeline integration for infrastructure deployment
- [Container Orchestration](container-orchestration.md) - Kubernetes clusters provisioned via IaC
