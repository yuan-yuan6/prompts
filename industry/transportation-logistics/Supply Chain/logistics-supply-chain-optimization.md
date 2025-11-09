# Supply Chain Optimization & Network Design

## Purpose
Advanced framework for end-to-end supply chain optimization, network design, inventory management, demand planning, and logistics coordination across global supply networks.

## Template

Design and optimize supply chain network for [COMPANY_NAME] with [SKU_COUNT] SKUs, [SUPPLIER_COUNT] suppliers, [DC_COUNT] distribution centers, serving [CUSTOMER_COUNT] customers with annual volume of [VOLUME] units.

### 1. Supply Chain Network Mapping

**Network Nodes:**
| **Node Type** | **Location** | **Capacity** | **Throughput** | **Lead Time** | **Cost Structure** |
|--------------|-------------|-------------|---------------|--------------|------------------|
| Suppliers | [SUPP_LOC] | [SUPP_CAP] units | [SUPP_THROUGH] | [SUPP_LEAD] days | [SUPP_COST] |
| Manufacturing | [MFG_LOC] | [MFG_CAP] units | [MFG_THROUGH] | [MFG_LEAD] days | [MFG_COST] |
| Distribution Centers | [DC_LOC] | [DC_CAP] units | [DC_THROUGH] | [DC_LEAD] days | [DC_COST] |
| Cross-Docks | [CD_LOC] | [CD_CAP] units | [CD_THROUGH] | [CD_LEAD] hours | [CD_COST] |
| Retail/Customers | [RETAIL_LOC] | N/A | [RETAIL_THROUGH] | [RETAIL_LEAD] days | [RETAIL_COST] |

### 2. Demand Planning & Forecasting

**Forecasting Models:**
| **Product Category** | **Method** | **Accuracy (MAPE)** | **Bias** | **Forecast Horizon** | **Update Frequency** |
|--------------------|-----------|-------------------|---------|-------------------|-------------------|
| [CATEGORY_1] | [METHOD_1] | [MAPE_1]% | [BIAS_1]% | [HORIZON_1] | [FREQ_1] |
| [CATEGORY_2] | [METHOD_2] | [MAPE_2]% | [BIAS_2]% | [HORIZON_2] | [FREQ_2] |
| [CATEGORY_3] | [METHOD_3] | [MAPE_3]% | [BIAS_3]% | [HORIZON_3] | [FREQ_3] |
| [CATEGORY_4] | [METHOD_4] | [MAPE_4]% | [BIAS_4]% | [HORIZON_4] | [FREQ_4] |
| [CATEGORY_5] | [METHOD_5] | [MAPE_5]% | [BIAS_5]% | [HORIZON_5] | [FREQ_5] |

**Demand Variability Analysis:**
```
Seasonal Patterns:
- Peak Season: [PEAK_MONTHS] ([PEAK_MULT]x baseline)
- Low Season: [LOW_MONTHS] ([LOW_MULT]x baseline)
- Promotional Impact: [PROMO_LIFT]%
- Weather Correlation: [WEATHER_CORR]

Demand Segmentation:
- Base Demand: [BASE_PCT]%
- Promotional: [PROMO_PCT]%
- Seasonal: [SEASONAL_PCT]%
- Trend: [TREND_PCT]%
```

### 3. Inventory Optimization Strategy

| **Inventory Type** | **Value** | **Turns** | **Days on Hand** | **Service Level** | **Optimization Method** |
|-------------------|----------|----------|-----------------|------------------|----------------------|
| Raw Materials | $[RAW_VALUE] | [RAW_TURNS] | [RAW_DOH] | [RAW_SL]% | [RAW_METHOD] |
| Work in Process | $[WIP_VALUE] | [WIP_TURNS] | [WIP_DOH] | N/A | [WIP_METHOD] |
| Finished Goods | $[FG_VALUE] | [FG_TURNS] | [FG_DOH] | [FG_SL]% | [FG_METHOD] |
| MRO/Spare Parts | $[MRO_VALUE] | [MRO_TURNS] | [MRO_DOH] | [MRO_SL]% | [MRO_METHOD] |
| Safety Stock | $[SAFETY_VALUE] | N/A | [SAFETY_DOH] | [SAFETY_SL]% | [SAFETY_METHOD] |

### 4. Transportation & Logistics Management

**Modal Analysis:**
| **Transport Mode** | **Volume (%)** | **Cost/Unit** | **Transit Time** | **Reliability** | **Carbon Footprint** |
|-------------------|---------------|--------------|-----------------|----------------|-------------------|
| Ocean Freight | [OCEAN_VOL]% | $[OCEAN_COST] | [OCEAN_TIME] days | [OCEAN_REL]% | [OCEAN_CO2] kg/unit |
| Air Freight | [AIR_VOL]% | $[AIR_COST] | [AIR_TIME] days | [AIR_REL]% | [AIR_CO2] kg/unit |
| Rail | [RAIL_VOL]% | $[RAIL_COST] | [RAIL_TIME] days | [RAIL_REL]% | [RAIL_CO2] kg/unit |
| Truck (FTL) | [FTL_VOL]% | $[FTL_COST] | [FTL_TIME] days | [FTL_REL]% | [FTL_CO2] kg/unit |
| Truck (LTL) | [LTL_VOL]% | $[LTL_COST] | [LTL_TIME] days | [LTL_REL]% | [LTL_CO2] kg/unit |
| Parcel | [PARCEL_VOL]% | $[PARCEL_COST] | [PARCEL_TIME] days | [PARCEL_REL]% | [PARCEL_CO2] kg/unit |

### 5. Supplier Performance Management

| **Supplier Tier** | **Count** | **On-Time Delivery** | **Quality Score** | **Cost Performance** | **Risk Score** |
|------------------|----------|---------------------|-----------------|-------------------|---------------|
| Strategic Partners | [STRAT_COUNT] | [STRAT_OTD]% | [STRAT_QUAL]/100 | [STRAT_COST]% variance | [STRAT_RISK] |
| Preferred Suppliers | [PREF_COUNT] | [PREF_OTD]% | [PREF_QUAL]/100 | [PREF_COST]% variance | [PREF_RISK] |
| Approved Vendors | [APPR_COUNT] | [APPR_OTD]% | [APPR_QUAL]/100 | [APPR_COST]% variance | [APPR_RISK] |
| Backup Sources | [BACK_COUNT] | [BACK_OTD]% | [BACK_QUAL]/100 | [BACK_COST]% variance | [BACK_RISK] |
| Under Review | [REVIEW_COUNT] | [REVIEW_OTD]% | [REVIEW_QUAL]/100 | [REVIEW_COST]% variance | [REVIEW_RISK] |

### 6. Warehouse Operations Optimization

**Warehouse Performance:**
| **Facility** | **Size (sq ft)** | **Throughput** | **Accuracy** | **Cost/Unit** | **Productivity** |
|-------------|-----------------|---------------|-------------|--------------|-----------------|
| [WH_1] | [SIZE_1] | [THROUGH_1] units/day | [ACC_1]% | $[COST_1] | [PROD_1] units/hour |
| [WH_2] | [SIZE_2] | [THROUGH_2] units/day | [ACC_2]% | $[COST_2] | [PROD_2] units/hour |
| [WH_3] | [SIZE_3] | [THROUGH_3] units/day | [ACC_3]% | $[COST_3] | [PROD_3] units/hour |
| [WH_4] | [SIZE_4] | [THROUGH_4] units/day | [ACC_4]% | $[COST_4] | [PROD_4] units/hour |

**Process Metrics:**
```
Receiving:
- Dock-to-Stock Time: [RECEIVE_TIME] hours
- Accuracy: [RECEIVE_ACC]%
- Cost: $[RECEIVE_COST]/unit

Picking:
- Pick Rate: [PICK_RATE] lines/hour
- Accuracy: [PICK_ACC]%
- Method: [PICK_METHOD]

Packing/Shipping:
- Pack Rate: [PACK_RATE] orders/hour
- Ship Accuracy: [SHIP_ACC]%
- On-Time Ship: [SHIP_OT]%
```

### 7. Risk Management & Resilience

| **Risk Category** | **Probability** | **Impact** | **Detection** | **Mitigation Strategy** | **Contingency Plan** |
|------------------|---------------|-----------|--------------|----------------------|-------------------|
| Supply Disruption | [SUPP_PROB]% | [SUPP_IMP] | [SUPP_DET] | [SUPP_MIT] | [SUPP_CONT] |
| Demand Volatility | [DEM_PROB]% | [DEM_IMP] | [DEM_DET] | [DEM_MIT] | [DEM_CONT] |
| Transportation | [TRANS_PROB]% | [TRANS_IMP] | [TRANS_DET] | [TRANS_MIT] | [TRANS_CONT] |
| Quality Issues | [QUAL_PROB]% | [QUAL_IMP] | [QUAL_DET] | [QUAL_MIT] | [QUAL_CONT] |
| Regulatory/Compliance | [REG_PROB]% | [REG_IMP] | [REG_DET] | [REG_MIT] | [REG_CONT] |
| Cyber/Technology | [CYBER_PROB]% | [CYBER_IMP] | [CYBER_DET] | [CYBER_MIT] | [CYBER_CONT] |

### 8. Technology & Digital Integration

**System Architecture:**
| **System** | **Function** | **Integration Level** | **Data Quality** | **User Adoption** | **ROI** |
|-----------|-------------|---------------------|-----------------|------------------|---------|
| ERP | [ERP_FUNC] | [ERP_INT]% | [ERP_QUAL]% | [ERP_ADOPT]% | [ERP_ROI]% |
| WMS | [WMS_FUNC] | [WMS_INT]% | [WMS_QUAL]% | [WMS_ADOPT]% | [WMS_ROI]% |
| TMS | [TMS_FUNC] | [TMS_INT]% | [TMS_QUAL]% | [TMS_ADOPT]% | [TMS_ROI]% |
| Planning (S&OP) | [PLAN_FUNC] | [PLAN_INT]% | [PLAN_QUAL]% | [PLAN_ADOPT]% | [PLAN_ROI]% |
| Analytics/BI | [BI_FUNC] | [BI_INT]% | [BI_QUAL]% | [BI_ADOPT]% | [BI_ROI]% |
| IoT/Visibility | [IOT_FUNC] | [IOT_INT]% | [IOT_QUAL]% | [IOT_ADOPT]% | [IOT_ROI]% |

### 9. Cost-to-Serve Analysis

**Customer Segmentation:**
| **Customer Segment** | **Revenue** | **Margin** | **Cost to Serve** | **Profitability** | **Service Strategy** |
|--------------------|-----------|-----------|------------------|------------------|-------------------|
| [SEGMENT_1] | $[REV_1] | [MARGIN_1]% | $[CTS_1] | $[PROFIT_1] | [STRATEGY_1] |
| [SEGMENT_2] | $[REV_2] | [MARGIN_2]% | $[CTS_2] | $[PROFIT_2] | [STRATEGY_2] |
| [SEGMENT_3] | $[REV_3] | [MARGIN_3]% | $[CTS_3] | $[PROFIT_3] | [STRATEGY_3] |
| [SEGMENT_4] | $[REV_4] | [MARGIN_4]% | $[CTS_4] | $[PROFIT_4] | [STRATEGY_4] |
| [SEGMENT_5] | $[REV_5] | [MARGIN_5]% | $[CTS_5] | $[PROFIT_5] | [STRATEGY_5] |

### 10. Performance Metrics & KPIs

**Supply Chain Scorecard:**
```
Service Metrics:
- Perfect Order Rate: [PERFECT_ORDER]%
- Fill Rate: [FILL_RATE]%
- On-Time Delivery: [OTD]%
- Order Cycle Time: [CYCLE_TIME] days

Cost Metrics:
- Total SC Cost/Revenue: [TSC_COST]%
- Logistics Cost/Unit: $[LOG_COST]
- Inventory Carrying Cost: [CARRY_COST]%
- Cash-to-Cash Cycle: [C2C] days

Asset Metrics:
- Inventory Turns: [INV_TURNS]
- Asset Utilization: [ASSET_UTIL]%
- Working Capital/Revenue: [WC_REV]%
- ROIC: [ROIC]%

Agility Metrics:
- Upside Flexibility: [UPSIDE_FLEX]%
- Downside Adaptability: [DOWN_ADAPT] days
- Supply Chain Cycle Time: [SC_CYCLE] days
- Time to Market: [TTM] days
```

## Usage Examples

### Example 1: Global Manufacturing Network
```
Company: International Electronics Corp
Network: 15 suppliers, 3 factories, 8 DCs
Products: 5,000 SKUs
Geography: 4 continents
Volume: 50M units/year
Challenge: Long lead times, inventory optimization
```

### Example 2: E-commerce Fulfillment
```
Company: Online Retailer
Network: 500 suppliers, 12 fulfillment centers
Orders: 1M/day
Delivery Promise: Same/next day
Technology: AI-driven demand planning
Focus: Last-mile optimization
```

### Example 3: Pharmaceutical Supply Chain
```
Company: Pharma Distributor
Products: Temperature-controlled medicines
Network: 50 manufacturers, 200 hospitals
Compliance: FDA, cold chain
Traceability: Serialization required
Challenge: Zero stock-outs, 100% compliance
```

## Customization Options

### 1. Industry Focus
- Manufacturing
- Retail/E-commerce
- Healthcare/Pharma
- Food & Beverage
- Automotive

### 2. Supply Chain Type
- Make-to-stock
- Make-to-order
- Configure-to-order
- Engineer-to-order
- Hybrid models

### 3. Geographic Scope
- Local/Regional
- National
- International
- Global
- Omnichannel

### 4. Optimization Priority
- Cost minimization
- Service maximization
- Inventory reduction
- Lead time compression
- Risk mitigation

### 5. Technology Maturity
- Manual/Excel-based
- Basic ERP
- Integrated systems
- Advanced analytics
- AI/ML-driven