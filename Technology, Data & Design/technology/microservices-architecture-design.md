---
category: technology
related_templates:
- technology/Software-Development/architecture-design.md
- technology/DevOps-Cloud/container-orchestration.md
- technology/Data-Engineering/integration-patterns.md
tags:
- microservices
- distributed-systems
- api-design
- event-driven
title: Microservices Architecture Design
use_cases:
- Designing microservices architectures with service decomposition, API contracts, and communication patterns achieving 99.9%+ availability at scale
- Implementing event-driven microservices with Kafka/RabbitMQ for decoupled, scalable systems with eventual consistency
- Migrating monolithic applications to microservices using strangler pattern with incremental decomposition and risk mitigation
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: microservices-architecture-design
---

# Microservices Architecture Design

## Purpose
Design and implement microservices architectures covering service decomposition, API design, communication patterns, data management, resilience patterns, and operational concerns achieving scalable, maintainable distributed systems.

## 🚀 Quick Microservices Prompt

> Design microservices for **[APPLICATION]** with **[SERVICE_COUNT]** services handling **[USERS]** concurrent users, **[TPS]** TPS. Decomposition: **[DDD/BUSINESS_FUNCTION]**. APIs: **[REST/GRPC]** with **[AUTH_METHOD]**. Async: **[KAFKA/RABBITMQ]** for events. Data: database per service (**[POSTGRES/MONGO]**). Orchestration: **[KUBERNETES]** with **[SERVICE_MESH]**. Resilience: circuit breakers, retry, timeout. Target: **[AVAILABILITY]**% availability, **[LATENCY]**ms p99.

---

## Template

Design microservices architecture for {APPLICATION} with {SERVICE_COUNT} services supporting {USER_LOAD} users achieving {AVAILABILITY_TARGET}% availability and {LATENCY_TARGET}ms p99 latency.

**SERVICE DECOMPOSITION**

Apply domain-driven design for meaningful service boundaries. Bounded context identification: map business domains, identify ubiquitous language per context, define context boundaries. Aggregate design: one aggregate per service (Order aggregate owns OrderItems), aggregate root enforces invariants. Context mapping: upstream/downstream relationships, anti-corruption layers for legacy integration, shared kernel only for truly shared concepts. Team alignment: Conway's Law, one team per service (2-pizza team size), full ownership including operations.

Choose decomposition strategy matching organizational context. Business capability: align services to business functions (Payments, Inventory, Shipping), clear ownership, stable boundaries. Subdomain classification: core (competitive advantage, build), supporting (necessary but not differentiating, build simple), generic (commodity, buy/use SaaS). User journey: decompose around user experiences for frontend-focused applications, BFF pattern for channel-specific APIs. Data partitioning: separate by data ownership, avoid shared databases, clear data contracts between services.

Size services appropriately avoiding nano-services and monoliths. Right-sizing indicators: deployable independently, owned by single team, <10K lines of code typical, 2-week rewrite rule. Too small signs: excessive inter-service communication, distributed monolith, chatty APIs, complex orchestration. Too large signs: multiple teams needed, long deployment cycles, mixed concerns, frequent merge conflicts. Strangler pattern for migration: extract services incrementally from monolith, facade routing, gradual traffic shift.

**SERVICE COMMUNICATION**

Design synchronous communication for request-response patterns. REST APIs: resource-oriented design, OpenAPI 3.0 specifications, JSON payloads, HTTP semantics (GET/POST/PUT/DELETE). gRPC: Protocol Buffers for schema, streaming support, better performance than REST (binary, HTTP/2), service mesh integration. API versioning: URL path versioning (/v1/orders) for major versions, header versioning for minor, backward compatibility required. Error handling: consistent error format (RFC 7807 Problem Details), meaningful status codes, correlation IDs for tracing.

Implement asynchronous messaging for event-driven patterns. Kafka for event streaming: topics per domain event, partition by entity key for ordering, consumer groups for scaling, replay capability. RabbitMQ for task queues: work queues for background jobs, pub/sub for notifications, dead letter exchanges for failures. Event schema: CloudEvents standard, Avro/Protobuf with schema registry, backward-compatible evolution. Exactly-once processing: idempotent consumers, deduplication with message IDs, transactional outbox pattern.

Configure API Gateway for cross-cutting concerns. Gateway functions: authentication/authorization, rate limiting, request transformation, response caching, routing. Technology options: Kong (open source, extensible), AWS API Gateway (managed, serverless), Apigee (enterprise, analytics). Rate limiting: per-client limits (1000 req/min), sliding window, graceful degradation (429 with Retry-After). Security: OAuth 2.0/JWT validation, API key management, mTLS termination, WAF integration.

**DATA MANAGEMENT**

Implement database per service for loose coupling. Service database: PostgreSQL per service for relational, MongoDB for documents, Redis for caching, technology matches use case. Data isolation: no shared databases, no cross-service queries, API-only data access. Schema management: Flyway/Liquibase migrations, version-controlled schemas, backward-compatible changes. Data ownership: service owns its data completely, authoritative source for domain entities.

Handle distributed data patterns. Event-driven sync: publish domain events on state changes, consumers maintain local projections. Saga pattern: distributed transactions via choreography (event-based) or orchestration (coordinator), compensating transactions for rollback. CQRS: separate command (write) and query (read) models, optimized for each workload, eventual consistency acceptable. Data consistency: embrace eventual consistency (seconds acceptable for most cases), strong consistency only where required (payments).

Design event sourcing for audit and temporal queries. Event store: append-only log of domain events (OrderCreated, PaymentProcessed), Kafka or EventStoreDB. State reconstruction: replay events to rebuild current state, snapshots for performance (every 100 events). Projections: build read models from events, multiple projections for different query patterns. Benefits: complete audit trail, temporal queries (state at any point), event replay for debugging.

**RESILIENCE PATTERNS**

Implement circuit breaker preventing cascade failures. Circuit breaker states: closed (normal), open (failing fast), half-open (testing recovery). Configuration: open after 5 consecutive failures, 30-second open duration, 3 successful calls to close. Implementation: Resilience4j (Java), Polly (.NET), Istio circuit breaker (service mesh). Fallback behavior: cached responses, default values, graceful degradation message.

Configure retry and timeout for transient failures. Retry policy: exponential backoff (100ms, 200ms, 400ms), max 3 retries, jitter to avoid thundering herd. Idempotency: retry-safe operations only, idempotency keys for non-idempotent calls. Timeout strategy: connect timeout (1-5s), read timeout (5-30s based on operation), deadline propagation through call chain. Bulkhead pattern: thread pool isolation per dependency, prevent single slow dependency from exhausting resources.

Design health checks for service observability. Liveness probe: process is running, restart if unhealthy, check internal state (no deadlocks). Readiness probe: ready to receive traffic, dependency health (database, cache), remove from load balancer if not ready. Startup probe: slow-starting containers, prevent liveness killing during startup, failureThreshold × periodSeconds > max startup. Deep health checks: verify downstream dependencies, but cache results to avoid cascading health check failures.

**SERVICE MESH AND NETWORKING**

Implement service mesh for observability and security. Mesh selection: Istio (full-featured, complex), Linkerd (lightweight, simpler), Consul Connect (HashiCorp ecosystem). Traffic management: canary deployments (5% → 25% → 100%), traffic mirroring for testing, fault injection for chaos. mTLS: automatic encryption between services, certificate rotation, zero-trust security. Observability: automatic distributed tracing, service-to-service metrics, traffic visualization.

Configure service discovery and load balancing. Service discovery: Kubernetes DNS (native), Consul (multi-platform), automatic registration and deregistration. Load balancing: round-robin (simple), least connections (better for varying response times), consistent hashing (stateful). Connection management: connection pooling, keep-alive settings, graceful connection draining during deployments.

**SECURITY ARCHITECTURE**

Implement authentication and authorization. Service-to-service: mTLS with SPIFFE/SPIRE workload identity, service accounts, no shared credentials. User authentication: OAuth 2.0 with JWT tokens, short-lived access tokens (15 minutes), refresh token rotation. Authorization: RBAC at service level, OPA/Gatekeeper for policy enforcement, attribute-based access for fine-grained control. API security: rate limiting, input validation, output encoding, OWASP API Security Top 10 compliance.

Secure data and network. Encryption at rest: AES-256 for databases, KMS-managed keys, field-level encryption for sensitive data. Encryption in transit: TLS 1.3 everywhere, mTLS between services, encrypted message queues. Network policies: Kubernetes NetworkPolicy, default deny, explicit allow rules. Secrets management: HashiCorp Vault or cloud KMS, automatic rotation, no secrets in code or environment variables.

**DEPLOYMENT AND OPERATIONS**

Configure Kubernetes deployment patterns. Container configuration: multi-stage builds, distroless base images, resource limits (CPU, memory). Deployment strategy: rolling update (maxSurge 25%, maxUnavailable 0), blue-green for critical services. Pod configuration: anti-affinity for spreading across nodes/AZs, PodDisruptionBudget for availability. Auto-scaling: HPA based on CPU/memory (target 70%), custom metrics (requests/second, queue depth), KEDA for event-driven.

Implement GitOps for deployment automation. ArgoCD/Flux: Git as source of truth, automatic sync, drift detection and remediation. Helm charts: chart per service, environment-specific values, umbrella charts for full stack. Deployment pipeline: PR creates preview environment, merge to main deploys to staging, promotion to production with approval.

**OBSERVABILITY STACK**

Implement comprehensive monitoring. Metrics: Prometheus for collection, Grafana for visualization, RED metrics (Rate, Errors, Duration) per service. Distributed tracing: Jaeger/Tempo, automatic instrumentation (OpenTelemetry), trace context propagation. Logging: structured JSON, correlation IDs, centralized aggregation (Loki/Elasticsearch), log-based alerting. Dashboards: service health overview, dependency graphs, SLO tracking, business metrics.

Configure alerting for operational awareness. SLO-based alerts: error budget burn rate, multi-window alerts (fast burn + slow burn). Symptom-based: alert on user impact (latency, errors), not causes (CPU, memory). On-call integration: PagerDuty/Opsgenie, escalation policies, runbook links in alerts.

Deliver microservices architecture as:

1. **SERVICE CATALOG** - Service list with boundaries, ownership, APIs, dependencies, data stores

2. **API CONTRACTS** - OpenAPI/Protobuf specifications, versioning strategy, breaking change policy

3. **COMMUNICATION PATTERNS** - Sync vs async decisions, event schemas, saga definitions

4. **DATA ARCHITECTURE** - Database per service design, data ownership, consistency requirements

5. **RESILIENCE CONFIGURATION** - Circuit breaker, retry, timeout settings per service interaction

6. **DEPLOYMENT SPECIFICATION** - Kubernetes manifests, Helm charts, scaling policies, health checks

7. **SECURITY CONTROLS** - Authentication, authorization, network policies, encryption

8. **OBSERVABILITY SETUP** - Metrics, traces, logs configuration, dashboards, alerting rules

---

## Usage Examples

### Example 1: E-commerce Platform
**Prompt:** Design microservices for EcommercePlatform with 12 services handling 100K concurrent users, 5000 TPS achieving 99.95% availability and <200ms p99 latency.

**Expected Output:** Service decomposition: User (authentication, profiles), Product (catalog, search), Cart (session management), Order (order lifecycle), Payment (payment processing), Inventory (stock management), Fulfillment (shipping, tracking), Notification (email, SMS, push), Promotion (coupons, discounts), Review (ratings, reviews), Analytics (tracking, reporting), Gateway (API aggregation). Bounded contexts: Order owns order state, Payment owns payment state, Inventory owns stock counts—no shared databases. Communication: REST APIs between services (OpenAPI 3.0), Kafka for async events (order-created, payment-completed, inventory-reserved), saga for order fulfillment (choreography with compensating transactions). Data: PostgreSQL per service (User, Order, Payment), MongoDB (Product catalog, Reviews), Redis (Cart sessions, caching), Elasticsearch (Product search). Resilience: circuit breaker on Payment service (5 failures → open 30s), retry with backoff for Inventory calls, 5s timeout on all synchronous calls. Deployment: EKS with Istio service mesh, HPA (2-50 pods per service), canary deployments for Order and Payment. Observability: Prometheus + Grafana (RED dashboards), Jaeger tracing, Loki for logs. Security: OAuth 2.0 + JWT for user auth, mTLS between services, API rate limiting (1000 req/min per user).

### Example 2: Financial Services Platform
**Prompt:** Design microservices for TradingPlatform with 20 services handling 10K concurrent traders, 50K orders/day achieving 99.99% availability and <50ms p99 latency with PCI-DSS compliance.

**Expected Output:** Service decomposition: core domain (Account, Portfolio, Order, Execution, Position), supporting (Market Data, Risk, Compliance, Reporting, Notification), generic (Authentication, Authorization, Audit). High-frequency paths: Order → Execution → Position optimized for latency (<10ms internal). Communication: gRPC for low-latency internal calls (Order → Execution), Kafka for event streaming (trades, market data), CQRS for Position service (command: update positions, query: portfolio views). Data: PostgreSQL with synchronous replication for transactional data, TimescaleDB for time-series (market data, trade history), event sourcing for Order (complete audit trail). Resilience: circuit breaker with fallback to cached market data, bulkhead isolation (separate thread pools for trading vs reporting), 2s timeout on external market feeds. Compliance: event sourcing provides immutable audit trail, PCI-DSS encryption (data at rest with HSM, TLS 1.3), field-level encryption for sensitive data. Deployment: on-premise OpenShift for regulatory requirements, blue-green deployments for zero-downtime, geo-redundant DR (RPO <1 minute). Security: mTLS everywhere, OPA policies for trade authorization, complete audit logging (who, what, when), SOC 2 controls.

### Example 3: SaaS Multi-tenant Platform
**Prompt:** Design microservices for SaaSPlatform with 15 services supporting 500 tenants, 50K users achieving 99.9% availability with tenant isolation and per-tenant customization.

**Expected Output:** Service decomposition: Tenant (provisioning, configuration), User (authentication, authorization), Subscription (billing, plans), core product services (varies by SaaS function), Integration (webhooks, API), Analytics (usage tracking, billing metrics). Multi-tenancy pattern: tenant context in JWT claims, tenant-aware service layer, logical isolation (shared infrastructure, tenant column in all tables). Data isolation: tenant_id in all queries (enforced at repository layer), row-level security in PostgreSQL, per-tenant encryption keys for sensitive data. Communication: REST APIs with tenant context header, Kafka with tenant-partitioned topics (enables per-tenant ordering), webhook delivery per tenant. Customization: feature flags per tenant (LaunchDarkly), configuration service for tenant-specific settings, plugin architecture for custom integrations. Scalability: noisy neighbor protection (per-tenant rate limiting, resource quotas), horizontal scaling based on aggregate load, dedicated resources for enterprise tenants. Deployment: shared Kubernetes cluster with namespace isolation, Helm values per tenant tier (starter/growth/enterprise), canary per tenant cohort. Security: tenant isolation validation on every request, data access audit logging, GDPR compliance (per-tenant data export, deletion).

---

## Cross-References

- [Architecture Design](Software-Development/architecture-design.md) - System architecture patterns and decisions
- [Container Orchestration](DevOps-Cloud/container-orchestration.md) - Kubernetes deployment patterns
- [Integration Patterns](Data-Engineering/integration-patterns.md) - API and messaging patterns
