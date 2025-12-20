---
category: technology
related_templates:
- technology/DevOps-Cloud/cloud-architecture.md
- technology/DevOps-Cloud/ci-cd-pipelines.md
- technology/DevOps-Cloud/infrastructure-as-code.md
tags:
- kubernetes
- container-orchestration
- eks-gke-aks
- auto-scaling
title: Container Orchestration
use_cases:
- Designing Kubernetes architectures on EKS/GKE/AKS with node pools, auto-scaling, and multi-tenancy for microservices platforms serving 10K+ requests/second
- Implementing deployment strategies (rolling, blue-green, canary) with service mesh integration achieving zero-downtime releases and automated rollback
- Building stateful workloads with persistent storage, backup strategies, and disaster recovery achieving 99.99% data durability
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: container-orchestration
---

# Container Orchestration

## Purpose
Design and implement Kubernetes-based container orchestration covering cluster architecture, deployment patterns, auto-scaling, service mesh, stateful workloads, and observability achieving production-grade reliability with efficient resource utilization.

## 🚀 Quick Container Orchestration Prompt

> Deploy **[APPLICATION]** on **[EKS/GKE/AKS]** with **[REPLICAS]** replicas. Resources: CPU **[REQUEST/LIMIT]**, memory **[REQUEST/LIMIT]**. Scaling: HPA **[MIN]-[MAX]** pods at **[CPU_THRESHOLD]**% CPU. Storage: **[STORAGE_CLASS]** PVC for **[STATEFUL_DATA]**. Networking: **[INGRESS_TYPE]** with TLS, **[SERVICE_MESH]** for traffic management. Observability: Prometheus metrics, **[LOGGING_STACK]**. Deploy strategy: **[ROLLING/CANARY/BLUE_GREEN]**.

---

## Template

Design container orchestration for {APPLICATION_TYPE} on {KUBERNETES_PLATFORM} supporting {SCALE_REQUIREMENTS} with {AVAILABILITY_TARGET}% availability and {RESOURCE_EFFICIENCY}% resource utilization.

**CLUSTER ARCHITECTURE**

Design node pools matching workload characteristics. General-purpose pool: m5.2xlarge/n2-standard-8 for typical workloads (8 vCPU, 32GB RAM), auto-scale 3-20 nodes. Compute-intensive pool: c5.4xlarge/c2-standard-16 for CPU-bound services, taint for dedicated scheduling (workload-type=compute:NoSchedule). Memory-intensive pool: r5.2xlarge/n2-highmem-8 for caching and analytics, taint for dedicated scheduling. Spot/preemptible pool: 60-70% cost savings for fault-tolerant workloads (batch jobs, CI/CD, dev environments), handle interruptions gracefully with PodDisruptionBudgets.

Configure cluster auto-scaling for cost efficiency. Cluster Autoscaler: scale nodes based on pending pods, scale-down delay 10 minutes (avoid thrashing), respect PodDisruptionBudgets during scale-down. Node pool sizing: min 3 nodes per AZ for HA (survives node failure), max based on peak load + 50% headroom. Bin packing: configure pod requests accurately to maximize node utilization (target 70-80%), avoid over-provisioning that wastes resources.

Implement multi-tenancy for shared clusters. Namespace isolation: one namespace per team/application, ResourceQuotas limit CPU/memory/pods per namespace. Network policies: default deny ingress/egress, explicit allow rules between namespaces. RBAC: team-scoped roles (can manage own namespace), cluster-admin for platform team only. Cost allocation: labels for chargeback (team, cost-center), namespace-level resource tracking with Kubecost.

**DEPLOYMENT PATTERNS**

Configure Deployments for stateless workloads. Rolling updates: maxSurge 25% (handle traffic during rollout), maxUnavailable 0 (zero downtime), minReadySeconds 30 (ensure pod stability before continuing). Pod anti-affinity: spread pods across nodes/AZs for resilience (requiredDuringSchedulingIgnoredDuringExecution for critical services). Resource requests and limits: requests for scheduling (guarantee minimum), limits for protection (prevent noisy neighbor), ratio typically 1:2 for burstable workloads.

Implement progressive delivery with canary deployments. Argo Rollouts: define canary steps (5% → 25% → 50% → 100%), analysis template checks metrics between steps. Promotion criteria: error rate <0.5%, p99 latency within 10% of baseline, no new error types in logs. Analysis duration: 5-10 minutes per step (balance confidence vs deployment time). Automated rollback: revert to stable version if analysis fails, alert team on rollback. Flagger alternative: integrates with Istio/Linkerd, similar progressive delivery capabilities.

Configure health checks for reliable traffic routing. Liveness probe: restart pod if unhealthy (deadlock detection), exec/httpGet/tcpSocket, initialDelaySeconds sufficient for startup (30-60s for JVM), periodSeconds 10, failureThreshold 3. Readiness probe: remove from service if not ready (dependency issues), same methods, shorter initialDelaySeconds (5-10s), check downstream dependencies. Startup probe: for slow-starting containers, prevents liveness probe from killing during startup, failureThreshold × periodSeconds > max startup time.

**AUTO-SCALING STRATEGIES**

Configure Horizontal Pod Autoscaler for demand-based scaling. CPU-based: target 70% utilization, scales pods to maintain average across replicas. Memory-based: target 80% utilization, useful for memory-bound services. Custom metrics: requests-per-second from Prometheus, queue depth from CloudWatch/Stackdriver. Multi-metric: HPA uses highest recommendation, combine CPU + custom for comprehensive scaling. Scaling behavior: scaleUp stabilization 0s (respond quickly to load), scaleDown stabilization 300s (avoid thrashing), policies limit change rate (max 100% increase per 30s).

Implement Vertical Pod Autoscaler for right-sizing. Recommendation mode: VPA recommends optimal requests/limits without applying (safe for production). Auto mode: VPA evicts and recreates pods with new resources (use for non-critical or with PDB). Update policy: apply changes during pod restart (recreate), avoid for latency-sensitive services. Resource bounds: set minAllowed/maxAllowed to prevent extreme recommendations, monitor for under/over-provisioning.

Configure KEDA for event-driven scaling. Scale triggers: queue length (SQS, RabbitMQ, Kafka), HTTP requests (Prometheus metrics), cron (scheduled scaling). Scale to zero: cost savings for idle workloads, pollingInterval determines wake-up latency (30s default). Scaled objects: reference Deployment/StatefulSet, define triggers and scaling parameters. Use cases: batch processing, event consumers, scheduled jobs, bursty workloads.

**SERVICE MESH AND NETWORKING**

Implement service mesh for traffic management. Istio: full-featured (traffic management, security, observability), higher resource overhead (~1GB sidecar memory). Linkerd: lightweight (~50MB sidecar), easier operations, fewer features. Traffic splitting: route percentage of traffic to canary versions, header-based routing for testing. Retry policies: automatic retries on transient failures (503, connection reset), exponential backoff, retry budgets prevent cascade. Circuit breakers: eject unhealthy endpoints, outlier detection (5 consecutive 5xx → 30s ejection).

Configure Ingress for external traffic. NGINX Ingress: widely used, path-based routing, rate limiting, SSL termination. ALB Ingress (AWS): native integration, target type IP for direct pod routing, WAF integration. Annotations: rate limiting (nginx.ingress.kubernetes.io/rate-limit: "100"), TLS redirect, proxy timeouts. TLS: cert-manager for automatic Let's Encrypt certificates, cluster-issuer for production, wildcard certs for simplicity.

Implement Network Policies for security. Default deny: start with deny-all ingress/egress, whitelist required traffic. Namespace isolation: allow traffic within namespace, explicit rules for cross-namespace. Egress control: limit outbound to required services (database, cache, external APIs), allow kube-dns (UDP 53). Policy enforcement: Calico, Cilium, or cloud provider CNI with network policy support.

**STATEFUL WORKLOADS**

Configure StatefulSets for stateful applications. Ordered deployment: pods created sequentially (0, 1, 2), ensures leader election and replication setup. Stable network identity: pod-0.service-name, consistent DNS for database connections. Persistent storage: volumeClaimTemplates provision PVC per pod, survive pod restarts and rescheduling. Pod management policy: OrderedReady (default, sequential), Parallel (for stateless-like scaling).

Design storage for reliability and performance. StorageClass selection: gp3/pd-ssd for general purpose (3K baseline IOPS), io2/pd-extreme for high IOPS requirements. Volume expansion: enable allowVolumeExpansion for future growth, resize PVC without data migration. Backup strategy: Velero for cluster-wide backup (PVs, resources), CSI snapshots for point-in-time recovery. Multi-AZ: volumeBindingMode WaitForFirstConsumer ensures PV in same AZ as pod.

Implement operators for complex stateful workloads. Database operators: PostgreSQL (Zalando, CrunchyData), MySQL (Oracle, Percona), Redis (Redis Enterprise), handle replication, failover, backup automatically. Kafka operators: Strimzi manages brokers, topics, users, handles rolling upgrades. Benefits: encapsulate operational knowledge, consistent deployment, automated day-2 operations. Considerations: operator maturity varies, understand failure modes, maintain operator versions.

**OBSERVABILITY AND MONITORING**

Implement metrics collection with Prometheus stack. Prometheus: scrape metrics from pods/services, store time-series, alerting rules. Metrics exposure: application exposes /metrics endpoint, ServiceMonitor defines scrape config. Key metrics: request rate, error rate, latency percentiles (RED method), saturation (CPU, memory, disk). Grafana dashboards: pre-built for Kubernetes (node, pod, namespace), custom for applications.

Configure centralized logging. Fluentd/Fluent Bit: DaemonSet collects container logs, parse and forward to backend. Log backends: Elasticsearch (powerful search, higher cost), Loki (simpler, integrates with Grafana), CloudWatch Logs (managed, AWS-native). Structured logging: JSON format, consistent fields (trace_id, service, level), enables filtering and aggregation. Retention: 7 days hot storage for debugging, 30-90 days archive for compliance.

Implement distributed tracing. OpenTelemetry: vendor-neutral instrumentation, auto-instrumentation for common frameworks. Trace backends: Jaeger (open source), Tempo (Grafana), X-Ray (AWS), Datadog (managed). Trace propagation: W3C trace context headers, consistent trace IDs across service boundaries. Sampling: 1-10% for production (balance observability vs cost), 100% for errors and slow requests.

**SECURITY AND COMPLIANCE**

Implement Pod Security Standards. Restricted profile: no privilege escalation, non-root user, read-only root filesystem, drop all capabilities. Baseline profile: minimal restrictions, blocks known privilege escalations. Enforcement: PodSecurity admission controller (built-in), Kyverno/OPA Gatekeeper for custom policies. Security contexts: runAsNonRoot, readOnlyRootFilesystem, capabilities drop ALL.

Configure RBAC for least privilege access. Service accounts: one per application, avoid default service account, automountServiceAccountToken false unless needed. Roles: namespace-scoped for applications (pods, configmaps, secrets), ClusterRoles for cluster-wide (nodes, PVs). IAM integration: EKS IRSA, GKE Workload Identity, AKS Pod Identity—map service accounts to cloud IAM roles. Audit: enable Kubernetes audit logging, review RBAC periodically, remove unused bindings.

Secure secrets management. Kubernetes Secrets: base64 encoded (not encrypted by default), enable encryption at rest with KMS. External secrets: AWS Secrets Manager, HashiCorp Vault, sync to Kubernetes Secrets via External Secrets Operator. Secret rotation: automate rotation in source, sync updates to cluster, restart pods to pick up new secrets. Avoid: secrets in ConfigMaps, environment variables in pod spec (visible in logs), hardcoded in images.

Deliver container orchestration as:

1. **CLUSTER ARCHITECTURE** - Node pools, auto-scaling configuration, multi-tenancy design, cost optimization

2. **DEPLOYMENT MANIFESTS** - Deployments, StatefulSets, Services, ConfigMaps, Secrets with best practices

3. **SCALING CONFIGURATION** - HPA, VPA, KEDA, cluster autoscaler settings and thresholds

4. **NETWORKING SETUP** - Ingress, Network Policies, Service Mesh configuration, TLS certificates

5. **STORAGE DESIGN** - StorageClasses, PVCs, backup procedures, operator selection for stateful workloads

6. **OBSERVABILITY STACK** - Prometheus, Grafana, logging, tracing configuration and dashboards

7. **SECURITY CONTROLS** - RBAC, Pod Security, secrets management, network policies

---

## Usage Examples

### Example 1: E-commerce Microservices Platform
**Prompt:** Design container orchestration for EcommercePlatform (25 microservices) on EKS supporting 10K requests/second with 99.95% availability and 75% resource utilization.

**Expected Output:** Cluster architecture: 3 node pools (general m5.2xlarge 5-30 nodes, compute c5.2xlarge 3-10 nodes, spot m5.xlarge for batch jobs), multi-AZ (3 AZs), cluster autoscaler with 10-minute scale-down delay. Deployment patterns: rolling updates (maxSurge 25%, maxUnavailable 0), Argo Rollouts for customer-facing services (5%→25%→100% canary over 30 minutes), PodDisruptionBudgets (minAvailable 2 for critical services). Scaling: HPA on CPU (70%) and requests-per-second (target 1000/pod), min 3 max 50 pods per service, KEDA for order processing queue (scale 1 pod per 100 messages). Networking: AWS ALB Ingress with WAF, Istio service mesh (traffic splitting, circuit breakers, mTLS), Network Policies isolating namespaces. Observability: Prometheus + Grafana (RED dashboards), Fluent Bit → Elasticsearch (7-day retention), Jaeger tracing (10% sampling). Cost: ~$15K/month (60% spot instances for non-critical), Kubecost for per-team allocation.

### Example 2: Healthcare Data Processing Pipeline
**Prompt:** Design container orchestration for HealthDataPipeline on GKE processing 5TB daily with HIPAA compliance, StatefulSet databases, and 99.99% data durability.

**Expected Output:** Cluster architecture: private GKE cluster (no public endpoints), node pools with confidential computing (N2D) for PHI processing, dedicated pool for PostgreSQL StatefulSets. Stateful workloads: PostgreSQL via CrunchyData operator (3-node HA, automatic failover, continuous backup to GCS), Redis Cluster via Redis operator, Kafka via Strimzi (3 brokers, 3 ZooKeeper). Storage: pd-ssd StorageClass with encryption, Velero daily backups (30-day retention), cross-region backup replication. Security: Pod Security restricted profile, Workload Identity for GCP service account mapping, all secrets in Secret Manager synced via External Secrets, network policies (deny all default, explicit allow). Processing: Apache Spark on Kubernetes (spark-operator), KEDA scaling based on pending jobs, preemptible nodes for batch processing. Compliance: VPC Service Controls, audit logging to BigQuery, encryption in transit (Istio mTLS) and at rest (CMEK). Observability: GKE-native monitoring, custom dashboards for data pipeline metrics, alerting on processing delays.

### Example 3: Global SaaS Multi-Region Deployment
**Prompt:** Design container orchestration for GlobalSaaS on AKS deployed across 3 regions (US, EU, APAC) with <100ms latency per region and unified GitOps deployment.

**Expected Output:** Cluster architecture: 3 AKS clusters (eastus, westeurope, southeastasia), Azure CNI with Calico network policies, node pools sized for regional traffic patterns. Multi-cluster management: Azure Arc for unified control plane, Flux CD for GitOps (one repo, environment overlays per region). Traffic routing: Azure Front Door for global load balancing, health probes per region, automatic failover on regional outage. Deployment strategy: sequential regional rollout (APAC → EU → US following sun), Flagger canary per region with regional metrics analysis. Service mesh: Linkerd (lightweight, <100MB per sidecar), cross-cluster service discovery via Linkerd multicluster. Data layer: Cosmos DB multi-region (automatic failover), Redis Enterprise geo-replication for session cache. Observability: Azure Monitor Container Insights, centralized Grafana with multi-cluster views, PagerDuty integration for regional alerts. Networking: ExpressRoute to on-premises per region, Private Link for Azure services, regional Ingress with Azure Application Gateway. Cost optimization: reserved instances for baseline (US cluster), spot VMs for EU/APAC variable capacity, ~$25K/month total.

---

## Cross-References

- [Cloud Architecture](cloud-architecture.md) - Cloud infrastructure supporting Kubernetes clusters
- [CI/CD Pipelines](ci-cd-pipelines.md) - Build and deployment pipelines for containerized applications
- [Infrastructure as Code](infrastructure-as-code.md) - Terraform/Pulumi for cluster provisioning
