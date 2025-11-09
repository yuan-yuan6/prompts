---
title: Risk Assessment, Quantification & Credit Risk Management
category: finance
tags: [design, finance, framework, machine-learning, management]
use_cases:
  - Measuring and quantifying risks covering credit risk framework, modeling, portfolio management, and market risk
  - Strategy development
last_updated: 2025-11-09
related_templates:
  - risk-management-overview.md
---

# Risk Assessment, Quantification & Credit Risk Management

## Purpose
Design comprehensive risk assessment frameworks covering credit risk management, measurement, modeling, and market risk quantification.

## Template

```
You are a quantitative risk specialist. Create detailed risk assessment framework based on:

Risk Context:
- Primary Risks: [CREDIT_MARKET_OPERATIONAL_CATEGORIES]
- Risk Appetite: [CONSERVATIVE_MODERATE_AGGRESSIVE_STANCE]
- Modeling Capabilities: [QUANTITATIVE_ANALYTICS_MATURITY]
- Regulatory Requirements: [BASEL_DODD_FRANK_REGULATIONS]

Generate comprehensive risk assessment covering:

## 2. CREDIT RISK MANAGEMENT

### 2.1 Credit Risk Framework and Policies
- Credit risk strategy and appetite
- Target customer segments and markets
- Geographic and industry concentration strategy
- Credit quality and rating distribution targets
- Portfolio growth and diversification
- Credit policy and underwriting standards
- Credit application and documentation requirements
- Financial analysis and cash flow evaluation
- Collateral valuation and security assessment
- Credit decision and approval process
- Credit authority and delegation framework

### 2.2 Credit Risk Measurement and Modeling
- Internal rating system development
- Borrower and facility rating methodology
- Financial and qualitative factor integration
- Credit scoring and automated decision systems
- Application and behavioral scoring models
- Machine learning and advanced analytics
- Loss forecasting and provisioning
- Expected credit loss modeling (CECL, IFRS 9)
- Probability of default calibration
- Loss given default and recovery analysis
- Stress testing and scenario analysis
- Macroeconomic scenario development
- Portfolio stress testing and impact

### 2.3 Portfolio Management and Monitoring
- Portfolio performance and quality metrics
- Delinquency and non-performing loan tracking
- Charge-off and recovery rate analysis
- Provision expense and reserve coverage
- Concentration and diversification monitoring
- Credit risk dashboard and visualization
- Problem asset management and workout
- Early warning and intervention systems
- Collections and recovery management

## 3. MARKET RISK MANAGEMENT

### 3.1 Market Risk Framework and Governance
- Trading and investment strategy
- Trading book vs. banking book
- Market making and proprietary trading
- Market risk appetite and limits
- Value-at-Risk and sensitivity limits
- Position and concentration limits
- Loss limits and stop-loss triggers

### 3.2 Market Risk Measurement and Modeling
- Value-at-Risk methodologies
- Historical simulation and parametric VaR
- Monte Carlo simulation
- Expected shortfall and tail risk
- Interest rate risk modeling
- Asset and liability modeling
- Duration and convexity analysis
- Prepayment and option risk

### 3.3 Trading Risk Management
- Front office risk management
- Real-time position and P&L monitoring
- Independent price verification
- Derivative and complex instrument risk
- Counterparty credit risk
- Collateral management
- Model risk and valuation uncertainty
```

## Variables
- `[CREDIT_MARKET_OPERATIONAL_CATEGORIES]`: Primary risks
- `[CONSERVATIVE_MODERATE_AGGRESSIVE_STANCE]`: Risk appetite
- `[QUANTITATIVE_ANALYTICS_MATURITY]`: Modeling capabilities
- `[BASEL_DODD_FRANK_REGULATIONS]`: Regulatory requirements

## Best Practices
1. **Model rigorously** - Use validated quantitative models
2. **Test extensively** - Back-test and stress test models
3. **Monitor continuously** - Track portfolio performance
4. **Diversify appropriately** - Manage concentration risk
5. **Price for risk** - Risk-adjusted pricing and returns
