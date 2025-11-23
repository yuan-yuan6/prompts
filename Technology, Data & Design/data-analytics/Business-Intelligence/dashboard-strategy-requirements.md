---
category: data-analytics
last_updated: 2025-11-22
related_templates:
- data-analytics/Business-Intelligence/dashboard-ux-design.md
- data-analytics/Business-Intelligence/dashboard-data-architecture.md
- data-analytics/Business-Intelligence/dashboard-design-overview.md
tags:
- data-analytics
- strategy
title: Dashboard Strategy & Business Requirements
use_cases:
- Defining dashboard business requirements
- Stakeholder alignment
- KPI framework development
industries:
- manufacturing
- technology
type: template
difficulty: intermediate
slug: dashboard-strategy-requirements
---

# Dashboard Strategy & Business Requirements

## Overview
Define comprehensive business requirements and strategic direction for dashboard initiatives. This prompt helps align stakeholder needs, establish KPIs, and create a solid foundation for dashboard development.

---

## Purpose
Use this prompt to:
- Establish clear business objectives for dashboard initiatives
- Identify and align stakeholder requirements
- Define critical KPIs and success metrics
- Create strategic dashboard portfolio architecture

---

## Quick Start

**30-Minute Requirements Workshop:**
1. **Identify stakeholders and objectives** - List key users (C-suite, managers, analysts), map to business goals (growth, efficiency, risk reduction)
2. **Prioritize 5-7 critical KPIs** - Focus on metrics that drive decisions, avoid vanity metrics (e.g., Revenue Growth, Customer Churn, NPS)
3. **Map data source availability** - Confirm each KPI's data exists and is accessible (CRM, ERP, databases)
4. **Define success criteria** - Set targets for adoption (% of users logging in weekly), accuracy (99%+), and business impact
5. **Create phased roadmap** - Phase 1: Executive dashboard, Phase 2: Departmental

**Key Decision:** Build incrementally. Ship 5 working KPIs this quarter beats planning 20 perfect ones for next year.

---

## Prompt

I need to develop a comprehensive business requirements framework for a dashboard solution with the following context:

### Organization Context
- Organization name: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR] (Financial/Healthcare/Manufacturing/Technology/Retail/Other)
- Company size: [COMPANY_SIZE] (Startup/SMB/Mid-market/Enterprise)
- Strategic objectives: [STRATEGIC_OBJECTIVES] (Growth/Efficiency/Innovation/Compliance)
- Dashboard scope: [DASHBOARD_SCOPE] (Executive/Departmental/Operational/Customer-facing)

### Stakeholder Requirements
- Primary users: [PRIMARY_USERS] (C-Suite/Directors/Managers/Analysts)
- User count: [USER_COUNT]
- Technical expertise level: [TECHNICAL_LEVEL] (Non-technical/Business users/Technical users)
- Decision-making needs: [DECISION_MAKING_NEEDS]
- Key stakeholders: [KEY_STAKEHOLDERS]

### Dashboard Portfolio
- Executive dashboards needed: [EXECUTIVE_DASHBOARD_COUNT]
- Departmental dashboards: [DEPARTMENTAL_DASHBOARDS]
- Real-time monitoring requirements: [REALTIME_REQUIREMENTS]
- Mobile dashboard needs: [MOBILE_REQUIREMENTS]

### System Integration Needs
- ERP system: [ERP_SYSTEM] (SAP/Oracle/NetSuite/Other/None)
- CRM system: [CRM_SYSTEM] (Salesforce/HubSpot/Microsoft Dynamics/Other/None)
- Other critical systems: [OTHER_SYSTEMS]
- External data sources: [EXTERNAL_DATA_SOURCES]

### Key Performance Indicators

**Financial Metrics:**
- Revenue indicators: [REVENUE_METRICS] (Total revenue/Growth rate/Recurring revenue/Forecast accuracy)
- Profitability measures: [PROFITABILITY_METRICS] (Gross margin/Operating margin/Net profit/EBITDA)
- Cash flow tracking: [CASHFLOW_METRICS]
- Budget variance: [BUDGET_METRICS]

**Operational Metrics:**
- Process efficiency: [PROCESS_METRICS] (Cycle time/Throughput/Utilization/Quality)
- Productivity measures: [PRODUCTIVITY_METRICS]
- Quality indicators: [QUALITY_METRICS] (Defect rates/First pass yield/Customer complaints)
- Resource utilization: [RESOURCE_METRICS]

**Customer Metrics:**
- Customer satisfaction: [CUSTOMER_SATISFACTION] (CSAT/NPS/CES)
- Customer lifecycle: [CUSTOMER_LIFECYCLE] (Acquisition cost/Retention rate/Churn rate/Lifetime value)
- Service quality: [SERVICE_METRICS] (Response time/Resolution time/First contact resolution)
- Market position: [MARKET_METRICS]

**Employee Metrics:**
- Employee engagement: [EMPLOYEE_ENGAGEMENT]
- Performance management: [PERFORMANCE_METRICS]
- Talent acquisition/retention: [TALENT_METRICS]
- Training effectiveness: [TRAINING_METRICS]

### Success Criteria
- Primary business outcomes: [BUSINESS_OUTCOMES]
- Adoption targets: [ADOPTION_TARGETS]
- ROI expectations: [ROI_EXPECTATIONS]
- Timeline: [TIMELINE]
- Budget: [BUDGET]

---

## Deliverables

Please provide:

1. **Strategic Dashboard Framework**
   - Business objectives alignment
   - Stakeholder analysis matrix
   - Dashboard portfolio architecture
   - Integration roadmap

2. **KPI Framework**
   - Prioritized KPI list with definitions
   - KPI ownership and accountability
   - Target values and thresholds
   - Measurement methodology

3. **Requirements Documentation**
   - Functional requirements
   - Non-functional requirements
   - User stories for key personas
   - Acceptance criteria

4. **Implementation Roadmap**
   - Phased delivery plan
   - Quick wins and long-term initiatives
   - Dependency mapping
   - Risk assessment

---

## Example Usage

### Example: Mid-Market SaaS Company

```
Organization name: CloudTech Solutions
Industry sector: Technology
Company size: Mid-market (500 employees)
Strategic objectives: Growth and Customer retention
Dashboard scope: Executive and Departmental

Primary users: C-Suite and Department heads
User count: 25 users
Technical expertise level: Business users
Decision-making needs: Strategic planning and operational oversight

Executive dashboards needed: 1 company-wide dashboard
Departmental dashboards: Sales, Marketing, Product, Customer Success
Real-time monitoring requirements: Sales pipeline and customer health scores
Mobile dashboard needs: Yes - key metrics for executives

ERP system: NetSuite
CRM system: Salesforce
Other critical systems: Zendesk, Stripe, Google Analytics
External data sources: Industry benchmarks

Revenue metrics: MRR, ARR, Growth rate, Churn
Profitability metrics: Gross margin, CAC payback period
Customer satisfaction: NPS, CSAT
Customer lifecycle: CAC, LTV, Retention rate, Churn rate
Service metrics: Ticket response time, Resolution time

Business outcomes: Reduce churn by 15%, Increase expansion revenue by 25%
Timeline: Phase 1 in 3 months
Budget: $150,000
```

---



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Dashboard Ux Design](dashboard-ux-design.md)** - Complementary approaches and methodologies
- **[Dashboard Data Architecture](dashboard-data-architecture.md)** - Leverage data analysis to drive informed decisions
- **[Dashboard Design Overview](dashboard-design-overview.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Dashboard Strategy & Business Requirements)
2. Use [Dashboard Ux Design](dashboard-ux-design.md) for deeper analysis
3. Apply [Dashboard Data Architecture](dashboard-data-architecture.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Business Intelligence](../../data-analytics/Business Intelligence/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Defining dashboard business requirements**: Combine this template with related analytics and strategy frameworks
- **Stakeholder alignment**: Combine this template with related analytics and strategy frameworks
- **KPI framework development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Start with business outcomes** - Define what success looks like before selecting KPIs
2. **Limit KPIs** - Focus on 5-7 critical metrics per dashboard to avoid information overload
3. **Align stakeholders early** - Get buy-in from all key stakeholders before development
4. **Define clear ownership** - Assign accountability for each KPI
5. **Plan for evolution** - Build in flexibility for changing business needs
6. **Prioritize ruthlessly** - Not everything can be in phase 1
7. **Validate with users** - Test assumptions with actual end users
8. **Document everything** - Clear requirements prevent scope creep
9. **Think mobile-first** - Executives often need mobile access
10. **Consider data availability** - Ensure required data exists and is accessible

---

## Common Pitfalls to Avoid

- Defining too many KPIs (focus on what matters most)
- Skipping stakeholder alignment (leads to rework)
- Ignoring data quality issues (garbage in, garbage out)
- Building everything at once (use phased approach)
- Overlooking user technical capabilities
- Failing to establish KPI ownership
- Not defining success criteria upfront
- Underestimating integration complexity

---

## Variables Quick Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `[ORGANIZATION_NAME]` | Company name | "TechCorp Industries" |
| `[INDUSTRY_SECTOR]` | Industry | "Healthcare" |
| `[COMPANY_SIZE]` | Organization size | "Enterprise" |
| `[STRATEGIC_OBJECTIVES]` | Business goals | "Growth, Operational Excellence" |
| `[DASHBOARD_SCOPE]` | Dashboard type | "Executive" |
| `[PRIMARY_USERS]` | Main user group | "C-Suite executives" |
| `[USER_COUNT]` | Number of users | "15 executives" |
| `[REVENUE_METRICS]` | Revenue KPIs | "ARR, Growth rate, Forecast accuracy" |
| `[CUSTOMER_SATISFACTION]` | Customer metrics | "NPS, CSAT, Customer effort score" |
| `[BUDGET]` | Project budget | "$200,000" |
| `[TIMELINE]` | Delivery timeline | "6 months" |

## Usage Examples

### Example 1: SaaS Executive Dashboard

**Context:** B2B SaaS company needs executive visibility into business performance

**Copy-paste this prompt:**

```
I need to develop a comprehensive business requirements framework for a dashboard solution with the following context:

### Organization Context
- Organization name: CloudMetrics SaaS
- Industry sector: Technology (B2B SaaS)
- Company size: Mid-market (250 employees, $50M ARR)
- Strategic objectives: Growth (expand ARR 40% YoY), Efficiency (reduce churn below 5%)
- Dashboard scope: Executive (C-suite and VP-level leadership)

### Stakeholder Requirements
- Primary users: CEO, CFO, CRO, VP Customer Success, VP Product
- User count: 12 executives
- Technical expertise level: Non-technical to business users
- Decision-making needs: Weekly business reviews, board reporting, strategic planning
- Key stakeholders: CEO (sponsor), CFO (budget owner), CRO (primary user)

### Dashboard Portfolio
- Executive dashboards needed: 1 unified executive dashboard with 5 focused views
- Departmental dashboards: Sales, Customer Success, Product, Finance (phase 2)
- Real-time monitoring requirements: ARR and pipeline updates daily, churn alerts real-time
- Mobile dashboard needs: Yes - CEO and CRO need mobile access for board meetings

### System Integration Needs
- ERP system: NetSuite (financials, billing)
- CRM system: Salesforce (pipeline, customers, ARR tracking)
- Other critical systems: Stripe (payments), Intercom (support tickets), Mixpanel (product usage)
- External data sources: Industry benchmarks (SaaS Capital, KeyBanc)

### Key Performance Indicators

**Financial Metrics:**
- Revenue indicators: ARR, MRR, Net New ARR, Expansion ARR, ARR Growth Rate
- Profitability measures: Gross margin, CAC payback period, LTV/CAC ratio
- Cash flow tracking: Runway months, burn rate, collections aging
- Budget variance: Actual vs forecast by department

**Operational Metrics:**
- Process efficiency: Sales cycle length, time to first value, support ticket resolution
- Productivity measures: Revenue per employee, deals per rep
- Quality indicators: Product uptime (99.9% SLA), bug resolution time
- Resource utilization: Engineering capacity allocation

**Customer Metrics:**
- Customer satisfaction: NPS (target: 50+), CSAT, Product satisfaction score
- Customer lifecycle: CAC, Gross retention, Net retention (target: 110%+), Logo churn
- Service quality: First response time (<4 hours), Resolution time, Escalation rate

Please provide:
1. KPI framework with definitions, owners, and targets
2. Dashboard portfolio architecture (what goes where)
3. Data source mapping for each KPI
4. Phased implementation roadmap (MVP in 6 weeks, full in 3 months)
5. Success criteria and adoption metrics
```

**Expected Output:**
- KPI hierarchy with 15-20 metrics across 4 categories
- Executive dashboard wireframe concept
- Data integration requirements by source
- 3-phase implementation plan

---

### Example 2: Manufacturing Operations Dashboard

**Context:** Manufacturing company needs real-time visibility into plant operations

**Copy-paste this prompt:**

```
I need to develop a comprehensive business requirements framework for a dashboard solution with the following context:

### Organization Context
- Organization name: PrecisionMfg Corp
- Industry sector: Manufacturing (discrete manufacturing, automotive parts)
- Company size: Enterprise (3,500 employees, 4 plants across US)
- Strategic objectives: Efficiency (reduce scrap 25%), Quality (zero defect shipments), Compliance (ISO 9001)
- Dashboard scope: Operational (plant managers, shift supervisors, quality engineers)

### Stakeholder Requirements
- Primary users: Plant managers (4), Shift supervisors (24), Quality engineers (8), VP Operations
- User count: 50 users across 4 facilities
- Technical expertise level: Mixed - managers are business users, supervisors need simple interfaces
- Decision-making needs: Real-time production decisions, shift handoff, quality escalation
- Key stakeholders: VP Operations (sponsor), Plant Manager - Detroit (pilot site)

### Dashboard Portfolio
- Executive dashboards needed: 1 cross-plant operations summary for VP
- Departmental dashboards: Per-plant production, quality, maintenance, safety
- Real-time monitoring requirements: Production rates every 5 minutes, quality alerts immediate
- Mobile dashboard needs: Yes - supervisors walk the floor with tablets

### System Integration Needs
- ERP system: SAP S/4HANA (production orders, inventory, costs)
- CRM system: None (B2B with EDI)
- Other critical systems: Ignition SCADA (machine data), Plex MES (production tracking), Maximo (maintenance)
- External data sources: Customer EDI portals, supplier delivery tracking

### Key Performance Indicators

**Financial Metrics:**
- Revenue indicators: Production value, cost per unit
- Profitability measures: Plant-level margin, scrap cost, overtime cost
- Cash flow tracking: Inventory turns, WIP value
- Budget variance: Maintenance budget, labor budget

**Operational Metrics:**
- Process efficiency: OEE (target: 85%+), cycle time, changeover time, throughput
- Productivity measures: Units per labor hour, machine utilization
- Quality indicators: First pass yield (target: 99.5%), PPM defects, scrap rate
- Resource utilization: Machine availability, labor efficiency

**Customer Metrics:**
- Customer satisfaction: On-time delivery rate (target: 98%+), quality PPM to customer
- Customer lifecycle: Customer scorecard ratings
- Service quality: Lead time, order fill rate

Please provide:
1. Real-time operational KPI framework with alert thresholds
2. Plant floor dashboard requirements (big-screen displays)
3. Shift handoff dashboard design
4. Integration architecture for SCADA/MES/ERP data
5. Alerting and escalation workflow
```

**Expected Output:**
- Real-time OEE dashboard specification
- Alert threshold matrix by KPI
- Shift handoff report template
- Data refresh requirements (5-min, hourly, daily)

---

### Example 3: Healthcare Revenue Cycle Dashboard

**Context:** Hospital system needs visibility into revenue cycle performance

**Copy-paste this prompt:**

```
I need to develop a comprehensive business requirements framework for a dashboard solution with the following context:

### Organization Context
- Organization name: Regional Health Partners (3-hospital system)
- Industry sector: Healthcare (acute care hospitals + outpatient)
- Company size: Enterprise (8,000 employees, $1.2B annual revenue)
- Strategic objectives: Efficiency (reduce AR days 15%), Compliance (prevent denials), Growth (increase net revenue 5%)
- Dashboard scope: Departmental (Revenue Cycle leadership and staff)

### Stakeholder Requirements
- Primary users: CFO, Revenue Cycle Director, Billing Managers (3), Coding Supervisors (2)
- User count: 25 revenue cycle staff + executive leadership
- Technical expertise level: Business users familiar with healthcare metrics
- Decision-making needs: Daily worklist prioritization, denial management, payer negotiation
- Key stakeholders: CFO (sponsor), Revenue Cycle Director (owner), IT Director (technical)

### Dashboard Portfolio
- Executive dashboards needed: 1 CFO revenue cycle summary (monthly board reporting)
- Departmental dashboards: Billing/Collections, Coding, Denials Management, Payer Analysis
- Real-time monitoring requirements: Claim status updates daily, denial alerts real-time
- Mobile dashboard needs: Limited - primarily desktop users

### System Integration Needs
- ERP system: Workday (financials)
- CRM system: None
- Other critical systems: Epic (EHR/billing), Waystar (claims clearinghouse), Contract Manager
- External data sources: Payer portals (via Waystar), CMS benchmarks

### Key Performance Indicators

**Financial Metrics:**
- Revenue indicators: Net patient revenue, gross-to-net ratio, case mix index
- Profitability measures: Cost to collect, collection rate by payer
- Cash flow tracking: Days in AR (target: <45), cash collections, bad debt write-offs
- Budget variance: Revenue vs budget, denials as % of revenue

**Operational Metrics:**
- Process efficiency: Clean claim rate (target: 95%+), coding turnaround, billing lag
- Productivity measures: Claims processed per FTE, accounts worked per day
- Quality indicators: Coding accuracy, first-pass resolution rate
- Resource utilization: Staff productivity by function

**Customer Metrics:**
- Customer satisfaction: Patient billing satisfaction, payment plan adoption
- Customer lifecycle: Patient financial engagement
- Service quality: Call center wait time, statement clarity

Please provide:
1. Revenue cycle KPI framework aligned with HFMA benchmarks
2. Denial management dashboard with root cause analysis
3. Payer performance scorecard design
4. AR aging analysis dashboard
5. Daily worklist prioritization logic
```

**Expected Output:**
- Revenue cycle scorecard with 20+ KPIs
- Denial waterfall analysis structure
- Payer contract performance comparison
- AR aging buckets with action triggers
