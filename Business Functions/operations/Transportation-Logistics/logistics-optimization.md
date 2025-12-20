---
category: operations
title: Logistics Optimization & Supply Chain Transportation Readiness Assessment
tags:
- logistics-optimization
- last-mile-delivery
- multimodal-transport
- supply-chain-visibility
- readiness-assessment
use_cases:
- Evaluating readiness to optimize logistics costs and service levels end-to-end
- Identifying gaps in network design, multimodal strategy, and visibility tooling
- Creating a 12-month roadmap for transportation and logistics performance improvement
related_templates:
- operations/Transportation-Logistics/route-optimization-framework.md
- operations/Transportation-Logistics/warehouse-management-system.md
- operations/Transportation-Logistics/fleet-management-system.md
industries:
- finance
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: logistics-optimization-readiness-assessment
---

# Logistics Optimization & Supply Chain Transportation Readiness Assessment

## Purpose
Assess readiness to optimize transportation and logistics operations across network design, multimodal planning, last-mile execution, visibility, and cost management.

## Template

Conduct a logistics optimization readiness assessment for {LOGISTICS_CONTEXT}.

Assess readiness across six dimensions, scoring each 1–5:

**1. NETWORK DESIGN & FLOWS**
- Network fit for service promise (delivery speed, coverage, variability)
- Lane design and freight flow analysis (where volume moves and why)
- Capacity planning for peaks and disruptions
- Decision tooling (modeling, what-if analysis) and refresh cadence

**2. MULTIMODAL TRANSPORTATION & CARRIER STRATEGY**
- Mode strategy (parcel, LTL/FTL, rail, ocean, air, intermodal)
- Carrier portfolio design (consolidation vs resilience)
- Procurement discipline (RFP cadence, rate governance, contract terms)
- Performance management (OTD, claims, tender acceptance, accessorials)

**3. LAST-MILE DELIVERY EXECUTION**
- Delivery model maturity (in-house, 3PL, hybrid) and cost control
- Route optimization capability (stop density, time windows, re-optimization)
- Customer experience: ETA accuracy, notifications, POD, returns handoff
- Urban logistics tactics (micro-fulfillment, lockers, consolidation)

**4. TECHNOLOGY & VISIBILITY**
- TMS/WMS maturity and adoption (process compliance)
- Track-and-trace coverage and event quality (milestones, latency)
- Exception management workflows and escalation paths
- Analytics maturity (dashboards, root-cause, predictive capability)

**5. WAREHOUSE / FULFILLMENT INTERFACES**
- Dock scheduling and yard management alignment
- Pick/pack/ship readiness to meet transportation cutoffs
- Inventory accuracy and master data quality (addresses, weights/dims)
- Packaging and cube optimization (impact on freight and damage)

**6. COST GOVERNANCE & CONTINUOUS IMPROVEMENT**
- Unit economics: cost/shipment, cost/lb, cost/order, cost/stop
- Benchmarking practice and target setting
- Savings identification and benefits tracking (avoid double-counting)
- Continuous improvement rhythm and accountability

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** – Overall score, maturity level, top 3 priorities, ROI range

2. **DIMENSION SCORECARD** – Table with score (X.X/5) and key finding per dimension

3. **CURRENT BASELINE** – Current KPIs (on-time %, cost per shipment, transit times, visibility %, claims)

4. **GAP ANALYSIS** – Top 5 gaps ranked by impact and urgency with recommended actions

5. **ROADMAP** – 0–90 days, 3–6 months, 6–12 months plan

6. **SUCCESS METRICS** – Current vs 6‑month and 12‑month targets

Use this maturity scale:
- 1.0–1.9: Initial (manual, reactive, low visibility)
- 2.0–2.9: Developing (basic tools, inconsistent execution)
- 3.0–3.9: Defined (standard processes, measurable control)
- 4.0–4.9: Managed (integrated systems, proactive optimization)
- 5.0: Optimized (predictive, continuously improving, benchmark-leading)

---

## Variables

| Variable | Description | Example |
|---|---|---|
| {LOGISTICS_CONTEXT} | Network, volumes, service promise, constraints | "Omnichannel retailer, 6 DCs, 2-day delivery promise, 5.5M shipments/year" |
| {TARGET_OUTCOMES} | Cost and service targets | "Cost/shipment -10%, on-time 96%, visibility 99%" |
| {CONSTRAINTS} | Hard constraints | "Fixed DC footprint, carrier contracts renew in 12 months" |

---

## Example

### Input
- **{LOGISTICS_CONTEXT}:** Omnichannel retailer, 6 DCs, 18 cross-docks, 5.8M shipments/year; service target is 2-day delivery on core SKUs
- **{TARGET_OUTCOMES}:** Reduce cost/shipment 10%, improve on-time delivery 87% → 96%, raise shipment visibility 70% → 98%
- **{CONSTRAINTS}:** DC footprint fixed for 18 months; TMS adoption low; parcel contracts renew next year

### 1) EXECUTIVE SUMMARY
- **Overall score:** 2.4/5 (Developing)
- **Top priorities:** (1) improve TMS adoption + visibility, (2) carrier portfolio + procurement discipline, (3) last-mile route optimization with CX metrics

### 2) DIMENSION SCORECARD
| Dimension | Score | Key finding |
|---|---:|---|
| Network Design & Flows | 2.2/5 | Network decisions not refreshed; limited what-if modeling |
| Multimodal & Carrier Strategy | 2.5/5 | Carrier base fragmented; performance metrics not tied to actions |
| Last-Mile Execution | 2.3/5 | Stop density and time-window performance not actively managed |
| Technology & Visibility | 2.6/5 | TMS exists but adoption is inconsistent; visibility gaps remain |
| Warehouse Interfaces | 2.4/5 | Cutoff misses due to dock/pack variability; master data issues |
| Cost Governance & CI | 2.2/5 | Cost tracked at aggregate level; benefits not audited regularly |

### 3) CURRENT BASELINE
- On-time delivery: 87%
- Cost/shipment: $28.50
- Visibility: 70% end-to-end milestone coverage
- Claims/damage: 1.6% of shipments

### 4) GAP ANALYSIS (Top 5)
1. Low TMS process adherence prevents consistent planning and measurement
2. Carrier performance signals don’t trigger operational changes
3. Last-mile routing lacks daily re-optimization and CX instrumentation
4. Warehouse cutoffs and master data degrade transportation plans
5. Savings not tracked with governance; projects lose momentum

### 5) ROADMAP
- **0–90 days:** KPI dictionary; visibility milestones; exception workflows; TMS adoption push; master data cleanup
- **3–6 months:** carrier scorecards + RFP prep; lane rationalization; last-mile pilot with route optimization
- **6–12 months:** network what-if refresh; procurement cycle; scale control-tower practices and dashboards

### 6) SUCCESS METRICS
- 6 months: on-time 92%, visibility 90%, cost/shipment -4%
- 12 months: on-time 96%, visibility 98%, cost/shipment -10%

---

