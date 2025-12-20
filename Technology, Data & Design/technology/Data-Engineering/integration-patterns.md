---
category: technology
related_templates:
- technology/Data-Engineering/data-pipeline-design.md
- technology/DevOps-Cloud/cloud-architecture.md
- technology/Software-Development/architecture-design.md
tags:
- integration-patterns
- api-integration
- event-driven
- messaging
title: Integration Patterns
use_cases:
- Designing API integration architectures with Kong/AWS API Gateway, OAuth 2.0, rate limiting achieving <100ms latency at 10K TPS
- Implementing event-driven architectures with Kafka/RabbitMQ for decoupled, scalable microservices with exactly-once processing
- Building data synchronization patterns using CDC, batch sync, and real-time streaming for multi-system data consistency
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: integration-patterns
---

# Integration Patterns

## Purpose
Design comprehensive integration architectures covering API patterns, messaging systems, event-driven architecture, and data synchronization achieving scalability, reliability, and maintainability for enterprise system interoperability.

## Template

Design integration architecture for {USE_CASE} connecting {SOURCE_SYSTEMS} to {TARGET_SYSTEMS} achieving {THROUGHPUT} throughput with {LATENCY} latency and {RELIABILITY}% reliability.

**INTEGRATION PATTERN SELECTION**

Choose pattern based on coupling requirements and latency tolerance. Synchronous request-reply: tight coupling, immediate response required, suitable for <1000 TPS, REST/gRPC APIs. Asynchronous messaging: loose coupling, eventual consistency acceptable, suitable for >1000 TPS, queue or topic-based. Event-driven: publish-subscribe, multiple consumers, event sourcing for audit, real-time reactions. Hybrid: synchronous for queries, async for commands, balance responsiveness with scalability.

Match pattern to data characteristics. Real-time data (<1 second freshness): event streaming with Kafka/Kinesis. Near-real-time (1-15 minutes): CDC with Debezium, micro-batch processing. Batch (hourly/daily): traditional ETL, file-based integration, scheduled jobs. Request-response: API calls for on-demand data retrieval, caching for performance.

Consider operational complexity tradeoffs. Synchronous: simpler debugging, single transaction boundary, cascading failures risk. Asynchronous: complex debugging (distributed tracing required), retry handling, dead letter management. Event-driven: event schema management, consumer lag monitoring, replay capability. Choose simplest pattern that meets requirements.

**API INTEGRATION**

Design REST APIs following best practices. Resource-oriented design: nouns for resources (/orders, /customers), HTTP verbs for actions. Versioning strategy: URL path (/v1/orders) for breaking changes, header versioning for minor. Response format: JSON with consistent structure, RFC 7807 problem details for errors. HATEOAS: include links for discoverability (optional but useful for complex APIs).

Configure API Gateway for cross-cutting concerns. Gateway selection: Kong (open source, flexible), AWS API Gateway (managed, serverless), Apigee (enterprise, analytics). Authentication: OAuth 2.0 + JWT for user context, API keys for service-to-service, mTLS for zero-trust. Rate limiting: per-client limits (1000 req/min), burst handling, graceful degradation on limit. Request transformation: header injection, payload modification, protocol translation.

Implement resilience patterns at API layer. Timeout configuration: connect timeout (1-5s), read timeout (5-30s), fail fast on slow dependencies. Retry logic: exponential backoff with jitter (1s, 2s, 4s), max 3 retries, idempotency keys for safety. Circuit breaker: open after 5 consecutive failures, half-open after 30s, close on success. Bulkhead: separate thread pools per dependency, prevent cascading failures.

**MESSAGING ARCHITECTURE**

Select message broker matching requirements. Apache Kafka: high throughput (millions msg/sec), ordered within partition, replay from offset, strong durability. RabbitMQ: flexible routing, message acknowledgment, lower throughput but simpler operations. AWS SQS/SNS: managed, auto-scaling, integrated with AWS ecosystem, limited features. Azure Service Bus: enterprise features, transactions, sessions, Azure-native.

Design topics and queues for scalability. Kafka topics: partition by entity key for ordering, 10-50 partitions for parallelism, replication factor 3. Queue patterns: work queue (competing consumers), pub/sub (fan-out), routing (content-based). Message retention: 7 days default for replay, longer for audit, compacted topics for latest-value semantics. Consumer groups: separate groups per use case, track offset per group.

Configure message delivery guarantees. At-most-once: fire and forget, lowest latency, acceptable data loss. At-least-once: acknowledge after processing, retry on failure, requires idempotent consumers. Exactly-once: transactional processing, deduplication, highest complexity and latency. Choose based on data criticality: financial transactions need exactly-once, logs can be at-most-once.

Handle message failures systematically. Dead letter queue (DLQ): route failed messages after max retries, preserve for investigation. Poison message handling: detect and quarantine malformed messages, don't block queue. Retry strategies: immediate retry for transient failures, delayed retry for rate limits. Monitoring: consumer lag, DLQ depth, processing latency, error rates by error type.

**EVENT-DRIVEN ARCHITECTURE**

Design events for loose coupling. Event schema: CloudEvents standard, include type, source, timestamp, correlation ID. Schema registry: Confluent Schema Registry, AWS Glue Schema Registry, version management. Backward compatibility: add fields as optional, don't remove or rename, handle unknown fields. Event granularity: domain events (OrderCreated), not CRUD events (OrderTableRowInserted).

Implement event sourcing for audit and replay. Event store: Kafka (simple), EventStoreDB (specialized), PostgreSQL with append-only table. State reconstruction: replay events to rebuild current state, snapshots for performance. Temporal queries: query state at any point in time, essential for financial and compliance. Event versioning: upcast old events to new schema, maintain backward compatibility.

Choose orchestration vs choreography. Choreography: services react to events independently, highly decoupled, harder to understand flow. Orchestration: central coordinator (Temporal, Camunda), explicit workflow, easier to debug. Saga pattern: distributed transactions via compensating actions, combine with either approach. Recommendation: choreography for simple flows, orchestration for complex multi-step processes.

**DATA SYNCHRONIZATION**

Select sync strategy matching consistency requirements. Real-time CDC: Debezium captures database changes, <1 second latency, no application changes. Scheduled batch: periodic full or incremental extracts, simpler but higher latency. Event-driven: application publishes events on change, requires code changes but cleanest. API polling: pull changes via API, suitable for external systems without CDC access.

Handle synchronization conflicts. Last-writer-wins: simple, timestamp-based, acceptable for non-critical data. Version vectors: track per-node versions, detect conflicts, require merge logic. Business rules: domain-specific conflict resolution, human review for complex cases. Conflict avoidance: single source of truth per field, partition ownership by region/time.

Implement data consistency patterns. Eventual consistency: changes propagate with delay, suitable for most read-heavy systems. Strong consistency: synchronous replication, higher latency, required for critical operations. Saga pattern: distributed transactions with compensation, maintain consistency across services. Outbox pattern: transactional outbox table, ensure event publish with database change.

**CHANGE DATA CAPTURE (CDC)**

Configure CDC for database replication. Debezium: open source, Kafka-native, supports PostgreSQL/MySQL/MongoDB/SQL Server. AWS DMS: managed service, supports heterogeneous replication, Aurora/RDS optimized. Oracle GoldenGate: enterprise, real-time, supports complex transformations. Striim: streaming CDC, built-in transformations, monitoring dashboard.

Design CDC topics and schemas. Topic per table: source.database.schema.table naming convention, enables selective consumption. Schema evolution: Avro with schema registry, handle column additions/renames. Initial snapshot: full table snapshot followed by streaming changes, consistent starting point. Delete handling: tombstone messages for deletes, soft delete vs hard delete considerations.

Monitor CDC pipeline health. Replication lag: time between source change and Kafka publish, alert on >5 seconds. Slot monitoring: PostgreSQL replication slots, prevent WAL bloat with slot advancement. Schema changes: detect DDL events, pause pipeline for breaking changes, automated handling for additive changes.

**SERVICE MESH AND MICROSERVICES**

Implement service mesh for microservices communication. Mesh selection: Istio (full-featured, complex), Linkerd (lightweight, simpler), Consul Connect (HashiCorp ecosystem). Traffic management: canary deployments, traffic splitting, fault injection for testing. mTLS: automatic encryption between services, certificate rotation, zero-trust security. Observability: automatic distributed tracing, service-to-service metrics, topology visualization.

Design inter-service communication patterns. Synchronous: REST/gRPC for request-response, use for queries and simple commands. Asynchronous: message queue for commands, event bus for events, use for decoupling. Service discovery: Kubernetes DNS, Consul, AWS Cloud Map for dynamic endpoint resolution. Load balancing: round-robin, least connections, consistent hashing for stateful workloads.

Implement resilience patterns. Circuit breaker: Resilience4j, Istio circuit breaker, fail fast on unhealthy dependencies. Retry with backoff: exponential backoff with jitter, max retries, idempotency required. Bulkhead: separate thread pools, connection limits per dependency. Timeout: explicit timeouts on all calls, propagate deadline through call chain.

**SECURITY AND COMPLIANCE**

Secure integration endpoints. Authentication: OAuth 2.0 for user context, mTLS for service-to-service, API keys for simple cases. Authorization: RBAC for role-based, ABAC for attribute-based, policy engines (OPA) for complex rules. Encryption: TLS 1.3 in transit, AES-256 at rest, end-to-end encryption for sensitive data. Rate limiting: protect against abuse, per-client and global limits, graceful degradation.

Implement audit and compliance. Audit logging: log all integration calls with correlation IDs, who/what/when/where. Data lineage: track data flow through integrations, required for GDPR/CCPA. Retention policies: comply with regulatory requirements, automated deletion. PII handling: mask in logs, encrypt in transit and at rest, access controls.

**MONITORING AND OBSERVABILITY**

Track integration health metrics. Throughput: messages/sec, requests/sec by endpoint, track trends. Latency: p50, p95, p99 latency, separate upstream vs downstream. Error rates: by error type, by endpoint, by client, set alerting thresholds. Availability: uptime percentage, MTBF, MTTR tracking.

Implement distributed tracing. Tracing tools: Jaeger, Zipkin, AWS X-Ray, Datadog APM. Trace propagation: W3C trace context headers, consistent across all services. Span design: meaningful span names, include relevant attributes, sample appropriately (1-10%). Root cause analysis: trace waterfall for debugging, correlate with logs and metrics.

Configure alerting for operational awareness. Critical alerts: integration down, error rate >5%, latency p99 >SLA. Warning alerts: consumer lag increasing, approaching rate limits, certificate expiration. Dashboards: integration health overview, per-integration details, dependency status.

Deliver integration architecture as:

1. **ARCHITECTURE DIAGRAM** - Component diagram showing systems, integration layer, data flows, protocols

2. **API SPECIFICATION** - OpenAPI specs, authentication config, rate limits, versioning strategy

3. **MESSAGING DESIGN** - Topic/queue structure, schemas, delivery guarantees, DLQ handling

4. **EVENT CATALOG** - Event types, schemas, producers, consumers, versioning approach

5. **SYNC CONFIGURATION** - CDC setup, sync schedules, conflict resolution, consistency guarantees

6. **SECURITY CONTROLS** - Auth/authz configuration, encryption, audit logging, compliance mapping

7. **MONITORING SETUP** - Metrics, alerts, dashboards, tracing configuration

---

## Usage Examples

### Example 1: E-commerce Order Processing
**Prompt:** Design integration architecture for OrderProcessing connecting web/mobile apps, payment gateway, inventory system, and shipping carriers achieving 5K orders/hour with <200ms API latency and 99.9% reliability.

**Expected Output:** Architecture: synchronous API for order placement (immediate confirmation), async messaging for fulfillment (decoupled processing). API layer: Kong Gateway with OAuth 2.0 (customer auth) + API keys (partner auth), rate limiting 100 req/min per customer, JWT validation. Order API: REST with OpenAPI 3.0, /v1/orders POST for creation, GET for status, webhook callbacks for updates. Messaging: Kafka topics (order-created, payment-completed, inventory-reserved, shipment-created), partition by customer_id, 20 partitions per topic. Event schema: Avro with schema registry, CloudEvents envelope, backward-compatible evolution. Payment integration: synchronous API call with 10s timeout, circuit breaker (5 failures → open), retry with idempotency key. Inventory: event-driven reservation on order-created, compensating event on payment failure. Shipping: async API for label generation, webhook for tracking updates. Error handling: DLQ per topic, 3 retries with exponential backoff, manual review queue in admin UI. Monitoring: Grafana dashboard (orders/hour, payment success rate, fulfillment latency), PagerDuty for critical alerts.

### Example 2: Financial Market Data
**Prompt:** Design integration architecture for MarketDataDistribution connecting exchange feeds, trading systems, and risk analytics achieving 100K messages/sec with <10ms latency and exactly-once processing for trade execution.

**Expected Output:** Architecture: ultra-low-latency streaming with Kafka for distribution, kernel bypass networking for exchange connectivity. Ingestion: direct market feed adapters (FIX protocol), normalize to internal format, timestamp at ingestion. Kafka configuration: 100 partitions, replication factor 3, acks=all for durability, linger.ms=0 for latency. Topic structure: market-data-raw (all ticks), market-data-aggregated (1-second bars), trade-signals (strategy output). Processing: Kafka Streams for real-time aggregation, Flink for complex event processing (pattern detection). Trade execution: exactly-once semantics with Kafka transactions, idempotent producer, atomic read-process-write. Risk integration: parallel consumer group, <100ms latency requirement, circuit breaker on risk system. Schema: Protobuf for performance (smaller, faster than Avro), schema registry for versioning. Monitoring: consumer lag <100ms alert, end-to-end latency tracking, message rate anomaly detection. DR: cross-region Kafka MirrorMaker, <1 minute failover, data reconciliation post-failover. Compliance: full message capture for regulatory reporting, 7-year retention, timestamp audit trail.

### Example 3: Healthcare Data Exchange
**Prompt:** Design integration architecture for HealthDataExchange connecting EHR systems, labs, pharmacies, and insurance with HL7 FHIR APIs achieving HIPAA compliance and <1 hour data freshness.

**Expected Output:** Architecture: FHIR REST APIs for synchronous queries, event-driven for notifications, batch for bulk data exchange. API Gateway: AWS API Gateway with OAuth 2.0 + SMART on FHIR, mTLS for system-to-system, audit logging enabled. FHIR server: HAPI FHIR, support for Patient, Encounter, Observation, MedicationRequest resources. Interoperability: HL7v2 to FHIR transformation (integration engine), CDA document ingestion. CDC: Debezium on PostgreSQL, replicate clinical data changes to Kafka, <5 minute latency. Event notifications: FHIR Subscriptions for real-time alerts (new lab result, medication change). Batch sync: nightly bulk export for analytics, FHIR $export operation, NDJSON format to S3. Security: encryption at rest (AES-256, customer-managed keys), TLS 1.3 in transit, PHI access logging. Consent management: patient consent records, enforce access restrictions, audit consent checks. Error handling: quarantine PHI violations, mandatory review before reprocessing. Compliance: BAA with all cloud providers, HIPAA audit controls, breach notification workflow. Monitoring: data freshness per source, consent violation alerts, API latency by operation type.

---

## Cross-References

- [Data Pipeline Design](data-pipeline-design.md) - Pipeline patterns for data integration
- [Cloud Architecture](../DevOps-Cloud/cloud-architecture.md) - Infrastructure supporting integrations
- [Architecture Design](../Software-Development/architecture-design.md) - System architecture patterns
