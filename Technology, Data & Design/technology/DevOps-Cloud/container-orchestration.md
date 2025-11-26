---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- design
- ai-ml
- strategy
title: Container Orchestration Template
use_cases:
- Creating design and implement container orchestration strategies using kubernetes,
  docker swarm, or other platforms to manage containerized applications at scale.
- Project planning and execution
- Strategy development
industries:
- manufacturing
- technology
type: template
difficulty: intermediate
slug: container-orchestration
---

# Container Orchestration Template

## Purpose
Design and implement container orchestration strategies using Kubernetes, Docker Swarm, or other platforms to manage containerized applications at scale.

## Quick Container Orchestration Prompt
Deploy [application] on Kubernetes ([EKS/GKE/AKS]). Config: [X replicas], resource limits (CPU: [Y], memory: [Z]), health checks (liveness, readiness). Services: LoadBalancer/Ingress with TLS. Scaling: HPA ([min]-[max] pods, [metric] threshold). Storage: PVC for [stateful data]. Observability: Prometheus metrics, Grafana dashboards, centralized logging.

## Quick Start

**Deploy container orchestration in 5 steps:**

1. **Create Kubernetes Cluster**: Set up EKS/GKE/AKS or local cluster with kubectl configured and cluster-autoscaler enabled
2. **Containerize Applications**: Write Dockerfiles, build images, push to registry (ECR/GCR/ACR), tag with semantic versions
3. **Deploy with Manifests**: Create Deployment, Service, and ConfigMap/Secret YAML files with resource limits and health checks
4. **Configure Auto-Scaling**: Implement HPA (Horizontal Pod Autoscaler) based on CPU/memory/custom metrics
5. **Set Up Monitoring**: Deploy Prometheus + Grafana for cluster metrics, logging with ELK/Loki, and distributed tracing

**Quick Kubernetes Deployment:**
```bash
# Create deployment with 3 replicas
kubectl create deployment app --image=myapp:v1.0 --replicas=3

# Expose as service
kubectl expose deployment app --port=80 --target-port=8080 --type=LoadBalancer

# Configure auto-scaling
kubectl autoscale deployment app --min=3 --max=10 --cpu-percent=70

# Check status
kubectl get pods,svc,hpa
```

## Template

```
You are a container orchestration expert with deep knowledge of Kubernetes, Docker, and cloud-native architectures. Generate a comprehensive container orchestration strategy based on:

Application Requirements:
- Application Type: [STATELESS/STATEFUL/BATCH]
- Number of Services: [SERVICE_COUNT]
- Traffic Pattern: [STEADY/BURSTY/PERIODIC]
- Data Requirements: [STORAGE_NEEDS]

Infrastructure:
- Platform: [KUBERNETES/SWARM/ECS/NOMAD]
- Environment: [CLOUD_PROVIDER]
- Cluster Size: [NODE_COUNT]
- High Availability: [HA_REQUIREMENTS]

Generate a comprehensive container orchestration implementation:

1. ARCHITECTURE OVERVIEW

   ## Container Platform Architecture

   ```yaml
   cluster_architecture:
     control_plane:
       masters:
         count: 3
         instance_type: m5.xlarge
         availability_zones: [us-east-1a, us-east-1b, us-east-1c]
         components:
           - kube-apiserver
           - kube-controller-manager
           - kube-scheduler
           - etcd

     data_plane:
       worker_pools:
         general:
           count: 5
           instance_type: m5.2xlarge
           autoscaling:
             min: 3
             max: 10
             target_cpu: 70

         compute_intensive:
           count: 3
           instance_type: c5.4xlarge
           taints:
             - key: workload-type
               value: compute
               effect: NoSchedule

         memory_intensive:
           count: 3
           instance_type: r5.2xlarge
           taints:
             - key: workload-type
               value: memory
               effect: NoSchedule
   ```

   ## Multi-Cluster Strategy

   ```python
   class MultiClusterOrchestration:
       def __init__(self):
           self.clusters = {
               'production': {
                   'region': 'us-east-1',
                   'purpose': 'production_workloads',
                   'size': 'large',
                   'ha': True
               },
               'staging': {
                   'region': 'us-east-1',
                   'purpose': 'pre_production',
                   'size': 'medium',
                   'ha': False
               },
               'development': {
                   'region': 'us-west-2',
                   'purpose': 'development',
                   'size': 'small',
                   'ha': False
               }
           }

       def setup_cluster_federation(self):
           federation_config = {
               'control_plane': 'production',
               'member_clusters': ['production', 'staging', 'development'],
               'dns_zone': 'federation.example.com',
               'cross_cluster_discovery': True,
               'global_load_balancing': True
           }
           return federation_config
   ```

2. KUBERNETES DEPLOYMENT PATTERNS

   ## Deployment Strategies

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: api-service
     namespace: production
   spec:
     replicas: 5
     strategy:
       type: RollingUpdate
       rollingUpdate:
         maxSurge: 2
         maxUnavailable: 1
     selector:
       matchLabels:
         app: api-service
     template:
       metadata:
         labels:
           app: api-service
           version: v2.0.0
       spec:
         affinity:
           podAntiAffinity:
             requiredDuringSchedulingIgnoredDuringExecution:
               - labelSelector:
                   matchExpressions:
                     - key: app
                       operator: In
                       values:
                         - api-service
                 topologyKey: kubernetes.io/hostname

         containers:
         - name: api
           image: api-service:2.0.0
           ports:
           - containerPort: 8080

           resources:
             requests:
               memory: "256Mi"
               cpu: "250m"
             limits:
               memory: "512Mi"
               cpu: "500m"

           livenessProbe:
             httpGet:
               path: /health
               port: 8080
             initialDelaySeconds: 30
             periodSeconds: 10

           readinessProbe:
             httpGet:
               path: /ready
               port: 8080
             initialDelaySeconds: 5
             periodSeconds: 5

           env:
           - name: DATABASE_URL
             valueFrom:
               secretKeyRef:
                 name: database-credentials
                 key: url

           volumeMounts:
           - name: config
             mountPath: /etc/config
             readOnly: true

         volumes:
         - name: config
           configMap:
             name: api-config
   ```

   ## Blue-Green Deployment

   ```python
   def blue_green_deployment():
       deployment_steps = {
           'step_1': 'Deploy green version alongside blue',
           'step_2': 'Run smoke tests on green',
           'step_3': 'Switch service selector to green',
           'step_4': 'Monitor green deployment',
           'step_5': 'Keep blue for rollback',
           'step_6': 'Remove blue after validation'
       }

       service_update = '''
       kubectl patch service api-service -p '
       {
         "spec": {
           "selector": {
             "version": "green"
           }
         }
       }'
       '''

       rollback_command = '''
       kubectl patch service api-service -p '
       {
         "spec": {
           "selector": {
             "version": "blue"
           }
         }
       }'
       '''

       return deployment_steps, service_update, rollback_command
   ```

3. SERVICE MESH IMPLEMENTATION

   ## Istio Configuration

   ```yaml
   # Virtual Service
   apiVersion: networking.istio.io/v1beta1
   kind: VirtualService
   metadata:
     name: api-service
   spec:
     hosts:
     - api.example.com
     gateways:
     - api-gateway
     http:
     - match:
       - headers:
           x-version:
             exact: canary
       route:
       - destination:
           host: api-service
           subset: canary
         weight: 100
     - route:
       - destination:
           host: api-service
           subset: stable
         weight: 90
       - destination:
           host: api-service
           subset: canary
         weight: 10
       timeout: 30s
       retries:
         attempts: 3
         perTryTimeout: 10s

   ---
   # Destination Rule
   apiVersion: networking.istio.io/v1beta1
   kind: DestinationRule
   metadata:
     name: api-service
   spec:
     host: api-service
     trafficPolicy:
       connectionPool:
         tcp:
           maxConnections: 100
         http:
           http1MaxPendingRequests: 50
           http2MaxRequests: 100
       loadBalancer:
         simple: LEAST_REQUEST
       outlierDetection:
         consecutive5xxErrors: 5
         interval: 30s
         baseEjectionTime: 30s
     subsets:
     - name: stable
       labels:
         version: stable
     - name: canary
       labels:
         version: canary
   ```

   ## Circuit Breaker Pattern

   ```python
   class CircuitBreakerConfig:
       def __init__(self):
           self.thresholds = {
               'consecutive_errors': 5,
               'error_percentage': 50,
               'interval': '30s',
               'base_ejection_time': '30s',
               'max_ejection_percentage': 50,
               'min_health_percentage': 30
           }

       def generate_envoy_config(self):
           return {
               'outlier_detection': {
                   'consecutive_5xx': self.thresholds['consecutive_errors'],
                   'interval': self.thresholds['interval'],
                   'base_ejection_time': self.thresholds['base_ejection_time'],
                   'max_ejection_percent': self.thresholds['max_ejection_percentage'],
                   'enforcing_consecutive_5xx': 100,
                   'enforcing_success_rate': 100,
                   'success_rate_minimum_hosts': 3,
                   'success_rate_request_volume': 50
               }
           }
   ```

4. STATEFUL WORKLOADS

   ## StatefulSet Configuration

   ```yaml
   apiVersion: apps/v1
   kind: StatefulSet
   metadata:
     name: postgres-cluster
   spec:
     serviceName: postgres-service
     replicas: 3
     selector:
       matchLabels:
         app: postgres
     template:
       metadata:
         labels:
           app: postgres
       spec:
         initContainers:
         - name: init-postgres
           image: postgres:13
           command:
           - bash
           - "-c"
           - |
             set -ex
             [[ `hostname` =~ -([0-9]+)$ ]] || exit 1
             ordinal=${BASH_REMATCH[1]}
             if [[ $ordinal -eq 0 ]]; then
               echo "Primary node initialization"
             else
               echo "Replica node initialization"
               pg_basebackup -h postgres-0.postgres-service -U replicator -D /var/lib/postgresql/data -Fp -Xs -P -R
             fi

         containers:
         - name: postgres
           image: postgres:13
           ports:
           - containerPort: 5432
           env:
           - name: POSTGRES_DB
             value: production
           - name: POSTGRES_USER
             valueFrom:
               secretKeyRef:
                 name: postgres-secret
                 key: username
           - name: POSTGRES_PASSWORD
             valueFrom:
               secretKeyRef:
                 name: postgres-secret
                 key: password

           volumeMounts:
           - name: postgres-storage
             mountPath: /var/lib/postgresql/data

           livenessProbe:
             exec:
               command:
                 - /bin/sh
                 - -c
                 - pg_isready -U postgres
             initialDelaySeconds: 30
             periodSeconds: 10

     volumeClaimTemplates:
     - metadata:
         name: postgres-storage
       spec:
         accessModes: ["ReadWriteOnce"]
         storageClassName: fast-ssd
         resources:
           requests:
             storage: 100Gi
   ```

5. AUTOSCALING STRATEGIES

   ## Horizontal Pod Autoscaler

   ```yaml
   apiVersion: autoscaling/v2
   kind: HorizontalPodAutoscaler
   metadata:
     name: api-service-hpa
   spec:
     scaleTargetRef:
       apiVersion: apps/v1
       kind: Deployment
       name: api-service
     minReplicas: 3
     maxReplicas: 50
     metrics:
     - type: Resource
       resource:
         name: cpu
         target:
           type: Utilization
           averageUtilization: 70
     - type: Resource
       resource:
         name: memory
         target:
           type: Utilization
           averageUtilization: 80
     - type: Pods
       pods:
         metric:
           name: http_requests_per_second
         target:
           type: AverageValue
           averageValue: "1000"
     - type: External
       external:
         metric:
           name: queue_messages
           selector:
             matchLabels:
               queue: work-queue
         target:
           type: Value
           value: "30"
     behavior:
       scaleDown:
         stabilizationWindowSeconds: 300
         policies:
         - type: Percent
           value: 50
           periodSeconds: 60
       scaleUp:
         stabilizationWindowSeconds: 0
         policies:
         - type: Percent
           value: 100
           periodSeconds: 30
         - type: Pods
           value: 5
           periodSeconds: 30
         selectPolicy: Max
   ```

   ## Vertical Pod Autoscaler

   ```yaml
   apiVersion: autoscaling.k8s.io/v1
   kind: VerticalPodAutoscaler
   metadata:
     name: api-service-vpa
   spec:
     targetRef:
       apiVersion: apps/v1
       kind: Deployment
       name: api-service
     updatePolicy:
       updateMode: "Auto"
     resourcePolicy:
       containerPolicies:
       - containerName: api
         minAllowed:
           cpu: 100m
           memory: 128Mi
         maxAllowed:
           cpu: 2
           memory: 2Gi
         controlledResources: ["cpu", "memory"]
   ```

6. NETWORKING & INGRESS

   ## Ingress Configuration

   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: api-ingress
     annotations:
       kubernetes.io/ingress.class: nginx
       cert-manager.io/cluster-issuer: letsencrypt-prod
       nginx.ingress.kubernetes.io/rate-limit: "100"
       nginx.ingress.kubernetes.io/ssl-redirect: "true"
       nginx.ingress.kubernetes.io/websocket-services: "websocket-service"
   spec:
     tls:
     - hosts:
       - api.example.com
       secretName: api-tls
     rules:
     - host: api.example.com
       http:
         paths:
         - path: /api/v1
           pathType: Prefix
           backend:
             service:
               name: api-service
               port:
                 number: 80
         - path: /ws
           pathType: Prefix
           backend:
             service:
               name: websocket-service
               port:
                 number: 8080
   ```

   ## Network Policies

   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: NetworkPolicy
   metadata:
     name: api-network-policy
   spec:
     podSelector:
       matchLabels:
         app: api-service
     policyTypes:
     - Ingress
     - Egress
     ingress:
     - from:
       - namespaceSelector:
           matchLabels:
             name: ingress-nginx
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
     - to:
       - podSelector:
           matchLabels:
             app: cache
       ports:
       - protocol: TCP
         port: 6379
     - to:
       - namespaceSelector: {}
         podSelector:
           matchLabels:
             k8s-app: kube-dns
       ports:
       - protocol: UDP
         port: 53
   ```

7. STORAGE ORCHESTRATION

   ## Persistent Volume Management

   ```yaml
   # StorageClass
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: fast-ssd
   provisioner: kubernetes.io/aws-ebs
   parameters:
     type: gp3
     iops: "10000"
     throughput: "250"
     encrypted: "true"
     kmsKeyId: arn:aws:kms:us-east-1:123456789:key/abc-123
   reclaimPolicy: Retain
   allowVolumeExpansion: true
   volumeBindingMode: WaitForFirstConsumer

   ---
   # PersistentVolumeClaim
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: data-volume
   spec:
     accessModes:
       - ReadWriteOnce
     storageClassName: fast-ssd
     resources:
       requests:
         storage: 100Gi
   ```

   ## CSI Driver Configuration

   ```python
   class StorageOrchestration:
       def __init__(self):
           self.csi_drivers = {
               'aws_ebs': {
                   'driver': 'ebs.csi.aws.com',
                   'features': ['resize', 'snapshot', 'clone'],
                   'volume_types': ['gp3', 'io2', 'st1']
               },
               'azure_disk': {
                   'driver': 'disk.csi.azure.com',
                   'features': ['resize', 'snapshot'],
                   'volume_types': ['Premium_LRS', 'Standard_LRS']
               },
               'gce_pd': {
                   'driver': 'pd.csi.storage.gke.io',
                   'features': ['resize', 'snapshot', 'clone'],
                   'volume_types': ['pd-ssd', 'pd-standard']
               }
           }

       def create_volume_snapshot(self, pvc_name):
           snapshot_config = f'''
           apiVersion: snapshot.storage.k8s.io/v1
           kind: VolumeSnapshot
           metadata:
             name: [PVC_NAME]-snapshot
           spec:
             volumeSnapshotClassName: csi-snapclass
             source:
               persistentVolumeClaimName: [PVC_NAME]
           '''
           return snapshot_config
   ```

8. SECURITY & RBAC

   ## RBAC Configuration

   ```yaml
   # ServiceAccount
   apiVersion: v1
   kind: ServiceAccount
   metadata:
     name: api-service-account
     namespace: production

   ---
   # Role
   apiVersion: rbac.authorization.k8s.io/v1
   kind: Role
   metadata:
     name: api-role
     namespace: production
   rules:
   - apiGroups: [""]
     resources: ["configmaps", "secrets"]
     verbs: ["get", "list", "watch"]
   - apiGroups: [""]
     resources: ["pods"]
     verbs: ["get", "list"]
   - apiGroups: ["apps"]
     resources: ["deployments"]
     verbs: ["get", "list", "watch"]

   ---
   # RoleBinding
   apiVersion: rbac.authorization.k8s.io/v1
   kind: RoleBinding
   metadata:
     name: api-rolebinding
     namespace: production
   subjects:
   - kind: ServiceAccount
     name: api-service-account
     namespace: production
   roleRef:
     kind: Role
     name: api-role
     apiGroup: rbac.authorization.k8s.io
   ```

   ## Pod Security Policies

   ```yaml
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
       - 'projected'
       - 'secret'
       - 'downwardAPI'
       - 'persistentVolumeClaim'
     hostNetwork: false
     hostIPC: false
     hostPID: false
     runAsUser:
       rule: 'MustRunAsNonRoot'
     seLinux:
       rule: 'RunAsAny'
     supplementalGroups:
       rule: 'RunAsAny'
     fsGroup:
       rule: 'RunAsAny'
     readOnlyRootFilesystem: true
   ```

9. OBSERVABILITY & MONITORING

   ## Prometheus Monitoring

   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: api-service
     annotations:
       prometheus.io/scrape: "true"
       prometheus.io/port: "8080"
       prometheus.io/path: "/metrics"
   spec:
     selector:
       app: api-service
     ports:
     - port: 80
       targetPort: 8080

   ---
   apiVersion: monitoring.coreos.com/v1
   kind: ServiceMonitor
   metadata:
     name: api-service-monitor
   spec:
     selector:
       matchLabels:
         app: api-service
     endpoints:
     - port: metrics
       interval: 30s
       path: /metrics
   ```

10. CI/CD INTEGRATION

    ## GitOps with ArgoCD

    ```yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: api-service
      namespace: argocd
    spec:
      project: default
      source:
        repoURL: https://github.com/example/k8s-configs
        targetRevision: HEAD
        path: applications/api-service
      destination:
        server: https://kubernetes.default.svc
        namespace: production
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
          allowEmpty: false
        syncOptions:
        - Validate=true
        - CreateNamespace=false
        - PrunePropagationPolicy=foreground
        retry:
          limit: 5
          backoff:
            duration: 5s
            factor: 2
            maxDuration: 3m
    ```

11. DISASTER RECOVERY

    ## Backup and Restore

    ```python
    class DisasterRecovery:
        def __init__(self):
            self.backup_strategy = {
                'etcd': self.backup_etcd(),
                'persistent_volumes': self.backup_volumes(),
                'configurations': self.backup_configs(),
                'secrets': self.backup_secrets()
            }

        def backup_etcd(self):
            return '''
            ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-snapshot.db \
              --endpoints=https://127.0.0.1:2379 \
              --cacert=/etc/kubernetes/pki/etcd/ca.crt \
              --cert=/etc/kubernetes/pki/etcd/server.crt \
              --key=/etc/kubernetes/pki/etcd/server.key
            '''

        def restore_cluster(self, backup_location):
            restore_steps = [
                'Stop kube-apiserver on all masters',
                'Restore etcd from snapshot',
                'Restore persistent volumes',
                'Apply configurations',
                'Restore secrets',
                'Verify cluster health',
                'Redeploy applications'
            ]
            return restore_steps
    ```

12. COST OPTIMIZATION

    ## Resource Optimization

    ```python
    def optimize_cluster_costs():
        strategies = {
            'spot_instances': {
                'percentage': 70,
                'on_demand_base': 30,
                'interruption_handling': 'graceful_shutdown'
            },
            'node_auto_scaling': {
                'enable': True,
                'min_nodes': 3,
                'max_nodes': 100,
                'scale_down_delay': '10m'
            },
            'resource_requests': {
                'cpu_utilization_target': 80,
                'memory_utilization_target': 85,
                'overprovisioning': 1.2
            },
            'idle_resource_cleanup': {
                'unused_volumes': 'delete_after_7_days',
                'orphaned_pods': 'immediate_cleanup',
                'completed_jobs': 'delete_after_24h'
            }
        }
        return strategies
    ```

Ensure the container orchestration is:
- Highly available and resilient
- Scalable and performant
- Secure by default
- Cost-optimized
- Observable and debuggable
```

## Variables
- `[STATELESS/STATEFUL/BATCH]`: Application type
- `[SERVICE_COUNT]`: Number of services
- `[STEADY/BURSTY/PERIODIC]`: Traffic patterns
- `[STORAGE_NEEDS]`: Storage requirements
- `[KUBERNETES/SWARM/ECS/NOMAD]`: Orchestration platform
- `[CLOUD_PROVIDER]`: Cloud environment
- `[NODE_COUNT]`: Cluster size
- `[HA_REQUIREMENTS]`: High availability needs

## Usage Example
Use for Kubernetes deployments, container platform design, microservices orchestration, or cloud-native transformations.

## Customization Tips
- Add specific scheduler configurations
- Include operator patterns
- Add multi-tenancy considerations
- Consider edge deployments

## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Container Orchestration Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/DevOps & Cloud](../../technology/DevOps & Cloud/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating design and implement container orchestration strategies using kubernetes, docker swarm, or other platforms to manage containerized applications at scale.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks
