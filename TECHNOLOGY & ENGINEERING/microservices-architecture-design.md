# Microservices Architecture Design Framework

## Purpose
Comprehensive framework for designing and implementing microservices architecture including service decomposition, API design, communication patterns, data management, deployment strategies, and operational considerations for scalable distributed systems.

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

GraphQL Federation:
- Schema Design: [GRAPHQL_SCHEMA]
- Resolver Pattern: [GRAPHQL_RESOLVER]
- Federation Gateway: [GRAPHQL_GATEWAY]
- Caching Strategy: [GRAPHQL_CACHE]
- Query Optimization: [GRAPHQL_OPTIMIZE]
- Security Rules: [GRAPHQL_SECURITY]

Asynchronous Messaging:
- Message Broker: [MESSAGE_BROKER]
- Event Streaming: [EVENT_STREAMING]
- Pub/Sub Pattern: [PUBSUB_PATTERN]
- Message Queues: [MESSAGE_QUEUES]
- Dead Letter Queue: [DEAD_LETTER]
- Event Sourcing: [EVENT_SOURCING]
```

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

Event Sourcing:
- Event Store: [EVENT_STORE]
- Event Schema: [EVENT_SCHEMA]
- Projection Building: [PROJECTION_BUILD]
- Snapshot Strategy: [SNAPSHOT_STRATEGY]
- Replay Mechanism: [REPLAY_MECHANISM]
- Audit Trail: [AUDIT_TRAIL]

CQRS Implementation:
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

Network Security:
- Service Mesh Security: [MESH_SECURITY]
- Network Policies: [NETWORK_POLICIES]
- Firewall Rules: [FIREWALL_RULES]
- VPC Configuration: [VPC_CONFIG]
- Security Groups: [SECURITY_GROUPS]
- SSL/TLS Termination: [SSL_TERMINATION]

Data Protection:
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