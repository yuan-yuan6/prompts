---
title: Real Estate Market Analysis & Investment Evaluation Framework
category: sales-marketing
tags:
- ai-ml
- framework
- research
- strategy
use_cases:
- Creating comprehensive framework for analyzing real estate markets, evaluating investment
  opportunities, conducting comparable analysis, and making data-driven property investment
  decisions.
- Project planning and execution
- Strategy development
related_templates:
- sales-marketing/Real-Estate/property-management-system.md
- sales-marketing/Real-Estate/construction-project-planning.md
last_updated: 2025-11-09
industries:
- finance
- healthcare
- retail
type: template
difficulty: intermediate
slug: real-estate-market-analysis
---

# Real Estate Market Analysis & Investment Evaluation Framework

## Purpose
Comprehensive framework for analyzing real estate markets, evaluating investment opportunities, conducting comparable analysis, and making data-driven property investment decisions.

## Quick Real Estate Market Analysis Prompt
Analyze real estate investment for [PROPERTY_TYPE] with [UNIT_COUNT] units in [MARKET_LOCATION] at [PURCHASE_PRICE] purchase price. Assess market: demographics, employment, supply/demand, rent trends. Current metrics: [OCCUPANCY]% occupied, [CURRENT_RENT] average rent, [PROJECTED_NOI] NOI. Model [INVESTMENT_STRATEGY] (core/value-add/opportunistic) with [HOLD_PERIOD] year hold. Calculate [IRR_TARGET]% target IRR. Identify [COMPARABLE_COUNT] comparable sales. Assess risks and exit strategies. Deliver investment recommendation with financial projections.

## Quick Start

**Need to analyze a real estate investment quickly?** Use this minimal example:

### Minimal Example
```
Analyze investment opportunity for a 12-unit apartment building in Austin, Texas, with $2.4M purchase price. Target: 15% IRR over 5-year hold period with value-add renovation strategy. Current metrics: 85% occupied, $1,200/unit average rent, $180K projected NOI. Need market analysis, comparable sales, financial projections, and risk assessment.
```

### When to Use This
- Evaluating property acquisition opportunities
- Conducting due diligence on real estate investments
- Analyzing market conditions and trends
- Comparing properties and determining fair market value
- Assessing investment returns and exit strategies

### Basic 3-Step Workflow
1. **Market research** - Analyze local market trends, demographics, supply/demand, comparables
2. **Financial analysis** - Model cash flows, calculate returns (IRR, cash-on-cash), assess risks
3. **Investment decision** - Reconcile valuations, evaluate exit options, make go/no-go recommendation

**Time to complete**: 3-5 days for initial analysis, 2-3 weeks for comprehensive evaluation

---

## Template

Analyze real estate opportunity for [PROPERTY_TYPE] in [LOCATION] with investment size of $[INVESTMENT_AMOUNT], targeting [TARGET_RETURN]% IRR over [HOLD_PERIOD] years with [EXIT_STRATEGY] exit strategy.

### 1. Market Overview & Trends

| **Market Indicator** | **Current Value** | **1-Year Change** | **3-Year CAGR** | **Market Rank** | **Forecast** |
|--------------------|------------------|------------------|-----------------|-----------------|-------------|
| Median Home Price | $[MEDIAN_PRICE] | [PRICE_1Y]% | [PRICE_3Y]% | [PRICE_RANK] | [PRICE_FORECAST] |
| Price per Sq Ft | $[PRICE_SQFT] | [SQFT_1Y]% | [SQFT_3Y]% | [SQFT_RANK] | [SQFT_FORECAST] |
| Inventory Levels | [INVENTORY] months | [INV_1Y]% | [INV_3Y]% | [INV_RANK] | [INV_FORECAST] |
| Days on Market | [DOM] days | [DOM_1Y]% | [DOM_3Y]% | [DOM_RANK] | [DOM_FORECAST] |
| Sales Volume | [SALES_VOL] units | [SALES_1Y]% | [SALES_3Y]% | [SALES_RANK] | [SALES_FORECAST] |
| Rental Rates | $[RENT_RATE]/mo | [RENT_1Y]% | [RENT_3Y]% | [RENT_RANK] | [RENT_FORECAST] |

### 2. Comparable Property Analysis

**Recent Comparable Sales:**
```
Comp 1: [COMP1_ADDRESS]
- Sale Date: [COMP1_DATE]
- Sale Price: $[COMP1_PRICE]
- Size: [COMP1_SIZE] sq ft
- Price/SF: $[COMP1_PSF]
- Condition: [COMP1_CONDITION]
- Adjustments: [COMP1_ADJUST]

Comp 2: [COMP2_ADDRESS]
- Sale Date: [COMP2_DATE]
- Sale Price: $[COMP2_PRICE]
- Size: [COMP2_SIZE] sq ft
- Price/SF: $[COMP2_PSF]
- Condition: [COMP2_CONDITION]
- Adjustments: [COMP2_ADJUST]

Comp 3: [COMP3_ADDRESS]
- Sale Date: [COMP3_DATE]
- Sale Price: $[COMP3_PRICE]
- Size: [COMP3_SIZE] sq ft
- Price/SF: $[COMP3_PSF]
- Condition: [COMP3_CONDITION]
- Adjustments: [COMP3_ADJUST]

Adjusted Value Range: $[VALUE_LOW] - $[VALUE_HIGH]
Recommended Value: $[RECOMMENDED_VALUE]
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[PROPERTY_TYPE]` | Type or category of property | "Standard" |
| `[LOCATION]` | Specify the location | "North America" |
| `[INVESTMENT_AMOUNT]` | Specify the investment amount | "[specify value]" |
| `[TARGET_RETURN]` | Target or intended return | "[specify value]" |
| `[HOLD_PERIOD]` | Specify the hold period | "[specify value]" |
| `[EXIT_STRATEGY]` | Strategy or approach for exit | "[specify value]" |
| `[MEDIAN_PRICE]` | Specify the median price | "[specify value]" |
| `[PRICE_1Y]` | Specify the price 1y | "[specify value]" |
| `[PRICE_3Y]` | Specify the price 3y | "[specify value]" |
| `[PRICE_RANK]` | Specify the price rank | "[specify value]" |
| `[PRICE_FORECAST]` | Specify the price forecast | "[specify value]" |
| `[PRICE_SQFT]` | Specify the price sqft | "[specify value]" |
| `[SQFT_1Y]` | Specify the sqft 1y | "[specify value]" |
| `[SQFT_3Y]` | Specify the sqft 3y | "[specify value]" |
| `[SQFT_RANK]` | Specify the sqft rank | "[specify value]" |
| `[SQFT_FORECAST]` | Specify the sqft forecast | "[specify value]" |
| `[INVENTORY]` | Specify the inventory | "[specify value]" |
| `[INV_1Y]` | Specify the inv 1y | "[specify value]" |
| `[INV_3Y]` | Specify the inv 3y | "[specify value]" |
| `[INV_RANK]` | Specify the inv rank | "[specify value]" |
| `[INV_FORECAST]` | Specify the inv forecast | "[specify value]" |
| `[DOM]` | Specify the dom | "[specify value]" |
| `[DOM_1Y]` | Specify the dom 1y | "[specify value]" |
| `[DOM_3Y]` | Specify the dom 3y | "[specify value]" |
| `[DOM_RANK]` | Specify the dom rank | "[specify value]" |
| `[DOM_FORECAST]` | Specify the dom forecast | "[specify value]" |
| `[SALES_VOL]` | Specify the sales vol | "[specify value]" |
| `[SALES_1Y]` | Specify the sales 1y | "[specify value]" |
| `[SALES_3Y]` | Specify the sales 3y | "[specify value]" |
| `[SALES_RANK]` | Specify the sales rank | "[specify value]" |
| `[SALES_FORECAST]` | Specify the sales forecast | "[specify value]" |
| `[RENT_RATE]` | Specify the rent rate | "[specify value]" |
| `[RENT_1Y]` | Specify the rent 1y | "[specify value]" |
| `[RENT_3Y]` | Specify the rent 3y | "[specify value]" |
| `[RENT_RANK]` | Specify the rent rank | "[specify value]" |
| `[RENT_FORECAST]` | Specify the rent forecast | "[specify value]" |
| `[COMP1_ADDRESS]` | Specify the comp1 address | "[specify value]" |
| `[COMP1_DATE]` | Specify the comp1 date | "2025-01-15" |
| `[COMP1_PRICE]` | Specify the comp1 price | "[specify value]" |
| `[COMP1_SIZE]` | Specify the comp1 size | "[specify value]" |
| `[COMP1_PSF]` | Specify the comp1 psf | "[specify value]" |
| `[COMP1_CONDITION]` | Specify the comp1 condition | "[specify value]" |
| `[COMP1_ADJUST]` | Specify the comp1 adjust | "[specify value]" |
| `[COMP2_ADDRESS]` | Specify the comp2 address | "[specify value]" |
| `[COMP2_DATE]` | Specify the comp2 date | "2025-01-15" |
| `[COMP2_PRICE]` | Specify the comp2 price | "[specify value]" |
| `[COMP2_SIZE]` | Specify the comp2 size | "[specify value]" |
| `[COMP2_PSF]` | Specify the comp2 psf | "[specify value]" |
| `[COMP2_CONDITION]` | Specify the comp2 condition | "[specify value]" |
| `[COMP2_ADJUST]` | Specify the comp2 adjust | "[specify value]" |
| `[COMP3_ADDRESS]` | Specify the comp3 address | "[specify value]" |
| `[COMP3_DATE]` | Specify the comp3 date | "2025-01-15" |
| `[COMP3_PRICE]` | Specify the comp3 price | "[specify value]" |
| `[COMP3_SIZE]` | Specify the comp3 size | "[specify value]" |
| `[COMP3_PSF]` | Specify the comp3 psf | "[specify value]" |
| `[COMP3_CONDITION]` | Specify the comp3 condition | "[specify value]" |
| `[COMP3_ADJUST]` | Specify the comp3 adjust | "[specify value]" |
| `[VALUE_LOW]` | Specify the value low | "[specify value]" |
| `[VALUE_HIGH]` | Specify the value high | "[specify value]" |
| `[RECOMMENDED_VALUE]` | Specify the recommended value | "[specify value]" |
| `[RENT_Y1]` | Specify the rent y1 | "[specify value]" |
| `[RENT_Y3]` | Specify the rent y3 | "[specify value]" |
| `[RENT_Y5]` | Specify the rent y5 | "[specify value]" |
| `[RENT_EXIT]` | Specify the rent exit | "[specify value]" |
| `[RENT_AVG]` | Specify the rent avg | "[specify value]" |
| `[OPEX_Y1]` | Specify the opex y1 | "[specify value]" |
| `[OPEX_Y3]` | Specify the opex y3 | "[specify value]" |
| `[OPEX_Y5]` | Specify the opex y5 | "[specify value]" |
| `[OPEX_EXIT]` | Specify the opex exit | "[specify value]" |
| `[OPEX_AVG]` | Specify the opex avg | "[specify value]" |
| `[NOI_Y1]` | Specify the noi y1 | "[specify value]" |
| `[NOI_Y3]` | Specify the noi y3 | "[specify value]" |
| `[NOI_Y5]` | Specify the noi y5 | "[specify value]" |
| `[NOI_EXIT]` | Specify the noi exit | "[specify value]" |
| `[NOI_AVG]` | Specify the noi avg | "[specify value]" |
| `[DEBT_Y1]` | Specify the debt y1 | "[specify value]" |
| `[DEBT_Y3]` | Specify the debt y3 | "[specify value]" |
| `[DEBT_Y5]` | Specify the debt y5 | "[specify value]" |
| `[DEBT_EXIT]` | Specify the debt exit | "[specify value]" |
| `[DEBT_AVG]` | Specify the debt avg | "[specify value]" |
| `[CF_Y1]` | Specify the cf y1 | "[specify value]" |
| `[CF_Y3]` | Specify the cf y3 | "[specify value]" |
| `[CF_Y5]` | Specify the cf y5 | "[specify value]" |
| `[CF_EXIT]` | Specify the cf exit | "[specify value]" |
| `[CF_AVG]` | Specify the cf avg | "[specify value]" |
| `[COC_Y1]` | Specify the coc y1 | "[specify value]" |
| `[COC_Y3]` | Specify the coc y3 | "[specify value]" |
| `[COC_Y5]` | Specify the coc y5 | "[specify value]" |
| `[COC_EXIT]` | Specify the coc exit | "[specify value]" |
| `[COC_AVG]` | Specify the coc avg | "[specify value]" |
| `[SUBJ_POP]` | Specify the subj pop | "[specify value]" |
| `[CITY_POP]` | Specify the city pop | "[specify value]" |
| `[POP_GROWTH]` | Specify the pop growth | "[specify value]" |
| `[SUBJ_INCOME]` | Specify the subj income | "[specify value]" |
| `[CITY_INCOME]` | Specify the city income | "[specify value]" |
| `[INCOME_GROWTH]` | Specify the income growth | "[specify value]" |
| `[SUBJ_EMPLOY]` | Specify the subj employ | "[specify value]" |
| `[CITY_EMPLOY]` | Specify the city employ | "[specify value]" |
| `[EMPLOY_GROWTH]` | Specify the employ growth | "[specify value]" |
| `[SUBJ_OWNER]` | Specify the subj owner | "[specify value]" |
| `[CITY_OWNER]` | Specify the city owner | "[specify value]" |
| `[OWNER_TREND]` | Specify the owner trend | "[specify value]" |
| `[SUBJ_SCHOOL]` | Specify the subj school | "[specify value]" |
| `[CITY_SCHOOL]` | Specify the city school | "[specify value]" |
| `[SCHOOL_TREND]` | Specify the school trend | "[specify value]" |
| `[SUBJ_CRIME]` | Specify the subj crime | "[specify value]" |
| `[CITY_CRIME]` | Specify the city crime | "[specify value]" |
| `[CRIME_TREND]` | Specify the crime trend | "[specify value]" |
| `[ACTIVE_LISTINGS]` | Specify the active listings | "[specify value]" |
| `[NEW_CONST]` | Specify the new const | "[specify value]" |
| `[PIPELINE]` | Specify the pipeline | "[specify value]" |
| `[VACANCY]` | Specify the vacancy | "[specify value]" |
| `[ABSORPTION]` | Specify the absorption | "[specify value]" |
| `[POP_DRIVER]` | Specify the pop driver | "[specify value]" |
| `[JOB_DRIVER]` | Specify the job driver | "[specify value]" |
| `[INCOME_DRIVER]` | Specify the income driver | "[specify value]" |
| `[MIGRATION_PATTERN]` | Specify the migration pattern | "[specify value]" |
| `[HOUSEHOLD_FORM]` | Specify the household form | "[specify value]" |
| `[SUPPLY_DEMAND_BAL]` | Specify the supply demand bal | "[specify value]" |
| `[SD_1YEAR]` | Specify the sd 1year | "[specify value]" |
| `[SD_3YEAR]` | Specify the sd 3year | "[specify value]" |
| `[EQUILIBRIUM]` | Specify the equilibrium | "[specify value]" |
| `[PRICE_PRESSURE]` | Specify the price pressure | "[specify value]" |
| `[SALES_COMP_VAL]` | Specify the sales comp val | "[specify value]" |
| `[SC_WEIGHT]` | Specify the sc weight | "[specify value]" |
| `[SC_WEIGHTED]` | Specify the sc weighted | "[specify value]" |
| `[SC_CONF]` | Specify the sc conf | "[specify value]" |
| `[SC_NOTES]` | Specify the sc notes | "[specify value]" |
| `[INCOME_VAL]` | Specify the income val | "[specify value]" |
| `[INC_WEIGHT]` | Specify the inc weight | "[specify value]" |
| `[INC_WEIGHTED]` | Specify the inc weighted | "[specify value]" |
| `[INC_CONF]` | Specify the inc conf | "[specify value]" |
| `[INC_NOTES]` | Specify the inc notes | "[specify value]" |
| `[COST_VAL]` | Specify the cost val | "[specify value]" |
| `[COST_WEIGHT]` | Specify the cost weight | "[specify value]" |
| `[COST_WEIGHTED]` | Specify the cost weighted | "[specify value]" |
| `[COST_CONF]` | Specify the cost conf | "[specify value]" |
| `[COST_NOTES]` | Specify the cost notes | "[specify value]" |
| `[DCF_VAL]` | Specify the dcf val | "[specify value]" |
| `[DCF_WEIGHT]` | Specify the dcf weight | "[specify value]" |
| `[DCF_WEIGHTED]` | Specify the dcf weighted | "[specify value]" |
| `[DCF_CONF]` | Specify the dcf conf | "[specify value]" |
| `[DCF_NOTES]` | Specify the dcf notes | "[specify value]" |
| `[FINAL_VALUE]` | Specify the final value | "[specify value]" |
| `[FINAL_CONF]` | Specify the final conf | "[specify value]" |
| `[FINAL_NOTES]` | Specify the final notes | "[specify value]" |
| `[MKT_PROB]` | Specify the mkt prob | "[specify value]" |
| `[MKT_IMPACT]` | Specify the mkt impact | "[specify value]" |
| `[MKT_SCORE]` | Specify the mkt score | "[specify value]" |
| `[MKT_MITIGATE]` | Specify the mkt mitigate | "[specify value]" |
| `[MKT_CONTINGENCY]` | Specify the mkt contingency | "[specify value]" |
| `[PROP_PROB]` | Specify the prop prob | "[specify value]" |
| `[PROP_IMPACT]` | Specify the prop impact | "[specify value]" |
| `[PROP_SCORE]` | Specify the prop score | "[specify value]" |
| `[PROP_MITIGATE]` | Specify the prop mitigate | "[specify value]" |
| `[PROP_CONTINGENCY]` | Specify the prop contingency | "[specify value]" |
| `[FIN_PROB]` | Specify the fin prob | "[specify value]" |
| `[FIN_IMPACT]` | Specify the fin impact | "[specify value]" |
| `[FIN_SCORE]` | Specify the fin score | "[specify value]" |
| `[FIN_MITIGATE]` | Specify the fin mitigate | "[specify value]" |
| `[FIN_CONTINGENCY]` | Specify the fin contingency | "[specify value]" |
| `[REG_PROB]` | Specify the reg prob | "[specify value]" |
| `[REG_IMPACT]` | Specify the reg impact | "[specify value]" |
| `[REG_SCORE]` | Specify the reg score | "[specify value]" |
| `[REG_MITIGATE]` | Specify the reg mitigate | "[specify value]" |
| `[REG_CONTINGENCY]` | Specify the reg contingency | "[specify value]" |
| `[ENV_PROB]` | Specify the env prob | "[specify value]" |
| `[ENV_IMPACT]` | Specify the env impact | "[specify value]" |
| `[ENV_SCORE]` | Specify the env score | "[specify value]" |
| `[ENV_MITIGATE]` | Specify the env mitigate | "[specify value]" |
| `[ENV_CONTINGENCY]` | Specify the env contingency | "[specify value]" |
| `[PURCHASE_PRICE]` | Specify the purchase price | "[specify value]" |
| `[CLOSING_COSTS]` | Specify the closing costs | "[specify value]" |
| `[RENOVATION]` | Specify the renovation | "[specify value]" |
| `[RESERVES]` | Specify the reserves | "[specify value]" |
| `[TOTAL_INVESTMENT]` | Specify the total investment | "[specify value]" |
| `[SENIOR_DEBT]` | Specify the senior debt | "[specify value]" |
| `[SENIOR_LTV]` | Specify the senior ltv | "[specify value]" |
| `[SENIOR_RATE]` | Specify the senior rate | "[specify value]" |
| `[SENIOR_TERM]` | Specify the senior term | "[specify value]" |
| `[SENIOR_AMORT]` | Specify the senior amort | "[specify value]" |
| `[MEZZ_DEBT]` | Specify the mezz debt | "[specify value]" |
| `[MEZZ_LTV]` | Specify the mezz ltv | "[specify value]" |
| `[MEZZ_RATE]` | Specify the mezz rate | "[specify value]" |
| `[MEZZ_TERM]` | Specify the mezz term | "[specify value]" |
| `[EQUITY]` | Specify the equity | "[specify value]" |
| `[EQUITY_PCT]` | Specify the equity pct | "25%" |
| `[EQUITY_RETURN]` | Specify the equity return | "[specify value]" |
| `[PREF_RETURN]` | Specify the pref return | "[specify value]" |
| `[PROFIT_SPLIT]` | Specify the profit split | "[specify value]" |
| `[SALE_TIME]` | Specify the sale time | "[specify value]" |
| `[SALE_VALUE]` | Specify the sale value | "[specify value]" |
| `[SALE_NET]` | Specify the sale net | "[specify value]" |
| `[SALE_IRR]` | Specify the sale irr | "[specify value]" |
| `[SALE_MULT]` | Specify the sale mult | "[specify value]" |
| `[SALE_PROB]` | Specify the sale prob | "[specify value]" |
| `[INV_TIME]` | Specify the inv time | "[specify value]" |
| `[INV_VALUE]` | Specify the inv value | "[specify value]" |
| `[INV_NET]` | Specify the inv net | "[specify value]" |
| `[INV_IRR]` | Specify the inv irr | "[specify value]" |
| `[INV_MULT]` | Specify the inv mult | "[specify value]" |
| `[INV_PROB]` | Specify the inv prob | "[specify value]" |
| `[REFI_TIME]` | Specify the refi time | "[specify value]" |
| `[REFI_VALUE]` | Specify the refi value | "[specify value]" |
| `[REFI_NET]` | Specify the refi net | "[specify value]" |
| `[REFI_IRR]` | Specify the refi irr | "[specify value]" |
| `[REFI_MULT]` | Specify the refi mult | "[specify value]" |
| `[REFI_PROB]` | Specify the refi prob | "[specify value]" |
| `[DEV_TIME]` | Specify the dev time | "[specify value]" |
| `[DEV_VALUE]` | Specify the dev value | "[specify value]" |
| `[DEV_NET]` | Specify the dev net | "[specify value]" |
| `[DEV_IRR]` | Specify the dev irr | "[specify value]" |
| `[DEV_MULT]` | Specify the dev mult | "[specify value]" |
| `[DEV_PROB]` | Specify the dev prob | "[specify value]" |
| `[PORT_TIME]` | Specify the port time | "[specify value]" |
| `[PORT_VALUE]` | Specify the port value | "[specify value]" |
| `[PORT_NET]` | Specify the port net | "[specify value]" |
| `[PORT_IRR]` | Specify the port irr | "[specify value]" |
| `[PORT_MULT]` | Specify the port mult | "[specify value]" |
| `[PORT_PROB]` | Specify the port prob | "[specify value]" |
| `[RETURN_SCORE]` | Specify the return score | "[specify value]" |
| `[RETURN_WT]` | Specify the return wt | "[specify value]" |
| `[RETURN_WEIGHTED]` | Specify the return weighted | "[specify value]" |
| `[RETURN_BENCH]` | Specify the return bench | "[specify value]" |
| `[RETURN_DEC]` | Specify the return dec | "[specify value]" |
| `[RISK_SCORE]` | Specify the risk score | "[specify value]" |
| `[RISK_WT]` | Specify the risk wt | "[specify value]" |
| `[RISK_WEIGHTED]` | Specify the risk weighted | "[specify value]" |
| `[RISK_BENCH]` | Specify the risk bench | "[specify value]" |
| `[RISK_DEC]` | Specify the risk dec | "[specify value]" |
| `[TIMING_SCORE]` | Specify the timing score | "[specify value]" |
| `[TIMING_WT]` | Specify the timing wt | "[specify value]" |
| `[TIMING_WEIGHTED]` | Specify the timing weighted | "[specify value]" |
| `[TIMING_BENCH]` | Specify the timing bench | "[specify value]" |
| `[TIMING_DEC]` | Specify the timing dec | "[specify value]" |
| `[LOC_SCORE]` | Specify the loc score | "[specify value]" |
| `[LOC_WT]` | Specify the loc wt | "[specify value]" |
| `[LOC_WEIGHTED]` | Specify the loc weighted | "[specify value]" |
| `[LOC_BENCH]` | Specify the loc bench | "[specify value]" |
| `[LOC_DEC]` | Specify the loc dec | "[specify value]" |
| `[EXIT_SCORE]` | Specify the exit score | "[specify value]" |
| `[EXIT_WT]` | Specify the exit wt | "[specify value]" |
| `[EXIT_WEIGHTED]` | Specify the exit weighted | "[specify value]" |
| `[EXIT_BENCH]` | Specify the exit bench | "[specify value]" |
| `[EXIT_DEC]` | Specify the exit dec | "[specify value]" |
| `[TOTAL_SCORE]` | Specify the total score | "[specify value]" |
| `[TOTAL_WEIGHTED]` | Specify the total weighted | "[specify value]" |
| `[TOTAL_BENCH]` | Specify the total bench | "[specify value]" |
| `[FINAL_DECISION]` | Specify the final decision | "[specify value]" |

### 3. Investment Financial Analysis

| **Financial Metric** | **Year 1** | **Year 3** | **Year 5** | **Exit Year** | **Average** |
|--------------------|-----------|-----------|-----------|-------------|-----------|
| Gross Rental Income | $[RENT_Y1] | $[RENT_Y3] | $[RENT_Y5] | $[RENT_EXIT] | $[RENT_AVG] |
| Operating Expenses | $[OPEX_Y1] | $[OPEX_Y3] | $[OPEX_Y5] | $[OPEX_EXIT] | $[OPEX_AVG] |
| Net Operating Income | $[NOI_Y1] | $[NOI_Y3] | $[NOI_Y5] | $[NOI_EXIT] | $[NOI_AVG] |
| Debt Service | $[DEBT_Y1] | $[DEBT_Y3] | $[DEBT_Y5] | $[DEBT_EXIT] | $[DEBT_AVG] |
| Cash Flow | $[CF_Y1] | $[CF_Y3] | $[CF_Y5] | $[CF_EXIT] | $[CF_AVG] |
| Cash-on-Cash Return | [COC_Y1]% | [COC_Y3]% | [COC_Y5]% | [COC_EXIT]% | [COC_AVG]% |

### 4. Location & Demographic Analysis

**Area Demographics:**
| **Factor** | **Subject Property** | **1-Mile Radius** | **3-Mile Radius** | **City Average** | **Growth Rate** |
|-----------|---------------------|------------------|------------------|-----------------|----------------|
| Population | [SUBJ_POP] | [1MI_POP] | [3MI_POP] | [CITY_POP] | [POP_GROWTH]% |
| Median Income | $[SUBJ_INCOME] | $[1MI_INCOME] | $[3MI_INCOME] | $[CITY_INCOME] | [INCOME_GROWTH]% |
| Employment Rate | [SUBJ_EMPLOY]% | [1MI_EMPLOY]% | [3MI_EMPLOY]% | [CITY_EMPLOY]% | [EMPLOY_GROWTH]% |
| Owner Occupied | [SUBJ_OWNER]% | [1MI_OWNER]% | [3MI_OWNER]% | [CITY_OWNER]% | [OWNER_TREND] |
| School Rating | [SUBJ_SCHOOL]/10 | [1MI_SCHOOL]/10 | [3MI_SCHOOL]/10 | [CITY_SCHOOL]/10 | [SCHOOL_TREND] |
| Crime Index | [SUBJ_CRIME] | [1MI_CRIME] | [3MI_CRIME] | [CITY_CRIME] | [CRIME_TREND] |

### 5. Supply & Demand Dynamics

**Market Supply Analysis:**
```
Current Supply:
- Active Listings: [ACTIVE_LISTINGS]
- New Construction: [NEW_CONST] units
- Pipeline Projects: [PIPELINE] units
- Vacancy Rate: [VACANCY]%
- Absorption Rate: [ABSORPTION] units/month

Demand Drivers:
- Population Growth: [POP_DRIVER]% annually
- Job Growth: [JOB_DRIVER] jobs/year
- Income Growth: [INCOME_DRIVER]% annually
- Migration Pattern: [MIGRATION_PATTERN]
- Household Formation: [HOUSEHOLD_FORM] units/year

Supply-Demand Balance:
- Current Balance: [SUPPLY_DEMAND_BAL]
- Projected 1-Year: [SD_1YEAR]
- Projected 3-Year: [SD_3YEAR]
- Market Equilibrium: [EQUILIBRIUM]
- Price Pressure: [PRICE_PRESSURE]
```

### 6. Property Valuation Methods

| **Valuation Method** | **Calculated Value** | **Weight** | **Weighted Value** | **Confidence** | **Notes** |
|--------------------|---------------------|-----------|-------------------|---------------|----------|
| Sales Comparison | $[SALES_COMP_VAL] | [SC_WEIGHT]% | $[SC_WEIGHTED] | [SC_CONF]% | [SC_NOTES] |
| Income Approach | $[INCOME_VAL] | [INC_WEIGHT]% | $[INC_WEIGHTED] | [INC_CONF]% | [INC_NOTES] |
| Cost Approach | $[COST_VAL] | [COST_WEIGHT]% | $[COST_WEIGHTED] | [COST_CONF]% | [COST_NOTES] |
| DCF Analysis | $[DCF_VAL] | [DCF_WEIGHT]% | $[DCF_WEIGHTED] | [DCF_CONF]% | [DCF_NOTES] |
| **Final Value** | **$[FINAL_VALUE]** | **100%** | **$[FINAL_VALUE]** | **[FINAL_CONF]%** | **[FINAL_NOTES]** |

### 7. Risk Assessment

**Risk Matrix:**
| **Risk Category** | **Probability** | **Impact** | **Risk Score** | **Mitigation Strategy** | **Contingency Plan** |
|------------------|---------------|-----------|---------------|----------------------|-------------------|
| Market Risk | [MKT_PROB]% | [MKT_IMPACT] | [MKT_SCORE] | [MKT_MITIGATE] | [MKT_CONTINGENCY] |
| Property Risk | [PROP_PROB]% | [PROP_IMPACT] | [PROP_SCORE] | [PROP_MITIGATE] | [PROP_CONTINGENCY] |
| Financial Risk | [FIN_PROB]% | [FIN_IMPACT] | [FIN_SCORE] | [FIN_MITIGATE] | [FIN_CONTINGENCY] |
| Regulatory Risk | [REG_PROB]% | [REG_IMPACT] | [REG_SCORE] | [REG_MITIGATE] | [REG_CONTINGENCY] |
| Environmental Risk | [ENV_PROB]% | [ENV_IMPACT] | [ENV_SCORE] | [ENV_MITIGATE] | [ENV_CONTINGENCY] |

### 8. Financing Structure

**Capital Stack:**
```
Acquisition Costs:
- Purchase Price: $[PURCHASE_PRICE]
- Closing Costs: $[CLOSING_COSTS]
- Renovation Budget: $[RENOVATION]
- Reserve Fund: $[RESERVES]
Total Investment: $[TOTAL_INVESTMENT]

Financing Structure:
- Senior Debt: $[SENIOR_DEBT] ([SENIOR_LTV]% LTV)
  Interest Rate: [SENIOR_RATE]%
  Term: [SENIOR_TERM] years
  Amortization: [SENIOR_AMORT] years

- Mezzanine Debt: $[MEZZ_DEBT] ([MEZZ_LTV]% LTV)
  Interest Rate: [MEZZ_RATE]%
  Term: [MEZZ_TERM] years

- Equity: $[EQUITY] ([EQUITY_PCT]%)
  Target Return: [EQUITY_RETURN]%
  Preferred Return: [PREF_RETURN]%
  Profit Split: [PROFIT_SPLIT]
```

### 9. Exit Strategy Analysis

| **Exit Option** | **Timeline** | **Projected Value** | **Net Proceeds** | **IRR** | **Multiple** | **Probability** |
|----------------|-------------|-------------------|-----------------|---------|-------------|---------------|
| Sale to End User | [SALE_TIME] | $[SALE_VALUE] | $[SALE_NET] | [SALE_IRR]% | [SALE_MULT]x | [SALE_PROB]% |
| Investor Sale | [INV_TIME] | $[INV_VALUE] | $[INV_NET] | [INV_IRR]% | [INV_MULT]x | [INV_PROB]% |
| Refinance & Hold | [REFI_TIME] | $[REFI_VALUE] | $[REFI_NET] | [REFI_IRR]% | [REFI_MULT]x | [REFI_PROB]% |
| Development | [DEV_TIME] | $[DEV_VALUE] | $[DEV_NET] | [DEV_IRR]% | [DEV_MULT]x | [DEV_PROB]% |
| Portfolio Sale | [PORT_TIME] | $[PORT_VALUE] | $[PORT_NET] | [PORT_IRR]% | [PORT_MULT]x | [PORT_PROB]% |

### 10. Investment Decision Matrix

**Decision Criteria:**
| **Factor** | **Score (1-10)** | **Weight** | **Weighted Score** | **Benchmark** | **Decision** |
|-----------|-----------------|-----------|-------------------|--------------|------------|
| Return Potential | [RETURN_SCORE] | [RETURN_WT]% | [RETURN_WEIGHTED] | [RETURN_BENCH] | [RETURN_DEC] |
| Risk Level | [RISK_SCORE] | [RISK_WT]% | [RISK_WEIGHTED] | [RISK_BENCH] | [RISK_DEC] |
| Market Timing | [TIMING_SCORE] | [TIMING_WT]% | [TIMING_WEIGHTED] | [TIMING_BENCH] | [TIMING_DEC] |
| Location Quality | [LOC_SCORE] | [LOC_WT]% | [LOC_WEIGHTED] | [LOC_BENCH] | [LOC_DEC] |
| Exit Flexibility | [EXIT_SCORE] | [EXIT_WT]% | [EXIT_WEIGHTED] | [EXIT_BENCH] | [EXIT_DEC] |
| **Total Score** | **[TOTAL_SCORE]** | **100%** | **[TOTAL_WEIGHTED]** | **[TOTAL_BENCH]** | **[FINAL_DECISION]** |

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: Residential Investment
```
Property: 4-unit apartment building
Location: Growing metro suburb
Investment: $1.2M
Strategy: Buy, renovate, hold
Target IRR: 18%
Hold Period: 5 years
```

### Example 2: Commercial Office
```
Property: Class B office building
Location: Downtown business district
Investment: $25M
Strategy: Value-add repositioning
Target IRR: 15%
Hold Period: 7 years
```

### Example 3: Development Project
```
Property: Mixed-use development site
Location: Urban infill location
Investment: $50M
Strategy: Ground-up development
Target IRR: 25%
Timeline: 3-year development
```

## Customization Options

### 1. Property Type
- Residential (SFH, Multi-family)
- Commercial (Office, Retail)
- Industrial (Warehouse, Flex)
- Hospitality (Hotel, Resort)
- Special Purpose

### 2. Investment Strategy
- Core (stable, low risk)
- Core-Plus (minor value-add)
- Value-Add (renovation)
- Opportunistic (development)
- Distressed (turnaround)

### 3. Market Type
- Primary markets
- Secondary markets
- Tertiary markets
- Emerging markets
- International

### 4. Investor Type
- Individual investor
- Institutional
- REIT
- Private equity
- Family office

### 5. Analysis Focus
- Cash flow focused
- Appreciation focused
- Tax benefit focused
- Portfolio diversification
- 1031 exchange