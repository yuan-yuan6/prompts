# Container Orchestration & Kubernetes Management Framework

## Purpose
Comprehensive framework for implementing container orchestration platforms including Kubernetes deployment, service mesh configuration, operator development, Helm chart management, and cloud-native application orchestration at scale.

## Template

Deploy container orchestration for [CLUSTER_NAME] with [NODE_COUNT] nodes, [POD_COUNT] pods, [NAMESPACE_COUNT] namespaces, managing [CONTAINER_COUNT] containers, achieving [UPTIME_TARGET]% uptime, [RESOURCE_UTILIZATION]% resource efficiency, [AUTO_SCALING] auto-scaling capability, [DEPLOYMENT_VELOCITY] deployments/day, and [RECOVERY_TIME] recovery time objective.

### 1. Kubernetes Cluster Architecture

| **Cluster Component** | **Configuration** | **Resource Allocation** | **High Availability** | **Security Level** | **Monitoring Setup** |
|---------------------|-----------------|----------------------|-------------------|------------------|-------------------|
| Control Plane | [CONTROL_CONFIG] | [CONTROL_RESOURCES] | [CONTROL_HA] | [CONTROL_SECURITY] | [CONTROL_MONITORING] |
| Worker Nodes | [WORKER_CONFIG] | [WORKER_RESOURCES] | [WORKER_HA] | [WORKER_SECURITY] | [WORKER_MONITORING] |
| etcd Cluster | [ETCD_CONFIG] | [ETCD_RESOURCES] | [ETCD_HA] | [ETCD_SECURITY] | [ETCD_MONITORING] |
| Networking Layer | [NETWORK_CONFIG] | [NETWORK_RESOURCES] | [NETWORK_HA] | [NETWORK_SECURITY] | [NETWORK_MONITORING] |
| Storage Backend | [STORAGE_CONFIG] | [STORAGE_RESOURCES] | [STORAGE_HA] | [STORAGE_SECURITY] | [STORAGE_MONITORING] |
| Ingress Controllers | [INGRESS_CONFIG] | [INGRESS_RESOURCES] | [INGRESS_HA] | [INGRESS_SECURITY] | [INGRESS_MONITORING] |

### 2. Container Management Framework

**Container Lifecycle Management:**
```
Docker/Container Runtime:
Image Management:
- Registry Configuration: [REGISTRY_CONFIG]
- Image Pull Policy: [PULL_POLICY]
- Image Scanning: [IMAGE_SCANNING]
- Layer Caching: [LAYER_CACHING]
- Garbage Collection: [GARBAGE_COLLECTION]
- Private Registries: [PRIVATE_REGISTRIES]

Container Configuration:
- Resource Limits: [RESOURCE_LIMITS]
- Resource Requests: [RESOURCE_REQUESTS]
- Environment Variables: [ENV_VARIABLES]
- Volume Mounts: [VOLUME_MOUNTS]
- Security Context: [SECURITY_CONTEXT]
- Health Checks: [HEALTH_CHECKS]

Pod Specifications:
- Pod Topology: [POD_TOPOLOGY]
- Init Containers: [INIT_CONTAINERS]
- Sidecar Patterns: [SIDECAR_PATTERNS]
- Pod Disruption Budget: [POD_DISRUPTION]
- Pod Priority: [POD_PRIORITY]
- Pod Affinity: [POD_AFFINITY]

Workload Types:
- Deployments: [DEPLOYMENT_CONFIG]
- StatefulSets: [STATEFULSET_CONFIG]
- DaemonSets: [DAEMONSET_CONFIG]
- Jobs/CronJobs: [JOB_CONFIG]
- ReplicaSets: [REPLICASET_CONFIG]
- Custom Resources: [CUSTOM_RESOURCES]
```

### 3. Service Mesh Implementation

| **Service Mesh Component** | **Technology Choice** | **Features Enabled** | **Performance Impact** | **Security Features** | **Observability** |
|--------------------------|---------------------|-------------------|----------------------|--------------------|--------------------|
| Data Plane | [DATA_PLANE_TECH] | [DATA_PLANE_FEATURES] | [DATA_PLANE_PERF] | [DATA_PLANE_SECURITY] | [DATA_PLANE_OBSERVE] |
| Control Plane | [CONTROL_PLANE_TECH] | [CONTROL_PLANE_FEATURES] | [CONTROL_PLANE_PERF] | [CONTROL_PLANE_SECURITY] | [CONTROL_PLANE_OBSERVE] |
| Traffic Management | [TRAFFIC_TECH] | [TRAFFIC_FEATURES] | [TRAFFIC_PERF] | [TRAFFIC_SECURITY] | [TRAFFIC_OBSERVE] |
| Security Policies | [SECURITY_TECH] | [SECURITY_FEATURES] | [SECURITY_PERF] | [SECURITY_SECURITY] | [SECURITY_OBSERVE] |
| Observability Stack | [OBSERVE_TECH] | [OBSERVE_FEATURES] | [OBSERVE_PERF] | [OBSERVE_SECURITY] | [OBSERVE_OBSERVE] |
| Multi-Cluster | [MULTI_TECH] | [MULTI_FEATURES] | [MULTI_PERF] | [MULTI_SECURITY] | [MULTI_OBSERVE] |

### 4. Kubernetes Operators Development

```
Operator Framework:
Custom Resource Definitions:
- API Version: [CRD_API_VERSION]
- Resource Schema: [CRD_SCHEMA]
- Validation Rules: [CRD_VALIDATION]
- Conversion Webhooks: [CRD_CONVERSION]
- Printer Columns: [CRD_PRINTER]
- Subresources: [CRD_SUBRESOURCES]

Controller Logic:
- Reconciliation Loop: [CONTROLLER_RECONCILE]
- Watch Configuration: [CONTROLLER_WATCH]
- Event Handling: [CONTROLLER_EVENTS]
- Error Handling: [CONTROLLER_ERRORS]
- Rate Limiting: [CONTROLLER_RATE_LIMIT]
- Leader Election: [CONTROLLER_LEADER]

Operator Patterns:
- Level 1 - Basic: [OPERATOR_BASIC]
- Level 2 - Seamless Upgrades: [OPERATOR_UPGRADES]
- Level 3 - Full Lifecycle: [OPERATOR_LIFECYCLE]
- Level 4 - Deep Insights: [OPERATOR_INSIGHTS]
- Level 5 - Auto Pilot: [OPERATOR_AUTOPILOT]
- Testing Strategy: [OPERATOR_TESTING]

Operator SDK:
- Development Framework: [SDK_FRAMEWORK]
- Scaffolding Tools: [SDK_SCAFFOLDING]
- Testing Framework: [SDK_TESTING]
- Bundle Generation: [SDK_BUNDLE]
- OLM Integration: [SDK_OLM]
- Deployment Method: [SDK_DEPLOYMENT]
```

### 5. Helm Chart Management

| **Helm Component** | **Chart Structure** | **Version Strategy** | **Dependencies** | **Testing Method** | **Distribution** |
|-------------------|-------------------|-------------------|-----------------|------------------|-----------------|
| Chart Templates | [TEMPLATE_STRUCTURE] | [TEMPLATE_VERSION] | [TEMPLATE_DEPS] | [TEMPLATE_TESTING] | [TEMPLATE_DIST] |
| Values Configuration | [VALUES_STRUCTURE] | [VALUES_VERSION] | [VALUES_DEPS] | [VALUES_TESTING] | [VALUES_DIST] |
| Chart Hooks | [HOOKS_STRUCTURE] | [HOOKS_VERSION] | [HOOKS_DEPS] | [HOOKS_TESTING] | [HOOKS_DIST] |
| Chart Tests | [TESTS_STRUCTURE] | [TESTS_VERSION] | [TESTS_DEPS] | [TESTS_TESTING] | [TESTS_DIST] |
| Library Charts | [LIBRARY_STRUCTURE] | [LIBRARY_VERSION] | [LIBRARY_DEPS] | [LIBRARY_TESTING] | [LIBRARY_DIST] |
| Umbrella Charts | [UMBRELLA_STRUCTURE] | [UMBRELLA_VERSION] | [UMBRELLA_DEPS] | [UMBRELLA_TESTING] | [UMBRELLA_DIST] |

### 6. Auto-Scaling & Resource Management

**Scaling Framework:**
| **Scaling Type** | **Trigger Metrics** | **Min/Max Limits** | **Scaling Speed** | **Cost Impact** | **Performance Gain** |
|-----------------|-------------------|------------------|-----------------|---------------|-------------------|
| Horizontal Pod Autoscaler | [HPA_METRICS] | [HPA_LIMITS] | [HPA_SPEED] | [HPA_COST] | [HPA_PERFORMANCE] |
| Vertical Pod Autoscaler | [VPA_METRICS] | [VPA_LIMITS] | [VPA_SPEED] | [VPA_COST] | [VPA_PERFORMANCE] |
| Cluster Autoscaler | [CA_METRICS] | [CA_LIMITS] | [CA_SPEED] | [CA_COST] | [CA_PERFORMANCE] |
| Custom Metrics Scaling | [CUSTOM_METRICS] | [CUSTOM_LIMITS] | [CUSTOM_SPEED] | [CUSTOM_COST] | [CUSTOM_PERFORMANCE] |
| Predictive Scaling | [PREDICT_METRICS] | [PREDICT_LIMITS] | [PREDICT_SPEED] | [PREDICT_COST] | [PREDICT_PERFORMANCE] |
| Multi-Dimensional Scaling | [MULTI_METRICS] | [MULTI_LIMITS] | [MULTI_SPEED] | [MULTI_COST] | [MULTI_PERFORMANCE] |

### 7. Networking & Service Discovery

```
Kubernetes Networking:
Network Policies:
- Ingress Rules: [NETWORK_INGRESS]
- Egress Rules: [NETWORK_EGRESS]
- Pod Selectors: [NETWORK_SELECTORS]
- Namespace Isolation: [NETWORK_ISOLATION]
- Default Policies: [NETWORK_DEFAULTS]
- Policy Testing: [NETWORK_TESTING]

Service Types:
- ClusterIP Services: [SERVICE_CLUSTERIP]
- NodePort Services: [SERVICE_NODEPORT]
- LoadBalancer Services: [SERVICE_LB]
- ExternalName Services: [SERVICE_EXTERNAL]
- Headless Services: [SERVICE_HEADLESS]
- Multi-Port Services: [SERVICE_MULTIPORT]

Ingress Configuration:
- Ingress Controllers: [INGRESS_CONTROLLERS]
- TLS Termination: [INGRESS_TLS]
- Path-Based Routing: [INGRESS_PATH]
- Host-Based Routing: [INGRESS_HOST]
- Rate Limiting: [INGRESS_RATE_LIMIT]
- WAF Integration: [INGRESS_WAF]

Service Discovery:
- DNS Configuration: [DISCOVERY_DNS]
- Service Registry: [DISCOVERY_REGISTRY]
- Endpoint Slices: [DISCOVERY_ENDPOINTS]
- External DNS: [DISCOVERY_EXTERNAL]
- Service Mesh Discovery: [DISCOVERY_MESH]
- Cross-Cluster Discovery: [DISCOVERY_CROSS]
```

### 8. Storage & Persistence

| **Storage Type** | **Storage Class** | **Provisioner** | **Performance** | **Backup Strategy** | **Disaster Recovery** |
|-----------------|-----------------|---------------|---------------|-------------------|---------------------|
| Block Storage | [BLOCK_CLASS] | [BLOCK_PROVISIONER] | [BLOCK_PERFORMANCE] | [BLOCK_BACKUP] | [BLOCK_DR] |
| File Storage | [FILE_CLASS] | [FILE_PROVISIONER] | [FILE_PERFORMANCE] | [FILE_BACKUP] | [FILE_DR] |
| Object Storage | [OBJECT_CLASS] | [OBJECT_PROVISIONER] | [OBJECT_PERFORMANCE] | [OBJECT_BACKUP] | [OBJECT_DR] |
| Local Storage | [LOCAL_CLASS] | [LOCAL_PROVISIONER] | [LOCAL_PERFORMANCE] | [LOCAL_BACKUP] | [LOCAL_DR] |
| CSI Drivers | [CSI_CLASS] | [CSI_PROVISIONER] | [CSI_PERFORMANCE] | [CSI_BACKUP] | [CSI_DR] |
| StatefulSet Storage | [STATEFUL_CLASS] | [STATEFUL_PROVISIONER] | [STATEFUL_PERFORMANCE] | [STATEFUL_BACKUP] | [STATEFUL_DR] |

### 9. Security & Compliance

**Container Security Framework:**
| **Security Layer** | **Implementation** | **Policy Engine** | **Audit Logging** | **Compliance Check** | **Incident Response** |
|-------------------|------------------|-----------------|-----------------|--------------------|--------------------|
| RBAC Configuration | [RBAC_IMPL] | [RBAC_POLICY] | [RBAC_AUDIT] | [RBAC_COMPLIANCE] | [RBAC_INCIDENT] |
| Pod Security Policies | [PSP_IMPL] | [PSP_POLICY] | [PSP_AUDIT] | [PSP_COMPLIANCE] | [PSP_INCIDENT] |
| Network Policies | [NETPOL_IMPL] | [NETPOL_POLICY] | [NETPOL_AUDIT] | [NETPOL_COMPLIANCE] | [NETPOL_INCIDENT] |
| Secret Management | [SECRET_IMPL] | [SECRET_POLICY] | [SECRET_AUDIT] | [SECRET_COMPLIANCE] | [SECRET_INCIDENT] |
| Image Security | [IMAGE_IMPL] | [IMAGE_POLICY] | [IMAGE_AUDIT] | [IMAGE_COMPLIANCE] | [IMAGE_INCIDENT] |
| Runtime Security | [RUNTIME_IMPL] | [RUNTIME_POLICY] | [RUNTIME_AUDIT] | [RUNTIME_COMPLIANCE] | [RUNTIME_INCIDENT] |

### 10. Monitoring & Observability

```
Observability Stack:
Metrics Collection:
- Prometheus Setup: [METRICS_PROMETHEUS]
- Custom Metrics: [METRICS_CUSTOM]
- Application Metrics: [METRICS_APPLICATION]
- System Metrics: [METRICS_SYSTEM]
- Business Metrics: [METRICS_BUSINESS]
- Cost Metrics: [METRICS_COST]

Logging Architecture:
- Log Aggregation: [LOGGING_AGGREGATION]
- Log Processing: [LOGGING_PROCESSING]
- Log Storage: [LOGGING_STORAGE]
- Log Analysis: [LOGGING_ANALYSIS]
- Log Retention: [LOGGING_RETENTION]
- Log Security: [LOGGING_SECURITY]

Distributed Tracing:
- Tracing Backend: [TRACING_BACKEND]
- Instrumentation: [TRACING_INSTRUMENTATION]
- Sampling Strategy: [TRACING_SAMPLING]
- Trace Analysis: [TRACING_ANALYSIS]
- Performance Impact: [TRACING_PERFORMANCE]
- Integration Points: [TRACING_INTEGRATION]

Alerting & Dashboards:
- Alert Rules: [ALERT_RULES]
- Alert Routing: [ALERT_ROUTING]
- Escalation Policy: [ALERT_ESCALATION]
- Dashboard Design: [DASHBOARD_DESIGN]
- SLI/SLO Tracking: [SLI_SLO_TRACKING]
- Reporting: [REPORTING]

Chaos Engineering:
- Failure Injection: [CHAOS_INJECTION]
- Game Days: [CHAOS_GAMEDAYS]
- Automated Testing: [CHAOS_AUTOMATED]
- Recovery Testing: [CHAOS_RECOVERY]
- Documentation: [CHAOS_DOCUMENTATION]
- Learning Process: [CHAOS_LEARNING]
```

## Usage Examples

### Example 1: Production Kubernetes Cluster
```
Environment: Multi-region production
Clusters: 3 regions, 15 nodes each
Workload: 500 microservices, 2000 pods
Service Mesh: Istio with mTLS
Storage: Persistent volumes with CSI
Monitoring: Prometheus + Grafana + Jaeger
Scaling: HPA + VPA + Cluster Autoscaler
Success: 99.99% uptime achieved
```

### Example 2: Edge Computing Platform
```
Deployment: K3s on edge devices
Nodes: 1000+ edge locations
Management: Fleet management with Rancher
Workloads: IoT data processing
Networking: Lightweight CNI
Updates: GitOps with Fleet
Monitoring: Lightweight telemetry
Scale: Managing 10,000+ containers
```

### Example 3: Development Platform
```
Purpose: Developer self-service platform
Clusters: Dynamic namespace provisioning
Tools: Tekton CI/CD, ArgoCD
Features: Automated environment creation
Developer Portal: Backstage integration
Cost Control: Resource quotas, auto-cleanup
Security: Zero-trust networking
Productivity: 50% faster deployments
```

## Customization Options

### 1. Cluster Type
- Production Multi-Region
- Development/Testing
- Edge Computing
- Hybrid Cloud
- Air-Gapped

### 2. Orchestration Platform
- Kubernetes (vanilla)
- OpenShift
- Rancher
- EKS/GKE/AKS
- K3s/MicroK8s

### 3. Workload Type
- Stateless Services
- Stateful Applications
- Batch Processing
- ML/AI Workloads
- Real-time Systems

### 4. Scale
- Small (< 10 nodes)
- Medium (10-100 nodes)
- Large (100-1000 nodes)
- Massive (> 1000 nodes)
- Multi-Cluster Federation

### 5. Compliance Level
- No Compliance
- Basic Security
- Industry Standard
- Regulated (HIPAA/PCI)
- Government/Military