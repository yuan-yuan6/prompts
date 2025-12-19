---
category: data-analytics
description: Analyze sentiment, emotions, and opinions in text using rule-based, ML, and transformer approaches with aspect-level and temporal analysis
title: Text Analytics - Sentiment Analysis
tags:
- sentiment-analysis
- opinion-mining
- emotion-detection
- text-analytics
use_cases:
- Analyzing customer review sentiment to identify satisfaction drivers and pain points
- Monitoring brand sentiment across social media and news sources
- Performing aspect-based sentiment analysis on product features or service attributes
- Tracking sentiment trends over time to detect shifts in public opinion
related_templates:
- data-analytics/Research-Analytics/text-analytics-preprocessing.md
- data-analytics/Research-Analytics/text-analytics-topic-modeling.md
- data-analytics/Research-Analytics/text-analytics-entity-recognition.md
- data-analytics/Research-Analytics/text-analytics-overview.md
industries:
- retail
- technology
- finance
- healthcare
- hospitality
type: framework
difficulty: intermediate
slug: text-analytics-sentiment-analysis
---

# Text Analytics - Sentiment Analysis

## Purpose
Conduct comprehensive sentiment analysis using multiple methods including rule-based (VADER, TextBlob), machine learning, and transformer-based deep learning models. Analyze overall sentiment, aspect-level opinions, emotions, and sentiment trends over time to extract actionable insights from text data.

## 🚀 Quick Start Prompt

> Analyze **sentiment** in **[TEXT DATA]** to understand **[ANALYSIS GOALS]**. Cover: (1) **Overall sentiment**—classify as positive/neutral/negative using multiple models (VADER for speed, transformers for accuracy); (2) **Aspect-based sentiment**—analyze opinions about specific attributes like quality, price, service; (3) **Emotion detection**—identify emotions beyond polarity (joy, anger, frustration, surprise); (4) **Temporal trends**—track sentiment changes over time. Deliver sentiment distribution, aspect scores with example quotes, emotion breakdown, trend visualization, and actionable recommendations.

---

## Template

Conduct comprehensive sentiment analysis on {TEXT_DATA_DESCRIPTION}, focusing on {ANALYSIS_OBJECTIVES} to support {BUSINESS_CONTEXT}.

**1. Sentiment Method Selection and Configuration**

Choose appropriate sentiment analysis methods based on your data characteristics and accuracy requirements. Rule-based methods like VADER excel at social media text with emojis, slang, and informal language, providing fast processing without training data. TextBlob offers simple polarity and subjectivity scores suitable for general text. Transformer models like RoBERTa and BERT provide superior accuracy on nuanced text but require more compute. Domain-specific models like FinBERT for financial text or BioBERT for biomedical content capture specialized vocabulary sentiment. Consider ensemble approaches combining multiple methods—use rule-based for initial filtering and transformers for final classification. Configure sentiment thresholds appropriate to your data; typical boundaries are compound scores above 0.05 for positive, below -0.05 for negative.

**2. Overall Sentiment Classification**

Apply sentiment classification to each document in your corpus. For rule-based analysis, calculate compound scores combining positive, negative, and neutral components, accounting for punctuation emphasis (!! increases intensity), capitalization (ALL CAPS signals emphasis), and negation handling (not good reverses polarity). For transformer models, extract predicted labels with confidence scores, flagging low-confidence predictions for review. Compare results across methods to identify disagreements indicating ambiguous or nuanced sentiment. Aggregate document-level results to corpus-level statistics—calculate the percentage distribution across positive, neutral, and negative categories, mean sentiment scores with standard deviations, and confidence-weighted averages.

**3. Aspect-Based Sentiment Analysis**

Move beyond overall sentiment to understand opinions about specific attributes. Define relevant aspects for your domain—product reviews might include quality, price, shipping, and customer service; employee surveys might cover compensation, management, work-life balance, and career growth. Extract aspect mentions using keyword matching, dependency parsing, or trained aspect extractors. For each aspect mention, analyze sentiment of the containing sentence or clause rather than the full document. Handle implicit aspects where sentiment is expressed without explicit mention (e.g., "too expensive" implies negative price sentiment). Aggregate aspect-level sentiment across documents to identify strengths and weaknesses, ranking aspects by sentiment gap from neutral or from competitors.

**4. Emotion Detection and Analysis**

Extend beyond positive/negative polarity to identify specific emotions. Apply emotion classification models that detect categories such as joy, anger, sadness, fear, surprise, and disgust. Note that multiple emotions can co-occur—a review might express both joy about product quality and frustration about shipping delays. Calculate emotion intensity scores when available, distinguishing mild annoyance from rage. Map emotions to business-relevant categories—anger and frustration often indicate service failures requiring immediate attention, while surprise might signal unexpected delight or disappointment. Analyze emotion distribution across your corpus and identify which aspects or topics trigger which emotions.

**5. Sentiment Trend Analysis**

Track sentiment changes over time to detect shifts and patterns. Aggregate sentiment scores by time period—hourly for social media monitoring, daily or weekly for reviews, monthly or quarterly for surveys. Calculate moving averages to smooth noise and reveal underlying trends. Detect significant shifts using change point detection or threshold-based alerting. Correlate sentiment changes with external events—product launches, marketing campaigns, PR incidents, or competitor actions. Analyze seasonal patterns if your domain has cyclical behavior. Visualize trends with time series charts showing sentiment scores, volume, and key events annotated.

**6. Handling Sentiment Challenges**

Address common sentiment analysis challenges that affect accuracy. Handle negation carefully—"not bad" and "not good" require special processing that many models miss. Detect sarcasm and irony which reverse literal sentiment; flag text with sarcasm indicators for manual review if high accuracy is critical. Account for comparative sentiment where text compares entities ("better than competitor" is positive for you, negative for them). Process mixed sentiment where documents contain both positive and negative opinions about different aspects. Handle neutral text appropriately—distinguish genuinely neutral opinions from factual statements lacking sentiment. Consider cultural and demographic factors that affect expression style and intensity.

**7. Validation and Quality Assessment**

Validate sentiment results to ensure reliability before acting on insights. Sample predictions across sentiment categories and confidence levels, comparing to human judgment. Calculate agreement metrics between model predictions and human labels—target at least 80% accuracy for business decisions. Analyze disagreement patterns to identify systematic errors or edge cases. Compare multiple model outputs to identify unreliable predictions where models disagree. Assess model calibration—do confidence scores reflect actual accuracy? Track performance over time as language evolves and new expressions emerge. Document known limitations and edge cases where the model performs poorly.

**8. Actionable Insights and Recommendations**

Transform sentiment analysis into business value. Identify top drivers of positive and negative sentiment through aspect analysis—what makes customers happy or unhappy? Extract representative quotes that illustrate key themes for stakeholder communication. Prioritize issues by combining sentiment negativity with mention volume—frequent complaints matter more than rare ones. Compare sentiment across segments (customer types, products, regions, time periods) to identify patterns. Generate alerts for sentiment spikes or drops requiring immediate attention. Create sentiment dashboards with key metrics, trends, and drill-down capabilities. Formulate specific recommendations tied to sentiment insights with expected impact.

Deliver your sentiment analysis as:

1. **Sentiment distribution** showing percentage breakdown across positive, neutral, negative with confidence intervals
2. **Method comparison** showing agreement and disagreement across sentiment models used
3. **Aspect-level analysis** with sentiment scores, rankings, and representative quotes per aspect
4. **Emotion breakdown** showing distribution and intensity of detected emotions
5. **Temporal trends** with visualizations, significant shifts, and event correlations
6. **Quality metrics** including accuracy validation, model agreement, and known limitations
7. **Key drivers** identifying top positive and negative sentiment factors
8. **Recommendations** with prioritized actions based on sentiment insights

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{TEXT_DATA_DESCRIPTION}` | Source, volume, and characteristics of text | "15,000 product reviews from Q4 2024 across electronics and home categories" |
| `{ANALYSIS_OBJECTIVES}` | Specific sentiment analysis goals | "understand customer satisfaction drivers, identify quality issues, track sentiment trends" |
| `{BUSINESS_CONTEXT}` | How insights will inform decisions | "product improvement roadmap and customer service training priorities" |

---

## Usage Examples

### Example 1: E-commerce Product Review Analysis
**Prompt:** "Conduct comprehensive sentiment analysis on {TEXT_DATA_DESCRIPTION: 25,000 product reviews with 1-5 star ratings from electronics marketplace}, focusing on {ANALYSIS_OBJECTIVES: understanding satisfaction drivers, identifying quality defects, and comparing sentiment across product categories}, to support {BUSINESS_CONTEXT: Q1 product quality improvement initiatives and vendor performance reviews}."

**Expected Output:** Overall sentiment distribution (62% positive, 18% neutral, 20% negative), aspect-level analysis showing shipping (3.8/5), product quality (4.1/5), value (3.9/5), customer service (3.2/5) with customer service identified as top improvement area. Emotion analysis revealing frustration concentrated in return/refund discussions. Trend analysis showing 8% sentiment improvement after October fulfillment changes. Top recommendations: improve return process (mentioned in 34% of negative reviews), address specific product defect pattern in Category X.

### Example 2: Social Media Brand Monitoring
**Prompt:** "Conduct comprehensive sentiment analysis on {TEXT_DATA_DESCRIPTION: real-time stream of 5,000 daily social media mentions across Twitter, Instagram, and Reddit}, focusing on {ANALYSIS_OBJECTIVES: monitoring brand perception, detecting emerging issues early, and measuring campaign effectiveness}, to support {BUSINESS_CONTEXT: marketing campaign optimization and reputation management}."

**Expected Output:** Hourly sentiment dashboard with 15-minute alerting for significant drops. Aspect analysis covering product mentions (72% positive), pricing discussions (58% positive), customer service mentions (45% positive). Emotion detection flagging anger spikes correlated with service outage on Tuesday. Campaign sentiment showing new product launch generating 78% positive with "surprise" and "joy" emotions dominant. Competitive comparison showing brand sentiment 12 points higher than primary competitor.

### Example 3: Employee Survey Analysis
**Prompt:** "Conduct comprehensive sentiment analysis on {TEXT_DATA_DESCRIPTION: 3,500 open-ended responses from annual employee engagement survey across 12 departments}, focusing on {ANALYSIS_OBJECTIVES: identifying engagement drivers and detractors, detecting department-level patterns, and tracking year-over-year sentiment changes}, to support {BUSINESS_CONTEXT: HR strategy development and manager coaching priorities}."

**Expected Output:** Overall engagement sentiment at 3.4/5 (up 0.2 from prior year). Aspect analysis showing career development (2.9/5), compensation (3.1/5), work-life balance (3.6/5), manager relationship (3.8/5), company direction (3.5/5). Department comparison identifying Engineering (3.8) and Sales (2.9) as highest and lowest. Emotion analysis showing frustration concentrated in promotion discussions, pride in company mission mentions. Year-over-year improvement in remote work sentiment. Priority recommendations: address career pathing concerns (top driver of negative sentiment), focus manager coaching in Sales and Operations.

---

## Cross-References

- [text-analytics-preprocessing.md](text-analytics-preprocessing.md) - Text cleaning and preparation for sentiment analysis
- [text-analytics-topic-modeling.md](text-analytics-topic-modeling.md) - Combine sentiment with topic discovery
- [text-analytics-entity-recognition.md](text-analytics-entity-recognition.md) - Entity-level sentiment analysis
- [text-analytics-overview.md](text-analytics-overview.md) - Guide to text analytics technique selection
