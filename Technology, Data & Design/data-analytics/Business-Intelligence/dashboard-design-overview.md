---
category: data-analytics
title: Dashboard Design Overview & Navigation
tags:
- business-intelligence
- dashboards
- project-planning
- bi-strategy
use_cases:
- Planning end-to-end dashboard development projects
- Selecting appropriate specialized templates for dashboard phases
- Assessing dashboard project readiness and resource requirements
- Creating phased implementation roadmaps
related_templates:
- data-analytics/Business-Intelligence/dashboard-strategy-requirements.md
- data-analytics/Business-Intelligence/dashboard-ux-design.md
- data-analytics/Business-Intelligence/dashboard-data-architecture.md
- data-analytics/Business-Intelligence/dashboard-technical-implementation.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: dashboard-design-overview
---

# Dashboard Design Overview & Navigation

## Purpose
Guide dashboard project planning by assessing readiness, selecting appropriate specialized templates, and creating phased implementation roadmaps. This framework helps navigate the comprehensive dashboard design template suite and ensures projects address all critical dimensions from strategy through deployment.

## 🚀 Quick Planning Prompt

> Plan a **dashboard initiative** for **[ORGANIZATION]** building **[DASHBOARD SCOPE]**. Assess readiness across: (1) **Requirements clarity**—are business objectives, KPIs, and stakeholder needs defined? (2) **Data readiness**—are source systems identified, data quality understood, and pipelines feasible? (3) **Technical foundation**—is BI platform selected, infrastructure available, and team skilled? (4) **Governance needs**—are security requirements, compliance obligations, and access controls understood? Provide a phase recommendation, template sequence, resource estimate, and implementation timeline.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid dashboard project planning.

---

## Template

Plan a comprehensive dashboard initiative for {ORGANIZATION_CONTEXT}, developing {DASHBOARD_SCOPE} to achieve {BUSINESS_OBJECTIVES}.

Assess project readiness across six dimensions, scoring each 1-5:

**1. REQUIREMENTS READINESS**

Evaluate clarity of business requirements starting with objective definition determining whether dashboard goals are articulated with measurable success criteria. Assess KPI identification confirming metrics are defined with calculation logic, targets, and data sources. Review stakeholder alignment checking whether decision-makers agree on priorities, scope, and expected outcomes. Examine user understanding evaluating whether personas, workflows, and usage patterns are documented. Consider scope boundaries determining whether inclusions and exclusions are clear and agreed upon. Identify requirement gaps noting areas needing further discovery before design can proceed. If requirements readiness is low, start with the Strategy and Requirements template before other phases.

**2. DATA READINESS**

Assess data foundation for dashboard analytics beginning with source identification confirming all required data systems are known with access paths understood. Evaluate data quality understanding determining whether completeness, accuracy, and timeliness are characterized for each source. Review data integration feasibility assessing whether extraction methods are viable and latency requirements achievable. Check data modeling status determining whether analytical models exist or need creation. Examine historical data availability confirming sufficient history exists for trend analysis and comparisons. Identify data gaps noting missing sources, quality issues, or integration challenges requiring resolution. If data readiness is low, prioritize the Data Architecture template early in the project sequence.

**3. TECHNICAL READINESS**

Evaluate technical foundation starting with platform status determining whether BI tool is selected, licensed, and configured. Assess infrastructure availability checking whether compute, storage, and network resources are provisioned. Review team capabilities confirming skills exist for data engineering, BI development, and platform administration. Examine integration capabilities assessing whether APIs, connectors, and authentication mechanisms are available. Consider performance requirements understanding query volumes, user concurrency, and response time expectations. Identify technical gaps noting platform decisions, infrastructure needs, or skill gaps requiring attention. If technical readiness is low, engage the Technical Implementation template before build phases.

**4. DESIGN READINESS**

Assess user experience foundation beginning with user research status determining whether personas, journeys, and pain points are understood. Evaluate visualization requirements checking whether chart types, layouts, and interaction patterns are identified. Review design system availability confirming whether brand guidelines, component libraries, and style standards exist. Examine accessibility requirements understanding compliance needs for WCAG or organizational standards. Consider device requirements determining desktop, mobile, and embedded access needs. Identify design gaps noting user research, mockup, or prototype work needed. If design readiness is low, schedule the UX Design template before development begins.

**5. SECURITY AND COMPLIANCE READINESS**

Evaluate governance requirements starting with security requirements clarity determining whether authentication, authorization, and encryption needs are documented. Assess compliance obligations confirming regulatory requirements like HIPAA, SOX, or GDPR are identified with control mappings. Review access control design checking whether row-level security, role definitions, and permission models are specified. Examine audit requirements understanding logging, retention, and reporting obligations. Consider data sensitivity classification determining whether data categories and handling requirements are defined. Identify governance gaps noting security decisions, compliance assessments, or control implementations needed. If governance readiness is low, engage the Security and Compliance template early, especially for regulated industries.

**6. OPERATIONAL READINESS**

Assess deployment and support foundation beginning with testing strategy determining whether test plans, environments, and acceptance criteria are defined. Evaluate deployment approach checking whether release process, rollback procedures, and communication plans exist. Review support model confirming whether maintenance responsibilities, escalation paths, and SLAs are established. Examine training requirements understanding user enablement needs and documentation requirements. Consider monitoring capabilities determining whether alerting, usage tracking, and health checks are planned. Identify operational gaps noting testing, deployment, or support preparations needed. Schedule the Testing and Deployment template as build phase completes.

Deliver your project plan as:

1. **READINESS SCORECARD** - Score per dimension with key finding and recommended action

2. **TEMPLATE SEQUENCE** - Ordered list of specialized templates to use based on readiness gaps

3. **PHASE PLAN** - Project phases with parallel and sequential workstreams mapped to templates

4. **RESOURCE ESTIMATE** - Team roles, skills, and time investment per phase

5. **TIMELINE** - Week-by-week or month-by-month schedule with milestones and dependencies

6. **RISK ASSESSMENT** - Top risks from readiness gaps with mitigation strategies

Use this readiness scale:
- 1.0-1.9: Not Started (no work done, significant discovery needed)
- 2.0-2.9: Early (initial work started, major gaps remain)
- 3.0-3.9: Progressing (solid progress, some gaps to address)
- 4.0-4.9: Ready (well-prepared, minor refinements needed)
- 5.0: Complete (fully ready, proceed to next phase)

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{ORGANIZATION_CONTEXT}` | Organization type, size, and current BI maturity | "Series B SaaS startup with no existing BI tool and data in 5 SaaS systems" |
| `{DASHBOARD_SCOPE}` | Dashboard types and coverage | "executive KPI dashboard plus departmental views for sales, marketing, and finance" |
| `{BUSINESS_OBJECTIVES}` | Goals and success criteria | "unified metrics visibility with daily refresh enabling data-driven weekly leadership meetings" |

---

## Usage Examples

### Example 1: Startup First Dashboard
**Prompt:** Plan a comprehensive dashboard initiative for TechStartup Inc, a Series B SaaS company with 80 employees and no existing BI infrastructure, developing executive KPI dashboard tracking MRR, churn, CAC, and LTV with departmental drill-downs to achieve unified metrics visibility replacing manual Excel reporting within 8 weeks.

**Expected Output:** Readiness scorecard showing low data readiness (data in 5 disconnected SaaS tools) and low technical readiness (no BI platform), template sequence starting with Strategy then Data Architecture then Technical Implementation in parallel with UX Design, 8-week timeline with weeks 1-2 for requirements and platform selection, weeks 3-5 for data pipeline and dashboard build, weeks 6-7 for testing, week 8 for deployment and training.

### Example 2: Enterprise Report Modernization
**Prompt:** Plan a comprehensive dashboard initiative for Fortune 500 manufacturer with 50+ legacy Crystal Reports serving 500 users, developing modern interactive dashboard suite consolidating operational and analytical reporting to achieve retirement of legacy reporting infrastructure over 18 months while maintaining SOX compliance for financial reports.

**Expected Output:** Readiness scorecard showing high requirements complexity (50+ reports to inventory), medium data readiness (existing data warehouse), high governance needs (SOX), template sequence starting with Security and Compliance then Strategy for report inventory then Data Architecture for semantic layer, phased 18-month plan prioritizing high-use reports first, parallel run strategy for validation, and change management emphasis for user adoption.

### Example 3: Embedded Analytics Product
**Prompt:** Plan a comprehensive dashboard initiative for B2B SaaS product company with 200 customers, developing embedded analytics feature within the product offering customer-facing dashboards with self-service capabilities to achieve new revenue stream with analytics add-on priced at $100-200 per customer monthly.

**Expected Output:** Readiness scorecard highlighting critical security needs (multi-tenant data isolation), technical complexity (embedded BI platform selection), and UX requirements (white-label design), template sequence prioritizing Technical Implementation for platform evaluation then Security for multi-tenancy then UX Design for seamless embedding, 12-week timeline with heavy emphasis on architecture decisions in first 4 weeks.

---

## Cross-References

- [Dashboard Strategy Requirements](dashboard-strategy-requirements.md) - Business objectives, KPIs, and stakeholder alignment
- [Dashboard UX Design](dashboard-ux-design.md) - User experience, visualization, and interaction design
- [Dashboard Data Architecture](dashboard-data-architecture.md) - Data pipelines, modeling, and quality frameworks
- [Dashboard Technical Implementation](dashboard-technical-implementation.md) - Platform selection and infrastructure
- [Dashboard Security Compliance](dashboard-security-compliance.md) - Access controls and regulatory compliance
- [Dashboard Testing Deployment](dashboard-testing-deployment.md) - Testing strategy and release management
