---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- communication
- design
- security
title: Architecture Design Template
use_cases:
- Creating design comprehensive system architectures including distributed systems,
  apis, databases, microservices, and enterprise solutions with scalability, security,
  and maintainability considerations.
- Project planning and execution
- Strategy development
industries:
- finance
- government
- healthcare
- retail
- technology
type: template
difficulty: intermediate
slug: architecture-design
---

# Architecture Design Template

## Purpose
Design comprehensive system architectures including distributed systems, APIs, databases, microservices, and enterprise solutions with scalability, security, and maintainability considerations.

## Quick Start

**Need to design system architecture quickly?** Use this minimal example:

### Minimal Example
```
Design architecture for an e-commerce platform handling 100K daily orders. Requirements: microservices for catalog, cart, checkout, payments; PostgreSQL for transactional data; Redis for sessions; Elasticsearch for search; message queue for order processing; RESTful APIs; support 10K concurrent users with 99.9% uptime.
```

### When to Use This
- Designing new systems or applications from scratch
- Refactoring monolithic applications to microservices
- Planning scalability and high-availability architectures
- Creating technical specifications for development teams

### Basic 3-Step Workflow
1. **Define requirements** - Functional, non-functional, constraints, scale
2. **Design components** - Services, databases, APIs, integrations
3. **Document decisions** - Architecture diagrams, trade-offs, rationale

**Time to complete**: 1-2 days for initial design, 3-5 days for detailed architecture

---

## Template Structure

### System Overview
- **System Name**: [SYSTEM_NAME]
- **System Purpose**: [SYSTEM_PURPOSE]
- **Business Domain**: [BUSINESS_DOMAIN]
- **Target Users**: [TARGET_USERS]
- **Expected Load**: [EXPECTED_LOAD]
- **Geographic Distribution**: [GEOGRAPHIC_DISTRIBUTION]
- **Regulatory Requirements**: [REGULATORY_REQUIREMENTS]
- **Budget Constraints**: [BUDGET_CONSTRAINTS]
- **Timeline**: [TIMELINE]
- **Success Metrics**: [SUCCESS_METRICS]

### Architecture Patterns
- **Primary Pattern**: [PRIMARY_PATTERN]
- **Secondary Patterns**: [SECONDARY_PATTERNS]
- **Design Principles**: [DESIGN_PRINCIPLES]
- **Architecture Style**: [ARCHITECTURE_STYLE]
- **Communication Pattern**: [COMMUNICATION_PATTERN]
- **Data Flow Pattern**: [DATA_FLOW_PATTERN]
- **Integration Pattern**: [INTEGRATION_PATTERN]
- **Deployment Pattern**: [DEPLOYMENT_PATTERN]
- **Security Pattern**: [SECURITY_PATTERN]
- **Resilience Pattern**: [RESILIENCE_PATTERN]

### System Components
- **Frontend Components**: [FRONTEND_COMPONENTS]
- **Backend Services**: [BACKEND_SERVICES]
- **Database Layer**: [DATABASE_LAYER]
- **Cache Layer**: [CACHE_LAYER]
- **Message Queue**: [MESSAGE_QUEUE]
- **API Gateway**: [API_GATEWAY]
- **Load Balancer**: [LOAD_BALANCER]
- **Service Mesh**: [SERVICE_MESH]
- **Monitoring System**: [MONITORING_SYSTEM]
- **Security Components**: [SECURITY_COMPONENTS]

### Technology Stack
- **Programming Languages**: [PROGRAMMING_LANGUAGES]
- **Frontend Framework**: [FRONTEND_FRAMEWORK]
- **Backend Framework**: [BACKEND_FRAMEWORK]
- **Database Technology**: [DATABASE_TECHNOLOGY]
- **Caching Solution**: [CACHING_SOLUTION]
- **Message Broker**: [MESSAGE_BROKER]
- **Container Platform**: [CONTAINER_PLATFORM]
- **Orchestration Tool**: [ORCHESTRATION_TOOL]
- **Cloud Provider**: [CLOUD_PROVIDER]
- **Development Tools**: [DEVELOPMENT_TOOLS]

### Scalability Design
- **Horizontal Scaling**: [HORIZONTAL_SCALING]
- **Vertical Scaling**: [VERTICAL_SCALING]
- **Auto Scaling**: [AUTO_SCALING]
- **Load Distribution**: [LOAD_DISTRIBUTION]
- **Caching Strategy**: [CACHING_STRATEGY]
- **Database Sharding**: [DATABASE_SHARDING]
- **CDN Strategy**: [CDN_STRATEGY]
- **Resource Optimization**: [RESOURCE_OPTIMIZATION]
- **Performance Targets**: [PERFORMANCE_TARGETS]
- **Capacity Planning**: [CAPACITY_PLANNING]

### Security Architecture
- **Authentication Method**: [AUTHENTICATION_METHOD]
- **Authorization Model**: [AUTHORIZATION_MODEL]
- **Data Encryption**: [DATA_ENCRYPTION]
- **Network Security**: [NETWORK_SECURITY]
- **API Security**: [API_SECURITY]
- **Database Security**: [DATABASE_SECURITY]
- **Infrastructure Security**: [INFRASTRUCTURE_SECURITY]
- **Application Security**: [APPLICATION_SECURITY]
- **Monitoring Security**: [MONITORING_SECURITY]
- **Compliance Framework**: [COMPLIANCE_FRAMEWORK]

### Data Architecture
- **Data Model**: [DATA_MODEL]
- **Database Design**: [DATABASE_DESIGN]
- **Data Storage**: [DATA_STORAGE]
- **Data Processing**: [DATA_PROCESSING]
- **Data Integration**: [DATA_INTEGRATION]
- **Data Governance**: [DATA_GOVERNANCE]
- **Data Quality**: [DATA_QUALITY]
- **Data Backup**: [DATA_BACKUP]
- **Data Recovery**: [DATA_RECOVERY]
- **Data Archival**: [DATA_ARCHIVAL]

### API Design
- **API Architecture**: [API_ARCHITECTURE]
- **API Protocol**: [API_PROTOCOL]
- **API Versioning**: [API_VERSIONING]
- **API Documentation**: [API_DOCUMENTATION]
- **Rate Limiting**: [RATE_LIMITING]
- **API Testing**: [API_TESTING]
- **API Monitoring**: [API_MONITORING]
- **API Security**: [API_SECURITY_MEASURES]
- **Error Handling**: [API_ERROR_HANDLING]
- **Response Format**: [API_RESPONSE_FORMAT]

### Microservices Design
- **Service Boundaries**: [SERVICE_BOUNDARIES]
- **Service Communication**: [SERVICE_COMMUNICATION]
- **Service Discovery**: [SERVICE_DISCOVERY]
- **Circuit Breaker**: [CIRCUIT_BREAKER]
- **Service Mesh**: [SERVICE_MESH_IMPLEMENTATION]
- **Event Sourcing**: [EVENT_SOURCING]
- **CQRS Pattern**: [CQRS_PATTERN]
- **Saga Pattern**: [SAGA_PATTERN]
- **Bulkhead Pattern**: [BULKHEAD_PATTERN]
- **Retry Logic**: [RETRY_LOGIC]

### Infrastructure Design
- **Cloud Architecture**: [CLOUD_ARCHITECTURE]
- **Network Topology**: [NETWORK_TOPOLOGY]
- **Server Configuration**: [SERVER_CONFIGURATION]
- **Container Strategy**: [CONTAINER_STRATEGY]
- **Storage Architecture**: [STORAGE_ARCHITECTURE]
- **Backup Strategy**: [BACKUP_STRATEGY]
- **Disaster Recovery**: [DISASTER_RECOVERY]
- **High Availability**: [HIGH_AVAILABILITY]
- **Fault Tolerance**: [FAULT_TOLERANCE]
- **Resource Management**: [RESOURCE_MANAGEMENT]

### Deployment Architecture
- **Deployment Strategy**: [DEPLOYMENT_STRATEGY]
- **Environment Setup**: [ENVIRONMENT_SETUP]
- **CI/CD Pipeline**: [CICD_PIPELINE_DESIGN]
- **Release Management**: [RELEASE_MANAGEMENT]
- **Blue-Green Deployment**: [BLUE_GREEN_DEPLOYMENT]
- **Canary Deployment**: [CANARY_DEPLOYMENT]
- **Rolling Updates**: [ROLLING_UPDATES]
- **Rollback Strategy**: [ROLLBACK_STRATEGY]
- **Configuration Management**: [CONFIGURATION_MANAGEMENT]
- **Secrets Management**: [SECRETS_MANAGEMENT]

### Monitoring and Observability
- **Logging Strategy**: [LOGGING_STRATEGY]
- **Metrics Collection**: [METRICS_COLLECTION]
- **Distributed Tracing**: [DISTRIBUTED_TRACING]
- **Health Checks**: [HEALTH_CHECKS]
- **Alerting System**: [ALERTING_SYSTEM]
- **Dashboard Design**: [DASHBOARD_DESIGN]
- **SLA Monitoring**: [SLA_MONITORING]
- **Performance Monitoring**: [PERFORMANCE_MONITORING]
- **Error Tracking**: [ERROR_TRACKING]
- **Business Metrics**: [BUSINESS_METRICS]

### Integration Architecture
- **External Integrations**: [EXTERNAL_INTEGRATIONS]
- **Third Party APIs**: [THIRD_PARTY_APIS]
- **Data Synchronization**: [DATA_SYNCHRONIZATION]
- **Event-Driven Architecture**: [EVENT_DRIVEN_ARCHITECTURE]
- **Message Patterns**: [MESSAGE_PATTERNS]
- **Webhook Management**: [WEBHOOK_MANAGEMENT]
- **File Transfer**: [FILE_TRANSFER]
- **Real-time Communication**: [REALTIME_COMMUNICATION]
- **Batch Processing**: [BATCH_PROCESSING]
- **Stream Processing**: [STREAM_PROCESSING]

### Performance Optimization
- **Caching Layers**: [CACHING_LAYERS]
- **Database Optimization**: [DATABASE_OPTIMIZATION]
- **Query Optimization**: [QUERY_OPTIMIZATION]
- **Connection Pooling**: [CONNECTION_POOLING]
- **Lazy Loading**: [LAZY_LOADING]
- **Compression**: [COMPRESSION]
- **Minification**: [MINIFICATION]
- **Image Optimization**: [IMAGE_OPTIMIZATION]
- **Content Delivery**: [CONTENT_DELIVERY]
- **Resource Bundling**: [RESOURCE_BUNDLING]

### Quality Attributes
- **Availability**: [AVAILABILITY]
- **Reliability**: [RELIABILITY]
- **Scalability**: [SCALABILITY]
- **Performance**: [PERFORMANCE]
- **Security**: [SECURITY]
- **Maintainability**: [MAINTAINABILITY]
- **Testability**: [TESTABILITY]
- **Usability**: [USABILITY]
- **Portability**: [PORTABILITY]
- **Interoperability**: [INTEROPERABILITY]

### Risk Management
- **Technical Risks**: [TECHNICAL_RISKS]
- **Security Risks**: [SECURITY_RISKS]
- **Performance Risks**: [PERFORMANCE_RISKS]
- **Scalability Risks**: [SCALABILITY_RISKS]
- **Integration Risks**: [INTEGRATION_RISKS]
- **Operational Risks**: [OPERATIONAL_RISKS]
- **Business Risks**: [BUSINESS_RISKS]
- **Mitigation Strategies**: [MITIGATION_STRATEGIES]
- **Contingency Plans**: [CONTINGENCY_PLANS]
- **Risk Monitoring**: [RISK_MONITORING]

### Documentation Requirements
- **Architecture Documentation**: [ARCHITECTURE_DOCUMENTATION]
- **Design Decisions**: [DESIGN_DECISIONS]
- **Trade-off Analysis**: [TRADEOFF_ANALYSIS]
- **Implementation Guide**: [IMPLEMENTATION_GUIDE]
- **Deployment Guide**: [DEPLOYMENT_GUIDE]
- **Operations Manual**: [OPERATIONS_MANUAL]
- **Troubleshooting Guide**: [TROUBLESHOOTING_GUIDE]
- **API Documentation**: [API_DOCUMENTATION_DETAILS]
- **Database Schema**: [DATABASE_SCHEMA]
- **Security Guidelines**: [SECURITY_GUIDELINES]

### Testing Strategy
- **Unit Testing**: [UNIT_TESTING]
- **Integration Testing**: [INTEGRATION_TESTING]
- **End-to-End Testing**: [END_TO_END_TESTING]
- **Performance Testing**: [PERFORMANCE_TESTING]
- **Security Testing**: [SECURITY_TESTING]
- **Load Testing**: [LOAD_TESTING]
- **Stress Testing**: [STRESS_TESTING]
- **Chaos Engineering**: [CHAOS_ENGINEERING]
- **A/B Testing**: [AB_TESTING]
- **Test Automation**: [TEST_AUTOMATION]

### Migration Strategy
- **Migration Approach**: [MIGRATION_APPROACH]
- **Legacy System**: [LEGACY_SYSTEM]
- **Migration Timeline**: [MIGRATION_TIMELINE]
- **Data Migration**: [DATA_MIGRATION]
- **Cutover Strategy**: [CUTOVER_STRATEGY]
- **Rollback Plan**: [ROLLBACK_PLAN]
- **Parallel Running**: [PARALLEL_RUNNING]
- **User Training**: [USER_TRAINING]
- **Change Management**: [CHANGE_MANAGEMENT]
- **Success Criteria**: [SUCCESS_CRITERIA]

## Prompt Template

Design a [ARCHITECTURE_STYLE] architecture for [SYSTEM_NAME] that serves [TARGET_USERS] with [EXPECTED_LOAD] load requirements. The system should implement [PRIMARY_PATTERN] pattern and support [BUSINESS_DOMAIN] domain.

**Core Architecture Requirements:**
- Implement [FRONTEND_COMPONENTS] frontend using [FRONTEND_FRAMEWORK]
- Design [BACKEND_SERVICES] backend services with [BACKEND_FRAMEWORK]
- Use [DATABASE_TECHNOLOGY] for data persistence with [DATABASE_DESIGN]
- Integrate [MESSAGE_BROKER] for [SERVICE_COMMUNICATION]
- Deploy on [CLOUD_PROVIDER] with [CONTAINER_PLATFORM]

**Scalability and Performance:**
- Support [HORIZONTAL_SCALING] and [AUTO_SCALING]
- Implement [CACHING_STRATEGY] with [CACHING_SOLUTION]
- Achieve [PERFORMANCE_TARGETS] response times
- Handle [LOAD_DISTRIBUTION] across multiple instances
- Use [CDN_STRATEGY] for content delivery

**Security Implementation:**
- Implement [AUTHENTICATION_METHOD] and [AUTHORIZATION_MODEL]
- Use [DATA_ENCRYPTION] for data protection
- Apply [NETWORK_SECURITY] and [API_SECURITY]
- Follow [COMPLIANCE_FRAMEWORK] requirements
- Include [MONITORING_SECURITY] measures

**Integration and Communication:**
- Design [API_ARCHITECTURE] APIs with [API_PROTOCOL]
- Implement [SERVICE_DISCOVERY] for microservices
- Use [EVENT_DRIVEN_ARCHITECTURE] for loose coupling
- Handle [EXTERNAL_INTEGRATIONS] with [THIRD_PARTY_APIS]
- Support [REALTIME_COMMUNICATION] where needed

**Reliability and Monitoring:**
- Implement [HIGH_AVAILABILITY] with [FAULT_TOLERANCE]
- Use [CIRCUIT_BREAKER] and [RETRY_LOGIC] patterns
- Design [DISASTER_RECOVERY] and [BACKUP_STRATEGY]
- Monitor with [DISTRIBUTED_TRACING] and [METRICS_COLLECTION]
- Set up [ALERTING_SYSTEM] for [SLA_MONITORING]

**Deployment Strategy:**
- Use [DEPLOYMENT_STRATEGY] with [CICD_PIPELINE_DESIGN]
- Implement [BLUE_GREEN_DEPLOYMENT] or [CANARY_DEPLOYMENT]
- Manage configuration with [CONFIGURATION_MANAGEMENT]
- Handle secrets with [SECRETS_MANAGEMENT]
- Support [ROLLING_UPDATES] with [ROLLBACK_STRATEGY]

**Quality Attributes:**
- Ensure [AVAILABILITY]% uptime and [RELIABILITY]
- Support [SCALABILITY] to handle growth
- Maintain [PERFORMANCE] under peak load
- Implement [SECURITY] best practices
- Design for [MAINTAINABILITY] and [TESTABILITY]

Please provide detailed architecture diagrams, component specifications, technology recommendations, deployment plans, and risk mitigation strategies. Include trade-off analysis for major design decisions and compliance with [REGULATORY_REQUIREMENTS].

## Usage Examples

### E-commerce Platform Architecture
```
Design a microservices architecture for ShopFlow e-commerce platform that serves 1M+ users with 10K concurrent load requirements. The system should implement event-driven pattern and support retail domain.

Core Architecture Requirements:
- Implement React SPA frontend using Next.js framework
- Design 8 backend services (user, product, order, payment, inventory, recommendation, notification, analytics) with Node.js/Express
- Use PostgreSQL for transactional data with normalized database design
- Integrate Apache Kafka for asynchronous service communication
- Deploy on AWS with Kubernetes container platform

Scalability and Performance:
- Support horizontal pod scaling and cluster autoscaling
- Implement multi-layer caching with Redis and CloudFront CDN
- Achieve <200ms API response times
- Handle geographic load distribution across multiple regions
- Use CloudFront CDN for static asset delivery

### Security Implementation
- Implement OAuth 2.0/JWT authentication and RBAC authorization model
- Use AES-256 encryption for PII data protection
- Apply WAF, API Gateway rate limiting, and OAuth security
- Follow PCI DSS compliance requirements
- Include SIEM monitoring and threat detection measures
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[SYSTEM_NAME]` | Specify the system name | "OrderFlow", "PaymentHub", "InventoryManager", "CustomerPortal" |
| `[SYSTEM_PURPOSE]` | Specify the system purpose | "Real-time order processing and fulfillment", "Customer identity and access management", "Inventory tracking and warehouse management" |
| `[BUSINESS_DOMAIN]` | Specify the business domain | "E-commerce retail", "Healthcare patient management", "Financial trading", "Logistics and supply chain" |
| `[TARGET_USERS]` | Specify the target users | "1M+ monthly active consumers", "500 internal employees", "10K B2B enterprise clients", "Global mobile users" |
| `[EXPECTED_LOAD]` | Specify the expected load | "10K concurrent users, 1M daily requests", "100K transactions per second at peak", "50TB data processing daily" |
| `[GEOGRAPHIC_DISTRIBUTION]` | Specify the geographic distribution | "Multi-region (US-East, US-West, EU-West)", "Global with edge locations", "Single region with DR failover" |
| `[REGULATORY_REQUIREMENTS]` | Specify the regulatory requirements | "PCI DSS Level 1, SOC 2 Type II", "HIPAA, HITECH compliance", "GDPR, CCPA data privacy", "FedRAMP Moderate" |
| `[BUDGET_CONSTRAINTS]` | Specify the budget constraints | "$500,000" |
| `[TIMELINE]` | Specify the timeline | "6 months" |
| `[SUCCESS_METRICS]` | Specify the success metrics | "99.99% uptime, <100ms p95 latency", "Zero security incidents, 50% cost reduction", "3x throughput improvement" |
| `[PRIMARY_PATTERN]` | Specify the primary pattern | "Microservices architecture", "Event-driven architecture", "Hexagonal (Ports & Adapters)", "CQRS with Event Sourcing" |
| `[SECONDARY_PATTERNS]` | Specify the secondary patterns | "API Gateway, Circuit Breaker, Saga", "Domain-Driven Design, Clean Architecture", "Strangler Fig, Anti-Corruption Layer" |
| `[DESIGN_PRINCIPLES]` | Specify the design principles | "SOLID, DRY, KISS", "Twelve-Factor App methodology", "Defense in depth, least privilege", "Eventual consistency, idempotency" |
| `[ARCHITECTURE_STYLE]` | Specify the architecture style | "Microservices", "Serverless", "Event-driven", "Layered N-tier", "Service mesh" |
| `[COMMUNICATION_PATTERN]` | Specify the communication pattern | "Synchronous REST/gRPC for queries, async messaging for commands", "Request-response with circuit breakers", "Pub/sub for event broadcasting" |
| `[DATA_FLOW_PATTERN]` | Specify the data flow pattern | "Event sourcing with materialized views", "Stream processing with Apache Kafka", "ETL pipelines with change data capture" |
| `[INTEGRATION_PATTERN]` | Specify the integration pattern | "API-first with OpenAPI contracts", "Message broker integration", "Webhook callbacks", "GraphQL federation" |
| `[DEPLOYMENT_PATTERN]` | Specify the deployment pattern | "Blue-green with instant rollback", "Canary releases with 5% traffic split", "Rolling updates with health checks" |
| `[SECURITY_PATTERN]` | Specify the security pattern | "Zero-trust architecture", "Defense in depth with WAF", "mTLS service mesh", "API gateway with OAuth 2.0" |
| `[RESILIENCE_PATTERN]` | Specify the resilience pattern | "Circuit breaker with fallback", "Bulkhead isolation per service", "Retry with exponential backoff", "Timeout cascades" |
| `[FRONTEND_COMPONENTS]` | Specify the frontend components | "React SPA with Next.js SSR", "Angular micro-frontends", "Vue.js with Nuxt", "Mobile apps (iOS/Android)" |
| `[BACKEND_SERVICES]` | Specify the backend services | "8 microservices: user, product, order, payment, inventory, notification, search, analytics", "3 core domains with 12 bounded contexts" |
| `[DATABASE_LAYER]` | Specify the database layer | "PostgreSQL for OLTP, MongoDB for documents, TimescaleDB for metrics", "Multi-model with polyglot persistence" |
| `[CACHE_LAYER]` | Specify the cache layer | "Redis Cluster for sessions and hot data", "Memcached for simple caching", "CDN edge caching for static assets" |
| `[MESSAGE_QUEUE]` | Specify the message queue | "Apache Kafka for event streaming", "RabbitMQ for task queues", "AWS SQS for async processing" |
| `[API_GATEWAY]` | Specify the api gateway | "Kong Enterprise with rate limiting", "AWS API Gateway", "NGINX Plus", "Envoy with custom filters" |
| `[LOAD_BALANCER]` | Specify the load balancer | "AWS ALB with WAF integration", "HAProxy for TCP/HTTP", "NGINX with sticky sessions", "F5 BIG-IP" |
| `[SERVICE_MESH]` | Specify the service mesh | "Istio with Envoy sidecars", "Linkerd for lightweight mesh", "Consul Connect", "AWS App Mesh" |
| `[MONITORING_SYSTEM]` | Specify the monitoring system | "Prometheus + Grafana + AlertManager", "Datadog APM", "New Relic One", "ELK Stack (Elasticsearch, Logstash, Kibana)" |
| `[SECURITY_COMPONENTS]` | Specify the security components | "HashiCorp Vault for secrets, OAuth 2.0/OIDC for auth", "WAF, IDS/IPS, SIEM integration", "mTLS certificates" |
| `[PROGRAMMING_LANGUAGES]` | Specify the programming languages | "Java 17, TypeScript 5.x, Python 3.11, Go 1.21", "Kotlin for Android, Swift for iOS" |
| `[FRONTEND_FRAMEWORK]` | Specify the frontend framework | "React 18 with Next.js 14", "Angular 17", "Vue 3 with Composition API", "Svelte with SvelteKit" |
| `[BACKEND_FRAMEWORK]` | Specify the backend framework | "Spring Boot 3.x, Node.js/Express, FastAPI", "NestJS, Django REST Framework", ".NET 8 Minimal APIs" |
| `[DATABASE_TECHNOLOGY]` | Specify the database technology | "PostgreSQL 15, MongoDB 7, Redis 7", "Amazon Aurora, DynamoDB", "CockroachDB for distributed SQL" |
| `[CACHING_SOLUTION]` | Specify the caching solution | "Redis Cluster with Sentinel", "AWS ElastiCache", "Hazelcast IMDG", "Apache Ignite" |
| `[MESSAGE_BROKER]` | Specify the message broker | "Apache Kafka 3.x with Schema Registry", "RabbitMQ 3.12", "AWS SNS/SQS", "Apache Pulsar" |
| `[CONTAINER_PLATFORM]` | Specify the container platform | "Docker with containerd runtime", "Podman for rootless containers", "AWS ECS/Fargate" |
| `[ORCHESTRATION_TOOL]` | Specify the orchestration tool | "Kubernetes 1.28 with Helm", "Amazon EKS", "Google GKE Autopilot", "Azure AKS" |
| `[CLOUD_PROVIDER]` | Specify the cloud provider | "AWS (primary), GCP (DR)", "Azure with hybrid on-prem", "Multi-cloud with Terraform", "Private cloud OpenStack" |
| `[DEVELOPMENT_TOOLS]` | Specify the development tools | "VS Code, IntelliJ IDEA, GitHub Copilot", "Docker Desktop, Postman, k9s", "Terraform, Ansible, ArgoCD" |
| `[HORIZONTAL_SCALING]` | Specify the horizontal scaling | "Kubernetes HPA based on CPU/memory (min 3, max 20 pods)", "Auto-scaling groups with target tracking", "Serverless with concurrency limits" |
| `[VERTICAL_SCALING]` | Specify the vertical scaling | "Instance right-sizing based on CloudWatch metrics", "Database read replicas and connection pooling", "Memory/CPU tier upgrades" |
| `[AUTO_SCALING]` | Specify the auto scaling | "CPU > 70% triggers scale-out, < 30% scale-in", "Request-based scaling with 5-minute cooldown", "Predictive scaling for known traffic patterns" |
| `[LOAD_DISTRIBUTION]` | Specify the load distribution | "Round-robin with health checks", "Weighted routing for A/B testing", "Geographic routing via Route 53", "Consistent hashing for sticky sessions" |
| `[CACHING_STRATEGY]` | Specify the caching strategy | "Multi-tier: CDN edge (static), Redis (session/API), local (app-level)", "Write-through for consistency, cache-aside for reads" |
| `[DATABASE_SHARDING]` | Specify the database sharding | "Hash-based sharding by customer_id", "Range partitioning by date", "Geographic sharding by region", "Vitess for MySQL sharding" |
| `[CDN_STRATEGY]` | Specify the cdn strategy | "CloudFront with 24-hour TTL for static assets", "Edge functions for dynamic content", "Multi-CDN failover (CloudFront + Fastly)" |
| `[RESOURCE_OPTIMIZATION]` | Specify the resource optimization | "Spot instances for batch jobs (70% savings)", "Reserved capacity for baseline load", "Graviton ARM instances for cost efficiency" |
| `[PERFORMANCE_TARGETS]` | Specify the performance targets | "p50 < 50ms, p95 < 200ms, p99 < 500ms API latency", "<2s page load, 100ms TTFB", "1M requests/second throughput" |
| `[CAPACITY_PLANNING]` | Specify the capacity planning | "6-month traffic forecasts with 30% buffer", "Load testing at 2x peak capacity", "Monthly capacity reviews and adjustments" |
| `[AUTHENTICATION_METHOD]` | Specify the authentication method | "OAuth 2.0 + OpenID Connect with JWT", "SAML 2.0 for enterprise SSO", "Multi-factor authentication (TOTP, WebAuthn)", "API keys with rotation" |
| `[AUTHORIZATION_MODEL]` | Specify the authorization model | "RBAC with hierarchical roles", "ABAC for fine-grained permissions", "Policy-based with OPA (Open Policy Agent)", "Resource-level ACLs" |
| `[DATA_ENCRYPTION]` | Specify the data encryption | "AES-256 at rest, TLS 1.3 in transit", "Customer-managed KMS keys", "Field-level encryption for PII", "Database TDE" |
| `[NETWORK_SECURITY]` | Specify the network security | "VPC with private subnets, NAT gateways", "Security groups with least privilege", "Network ACLs for subnet isolation", "PrivateLink for AWS services" |
| `[API_SECURITY]` | Specify the api security | "Rate limiting (1000 req/min per client)", "Request signing and validation", "CORS policy enforcement", "API versioning with deprecation" |
| `[DATABASE_SECURITY]` | Specify the database security | "Encrypted connections (SSL/TLS required)", "IAM database authentication", "Row-level security policies", "Audit logging enabled" |
| `[INFRASTRUCTURE_SECURITY]` | Specify the infrastructure security | "Immutable infrastructure with golden AMIs", "AWS Config compliance rules", "CIS benchmark hardened images", "Secrets in AWS Secrets Manager" |
| `[APPLICATION_SECURITY]` | Specify the application security | "OWASP Top 10 mitigations", "Dependency scanning (Snyk, Dependabot)", "SAST/DAST in CI pipeline", "Runtime application self-protection (RASP)" |
| `[MONITORING_SECURITY]` | Specify the monitoring security | "SIEM integration (Splunk/Sentinel)", "CloudTrail audit logs with alerting", "Anomaly detection for unusual access", "Security dashboards and KPIs" |
| `[COMPLIANCE_FRAMEWORK]` | Specify the compliance framework | "SOC 2 Type II controls", "PCI DSS Level 1 requirements", "HIPAA technical safeguards", "ISO 27001 ISMS", "GDPR Article 32 measures" |
| `[DATA_MODEL]` | Specify the data model | "Domain-driven design with bounded contexts", "Event sourcing with aggregate roots", "Document-oriented for flexible schemas", "Graph model for relationships" |
| `[DATABASE_DESIGN]` | Specify the database design | "Normalized 3NF for transactional data", "Denormalized for read performance", "Star schema for analytics", "Polyglot persistence per service" |
| `[DATA_STORAGE]` | Specify the data storage | "Hot data in SSD-backed RDS, warm in S3, cold in Glacier", "Time-series in InfluxDB/TimescaleDB", "Binary/media in S3 with CloudFront" |
| `[DATA_PROCESSING]` | Specify the data processing | "Real-time streaming with Kafka Streams/Flink", "Batch processing with Apache Spark", "ETL pipelines with Airflow/dbt" |
| `[DATA_INTEGRATION]` | Specify the data integration | "Change data capture with Debezium", "API-based sync with rate limiting", "Event-driven integration via message bus", "File-based batch imports" |
| `[DATA_GOVERNANCE]` | Specify the data governance | "Data catalog with Apache Atlas/AWS Glue", "Data lineage tracking", "Classification and tagging policies", "Data stewardship roles" |
| `[DATA_QUALITY]` | Specify the data quality | "Schema validation on ingestion", "Great Expectations for data testing", "Automated profiling and anomaly detection", "SLA monitoring for freshness" |
| `[DATA_BACKUP]` | Specify the data backup | "Automated daily snapshots with 30-day retention", "Cross-region replication for DR", "Point-in-time recovery enabled", "Weekly full + daily incremental" |
| `[DATA_RECOVERY]` | Specify the data recovery | "RTO: 4 hours, RPO: 1 hour for critical systems", "Automated failover to standby", "Runbook-driven recovery procedures", "Regular DR drills quarterly" |
| `[DATA_ARCHIVAL]` | Specify the data archival | "90-day hot, 1-year warm, 7-year cold storage", "Lifecycle policies for automatic tiering", "Compliance-driven retention periods", "Searchable archive indexes" |
| `[API_ARCHITECTURE]` | Specify the api architecture | "RESTful with HATEOAS", "GraphQL for flexible queries", "gRPC for internal service-to-service", "AsyncAPI for event-driven" |
| `[API_PROTOCOL]` | Specify the api protocol | "HTTPS REST with JSON payloads", "gRPC with Protocol Buffers", "WebSocket for real-time", "Server-Sent Events for streaming" |
| `[API_VERSIONING]` | Specify the api versioning | "URL path versioning (/v1/, /v2/)", "Header-based (Accept-Version)", "Query parameter (?version=2)", "Semantic versioning with deprecation notices" |
| `[API_DOCUMENTATION]` | Specify the api documentation | "OpenAPI 3.1 specification", "Swagger UI for interactive docs", "Postman collections with examples", "API changelog and migration guides" |
| `[RATE_LIMITING]` | Specify the rate limiting | "Token bucket: 1000 req/min per API key", "Sliding window for burst handling", "Tiered limits by subscription plan", "429 responses with Retry-After header" |
| `[API_TESTING]` | Specify the api testing | "Contract testing with Pact", "Integration tests with Postman/Newman", "Load testing with k6/Locust", "Security testing with OWASP ZAP" |
| `[API_MONITORING]` | Specify the api monitoring | "Request/response logging with correlation IDs", "Latency percentiles (p50, p95, p99)", "Error rate dashboards", "SLA compliance tracking" |
| `[API_SECURITY_MEASURES]` | Specify the api security measures | "JWT validation with RS256", "API key rotation every 90 days", "Request signing for webhooks", "Input sanitization and validation" |
| `[API_ERROR_HANDLING]` | Specify the api error handling | "RFC 7807 Problem Details format", "Consistent error codes with messages", "Stack traces only in dev environments", "Retry guidance in error responses" |
| `[API_RESPONSE_FORMAT]` | Specify the api response format | "JSON:API specification", "HAL+JSON with hypermedia links", "Envelope pattern with metadata", "Consistent pagination (cursor-based)" |
| `[SERVICE_BOUNDARIES]` | Specify the service boundaries | "Domain-driven bounded contexts", "One service per aggregate root", "Team-aligned service ownership", "API-first contract boundaries" |
| `[SERVICE_COMMUNICATION]` | Specify the service communication | "Sync: REST/gRPC with timeouts, Async: Kafka events", "Request-reply for queries, fire-and-forget for commands", "Choreography for loose coupling" |
| `[SERVICE_DISCOVERY]` | Specify the service discovery | "Kubernetes DNS-based discovery", "Consul service registry", "AWS Cloud Map", "Eureka with client-side load balancing" |
| `[CIRCUIT_BREAKER]` | Specify the circuit breaker | "Resilience4j with 50% failure threshold", "5-second open state, 10-second half-open", "Fallback to cached data or default response" |
| `[SERVICE_MESH_IMPLEMENTATION]` | Specify the service mesh implementation | "Istio with Envoy sidecars for mTLS", "Traffic splitting for canary deployments", "Distributed tracing with Jaeger integration" |
| `[EVENT_SOURCING]` | Specify the event sourcing | "EventStoreDB for event storage", "Kafka as event log with compaction", "Aggregate replay for state reconstruction", "Snapshots every 100 events" |
| `[CQRS_PATTERN]` | Specify the cqrs pattern | "Separate read/write databases", "Command handlers with domain validation", "Query services with materialized views", "Eventual consistency with 2-second lag" |
| `[SAGA_PATTERN]` | Specify the saga pattern | "Choreography-based for simple flows", "Orchestration with Temporal/Camunda for complex workflows", "Compensating transactions for rollback" |
| `[BULKHEAD_PATTERN]` | Specify the bulkhead pattern | "Thread pool isolation per downstream service", "Connection pool limits (max 50 per service)", "Separate queues for priority traffic" |
| `[RETRY_LOGIC]` | Specify the retry logic | "Exponential backoff: 100ms, 200ms, 400ms, max 3 retries", "Jitter to prevent thundering herd", "Idempotency keys for safe retries" |
| `[CLOUD_ARCHITECTURE]` | Specify the cloud architecture | "Multi-AZ deployment with cross-region DR", "VPC with public/private subnet tiers", "Hybrid cloud with Direct Connect", "Landing zone with Control Tower" |
| `[NETWORK_TOPOLOGY]` | Specify the network topology | "Hub-and-spoke with Transit Gateway", "Three-tier: DMZ, application, data", "Service mesh overlay network", "Zero-trust microsegmentation" |
| `[SERVER_CONFIGURATION]` | Specify the server configuration | "Immutable AMIs with Packer", "Configuration as code with Ansible", "EC2 c6i.xlarge for compute, r6i.2xlarge for memory-intensive", "Spot fleet for batch workloads" |
| `[CONTAINER_STRATEGY]` | Specify the container strategy | "One process per container", "Multi-stage builds for minimal images", "Distroless base images for security", "Resource limits: 512Mi memory, 500m CPU" |
| `[STORAGE_ARCHITECTURE]` | Specify the storage architecture | "EBS gp3 for databases, EFS for shared storage", "S3 for objects with intelligent tiering", "FSx for high-performance file systems" |
| `[BACKUP_STRATEGY]` | Specify the backup strategy | "AWS Backup with daily snapshots", "Cross-region replication for critical data", "Application-consistent backups for databases", "30-day retention, 7-year archive" |
| `[DISASTER_RECOVERY]` | Specify the disaster recovery | "Pilot light DR in secondary region", "RTO 4 hours, RPO 1 hour", "Automated failover with Route 53 health checks", "Quarterly DR testing" |
| `[HIGH_AVAILABILITY]` | Specify the high availability | "Multi-AZ deployments (99.99% SLA)", "Active-active with global load balancing", "Database replicas with automatic failover", "Stateless services for easy scaling" |
| `[FAULT_TOLERANCE]` | Specify the fault tolerance | "Graceful degradation with feature flags", "Circuit breakers preventing cascade failures", "Chaos engineering with Gremlin/LitmusChaos", "Self-healing with Kubernetes liveness probes" |
| `[RESOURCE_MANAGEMENT]` | Specify the resource management | "Kubernetes resource quotas per namespace", "Cost allocation tags for chargebacks", "FinOps practices with Kubecost", "Right-sizing recommendations monthly" |
| `[DEPLOYMENT_STRATEGY]` | Specify the deployment strategy | "GitOps with ArgoCD", "Blue-green with AWS CodeDeploy", "Progressive delivery with Flagger", "Feature flags with LaunchDarkly" |
| `[ENVIRONMENT_SETUP]` | Specify the environment setup | "Dev, Staging, Production with infrastructure parity", "Ephemeral preview environments per PR", "Terraform workspaces per environment" |
| `[CICD_PIPELINE_DESIGN]` | Specify the cicd pipeline design | "GitHub Actions: build, test, scan, deploy", "Jenkins multibranch with shared libraries", "GitLab CI/CD with Auto DevOps", "Tekton pipelines on Kubernetes" |
| `[RELEASE_MANAGEMENT]` | Specify the release management | "Semantic versioning with auto-changelog", "Release branches with cherry-pick hotfixes", "Feature flags for trunk-based development", "Release trains every 2 weeks" |
| `[BLUE_GREEN_DEPLOYMENT]` | Specify the blue green deployment | "Two identical production environments", "DNS cutover with Route 53 weighted routing", "Database compatibility for both versions", "Instant rollback capability" |
| `[CANARY_DEPLOYMENT]` | Specify the canary deployment | "5% traffic initially, increment by 20% hourly", "Automated promotion based on error rate < 0.1%", "Automatic rollback on SLO violation", "Observability-driven deployment" |
| `[ROLLING_UPDATES]` | Specify the rolling updates | "maxSurge: 25%, maxUnavailable: 25%", "Health check grace period: 60 seconds", "Minimum ready seconds: 10", "Pod disruption budget: minAvailable 80%" |
| `[ROLLBACK_STRATEGY]` | Specify the rollback strategy | "One-click rollback to previous version", "Kubernetes rollout undo within 5 minutes", "Database migration rollback scripts", "Feature flag kill switch" |
| `[CONFIGURATION_MANAGEMENT]` | Specify the configuration management | "Kubernetes ConfigMaps and Secrets", "External configuration with Consul/etcd", "Environment-specific overlays with Kustomize", "GitOps with sealed secrets" |
| `[SECRETS_MANAGEMENT]` | Specify the secrets management | "HashiCorp Vault with dynamic credentials", "AWS Secrets Manager with rotation", "Kubernetes External Secrets Operator", "SOPS for encrypted secrets in Git" |
| `[LOGGING_STRATEGY]` | Specify the logging strategy | "Structured JSON logs with correlation IDs", "ELK Stack centralized logging", "Log levels: DEBUG (dev), INFO (prod)", "30-day retention, 1-year archive" |
| `[METRICS_COLLECTION]` | Specify the metrics collection | "Prometheus with service discovery", "Custom metrics via OpenTelemetry", "RED metrics: Rate, Errors, Duration", "USE metrics for infrastructure" |
| `[DISTRIBUTED_TRACING]` | Specify the distributed tracing | "Jaeger with OpenTelemetry instrumentation", "W3C Trace Context propagation", "100% sampling in dev, 10% in prod", "Trace-to-log correlation" |
| `[HEALTH_CHECKS]` | Specify the health checks | "Liveness: /healthz every 10s", "Readiness: /ready with dependency checks", "Startup probes for slow-starting apps", "Deep health checks for critical paths" |
| `[ALERTING_SYSTEM]` | Specify the alerting system | "PagerDuty for P1/P2 incidents", "Slack integration for warnings", "Alert routing by service ownership", "Runbook links in every alert" |
| `[DASHBOARD_DESIGN]` | Specify the dashboard design | "Grafana dashboards per service", "Executive summary dashboard", "Real-time operations center view", "SLO/SLA compliance dashboards" |
| `[SLA_MONITORING]` | Specify the sla monitoring | "99.9% availability target (43.8 min/month downtime)", "SLI: successful requests / total requests", "Error budget tracking and burn rate alerts", "Monthly SLA reports" |
| `[PERFORMANCE_MONITORING]` | Specify the performance monitoring | "APM with Datadog/New Relic", "Real user monitoring (RUM) for frontend", "Synthetic monitoring for critical flows", "Database query performance tracking" |
| `[ERROR_TRACKING]` | Specify the error tracking | "Sentry for exception tracking", "Error grouping and deduplication", "Stack traces with source maps", "Error trends and regression detection" |
| `[BUSINESS_METRICS]` | Specify the business metrics | "Orders per minute, conversion rate", "Revenue tracking with attribution", "User engagement metrics (DAU/MAU)", "Funnel analysis for key flows" |
| `[EXTERNAL_INTEGRATIONS]` | Specify the external integrations | "Payment gateways (Stripe, PayPal)", "CRM (Salesforce, HubSpot)", "ERP (SAP, Oracle)", "Shipping carriers (FedEx, UPS APIs)" |
| `[THIRD_PARTY_APIS]` | Specify the third party apis | "Twilio for SMS/voice", "SendGrid for email", "Auth0 for identity", "Google Maps for geolocation" |
| `[DATA_SYNCHRONIZATION]` | Specify the data synchronization | "CDC with Debezium for real-time sync", "Batch ETL jobs nightly", "Two-way sync with conflict resolution", "Event-driven eventual consistency" |
| `[EVENT_DRIVEN_ARCHITECTURE]` | Specify the event driven architecture | "Domain events published to Kafka topics", "Event storming for domain modeling", "Choreography between services", "Event versioning with schema registry" |
| `[MESSAGE_PATTERNS]` | Specify the message patterns | "Pub/sub for broadcast events", "Point-to-point for commands", "Request-reply for synchronous needs", "Dead letter queues for failures" |
| `[WEBHOOK_MANAGEMENT]` | Specify the webhook management | "Webhook registry with retry logic", "HMAC signature verification", "Exponential backoff on failures", "Event delivery status tracking" |
| `[FILE_TRANSFER]` | Specify the file transfer | "S3 presigned URLs for large files", "SFTP for legacy integrations", "AWS Transfer Family for managed SFTP", "Multipart uploads for >100MB files" |
| `[REALTIME_COMMUNICATION]` | Specify the realtime communication | "WebSocket with Socket.io", "Server-Sent Events for updates", "AWS AppSync for GraphQL subscriptions", "Pusher/Ably for managed real-time" |
| `[BATCH_PROCESSING]` | Specify the batch processing | "AWS Batch for compute-intensive jobs", "Apache Spark for large-scale data", "Step Functions for orchestration", "Nightly jobs with 4-hour processing window" |
| `[STREAM_PROCESSING]` | Specify the stream processing | "Kafka Streams for stateful processing", "Apache Flink for complex event processing", "Kinesis Data Analytics", "Real-time aggregations and windowing" |
| `[CACHING_LAYERS]` | Specify the caching layers | "L1: In-memory (Caffeine), L2: Distributed (Redis), L3: CDN edge", "Cache-aside pattern with TTL-based invalidation", "Write-through for consistency" |
| `[DATABASE_OPTIMIZATION]` | Specify the database optimization | "Query plan analysis and index tuning", "Connection pooling with PgBouncer", "Read replicas for query distribution", "Partitioning for large tables" |
| `[QUERY_OPTIMIZATION]` | Specify the query optimization | "EXPLAIN ANALYZE for slow queries", "Index coverage for common queries", "Query caching with prepared statements", "N+1 query detection and batching" |
| `[CONNECTION_POOLING]` | Specify the connection pooling | "HikariCP with 20-50 connections per service", "PgBouncer in transaction mode", "Connection validation on borrow", "Idle timeout: 10 minutes" |
| `[LAZY_LOADING]` | Specify the lazy loading | "JPA lazy fetch for relationships", "GraphQL deferred loading", "React lazy components with Suspense", "Intersection Observer for images" |
| `[COMPRESSION]` | Specify the compression | "Gzip/Brotli for HTTP responses", "Protocol Buffers for binary payloads", "LZ4 for Kafka message compression", "Snappy for database storage" |
| `[MINIFICATION]` | Specify the minification | "Terser for JavaScript", "cssnano for CSS", "HTMLMinifier for HTML", "Source maps for debugging" |
| `[IMAGE_OPTIMIZATION]` | Specify the image optimization | "WebP/AVIF with fallbacks", "Responsive images with srcset", "Lazy loading with blur placeholders", "CloudFront image optimization" |
| `[CONTENT_DELIVERY]` | Specify the content delivery | "CloudFront CDN with 200+ edge locations", "Cache-Control headers for static assets", "Origin shield for cache efficiency", "Lambda@Edge for dynamic content" |
| `[RESOURCE_BUNDLING]` | Specify the resource bundling | "Webpack code splitting by route", "Tree shaking for dead code elimination", "Dynamic imports for on-demand loading", "Shared chunks for common dependencies" |
| `[AVAILABILITY]` | Specify the availability | "99.99% uptime (52 min downtime/year)", "Multi-AZ with automatic failover", "Zero-downtime deployments", "RTO < 15 minutes" |
| `[RELIABILITY]` | Specify the reliability | "Mean time between failures (MTBF) > 720 hours", "Error rate < 0.1%", "Automatic recovery from transient failures", "Chaos engineering validated" |
| `[SCALABILITY]` | Specify the scalability | "Horizontal scaling to 100x baseline load", "Auto-scaling within 2 minutes", "Linear cost scaling with traffic", "Stateless services for easy replication" |
| `[PERFORMANCE]` | Specify the performance | "API p95 latency < 200ms", "Page load < 2 seconds", "Database query p99 < 100ms", "Throughput: 10K requests/second" |
| `[SECURITY]` | Specify the security | "Zero-trust architecture", "Defense in depth with multiple layers", "Compliance: SOC 2, PCI DSS, GDPR", "Regular penetration testing" |
| `[MAINTAINABILITY]` | Specify the maintainability | "Modular microservices architecture", "Comprehensive documentation", "Automated testing > 80% coverage", "Infrastructure as code" |
| `[TESTABILITY]` | Specify the testability | "Dependency injection for mocking", "Contract testing between services", "Test environments mirror production", "Feature flags for testing in production" |
| `[USABILITY]` | Specify the usability | "API developer portal with examples", "Self-service onboarding", "Comprehensive error messages", "SDK support for major languages" |
| `[PORTABILITY]` | Specify the portability | "Containerized workloads (Docker/Kubernetes)", "Cloud-agnostic with Terraform", "No vendor lock-in for core services", "Standard protocols (REST, GraphQL, gRPC)" |
| `[INTEROPERABILITY]` | Specify the interoperability | "OpenAPI specifications for all APIs", "Standard data formats (JSON, Protocol Buffers)", "Event schemas in Avro/JSON Schema", "OAuth 2.0/OIDC for authentication" |
| `[TECHNICAL_RISKS]` | Specify the technical risks | "Database scaling limits at 10M rows/table", "Legacy system integration complexity", "Third-party API dependency failures", "Technology obsolescence" |
| `[SECURITY_RISKS]` | Specify the security risks | "Data breach potential (PII exposure)", "API vulnerabilities (OWASP Top 10)", "Insider threat vectors", "Supply chain attacks via dependencies" |
| `[PERFORMANCE_RISKS]` | Specify the performance risks | "Database hotspots under peak load", "Network latency in cross-region calls", "Memory leaks in long-running processes", "Cache stampede scenarios" |
| `[SCALABILITY_RISKS]` | Specify the scalability risks | "Stateful service scaling limitations", "Database write throughput bottlenecks", "Message queue consumer lag", "Cost explosion with traffic spikes" |
| `[INTEGRATION_RISKS]` | Specify the integration risks | "Third-party API changes breaking integrations", "Data format incompatibilities", "Authentication/authorization mismatches", "Timeout cascade failures" |
| `[OPERATIONAL_RISKS]` | Specify the operational risks | "Configuration drift across environments", "Inadequate monitoring coverage", "Manual deployment errors", "Insufficient disaster recovery testing" |
| `[BUSINESS_RISKS]` | Specify the business risks | "Revenue loss during outages", "Reputation damage from security incidents", "Regulatory non-compliance penalties", "Vendor lock-in increasing costs" |
| `[MITIGATION_STRATEGIES]` | Specify the mitigation strategies | "Circuit breakers for dependency failures", "Multi-region deployment for availability", "Regular security audits and pen tests", "Automated compliance monitoring" |
| `[CONTINGENCY_PLANS]` | Specify the contingency plans | "Documented runbooks for all failure scenarios", "On-call rotation with escalation paths", "Pre-approved change rollback procedures", "Business continuity communication plans" |
| `[RISK_MONITORING]` | Specify the risk monitoring | "Real-time dashboards for risk indicators", "Automated alerts on threshold breaches", "Weekly risk review meetings", "Quarterly risk assessment updates" |
| `[ARCHITECTURE_DOCUMENTATION]` | Specify the architecture documentation | "C4 model diagrams (Context, Container, Component)", "Architecture Decision Records (ADRs)", "Living documentation in Confluence/Notion" |
| `[DESIGN_DECISIONS]` | Specify the design decisions | "ADR format: context, decision, consequences", "Decision log with rationale and alternatives", "Review board approval for major changes" |
| `[TRADEOFF_ANALYSIS]` | Specify the tradeoff analysis | "CAP theorem considerations documented", "Cost vs. performance analysis", "Build vs. buy decisions with TCO" |
| `[IMPLEMENTATION_GUIDE]` | Specify the implementation guide | "Step-by-step setup instructions", "Code examples and templates", "Common patterns and anti-patterns", "FAQ for developers" |
| `[DEPLOYMENT_GUIDE]` | Specify the deployment guide | "Environment-specific deployment steps", "Pre/post deployment checklists", "Rollback procedures documented", "Smoke test verification steps" |
| `[OPERATIONS_MANUAL]` | Specify the operations manual | "Runbooks for common operations", "On-call playbooks with escalation", "Incident response procedures", "Maintenance windows and procedures" |
| `[TROUBLESHOOTING_GUIDE]` | Specify the troubleshooting guide | "Common error codes and resolutions", "Log analysis procedures", "Performance debugging steps", "Escalation criteria and contacts" |
| `[API_DOCUMENTATION_DETAILS]` | Specify the api documentation details | "OpenAPI 3.1 specs with examples", "Postman collections for testing", "SDK documentation and samples", "Changelog with breaking changes" |
| `[DATABASE_SCHEMA]` | Specify the database schema | "ERD diagrams with relationships", "Table definitions with constraints", "Index documentation with query patterns", "Migration history and versioning" |
| `[SECURITY_GUIDELINES]` | Specify the security guidelines | "Secure coding standards (OWASP)", "Authentication/authorization patterns", "Data handling and encryption requirements", "Incident reporting procedures" |
| `[UNIT_TESTING]` | Specify the unit testing | "Jest/JUnit for unit tests, 80% coverage target", "Mocking external dependencies", "Test naming: should_ExpectedBehavior_When_StateUnderTest", "TDD for critical business logic" |
| `[INTEGRATION_TESTING]` | Specify the integration testing | "Testcontainers for database/message queue tests", "API contract testing with Pact", "Service virtualization for external APIs", "Test data factories" |
| `[END_TO_END_TESTING]` | Specify the end to end testing | "Cypress/Playwright for UI flows", "Critical user journey coverage", "Visual regression testing", "Cross-browser testing matrix" |
| `[PERFORMANCE_TESTING]` | Specify the performance testing | "k6/Gatling for load testing", "Baseline performance benchmarks", "Performance regression detection in CI", "APM integration for profiling" |
| `[SECURITY_TESTING]` | Specify the security testing | "SAST with SonarQube/Checkmarx", "DAST with OWASP ZAP", "Dependency scanning with Snyk", "Annual penetration testing" |
| `[LOAD_TESTING]` | Specify the load testing | "2x expected peak load tests", "Sustained load for 1 hour", "Identify breaking points and bottlenecks", "Monthly load test schedule" |
| `[STRESS_TESTING]` | Specify the stress testing | "Gradual load increase until failure", "Resource exhaustion scenarios", "Recovery time measurement", "Failover verification" |
| `[CHAOS_ENGINEERING]` | Specify the chaos engineering | "Gremlin/LitmusChaos experiments", "Game days for incident practice", "Network partition simulations", "Dependency failure injection" |
| `[AB_TESTING]` | Specify the ab testing | "Feature flags with LaunchDarkly/Split", "Statistical significance requirements", "Gradual rollout with monitoring", "Experiment documentation and learnings" |
| `[TEST_AUTOMATION]` | Specify the test automation | "CI pipeline: lint, unit, integration, E2E", "Parallel test execution", "Flaky test quarantine process", "Test result dashboards and trends" |
| `[MIGRATION_APPROACH]` | Specify the migration approach | "Strangler fig pattern for gradual migration", "API gateway for traffic routing", "Feature parity validation", "Phased rollout by customer segment" |
| `[LEGACY_SYSTEM]` | Specify the legacy system | "Monolithic Java application on Oracle", "COBOL mainframe batch processing", "On-premises .NET application", "Legacy SOAP services" |
| `[MIGRATION_TIMELINE]` | Specify the migration timeline | "6 months" |
| `[DATA_MIGRATION]` | Specify the data migration | "ETL with validation checksums", "Incremental sync during parallel run", "Data cleansing and transformation", "Zero-downtime cutover with CDC" |
| `[CUTOVER_STRATEGY]` | Specify the cutover strategy | "Big bang weekend cutover", "Phased migration by module", "Traffic shifting with feature flags", "Blue-green with instant rollback" |
| `[ROLLBACK_PLAN]` | Specify the rollback plan | "Database point-in-time recovery", "Traffic routing back to legacy", "Data sync reversal procedures", "Communication templates prepared" |
| `[PARALLEL_RUNNING]` | Specify the parallel running | "2-week parallel operation period", "Result comparison and reconciliation", "Automatic discrepancy alerting", "Gradual traffic shifting" |
| `[USER_TRAINING]` | Specify the user training | "Role-based training sessions", "Video tutorials and documentation", "Sandbox environment for practice", "Super-user champion program" |
| `[CHANGE_MANAGEMENT]` | Specify the change management | "Stakeholder communication plan", "Change impact assessment", "User acceptance testing sign-off", "Go/no-go decision criteria" |
| `[SUCCESS_CRITERIA]` | Specify the success criteria | "All critical functions operational", "Performance within SLA targets", "Zero data loss verification", "User satisfaction survey > 80%" |

### Healthcare System Architecture
```
Design a HIPAA-compliant architecture for MedConnect patient management system that serves healthcare providers with enterprise-grade requirements. The system should implement layered architecture pattern and support healthcare domain.

Core Architecture Requirements:
- Implement Angular frontend using Angular Material framework
- Design modular backend services (patient, appointment, billing, EHR, reporting) with Java Spring Boot
- Use encrypted PostgreSQL for PHI data with audit logging
- Integrate HL7 FHIR messaging for healthcare interoperability
- Deploy on Azure with container orchestration

Security Implementation:
- Implement multi-factor authentication and attribute-based authorization
- Use end-to-end encryption for all PHI data protection
- Apply network segmentation, API security scanning, and access controls
- Follow HIPAA, HITECH compliance frameworks
- Include comprehensive audit logging and compliance monitoring
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Architecture Design Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Software Development](../../technology/Software Development/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating design comprehensive system architectures including distributed systems, apis, databases, microservices, and enterprise solutions with scalability, security, and maintainability considerations.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Start with business requirements and quality attributes**
2. **Consider scalability from day one, not as an afterthought**
3. **Design for failure - implement circuit breakers and fallbacks**
4. **Prioritize security throughout all architectural layers**
5. **Document architectural decisions and trade-offs**
6. **Plan for monitoring and observability early**
7. **Design APIs with versioning and backward compatibility**
8. **Consider data consistency patterns for distributed systems**
9. **Plan deployment and rollback strategies upfront**
10. **Include performance budgets and SLA requirements**