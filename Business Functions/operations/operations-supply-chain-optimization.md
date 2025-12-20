---
category: operations
title: Supply Chain & Logistics Readiness Assessment
tags:
- supply-chain
- inventory-management
- demand-planning
- procurement
- readiness-assessment
use_cases:
- Assessing readiness to optimize end-to-end supply chain performance (cost, service, working capital, resilience)
- Identifying capability gaps across demand planning, inventory policy, logistics execution, and supplier management
- Creating a prioritized roadmap to improve forecast accuracy, inventory turns, on-time delivery, and risk posture
related_templates:
- operations/operations-resource-management.md
- operations/lean-six-sigma-implementation.md
- strategy/digital-transformation-roadmap.md
industries:
- finance
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: supply-chain-readiness-assessment
---

# Supply Chain & Logistics Readiness Assessment

## Purpose
Assess an organization's readiness to optimize and modernize its end-to-end supply chain across six dimensions: Demand Planning, Inventory & Working Capital, Network & Logistics Execution, Supplier & Procurement, Data & Systems, and Risk & Governance. Identify gaps, prioritize initiatives, and create a roadmap for measurable improvements.

## Template

Conduct a comprehensive supply chain readiness assessment for {ORGANIZATION}, a {INDUSTRY} organization operating {NETWORK_SCOPE} and managing approximately {SKU_COUNT} SKUs.

Assess readiness across six dimensions, scoring each 1-5:

**1. DEMAND PLANNING & S&OP READINESS**
- Forecasting approach (statistical/ML/hybrid) and accuracy by segment
- Forecast bias tracking and exception management
- S&OP / IBP cadence, roles, and decision rights
- Promotion/seasonality/new product planning capability
- Demand signal integration (orders, POS, market intel)
- Planning time horizons and scenario planning capability

**2. INVENTORY & WORKING CAPITAL READINESS**
- Inventory segmentation (ABC/XYZ, margin, service criticality)
- Safety stock and reorder parameter governance
- Inventory accuracy (cycle counts, shrink, adjustments)
- Replenishment logic (min/max, MRP, pull/kanban) appropriateness
- Obsolescence and lifecycle management
- Working capital visibility (days of inventory, cash-to-cash)

**3. NETWORK & LOGISTICS EXECUTION READINESS**
- Network design fit (DC placement, flow paths, cross-dock/direct ship)
- OTIF / service level performance and lead time variability
- Transportation strategy (mode mix, carrier management, routing)
- Warehouse execution capability (slotting, picking, throughput, labor)
- Returns and reverse logistics maturity
- Continuous improvement capability for logistics operations

**4. SUPPLIER & PROCUREMENT READINESS**
- Supplier segmentation and performance scorecards
- Lead time reliability and capacity collaboration with suppliers
- Contracting strategy (terms, penalties, flexibility, dual sourcing)
- Procurement process maturity (category strategy, sourcing events)
- Supplier risk assessment (financial, geo, single points of failure)
- Quality management (incoming inspection, supplier corrective actions)

**5. DATA, SYSTEMS & ANALYTICS READINESS**
- ERP/WMS/TMS/Planning tool coverage and integration
- Master data quality (item, BOM, lead times, MOQ, pack sizes)
- Visibility into inventory, orders, shipments, and exceptions
- KPI dashboards and self-serve analytics capability
- Data governance and ownership for planning parameters
- Automation opportunities (alerts, exception workflows, EDI/API)

**6. RISK, COMPLIANCE & GOVERNANCE READINESS**
- Risk management approach (scenarios, stress tests, playbooks)
- Compliance requirements (trade, customs, quality, privacy where relevant)
- Governance cadence (weekly execution, monthly S&OP, quarterly network review)
- KPI ownership and accountability (service, cost, inventory, resilience)
- Incident response and disruption management
- Change management capability for process/system rollouts

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** - Overall readiness score, maturity level, top 3 priorities, investment range and timeline

2. **DIMENSION SCORECARD** - Table with score (X.X/5) and key finding per dimension

3. **SEGMENT READINESS** - Readiness by product/channel segment (✓/△/✗) and expected impact on service/cost/inventory

4. **GAP ANALYSIS** - Top 5 gaps ranked by business impact (service, cost, working capital, risk), with recommended actions

5. **ROADMAP** - Quarterly plan across planning, inventory policy, logistics execution, supplier programs, and systems/data

6. **SUCCESS METRICS** - Baseline vs 6-month and 12-month targets for: forecast accuracy, inventory turns, OTIF, lead time variability, expedited freight %, obsolescence

Use this maturity scale:
- 1.0-1.9: Initial (reactive, siloed, limited visibility)
- 2.0-2.9: Developing (basic planning, inconsistent execution, spreadsheet-heavy)
- 3.0-3.9: Defined (standard processes, managed KPIs, improving integration)
- 4.0-4.9: Managed (optimized policies, integrated systems, proactive exception handling)
- 5.0: Optimized (predictive, resilient, continuously improving, near real-time visibility)

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ORGANIZATION]` | Name of the organization | "NorthStar Retail" |
| `[SKU_COUNT]` | Approximate number of active SKUs | "12,000" |
| `[NETWORK_SCOPE]` | Network footprint | "2 factories, 1 central DC, 5 regional DCs, e-commerce + stores" |

## Example

**Retail - Forecast and Inventory Stabilization**

> Assess supply chain optimization readiness for **NorthStar Retail** operating **2 factories, 1 central DC, 5 regional DCs, e-commerce + stores** and managing **12,000** SKUs. (1) Demand planning—forecast accuracy ~62% for seasonal categories, no formal bias tracking, S&OP is informal and attendance inconsistent. (2) Inventory policy—parameters not governed, safety stock copied across items, inventory accuracy ~92% with frequent adjustments. (3) Logistics—OTIF 88%, expedited freight is rising, lead times vary widely, WMS exists but labor planning is manual. (4) Suppliers—no segmentation, performance tracked ad-hoc, single-source risk unassessed. (5) Data & systems—ERP and WMS not fully integrated, master data quality issues (MOQ/lead times), limited exception visibility. (6) Governance—KPIs exist but unclear owners; disruption playbooks are minimal. Provide scorecard, top gaps, and a 12-month roadmap to reach 85% forecast accuracy, 95% inventory accuracy, 95% OTIF, and +2 inventory turns.

