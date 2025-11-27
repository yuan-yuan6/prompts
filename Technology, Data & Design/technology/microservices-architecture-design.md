---
title: Microservices Architecture Design Framework
category: technology
tags:
- microservices
- distributed-systems
- api-design
- event-driven
use_cases:
- Creating comprehensive framework for designing and implementing microservices architecture
  including service decomposition, api design, communication patterns, data management,
  deployment strategies, and operational considerations for scalable distributed systems.
- Project planning and execution
- Strategy development
last_updated: 2025-11-09
industries:
- finance
- government
- retail
- technology
type: template
difficulty: intermediate
slug: microservices-architecture-design
---

# Microservices Architecture Design Framework

## Purpose
Comprehensive framework for designing and implementing microservices architecture including service decomposition, API design, communication patterns, data management, deployment strategies, and operational considerations for scalable distributed systems.

## Quick Microservices Prompt
Design microservices for [application] with [X services] handling [Y concurrent users], [Z req/sec]. Define: service boundaries (domain-driven), API contracts (REST/gRPC), communication (sync + async via Kafka), database per service, caching (Redis). Infrastructure: Kubernetes, service mesh (Istio), distributed tracing (Jaeger). Target: [99.95%] availability, <[X]ms p99 latency.

## Quick Start

**Need to design microservices architecture quickly?** Use this minimal example:

### Minimal Example
```
Design microservices for OrderManagement with 8 services (user, product, cart, order, payment, inventory, notification, shipping), 50K concurrent users, 1000 req/sec. Use: REST APIs with JWT auth, Kafka for async messaging, PostgreSQL per service, Redis cache, Kubernetes on AWS, Istio service mesh, distributed tracing with Jaeger, 99.95% availability target.
```

### When to Use This
- Decomposing monolithic applications into microservices
- Designing new distributed systems from scratch
- Scaling applications for high availability and performance
- Implementing event-driven architectures

### Basic 3-Step Workflow
1. **Define services** - Domain-driven decomposition, service boundaries, API contracts
2. **Design infrastructure** - Communication patterns, data management, service mesh
3. **Implement operations** - CI/CD pipelines, monitoring, resilience patterns

**Time to complete**: 2-3 weeks for architecture design, 3-6 months for full implementation

---

## Template

Design microservices architecture for [APPLICATION_NAME] with [SERVICE_COUNT] services, [USER_LOAD] concurrent users, [TRANSACTION_VOLUME] transactions/second, achieving [AVAILABILITY_TARGET]% availability, [LATENCY_TARGET]ms latency, [SCALABILITY_FACTOR]x scalability, and [DEPLOYMENT_FREQUENCY] deployment frequency.

### 1. Service Decomposition Strategy

| **Decomposition Method** | **Business Capability** | **Service Boundaries** | **Data Ownership** | **Team Assignment** | **Dependencies** |
|------------------------|----------------------|-------------------|------------------|-------------------|-----------------|
| Domain-Driven Design | [DDD_CAPABILITY] | [DDD_BOUNDARIES] | [DDD_DATA] | [DDD_TEAM] | [DDD_DEPENDENCIES] |
| Business Function | [FUNCTION_CAPABILITY] | [FUNCTION_BOUNDARIES] | [FUNCTION_DATA] | [FUNCTION_TEAM] | [FUNCTION_DEPENDENCIES] |
| Data Partitioning | [DATA_CAPABILITY] | [DATA_BOUNDARIES] | [DATA_OWNERSHIP] | [DATA_TEAM] | [DATA_DEPENDENCIES] |
| User Journey | [JOURNEY_CAPABILITY] | [JOURNEY_BOUNDARIES] | [JOURNEY_DATA] | [JOURNEY_TEAM] | [JOURNEY_DEPENDENCIES] |
| Subdomain Modeling | [SUBDOMAIN_CAPABILITY] | [SUBDOMAIN_BOUNDARIES] | [SUBDOMAIN_DATA] | [SUBDOMAIN_TEAM] | [SUBDOMAIN_DEPENDENCIES] |
| Strangler Pattern | [STRANGLER_CAPABILITY] | [STRANGLER_BOUNDARIES] | [STRANGLER_DATA] | [STRANGLER_TEAM] | [STRANGLER_DEPENDENCIES] |

### 2. Service Communication Patterns

**Inter-Service Communication Framework:**
```
Synchronous Communication:
REST APIs:
- Protocol: [REST_PROTOCOL]
- Data Format: [REST_FORMAT]
- Authentication: [REST_AUTH]
- Rate Limiting: [REST_RATE_LIMIT]
- Timeout Strategy: [REST_TIMEOUT]
- Retry Policy: [REST_RETRY]

gRPC Communication:
- Protocol Buffers: [GRPC_PROTOBUF]
- Service Contracts: [GRPC_CONTRACTS]
- Streaming Support: [GRPC_STREAMING]
- Load Balancing: [GRPC_LOAD_BALANCE]
- Error Handling: [GRPC_ERROR]
- Performance: [GRPC_PERFORMANCE]

### GraphQL Federation
- Schema Design: [GRAPHQL_SCHEMA]
- Resolver Pattern: [GRAPHQL_RESOLVER]
- Federation Gateway: [GRAPHQL_GATEWAY]
- Caching Strategy: [GRAPHQL_CACHE]
- Query Optimization: [GRAPHQL_OPTIMIZE]
- Security Rules: [GRAPHQL_SECURITY]

### Asynchronous Messaging
- Message Broker: [MESSAGE_BROKER]
- Event Streaming: [EVENT_STREAMING]
- Pub/Sub Pattern: [PUBSUB_PATTERN]
- Message Queues: [MESSAGE_QUEUES]
- Dead Letter Queue: [DEAD_LETTER]
- Event Sourcing: [EVENT_SOURCING]
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[APPLICATION_NAME]` | Name of the application | "John Smith" |
| `[SERVICE_COUNT]` | Specify the service count | "10" |
| `[USER_LOAD]` | Specify the user load | "50K concurrent users", "100K peak", "10K sustained" |
| `[TRANSACTION_VOLUME]` | Specify the transaction volume | "1000 TPS", "10K requests/sec", "100K events/min" |
| `[AVAILABILITY_TARGET]` | Target or intended availability | "99.9% SLA", "99.99% critical", "99.95% standard" |
| `[LATENCY_TARGET]` | Target or intended latency | "< 100ms p95", "< 200ms p99", "< 50ms average" |
| `[SCALABILITY_FACTOR]` | Specify the scalability factor | "10x horizontal scaling", "Auto-scale 2-100 pods", "Elastic capacity" |
| `[DEPLOYMENT_FREQUENCY]` | Specify the deployment frequency | "Multiple per day", "Continuous deployment", "Weekly releases" |
| `[DDD_CAPABILITY]` | Specify the ddd capability | "Bounded contexts identified", "Aggregate roots defined", "Domain events modeled" |
| `[DDD_BOUNDARIES]` | Specify the ddd boundaries | "Context mapping complete", "Anti-corruption layers", "Shared kernel minimal" |
| `[DDD_DATA]` | Specify the ddd data | "Each context owns data", "No shared databases", "Event-driven sync" |
| `[DDD_TEAM]` | Specify the ddd team | "Cross-functional teams", "Conway's law alignment", "2-pizza team size" |
| `[DDD_DEPENDENCIES]` | Specify the ddd dependencies | "Upstream/downstream mapped", "Consumer-driven contracts", "API versioning" |
| `[FUNCTION_CAPABILITY]` | Specify the function capability | "Business function mapping", "Single responsibility", "Clear ownership" |
| `[FUNCTION_BOUNDARIES]` | Specify the function boundaries | "Function-aligned services", "API contracts", "Shared nothing" |
| `[FUNCTION_DATA]` | Specify the function data | "Function owns its data", "Local persistence", "Async replication" |
| `[FUNCTION_TEAM]` | Specify the function team | "Function-aligned teams", "Full-stack ownership", "DevOps responsibility" |
| `[FUNCTION_DEPENDENCIES]` | Specify the function dependencies | "Loose coupling", "Event-driven communication", "API gateway" |
| `[DATA_CAPABILITY]` | Specify the data capability | "Data domain identification", "Master data management", "Data products" |
| `[DATA_BOUNDARIES]` | Specify the data boundaries | "Data mesh principles", "Domain data ownership", "Self-serve infrastructure" |
| `[DATA_OWNERSHIP]` | Specify the data ownership | "Domain teams own data", "Data as a product", "Federated governance" |
| `[DATA_TEAM]` | Specify the data team | "Data product owners", "Platform team support", "Domain autonomy" |
| `[DATA_DEPENDENCIES]` | Specify the data dependencies | "Data contracts", "Schema registry", "Event catalog" |
| `[JOURNEY_CAPABILITY]` | Specify the journey capability | "User journey mapping", "Experience-driven decomposition", "Channel alignment" |
| `[JOURNEY_BOUNDARIES]` | Specify the journey boundaries | "Journey-based services", "BFF pattern", "Channel-specific APIs" |
| `[JOURNEY_DATA]` | Specify the journey data | "Journey context data", "Session management", "User preferences" |
| `[JOURNEY_TEAM]` | Specify the journey team | "Journey-aligned squads", "UX ownership", "Full-stack teams" |
| `[JOURNEY_DEPENDENCIES]` | Specify the journey dependencies | "Orchestration services", "Saga patterns", "Process managers" |
| `[SUBDOMAIN_CAPABILITY]` | Specify the subdomain capability | "Core/Supporting/Generic identified", "Strategic classification", "Investment priorities" |
| `[SUBDOMAIN_BOUNDARIES]` | Specify the subdomain boundaries | "Subdomain services", "Integration patterns", "Context translation" |
| `[SUBDOMAIN_DATA]` | Specify the subdomain data | "Subdomain data stores", "Translation layers", "Canonical models" |
| `[SUBDOMAIN_TEAM]` | Specify the subdomain team | "Subdomain ownership", "Buy vs build decisions", "Partner integrations" |
| `[SUBDOMAIN_DEPENDENCIES]` | Specify the subdomain dependencies | "Conformist patterns", "Open host services", "Published language" |
| `[STRANGLER_CAPABILITY]` | Specify the strangler capability | "Legacy function mapping", "Incremental extraction", "Risk-based prioritization" |
| `[STRANGLER_BOUNDARIES]` | Specify the strangler boundaries | "Facade pattern", "Branch by abstraction", "Feature toggles" |
| `[STRANGLER_DATA]` | Specify the strangler data | "Data synchronization", "CDC pipelines", "Dual-write mitigation" |
| `[STRANGLER_TEAM]` | Specify the strangler team | "Migration team", "Legacy expertise", "New tech training" |
| `[STRANGLER_DEPENDENCIES]` | Specify the strangler dependencies | "Proxy routing", "Traffic shifting", "Rollback capability" |
| `[REST_PROTOCOL]` | Specify the rest protocol | "HTTP/1.1 + HTTP/2", "JSON over HTTPS", "OpenAPI 3.0 specs" |
| `[REST_FORMAT]` | Specify the rest format | "JSON primary", "Protocol Buffers optional", "HAL hypermedia" |
| `[REST_AUTH]` | Specify the rest auth | "JWT Bearer tokens", "OAuth 2.0 flows", "API key fallback" |
| `[REST_RATE_LIMIT]` | Specify the rest rate limit | "1000 req/min per client", "Sliding window", "429 with Retry-After" |
| `[REST_TIMEOUT]` | Specify the rest timeout | "30s default", "5s for reads", "60s for writes" |
| `[REST_RETRY]` | Specify the rest retry | "Exponential backoff", "3 retries max", "Idempotency keys" |
| `[GRPC_PROTOBUF]` | Specify the grpc protobuf | "Proto3 syntax", "Well-known types", "Custom options" |
| `[GRPC_CONTRACTS]` | Specify the grpc contracts | "Service definitions", "Versioned protos", "Breaking change policy" |
| `[GRPC_STREAMING]` | Specify the grpc streaming | "Unary + Server streaming", "Bidirectional for real-time", "Deadlines" |
| `[GRPC_LOAD_BALANCE]` | Specify the grpc load balance | "Client-side LB", "xDS protocol", "Envoy integration" |
| `[GRPC_ERROR]` | Specify the grpc error | "Status codes", "Error details", "Retry policies" |
| `[GRPC_PERFORMANCE]` | Specify the grpc performance | "Connection pooling", "Keep-alive", "Compression" |
| `[GRAPHQL_SCHEMA]` | Specify the graphql schema | "Schema-first design", "SDL definitions", "Type system" |
| `[GRAPHQL_RESOLVER]` | Specify the graphql resolver | "Field resolvers", "DataLoader batching", "N+1 prevention" |
| `[GRAPHQL_GATEWAY]` | Specify the graphql gateway | "Apollo Federation", "Schema stitching", "Subgraph composition" |
| `[GRAPHQL_CACHE]` | Specify the graphql cache | "Persisted queries", "Response caching", "CDN integration" |
| `[GRAPHQL_OPTIMIZE]` | Specify the graphql optimize | "Query complexity limits", "Depth limiting", "Cost analysis" |
| `[GRAPHQL_SECURITY]` | Specify the graphql security | "Introspection disabled", "Field-level auth", "Input validation" |
| `[MESSAGE_BROKER]` | Specify the message broker | "Apache Kafka", "RabbitMQ", "Amazon SQS/SNS" |
| `[EVENT_STREAMING]` | Specify the event streaming | "Kafka Streams", "Apache Flink", "Kinesis Data Streams" |
| `[PUBSUB_PATTERN]` | Specify the pubsub pattern | "Topic-based routing", "Fan-out delivery", "Subscription filters" |
| `[MESSAGE_QUEUES]` | Specify the message queues | "Point-to-point queues", "Priority queues", "Delay queues" |
| `[DEAD_LETTER]` | Specify the dead letter | "DLQ per queue/topic", "Automatic routing", "Retry policies" |
| `[EVENT_SOURCING]` | Specify the event sourcing | "Event store (EventStoreDB)", "Append-only log", "Projections" |
| `[GATEWAY_TECH]` | Specify the gateway tech | "Kong Gateway", "AWS API Gateway", "Apigee", "Ambassador" |
| `[GATEWAY_FEATURES]` | Specify the gateway features | "Rate limiting", "Authentication", "Request transformation", "Caching" |
| `[GATEWAY_CONFIG]` | Specify the gateway config | "Declarative config", "GitOps managed", "Environment-specific" |
| `[GATEWAY_SECURITY]` | Specify the gateway security | "OAuth 2.0 / JWT", "API key validation", "mTLS termination", "WAF" |
| `[GATEWAY_SLA]` | Specify the gateway sla | "99.99% availability", "< 10ms latency overhead", "10K RPS capacity" |
| `[MESH_TECH]` | Specify the mesh tech | "Istio", "Linkerd", "Consul Connect", "AWS App Mesh" |
| `[MESH_FEATURES]` | Specify the mesh features | "Traffic management", "Observability", "Security policies", "Resilience" |
| `[MESH_CONFIG]` | Specify the mesh config | "VirtualService", "DestinationRule", "Gateway", "ServiceEntry" |
| `[MESH_SECURITY]` | Specify the mesh security | "mTLS encryption", "AuthorizationPolicy", "PeerAuthentication" |
| `[MESH_SLA]` | Specify the mesh sla | "< 1ms proxy latency", "99.99% control plane", "Zero-downtime upgrades" |
| `[LB_TECH]` | Specify the lb tech | "NGINX", "HAProxy", "AWS ALB/NLB", "Envoy" |
| `[LB_FEATURES]` | Specify the lb features | "Round-robin", "Least connections", "Weighted routing", "Health checks" |
| `[LB_CONFIG]` | Specify the lb config | "Connection limits", "Timeouts", "Keep-alive settings", "SSL termination" |
| `[LB_SECURITY]` | Specify the lb security | "TLS 1.3", "DDoS protection", "IP allowlisting", "WAF integration" |
| `[LB_SLA]` | Specify the lb sla | "99.99% availability", "Million connections/sec", "Sub-ms latency" |
| `[CB_TECH]` | Specify the cb tech | "Resilience4j", "Hystrix (legacy)", "Istio circuit breaker", "Envoy" |
| `[CB_FEATURES]` | Specify the cb features | "Failure threshold", "Half-open state", "Fallback methods", "Bulkhead" |
| `[CB_CONFIG]` | Specify the cb config | "5 failures to open", "30s open duration", "3 calls in half-open" |
| `[CB_SECURITY]` | Specify the cb security | "Secure fallback endpoints", "Error masking", "Audit logging" |
| `[CB_SLA]` | Specify the cb sla | "< 1ms overhead", "Instant state transitions", "Metrics emission" |
| `[REGISTRY_TECH]` | Specify the registry tech | "Kubernetes DNS", "Consul", "Eureka", "etcd" |
| `[REGISTRY_FEATURES]` | Specify the registry features | "Service registration", "Health checking", "DNS resolution", "Load balancing" |
| `[REGISTRY_CONFIG]` | Specify the registry config | "TTL settings", "Health check intervals", "Deregistration policies" |
| `[REGISTRY_SECURITY]` | Specify the registry security | "ACL policies", "TLS communication", "Token authentication" |
| `[REGISTRY_SLA]` | Specify the registry sla | "99.99% availability", "< 100ms registration", "Real-time updates" |
| `[CONFIG_TECH]` | Specify the config tech | "Kubernetes ConfigMaps", "HashiCorp Consul", "Spring Cloud Config", "AWS AppConfig" |
| `[CONFIG_FEATURES]` | Specify the config features | "Centralized config", "Dynamic updates", "Environment-specific", "Versioning" |
| `[CONFIG_CONFIG]` | Specify the config config | "Config hierarchy", "Override rules", "Encryption at rest", "Git backend" |
| `[CONFIG_SECURITY]` | Specify the config security | "Secrets encryption", "RBAC access", "Audit logging", "KMS integration" |
| `[CONFIG_SLA]` | Specify the config sla | "99.99% availability", "< 1s propagation", "Version rollback" |
| `[SERVICE_DATABASE]` | Specify the service database | "PostgreSQL per service", "MongoDB for documents", "Redis for caching" |
| `[DATA_ISOLATION]` | Specify the data isolation | "Separate schemas/databases", "No cross-service queries", "API-only access" |
| `[SCHEMA_MANAGEMENT]` | Specify the schema management | "Flyway migrations", "Liquibase", "Schema registry", "Version control" |
| `[BACKUP_STRATEGY]` | Strategy or approach for backup | "Daily automated backups", "Point-in-time recovery", "Cross-region replication" |
| `[RECOVERY_PLAN]` | Specify the recovery plan | "< 1 hour RTO", "< 15 min RPO", "Automated failover", "Runbooks" |
| `[DATA_MIGRATION]` | Specify the data migration | "Blue-green data migration", "CDC with Debezium", "Dual-write period" |
| `[SHARED_CASES]` | Specify the shared cases | "Reference data only", "Legacy transition", "Read replicas acceptable" |
| `[SCHEMA_SEPARATION]` | Specify the schema separation | "Schema per service", "Logical separation", "Access boundaries" |
| `[ACCESS_CONTROL]` | Specify the access control | "Service-specific credentials", "Least privilege", "Connection pooling" |
| `[TRANSACTION_MGMT]` | Specify the transaction mgmt | "Saga pattern", "Eventual consistency", "Compensating transactions" |
| `[CONFLICT_RESOLUTION]` | Specify the conflict resolution | "Last-writer-wins", "Vector clocks", "CRDTs", "Manual resolution" |
| `[MIGRATION_PATH]` | Specify the migration path | "Strangler pattern", "Database-per-service evolution", "Event sourcing" |
| `[EVENT_STORE]` | Specify the event store | "EventStoreDB", "Apache Kafka", "AWS Kinesis", "PostgreSQL events table" |
| `[EVENT_SCHEMA]` | Specify the event schema | "JSON Schema", "Avro", "Protobuf", "CloudEvents spec" |
| `[PROJECTION_BUILD]` | Specify the projection build | "Read model updates", "Materialized views", "Async projectors" |
| `[SNAPSHOT_STRATEGY]` | Strategy or approach for snapshot | "Every 100 events", "Time-based (daily)", "Size threshold" |
| `[REPLAY_MECHANISM]` | Specify the replay mechanism | "Full stream replay", "Checkpoint-based", "Parallel replay" |
| `[AUDIT_TRAIL]` | Specify the audit trail | "Complete event history", "Immutable log", "Compliance ready" |
| `[COMMAND_MODEL]` | Specify the command model | "Command handlers", "Aggregate roots", "Domain validation" |
| `[QUERY_MODEL]` | Specify the query model | "Denormalized views", "Read optimized", "Multiple projections" |
| `[CQRS_SYNC]` | Specify the cqrs sync | "Event-driven sync", "Eventually consistent", "< 1s typical lag" |
| `[CONSISTENCY_MODEL]` | Specify the consistency model | "Eventual consistency", "Causal consistency", "Strong for commands" |
| `[CQRS_PERFORMANCE]` | Specify the cqrs performance | "Optimized read/write paths", "Horizontal scaling", "Cache-friendly" |
| `[CQRS_COMPLEXITY]` | Specify the cqrs complexity | "Eventual consistency handling", "Multiple models", "Debugging challenges" |
| `[CB_IMPLEMENTATION]` | Specify the cb implementation | "Resilience4j CircuitBreaker", "Istio outlier detection", "Envoy circuit breaker" |
| `[CB_SCENARIOS]` | Specify the cb scenarios | "Service timeout", "Error rate spike", "Downstream unavailable" |
| `[CB_RECOVERY]` | Specify the cb recovery | "< 30s open state", "Gradual traffic restoration", "Health check validation" |
| `[CB_METRICS]` | Specify the cb metrics | "State transitions", "Failure rate", "Slow call rate", "Call outcomes" |
| `[CB_TESTING]` | Specify the cb testing | "Chaos injection", "Load testing", "Failure simulation" |
| `[RETRY_IMPLEMENTATION]` | Specify the retry implementation | "Exponential backoff", "Resilience4j Retry", "Spring Retry" |
| `[RETRY_SCENARIOS]` | Specify the retry scenarios | "Transient failures", "Network timeouts", "Rate limit exceeded" |
| `[RETRY_RECOVERY]` | Specify the retry recovery | "3 retries max", "Exponential delay 100ms-10s", "Idempotent operations" |
| `[RETRY_METRICS]` | Specify the retry metrics | "Retry count", "Success after retry", "Final failure rate" |
| `[RETRY_TESTING]` | Specify the retry testing | "Fault injection", "Latency simulation", "Error rate testing" |
| `[TIMEOUT_IMPLEMENTATION]` | Specify the timeout implementation | "Connection timeout", "Read timeout", "Request deadline" |
| `[TIMEOUT_SCENARIOS]` | Specify the timeout scenarios | "Slow downstream", "Network partition", "Resource exhaustion" |
| `[TIMEOUT_RECOVERY]` | Specify the timeout recovery | "Immediate failover", "Cached response", "Graceful degradation" |
| `[TIMEOUT_METRICS]` | Specify the timeout metrics | "Timeout count", "P95/P99 latency", "SLA violations" |
| `[TIMEOUT_TESTING]` | Specify the timeout testing | "Latency injection", "Network simulation", "Load testing" |
| `[BULKHEAD_IMPLEMENTATION]` | Specify the bulkhead implementation | "Thread pool isolation", "Semaphore limiting", "Connection pool limits" |
| `[BULKHEAD_SCENARIOS]` | Specify the bulkhead scenarios | "Dependency failure isolation", "Noisy neighbor protection", "Resource contention" |
| `[BULKHEAD_RECOVERY]` | Specify the bulkhead recovery | "Isolated failure", "Other services unaffected", "Quick recovery" |
| `[BULKHEAD_METRICS]` | Specify the bulkhead metrics | "Pool utilization", "Rejection rate", "Wait time" |
| `[BULKHEAD_TESTING]` | Specify the bulkhead testing | "Dependency failure", "Load testing", "Resource exhaustion" |
| `[FALLBACK_IMPLEMENTATION]` | Specify the fallback implementation | "Cached response", "Default values", "Alternative service" |
| `[FALLBACK_SCENARIOS]` | Specify the fallback scenarios | "Circuit open", "Timeout exceeded", "Error response" |
| `[FALLBACK_RECOVERY]` | Specify the fallback recovery | "Degraded but functional", "User notified", "Background retry" |
| `[FALLBACK_METRICS]` | Specify the fallback metrics | "Fallback invocation rate", "Fallback success", "User impact" |
| `[FALLBACK_TESTING]` | Specify the fallback testing | "Fallback verification", "Quality of degraded service", "User experience" |
| `[HEALTH_IMPLEMENTATION]` | Specify the health implementation | "Liveness probes", "Readiness probes", "Deep health checks" |
| `[HEALTH_SCENARIOS]` | Specify the health scenarios | "Startup checks", "Dependency validation", "Resource availability" |
| `[HEALTH_RECOVERY]` | Specify the health recovery | "Auto-restart on failure", "Traffic removal", "Self-healing" |
| `[HEALTH_METRICS]` | Specify the health metrics | "Health check latency", "Failure rate", "Recovery time" |
| `[HEALTH_TESTING]` | Specify the health testing | "Health endpoint testing", "Dependency simulation", "Startup testing" |
| `[CONTAINER_CONFIG]` | Specify the container config | "Docker/OCI images", "Multi-stage builds", "Distroless base" |
| `[CONTAINER_LIMITS]` | Specify the container limits | "CPU: 1 core max", "Memory: 2Gi max", "Ephemeral: 10Gi" |
| `[CONTAINER_SCALING]` | Specify the container scaling | "HPA based on CPU/Memory", "Custom metrics scaling", "KEDA event-driven" |
| `[CONTAINER_UPDATE]` | Specify the container update | "Rolling update", "maxSurge: 25%", "maxUnavailable: 0" |
| `[CONTAINER_ROLLBACK]` | Specify the container rollback | "Automatic on failure", "kubectl rollout undo", "Git revert + deploy" |
| `[POD_CONFIG]` | Specify the pod config | "Multi-container pods", "Init containers", "Sidecar pattern" |
| `[POD_LIMITS]` | Specify the pod limits | "Resource quotas", "LimitRange", "QoS class: Guaranteed" |
| `[POD_SCALING]` | Specify the pod scaling | "HPA: 2-100 replicas", "VPA recommendations", "Cluster autoscaler" |
| `[POD_UPDATE]` | Specify the pod update | "RollingUpdate strategy", "PodDisruptionBudget", "Readiness gates" |
| `[POD_ROLLBACK]` | Specify the pod rollback | "ReplicaSet rollback", "Revision history", "Instant switch" |
| `[SERVICE_CONFIG]` | Specify the service config | "ClusterIP default", "Headless for StatefulSet", "Named ports" |
| `[SERVICE_LIMITS]` | Specify the service limits | "Connection limits", "Rate limiting via Istio", "Circuit breakers" |
| `[SERVICE_SCALING]` | Specify the service scaling | "EndpointSlices", "Topology-aware routing", "Multi-cluster" |
| `[SERVICE_UPDATE]` | Specify the service update | "Label selector changes", "Port updates", "Zero-downtime" |
| `[SERVICE_ROLLBACK]` | Specify the service rollback | "Selector revert", "Traffic policy rollback", "DNS propagation" |
| `[INGRESS_CONFIG]` | Specify the ingress config | "NGINX Ingress Controller", "Path-based routing", "TLS termination" |
| `[INGRESS_LIMITS]` | Specify the ingress limits | "Rate limiting annotations", "Connection limits", "Request size limits" |
| `[INGRESS_SCALING]` | Specify the ingress scaling | "HPA for controller", "Multiple replicas", "Zone distribution" |
| `[INGRESS_UPDATE]` | Specify the ingress update | "Blue-green ingress", "Canary annotations", "Traffic splitting" |
| `[INGRESS_ROLLBACK]` | Specify the ingress rollback | "Annotation revert", "Backend switch", "DNS failover" |
| `[NAMESPACE_CONFIG]` | Name of the space config | "John Smith" |
| `[NAMESPACE_LIMITS]` | Name of the space limits | "John Smith" |
| `[NAMESPACE_SCALING]` | Name of the space scaling | "John Smith" |
| `[NAMESPACE_UPDATE]` | Name of the space update | "John Smith" |
| `[NAMESPACE_ROLLBACK]` | Name of the space rollback | "John Smith" |
| `[HELM_CONFIG]` | Specify the helm config | "Chart per service", "Umbrella charts", "GitOps with ArgoCD" |
| `[HELM_LIMITS]` | Specify the helm limits | "Values validation", "Chart testing", "Version constraints" |
| `[HELM_SCALING]` | Specify the helm scaling | "Replica values", "HPA templates", "Resource templates" |
| `[HELM_UPDATE]` | Specify the helm update | "helm upgrade --atomic", "Rollback on failure", "Pre/post hooks" |
| `[HELM_ROLLBACK]` | Specify the helm rollback | "helm rollback", "Revision history", "Automatic on failure" |
| `[OAUTH_IMPLEMENTATION]` | Specify the oauth implementation | "Keycloak/Auth0/Okta", "Authorization code flow", "Client credentials for services" |
| `[JWT_IMPLEMENTATION]` | Specify the jwt implementation | "RS256 signing", "Short-lived access tokens", "Refresh token rotation" |
| `[MTLS_IMPLEMENTATION]` | Specify the mtls implementation | "Istio auto-mTLS", "cert-manager certificates", "SPIFFE workload identity" |
| `[API_KEY_IMPLEMENTATION]` | Specify the api key implementation | "Gateway validation", "Rate limiting per key", "Key rotation policies" |
| `[SERVICE_ACCOUNTS]` | Specify the service accounts | "10" |
| `[TOKEN_ROTATION]` | Specify the token rotation | "Access: 15min expiry", "Refresh: 7 days", "Automatic rotation" |
| `[RBAC_MODEL]` | Specify the rbac model | "Role-based access", "Service-level permissions", "Namespace isolation" |
| `[POLICY_ENGINE]` | Specify the policy engine | "OPA/Gatekeeper", "Istio AuthorizationPolicy", "Custom admission webhooks" |
| `[ATTRIBUTE_BASED]` | Specify the attribute based | "Claims-based authorization", "Context-aware policies", "Dynamic permissions" |
| `[SCOPE_MANAGEMENT]` | Scope or boundaries of management | "OAuth scopes per API", "Fine-grained permissions", "Scope validation" |
| `[PERMISSION_MATRIX]` | Specify the permission matrix | "Role-permission mapping", "Resource-action matrix", "Audit trail" |
| `[AUDIT_LOGGING]` | Specify the audit logging | "All auth events logged", "Request/response logging", "Compliance retention" |
| `[NETWORK_POLICIES]` | Specify the network policies | "Calico/Cilium policies", "Default deny all", "Namespace isolation" |
| `[FIREWALL_RULES]` | Specify the firewall rules | "Ingress/egress rules", "Port restrictions", "IP allowlisting" |
| `[VPC_CONFIG]` | Specify the vpc config | "Private subnets", "NAT gateway", "VPC peering", "Transit gateway" |
| `[SECURITY_GROUPS]` | Specify the security groups | "Service-specific SGs", "Least privilege", "Micro-segmentation" |
| `[SSL_TERMINATION]` | Specify the ssl termination | "ALB/Ingress termination", "TLS 1.3 minimum", "cert-manager automation" |
| `[ENCRYPTION_REST]` | Specify the encryption rest | "AES-256 encryption", "KMS managed keys", "Database encryption" |
| `[ENCRYPTION_TRANSIT]` | Specify the encryption transit | "TLS everywhere", "mTLS between services", "Encrypted message queues" |
| `[KEY_MANAGEMENT]` | Specify the key management | "AWS KMS / HashiCorp Vault", "Key rotation policies", "HSM for sensitive" |
| `[DATA_MASKING]` | Specify the data masking | "PII field masking", "Log sanitization", "Dynamic masking" |
| `[PII_HANDLING]` | Specify the pii handling | "Data classification", "Access controls", "GDPR/CCPA compliance" |
| `[COMPLIANCE_CONTROLS]` | Specify the compliance controls | "SOC 2 controls", "PCI-DSS for payments", "HIPAA for health data" |
| `[TRACING_TOOLS]` | Specify the tracing tools | "Jaeger", "Zipkin", "AWS X-Ray", "Datadog APM" |
| `[TRACING_METRICS]` | Specify the tracing metrics | "Trace duration", "Span count", "Error traces", "Service dependencies" |
| `[TRACING_ALERTS]` | Specify the tracing alerts | "High latency spans", "Error rate spikes", "Missing traces" |
| `[TRACING_DASHBOARDS]` | Specify the tracing dashboards | "Service map", "Trace search", "Latency distribution", "Error analysis" |
| `[TRACING_RETENTION]` | Specify the tracing retention | "7 days detailed", "30 days aggregated", "Sampling for long-term" |
| `[METRICS_TOOLS]` | Specify the metrics tools | "Prometheus", "Datadog", "CloudWatch", "Grafana" |
| `[METRICS_COLLECTED]` | Specify the metrics collected | "RED metrics", "Golden signals", "Custom business metrics" |
| `[METRICS_ALERTS]` | Specify the metrics alerts | "SLO violations", "Error rate thresholds", "Latency percentiles" |
| `[METRICS_DASHBOARDS]` | Specify the metrics dashboards | "Service overview", "Golden signals", "SLO tracking", "Cost metrics" |
| `[METRICS_RETENTION]` | Specify the metrics retention | "15 days raw", "1 year downsampled", "Thanos long-term" |
| `[LOG_TOOLS]` | Specify the log tools | "Loki", "Elasticsearch", "CloudWatch Logs", "Splunk" |
| `[LOG_METRICS]` | Specify the log metrics | "Log volume", "Error log rate", "Warning patterns", "Audit events" |
| `[LOG_ALERTS]` | Specify the log alerts | "Error log spikes", "Security events", "Pattern matching alerts" |
| `[LOG_DASHBOARDS]` | Specify the log dashboards | "Log explorer", "Error aggregation", "Security audit", "Request tracing" |
| `[LOG_RETENTION]` | Specify the log retention | "30 days hot", "90 days warm", "1 year cold/archive" |
| `[APM_TOOLS]` | Specify the apm tools | "Datadog APM", "New Relic", "Dynatrace", "Elastic APM" |
| `[APM_METRICS]` | Specify the apm metrics | "Transaction times", "Error rates", "Apdex scores", "Throughput" |
| `[APM_ALERTS]` | Specify the apm alerts | "Apdex degradation", "Error rate increase", "Throughput drop" |
| `[APM_DASHBOARDS]` | Specify the apm dashboards | "Service performance", "Transaction breakdown", "Error analysis" |
| `[APM_RETENTION]` | Specify the apm retention | "14 days full traces", "90 days metrics", "Custom retention" |
| `[HEALTH_TOOLS]` | Specify the health tools | "Kubernetes probes", "Synthetic monitoring", "Uptime monitoring" |
| `[HEALTH_ALERTS]` | Specify the health alerts | "Service down", "High latency", "Dependency failures" |
| `[HEALTH_DASHBOARDS]` | Specify the health dashboards | "Service status", "Dependency health", "SLA tracking" |
| `[HEALTH_RETENTION]` | Specify the health retention | "30 days detailed", "1 year availability data" |
| `[BUSINESS_TOOLS]` | Specify the business tools | "Mixpanel", "Amplitude", "Custom analytics", "Looker" |
| `[BUSINESS_METRICS]` | Specify the business metrics | "Conversion rate", "Revenue metrics", "User engagement", "Funnel analytics" |
| `[BUSINESS_ALERTS]` | Specify the business alerts | "Revenue drop", "Conversion decline", "User churn spike" |
| `[BUSINESS_DASHBOARDS]` | Specify the business dashboards | "KPI overview", "Revenue tracking", "User analytics", "Funnel views" |
| `[BUSINESS_RETENTION]` | Specify the business retention | "90 days detailed", "Years for aggregates", "Compliance requirements" |
| `[UNIT_TOOLS]` | Specify the unit tools | "Jest", "JUnit 5", "pytest", "xUnit", "Mocha/Chai", "Go testing" |
| `[UNIT_COVERAGE]` | Specify the unit coverage | "80% minimum line coverage", "90% branch coverage", "100% critical paths" |
| `[UNIT_FREQUENCY]` | Specify the unit frequency | "Every commit", "Pre-push hook", "CI pipeline trigger" |
| `[UNIT_ENV]` | Specify the unit env | "Local developer machine", "CI container", "Isolated test runner" |
| `[UNIT_CRITERIA]` | Specify the unit criteria | "All tests pass", "Coverage threshold met", "No regressions", "Fast execution <5min" |
| `[INTEGRATION_TOOLS]` | Specify the integration tools | "Testcontainers", "Docker Compose", "WireMock", "LocalStack", "MockServer" |
| `[INTEGRATION_COVERAGE]` | Specify the integration coverage | "All service boundaries", "Database interactions", "API contracts", "Message queues" |
| `[INTEGRATION_FREQUENCY]` | Specify the integration frequency | "PR merge", "Nightly builds", "Pre-deployment", "Scheduled regression" |
| `[INTEGRATION_ENV]` | Specify the integration env | "Docker Compose stack", "Kubernetes namespace", "Ephemeral test cluster" |
| `[INTEGRATION_CRITERIA]` | Specify the integration criteria | "All integrations pass", "No timeout failures", "Database rollback clean" |
| `[CONTRACT_TOOLS]` | Specify the contract tools | "Pact", "Spring Cloud Contract", "Dredd", "Prism", "Specmatic" |
| `[CONTRACT_COVERAGE]` | Specify the contract coverage | "All consumer-provider pairs", "API endpoints", "Event schemas", "Message formats" |
| `[CONTRACT_FREQUENCY]` | Specify the contract frequency | "Every PR", "Provider deploy", "Consumer update", "Weekly full suite" |
| `[CONTRACT_ENV]` | Specify the contract env | "Pact Broker", "Contract registry", "CI pipeline with broker integration" |
| `[CONTRACT_CRITERIA]` | Specify the contract criteria | "No breaking changes", "Backward compatibility", "Schema validation pass" |
| `[E2E_TOOLS]` | Specify the e2e tools | "Cypress", "Playwright", "Selenium", "k6", "Postman/Newman", "Karate" |
| `[E2E_COVERAGE]` | Specify the e2e coverage | "Critical user journeys", "Business workflows", "Cross-service scenarios" |
| `[E2E_FREQUENCY]` | Specify the e2e frequency | "Pre-production deploy", "Nightly on staging", "Post-release smoke" |
| `[E2E_ENV]` | Specify the e2e env | "Staging environment", "Pre-production replica", "Isolated E2E cluster" |
| `[E2E_CRITERIA]` | Specify the e2e criteria | "All journeys pass", "Response times within SLA", "No data corruption" |
| `[PERF_TOOLS]` | Specify the perf tools | "k6", "Gatling", "JMeter", "Locust", "Artillery", "wrk" |
| `[PERF_COVERAGE]` | Specify the perf coverage | "Critical APIs", "High-traffic endpoints", "Database queries", "Async processing" |
| `[PERF_FREQUENCY]` | Specify the perf frequency | "Weekly baseline", "Pre-release load test", "Monthly stress test" |
| `[PERF_ENV]` | Specify the perf env | "Production-like environment", "Scaled-down replica", "Dedicated perf cluster" |
| `[PERF_CRITERIA]` | Specify the perf criteria | "p95 latency <200ms", "Throughput >1000 RPS", "Error rate <0.1%", "No memory leaks" |
| `[CHAOS_TOOLS]` | Specify the chaos tools | "Chaos Monkey", "Litmus", "Gremlin", "Chaos Mesh", "AWS Fault Injection Simulator" |
| `[CHAOS_COVERAGE]` | Specify the chaos coverage | "Service failures", "Network partitions", "Resource exhaustion", "Dependency outages" |
| `[CHAOS_FREQUENCY]` | Specify the chaos frequency | "Monthly game days", "Weekly automated experiments", "Post-incident validation" |
| `[CHAOS_ENV]` | Specify the chaos env | "Staging with blast radius", "Production canary", "Isolated chaos namespace" |
| `[CHAOS_CRITERIA]` | Specify the chaos criteria | "Graceful degradation", "Auto-recovery", "Alert triggers", "No cascading failures" |
| `[CURRENT_STATE]` | Specify the current state | "Monolithic application", "Tightly coupled modules", "Shared database", "Legacy stack" |
| `[SERVICE_IDENTIFICATION]` | Specify the service identification | "Domain-driven design", "Business capability mapping", "Bounded context analysis" |
| `[DEPENDENCY_MAPPING]` | Specify the dependency mapping | "Service dependency graph", "Data flow analysis", "API call matrix", "Database coupling audit" |
| `[RISK_ASSESSMENT]` | Specify the risk assessment | "High/Medium/Low classification", "Impact analysis", "Mitigation strategies", "Contingency plans" |
| `[RESOURCE_PLANNING]` | Specify the resource planning | "Team allocation", "Skill gap analysis", "Training needs", "Infrastructure budget" |
| `[TIMELINE_DEFINITION]` | Timeline or schedule for definition | "6 months", "12-18 month phased approach", "Quarterly milestones" |
| `[PILOT_SELECTION]` | Specify the pilot selection | "Low-risk service", "Well-defined boundaries", "Minimal dependencies", "High business value" |
| `[PILOT_IMPLEMENTATION]` | Specify the pilot implementation | "Extract and refactor", "API-first approach", "Database separation", "CI/CD setup" |
| `[PILOT_TESTING]` | Specify the pilot testing | "Parallel running", "Shadow traffic", "A/B comparison", "Load testing" |
| `[PILOT_ROLLOUT]` | Specify the pilot rollout | "Canary deployment", "Feature flag controlled", "Gradual traffic shift" |
| `[PILOT_METRICS]` | Specify the pilot metrics | "Latency comparison", "Error rates", "Resource utilization", "Developer velocity" |
| `[PILOT_LESSONS]` | Specify the pilot lessons | "Retrospective findings", "Process improvements", "Tool adjustments", "Pattern refinements" |
| `[MIGRATION_ORDER]` | Specify the migration order | "Dependency-based ordering", "Risk-adjusted priority", "Business value ranking" |
| `[STRANGLER_PATTERN]` | Specify the strangler pattern | "Facade layer", "Route-based switching", "Incremental replacement", "Feature-by-feature migration" |
| `[DATA_MIGRATION_PLAN]` | Specify the data migration plan | "Dual-write period", "Change data capture", "Bulk migration + sync", "Schema versioning" |
| `[CUTOVER_STRATEGY]` | Strategy or approach for cutover | "Big bang with rollback", "Blue-green switch", "Gradual traffic shift", "Feature flag flip" |
| `[ROLLBACK_PROCEDURES]` | Specify the rollback procedures | "DNS failback", "Traffic reroute", "Database restore point", "Feature flag disable" |
| `[PROGRESS_TRACKING]` | Specify the progress tracking | "Migration dashboard", "Service scorecards", "Burndown charts", "Weekly status reports" |
| `[PERFORMANCE_TUNING]` | Specify the performance tuning | "Query optimization", "Caching implementation", "Connection pooling", "Resource right-sizing" |
| `[COST_OPTIMIZATION]` | Specify the cost optimization | "Right-sizing instances", "Reserved capacity", "Spot instances for batch", "Storage tiering" |
| `[ARCHITECTURE_REFINE]` | Specify the architecture refine | "Service boundary adjustments", "API versioning strategy", "Event schema evolution" |
| `[AUTOMATION_ENHANCE]` | Specify the automation enhance | "CI/CD pipeline improvements", "IaC templates", "Auto-scaling policies", "Self-healing scripts" |
| `[DOCUMENTATION_UPDATE]` | Specify the documentation update | "Architecture decision records", "Runbooks", "API documentation", "Onboarding guides" |
| `[KNOWLEDGE_TRANSFER]` | Specify the knowledge transfer | "Tech talks", "Pair programming", "Documentation sessions", "Brown bag lunches" |

### 3. API Gateway & Service Mesh

| **Component** | **Technology Choice** | **Features** | **Configuration** | **Security Policies** | **Performance SLA** |
|-------------|---------------------|------------|-----------------|---------------------|-------------------|
| API Gateway | [GATEWAY_TECH] | [GATEWAY_FEATURES] | [GATEWAY_CONFIG] | [GATEWAY_SECURITY] | [GATEWAY_SLA] |
| Service Mesh | [MESH_TECH] | [MESH_FEATURES] | [MESH_CONFIG] | [MESH_SECURITY] | [MESH_SLA] |
| Load Balancer | [LB_TECH] | [LB_FEATURES] | [LB_CONFIG] | [LB_SECURITY] | [LB_SLA] |
| Circuit Breaker | [CB_TECH] | [CB_FEATURES] | [CB_CONFIG] | [CB_SECURITY] | [CB_SLA] |
| Service Registry | [REGISTRY_TECH] | [REGISTRY_FEATURES] | [REGISTRY_CONFIG] | [REGISTRY_SECURITY] | [REGISTRY_SLA] |
| Config Server | [CONFIG_TECH] | [CONFIG_FEATURES] | [CONFIG_CONFIG] | [CONFIG_SECURITY] | [CONFIG_SLA] |

### 4. Data Management Strategy

```
Data Architecture Patterns:
Database per Service:
- Service Database: [SERVICE_DATABASE]
- Data Isolation: [DATA_ISOLATION]
- Schema Management: [SCHEMA_MANAGEMENT]
- Backup Strategy: [BACKUP_STRATEGY]
- Recovery Plan: [RECOVERY_PLAN]
- Data Migration: [DATA_MIGRATION]

Shared Database:
- Anti-Pattern Cases: [SHARED_CASES]
- Schema Separation: [SCHEMA_SEPARATION]
- Access Control: [ACCESS_CONTROL]
- Transaction Management: [TRANSACTION_MGMT]
- Conflict Resolution: [CONFLICT_RESOLUTION]
- Migration Path: [MIGRATION_PATH]

### Event Sourcing
- Event Store: [EVENT_STORE]
- Event Schema: [EVENT_SCHEMA]
- Projection Building: [PROJECTION_BUILD]
- Snapshot Strategy: [SNAPSHOT_STRATEGY]
- Replay Mechanism: [REPLAY_MECHANISM]
- Audit Trail: [AUDIT_TRAIL]

### CQRS Implementation
- Command Model: [COMMAND_MODEL]
- Query Model: [QUERY_MODEL]
- Synchronization: [CQRS_SYNC]
- Consistency Model: [CONSISTENCY_MODEL]
- Performance Optimization: [CQRS_PERFORMANCE]
- Complexity Management: [CQRS_COMPLEXITY]
```

### 5. Service Resilience & Fault Tolerance

| **Resilience Pattern** | **Implementation** | **Failure Scenarios** | **Recovery Time** | **Monitoring Metrics** | **Testing Strategy** |
|----------------------|------------------|--------------------|-----------------|--------------------|-------------------|
| Circuit Breaker | [CB_IMPLEMENTATION] | [CB_SCENARIOS] | [CB_RECOVERY] | [CB_METRICS] | [CB_TESTING] |
| Retry Logic | [RETRY_IMPLEMENTATION] | [RETRY_SCENARIOS] | [RETRY_RECOVERY] | [RETRY_METRICS] | [RETRY_TESTING] |
| Timeout Handling | [TIMEOUT_IMPLEMENTATION] | [TIMEOUT_SCENARIOS] | [TIMEOUT_RECOVERY] | [TIMEOUT_METRICS] | [TIMEOUT_TESTING] |
| Bulkhead Pattern | [BULKHEAD_IMPLEMENTATION] | [BULKHEAD_SCENARIOS] | [BULKHEAD_RECOVERY] | [BULKHEAD_METRICS] | [BULKHEAD_TESTING] |
| Fallback Methods | [FALLBACK_IMPLEMENTATION] | [FALLBACK_SCENARIOS] | [FALLBACK_RECOVERY] | [FALLBACK_METRICS] | [FALLBACK_TESTING] |
| Health Checks | [HEALTH_IMPLEMENTATION] | [HEALTH_SCENARIOS] | [HEALTH_RECOVERY] | [HEALTH_METRICS] | [HEALTH_TESTING] |

### 6. Container Orchestration & Deployment

**Kubernetes Deployment Strategy:**
| **Deployment Aspect** | **Configuration** | **Resource Limits** | **Scaling Policy** | **Update Strategy** | **Rollback Plan** |
|---------------------|-----------------|-------------------|------------------|-------------------|-----------------|
| Container Specs | [CONTAINER_CONFIG] | [CONTAINER_LIMITS] | [CONTAINER_SCALING] | [CONTAINER_UPDATE] | [CONTAINER_ROLLBACK] |
| Pod Configuration | [POD_CONFIG] | [POD_LIMITS] | [POD_SCALING] | [POD_UPDATE] | [POD_ROLLBACK] |
| Service Definition | [SERVICE_CONFIG] | [SERVICE_LIMITS] | [SERVICE_SCALING] | [SERVICE_UPDATE] | [SERVICE_ROLLBACK] |
| Ingress Rules | [INGRESS_CONFIG] | [INGRESS_LIMITS] | [INGRESS_SCALING] | [INGRESS_UPDATE] | [INGRESS_ROLLBACK] |
| Namespace Strategy | [NAMESPACE_CONFIG] | [NAMESPACE_LIMITS] | [NAMESPACE_SCALING] | [NAMESPACE_UPDATE] | [NAMESPACE_ROLLBACK] |
| Helm Charts | [HELM_CONFIG] | [HELM_LIMITS] | [HELM_SCALING] | [HELM_UPDATE] | [HELM_ROLLBACK] |

### 7. Security Architecture

```
Security Implementation:
Service Authentication:
- OAuth 2.0: [OAUTH_IMPLEMENTATION]
- JWT Tokens: [JWT_IMPLEMENTATION]
- mTLS: [MTLS_IMPLEMENTATION]
- API Keys: [API_KEY_IMPLEMENTATION]
- Service Accounts: [SERVICE_ACCOUNTS]
- Token Rotation: [TOKEN_ROTATION]

Authorization Framework:
- RBAC Model: [RBAC_MODEL]
- Policy Engine: [POLICY_ENGINE]
- Attribute-Based: [ATTRIBUTE_BASED]
- Scope Management: [SCOPE_MANAGEMENT]
- Permission Matrix: [PERMISSION_MATRIX]
- Audit Logging: [AUDIT_LOGGING]

### Network Security
- Service Mesh Security: [MESH_SECURITY]
- Network Policies: [NETWORK_POLICIES]
- Firewall Rules: [FIREWALL_RULES]
- VPC Configuration: [VPC_CONFIG]
- Security Groups: [SECURITY_GROUPS]
- SSL/TLS Termination: [SSL_TERMINATION]

### Data Protection
- Encryption at Rest: [ENCRYPTION_REST]
- Encryption in Transit: [ENCRYPTION_TRANSIT]
- Key Management: [KEY_MANAGEMENT]
- Data Masking: [DATA_MASKING]
- PII Handling: [PII_HANDLING]
- Compliance Controls: [COMPLIANCE_CONTROLS]
```

### 8. Monitoring & Observability

| **Observability Pillar** | **Tools & Technologies** | **Metrics Collected** | **Alert Thresholds** | **Dashboard Views** | **Retention Policy** |
|------------------------|----------------------|--------------------|--------------------|-------------------|-------------------|
| Distributed Tracing | [TRACING_TOOLS] | [TRACING_METRICS] | [TRACING_ALERTS] | [TRACING_DASHBOARDS] | [TRACING_RETENTION] |
| Metrics Collection | [METRICS_TOOLS] | [METRICS_COLLECTED] | [METRICS_ALERTS] | [METRICS_DASHBOARDS] | [METRICS_RETENTION] |
| Log Aggregation | [LOG_TOOLS] | [LOG_METRICS] | [LOG_ALERTS] | [LOG_DASHBOARDS] | [LOG_RETENTION] |
| APM Integration | [APM_TOOLS] | [APM_METRICS] | [APM_ALERTS] | [APM_DASHBOARDS] | [APM_RETENTION] |
| Service Health | [HEALTH_TOOLS] | [HEALTH_METRICS] | [HEALTH_ALERTS] | [HEALTH_DASHBOARDS] | [HEALTH_RETENTION] |
| Business Metrics | [BUSINESS_TOOLS] | [BUSINESS_METRICS] | [BUSINESS_ALERTS] | [BUSINESS_DASHBOARDS] | [BUSINESS_RETENTION] |

### 9. Testing Strategy

**Testing Framework:**
| **Test Type** | **Tools Used** | **Coverage Target** | **Execution Frequency** | **Environment** | **Success Criteria** |
|-------------|-------------|-------------------|----------------------|---------------|-------------------|
| Unit Testing | [UNIT_TOOLS] | [UNIT_COVERAGE]% | [UNIT_FREQUENCY] | [UNIT_ENV] | [UNIT_CRITERIA] |
| Integration Testing | [INTEGRATION_TOOLS] | [INTEGRATION_COVERAGE]% | [INTEGRATION_FREQUENCY] | [INTEGRATION_ENV] | [INTEGRATION_CRITERIA] |
| Contract Testing | [CONTRACT_TOOLS] | [CONTRACT_COVERAGE]% | [CONTRACT_FREQUENCY] | [CONTRACT_ENV] | [CONTRACT_CRITERIA] |
| End-to-End Testing | [E2E_TOOLS] | [E2E_COVERAGE]% | [E2E_FREQUENCY] | [E2E_ENV] | [E2E_CRITERIA] |
| Performance Testing | [PERF_TOOLS] | [PERF_COVERAGE]% | [PERF_FREQUENCY] | [PERF_ENV] | [PERF_CRITERIA] |
| Chaos Engineering | [CHAOS_TOOLS] | [CHAOS_COVERAGE]% | [CHAOS_FREQUENCY] | [CHAOS_ENV] | [CHAOS_CRITERIA] |

### 10. Migration & Evolution Strategy

```
Migration Roadmap:
Phase 1 - Assessment:
- Current State Analysis: [CURRENT_STATE]
- Service Identification: [SERVICE_IDENTIFICATION]
- Dependency Mapping: [DEPENDENCY_MAPPING]
- Risk Assessment: [RISK_ASSESSMENT]
- Resource Planning: [RESOURCE_PLANNING]
- Timeline Definition: [TIMELINE_DEFINITION]

Phase 2 - Pilot Services:
- Service Selection: [PILOT_SELECTION]
- Implementation Approach: [PILOT_IMPLEMENTATION]
- Testing Strategy: [PILOT_TESTING]
- Rollout Plan: [PILOT_ROLLOUT]
- Success Metrics: [PILOT_METRICS]
- Lessons Learned: [PILOT_LESSONS]

Phase 3 - Incremental Migration:
- Migration Order: [MIGRATION_ORDER]
- Strangler Pattern: [STRANGLER_PATTERN]
- Data Migration: [DATA_MIGRATION_PLAN]
- Cutover Strategy: [CUTOVER_STRATEGY]
- Rollback Procedures: [ROLLBACK_PROCEDURES]
- Progress Tracking: [PROGRESS_TRACKING]

Phase 4 - Optimization:
- Performance Tuning: [PERFORMANCE_TUNING]
- Cost Optimization: [COST_OPTIMIZATION]
- Architecture Refinement: [ARCHITECTURE_REFINE]
- Automation Enhancement: [AUTOMATION_ENHANCE]
- Documentation Update: [DOCUMENTATION_UPDATE]
- Knowledge Transfer: [KNOWLEDGE_TRANSFER]
```

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: E-commerce Platform
```
Application: Online marketplace
Services: 25 microservices
Architecture: Event-driven with CQRS
Technologies: Spring Boot, Kafka, PostgreSQL
Deployment: Kubernetes on AWS
Scale: 100K concurrent users
Results: 99.99% availability, 50ms p99 latency
```

### Example 2: Financial Services
```
System: Banking platform
Services: 40 microservices
Communication: gRPC with service mesh
Data Strategy: Event sourcing
Infrastructure: OpenShift on-premise
Compliance: PCI-DSS, SOC2
Outcome: 10x transaction throughput
```

### Example 3: Media Streaming
```
Platform: Video streaming service
Architecture: 60+ microservices
Pattern: API Gateway with GraphQL
Deployment: Multi-region Kubernetes
Scale: 1M concurrent streams
Performance: <100ms API response time
Success: 40% infrastructure cost reduction
```

## Customization Options

### 1. Application Type
- Web Applications
- Mobile Backends
- IoT Platforms
- Real-time Systems
- Batch Processing

### 2. Scale Requirements
- Small (<10 services)
- Medium (10-50 services)
- Large (50-100 services)
- Enterprise (100+ services)
- Hyperscale

### 3. Deployment Model
- Public Cloud
- Private Cloud
- Hybrid Cloud
- On-Premise
- Multi-Cloud

### 4. Technology Stack
- Java/Spring
- .NET Core
- Node.js
- Python
- Go

### 5. Industry Requirements
- Financial Services
- Healthcare
- E-commerce
- Telecommunications
- Government