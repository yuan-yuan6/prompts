---
category: finance
last_updated: 2025-11-09
related_templates:
- finance/investment-portfolio-management.md
- finance/digital-banking-strategy.md
- finance/risk-management-framework.md
tags:
- enterprise-risk-management
- coso-framework
- three-lines-defense
- risk-culture
title: Enterprise Risk Management (ERM) Framework
use_cases:
- Creating comprehensive framework for implementing enterprise risk management including
  risk identification, assessment, mitigation strategies, regulatory compliance, and
  governance structures for financial institutions.
- Project planning and execution
- Strategy development
industries:
- finance
- government
- technology
type: template
difficulty: intermediate
slug: enterprise-risk-management
---

# Enterprise Risk Management (ERM) Framework

## Purpose
Comprehensive framework for implementing enterprise risk management including risk identification, assessment, mitigation strategies, regulatory compliance, and governance structures for financial institutions.

## Quick ERM Prompt
Implement ERM for [institution type] with $[X] assets. Risk appetite: [statement]. Categories: credit (NPL [X%], concentration [Y%]), market (VaR $[Z], EVE shock), operational (cyber, BCP), strategic, reputational. Governance: board oversight, risk committee, 3 lines of defense. Framework: [COSO/ISO 31000]. KRIs: [5-7 per category]. Reporting: [monthly dashboard], [quarterly board report]. Culture: training, incentives.

## Quick Start

Implement enterprise risk management basics in 1-2 hours with these practical scenarios:

### Example 1: Quick Risk Assessment
Conduct initial risk assessment for a regional bank with $10B in assets:
```
Institution: Regional commercial bank
Assets: $10 billion
Risk Appetite: Moderate
Priority Risks Identified:

Credit Risk:
- NPL Ratio: 1.2% (acceptable, industry avg 1.5%)
- Concentration: Top 10 borrowers = 18% of loans (monitor)
- Action: Implement concentration limit at 20%

Market Risk:
- Interest Rate Risk: $15M EVE exposure per 200bp shock
- Action: Establish hedging strategy with interest rate swaps

Operational Risk:
- Cyber incidents: 3 minor breaches YTD
- Action: Upgrade cybersecurity controls, conduct penetration testing

Quick Risk Dashboard Setup (30 min):
1. Define 5-7 key risk indicators per category
2. Set red/yellow/green thresholds
3. Establish weekly monitoring cadence
4. Create escalation protocol for breaches
```

### Example 2: Stress Testing Implementation
Run basic stress test for loan portfolio:
```
Scenario: Severe Economic Recession
- GDP decline: -3%
- Unemployment: +5%
- Commercial real estate values: -25%

Impact Analysis:
Current Portfolio: $5B commercial loans
- Probability of default: 2% → 6% (stress scenario)
- Expected losses: $100M → $300M
- Capital impact: -2.5% to capital ratio
- Current CET1: 12.5% → Stressed: 10.0%

Regulatory Minimum: 7%
Buffer: 3% above minimum ✓

Management Actions if Triggered:
- Suspend dividend payments
- Reduce new loan originations by 30%
- Raise $150M in Tier 1 capital
- Increase loan loss provisions
```

### Example 3: Governance Structure Setup
Establish basic risk committee structure:
```
Three Lines of Defense Model:

1st Line - Business Units:
- Risk owners: Business line managers
- Responsibility: Day-to-day risk management
- Meeting: Weekly risk reviews

2nd Line - Risk Management:
- Chief Risk Officer (CRO)
- Responsibility: Independent risk oversight
- Meeting: Monthly risk committee

3rd Line - Internal Audit:
- Responsibility: Independent assurance
- Meeting: Quarterly audit committee

Quick Implementation:
1. Assign risk owners for each business line
2. Create monthly risk reporting template
3. Establish escalation triggers (e.g., limit breaches)
4. Schedule quarterly board risk committee meetings
```

### Rapid Risk Assessment Checklist
Use this 15-minute checklist for initial risk evaluation:

**Credit Risk** - ☐ NPL ratio reviewed ☐ Concentration limits set ☐ Provision adequacy checked
**Market Risk** - ☐ VaR calculated ☐ Interest rate exposure measured ☐ FX exposure quantified
**Operational Risk** - ☐ Loss events tracked ☐ KRIs monitored ☐ Business continuity tested
**Liquidity Risk** - ☐ LCR calculated ☐ Funding sources diversified ☐ Stress scenarios run
**Compliance Risk** - ☐ Regulatory changes tracked ☐ Policies updated ☐ Training completed

### Essential First Steps
1. Identify top 10 risks to the institution
2. Quantify exposure for each major risk category
3. Set risk appetite limits with board approval
4. Implement basic risk monitoring dashboard
5. Establish monthly risk reporting to senior management
6. Create incident response and escalation procedures

## Template

Develop ERM framework for [INSTITUTION_NAME] with [ASSET_SIZE] in assets, [RISK_APPETITE] risk appetite level, [REGULATORY_REGIME] regulatory requirements, targeting [CAPITAL_RATIO]% capital adequacy, [ROE_TARGET]% ROE, and [RISK_SCORE] composite risk rating.

### 1. Risk Governance Structure

| **Governance Layer** | **Responsibilities** | **Reporting Lines** | **Meeting Frequency** | **Decision Authority** | **Escalation Path** |
|--------------------|-------------------|------------------|-------------------|---------------------|-------------------|
| Board Risk Committee | [BOARD_RESP] | [BOARD_REPORT] | [BOARD_FREQ] | [BOARD_AUTH] | [BOARD_ESCALATE] |
| Executive Risk Committee | [EXEC_RESP] | [EXEC_REPORT] | [EXEC_FREQ] | [EXEC_AUTH] | [EXEC_ESCALATE] |
| Chief Risk Officer | [CRO_RESP] | [CRO_REPORT] | [CRO_FREQ] | [CRO_AUTH] | [CRO_ESCALATE] |
| Business Risk Committees | [BUS_RESP] | [BUS_REPORT] | [BUS_FREQ] | [BUS_AUTH] | [BUS_ESCALATE] |
| Risk Management Function | [RISK_RESP] | [RISK_REPORT] | [RISK_FREQ] | [RISK_AUTH] | [RISK_ESCALATE] |
| Three Lines of Defense | [THREE_LINES] | [THREE_REPORT] | [THREE_FREQ] | [THREE_AUTH] | [THREE_ESCALATE] |

### 2. Risk Identification & Assessment

**Risk Taxonomy & Classification:**
```
Credit Risk:
- Probability of Default: [PD_MEASURE]%
- Loss Given Default: [LGD_MEASURE]%
- Exposure at Default: $[EAD_MEASURE]
- Expected Loss: $[EL_MEASURE]
- Risk Rating Distribution: [RATING_DIST]
- Concentration Risk: [CONCENTRATION]

Market Risk:
- Value at Risk (VaR): $[VAR_MEASURE]
- Stressed VaR: $[SVAR_MEASURE]
- Interest Rate Risk: [IRR_MEASURE] bps
- FX Risk: $[FX_MEASURE]
- Equity Risk: $[EQUITY_MEASURE]
- Commodity Risk: $[COMMODITY_MEASURE]

### Operational Risk
- Op Risk Capital: $[OP_CAPITAL]
- Loss Events: [LOSS_EVENTS]/year
- Key Risk Indicators: [KRI_COUNT]
- Control Failures: [CONTROL_FAIL]
- Process Risk: [PROCESS_RISK]
- Technology Risk: [TECH_RISK]

### Liquidity Risk
- Liquidity Coverage Ratio: [LCR_RATIO]%
- Net Stable Funding Ratio: [NSFR_RATIO]%
- Cash Flow at Risk: $[CFAR_MEASURE]
- Funding Concentration: [FUND_CONC]
- Stress Testing Results: [STRESS_RESULT]
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[INSTITUTION_NAME]` | Name of the institution | "John Smith" |
| `[ASSET_SIZE]` | Specify the asset size | "[specify value]" |
| `[RISK_APPETITE]` | Specify the risk appetite | "[specify value]" |
| `[REGULATORY_REGIME]` | Specify the regulatory regime | "[specify value]" |
| `[CAPITAL_RATIO]` | Specify the capital ratio | "[specify value]" |
| `[ROE_TARGET]` | Target or intended roe | "[specify value]" |
| `[RISK_SCORE]` | Specify the risk score | "[specify value]" |
| `[BOARD_RESP]` | Specify the board resp | "[specify value]" |
| `[BOARD_REPORT]` | Specify the board report | "[specify value]" |
| `[BOARD_FREQ]` | Specify the board freq | "[specify value]" |
| `[BOARD_AUTH]` | Specify the board auth | "[specify value]" |
| `[BOARD_ESCALATE]` | Specify the board escalate | "[specify value]" |
| `[EXEC_RESP]` | Specify the exec resp | "[specify value]" |
| `[EXEC_REPORT]` | Specify the exec report | "[specify value]" |
| `[EXEC_FREQ]` | Specify the exec freq | "[specify value]" |
| `[EXEC_AUTH]` | Specify the exec auth | "[specify value]" |
| `[EXEC_ESCALATE]` | Specify the exec escalate | "[specify value]" |
| `[CRO_RESP]` | Specify the cro resp | "[specify value]" |
| `[CRO_REPORT]` | Specify the cro report | "[specify value]" |
| `[CRO_FREQ]` | Specify the cro freq | "[specify value]" |
| `[CRO_AUTH]` | Specify the cro auth | "[specify value]" |
| `[CRO_ESCALATE]` | Specify the cro escalate | "[specify value]" |
| `[BUS_RESP]` | Specify the bus resp | "[specify value]" |
| `[BUS_REPORT]` | Specify the bus report | "[specify value]" |
| `[BUS_FREQ]` | Specify the bus freq | "[specify value]" |
| `[BUS_AUTH]` | Specify the bus auth | "[specify value]" |
| `[BUS_ESCALATE]` | Specify the bus escalate | "[specify value]" |
| `[RISK_RESP]` | Specify the risk resp | "[specify value]" |
| `[RISK_REPORT]` | Specify the risk report | "[specify value]" |
| `[RISK_FREQ]` | Specify the risk freq | "[specify value]" |
| `[RISK_AUTH]` | Specify the risk auth | "[specify value]" |
| `[RISK_ESCALATE]` | Specify the risk escalate | "[specify value]" |
| `[THREE_LINES]` | Specify the three lines | "[specify value]" |
| `[THREE_REPORT]` | Specify the three report | "[specify value]" |
| `[THREE_FREQ]` | Specify the three freq | "[specify value]" |
| `[THREE_AUTH]` | Specify the three auth | "[specify value]" |
| `[THREE_ESCALATE]` | Specify the three escalate | "[specify value]" |
| `[PD_MEASURE]` | Specify the pd measure | "[specify value]" |
| `[LGD_MEASURE]` | Specify the lgd measure | "[specify value]" |
| `[EAD_MEASURE]` | Specify the ead measure | "[specify value]" |
| `[EL_MEASURE]` | Specify the el measure | "[specify value]" |
| `[RATING_DIST]` | Specify the rating dist | "[specify value]" |
| `[CONCENTRATION]` | Specify the concentration | "[specify value]" |
| `[VAR_MEASURE]` | Specify the var measure | "[specify value]" |
| `[SVAR_MEASURE]` | Specify the svar measure | "[specify value]" |
| `[IRR_MEASURE]` | Specify the irr measure | "[specify value]" |
| `[FX_MEASURE]` | Specify the fx measure | "[specify value]" |
| `[EQUITY_MEASURE]` | Specify the equity measure | "[specify value]" |
| `[COMMODITY_MEASURE]` | Specify the commodity measure | "[specify value]" |
| `[OP_CAPITAL]` | Specify the op capital | "[specify value]" |
| `[LOSS_EVENTS]` | Specify the loss events | "[specify value]" |
| `[KRI_COUNT]` | Specify the kri count | "10" |
| `[CONTROL_FAIL]` | Specify the control fail | "[specify value]" |
| `[PROCESS_RISK]` | Specify the process risk | "[specify value]" |
| `[TECH_RISK]` | Specify the tech risk | "[specify value]" |
| `[LCR_RATIO]` | Specify the lcr ratio | "[specify value]" |
| `[NSFR_RATIO]` | Specify the nsfr ratio | "[specify value]" |
| `[CFAR_MEASURE]` | Specify the cfar measure | "[specify value]" |
| `[FUND_CONC]` | Specify the fund conc | "[specify value]" |
| `[STRESS_RESULT]` | Specify the stress result | "[specify value]" |
| `[CREDIT_APPETITE]` | Specify the credit appetite | "[specify value]" |
| `[CREDIT_TOLERANCE]` | Specify the credit tolerance | "[specify value]" |
| `[CREDIT_EXPOSURE]` | Specify the credit exposure | "[specify value]" |
| `[CREDIT_UTIL]` | Specify the credit util | "[specify value]" |
| `[CREDIT_ACTION]` | Specify the credit action | "[specify value]" |
| `[MARKET_APPETITE]` | Specify the market appetite | "[specify value]" |
| `[MARKET_TOLERANCE]` | Specify the market tolerance | "[specify value]" |
| `[MARKET_EXPOSURE]` | Specify the market exposure | "[specify value]" |
| `[MARKET_UTIL]` | Specify the market util | "[specify value]" |
| `[MARKET_ACTION]` | Specify the market action | "[specify value]" |
| `[OP_APPETITE]` | Specify the op appetite | "[specify value]" |
| `[OP_TOLERANCE]` | Specify the op tolerance | "[specify value]" |
| `[OP_EXPOSURE]` | Specify the op exposure | "[specify value]" |
| `[OP_UTIL]` | Specify the op util | "[specify value]" |
| `[OP_ACTION]` | Specify the op action | "[specify value]" |
| `[LIQ_APPETITE]` | Specify the liq appetite | "[specify value]" |
| `[LIQ_TOLERANCE]` | Specify the liq tolerance | "[specify value]" |
| `[LIQ_EXPOSURE]` | Specify the liq exposure | "[specify value]" |
| `[LIQ_UTIL]` | Specify the liq util | "[specify value]" |
| `[LIQ_ACTION]` | Specify the liq action | "[specify value]" |
| `[COMP_APPETITE]` | Specify the comp appetite | "[specify value]" |
| `[COMP_TOLERANCE]` | Specify the comp tolerance | "[specify value]" |
| `[COMP_EXPOSURE]` | Specify the comp exposure | "[specify value]" |
| `[COMP_UTIL]` | Specify the comp util | "[specify value]" |
| `[COMP_ACTION]` | Specify the comp action | "[specify value]" |
| `[REP_APPETITE]` | Specify the rep appetite | "[specify value]" |
| `[REP_TOLERANCE]` | Specify the rep tolerance | "[specify value]" |
| `[REP_EXPOSURE]` | Specify the rep exposure | "[specify value]" |
| `[REP_UTIL]` | Specify the rep util | "[specify value]" |
| `[REP_ACTION]` | Specify the rep action | "[specify value]" |
| `[POLICY_CONTROLS]` | Specify the policy controls | "[specify value]" |
| `[LIMIT_CONTROLS]` | Specify the limit controls | "[specify value]" |
| `[APPROVAL_CONTROLS]` | Specify the approval controls | "[specify value]" |
| `[SYSTEM_CONTROLS]` | Specify the system controls | "[specify value]" |
| `[SOD_CONTROLS]` | Specify the sod controls | "[specify value]" |
| `[MONITOR_CONTROLS]` | Specify the monitor controls | "[specify value]" |
| `[EXCEPTION_CONTROLS]` | Specify the exception controls | "[specify value]" |
| `[RECON_CONTROLS]` | Specify the recon controls | "[specify value]" |
| `[REVIEW_CONTROLS]` | Specify the review controls | "[specify value]" |
| `[AUDIT_CONTROLS]` | Specify the audit controls | "[specify value]" |
| `[INCIDENT_CONTROLS]` | Specify the incident controls | "[specify value]" |
| `[RECOVERY_CONTROLS]` | Specify the recovery controls | "[specify value]" |
| `[REMEDIATE_CONTROLS]` | Specify the remediate controls | "[specify value]" |
| `[ESCALATE_CONTROLS]` | Specify the escalate controls | "[specify value]" |
| `[IMPROVE_CONTROLS]` | Specify the improve controls | "[specify value]" |
| `[INSURANCE_COVER]` | Specify the insurance cover | "[specify value]" |
| `[HEDGE_STRATEGY]` | Strategy or approach for hedge | "[specify value]" |
| `[GUARANTEE_AMOUNT]` | Specify the guarantee amount | "[specify value]" |
| `[COLLATERAL_MGMT]` | Specify the collateral mgmt | "[specify value]" |
| `[DERIVATIVE_USE]` | Specify the derivative use | "[specify value]" |
| `[BASEL_CURRENT]` | Specify the basel current | "[specify value]" |
| `[BASEL_TARGET]` | Target or intended basel | "[specify value]" |
| `[BASEL_GAP]` | Specify the basel gap | "[specify value]" |
| `[BASEL_ACTION]` | Specify the basel action | "[specify value]" |
| `[BASEL_TIME]` | Specify the basel time | "[specify value]" |
| `[LEVERAGE_CURRENT]` | Specify the leverage current | "[specify value]" |
| `[LEVERAGE_TARGET]` | Target or intended leverage | "[specify value]" |
| `[LEVERAGE_GAP]` | Specify the leverage gap | "[specify value]" |
| `[LEVERAGE_ACTION]` | Specify the leverage action | "[specify value]" |
| `[LEVERAGE_TIME]` | Specify the leverage time | "[specify value]" |
| `[ICAAP_CURRENT]` | Specify the icaap current | "[specify value]" |
| `[ICAAP_TARGET]` | Target or intended icaap | "[specify value]" |
| `[ICAAP_GAP]` | Specify the icaap gap | "[specify value]" |
| `[ICAAP_ACTION]` | Specify the icaap action | "[specify value]" |
| `[ICAAP_TIME]` | Specify the icaap time | "[specify value]" |
| `[STRESS_CURRENT]` | Specify the stress current | "[specify value]" |
| `[STRESS_TARGET]` | Target or intended stress | "[specify value]" |
| `[STRESS_GAP]` | Specify the stress gap | "[specify value]" |
| `[STRESS_ACTION]` | Specify the stress action | "[specify value]" |
| `[STRESS_TIME]` | Specify the stress time | "[specify value]" |
| `[IFRS_CURRENT]` | Specify the ifrs current | "[specify value]" |
| `[IFRS_TARGET]` | Target or intended ifrs | "[specify value]" |
| `[IFRS_GAP]` | Specify the ifrs gap | "[specify value]" |
| `[IFRS_ACTION]` | Specify the ifrs action | "[specify value]" |
| `[IFRS_TIME]` | Specify the ifrs time | "[specify value]" |
| `[AML_CURRENT]` | Specify the aml current | "[specify value]" |
| `[AML_TARGET]` | Target or intended aml | "[specify value]" |
| `[AML_GAP]` | Specify the aml gap | "[specify value]" |
| `[AML_ACTION]` | Specify the aml action | "[specify value]" |
| `[AML_TIME]` | Specify the aml time | "[specify value]" |
| `[QUALITY_METRICS]` | Specify the quality metrics | "[specify value]" |
| `[QUALITY_FREQ]` | Specify the quality freq | "[specify value]" |
| `[QUALITY_THRESH]` | Specify the quality thresh | "[specify value]" |
| `[QUALITY_VALUE]` | Specify the quality value | "[specify value]" |
| `[QUALITY_TREND]` | Specify the quality trend | "[specify value]" |
| `[MARKET_METRICS]` | Specify the market metrics | "[specify value]" |
| `[MARKET_FREQ]` | Specify the market freq | "[specify value]" |
| `[MARKET_THRESH]` | Specify the market thresh | "[specify value]" |
| `[MARKET_VALUE]` | Specify the market value | "[specify value]" |
| `[MARKET_TREND]` | Specify the market trend | "[specify value]" |
| `[OP_METRICS]` | Specify the op metrics | "[specify value]" |
| `[OP_FREQ]` | Specify the op freq | "[specify value]" |
| `[OP_THRESH]` | Specify the op thresh | "[specify value]" |
| `[OP_VALUE]` | Specify the op value | "[specify value]" |
| `[OP_TREND]` | Specify the op trend | "[specify value]" |
| `[LIQ_METRICS]` | Specify the liq metrics | "[specify value]" |
| `[LIQ_FREQ]` | Specify the liq freq | "[specify value]" |
| `[LIQ_THRESH]` | Specify the liq thresh | "[specify value]" |
| `[LIQ_VALUE]` | Specify the liq value | "[specify value]" |
| `[LIQ_TREND]` | Specify the liq trend | "[specify value]" |
| `[COMP_METRICS]` | Specify the comp metrics | "[specify value]" |
| `[COMP_FREQ]` | Specify the comp freq | "[specify value]" |
| `[COMP_THRESH]` | Specify the comp thresh | "[specify value]" |
| `[COMP_VALUE]` | Specify the comp value | "[specify value]" |
| `[COMP_TREND]` | Specify the comp trend | "[specify value]" |
| `[EWS_METRICS]` | Specify the ews metrics | "[specify value]" |
| `[EWS_FREQ]` | Specify the ews freq | "[specify value]" |
| `[EWS_THRESH]` | Specify the ews thresh | "[specify value]" |
| `[EWS_VALUE]` | Specify the ews value | "[specify value]" |
| `[EWS_TREND]` | Specify the ews trend | "[specify value]" |
| `[BASELINE_SCENARIO]` | Specify the baseline scenario | "[specify value]" |
| `[ADVERSE_SCENARIO]` | Specify the adverse scenario | "[specify value]" |
| `[SEVERE_SCENARIO]` | Specify the severe scenario | "[specify value]" |
| `[IDIO_SCENARIO]` | Specify the idio scenario | "[specify value]" |
| `[REVERSE_SCENARIO]` | Specify the reverse scenario | "[specify value]" |
| `[CAPITAL_IMPACT]` | Specify the capital impact | "[specify value]" |
| `[PL_IMPACT]` | Specify the pl impact | "[specify value]" |
| `[LIQ_IMPACT]` | Specify the liq impact | "[specify value]" |
| `[CREDIT_LOSSES]` | Specify the credit losses | "[specify value]" |
| `[MARKET_LOSSES]` | Specify the market losses | "[specify value]" |
| `[CAPITAL_ACTIONS]` | Specify the capital actions | "[specify value]" |
| `[RISK_ACTIONS]` | Specify the risk actions | "[specify value]" |
| `[LIQ_ACTIONS]` | Specify the liq actions | "[specify value]" |
| `[BCP_ACTIONS]` | Specify the bcp actions | "[specify value]" |
| `[RECOVERY_ACTIONS]` | Specify the recovery actions | "[specify value]" |
| `[CCAR_STATUS]` | Specify the ccar status | "In Progress" |
| `[EBA_STATUS]` | Specify the eba status | "In Progress" |
| `[INTERNAL_STATUS]` | Specify the internal status | "In Progress" |
| `[DOC_STATUS]` | Specify the doc status | "In Progress" |
| `[VALIDATION_STATUS]` | Specify the validation status | "In Progress" |
| `[DW_CURRENT]` | Specify the dw current | "[specify value]" |
| `[DW_TARGET]` | Target or intended dw | "[specify value]" |
| `[DW_INVEST]` | Specify the dw invest | "[specify value]" |
| `[DW_BENEFIT]` | Specify the dw benefit | "[specify value]" |
| `[DW_TIMELINE]` | Timeline or schedule for dw | "6 months" |
| `[ANALYTICS_CURRENT]` | Specify the analytics current | "[specify value]" |
| `[ANALYTICS_TARGET]` | Target or intended analytics | "[specify value]" |
| `[ANALYTICS_INVEST]` | Specify the analytics invest | "[specify value]" |
| `[ANALYTICS_BENEFIT]` | Specify the analytics benefit | "[specify value]" |
| `[ANALYTICS_TIMELINE]` | Timeline or schedule for analytics | "6 months" |
| `[REG_CURRENT]` | Specify the reg current | "[specify value]" |
| `[REG_TARGET]` | Target or intended reg | "[specify value]" |
| `[REG_INVEST]` | Specify the reg invest | "[specify value]" |
| `[REG_BENEFIT]` | Specify the reg benefit | "[specify value]" |
| `[REG_TIMELINE]` | Timeline or schedule for reg | "6 months" |
| `[AI_CURRENT]` | Specify the ai current | "[specify value]" |
| `[AI_TARGET]` | Target or intended ai | "[specify value]" |
| `[AI_INVEST]` | Specify the ai invest | "[specify value]" |
| `[AI_BENEFIT]` | Specify the ai benefit | "[specify value]" |
| `[AI_TIMELINE]` | Timeline or schedule for ai | "6 months" |
| `[RT_CURRENT]` | Specify the rt current | "[specify value]" |
| `[RT_TARGET]` | Target or intended rt | "[specify value]" |
| `[RT_INVEST]` | Specify the rt invest | "[specify value]" |
| `[RT_BENEFIT]` | Specify the rt benefit | "[specify value]" |
| `[RT_TIMELINE]` | Timeline or schedule for rt | "6 months" |
| `[CLOUD_CURRENT]` | Specify the cloud current | "[specify value]" |
| `[CLOUD_TARGET]` | Target or intended cloud | "[specify value]" |
| `[CLOUD_INVEST]` | Specify the cloud invest | "[specify value]" |
| `[CLOUD_BENEFIT]` | Specify the cloud benefit | "[specify value]" |
| `[CLOUD_TIMELINE]` | Timeline or schedule for cloud | "6 months" |
| `[LIQ_TEAM]` | Specify the liq team | "[specify value]" |
| `[LIQ_COMM]` | Specify the liq comm | "[specify value]" |
| `[LIQ_DECISION]` | Specify the liq decision | "[specify value]" |
| `[LIQ_RECOVERY]` | Specify the liq recovery | "[specify value]" |
| `[LIQ_TEST]` | Specify the liq test | "[specify value]" |
| `[CREDIT_TEAM]` | Specify the credit team | "[specify value]" |
| `[CREDIT_COMM]` | Specify the credit comm | "[specify value]" |
| `[CREDIT_DECISION]` | Specify the credit decision | "[specify value]" |
| `[CREDIT_RECOVERY]` | Specify the credit recovery | "[specify value]" |
| `[CREDIT_TEST]` | Specify the credit test | "[specify value]" |
| `[MARKET_TEAM]` | Specify the market team | "[specify value]" |
| `[MARKET_COMM]` | Specify the market comm | "[specify value]" |
| `[MARKET_DECISION]` | Specify the market decision | "[specify value]" |
| `[MARKET_RECOVERY]` | Specify the market recovery | "[specify value]" |
| `[MARKET_TEST]` | Specify the market test | "[specify value]" |
| `[OP_TEAM]` | Specify the op team | "[specify value]" |
| `[OP_COMM]` | Specify the op comm | "[specify value]" |
| `[OP_DECISION]` | Specify the op decision | "[specify value]" |
| `[OP_RECOVERY]` | Specify the op recovery | "[specify value]" |
| `[OP_TEST]` | Specify the op test | "[specify value]" |
| `[CYBER_TEAM]` | Specify the cyber team | "[specify value]" |
| `[CYBER_COMM]` | Specify the cyber comm | "[specify value]" |
| `[CYBER_DECISION]` | Specify the cyber decision | "[specify value]" |
| `[CYBER_RECOVERY]` | Specify the cyber recovery | "[specify value]" |
| `[CYBER_TEST]` | Specify the cyber test | "[specify value]" |
| `[REG_TEAM]` | Specify the reg team | "[specify value]" |
| `[REG_COMM]` | Specify the reg comm | "[specify value]" |
| `[REG_DECISION]` | Specify the reg decision | "[specify value]" |
| `[REG_RECOVERY]` | Specify the reg recovery | "[specify value]" |
| `[REG_TEST]` | Specify the reg test | "[specify value]" |
| `[AWARENESS_SCORE]` | Specify the awareness score | "[specify value]" |
| `[ACCOUNTABILITY]` | Specify the accountability | "10" |
| `[TRANSPARENCY]` | Specify the transparency | "[specify value]" |
| `[CHALLENGE]` | Specify the challenge | "[specify value]" |
| `[LEARNING]` | Specify the learning | "[specify value]" |
| `[BOARD_TRAINING]` | Specify the board training | "[specify value]" |
| `[EXEC_TRAINING]` | Specify the exec training | "[specify value]" |
| `[PROF_TRAINING]` | Specify the prof training | "[specify value]" |
| `[BUS_TRAINING]` | Specify the bus training | "[specify value]" |
| `[NEW_TRAINING]` | Specify the new training | "[specify value]" |
| `[KPI_INTEGRATION]` | Specify the kpi integration | "[specify value]" |
| `[RISK_COMP]` | Specify the risk comp | "[specify value]" |
| `[CONSEQUENCE]` | Specify the consequence | "[specify value]" |
| `[RECOGNITION]` | Specify the recognition | "[specify value]" |
| `[CAREER_DEV]` | Specify the career dev | "[specify value]" |
| `[COMMITTEE_COMM]` | Specify the committee comm | "[specify value]" |
| `[TOWNHALL_FREQ]` | Specify the townhall freq | "[specify value]" |
| `[NEWSLETTER]` | Specify the newsletter | "[specify value]" |
| `[INTRANET]` | Specify the intranet | "[specify value]" |
| `[MATERIALS]` | Specify the materials | "[specify value]" |

### 3. Risk Appetite Framework

| **Risk Category** | **Risk Appetite** | **Risk Tolerance** | **Current Exposure** | **Limit Utilization** | **Action Required** |
|------------------|-----------------|------------------|-------------------|---------------------|-------------------|
| Credit Risk | [CREDIT_APPETITE] | [CREDIT_TOLERANCE] | [CREDIT_EXPOSURE] | [CREDIT_UTIL]% | [CREDIT_ACTION] |
| Market Risk | [MARKET_APPETITE] | [MARKET_TOLERANCE] | [MARKET_EXPOSURE] | [MARKET_UTIL]% | [MARKET_ACTION] |
| Operational Risk | [OP_APPETITE] | [OP_TOLERANCE] | [OP_EXPOSURE] | [OP_UTIL]% | [OP_ACTION] |
| Liquidity Risk | [LIQ_APPETITE] | [LIQ_TOLERANCE] | [LIQ_EXPOSURE] | [LIQ_UTIL]% | [LIQ_ACTION] |
| Compliance Risk | [COMP_APPETITE] | [COMP_TOLERANCE] | [COMP_EXPOSURE] | [COMP_UTIL]% | [COMP_ACTION] |
| Reputational Risk | [REP_APPETITE] | [REP_TOLERANCE] | [REP_EXPOSURE] | [REP_UTIL]% | [REP_ACTION] |

### 4. Risk Mitigation Strategies

```
Risk Control Framework:
Preventive Controls:
- Policy Framework: [POLICY_CONTROLS]
- Limit Structure: [LIMIT_CONTROLS]
- Approval Hierarchy: [APPROVAL_CONTROLS]
- System Controls: [SYSTEM_CONTROLS]
- Segregation of Duties: [SOD_CONTROLS]

Detective Controls:
- Monitoring Systems: [MONITOR_CONTROLS]
- Exception Reporting: [EXCEPTION_CONTROLS]
- Reconciliations: [RECON_CONTROLS]
- Independent Review: [REVIEW_CONTROLS]
- Audit Program: [AUDIT_CONTROLS]

### Corrective Controls
- Incident Management: [INCIDENT_CONTROLS]
- Recovery Plans: [RECOVERY_CONTROLS]
- Remediation Process: [REMEDIATE_CONTROLS]
- Escalation Procedures: [ESCALATE_CONTROLS]
- Continuous Improvement: [IMPROVE_CONTROLS]

### Risk Transfer
- Insurance Coverage: $[INSURANCE_COVER]
- Hedging Strategies: [HEDGE_STRATEGY]
- Guarantees: $[GUARANTEE_AMOUNT]
- Collateral Management: [COLLATERAL_MGMT]
- Derivatives Usage: [DERIVATIVE_USE]
```

### 5. Regulatory Compliance & Capital Management

| **Regulatory Requirement** | **Current Status** | **Target Level** | **Gap Analysis** | **Action Plan** | **Timeline** |
|--------------------------|------------------|----------------|----------------|---------------|------------|
| Basel III Capital | [BASEL_CURRENT]% | [BASEL_TARGET]% | [BASEL_GAP] | [BASEL_ACTION] | [BASEL_TIME] |
| Leverage Ratio | [LEVERAGE_CURRENT]% | [LEVERAGE_TARGET]% | [LEVERAGE_GAP] | [LEVERAGE_ACTION] | [LEVERAGE_TIME] |
| ICAAP/ILAAP | [ICAAP_CURRENT] | [ICAAP_TARGET] | [ICAAP_GAP] | [ICAAP_ACTION] | [ICAAP_TIME] |
| Stress Testing | [STRESS_CURRENT] | [STRESS_TARGET] | [STRESS_GAP] | [STRESS_ACTION] | [STRESS_TIME] |
| IFRS 9/CECL | [IFRS_CURRENT] | [IFRS_TARGET] | [IFRS_GAP] | [IFRS_ACTION] | [IFRS_TIME] |
| AML/CFT Compliance | [AML_CURRENT] | [AML_TARGET] | [AML_GAP] | [AML_ACTION] | [AML_TIME] |

### 6. Risk Monitoring & Reporting

**Risk Dashboard & Metrics:**
| **Monitoring Area** | **Key Metrics** | **Frequency** | **Threshold** | **Current Value** | **Trend** |
|-------------------|---------------|-------------|-------------|-----------------|----------|
| Portfolio Quality | [QUALITY_METRICS] | [QUALITY_FREQ] | [QUALITY_THRESH] | [QUALITY_VALUE] | [QUALITY_TREND] |
| Market Exposure | [MARKET_METRICS] | [MARKET_FREQ] | [MARKET_THRESH] | [MARKET_VALUE] | [MARKET_TREND] |
| Operational Losses | [OP_METRICS] | [OP_FREQ] | [OP_THRESH] | [OP_VALUE] | [OP_TREND] |
| Liquidity Position | [LIQ_METRICS] | [LIQ_FREQ] | [LIQ_THRESH] | [LIQ_VALUE] | [LIQ_TREND] |
| Compliance Issues | [COMP_METRICS] | [COMP_FREQ] | [COMP_THRESH] | [COMP_VALUE] | [COMP_TREND] |
| Early Warning Signals | [EWS_METRICS] | [EWS_FREQ] | [EWS_THRESH] | [EWS_VALUE] | [EWS_TREND] |

### 7. Stress Testing & Scenario Analysis

```
Stress Testing Framework:
Scenario Design:
- Baseline Scenario: [BASELINE_SCENARIO]
- Adverse Scenario: [ADVERSE_SCENARIO]
- Severely Adverse: [SEVERE_SCENARIO]
- Idiosyncratic Shocks: [IDIO_SCENARIO]
- Reverse Stress Test: [REVERSE_SCENARIO]

Impact Assessment:
- Capital Impact: [CAPITAL_IMPACT]%
- P&L Impact: $[PL_IMPACT]
- Liquidity Impact: [LIQ_IMPACT] days
- Credit Losses: $[CREDIT_LOSSES]
- Market Losses: $[MARKET_LOSSES]

### Management Actions
- Capital Conservation: [CAPITAL_ACTIONS]
- Risk Reduction: [RISK_ACTIONS]
- Liquidity Management: [LIQ_ACTIONS]
- Business Continuity: [BCP_ACTIONS]
- Recovery Planning: [RECOVERY_ACTIONS]

### Regulatory Submissions
- CCAR/DFAST: [CCAR_STATUS]
- EBA Stress Test: [EBA_STATUS]
- Internal Stress Test: [INTERNAL_STATUS]
- Documentation: [DOC_STATUS]
- Model Validation: [VALIDATION_STATUS]
```

### 8. Technology & Data Management

| **Technology Component** | **Current State** | **Target State** | **Investment** | **Benefits** | **Implementation** |
|------------------------|-----------------|----------------|--------------|------------|-------------------|
| Risk Data Warehouse | [DW_CURRENT] | [DW_TARGET] | $[DW_INVEST] | [DW_BENEFIT] | [DW_TIMELINE] |
| Risk Analytics Platform | [ANALYTICS_CURRENT] | [ANALYTICS_TARGET] | $[ANALYTICS_INVEST] | [ANALYTICS_BENEFIT] | [ANALYTICS_TIMELINE] |
| Regulatory Reporting | [REG_CURRENT] | [REG_TARGET] | $[REG_INVEST] | [REG_BENEFIT] | [REG_TIMELINE] |
| AI/ML Models | [AI_CURRENT] | [AI_TARGET] | $[AI_INVEST] | [AI_BENEFIT] | [AI_TIMELINE] |
| Real-time Monitoring | [RT_CURRENT] | [RT_TARGET] | $[RT_INVEST] | [RT_BENEFIT] | [RT_TIMELINE] |
| Cloud Infrastructure | [CLOUD_CURRENT] | [CLOUD_TARGET] | $[CLOUD_INVEST] | [CLOUD_BENEFIT] | [CLOUD_TIMELINE] |

### 9. Crisis Management & Recovery

**Crisis Response Framework:**
| **Crisis Type** | **Response Team** | **Communication Plan** | **Decision Authority** | **Recovery Time** | **Testing Frequency** |
|---------------|-----------------|---------------------|---------------------|-----------------|---------------------|
| Liquidity Crisis | [LIQ_TEAM] | [LIQ_COMM] | [LIQ_DECISION] | [LIQ_RECOVERY] | [LIQ_TEST] |
| Credit Event | [CREDIT_TEAM] | [CREDIT_COMM] | [CREDIT_DECISION] | [CREDIT_RECOVERY] | [CREDIT_TEST] |
| Market Disruption | [MARKET_TEAM] | [MARKET_COMM] | [MARKET_DECISION] | [MARKET_RECOVERY] | [MARKET_TEST] |
| Operational Failure | [OP_TEAM] | [OP_COMM] | [OP_DECISION] | [OP_RECOVERY] | [OP_TEST] |
| Cyber Attack | [CYBER_TEAM] | [CYBER_COMM] | [CYBER_DECISION] | [CYBER_RECOVERY] | [CYBER_TEST] |
| Regulatory Breach | [REG_TEAM] | [REG_COMM] | [REG_DECISION] | [REG_RECOVERY] | [REG_TEST] |

### 10. Risk Culture & Training

```
Risk Culture Development:
Culture Assessment:
- Risk Awareness: [AWARENESS_SCORE]/10
- Accountability: [ACCOUNTABILITY]/10
- Transparency: [TRANSPARENCY]/10
- Challenge Culture: [CHALLENGE]/10
- Learning Orientation: [LEARNING]/10

Training Programs:
- Board Training: [BOARD_TRAINING]
- Executive Training: [EXEC_TRAINING]
- Risk Professional: [PROF_TRAINING]
- Business Training: [BUS_TRAINING]
- New Employee: [NEW_TRAINING]

### Performance Management
- Risk KPIs in Goals: [KPI_INTEGRATION]%
- Risk-Adjusted Comp: [RISK_COMP]
- Consequence Mgmt: [CONSEQUENCE]
- Recognition Program: [RECOGNITION]
- Career Development: [CAREER_DEV]

### Communication
- Risk Committees: [COMMITTEE_COMM]
- Town Halls: [TOWNHALL_FREQ]
- Risk Newsletter: [NEWSLETTER]
- Intranet Updates: [INTRANET]
- Training Materials: [MATERIALS]
```

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
### Example 1: Global Bank
```
Institution: Universal bank
Assets: $2 trillion
Risk Profile: Moderate
Regulatory: Basel III Advanced
Capital Ratio: 13.5% CET1
Technology: Integrated GRC platform
Stress Testing: CCAR/DFAST compliant
Risk Culture: Mature embedded
```

### Example 2: Regional Bank
```
Institution: Commercial bank
Assets: $50 billion
Focus: Credit and operational risk
Regulatory: Standardized approach
Capital Planning: ICAAP process
Technology: Risk data mart
Monitoring: Quarterly dashboards
Training: Annual certification
```

### Example 3: Investment Firm
```
Institution: Broker-dealer
Assets: $10 billion AUM
Focus: Market and liquidity risk
VaR Limit: $50 million
Systems: Real-time risk analytics
Hedging: Dynamic strategies
Compliance: SEC/FINRA
Reporting: Daily risk reports
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Investment Portfolio Management](investment-portfolio-management.md)** - Complementary approaches and methodologies
- **[Digital Banking Strategy](digital-banking-strategy.md)** - Strategic planning and execution frameworks
- **[Risk Management Framework](risk-management-framework.md)** - Identify, assess, and mitigate potential risks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Enterprise Risk Management (ERM) Framework)
2. Use [Investment Portfolio Management](investment-portfolio-management.md) for deeper analysis
3. Apply [Digital Banking Strategy](digital-banking-strategy.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[finance/Risk Management](../../finance/Risk Management/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive framework for implementing enterprise risk management including risk identification, assessment, mitigation strategies, regulatory compliance, and governance structures for financial institutions.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Customization Options

### 1. Institution Type
- Commercial Bank
- Investment Bank
- Asset Manager
- Insurance Company
- Fintech

### 2. Regulatory Regime
- Basel III/IV
- Dodd-Frank
- MiFID II
- Solvency II
- Local Regulations

### 3. Risk Profile
- Conservative
- Moderate
- Aggressive
- Specialized
- Emerging

### 4. Geographic Scope
- Domestic
- Regional
- International
- Global
- Cross-Border

### 5. Maturity Level
- Basic Compliance
- Developing
- Established
- Advanced
- Leading Practice