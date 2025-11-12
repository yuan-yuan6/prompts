---
category: sustainability/Climate-Environment
last_updated: 2025-11-12
title: Carbon Footprint & GHG Accounting
tags:
  - sustainability
  - carbon-footprint
  - ghg-emissions
  - scope-1-2-3
  - ghg-protocol
use_cases:
  - Measuring comprehensive greenhouse gas (GHG) emissions inventory
  - Calculating Scope 1, 2, and 3 emissions following GHG Protocol
  - Establishing carbon footprint baseline for target setting
  - Supporting carbon disclosure (CDP, TCFD, CSRD, SEC)
related_templates:
  - sustainability/climate-strategy-net-zero.md
  - sustainability/renewable-energy-transition.md
  - sustainability/esg-reporting-disclosure.md
industries:
  - technology
  - finance
  - healthcare
  - retail
  - manufacturing
  - energy
  - construction
---

# Carbon Footprint & GHG Accounting Template

## Purpose
Measure comprehensive greenhouse gas emissions inventory following GHG Protocol, calculate Scope 1, 2, and 3 emissions accurately, establish carbon footprint baseline, support climate strategy and disclosure, and enable science-based target setting.

## Quick Start

**Need carbon footprint quickly?** Use this streamlined approach:

### Minimal Example
```
Company: Mid-size manufacturing (10 facilities, $500M revenue)
Baseline Year: 2024

Scope 1 (Direct): 18,500 tCO2e
- Natural gas (boilers): 12,000 tCO2e
- Diesel (generators, forklifts): 4,200 tCO2e
- Refrigerants (leaks): 2,300 tCO2e

Scope 2 (Electricity): 8,200 tCO2e (market-based)
- Electricity: 42,000 MWh × 0.195 tCO2e/MWh
- Renewable: 35% (RECs)

Scope 3 (Value Chain): 45,600 tCO2e (8 of 15 categories measured)
- Cat 1 - Purchased goods: 28,000 tCO2e (60%)
- Cat 4 - Upstream transport: 8,500 tCO2e (18%)
- Cat 6 - Business travel: 3,200 tCO2e (7%)
- Cat 7 - Commuting: 2,900 tCO2e (6%)
- Other categories: 3,000 tCO2e (9%)

Total: 72,300 tCO2e (Scope 3 = 63% of footprint)
Intensity: 145 tCO2e per $M revenue

Next Steps: Set SBTi targets, expand Scope 3 measurement, implement tracking system
```

### When to Use This
- Establishing first comprehensive GHG inventory
- Preparing for science-based target setting (SBTi)
- Responding to carbon disclosure requests (CDP, TCFD)
- Regulatory compliance (SEC climate rules, CSRD)
- Baseline for decarbonization strategy

### Basic 4-Step Workflow
1. **Scope & Boundary** - Define organizational and operational boundaries (1 week)
2. **Data Collection** - Gather activity data (energy, fuel, materials, travel) (3-4 weeks)
3. **Calculation** - Apply emission factors, calculate all scopes (2-3 weeks)
4. **Reporting** - Document methodology, prepare disclosure (2 weeks)

---

## Template

```
You are a carbon accounting and GHG Protocol expert. Calculate a comprehensive greenhouse gas emissions inventory for [COMPANY_NAME] in [INDUSTRY] with [OPERATIONS] covering [ORGANIZATIONAL_BOUNDARY] for [REPORTING_YEAR] following [GHG_PROTOCOL_STANDARDS] to establish [CARBON_FOOTPRINT_BASELINE].

### 1. ORGANIZATIONAL & OPERATIONAL BOUNDARIES

Organizational Boundary:
Approach: [EQUITY_SHARE/FINANCIAL_CONTROL/OPERATIONAL_CONTROL]
Rationale: [WHY_THIS_APPROACH]
Entities included: [SUBSIDIARIES/FACILITIES/JVS]
Entities excluded: [WHAT_AND_WHY]

Operational Boundary:
Scope 1: Direct GHG emissions [INCLUDED]
Scope 2: Indirect emissions from purchased electricity, steam, heating, cooling [INCLUDED]
Scope 3: Other indirect emissions in value chain [INCLUDED - CATEGORIES_LISTED]

Geographic Coverage: [ALL_OPERATIONS/SPECIFIC_COUNTRIES]
Reporting Period: [START_DATE to END_DATE]

### 2. SCOPE 1 (DIRECT EMISSIONS)

Scope 1 Definition:
Direct GHG emissions from sources owned or controlled by the company

Categories:

Stationary Combustion:
Emission Source: [BOILERS/FURNACES/HEATERS]
Activity Data:
- Natural gas: [THERMS or MMBTU or M3]
- Fuel oil: [GALLONS or LITERS]
- Propane: [GALLONS]
- Coal: [TONNES]

Calculation:
Natural gas example:
- Consumption: 1,200,000 therms
- Emission factor: 0.0053 tCO2e/therm (EPA)
- Emissions: 1,200,000 × 0.0053 = 6,360 tCO2e

Mobile Combustion:
Emission Source: [COMPANY_VEHICLES/FORKLIFTS]
Activity Data:
- Gasoline vehicles: [GALLONS] or [MILES/MPG]
- Diesel vehicles: [GALLONS] or [MILES/MPG]
- Fleet count: [VEHICLES_BY_TYPE]

Calculation:
Diesel example:
- Consumption: 50,000 gallons
- Emission factor: 0.0102 tCO2e/gallon (EPA)
- Emissions: 50,000 × 0.0102 = 510 tCO2e

Process Emissions:
Emission Source: [INDUSTRIAL_PROCESSES]
Examples:
- Cement production: [CALCINATION_CO2]
- Chemical reactions: [PROCESS_CO2]
- Metal production: [CO2_FROM_REDUCTION]

Calculation:
Based on process-specific emission factors or mass balance

Fugitive Emissions:
Emission Source: [REFRIGERANTS/LEAKS]
Activity Data:
- Refrigerant type: [R-410A/R-134a/R-404A]
- Amount leaked/recharged: [POUNDS or KG]
- Global Warming Potential (GWP): [GWP_VALUE]

Calculation:
R-404A refrigerant:
- Leaked: 100 pounds
- GWP: 3,922
- Emissions: (100 lbs / 2,204.62 lbs/tonne) × 3,922 = 178 tCO2e

Scope 1 Total:
Source | Activity | Emission Factor | tCO2e | %
-------|----------|-----------------|-------|---
Natural gas | 1.2M therms | 0.0053 tCO2e/therm | 6,360 | 34%
Diesel | 50K gallons | 0.0102 tCO2e/gal | 510 | 3%
Company fleet | 500K miles | var by vehicle | 450 | 2%
Refrigerants | 100 lbs leaked | GWP 3,922 | 178 | 1%
[Other] | [Data] | [Factor] | [Amount] | [%]
**Total Scope 1** | | | **18,500** | **100%**

### 3. SCOPE 2 (PURCHASED ENERGY)

Scope 2 Definition:
Indirect GHG emissions from purchased electricity, steam, heating, and cooling

Electricity:
Activity Data by Facility:
- Facility 1: [MWH] - Grid: [REGION] - Factor: [KG_CO2E/MWH]
- Facility 2: [MWH] - Grid: [REGION] - Factor: [KG_CO2E/MWH]
Total electricity: [TOTAL_MWH]

Location-Based Method:
Uses average emission factor for grid where electricity consumed
Calculation:
- Total electricity: 42,000 MWh
- Grid factor (regional): 0.385 tCO2e/MWh
- Location-based emissions: 42,000 × 0.385 = 16,170 tCO2e

Market-Based Method:
Reflects emissions from specific electricity products purchased
Adjustments:
- Grid electricity: 27,300 MWh × 0.385 = 10,511 tCO2e
- Renewable PPAs: 10,000 MWh × 0 = 0 tCO2e
- RECs purchased: 4,700 MWh × 0 = 0 tCO2e
- Market-based emissions: 10,511 tCO2e
- Renewable %: 35% [(10,000+4,700)/42,000]

Purchased Steam/Heat/Cool (if applicable):
- Steam: [MMBTU] × [FACTOR] = [TCO2E]
- District heating: [MWH] × [FACTOR] = [TCO2E]
- District cooling: [MWH] × [FACTOR] = [TCO2E]

Scope 2 Reporting:
Location-based: [TCO2E]
Market-based: [TCO2E]
Primary method for targets: [MARKET-BASED_RECOMMENDED]

Scope 2 Total:
Location-based: 16,170 tCO2e
Market-based: 10,511 tCO2e (with 35% renewable)

Quality Score (Scope 2):
- Metered data: [%]
- Estimated data: [%]
- Emission factors: [REGION-SPECIFIC/DEFAULT]

### 4. SCOPE 3 (VALUE CHAIN)

Scope 3 Definition:
All other indirect emissions in value chain (upstream and downstream)

Upstream Categories:

Category 1 - Purchased Goods & Services:
Scope: Cradle-to-gate emissions from production of purchased products
Data Sources:
- Procurement data: $[SPEND_BY_CATEGORY]
- Supplier-specific data: [IF_AVAILABLE]
Calculation:
Spend-based method:
- Material A spend: $10M × 0.5 tCO2e/$1,000 = 5,000 tCO2e
- Material B spend: $15M × 0.8 tCO2e/$1,000 = 12,000 tCO2e
- Services: $5M × 0.3 tCO2e/$1,000 = 1,500 tCO2e
Total Cat 1: 28,000 tCO2e
Data quality: [SECONDARY_SPEND-BASED]

Category 2 - Capital Goods:
Scope: Cradle-to-gate emissions from capital purchases
Calculation:
- Machinery: $[CAPEX] × [FACTOR] = [TCO2E]
- Vehicles: $[CAPEX] × [FACTOR] = [TCO2E]
Total Cat 2: [TCO2E]

Category 3 - Fuel & Energy Related:
Scope: Extraction, production, transport of fuels/energy (not in Scope 1/2)
Calculation:
- Upstream emissions of natural gas: [SCOPE_1_FUEL] × [FACTOR] = [TCO2E]
- Well-to-tank emissions: [CALCULATION]
- T&D losses (electricity): [MWH] × [T&D_FACTOR] = [TCO2E]
Total Cat 3: [TCO2E]

Category 4 - Upstream Transportation & Distribution:
Scope: Transportation of purchased products in vehicles not owned by company
Data Sources:
- Freight bills: [TONNES × KM or SHIPMENTS]
- Supplier shipments to company
Calculation:
- Truck freight: 5,000 tonnes × 500 km × 0.000062 tCO2e/tonne-km = 155 tCO2e
- Ocean freight: [CALCULATION]
- Air freight: [CALCULATION]
Total Cat 4: 8,500 tCO2e
Data quality: [DISTANCE-BASED]

Category 5 - Waste Generated in Operations:
Scope: Disposal and treatment of waste
Calculation:
- Landfill waste: 500 tonnes × 0.5 tCO2e/tonne = 250 tCO2e
- Recycled: [TONNES] × [AVOIDED_FACTOR]
- Incinerated: [TONNES] × [FACTOR]
Total Cat 5: [TCO2E]

Category 6 - Business Travel:
Scope: Employee travel in vehicles not owned by company
Data Sources:
- Airfare data: [MILES or SPEND]
- Hotel nights: [COUNT]
- Rental cars: [MILES or DAYS]
Calculation:
- Air travel: 10M miles × 0.00023 tCO2e/mile = 2,300 tCO2e
- Hotel: 5,000 nights × 12.3 kg CO2e/night = 62 tCO2e
- Rental cars: [CALCULATION]
Total Cat 6: 3,200 tCO2e

Category 7 - Employee Commuting:
Scope: Employees traveling to/from work
Data Sources:
- Employee survey: [COMMUTE_DISTANCE × DAYS × EMPLOYEES]
- Assumptions: [AVG_DISTANCE/VEHICLE/FREQUENCY]
Calculation:
- 2,000 employees × 20 miles RT × 220 days × 0.000324 tCO2e/mile = 2,850 tCO2e
- Remote work: [ADJUSTMENT]
Total Cat 7: 2,900 tCO2e

Category 8 - Upstream Leased Assets:
Scope: Operation of assets leased by company (not in Scope 1/2)
Calculation:
If applicable: [LEASED_OFFICE/WAREHOUSE_EMISSIONS]
Total Cat 8: [TCO2E or NOT_MATERIAL]

Downstream Categories:

Category 9 - Downstream Transportation & Distribution:
Scope: Transport and storage of sold products (after sale)
Calculation:
- Retail distribution: [TONNES] × [KM] × [FACTOR] = [TCO2E]
Total Cat 9: [TCO2E or NOT_APPLICABLE]

Category 10 - Processing of Sold Products:
Scope: Industrial customers processing company's sold products
Applicability: [IF_B2B_INTERMEDIATE_PRODUCTS]
Total Cat 10: [TCO2E or NOT_APPLICABLE]

Category 11 - Use of Sold Products:
Scope: End use of products by customers (e.g., electricity consumption)
Relevance: [HIGH_FOR_ENERGY-USING_PRODUCTS]
Calculation:
- Products sold: [UNITS]
- Lifetime energy use: [KWH_PER_UNIT × LIFETIME_YEARS]
- Emissions: [ENERGY] × [GRID_FACTOR] = [TCO2E]
Total Cat 11: [TCO2E]

Example - Electronics:
- 100,000 devices sold
- 50 kWh/year/device × 5 year life = 250 kWh lifetime
- 100,000 × 250 × 0.385 tCO2e/MWh = 9,625 tCO2e

Category 12 - End-of-Life Treatment:
Scope: Waste disposal and treatment of sold products
Calculation:
- Product mass: [TONNES_SOLD]
- Disposal method: [LANDFILL/RECYCLING/INCINERATION_%]
- Emissions: [TONNES] × [FACTOR_BY_METHOD] = [TCO2E]
Total Cat 12: [TCO2E]

Category 13 - Downstream Leased Assets:
Scope: Operation of assets owned and leased to others
Applicability: [IF_LESSOR]
Total Cat 13: [NOT_APPLICABLE_FOR_MOST]

Category 15 - Investments:
Scope: Financed emissions from investments (relevant for financial sector)
Calculation:
- Equity investments: [PROPORTIONAL_EMISSIONS]
- Debt (loans): [FINANCED_EMISSIONS_PCAF_METHOD]
Total Cat 15: [TCO2E_FOR_FINANCIAL_INSTITUTIONS]

Scope 3 Summary:
Category | tCO2e | % of Scope 3 | Data Quality
---------|-------|--------------|-------------
1 - Purchased goods | 28,000 | 61% | Secondary (spend-based)
4 - Upstream transport | 8,500 | 19% | Modeled (distance-based)
6 - Business travel | 3,200 | 7% | Primary (actual miles)
7 - Commuting | 2,900 | 6% | Survey + assumptions
[Other categories] | 3,000 | 7% | Various
**Total Scope 3** | **45,600** | **100%** | **8 of 15 categories**

### 5. TOTAL CARBON FOOTPRINT

Emissions Summary:
Scope | tCO2e | % of Total
------|-------|------------
Scope 1 (Direct) | 18,500 | 26%
Scope 2 (Electricity - market) | 8,200 | 11%
Scope 3 (Value chain) | 45,600 | 63%
**Total** | **72,300** | **100%**

Intensity Metrics:
- Per revenue: 72,300 tCO2e / $500M = 145 tCO2e per $M revenue
- Per employee: 72,300 / 2,000 = 36 tCO2e per employee
- Per facility: 72,300 / 10 = 7,230 tCO2e per facility
- Per product: [IF_APPLICABLE]

Trends:
Year | Scope 1 | Scope 2 | Scope 3 | Total | Intensity
-----|---------|---------|---------|-------|----------
2022 | 19,200 | 10,800 | 42,000 | 72,000 | 160 tCO2e/$M
2023 | 18,800 | 9,500 | 43,800 | 72,100 | 152 tCO2e/$M
2024 | 18,500 | 8,200 | 45,600 | 72,300 | 145 tCO2e/$M
Change | -4% | -24% | +9% | +0.4% | -9% (intensity improving)

### 6. DATA QUALITY & UNCERTAINTY

Data Quality Assessment:
Scope 1:
- Primary metered data: 85%
- Estimates: 15%
- Uncertainty: ±5%

Scope 2:
- Primary metered data: 95%
- Emission factors: Regional-specific
- Uncertainty: ±3%

Scope 3:
- Primary data: 20%
- Secondary (supplier-specific): 15%
- Estimates (spend/industry average): 65%
- Uncertainty: ±30-50%

Data Gaps:
- Scope 3 Cat 10, 11, 12, 13 not measured (not material for our business)
- Scope 3 Cat 2 (capital goods) partial measurement
- Some Scope 3 using spend-based (lower quality)
Improvement plan: [HOW_TO_IMPROVE]

### 7. EMISSION FACTORS USED

Scope 1 & 2:
- US EPA emission factors (latest)
- IEA grid factors by country/region
- IPCC GWP values (AR6 or AR5)

Scope 3:
- DEFRA spend-based factors
- GLEC Framework (logistics)
- Supplier-specific data (where available)
- EEIO models (spend-based fallback)

### 8. METHODOLOGY & ASSUMPTIONS

GHG Protocol Standards:
- Corporate Accounting & Reporting Standard
- Corporate Value Chain (Scope 3) Standard

Assumptions:
- Organizational boundary: Operational control
- Base year: 2024
- Scope 3 materiality threshold: >5% of total Scope 3
- Employee commute: Average 20 miles round-trip, 220 days/year
- [OTHER_KEY_ASSUMPTIONS]

Exclusions:
- [WHAT_EXCLUDED_AND_WHY]
- Materiality: [CATEGORIES_<5%]

### 9. VERIFICATION & ASSURANCE

Internal Review:
- Data collection: [PROCESS]
- Calculation review: [QA_PROCESS]
- Management approval: [SIGN-OFF]

External Assurance:
- Assurance level: [LIMITED/REASONABLE/NONE]
- Scope: [WHAT_ASSURED - typically Scope 1&2]
- Standard: [ISAE_3000]
- Provider: [FIRM]

### 10. REPORTING & DISCLOSURE

Internal Use:
- Baseline for climate strategy
- Input to science-based targets
- Track progress quarterly

External Disclosure:
- CDP Climate questionnaire
- TCFD disclosure
- Annual ESG report
- SEC 10-K (if applicable)
- CSRD (if EU)

Continuous Improvement:
- Expand Scope 3 measurement (remaining categories)
- Improve data quality (primary data vs estimates)
- Engage suppliers for direct data
- Update emission factors annually
```

## Variables

### COMPANY_NAME, INDUSTRY, OPERATIONS
**Examples:**
- "TechManufacturing Inc., automotive parts, 10 facilities"
- "Global Software Corp, SaaS, cloud-based operations"
- "Regional Retailer, 500 stores + warehouses"

### ORGANIZATIONAL_BOUNDARY
**Examples:**
- "All wholly-owned subsidiaries (operational control approach)"
- "All entities where >50% ownership (financial control)"
- "Global operations except recent acquisition (to add next year)"

### REPORTING_YEAR
**Examples:**
- "Calendar year 2024 (January 1 - December 31, 2024)"
- "Fiscal year 2024 (July 1, 2023 - June 30, 2024)"

## Usage Examples

### Example 1: Manufacturing Company
```
Company: Automotive parts (8,000 employees, 12 facilities)
Total: 98,000 tCO2e
- Scope 1: 35,000 (36%): Natural gas 22K, fleet 8K, refrigerants 5K
- Scope 2: 15,000 (15%): Electricity 75,000 MWh, 40% renewable
- Scope 3: 48,000 (49%): Cat 1 (materials) 60%, Cat 4 (logistics) 25%, Other 15%
Intensity: 196 tCO2e/$M revenue
Focus: Scope 1 gas boilers, Scope 2 renewable energy, Scope 3 supplier engagement
```

### Example 2: Technology Company
```
Company: SaaS (3,500 employees, cloud-based)
Total: 52,000 tCO2e
- Scope 1: 450 (1%): Company vehicles only
- Scope 2: 550 (1%): Offices (85% renewable)
- Scope 3: 51,000 (98%): Cat 1 (cloud AWS/Azure) 80%, Cat 6 (travel) 10%, Cat 7 (commute) 5%, Other 5%
Intensity: 65 tCO2e/$M ARR
Focus: Scope 3 cloud providers (partnering for decarbonization), reduce travel
```

### Example 3: Retail Company
```
Company: Omnichannel (600 stores, 18,000 employees)
Total: 550,000 tCO2e
- Scope 1: 35,000 (6%): Delivery fleet, store HVAC
- Scope 2: 45,000 (8%): Store electricity, 25% renewable
- Scope 3: 470,000 (86%): Cat 1 (products sold) 90%, Cat 4 (logistics) 6%, Other 4%
Intensity: 138 tCO2e/$M revenue
Focus: Product sourcing (supplier engagement), store renewables, electric delivery fleet
```

## Best Practices

1. **GHG Protocol compliance** - Follow standards exactly
2. **Comprehensive Scope 3** - Measure all material categories (>5%)
3. **Primary data preferred** - Metered over estimated
4. **Document methodology** - Transparent assumptions
5. **Annual updates** - Refresh emission factors, improve data quality

## Common Pitfalls

❌ **Ignoring Scope 3** - Only measuring Scope 1&2
✅ Instead: Comprehensive value chain (Scope 3 often 80%+)

❌ **Poor data quality** - All estimates, no primary data
✅ Instead: Metered data for Scope 1&2, work toward Scope 3 primary data

❌ **Inconsistent boundaries** - Changing what's included year-to-year
✅ Instead: Consistent boundaries, document changes

❌ **Wrong emission factors** - Outdated or incorrect factors
✅ Instead: Latest EPA, IEA, DEFRA factors; update annually

❌ **No documentation** - Can't recreate calculations
✅ Instead: Detailed methodology, assumptions, data sources

## Carbon Accounting Checklist

- [ ] Organizational boundary defined
- [ ] Scope 1 data collected (fuel, refrigerants)
- [ ] Scope 2 data collected (electricity, location & market-based)
- [ ] Scope 3 categories assessed (materiality screening)
- [ ] Scope 3 data collected (prioritize material categories)
- [ ] Latest emission factors applied
- [ ] Calculations documented
- [ ] Intensity metrics calculated
- [ ] Data quality assessed
- [ ] Methodology documented
- [ ] External assurance (if applicable)
- [ ] Baseline approved for target setting

---

**Last Updated:** 2025-11-12
**Category:** Sustainability > Climate & Environment
**Difficulty:** Intermediate to Advanced
**Estimated Time:** 6-10 weeks for comprehensive first-time inventory including Scope 3
