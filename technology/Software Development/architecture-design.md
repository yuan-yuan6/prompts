---
category: technology/Software Development
last_updated: 2025-11-09
related_templates:
- cloud-architecture-framework.md
- site-reliability-engineering.md
- cloud-migration-strategy.md
tags:
- communication
- design
- security
- technology
- template
title: Architecture Design Template
use_cases:
- Creating design comprehensive system architectures including distributed systems,
  apis, databases, microservices, and enterprise solutions with scalability, security,
  and maintainability considerations.
- Project planning and execution
- Strategy development
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
| `[SYSTEM_NAME]` | Specify the system name | "John Smith" |
| `[SYSTEM_PURPOSE]` | Specify the system purpose | "[specify value]" |
| `[BUSINESS_DOMAIN]` | Specify the business domain | "[specify value]" |
| `[TARGET_USERS]` | Specify the target users | "[specify value]" |
| `[EXPECTED_LOAD]` | Specify the expected load | "[specify value]" |
| `[GEOGRAPHIC_DISTRIBUTION]` | Specify the geographic distribution | "[specify value]" |
| `[REGULATORY_REQUIREMENTS]` | Specify the regulatory requirements | "[specify value]" |
| `[BUDGET_CONSTRAINTS]` | Specify the budget constraints | "$500,000" |
| `[TIMELINE]` | Specify the timeline | "6 months" |
| `[SUCCESS_METRICS]` | Specify the success metrics | "[specify value]" |
| `[PRIMARY_PATTERN]` | Specify the primary pattern | "[specify value]" |
| `[SECONDARY_PATTERNS]` | Specify the secondary patterns | "[specify value]" |
| `[DESIGN_PRINCIPLES]` | Specify the design principles | "[specify value]" |
| `[ARCHITECTURE_STYLE]` | Specify the architecture style | "[specify value]" |
| `[COMMUNICATION_PATTERN]` | Specify the communication pattern | "[specify value]" |
| `[DATA_FLOW_PATTERN]` | Specify the data flow pattern | "[specify value]" |
| `[INTEGRATION_PATTERN]` | Specify the integration pattern | "[specify value]" |
| `[DEPLOYMENT_PATTERN]` | Specify the deployment pattern | "[specify value]" |
| `[SECURITY_PATTERN]` | Specify the security pattern | "[specify value]" |
| `[RESILIENCE_PATTERN]` | Specify the resilience pattern | "[specify value]" |
| `[FRONTEND_COMPONENTS]` | Specify the frontend components | "[specify value]" |
| `[BACKEND_SERVICES]` | Specify the backend services | "[specify value]" |
| `[DATABASE_LAYER]` | Specify the database layer | "[specify value]" |
| `[CACHE_LAYER]` | Specify the cache layer | "[specify value]" |
| `[MESSAGE_QUEUE]` | Specify the message queue | "[specify value]" |
| `[API_GATEWAY]` | Specify the api gateway | "[specify value]" |
| `[LOAD_BALANCER]` | Specify the load balancer | "[specify value]" |
| `[SERVICE_MESH]` | Specify the service mesh | "[specify value]" |
| `[MONITORING_SYSTEM]` | Specify the monitoring system | "[specify value]" |
| `[SECURITY_COMPONENTS]` | Specify the security components | "[specify value]" |
| `[PROGRAMMING_LANGUAGES]` | Specify the programming languages | "[specify value]" |
| `[FRONTEND_FRAMEWORK]` | Specify the frontend framework | "[specify value]" |
| `[BACKEND_FRAMEWORK]` | Specify the backend framework | "[specify value]" |
| `[DATABASE_TECHNOLOGY]` | Specify the database technology | "[specify value]" |
| `[CACHING_SOLUTION]` | Specify the caching solution | "[specify value]" |
| `[MESSAGE_BROKER]` | Specify the message broker | "[specify value]" |
| `[CONTAINER_PLATFORM]` | Specify the container platform | "[specify value]" |
| `[ORCHESTRATION_TOOL]` | Specify the orchestration tool | "[specify value]" |
| `[CLOUD_PROVIDER]` | Specify the cloud provider | "[specify value]" |
| `[DEVELOPMENT_TOOLS]` | Specify the development tools | "[specify value]" |
| `[HORIZONTAL_SCALING]` | Specify the horizontal scaling | "[specify value]" |
| `[VERTICAL_SCALING]` | Specify the vertical scaling | "[specify value]" |
| `[AUTO_SCALING]` | Specify the auto scaling | "[specify value]" |
| `[LOAD_DISTRIBUTION]` | Specify the load distribution | "[specify value]" |
| `[CACHING_STRATEGY]` | Specify the caching strategy | "[specify value]" |
| `[DATABASE_SHARDING]` | Specify the database sharding | "[specify value]" |
| `[CDN_STRATEGY]` | Specify the cdn strategy | "[specify value]" |
| `[RESOURCE_OPTIMIZATION]` | Specify the resource optimization | "[specify value]" |
| `[PERFORMANCE_TARGETS]` | Specify the performance targets | "[specify value]" |
| `[CAPACITY_PLANNING]` | Specify the capacity planning | "[specify value]" |
| `[AUTHENTICATION_METHOD]` | Specify the authentication method | "[specify value]" |
| `[AUTHORIZATION_MODEL]` | Specify the authorization model | "[specify value]" |
| `[DATA_ENCRYPTION]` | Specify the data encryption | "[specify value]" |
| `[NETWORK_SECURITY]` | Specify the network security | "[specify value]" |
| `[API_SECURITY]` | Specify the api security | "[specify value]" |
| `[DATABASE_SECURITY]` | Specify the database security | "[specify value]" |
| `[INFRASTRUCTURE_SECURITY]` | Specify the infrastructure security | "[specify value]" |
| `[APPLICATION_SECURITY]` | Specify the application security | "[specify value]" |
| `[MONITORING_SECURITY]` | Specify the monitoring security | "[specify value]" |
| `[COMPLIANCE_FRAMEWORK]` | Specify the compliance framework | "[specify value]" |
| `[DATA_MODEL]` | Specify the data model | "[specify value]" |
| `[DATABASE_DESIGN]` | Specify the database design | "[specify value]" |
| `[DATA_STORAGE]` | Specify the data storage | "[specify value]" |
| `[DATA_PROCESSING]` | Specify the data processing | "[specify value]" |
| `[DATA_INTEGRATION]` | Specify the data integration | "[specify value]" |
| `[DATA_GOVERNANCE]` | Specify the data governance | "[specify value]" |
| `[DATA_QUALITY]` | Specify the data quality | "[specify value]" |
| `[DATA_BACKUP]` | Specify the data backup | "[specify value]" |
| `[DATA_RECOVERY]` | Specify the data recovery | "[specify value]" |
| `[DATA_ARCHIVAL]` | Specify the data archival | "[specify value]" |
| `[API_ARCHITECTURE]` | Specify the api architecture | "[specify value]" |
| `[API_PROTOCOL]` | Specify the api protocol | "[specify value]" |
| `[API_VERSIONING]` | Specify the api versioning | "[specify value]" |
| `[API_DOCUMENTATION]` | Specify the api documentation | "[specify value]" |
| `[RATE_LIMITING]` | Specify the rate limiting | "[specify value]" |
| `[API_TESTING]` | Specify the api testing | "[specify value]" |
| `[API_MONITORING]` | Specify the api monitoring | "[specify value]" |
| `[API_SECURITY_MEASURES]` | Specify the api security measures | "[specify value]" |
| `[API_ERROR_HANDLING]` | Specify the api error handling | "[specify value]" |
| `[API_RESPONSE_FORMAT]` | Specify the api response format | "[specify value]" |
| `[SERVICE_BOUNDARIES]` | Specify the service boundaries | "[specify value]" |
| `[SERVICE_COMMUNICATION]` | Specify the service communication | "[specify value]" |
| `[SERVICE_DISCOVERY]` | Specify the service discovery | "[specify value]" |
| `[CIRCUIT_BREAKER]` | Specify the circuit breaker | "[specify value]" |
| `[SERVICE_MESH_IMPLEMENTATION]` | Specify the service mesh implementation | "[specify value]" |
| `[EVENT_SOURCING]` | Specify the event sourcing | "[specify value]" |
| `[CQRS_PATTERN]` | Specify the cqrs pattern | "[specify value]" |
| `[SAGA_PATTERN]` | Specify the saga pattern | "[specify value]" |
| `[BULKHEAD_PATTERN]` | Specify the bulkhead pattern | "[specify value]" |
| `[RETRY_LOGIC]` | Specify the retry logic | "[specify value]" |
| `[CLOUD_ARCHITECTURE]` | Specify the cloud architecture | "[specify value]" |
| `[NETWORK_TOPOLOGY]` | Specify the network topology | "[specify value]" |
| `[SERVER_CONFIGURATION]` | Specify the server configuration | "[specify value]" |
| `[CONTAINER_STRATEGY]` | Specify the container strategy | "[specify value]" |
| `[STORAGE_ARCHITECTURE]` | Specify the storage architecture | "[specify value]" |
| `[BACKUP_STRATEGY]` | Specify the backup strategy | "[specify value]" |
| `[DISASTER_RECOVERY]` | Specify the disaster recovery | "[specify value]" |
| `[HIGH_AVAILABILITY]` | Specify the high availability | "[specify value]" |
| `[FAULT_TOLERANCE]` | Specify the fault tolerance | "[specify value]" |
| `[RESOURCE_MANAGEMENT]` | Specify the resource management | "[specify value]" |
| `[DEPLOYMENT_STRATEGY]` | Specify the deployment strategy | "[specify value]" |
| `[ENVIRONMENT_SETUP]` | Specify the environment setup | "[specify value]" |
| `[CICD_PIPELINE_DESIGN]` | Specify the cicd pipeline design | "[specify value]" |
| `[RELEASE_MANAGEMENT]` | Specify the release management | "[specify value]" |
| `[BLUE_GREEN_DEPLOYMENT]` | Specify the blue green deployment | "[specify value]" |
| `[CANARY_DEPLOYMENT]` | Specify the canary deployment | "[specify value]" |
| `[ROLLING_UPDATES]` | Specify the rolling updates | "2025-01-15" |
| `[ROLLBACK_STRATEGY]` | Specify the rollback strategy | "[specify value]" |
| `[CONFIGURATION_MANAGEMENT]` | Specify the configuration management | "[specify value]" |
| `[SECRETS_MANAGEMENT]` | Specify the secrets management | "[specify value]" |
| `[LOGGING_STRATEGY]` | Specify the logging strategy | "[specify value]" |
| `[METRICS_COLLECTION]` | Specify the metrics collection | "[specify value]" |
| `[DISTRIBUTED_TRACING]` | Specify the distributed tracing | "[specify value]" |
| `[HEALTH_CHECKS]` | Specify the health checks | "[specify value]" |
| `[ALERTING_SYSTEM]` | Specify the alerting system | "[specify value]" |
| `[DASHBOARD_DESIGN]` | Specify the dashboard design | "[specify value]" |
| `[SLA_MONITORING]` | Specify the sla monitoring | "[specify value]" |
| `[PERFORMANCE_MONITORING]` | Specify the performance monitoring | "[specify value]" |
| `[ERROR_TRACKING]` | Specify the error tracking | "[specify value]" |
| `[BUSINESS_METRICS]` | Specify the business metrics | "[specify value]" |
| `[EXTERNAL_INTEGRATIONS]` | Specify the external integrations | "[specify value]" |
| `[THIRD_PARTY_APIS]` | Specify the third party apis | "[specify value]" |
| `[DATA_SYNCHRONIZATION]` | Specify the data synchronization | "[specify value]" |
| `[EVENT_DRIVEN_ARCHITECTURE]` | Specify the event driven architecture | "[specify value]" |
| `[MESSAGE_PATTERNS]` | Specify the message patterns | "[specify value]" |
| `[WEBHOOK_MANAGEMENT]` | Specify the webhook management | "[specify value]" |
| `[FILE_TRANSFER]` | Specify the file transfer | "[specify value]" |
| `[REALTIME_COMMUNICATION]` | Specify the realtime communication | "[specify value]" |
| `[BATCH_PROCESSING]` | Specify the batch processing | "[specify value]" |
| `[STREAM_PROCESSING]` | Specify the stream processing | "[specify value]" |
| `[CACHING_LAYERS]` | Specify the caching layers | "[specify value]" |
| `[DATABASE_OPTIMIZATION]` | Specify the database optimization | "[specify value]" |
| `[QUERY_OPTIMIZATION]` | Specify the query optimization | "[specify value]" |
| `[CONNECTION_POOLING]` | Specify the connection pooling | "[specify value]" |
| `[LAZY_LOADING]` | Specify the lazy loading | "[specify value]" |
| `[COMPRESSION]` | Specify the compression | "[specify value]" |
| `[MINIFICATION]` | Specify the minification | "[specify value]" |
| `[IMAGE_OPTIMIZATION]` | Specify the image optimization | "[specify value]" |
| `[CONTENT_DELIVERY]` | Specify the content delivery | "[specify value]" |
| `[RESOURCE_BUNDLING]` | Specify the resource bundling | "[specify value]" |
| `[AVAILABILITY]` | Specify the availability | "[specify value]" |
| `[RELIABILITY]` | Specify the reliability | "[specify value]" |
| `[SCALABILITY]` | Specify the scalability | "[specify value]" |
| `[PERFORMANCE]` | Specify the performance | "[specify value]" |
| `[SECURITY]` | Specify the security | "[specify value]" |
| `[MAINTAINABILITY]` | Specify the maintainability | "[specify value]" |
| `[TESTABILITY]` | Specify the testability | "[specify value]" |
| `[USABILITY]` | Specify the usability | "[specify value]" |
| `[PORTABILITY]` | Specify the portability | "[specify value]" |
| `[INTEROPERABILITY]` | Specify the interoperability | "[specify value]" |
| `[TECHNICAL_RISKS]` | Specify the technical risks | "[specify value]" |
| `[SECURITY_RISKS]` | Specify the security risks | "[specify value]" |
| `[PERFORMANCE_RISKS]` | Specify the performance risks | "[specify value]" |
| `[SCALABILITY_RISKS]` | Specify the scalability risks | "[specify value]" |
| `[INTEGRATION_RISKS]` | Specify the integration risks | "[specify value]" |
| `[OPERATIONAL_RISKS]` | Specify the operational risks | "[specify value]" |
| `[BUSINESS_RISKS]` | Specify the business risks | "[specify value]" |
| `[MITIGATION_STRATEGIES]` | Specify the mitigation strategies | "[specify value]" |
| `[CONTINGENCY_PLANS]` | Specify the contingency plans | "[specify value]" |
| `[RISK_MONITORING]` | Specify the risk monitoring | "[specify value]" |
| `[ARCHITECTURE_DOCUMENTATION]` | Specify the architecture documentation | "[specify value]" |
| `[DESIGN_DECISIONS]` | Specify the design decisions | "[specify value]" |
| `[TRADEOFF_ANALYSIS]` | Specify the tradeoff analysis | "[specify value]" |
| `[IMPLEMENTATION_GUIDE]` | Specify the implementation guide | "[specify value]" |
| `[DEPLOYMENT_GUIDE]` | Specify the deployment guide | "[specify value]" |
| `[OPERATIONS_MANUAL]` | Specify the operations manual | "[specify value]" |
| `[TROUBLESHOOTING_GUIDE]` | Specify the troubleshooting guide | "[specify value]" |
| `[API_DOCUMENTATION_DETAILS]` | Specify the api documentation details | "[specify value]" |
| `[DATABASE_SCHEMA]` | Specify the database schema | "[specify value]" |
| `[SECURITY_GUIDELINES]` | Specify the security guidelines | "[specify value]" |
| `[UNIT_TESTING]` | Specify the unit testing | "[specify value]" |
| `[INTEGRATION_TESTING]` | Specify the integration testing | "[specify value]" |
| `[END_TO_END_TESTING]` | Specify the end to end testing | "[specify value]" |
| `[PERFORMANCE_TESTING]` | Specify the performance testing | "[specify value]" |
| `[SECURITY_TESTING]` | Specify the security testing | "[specify value]" |
| `[LOAD_TESTING]` | Specify the load testing | "[specify value]" |
| `[STRESS_TESTING]` | Specify the stress testing | "[specify value]" |
| `[CHAOS_ENGINEERING]` | Specify the chaos engineering | "[specify value]" |
| `[AB_TESTING]` | Specify the ab testing | "[specify value]" |
| `[TEST_AUTOMATION]` | Specify the test automation | "[specify value]" |
| `[MIGRATION_APPROACH]` | Specify the migration approach | "[specify value]" |
| `[LEGACY_SYSTEM]` | Specify the legacy system | "[specify value]" |
| `[MIGRATION_TIMELINE]` | Specify the migration timeline | "6 months" |
| `[DATA_MIGRATION]` | Specify the data migration | "[specify value]" |
| `[CUTOVER_STRATEGY]` | Specify the cutover strategy | "[specify value]" |
| `[ROLLBACK_PLAN]` | Specify the rollback plan | "[specify value]" |
| `[PARALLEL_RUNNING]` | Specify the parallel running | "[specify value]" |
| `[USER_TRAINING]` | Specify the user training | "[specify value]" |
| `[CHANGE_MANAGEMENT]` | Specify the change management | "[specify value]" |
| `[SUCCESS_CRITERIA]` | Specify the success criteria | "[specify value]" |

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