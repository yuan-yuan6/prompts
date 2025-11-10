---
title: Financial Ratio Analysis
category: business/Finance & Accounting
tags: [business, finance, ratios, performance-metrics, benchmarking]
use_cases:
  - Analyze a company's financial health using key ratios (30-45 min task)
  - Benchmark company performance against industry peers
  - Prepare executive summary of financial position for board presentation
related_templates:
  - financial-statement-analysis.md
  - financial-forecasting.md
  - financial-valuation-recommendations.md
last_updated: 2025-11-09
---

# Financial Ratio Analysis

## Purpose
Calculate and interpret key financial ratios to evaluate company performance across liquidity, efficiency, leverage, profitability, and market valuation dimensions.

## Quick Start

**For Financial Analysts & CFOs**: Calculate key financial ratios and generate performance benchmarking reports in 30-45 minutes.

**Common Business Scenarios:**
- **Board Presentation**: Analyze company financial health using 15-20 key ratios, compare to 3-5 industry peers, identify top 3 strengths and concerns
- **Credit Review**: Evaluate liquidity (current ratio, quick ratio, cash ratio) and leverage ratios (debt/equity, interest coverage) for lending decisions
- **Investment Analysis**: Calculate profitability ratios (ROE, ROA, margins) and efficiency metrics (inventory turnover, asset turnover) to assess company performance
- **M&A Due Diligence**: Comprehensive ratio analysis across all categories to evaluate acquisition targets
- **Performance Monitoring**: Quarterly ratio tracking with trend analysis to identify operational improvements

**What You'll Need:**
- Recent financial statements (balance sheet, income statement, cash flow)
- Industry benchmark data for 3-5 comparable companies
- Prior period data for trend analysis

**You'll Get:**
- Calculated ratios across 5 categories (liquidity, efficiency, leverage, profitability, market)
- Comparison to industry benchmarks
- Visual scorecard with ratings
- Top 3 strengths and concerns
- Actionable recommendations

## Template

```
You are a financial analyst specializing in ratio analysis and performance benchmarking. Calculate and interpret key financial ratios based on the following data:

Company Information:
- Company Name: [COMPANY_NAME]
- Industry: [INDUSTRY_SECTOR]
- Analysis Period: [ANALYSIS_PERIOD]

Financial Data:
- Revenue: [REVENUE]
- Gross Profit: [GROSS_PROFIT]
- Operating Income: [OPERATING_INCOME]
- Net Income: [NET_INCOME]
- Total Assets: [TOTAL_ASSETS]
- Current Assets: [CURRENT_ASSETS]
- Cash: [CASH]
- Inventory: [INVENTORY]
- Accounts Receivable: [AR]
- Current Liabilities: [CURRENT_LIABILITIES]
- Total Liabilities: [TOTAL_LIABILITIES]
- Total Debt: [TOTAL_DEBT]
- Shareholders' Equity: [EQUITY]
- Interest Expense: [INTEREST_EXPENSE]
- Cost of Goods Sold: [COGS]

Industry Benchmarks (if available):
- Industry Average Current Ratio: [INDUSTRY_CR]
- Industry Average ROE: [INDUSTRY_ROE]
- Industry Average Debt/Equity: [INDUSTRY_DE]

## 1. LIQUIDITY RATIOS

### Current Ratio
**Formula:** Current Assets ÷ Current Liabilities

Calculate and interpret:
- Current ratio value
- Comparison to industry standard (typically 1.5-3.0)
- Trend vs. prior periods
- Assessment: Does the company have sufficient liquid assets to cover short-term obligations?
- Red flags: Ratio < 1.0 indicates potential liquidity stress

### Quick Ratio (Acid-Test)
**Formula:** (Current Assets - Inventory) ÷ Current Liabilities

Calculate and interpret:
- Quick ratio value
- Comparison to industry standard (typically 1.0-2.0)
- More conservative liquidity measure
- Assessment: Can the company meet obligations without selling inventory?
- Red flags: Ratio < 0.8 indicates immediate liquidity concerns

### Cash Ratio
**Formula:** Cash ÷ Current Liabilities

Calculate and interpret:
- Cash ratio value
- Ultimate liquidity test
- Emergency liquidity capacity
- Assessment: What portion of current liabilities can be paid immediately?
- Target: Minimum 0.2-0.5 for most industries

**Liquidity Summary:**
- Overall liquidity position (Strong/Adequate/Weak)
- Seasonal considerations
- Working capital adequacy
- Immediate risks or concerns

## 2. EFFICIENCY RATIOS

### Inventory Turnover
**Formula:** Cost of Goods Sold ÷ Average Inventory

Calculate and interpret:
- Inventory turnover ratio
- Days in inventory: 365 ÷ Inventory Turnover
- Comparison to industry benchmark
- Assessment: How efficiently is inventory managed?
- Higher = better (but watch for stockouts)
- Industry-specific norms vary widely

### Accounts Receivable Turnover
**Formula:** Revenue ÷ Average Accounts Receivable

Calculate and interpret:
- AR turnover ratio
- Days sales outstanding (DSO): 365 ÷ AR Turnover
- Comparison to credit terms offered
- Assessment: How efficiently are receivables collected?
- Lower DSO = faster collection = better cash flow

### Total Asset Turnover
**Formula:** Revenue ÷ Total Assets

Calculate and interpret:
- Asset turnover ratio
- Revenue generated per dollar of assets
- Comparison to industry (varies by industry)
- Assessment: How productively are assets utilized?
- Capital-intensive industries typically have lower ratios

### Cash Conversion Cycle
**Formula:** Days Inventory + DSO - Days Payable Outstanding

Calculate and interpret:
- Cash conversion cycle (days)
- Time from cash outlay to cash collection
- Shorter cycle = more efficient working capital
- Assessment: How quickly does the company convert operations to cash?
- Opportunities for improvement

**Efficiency Summary:**
- Overall operating efficiency (Excellent/Good/Needs Improvement)
- Working capital management effectiveness
- Key improvement opportunities

## 3. LEVERAGE RATIOS

### Debt-to-Equity Ratio
**Formula:** Total Debt ÷ Shareholders' Equity

Calculate and interpret:
- Debt-to-equity ratio
- Capital structure assessment
- Comparison to industry average
- Assessment: Is leverage excessive or conservative?
- High ratio = higher financial risk
- Industry context matters (utilities vs. tech)

### Debt-to-Assets Ratio
**Formula:** Total Debt ÷ Total Assets

Calculate and interpret:
- Debt-to-assets ratio
- Percentage of assets financed by debt
- Assessment: What portion of assets are debt-financed?
- Target: Typically < 0.6 for most industries
- Higher ratio = less financial flexibility

### Interest Coverage Ratio
**Formula:** Operating Income ÷ Interest Expense

Calculate and interpret:
- Interest coverage ratio
- Debt service capability
- Assessment: How many times can the company cover interest payments?
- Minimum acceptable: 2.5-3.0
- Below 1.5 = financial distress warning
- Higher = better debt service capacity

**Leverage Summary:**
- Overall leverage assessment (Conservative/Moderate/Aggressive)
- Financial risk level
- Debt capacity remaining
- Credit rating implications

## 4. PROFITABILITY RATIOS

### Gross Profit Margin
**Formula:** (Gross Profit ÷ Revenue) × 100

Calculate and interpret:
- Gross margin percentage
- Comparison to industry and competitors
- Trend analysis
- Assessment: How profitable are core operations?
- Higher margins indicate pricing power or cost advantage

### Operating Profit Margin
**Formula:** (Operating Income ÷ Revenue) × 100

Calculate and interpret:
- Operating margin percentage
- Comparison to industry benchmark
- Trend vs. prior periods
- Assessment: How efficiently is the business operated?
- Reflects operational excellence

### Net Profit Margin
**Formula:** (Net Income ÷ Revenue) × 100

Calculate and interpret:
- Net margin percentage
- Bottom-line profitability
- Comparison to peers
- Assessment: What percentage of revenue becomes profit?
- Consider tax and interest impacts

### Return on Assets (ROA)
**Formula:** (Net Income ÷ Total Assets) × 100

Calculate and interpret:
- ROA percentage
- Asset productivity measure
- Comparison to industry
- Assessment: How effectively do assets generate profit?
- Higher = better asset utilization

### Return on Equity (ROE)
**Formula:** (Net Income ÷ Shareholders' Equity) × 100

Calculate and interpret:
- ROE percentage
- Shareholder value creation measure
- Comparison to cost of equity and industry
- Assessment: What return do shareholders earn on their investment?
- Target: > 15% is generally strong

### DuPont Analysis
**Formula:** ROE = Net Margin × Asset Turnover × Equity Multiplier

Break down ROE into:
- Profit margin component
- Asset turnover component
- Leverage component
- Identify which factors drive ROE
- Determine focus areas for improvement

**Profitability Summary:**
- Overall profitability assessment (Excellent/Good/Fair/Poor)
- Margin trends and drivers
- Competitive profitability position
- Improvement priorities

## 5. COMPREHENSIVE RATIO SCORECARD

Create a scorecard showing:
- All calculated ratios
- Industry benchmarks
- Prior period comparison
- Rating for each category (1-5 stars)
- Overall financial health score

### Key Findings
- Top 3 ratio strengths
- Top 3 ratio concerns
- Critical trends
- Comparison to best-in-class performers

### Recommendations
- Priority improvement areas
- Specific ratio targets
- Action items to improve weak ratios
```

## Variables
- `[COMPANY_NAME]`: Company name
- `[INDUSTRY_SECTOR]`: Industry classification
- `[ANALYSIS_PERIOD]`: Period analyzed
- `[REVENUE]`: Total revenue
- `[GROSS_PROFIT]`: Gross profit
- `[OPERATING_INCOME]`: Operating income
- `[NET_INCOME]`: Net income
- `[TOTAL_ASSETS]`: Total assets
- `[CURRENT_ASSETS]`: Current assets
- `[CASH]`: Cash and equivalents
- `[INVENTORY]`: Inventory balance
- `[AR]`: Accounts receivable
- `[CURRENT_LIABILITIES]`: Current liabilities
- `[TOTAL_LIABILITIES]`: Total liabilities
- `[TOTAL_DEBT]`: Total debt
- `[EQUITY]`: Shareholders' equity
- `[INTEREST_EXPENSE]`: Interest expense
- `[COGS]`: Cost of goods sold
- `[INDUSTRY_*]`: Industry benchmarks

## Usage Example

**Input:**
- Company: RetailCo
- Revenue: $500M
- Current Assets: $120M
- Current Liabilities: $60M
- Inventory: $40M
- Total Assets: $300M
- Total Debt: $100M
- Equity: $150M
- Net Income: $25M

**Output will calculate:**
- Current Ratio: 2.0 (Strong)
- Quick Ratio: 1.33 (Adequate)
- Debt/Equity: 0.67 (Moderate)
- ROE: 16.7% (Good)
- Net Margin: 5.0%

## Best Practices
- **Compare to industry peers, not just benchmarks** - Look at 3-5 direct competitors for realistic context
- **Focus on ratio trends over time** - A declining current ratio from 2.5 to 1.8 matters more than the absolute number
- **Investigate unusual ratios immediately** - If ROE is 5% in an industry averaging 15%, understand why before presenting
- **Adjust for one-time events** - Remove impact of asset sales, restructuring charges before calculating margins
- **Cluster analysis first** - Group liquidity, profitability, efficiency, and leverage ratios to tell a coherent story
