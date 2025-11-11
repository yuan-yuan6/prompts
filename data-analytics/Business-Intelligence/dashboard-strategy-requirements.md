---
category: data-analytics/Business-Intelligence
last_updated: 2025-11-09
related_templates:
- dashboard-ux-design.md
- dashboard-data-architecture.md
- dashboard-design-overview.md
tags:
- data-analytics
- business-intelligence
- strategy
- requirements
- kpi
title: Dashboard Strategy & Business Requirements
use_cases:
- Defining dashboard business requirements
- Stakeholder alignment
- KPI framework development
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
