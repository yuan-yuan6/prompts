---
title: Pipeline Infrastructure & Performance Template
category: data-analytics/Analytics Engineering
tags: [automation, data-analytics, infrastructure, terraform, kubernetes, performance, scaling]
use_cases:
  - Implementing pipeline performance optimization strategies
  - Designing infrastructure as code with Terraform for data platforms
  - Deploying containerized pipelines with Kubernetes orchestration
  - Building auto-scaling and resource management systems
related_templates:
  - pipeline-ingestion.md
  - pipeline-transformation.md
  - pipeline-orchestration.md
  - pipeline-observability.md
last_updated: 2025-11-10
---

# Pipeline Infrastructure & Performance Template

## Purpose
Design and implement scalable infrastructure for data pipelines with performance optimization, infrastructure as code (Terraform), container orchestration (Kubernetes), and auto-scaling strategies. This template covers infrastructure provisioning, deployment automation, performance tuning, and resource management.

## Quick Start

### For Data Engineers & DevOps
Get started with pipeline infrastructure in 3 steps:

1. **Optimize Pipeline Performance**
   - **Analyze Bottlenecks**: Identify CPU, memory, I/O, or network constraints
   - **Tune Parameters**: Optimize batch sizes, parallelism, memory allocation
   - **Implement Caching**: Reduce redundant computations and I/O
   - Example: `BOTTLENECK: "High memory usage", OPTIMIZATION: "Reduce batch size from 100K to 50K rows"`

2. **Provision Infrastructure with IaC**
   - **Terraform**: Define compute clusters, storage, databases, networking
   - **Modular Design**: Create reusable modules for common components
   - **Environment Management**: Separate configs for dev/staging/prod
   - Start with Terraform templates (lines 300-456)

3. **Deploy with Kubernetes**
   - **Containerization**: Package pipeline code in Docker containers
   - **Deployments**: Define replica counts, resource limits, health checks
   - **Auto-scaling**: Configure HPA for dynamic scaling based on metrics
   - Use Kubernetes configs (lines 458-612)

**Key Sections**: Performance Optimization (lines 77-298), Infrastructure as Code (300-456), Container Orchestration (458-612)

## Template

```
You are a data platform infrastructure architect specializing in [INFRASTRUCTURE_APPROACH]. Design a comprehensive infrastructure and performance optimization solution for [ORGANIZATION_NAME] to support [PIPELINE_SCOPE] using [IAC_TOOL] and [CONTAINER_PLATFORM].

INFRASTRUCTURE ARCHITECTURE OVERVIEW:
Project Specifications:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Pipeline scope: [PIPELINE_SCOPE]
- Performance objectives: [PERFORMANCE_OBJECTIVES]
- Scale requirements: [SCALE_REQUIREMENTS]
- Budget constraints: [BUDGET_CONSTRAINTS]

### Architecture Principles
- Infrastructure approach: [INFRASTRUCTURE_APPROACH] (Cloud-native/Hybrid/On-premise)
- IaC strategy: [IAC_STRATEGY]
- Container orchestration: [ORCHESTRATION_STRATEGY]
- Auto-scaling policy: [AUTOSCALING_POLICY]
- Cost optimization: [COST_OPTIMIZATION_STRATEGY]
- High availability: [HA_STRATEGY]
- Disaster recovery: [DR_STRATEGY]

### Technical Stack
- Cloud provider: [CLOUD_PROVIDER] (AWS/Azure/GCP)
- IaC tool: [IAC_TOOL] (Terraform/CloudFormation/Pulumi)
- Container platform: [CONTAINER_PLATFORM] (Kubernetes/ECS/Cloud Run)
- Container registry: [CONTAINER_REGISTRY]
- Compute platform: [COMPUTE_PLATFORM]
- Storage systems: [STORAGE_SYSTEMS]
- Networking: [NETWORKING_ARCHITECTURE]

### Performance Requirements
- Throughput target: [THROUGHPUT_TARGET]
- Latency requirements: [LATENCY_REQUIREMENTS]
- Concurrency level: [CONCURRENCY_LEVEL]
- Resource efficiency: [RESOURCE_EFFICIENCY_TARGET]
- Scalability range: [SCALABILITY_RANGE]

### PERFORMANCE OPTIMIZATION

### Pipeline Performance Tuning
```python
# Performance optimization framework
class PipelinePerformanceOptimizer:
    def __init__(self, config: dict):
        self.config = config
        self.performance_metrics = [PERFORMANCE_METRICS_COLLECTOR]()
        self.optimization_strategies = self.load_optimization_strategies()

    def optimize_pipeline_performance(self, pipeline_config: dict) -> dict:
        """
        Analyze and optimize pipeline performance

        Args:
            pipeline_config: Pipeline configuration details

        Returns:
            Optimization recommendations and results
        """
        # Analyze current performance
        performance_analysis = self.analyze_current_performance(pipeline_config)

        # Identify bottlenecks
        bottlenecks = self.identify_bottlenecks(performance_analysis)

        # Generate optimization recommendations
        recommendations = self.generate_optimization_recommendations(bottlenecks)

        # Apply optimizations
        optimization_results = self.apply_optimizations(
            pipeline_config,
            recommendations
        )

        return {
            'performance_analysis': performance_analysis,
            'bottlenecks': bottlenecks,
            'recommendations': recommendations,
            'optimization_results': optimization_results
        }

    def analyze_current_performance(self, pipeline_config: dict) -> dict:
        """
        Analyze current pipeline performance metrics
        """
        pipeline_id = pipeline_config['pipeline_id']

        # Collect historical performance data
        performance_data = self.performance_metrics.get_pipeline_metrics(
            pipeline_id=pipeline_id,
            time_range='[ANALYSIS_TIME_RANGE]',
            metrics=[
                'execution_duration',
                'throughput',
                'resource_utilization',
                'error_rate',
                'data_volume'
            ]
        )

        # Calculate performance statistics
        analysis = {
            'avg_execution_duration': [AVG_DURATION_CALCULATION],
            'p95_execution_duration': [P95_DURATION_CALCULATION],
            'avg_throughput': [AVG_THROUGHPUT_CALCULATION],
            'peak_cpu_usage': [PEAK_CPU_CALCULATION],
            'peak_memory_usage': [PEAK_MEMORY_CALCULATION],
            'avg_error_rate': [AVG_ERROR_RATE_CALCULATION],
            'data_volume_trend': [DATA_VOLUME_TREND_CALCULATION],
            'seasonal_patterns': self.identify_seasonal_patterns(performance_data),
            'resource_efficiency': self.calculate_resource_efficiency(performance_data)
        }

        return analysis

    def identify_bottlenecks(self, performance_analysis: dict) -> list:
        """
        Identify performance bottlenecks in the pipeline
        """
        bottlenecks = []
        thresholds = self.config['bottleneck_thresholds']

        # Duration bottlenecks
        if performance_analysis['p95_execution_duration'] > thresholds['max_duration']:
            bottlenecks.append({
                'type': 'DURATION_BOTTLENECK',
                'severity': 'HIGH',
                'current_value': performance_analysis['p95_execution_duration'],
                'threshold': thresholds['max_duration'],
                'description': 'Pipeline execution duration exceeds acceptable limits'
            })

        # Throughput bottlenecks
        if performance_analysis['avg_throughput'] < thresholds['min_throughput']:
            bottlenecks.append({
                'type': 'THROUGHPUT_BOTTLENECK',
                'severity': 'MEDIUM',
                'current_value': performance_analysis['avg_throughput'],
                'threshold': thresholds['min_throughput'],
                'description': 'Pipeline throughput below expected levels'
            })

        # Resource bottlenecks
        if performance_analysis['peak_cpu_usage'] > thresholds['max_cpu_usage']:
            bottlenecks.append({
                'type': 'CPU_BOTTLENECK',
                'severity': 'HIGH',
                'current_value': performance_analysis['peak_cpu_usage'],
                'threshold': thresholds['max_cpu_usage'],
                'description': 'CPU usage consistently high'
            })

        if performance_analysis['peak_memory_usage'] > thresholds['max_memory_usage']:
            bottlenecks.append({
                'type': 'MEMORY_BOTTLENECK',
                'severity': 'HIGH',
                'current_value': performance_analysis['peak_memory_usage'],
                'threshold': thresholds['max_memory_usage'],
                'description': 'Memory usage approaching limits'
            })

        # Error rate bottlenecks
        if performance_analysis['avg_error_rate'] > thresholds['max_error_rate']:
            bottlenecks.append({
                'type': 'ERROR_RATE_BOTTLENECK',
                'severity': 'CRITICAL',
                'current_value': performance_analysis['avg_error_rate'],
                'threshold': thresholds['max_error_rate'],
                'description': 'Error rate exceeds acceptable levels'
            })

        return bottlenecks

    def generate_optimization_recommendations(self, bottlenecks: list) -> list:
        """
        Generate optimization recommendations based on identified bottlenecks
        """
        recommendations = []

        for bottleneck in bottlenecks:
            if bottleneck['type'] == 'DURATION_BOTTLENECK':
                recommendations.extend([
                    {
                        'optimization': 'PARALLEL_PROCESSING',
                        'description': 'Increase parallelization of tasks',
                        'implementation': self.increase_parallelization,
                        'expected_improvement': '[PARALLELIZATION_IMPROVEMENT_ESTIMATE]',
                        'implementation_effort': 'MEDIUM'
                    },
                    {
                        'optimization': 'BATCH_SIZE_OPTIMIZATION',
                        'description': 'Optimize batch sizes for better throughput',
                        'implementation': self.optimize_batch_sizes,
                        'expected_improvement': '[BATCH_SIZE_IMPROVEMENT_ESTIMATE]',
                        'implementation_effort': 'LOW'
                    }
                ])

            elif bottleneck['type'] == 'THROUGHPUT_BOTTLENECK':
                recommendations.extend([
                    {
                        'optimization': 'RESOURCE_SCALING',
                        'description': 'Scale up compute resources',
                        'implementation': self.scale_compute_resources,
                        'expected_improvement': '[SCALING_IMPROVEMENT_ESTIMATE]',
                        'implementation_effort': 'LOW'
                    },
                    {
                        'optimization': 'CACHING_STRATEGY',
                        'description': 'Implement intelligent caching',
                        'implementation': self.implement_caching,
                        'expected_improvement': '[CACHING_IMPROVEMENT_ESTIMATE]',
                        'implementation_effort': 'HIGH'
                    }
                ])

            elif bottleneck['type'] == 'MEMORY_BOTTLENECK':
                recommendations.extend([
                    {
                        'optimization': 'MEMORY_OPTIMIZATION',
                        'description': 'Optimize memory usage patterns',
                        'implementation': self.optimize_memory_usage,
                        'expected_improvement': '[MEMORY_IMPROVEMENT_ESTIMATE]',
                        'implementation_effort': 'MEDIUM'
                    },
                    {
                        'optimization': 'STREAMING_PROCESSING',
                        'description': 'Convert to streaming processing',
                        'implementation': self.convert_to_streaming,
                        'expected_improvement': '[STREAMING_IMPROVEMENT_ESTIMATE]',
                        'implementation_effort': 'HIGH'
                    }
                ])

        # Sort by expected improvement and implementation effort
        recommendations.sort(
            key=lambda x: ([IMPROVEMENT_WEIGHT] * float(x['expected_improvement'][:-1]) -
                          [EFFORT_WEIGHT] * {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}[x['implementation_effort']]),
            reverse=True
        )

        return recommendations

# Batch size optimization algorithm
def optimize_batch_size(current_metrics: dict, target_metrics: dict) -> int:
    """
    Calculate optimal batch size based on performance metrics
    """
    current_batch_size = current_metrics['batch_size']
    current_throughput = current_metrics['throughput']
    current_memory_usage = current_metrics['memory_usage']

    target_throughput = target_metrics['target_throughput']
    max_memory_usage = target_metrics['max_memory_usage']

    # Calculate throughput efficiency
    throughput_ratio = target_throughput / current_throughput

    # Calculate memory constraint
    memory_ratio = max_memory_usage / current_memory_usage

    # Determine optimal batch size
    size_multiplier = min(throughput_ratio, memory_ratio, [MAX_BATCH_SIZE_MULTIPLIER])

    optimal_batch_size = int(current_batch_size * size_multiplier)

    # Apply constraints
    optimal_batch_size = max(optimal_batch_size, [MIN_BATCH_SIZE])
    optimal_batch_size = min(optimal_batch_size, [MAX_BATCH_SIZE])

    return optimal_batch_size

# Resource auto-scaling configuration
AUTOSCALING_CONFIG = {
    'cpu_scale_up_threshold': [CPU_SCALE_UP_THRESHOLD],
    'cpu_scale_down_threshold': [CPU_SCALE_DOWN_THRESHOLD],
    'memory_scale_up_threshold': [MEMORY_SCALE_UP_THRESHOLD],
    'memory_scale_down_threshold': [MEMORY_SCALE_DOWN_THRESHOLD],
    'min_instances': [MIN_INSTANCES],
    'max_instances': [MAX_INSTANCES],
    'scale_up_cooldown': '[SCALE_UP_COOLDOWN]',
    'scale_down_cooldown': '[SCALE_DOWN_COOLDOWN]'
}
```

### DEPLOYMENT AND INFRASTRUCTURE

### Infrastructure as Code (Terraform)
```yaml
# Terraform configuration for pipeline infrastructure
provider "[CLOUD_PROVIDER]" {
  region = "[DEPLOYMENT_REGION]"
}

# Data processing cluster
resource "[CLOUD_PROVIDER]_[COMPUTE_RESOURCE]" "[CLUSTER_NAME]" {
  name               = "[CLUSTER_NAME]"
  [CLUSTER_VERSION]  = "[VERSION]"
  node_count         = [NODE_COUNT]
  node_type          = "[NODE_TYPE]"
  disk_size          = [DISK_SIZE]

  # Auto-scaling configuration
  autoscaling {
    min_size         = [MIN_NODES]
    max_size         = [MAX_NODES]
    target_cpu       = [TARGET_CPU_UTILIZATION]
    target_memory    = [TARGET_MEMORY_UTILIZATION]
  }

  # Network configuration
  vpc_id             = [VPC_ID]
  subnet_ids         = [SUBNET_IDS]
  security_group_ids = [SECURITY_GROUP_IDS]

  tags = {
    Environment = "[ENVIRONMENT]"
    Project     = "[PROJECT_NAME]"
    Owner       = "[TEAM_OWNER]"
  }
}

# Orchestration platform deployment
resource "[CLOUD_PROVIDER]_[ORCHESTRATION_SERVICE]" "[ORCHESTRATION_INSTANCE]" {
  name                = "[ORCHESTRATION_INSTANCE_NAME]"
  service_version     = "[ORCHESTRATION_VERSION]"
  instance_type       = "[ORCHESTRATION_INSTANCE_TYPE]"

  # High availability configuration
  availability_zones  = [AVAILABILITY_ZONES]
  replica_count       = [REPLICA_COUNT]

  # Storage configuration
  storage {
    size              = [STORAGE_SIZE]
    type              = "[STORAGE_TYPE]"
    encryption        = true
  }

  # Networking
  vpc_configuration {
    vpc_id            = [VPC_ID]
    subnet_ids        = [PRIVATE_SUBNET_IDS]
    security_group_id = [ORCHESTRATION_SECURITY_GROUP_ID]
  }

  # Monitoring and logging
  monitoring {
    enabled           = true
    log_level         = "[LOG_LEVEL]"
    metrics_enabled   = true
  }
}

# Data storage resources
resource "[CLOUD_PROVIDER]_[STORAGE_SERVICE]" "[DATA_LAKE_STORAGE]" {
  bucket_name         = "[DATA_LAKE_BUCKET_NAME]"
  storage_class       = "[STORAGE_CLASS]"
  versioning          = true

  # Lifecycle management
  lifecycle_rule {
    name              = "data_archival"
    enabled           = true

    transition {
      days            = [TRANSITION_TO_IA_DAYS]
      storage_class   = "[INFREQUENT_ACCESS_CLASS]"
    }

    transition {
      days            = [TRANSITION_TO_GLACIER_DAYS]
      storage_class   = "[ARCHIVE_CLASS]"
    }

    expiration {
      days            = [EXPIRATION_DAYS]
    }
  }

  # Encryption
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "[ENCRYPTION_ALGORITHM]"
        kms_master_key_id = [KMS_KEY_ID]
      }
    }
  }
}

# Database resources
resource "[CLOUD_PROVIDER]_[DATABASE_SERVICE]" "[DATA_WAREHOUSE]" {
  identifier          = "[DATA_WAREHOUSE_IDENTIFIER]"
  engine              = "[DATABASE_ENGINE]"
  engine_version      = "[DATABASE_VERSION]"
  instance_class      = "[DATABASE_INSTANCE_CLASS]"
  allocated_storage   = [DATABASE_STORAGE_SIZE]

  # High availability
  multi_az            = [MULTI_AZ_ENABLED]
  backup_retention_period = [BACKUP_RETENTION_DAYS]
  backup_window       = "[BACKUP_WINDOW]"
  maintenance_window  = "[MAINTENANCE_WINDOW]"

  # Security
  vpc_security_group_ids = [DATABASE_SECURITY_GROUP_IDS]
  subnet_group_name   = [DATABASE_SUBNET_GROUP]
  encrypted           = true
  kms_key_id          = [DATABASE_KMS_KEY_ID]

  # Performance
  performance_insights_enabled = true
  monitoring_interval = [MONITORING_INTERVAL]
}
```

### Container Orchestration (Kubernetes)
```yaml
# Kubernetes deployment for pipeline components
apiVersion: apps/v1
kind: Deployment
metadata:
  name: [PIPELINE_SERVICE_NAME]
  namespace: [NAMESPACE]
  labels:
    app: [PIPELINE_SERVICE_NAME]
    version: [SERVICE_VERSION]
spec:
  replicas: [REPLICA_COUNT]
  selector:
    matchLabels:
      app: [PIPELINE_SERVICE_NAME]
  template:
    metadata:
      labels:
        app: [PIPELINE_SERVICE_NAME]
        version: [SERVICE_VERSION]
    spec:
      containers:
      - name: [CONTAINER_NAME]
        image: [CONTAINER_IMAGE]:[IMAGE_TAG]
        ports:
        - containerPort: [CONTAINER_PORT]
        env:
        - name: [ENV_VAR_1]
          value: "[ENV_VALUE_1]"
        - name: [ENV_VAR_2]
          valueFrom:
            secretKeyRef:
              name: [SECRET_NAME]
              key: [SECRET_KEY]
        resources:
          requests:
            memory: "[MEMORY_REQUEST]"
            cpu: "[CPU_REQUEST]"
          limits:
            memory: "[MEMORY_LIMIT]"
            cpu: "[CPU_LIMIT]"
        volumeMounts:
        - name: [VOLUME_NAME]
          mountPath: [MOUNT_PATH]
        livenessProbe:
          httpGet:
            path: [HEALTH_CHECK_PATH]
            port: [HEALTH_CHECK_PORT]
          initialDelaySeconds: [LIVENESS_INITIAL_DELAY]
          periodSeconds: [LIVENESS_PERIOD]
        readinessProbe:
          httpGet:
            path: [READINESS_CHECK_PATH]
            port: [READINESS_CHECK_PORT]
          initialDelaySeconds: [READINESS_INITIAL_DELAY]
          periodSeconds: [READINESS_PERIOD]
      volumes:
      - name: [VOLUME_NAME]
        persistentVolumeClaim:
          claimName: [PVC_NAME]

---
apiVersion: v1
kind: Service
metadata:
  name: [SERVICE_NAME]
  namespace: [NAMESPACE]
spec:
  selector:
    app: [PIPELINE_SERVICE_NAME]
  ports:
  - port: [SERVICE_PORT]
    targetPort: [CONTAINER_PORT]
  type: [SERVICE_TYPE]

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: [HPA_NAME]
  namespace: [NAMESPACE]
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: [PIPELINE_SERVICE_NAME]
  minReplicas: [MIN_REPLICAS]
  maxReplicas: [MAX_REPLICAS]
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: [CPU_TARGET_UTILIZATION]
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: [MEMORY_TARGET_UTILIZATION]
```

OUTPUT: Deliver comprehensive infrastructure and performance solution including:
1. Performance analysis and bottleneck identification
2. Optimization recommendations with implementation guidance
3. Batch size and parallelism tuning strategies
4. Auto-scaling configuration for dynamic resource allocation
5. Complete Terraform infrastructure as code templates
6. Kubernetes deployment manifests with best practices
7. Resource allocation and limits configuration
8. High availability and disaster recovery setup
9. Cost optimization through lifecycle policies
10. Monitoring and observability integration
11. Security configurations (encryption, IAM, network policies)
12. CI/CD pipeline integration for infrastructure deployment
```

## Variables

### Core Configuration
[INFRASTRUCTURE_APPROACH], [ORGANIZATION_NAME], [PIPELINE_SCOPE], [PERFORMANCE_OBJECTIVES], [SCALE_REQUIREMENTS], [BUDGET_CONSTRAINTS]

### Architecture Settings
[IAC_STRATEGY], [ORCHESTRATION_STRATEGY], [AUTOSCALING_POLICY], [COST_OPTIMIZATION_STRATEGY], [HA_STRATEGY], [DR_STRATEGY]

### Technical Stack
[CLOUD_PROVIDER], [IAC_TOOL], [CONTAINER_PLATFORM], [CONTAINER_REGISTRY], [COMPUTE_PLATFORM], [STORAGE_SYSTEMS], [NETWORKING_ARCHITECTURE]

### Performance Requirements
[THROUGHPUT_TARGET], [LATENCY_REQUIREMENTS], [CONCURRENCY_LEVEL], [RESOURCE_EFFICIENCY_TARGET], [SCALABILITY_RANGE]

### Performance Optimization
[PERFORMANCE_METRICS_COLLECTOR], [ANALYSIS_TIME_RANGE], [AVG_DURATION_CALCULATION], [P95_DURATION_CALCULATION], [AVG_THROUGHPUT_CALCULATION], [PEAK_CPU_CALCULATION], [PEAK_MEMORY_CALCULATION], [AVG_ERROR_RATE_CALCULATION], [DATA_VOLUME_TREND_CALCULATION]

### Optimization Parameters
[PARALLELIZATION_IMPROVEMENT_ESTIMATE], [BATCH_SIZE_IMPROVEMENT_ESTIMATE], [SCALING_IMPROVEMENT_ESTIMATE], [CACHING_IMPROVEMENT_ESTIMATE], [MEMORY_IMPROVEMENT_ESTIMATE], [STREAMING_IMPROVEMENT_ESTIMATE], [IMPROVEMENT_WEIGHT], [EFFORT_WEIGHT]

### Batch Optimization
[MAX_BATCH_SIZE_MULTIPLIER], [MIN_BATCH_SIZE], [MAX_BATCH_SIZE]

### Auto-scaling
[CPU_SCALE_UP_THRESHOLD], [CPU_SCALE_DOWN_THRESHOLD], [MEMORY_SCALE_UP_THRESHOLD], [MEMORY_SCALE_DOWN_THRESHOLD], [MIN_INSTANCES], [MAX_INSTANCES], [SCALE_UP_COOLDOWN], [SCALE_DOWN_COOLDOWN]

### Terraform Configuration
[DEPLOYMENT_REGION], [COMPUTE_RESOURCE], [CLUSTER_NAME], [VERSION], [NODE_COUNT], [NODE_TYPE], [DISK_SIZE], [MIN_NODES], [MAX_NODES], [TARGET_CPU_UTILIZATION], [TARGET_MEMORY_UTILIZATION], [VPC_ID], [SUBNET_IDS], [SECURITY_GROUP_IDS], [ENVIRONMENT], [PROJECT_NAME], [TEAM_OWNER]

### Orchestration Infrastructure
[ORCHESTRATION_SERVICE], [ORCHESTRATION_INSTANCE], [ORCHESTRATION_INSTANCE_NAME], [ORCHESTRATION_VERSION], [ORCHESTRATION_INSTANCE_TYPE], [AVAILABILITY_ZONES], [REPLICA_COUNT], [STORAGE_SIZE], [STORAGE_TYPE], [PRIVATE_SUBNET_IDS], [ORCHESTRATION_SECURITY_GROUP_ID], [LOG_LEVEL]

### Storage Configuration
[STORAGE_SERVICE], [DATA_LAKE_STORAGE], [DATA_LAKE_BUCKET_NAME], [STORAGE_CLASS], [TRANSITION_TO_IA_DAYS], [INFREQUENT_ACCESS_CLASS], [TRANSITION_TO_GLACIER_DAYS], [ARCHIVE_CLASS], [EXPIRATION_DAYS], [ENCRYPTION_ALGORITHM], [KMS_KEY_ID]

### Database Configuration
[DATABASE_SERVICE], [DATA_WAREHOUSE], [DATA_WAREHOUSE_IDENTIFIER], [DATABASE_ENGINE], [DATABASE_VERSION], [DATABASE_INSTANCE_CLASS], [DATABASE_STORAGE_SIZE], [MULTI_AZ_ENABLED], [BACKUP_RETENTION_DAYS], [BACKUP_WINDOW], [MAINTENANCE_WINDOW], [DATABASE_SECURITY_GROUP_IDS], [DATABASE_SUBNET_GROUP], [DATABASE_KMS_KEY_ID], [MONITORING_INTERVAL]

### Kubernetes Configuration
[PIPELINE_SERVICE_NAME], [NAMESPACE], [SERVICE_VERSION], [CONTAINER_NAME], [CONTAINER_IMAGE], [IMAGE_TAG], [CONTAINER_PORT], [ENV_VAR_1], [ENV_VALUE_1], [ENV_VAR_2], [SECRET_NAME], [SECRET_KEY], [MEMORY_REQUEST], [CPU_REQUEST], [MEMORY_LIMIT], [CPU_LIMIT], [VOLUME_NAME], [MOUNT_PATH], [HEALTH_CHECK_PATH], [HEALTH_CHECK_PORT], [LIVENESS_INITIAL_DELAY], [LIVENESS_PERIOD], [READINESS_CHECK_PATH], [READINESS_CHECK_PORT], [READINESS_INITIAL_DELAY], [READINESS_PERIOD], [PVC_NAME], [SERVICE_NAME], [SERVICE_PORT], [SERVICE_TYPE], [HPA_NAME], [MIN_REPLICAS], [MAX_REPLICAS], [CPU_TARGET_UTILIZATION], [MEMORY_TARGET_UTILIZATION]

## Usage Examples

### Example 1: AWS Data Lake Infrastructure
```
CLOUD_PROVIDER: "AWS"
IAC_TOOL: "Terraform"
INFRASTRUCTURE:
  - EMR cluster (5 m5.2xlarge spot instances, auto-scale 3-10 nodes)
  - S3 data lake (Bronze/Silver/Gold layers with lifecycle policies)
  - RDS PostgreSQL (db.r5.large, Multi-AZ, automated backups)
  - Managed Airflow (MWAA, medium environment)
COST_OPTIMIZATION:
  - Use spot instances for transient workloads (60% cost savings)
  - S3 Intelligent-Tiering for automatic cost optimization
  - RDS reserved instances for predictable workloads
PERFORMANCE: Target 100K records/sec throughput, < 2 hour batch processing
```

### Example 2: Kubernetes-based Pipeline Platform
```
CONTAINER_PLATFORM: "Kubernetes (EKS)"
DEPLOYMENT_STRATEGY: "Blue-green deployments with canary testing"
PIPELINE_SERVICES:
  - Spark jobs: 3-20 replicas (HPA based on queue depth)
  - Airflow workers: 5-15 replicas (HPA based on pending tasks)
  - API services: 2-10 replicas (HPA based on CPU/memory)
RESOURCE_LIMITS:
  - Spark: 4 CPU, 16GB memory per pod
  - Airflow: 2 CPU, 8GB memory per pod
AUTO_SCALING: Scale up when CPU > 70%, scale down when CPU < 30%
HEALTH_CHECKS: Liveness probe every 30s, readiness probe every 10s
```

### Example 3: Performance Optimization for Large-scale ETL
```
BOTTLENECK: "5-hour nightly ETL exceeding 4-hour SLA"
ANALYSIS_RESULTS:
  - CPU: 45% avg (not bottleneck)
  - Memory: 85% peak (potential bottleneck)
  - I/O: High shuffle write (major bottleneck)
OPTIMIZATIONS_APPLIED:
  1. Increased Spark partitions from 200 to 800 (reduced shuffle)
  2. Enabled adaptive query execution (AQE)
  3. Tuned batch size from 100K to 50K rows (reduced memory)
  4. Implemented broadcast joins for small dimension tables
  5. Added caching for repeatedly-accessed intermediate tables
RESULTS: ETL duration reduced from 5h to 2.5h (50% improvement)
```

## Best Practices

1. **Infrastructure as Code** - Version control all infrastructure configurations
2. **Immutable infrastructure** - Replace rather than update infrastructure
3. **Environment parity** - Keep dev/staging/prod environments consistent
4. **Right-sizing** - Monitor and adjust resource allocations regularly
5. **Cost tagging** - Tag all resources for cost attribution and optimization
6. **Security by default** - Enable encryption, least privilege access, network isolation
7. **Automated testing** - Test infrastructure changes before production deployment
8. **Disaster recovery** - Regular backups, multi-region deployments for critical systems
9. **Observability integration** - Build monitoring into infrastructure from the start
10. **Documentation** - Maintain architecture diagrams and runbooks

## Tips for Success

- Use Terraform modules for reusable infrastructure components
- Implement remote state storage with locking (S3 + DynamoDB)
- Use separate Terraform workspaces for different environments
- Enable Terraform state versioning for rollback capability
- Implement pre-commit hooks to validate Terraform syntax
- Use cost estimation tools (Infracost) before applying changes
- Implement policy-as-code (OPA, Sentinel) for governance
- Use container image scanning for security vulnerabilities
- Implement resource quotas in Kubernetes namespaces
- Use Pod Disruption Budgets (PDB) for high availability
- Implement network policies for pod-to-pod communication control
- Use secrets management (AWS Secrets Manager, HashiCorp Vault)
- Configure pod anti-affinity for spreading replicas across nodes
- Use node selectors/taints for workload-specific node pools
- Implement graceful shutdown handlers in containerized applications
- Monitor infrastructure drift with tools like Driftctl
- Use GitOps (ArgoCD, Flux) for Kubernetes deployment automation
- Implement automated scaling based on custom metrics (KEDA)
- Use spot instances for fault-tolerant batch workloads
- Regularly review and optimize cloud costs with FinOps practices
