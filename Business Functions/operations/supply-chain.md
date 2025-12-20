---
category: operations
title: Supply Chain Readiness Assessment
tags:
- supply-chain-management
- vendor-relations
- logistics-coordination
- inventory-control
- readiness-assessment
use_cases:
- Assessing readiness to improve end-to-end supply chain performance (cost, service, working capital)
- Identifying constraints in planning, sourcing, inventory, and logistics before investing in new systems
- Creating a practical 90-day supply chain improvement roadmap with measurable targets
related_templates:
- operations/operations-supply-chain-optimization.md
- operations/process-optimization.md
- strategy/digital-transformation-roadmap.md
- strategy/okr-implementation-framework.md
industries:
- education
- finance
- government
- healthcare
- manufacturing
- nonprofit
- retail
- technology
type: framework
difficulty: intermediate
slug: supply-chain-readiness-assessment
---

# Supply Chain Readiness Assessment

## Purpose
Assess an organization's readiness to run and improve an end-to-end supply chain across six dimensions: Visibility & Data, Planning & Forecasting, Procurement & Supplier Management, Inventory & Fulfillment, Logistics Execution, and Risk & Performance Governance. Identify gaps, prioritize interventions, and produce a roadmap tied to measurable outcomes.

## Template

Conduct a comprehensive supply chain readiness assessment for {ORGANIZATION}, a {INDUSTRY} organization operating across {SUPPLY_CHAIN_SCOPE}.

Assess readiness across six dimensions, scoring each 1–5:

**1. VISIBILITY & DATA READINESS**
- End-to-end flow visibility (orders, inventory, lead times, capacity)
- Master data discipline (SKUs, suppliers, locations, BOM, units of measure)
- Data quality and timeliness (accuracy, latency, completeness)
- Integration across systems (ERP/WMS/TMS/OMS; EDI/APIs)
- Exception visibility (late orders, shortages, capacity constraints)
- Reporting and segmentation (by channel, product family, customer, region)

**2. PLANNING & FORECASTING READINESS**
- Demand planning approach (statistical, collaborative, promo/new product handling)
- Forecast measurement (accuracy, bias, MAPE by segment)
- S&OP/IBP cadence (decision making, tradeoffs, scenario planning)
- Supply planning (capacity, constraints, lead times, allocation)
- Planning parameter governance (service levels, MOQs, lead times, lot sizes)
- Decision latency (how fast plans update when reality changes)

**3. PROCUREMENT & SUPPLIER MANAGEMENT READINESS**
- Category strategy and sourcing discipline (TCO, negotiation, segmentation)
- Contract and commercial controls (terms, SLAs, change management)
- Supplier qualification and onboarding (quality, compliance, risk)
- Supplier performance management (scorecards, QBRs, corrective actions)
- Collaboration mechanisms (forecast sharing, VMI/consignment where relevant)
- Supplier risk monitoring (single-source exposure, geopolitical/logistics risks)

**4. INVENTORY & FULFILLMENT READINESS**
- Inventory policy design (safety stock, reorder points, service level targets)
- Inventory accuracy (cycle counts, shrink, reconciliation)
- Allocation and prioritization rules (channel/customer segmentation)
- Obsolescence and lifecycle management (slow movers, end-of-life)
- Order management discipline (backorders, substitutions, promise dates)
- Working capital visibility (cash-to-cash, inventory turns, aged inventory)

**5. LOGISTICS EXECUTION READINESS**
- Warehouse process stability (receiving, putaway, pick/pack/ship, returns)
- Transportation management (carrier strategy, routing, consolidation)
- OTIF/perfect order measurement and root-cause discipline
- Capacity management (labor planning, peak planning, slotting)
- Technology enablement (WMS/TMS/yard/telematics where applicable)
- Continuous improvement in operations (standard work, controls, escalation)

**6. RISK & PERFORMANCE GOVERNANCE READINESS**
- KPI ownership and cadence (service, cost, quality, working capital)
- Cross-functional decision rights (tradeoffs among cost, service, inventory)
- Risk and resilience practices (dual sourcing, buffers, playbooks, BCP)
- Compliance and sustainability requirements (as applicable) integrated into decisions
- Portfolio management (initiative pipeline, sequencing, dependency management)
- Learning system (post-mortems, supplier learnings, standard playbooks)

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** - Overall score, maturity level, top 3 priorities, major risks

2. **DIMENSION SCORECARD** - Table with score (X.X/5) and key finding per dimension

3. **NETWORK & FLOW BASELINE** - Map + baseline metrics (OTIF, turns, lead times, cost-to-serve)

4. **GAP ANALYSIS** - Top 5 gaps ranked by impact and urgency, with recommended actions

5. **90-DAY ROADMAP** - Sequenced actions across planning, suppliers, inventory, logistics, governance

6. **SUCCESS METRICS** - Baseline vs 30/60/90-day targets (OTIF, turns, forecast bias, expedited spend)

Use this maturity scale:
- 1.0-1.9: Initial (ad-hoc, limited visibility, reactive execution)
- 2.0-2.9: Developing (basic processes, inconsistent planning, frequent exceptions)
- 3.0-3.9: Defined (repeatable methods, managed KPIs, improving reliability)
- 4.0-4.9: Managed (integrated planning, disciplined execution, proactive supplier management)
- 5.0: Optimized (resilient, data-driven, continuously improving end-to-end system)

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ORGANIZATION]` | Name of the organization | "Summit Outdoor Retail" |
| `[SUPPLY_CHAIN_SCOPE]` | Scope (products, channels, regions, nodes) | "Omnichannel (stores + ecomm) in US/Canada" |
| `[PERFORMANCE_GOALS]` | Desired outcomes and constraints | "+5 pts OTIF, -15% inventory, -10% freight cost" |

## Example

**Retail - Omnichannel Fulfillment**

> Assess supply chain readiness for **Summit Outdoor Retail** across **omnichannel (stores + ecomm) in US/Canada** to achieve **+5 pts OTIF, -15% inventory, -10% freight cost**. (1) Visibility—inventory accuracy is uneven; lead time data is outdated; exception reporting is limited. (2) Planning—forecast accuracy varies heavily by category; promo uplift is manual; S&OP decisions are slow. (3) Suppliers—top suppliers lack scorecards; single-source risk exists in key categories. (4) Inventory—safety stocks are rule-of-thumb; allocations favor ecomm causing store stockouts. (5) Logistics—warehouse picking errors drive returns; carrier mix creates peak surcharges. (6) Governance—KPIs exist but owners are unclear; tradeoffs aren’t decided consistently. Provide scorecard, top gaps, and a 90-day roadmap focused on master data, planning parameters, and OTIF root-cause.

