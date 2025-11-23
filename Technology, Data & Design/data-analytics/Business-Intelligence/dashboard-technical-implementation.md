---
title: Dashboard Technical Implementation & Platform
category: data-analytics
tags:
- data-analytics
- infrastructure
use_cases:
- Select and configure BI platform for organization's dashboard needs
- Design technical architecture for scalable dashboard infrastructure
- Implement performance optimization for slow-loading dashboards
related_templates:
- data-analytics/Business-Intelligence/dashboard-data-architecture.md
- data-analytics/Business-Intelligence/dashboard-security-compliance.md
- data-analytics/Business-Intelligence/dashboard-design-overview.md
last_updated: 2025-11-22
industries:
- technology
type: template
difficulty: intermediate
slug: dashboard-technical-implementation
---

# Dashboard Technical Implementation & Platform

## Overview
Design robust technical architecture and select appropriate platforms for dashboard implementation. This prompt guides technology stack selection, infrastructure design, and performance optimization.

---

## Purpose
Use this prompt to:
- Select appropriate BI platforms and technologies
- Design scalable infrastructure architecture
- Optimize for performance and reliability
- Plan for multi-device and mobile access

---

## Quick Start

**Platform Selection in 1 Hour:**
1. **Assess user base and budget** - Count users (100+ users → Power BI/Tableau, <50 users → consider Metabase), check budget ($50-150/user/month typical)
2. **Test with POC** - Download trial versions, load actual data, build 2-3 key dashboards in each platform
3. **Evaluate performance** - Test with realistic data volumes (1M+ rows → extract/cache required, <100K → live connection works)
4. **Design caching strategy** - Pre-aggregate daily/monthly summaries, cache query results 15-30 min, use CDN for static assets
5. **Set up monitoring** - Track dashboard load times (<3 sec target), query performance, concurrent users

**Key Decision:** For 1M+ rows, use extracts/aggregations. For real-time needs (<5 min latency), implement incremental refresh or streaming.

---

## Prompt

I need to design the technical architecture and select platforms for a dashboard solution with the following requirements:

### Platform Selection
**Dashboard Platform:**
- Platform preference: [PLATFORM_PREFERENCE] (Tableau/Power BI/Looker/Qlik/Custom development/Undecided)
- Key decision factors: [DECISION_FACTORS] (Cost/Ease of use/Scalability/Features/Existing tools)
- User licensing model: [LICENSING_MODEL] (Named users/Concurrent/Consumption-based)
- Expected user count: [USER_COUNT]
- Budget constraints: [BUDGET_CONSTRAINTS]

**Technology Stack:**
- Data warehouse: [DATA_WAREHOUSE] (Snowflake/Redshift/BigQuery/Synapse/Other)
- Backend requirements: [BACKEND_NEEDS] (APIs/Microservices/None)
- Frontend requirements: [FRONTEND_NEEDS] (Embedded analytics/White-label/Standard)
- Development framework: [DEV_FRAMEWORK] (React/Angular/Vue/None if using BI tool)
- Cloud provider: [CLOUD_PROVIDER] (AWS/Azure/GCP/Multi-cloud/On-premises)

### Infrastructure Requirements
**Compute & Storage:**
- Expected concurrent users: [CONCURRENT_USERS]
- Peak usage periods: [PEAK_USAGE]
- Query complexity: [QUERY_COMPLEXITY] (Simple aggregations/Complex joins/Advanced analytics)
- Data volume: [DATA_VOLUME]
- Performance target: [PERFORMANCE_TARGET] (Dashboard load time)

**Scalability:**
- Growth projection: [GROWTH_PROJECTION] (Users and data volume)
- Auto-scaling needs: [AUTO_SCALING] (Yes/No/Partial)
- Geographic distribution: [GEOGRAPHIC_DISTRIBUTION] (Single region/Multi-region/Global)
- High availability requirements: [HA_REQUIREMENTS] (SLA target)

### Multi-Device Support
**Desktop Experience:**
- Primary browsers: [SUPPORTED_BROWSERS] (Chrome/Firefox/Safari/Edge)
- Minimum screen resolution: [MIN_RESOLUTION]
- Desktop-specific features: [DESKTOP_FEATURES]

**Mobile Requirements:**
- Mobile platform priority: [MOBILE_PRIORITY] (iOS/Android/Both/Low priority)
- Mobile use cases: [MOBILE_USE_CASES]
- Offline capability: [OFFLINE_SUPPORT] (Required/Nice to have/Not needed)
- Native app vs. responsive web: [MOBILE_APPROACH]
- Tablet optimization: [TABLET_OPTIMIZATION]

**Cross-Platform Features:**
- Synchronization needs: [SYNC_REQUIREMENTS]
- Device-specific adaptations: [DEVICE_ADAPTATIONS]
- Performance targets by device: [DEVICE_PERFORMANCE]

### Performance Optimization
**Caching Strategy:**
- Caching requirements: [CACHING_NEEDS] (Query results/Aggregations/Full dashboards)
- Cache invalidation: [CACHE_INVALIDATION]
- CDN usage: [CDN_REQUIREMENTS]

**Query Optimization:**
- Pre-aggregation strategy: [AGGREGATION_STRATEGY]
- Materialized views: [MATERIALIZED_VIEWS]
- Query optimization approach: [QUERY_OPTIMIZATION]
- Partitioning strategy: [PARTITIONING]

### Integration & APIs
**Integration Points:**
- SSO integration: [SSO_INTEGRATION] (SAML/OAuth/LDAP/None)
- Embedding requirements: [EMBEDDING_NEEDS]
- API requirements: [API_NEEDS] (Read-only/Read-write/None)
- Webhook support: [WEBHOOK_NEEDS]
- Third-party integrations: [THIRD_PARTY_INTEGRATIONS]

**Development & Deployment:**
- Development environment: [DEV_ENVIRONMENT]
- CI/CD requirements: [CICD_REQUIREMENTS]
- Version control: [VERSION_CONTROL] (Git/Other)
- Testing environments: [TEST_ENVIRONMENTS] (Dev/Test/UAT/Prod)
- Deployment approach: [DEPLOYMENT_APPROACH] (Blue-green/Canary/Rolling)

---

## Deliverables

Please provide:

1. **Platform Recommendation**
   - Recommended BI platform with justification
   - Technology stack recommendations
   - Licensing and cost analysis
   - Platform comparison matrix
   - Implementation risks and mitigation

2. **Technical Architecture Design**
   - High-level architecture diagram
   - Component architecture
   - Network topology
   - Integration architecture
   - Security architecture overview

3. **Infrastructure Specifications**
   - Compute requirements (CPU, memory, storage)
   - Scaling strategy and configuration
   - Load balancing approach
   - Disaster recovery design
   - Monitoring and alerting setup

4. **Performance Optimization Plan**
   - Caching architecture
   - Query optimization strategies
   - Pre-aggregation design
   - CDN configuration (if applicable)
   - Performance monitoring approach

5. **Mobile & Multi-Device Strategy**
   - Responsive design specifications
   - Mobile app architecture (if applicable)
   - Offline capability design
   - Cross-device synchronization
   - Device-specific optimizations

6. **Implementation Roadmap**
   - Environment setup plan
   - Development workflow
   - Testing strategy
   - Deployment plan
   - Post-deployment monitoring

---

## Example Usage

### Example: Cloud-Native Analytics Platform

```
Platform preference: Undecided - need recommendation
Key decision factors: Ease of use for business users, cost-effectiveness, cloud-native
User licensing model: Named users preferred
Expected user count: 100 users (20 heavy users, 80 light users)
Budget constraints: $50K annually for platform licenses

Data warehouse: Snowflake
Backend requirements: REST APIs for embedded analytics
Frontend requirements: Embedded in internal portal
Development framework: React for custom components
Cloud provider: AWS

Expected concurrent users: 25-30 during business hours
Peak usage periods: Monday mornings, month-end
Query complexity: Mix of simple aggregations and complex multi-table joins
Data volume: 1 TB, growing 20% annually
Performance target: <3 seconds for dashboard load, <5 seconds for complex queries

Growth projection: 150 users in year 2, 250 users in year 3
Auto-scaling needs: Yes - handle peak loads automatically
Geographic distribution: US-based, single region (us-east-1)
High availability requirements: 99.5% uptime SLA

Primary browsers: Chrome (primary), Safari, Edge
Minimum screen resolution: 1366x768
Desktop-specific features: Multi-monitor support for power users

Mobile platform priority: Both iOS and Android
Mobile use cases: Executive dashboard viewing, KPI monitoring
Offline capability: Nice to have for core metrics
Mobile approach: Progressive Web App (PWA)
Tablet optimization: Yes - common use case for presentations

Synchronization needs: Saved filters and bookmarks across devices
Device-specific adaptations: Simplified charts on mobile, full detail on desktop
Device performance targets: <5 seconds on mobile, <3 seconds on desktop

Caching requirements: Cache query results for 15 minutes, pre-cache common dashboards
Cache invalidation: Time-based + manual refresh option
CDN usage: CloudFront for static assets

Aggregation strategy: Pre-aggregate daily/monthly summaries
Materialized views: For complex calculations and multi-table joins
Query optimization: Column pruning, partition elimination
Partitioning: By month on transaction date

SSO integration: SAML 2.0 with Okta
Embedding requirements: Embed dashboards in internal React app
API requirements: Read-only API for custom integrations
Webhook support: Not required
Third-party integrations: Slack for alerts

Development environment: Local development with Docker
CI/CD requirements: GitHub Actions for automated testing and deployment
Version control: Git (GitHub)
Test environments: Dev, Test, Prod
Deployment approach: Blue-green deployment to minimize downtime
```

---

## Usage Examples

### Example 1: Healthcare Provider Analytics Platform

**Context:** Regional hospital system needs BI platform for clinical and operational analytics

**Copy-paste this prompt:**

```
I need to design the technical architecture and select platforms for a dashboard solution with the following requirements:

### Platform Selection
**Dashboard Platform:**
- Platform preference: Undecided - need HIPAA-compliant recommendation
- Key decision factors: HIPAA compliance, ease of use for clinical staff, mobile access
- User licensing model: Named users for analytics, embedded for patient portals
- Expected user count: 500 (200 physicians, 150 nurses, 100 admin, 50 executives)
- Budget constraints: $200K annually for platform and infrastructure

**Technology Stack:**
- Data warehouse: Azure Synapse Analytics (existing Microsoft ecosystem)
- Backend requirements: APIs for Epic EHR integration, patient portal embedding
- Frontend requirements: Standard dashboards + embedded analytics in patient portal
- Development framework: React for custom patient-facing components
- Cloud provider: Azure (existing BAA in place)

### Infrastructure Requirements
**Compute & Storage:**
- Expected concurrent users: 100-150 during shift changes
- Peak usage periods: 7 AM shift change, month-end reporting
- Query complexity: Mix of real-time operational queries and complex analytics
- Data volume: 500 GB clinical data, growing 50 GB/month
- Performance target: <5 seconds for clinical dashboards, <10 seconds for analytics

**Scalability:**
- Growth projection: Adding 2 new hospitals in 2 years (3x users, 4x data)
- Auto-scaling needs: Yes - handle shift change peaks automatically
- Geographic distribution: Single region (US-East) with DR in US-West
- High availability requirements: 99.9% uptime (clinical operations)

### Multi-Device Support
**Desktop Experience:**
- Primary browsers: Chrome on clinical workstations, Edge on admin
- Minimum screen resolution: 1920x1080 (large monitors at nursing stations)
- Desktop-specific features: Multi-dashboard views for command centers

**Mobile Requirements:**
- Mobile platform priority: iOS primary (physicians), Android secondary
- Mobile use cases: Census updates, critical alerts, on-call dashboard access
- Offline capability: Required for basic patient census (network outages)
- Native app vs. responsive web: Native app for push notifications
- Tablet optimization: Yes - tablets used during rounds

### Performance Optimization
**Caching Strategy:**
- Caching requirements: Cache patient census (5-min refresh), cache analytics (hourly)
- Cache invalidation: Event-driven for critical alerts, time-based for analytics
- CDN usage: Azure CDN for static assets, not for PHI

**Query Optimization:**
- Pre-aggregation strategy: Daily patient statistics, rolling 30-day metrics
- Materialized views: For quality metrics, length of stay calculations
- Query optimization: Partition by facility_id and date
- Partitioning: Monthly partitions on service_date

### Integration & APIs
**Integration Points:**
- SSO integration: SAML with Azure AD, Epic SSO for clinical context
- Embedding requirements: Embed in Epic (Hyperspace), patient portal
- API requirements: Read-only REST APIs for third-party applications
- Webhook support: Required for critical alert notifications
- Third-party integrations: Epic FHIR APIs, Microsoft Teams for alerts

Please provide:
1. HIPAA-compliant BI platform recommendation with BAA availability
2. Technical architecture with Epic EHR integration
3. Mobile strategy for clinical staff (iOS app architecture)
4. HA/DR design for 99.9% availability requirement
5. Performance optimization for shift-change peaks
```

**Expected Output:**
- Platform: Power BI Premium (Microsoft BAA available) or Tableau Server (HIPAA-compliant)
- Epic integration: FHIR R4 APIs for patient context, SMART on FHIR for launch
- Mobile: Native iOS app with Power BI Embedded SDK, push notifications for critical alerts
- HA: Multi-AZ deployment, Azure paired regions for DR, geo-redundant backups

---

### Example 2: Embedded Analytics for SaaS Product

**Context:** B2B SaaS company embedding analytics into their product for customers

**Copy-paste this prompt:**

```
I need to design the technical architecture and select platforms for a dashboard solution with the following requirements:

### Platform Selection
**Dashboard Platform:**
- Platform preference: Embedded-first platform (considering Looker, Sisense, Sigma, custom)
- Key decision factors: White-label capability, multi-tenant, API-first, developer experience
- User licensing model: Consumption-based or flat fee per customer
- Expected user count: 500 customers, 5-50 users each = 5,000-25,000 total users
- Budget constraints: $150K/year platform + margin for customer pricing ($100-500/customer/month)

**Technology Stack:**
- Data warehouse: Snowflake (existing)
- Backend requirements: REST APIs for customer data access, GraphQL for custom queries
- Frontend requirements: Full white-label, JavaScript SDK, React components
- Development framework: React (existing product frontend)
- Cloud provider: AWS (existing infrastructure)

### Infrastructure Requirements
**Compute & Storage:**
- Expected concurrent users: 500-1000 across all tenants
- Peak usage periods: Business hours across time zones (always-on)
- Query complexity: Simple aggregations per tenant, complex cross-tenant for admins
- Data volume: 100 GB per large customer, 2 TB total
- Performance target: <2 seconds (must match product performance)

**Scalability:**
- Growth projection: 2x customers in 12 months, 5x in 24 months
- Auto-scaling needs: Critical - must scale with customer growth
- Geographic distribution: US (primary), EU (expanding)
- High availability requirements: 99.9% (SLA to customers)

### Multi-Tenant Architecture
**Tenant Isolation:**
- Data isolation: Row-level security with tenant_id in every query
- Compute isolation: Shared compute with tenant-aware query limits
- Customization: Per-tenant themes, custom metrics, custom dashboards

### Multi-Device Support
**Desktop Experience:**
- Primary browsers: Chrome, Safari, Firefox, Edge (all current versions)
- Desktop-specific features: Full analytics, dashboard builder for power users

**Mobile Requirements:**
- Mobile platform priority: Responsive web (not native app)
- Mobile use cases: Quick metric checks, alerts
- Offline capability: Not required
- Mobile approach: Progressive Web App with responsive design

### Performance Optimization
**Caching Strategy:**
- Caching requirements: Per-tenant query result caching (15-min TTL)
- Cache invalidation: Tenant-aware cache keys, invalidate on data refresh
- CDN usage: CloudFront for static assets, cache API responses at edge

**Query Optimization:**
- Pre-aggregation strategy: Tenant-level daily/monthly aggregations
- Materialized views: Per-tenant summary tables
- Query optimization: Snowflake warehouse scaling, result caching
- Partitioning: By tenant_id and date

### Integration & APIs
**Integration Points:**
- SSO integration: Customer's SSO via SAML/OIDC, JWT from our product auth
- Embedding requirements: iFrame with signed tokens, JavaScript SDK preferred
- API requirements: Full REST API for customers to pull their data
- Webhook support: Required for customers' integrations
- Third-party integrations: Slack, Zapier for customer workflows

Please provide:
1. Embedded BI platform comparison for multi-tenant SaaS
2. Multi-tenant data architecture with Snowflake
3. White-label embedding architecture (SDK vs. iFrame)
4. Per-tenant caching and query optimization
5. Pricing model for analytics feature (cost structure)
```

**Expected Output:**
- Platform comparison: Looker (LookML flexibility), Sisense (embedded-first), Sigma (cloud-native), Custom (full control)
- Multi-tenant: Snowflake Row Access Policies, tenant_id in all tables, secure views
- Embedding: JavaScript SDK with signed JWT tokens, tenant context in embed URL
- Caching: Redis with tenant-prefixed keys, Snowflake result caching per query

---

### Example 3: Enterprise Self-Service BI Migration

**Context:** Enterprise migrating from on-premise SSRS to cloud-based self-service BI

**Copy-paste this prompt:**

```
I need to design the technical architecture and select platforms for a dashboard solution with the following requirements:

### Platform Selection
**Dashboard Platform:**
- Platform preference: Evaluating Power BI vs. Tableau for enterprise self-service
- Key decision factors: Self-service for business users, governance for IT, Microsoft ecosystem
- User licensing model: Named users (viewers + creators)
- Expected user count: 2,000 total (200 creators, 1,800 viewers)
- Budget constraints: $500K annually (platform + infrastructure)

**Technology Stack:**
- Data warehouse: Migrating from SQL Server to Snowflake (in progress)
- Backend requirements: Enterprise service bus integration, existing APIs
- Frontend requirements: SharePoint integration, Teams embedding
- Development framework: N/A - using BI platform native development
- Cloud provider: Azure (primary), some AWS for data sources

### Infrastructure Requirements
**Compute & Storage:**
- Expected concurrent users: 300-500 during business hours
- Peak usage periods: 9 AM globally, month-end close
- Query complexity: Range from simple to complex ad-hoc analysis
- Data volume: 5 TB in Snowflake, growing 500 GB/month
- Performance target: <10 seconds for complex ad-hoc, <3 seconds for standard reports

**Scalability:**
- Growth projection: 3,000 users in 2 years (50% growth)
- Auto-scaling needs: Yes - Snowflake auto-suspend, BI platform capacity units
- Geographic distribution: Global (US, EU, APAC offices)
- High availability requirements: 99.5% for analytics, 99.9% for critical reports

### Multi-Device Support
**Desktop Experience:**
- Primary browsers: Edge and Chrome (enterprise-managed)
- Minimum screen resolution: 1366x768 (older laptops in field)
- Desktop-specific features: Excel integration, PowerPoint export

**Mobile Requirements:**
- Mobile platform priority: Both iOS and Android (managed devices)
- Mobile use cases: KPI monitoring, approval workflows
- Offline capability: Required for field sales (spotty connectivity)
- Native app vs. responsive web: Native app for push and offline
- Tablet optimization: Yes - executives use iPads

### Performance Optimization
**Caching Strategy:**
- Caching requirements: Dataset refresh caching, incremental refresh
- Cache invalidation: Scheduled refresh (most datasets 4x daily, some hourly)
- CDN usage: Microsoft CDN for Power BI, CloudFront for custom portal

**Query Optimization:**
- Pre-aggregation strategy: Power BI aggregations for common queries
- Materialized views: Snowflake materialized views for complex calcs
- Query optimization: Power BI composite models, DirectQuery for real-time
- Partitioning: Incremental refresh partitions by month

### Integration & APIs
**Integration Points:**
- SSO integration: Azure AD (existing), federated for acquired companies
- Embedding requirements: SharePoint, Teams, custom portals
- API requirements: Power BI REST APIs for automation and embedding
- Webhook support: Power Automate for alerting and workflow
- Third-party integrations: ServiceNow (IT), Workday (HR), SAP (finance)

### Governance & Management
**Enterprise Features:**
- Deployment pipeline: Dev → Test → Prod with CI/CD
- Version control: Azure DevOps for Power BI dataset definitions
- Certification: Certified datasets for trusted data sources
- Lineage: Data lineage tracking for audit and compliance

Please provide:
1. Power BI vs. Tableau enterprise comparison for this use case
2. Enterprise deployment architecture (Premium capacity sizing)
3. Governance framework for self-service with guardrails
4. Hybrid DirectQuery + Import strategy for performance
5. Global deployment with regional performance optimization
```

**Expected Output:**
- Recommendation: Power BI Premium for Microsoft ecosystem alignment
- Capacity sizing: 2x P2 capacities (one US, one EU) with EM sizing for APAC
- Governance: Certified datasets, deployment pipelines, usage monitoring
- Hybrid model: Import for historical, DirectQuery for real-time, composite for both

---

## Best Practices

**Top 5 Critical Practices:**
1. **Optimize the slowest query first** - One 30-second query ruins an otherwise fast dashboard
2. **Use extracts for large datasets, live connections for small** - 1M+ rows? Extract. <100K? Live connection works fine
3. **Test with real users on real devices** - Your high-speed connection ≠ executive's airport WiFi
4. **Build in phases, not all at once** - Ship 5 metrics this week > perfect 20 metrics next quarter
5. **Monitor what users actually click** - If nobody uses that fancy drill-down, remove it and speed up the dashboard

### Platform Selection
1. **Align with user skills** - Choose tools that match your team's capabilities
2. **Consider total cost** - Include licenses, infrastructure, and maintenance
3. **Evaluate cloud-native options** - Often more scalable and cost-effective
4. **Test with real use cases** - Run POC with actual data and users
5. **Check integration capabilities** - Ensure it works with your data sources

### Technical Architecture
6. **Design for scalability** - Plan for 3x current requirements
7. **Implement caching strategically** - Balance freshness with performance
8. **Use CDN for static assets** - Reduce latency for global users
9. **Separate compute and storage** - Enable independent scaling
10. **Plan for multi-region** - Even if starting with one region

### Performance Optimization
11. **Pre-aggregate common queries** - Create summary tables
12. **Use incremental refresh** - Update only changed data
13. **Implement query result caching** - Reduce database load
14. **Optimize data model** - Denormalize for read performance
15. **Monitor and tune regularly** - Continuously optimize slow queries

### Mobile & Multi-Device
16. **Mobile-first for executives** - They often use mobile primarily
17. **Progressive Web App** - Often better than native apps for dashboards
18. **Adaptive, not just responsive** - Tailor experience to device
19. **Optimize for bandwidth** - Minimize data transfer on mobile
20. **Test on real devices** - Emulators don't catch everything

---

## Platform Comparison Matrix

### Commercial BI Platforms

| Platform | Best For | Strengths | Limitations | Cost Range |
|----------|----------|-----------|-------------|------------|
| **Tableau** | Complex visualizations, power users | Best-in-class viz, strong community | Steeper learning curve, higher cost | $$$ |
| **Power BI** | Microsoft ecosystem | Office integration, cost-effective | Limited customization | $-$$ |
| **Looker** | Developer-centric teams | LookML, Git integration, embedded | Requires SQL knowledge | $$-$$$ |
| **Qlik** | Associative analysis | Powerful data discovery | Complex licensing | $$$ |
| **Thoughtspot** | Search-driven analytics | Natural language queries | Newer platform | $$-$$$ |

### Custom Development

| Approach | Best For | Strengths | Limitations | Cost Range |
|----------|----------|-----------|-------------|------------|
| **React + D3.js** | Full customization | Complete control, brand alignment | High dev effort | $$-$$$ |
| **Superset** | Open source, customizable | Free, flexible | Requires hosting & support | $-$$ |
| **Metabase** | Simple self-service | Easy to use, open source | Limited advanced features | $-$$ |

**Cost Range**: $ = <$50/user/month, $$ = $50-150/user/month, $$$ = >$150/user/month

---

## Infrastructure Sizing Guide

### Small Implementation (25-50 users)

```
Platform: Power BI Pro or Tableau Creator
Data Warehouse: Snowflake X-Small (auto-suspend enabled)
Caching: Redis (small instance)
Load Balancer: Not required
Estimated Monthly Cost: $3,000-$5,000
```

### Medium Implementation (50-250 users)

```
Platform: Tableau Server or Power BI Premium
Data Warehouse: Snowflake Small-Medium with auto-scaling
Caching: Redis (medium instance, multi-AZ)
Load Balancer: Application Load Balancer
CDN: CloudFront
Estimated Monthly Cost: $15,000-$30,000
```

### Large Implementation (250+ users)

```
Platform: Tableau Server (HA) or Power BI Premium (Multi-Geo)
Data Warehouse: Snowflake Large+ with auto-scaling
Caching: Redis cluster (multi-AZ)
Load Balancer: Application Load Balancer (multi-region)
CDN: CloudFront (global)
Estimated Monthly Cost: $50,000-$150,000+
```

---

## Common Pitfalls to Avoid

- Underestimating infrastructure costs for cloud platforms
- Choosing platform based on features rather than user needs
- Not planning for mobile access from the start
- Over-engineering for current needs (vs. scalable architecture)
- Ignoring data transfer costs between cloud services
- Poor caching strategy leading to slow performance
- Not testing performance at scale before launch
- Insufficient monitoring and alerting
- Lack of disaster recovery plan
- Not considering user training and adoption

---

## Decision Framework

### When to Choose Commercial BI Tools

✅ Use when:
- Users need self-service analytics
- Budget allows for licensing costs
- Standard visualizations meet needs
- Quick time to market is critical
- Limited development resources

❌ Avoid when:
- Highly custom visualizations required
- Extreme cost sensitivity
- Need complete white-labeling
- Embedding is primary use case
- Very large user base (>1000 users)

### When to Build Custom

✅ Use when:
- Unique UX requirements
- Embedding in customer-facing app
- Very specific industry workflows
- Cost-effectiveness at scale
- Full control over technology stack

❌ Avoid when:
- Limited development resources
- Need rapid deployment
- Users expect self-service
- Standard BI features sufficient
- Ongoing maintenance is concern

---

## Variables Quick Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `[PLATFORM_PREFERENCE]` | BI platform choice | "Power BI" |
| `[USER_COUNT]` | Number of users | "150 users" |
| `[DATA_WAREHOUSE]` | DW platform | "Snowflake" |
| `[CLOUD_PROVIDER]` | Cloud platform | "AWS" |
| `[CONCURRENT_USERS]` | Peak concurrent users | "30 users" |
| `[PERFORMANCE_TARGET]` | Load time goal | "<3 seconds" |
| `[MOBILE_PRIORITY]` | Mobile importance | "Both iOS and Android" |
| `[MOBILE_APPROACH]` | Mobile strategy | "Progressive Web App" |
| `[CACHING_NEEDS]` | Caching strategy | "Query results for 15 min" |
| `[SSO_INTEGRATION]` | SSO method | "SAML 2.0 with Okta" |
