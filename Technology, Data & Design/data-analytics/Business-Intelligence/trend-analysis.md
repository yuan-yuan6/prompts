---
title: Trend Analysis & Forecasting Assessment
category: data-analytics
tags:
- business-intelligence
- trend-analysis
- forecasting
- anomaly-detection
- time-series
use_cases:
- Evaluating forecasting capability maturity
- Identifying gaps in trend analysis methodologies
- Assessing anomaly detection and monitoring readiness
- Creating predictive analytics roadmaps
related_templates:
- data-analytics/Business-Intelligence/dashboard-data-architecture.md
- data-analytics/Business-Intelligence/dashboard-strategy-requirements.md
industries:
- finance
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: trend-analysis
---

# Trend Analysis & Forecasting Assessment

## Purpose
Comprehensively assess trend analysis and forecasting capabilities across six dimensions: Data Foundation, Pattern Recognition, Forecasting Methods, Anomaly Detection, Model Validation, and Business Integration. This framework identifies methodology gaps, evaluates predictive accuracy, and creates roadmaps for analytics maturity.

## 🚀 Quick Assessment Prompt

> Assess **forecasting readiness** for **[ORGANIZATION]** analyzing **[METRICS/KPIs]** over **[TIME HORIZON]**. Evaluate across: (1) **Data foundation**—is historical data complete, clean, and sufficient for pattern detection? What's the data quality and refresh frequency? (2) **Pattern recognition**—can you identify trends, seasonality, and cycles? Are structural breaks detected? (3) **Forecasting methods**—what techniques are used (moving averages, exponential smoothing, ARIMA, ML)? Are they appropriate for data characteristics? (4) **Anomaly detection**—can you identify outliers, level shifts, and unexpected patterns? Are alerts configured? (5) **Model validation**—how is forecast accuracy measured? What error metrics and backtesting exist? Provide a maturity scorecard (1-5 per dimension), gap analysis, method recommendations, and 90-day capability roadmap.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid forecasting capability evaluation.

---

## Template

Conduct a comprehensive trend analysis and forecasting assessment for {ORGANIZATION_CONTEXT}, analyzing {FORECASTING_SCOPE} to support {BUSINESS_DECISIONS}.

**1. Data Foundation Readiness**

Assess the quality and completeness of historical data supporting forecasting. Evaluate data availability including length of history, granularity levels, and coverage across relevant dimensions such as products, regions, and channels. Examine data quality across completeness, accuracy, consistency, and timeliness dimensions. Review data preparation practices including cleansing procedures, outlier treatment approaches, and missing value handling strategies. Analyze data integration assessing whether relevant external factors like economic indicators, competitive data, and weather are incorporated. Assess data refresh frequency and latency determining whether data arrives with sufficient timeliness for forecasting needs. Evaluate data governance including documentation of definitions, lineage tracking, and quality monitoring.

**2. Pattern Recognition Readiness**

Evaluate capabilities for identifying underlying patterns in time series data. Assess trend identification including detection of linear, exponential, and structural trends with appropriate statistical methods. Examine seasonality analysis including identification of annual, quarterly, monthly, weekly, and daily patterns with proper decomposition techniques. Review cyclical pattern detection for longer-term business cycles distinct from seasonal effects. Analyze structural break identification for regime changes, level shifts, and trend inflection points. Evaluate correlation analysis including lead-lag relationships between related metrics and potential causal factors. Assess visualization capabilities for pattern exploration including time series plots, decomposition charts, and autocorrelation displays.

**3. Forecasting Methods Readiness**

Assess the sophistication and appropriateness of forecasting techniques. Evaluate statistical methods including moving averages, exponential smoothing variants, and ARIMA family models. Examine regression-based approaches including dynamic regression with external regressors. Review machine learning methods including tree-based models, neural networks, and ensemble techniques where appropriate for data characteristics. Analyze method selection criteria determining how techniques are matched to data patterns, forecast horizons, and accuracy requirements. Assess ensemble and combination approaches that leverage multiple models for improved accuracy. Evaluate automation capabilities including automatic model selection, hyperparameter tuning, and pipeline orchestration.

**4. Anomaly Detection Readiness**

Evaluate capabilities for identifying unusual patterns and outliers. Assess statistical anomaly detection including z-score methods, interquartile range approaches, and formal outlier tests. Examine time series specific detection including identification of additive outliers, level shifts, and temporary changes. Review real-time monitoring capabilities including control charts, threshold alerts, and sequential detection. Analyze machine learning anomaly detection including isolation forests, autoencoders, and density-based methods where applicable. Assess alert configuration including severity classification, notification routing, and escalation procedures. Evaluate root cause analysis capabilities for investigating detected anomalies.

**5. Model Validation Readiness**

Assess forecast accuracy measurement and model governance practices. Evaluate error metrics including MAE, RMSE, MAPE, and directional accuracy measures appropriate for business context. Examine backtesting practices including walk-forward validation, holdout testing, and out-of-sample evaluation. Review model comparison frameworks including statistical tests for forecast comparison and information criteria. Analyze uncertainty quantification including prediction intervals, confidence levels, and scenario analysis. Assess model monitoring for production forecasts including drift detection and accuracy degradation alerts. Evaluate documentation practices including model cards, assumption documentation, and limitation disclosure.

**6. Business Integration Readiness**

Evaluate how forecasting capabilities connect to business decisions. Assess decision mapping determining which business processes consume forecasts and what accuracy levels they require. Examine stakeholder communication including forecast presentation, uncertainty explanation, and assumption transparency. Review planning integration including how forecasts feed into budgeting, resource allocation, and strategic planning cycles. Analyze feedback loops capturing whether forecast consumers report on decision outcomes and forecast utility. Assess scenario planning capabilities for what-if analysis, sensitivity testing, and contingency planning. Evaluate continuous improvement processes for systematic accuracy tracking and methodology refinement.

Deliver your assessment as:

1. **Executive Summary** providing overall forecasting maturity score, key capability strengths, critical gaps, and recommended investment priorities.

2. **Dimension Scorecard** presenting a table with maturity score from one to five and key findings for each of the six assessment dimensions.

3. **Method Recommendations** mapping data characteristics to appropriate forecasting techniques with rationale for selection.

4. **Accuracy Baseline** establishing current forecast accuracy by metric and horizon with targets for improvement.

5. **Capability Roadmap** providing phased improvements: quick wins within thirty days, method enhancements within sixty days, and advanced capabilities within ninety days.

6. **Success Metrics** defining accuracy targets, detection rates, and business impact measures with measurement approach.

Use this maturity scale: 1.0-1.9 Initial with ad-hoc forecasting and no systematic methods, 2.0-2.9 Developing with basic techniques but limited validation, 3.0-3.9 Defined with solid methodology and regular accuracy tracking, 4.0-4.9 Managed with advanced methods and automated pipelines, 5.0 Optimized with ML-enhanced forecasting and continuous improvement.

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{ORGANIZATION_CONTEXT}` | Organization type, industry, and forecasting maturity | "mid-market retail company with 200 stores, currently using spreadsheet-based forecasting" |
| `{FORECASTING_SCOPE}` | Metrics being forecast and time horizons | "weekly sales by store and category with 13-week forecast horizon, plus monthly demand for inventory planning" |
| `{BUSINESS_DECISIONS}` | Decisions supported by forecasts | "inventory replenishment, staffing schedules, promotional planning, and annual budget development" |

---

## Usage Examples

**Example 1: Retail Demand Forecasting**

Conduct a comprehensive trend analysis and forecasting assessment for a mid-market retail company with two hundred stores and five years of transaction history, analyzing weekly sales by store, category, and SKU with thirteen-week rolling forecasts and monthly aggregate projections, to support inventory replenishment decisions, staffing optimization, promotional effectiveness measurement, and annual budget planning. The assessment should address seasonal pattern detection for holiday and back-to-school periods, promotional lift modeling, new store forecasting without history, anomaly detection for stockouts and demand spikes, and forecast accuracy targets by planning horizon.

**Example 2: Financial Revenue Forecasting**

Conduct a comprehensive trend analysis and forecasting assessment for a B2B SaaS company with fifty million ARR and three years of subscription data, analyzing monthly recurring revenue, expansion, contraction, and churn with twelve-month rolling forecasts at customer cohort and segment levels, to support board reporting, sales capacity planning, cash flow management, and investor communications. The assessment should address cohort-based revenue modeling, leading indicator correlation with pipeline and usage metrics, scenario analysis for best and worst case projections, anomaly detection for unusual churn patterns, and confidence interval communication to stakeholders.

**Example 3: Manufacturing Production Forecasting**

Conduct a comprehensive trend analysis and forecasting assessment for an industrial manufacturer with four production facilities and ten years of operational history, analyzing daily production volumes, equipment utilization, and quality metrics with thirty-day operational forecasts and quarterly capacity projections, to support production scheduling, maintenance planning, workforce allocation, and capital investment decisions. The assessment should address cyclical demand patterns, equipment degradation trends, seasonal maintenance impacts, anomaly detection for quality deviations and equipment failures, and integration with supply chain planning systems.

---

## Cross-References

- **Dashboard Data Architecture** for data pipeline design supporting forecasting
- **Dashboard Strategy & Requirements** for KPI definitions and business context
- **Dashboard Technical Implementation** for platform capabilities and automation
