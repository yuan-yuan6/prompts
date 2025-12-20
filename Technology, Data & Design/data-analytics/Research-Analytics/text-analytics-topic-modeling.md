---
category: data-analytics
description: Discover latent topics in document collections using LDA, BERTopic, NMF, and hierarchical methods with evaluation and temporal tracking
title: Text Analytics - Topic Modeling
tags:
- topic-modeling
- lda
- bertopic
- text-analytics
use_cases:
- Discovering themes and topics in large document collections
- Tracking topic evolution over time in dynamic datasets
- Organizing unstructured content libraries into coherent categories
- Identifying emerging trends and declining themes in text corpora
related_templates:
- data-analytics/Research-Analytics/text-analytics-preprocessing.md
- data-analytics/Research-Analytics/text-analytics-sentiment-analysis.md
- data-analytics/Research-Analytics/text-analytics-entity-recognition.md
- data-analytics/Research-Analytics/text-analytics-overview.md
industries:
- technology
- healthcare
- finance
- media
- research
type: framework
difficulty: intermediate
slug: text-analytics-topic-modeling
---

# Text Analytics - Topic Modeling

## Purpose
Discover and analyze latent topics in document collections using state-of-the-art topic modeling algorithms including LDA, BERTopic, NMF, and Hierarchical Dirichlet Process. Extract interpretable topics, track topic evolution over time, evaluate model quality, and generate visualizations for topic exploration.

## 🚀 Quick Start Prompt

> Discover **topics** in **[DOCUMENT CORPUS]** to understand **[ANALYSIS GOALS]**. Cover: (1) **Topic extraction**—identify 8-15 coherent topics using LDA and/or BERTopic; (2) **Evaluation**—measure coherence scores (target >0.4), assess topic distinctiveness; (3) **Interpretation**—extract top keywords, representative documents, and assign meaningful labels; (4) **Temporal analysis**—track topic evolution if timestamps available. Deliver topic descriptions with keywords, coherence metrics, document assignments, and visualizations.

---

## Template

Conduct topic modeling analysis on {DOCUMENT_CORPUS}, aiming to {ANALYSIS_OBJECTIVES} in support of {BUSINESS_CONTEXT}.

**1. Corpus Preparation and Method Selection**

Prepare your document collection for topic modeling by ensuring consistent preprocessing. Remove noise while preserving semantically meaningful terms—aggressive preprocessing removes signal needed for topic discovery. Filter vocabulary to remove very rare terms (appearing in fewer than 2-3 documents) and very common terms (appearing in more than 90-95% of documents) that don't discriminate between topics. Select the appropriate algorithm based on your data: LDA works well for longer documents and established domains with interpretable probabilistic topics; BERTopic leverages transformer embeddings for superior performance on short texts and diverse domains; NMF provides fast, sparse topics good for interpretability; HDP (Hierarchical Dirichlet Process) automatically determines the number of topics when you don't have a target.

**2. Model Training and Parameter Tuning**

Train topic models with appropriate parameters for your corpus size and complexity. For LDA, start with 10-15 topics and adjust based on coherence evaluation, use alpha='auto' and eta='auto' to let the model learn document-topic and topic-word distributions, and run sufficient passes (20-50) for convergence. For BERTopic, choose a sentence transformer model appropriate to your domain (general-purpose like 'all-MiniLM-L6-v2' or domain-specific), set minimum topic size based on your corpus (larger corpora can support smaller minimum sizes), and consider whether to merge similar topics. For NMF, regularization parameters control topic sparsity. Run multiple models with different random seeds to assess stability—topics that appear consistently across runs are more reliable.

**3. Model Evaluation and Selection**

Evaluate topic quality using multiple metrics to select the optimal model. Calculate coherence scores using C_v coherence (target above 0.4 for interpretable topics) which measures how frequently top words co-occur in the corpus. Compute topic diversity measuring the percentage of unique words across topics—low diversity indicates redundant topics. Assess perplexity as a measure of how well the model predicts held-out documents, though coherence often better predicts human interpretability. Test different numbers of topics plotting coherence against topic count to find the elbow where additional topics provide diminishing returns. Examine topic overlap—if top words repeat across multiple topics, reduce the topic count or adjust parameters.

**4. Topic Interpretation and Labeling**

Transform model outputs into meaningful topic descriptions. Extract the top 15-20 keywords per topic ranked by their probability or weight within that topic. Review keywords for coherence—do they tell a consistent story about a theme? If not, the topic may be too broad or mixing unrelated concepts. Retrieve representative documents for each topic—the 5-10 documents with highest probability assignment to that topic. Read representative documents to validate that keywords accurately capture the theme. Assign human-readable topic labels based on keyword review and representative document examination. Identify any "junk" topics that capture noise, boilerplate, or mixed content rather than coherent themes—these are common and can be excluded from analysis.

**5. Document-Topic Assignment**

Analyze how topics distribute across your document corpus. Assign each document to topics based on probability distributions—documents may belong strongly to one topic or span multiple topics. Calculate dominant topic for each document as the highest-probability topic assignment. Analyze topic proportions across the corpus—which topics are most prevalent and which are niche? Examine documents with high uncertainty (no dominant topic) to understand whether they represent transitional content or model confusion. Cross-tabulate topic assignments with document metadata (source, author, category, date) to identify patterns. Calculate topic co-occurrence to understand which themes frequently appear together in documents.

**6. Temporal Topic Analysis**

Track how topics evolve over time when documents have timestamps. Aggregate topic proportions by time period (daily, weekly, monthly, quarterly) to visualize trends. Identify emerging topics showing increasing prevalence over time and declining topics losing share. Detect topic shifts where the composition of a topic (its characteristic words) changes between time periods. Use dynamic topic models for formal temporal analysis that models how topic word distributions evolve. Correlate topic trends with external events—product launches, news events, seasonal patterns—to understand what drives topic salience. Create topic timeline visualizations showing the rise and fall of different themes.

**7. Visualization and Exploration**

Create visualizations that enable topic exploration and communication. Use pyLDAvis for LDA models to create interactive visualizations showing topic positions, sizes, and word distributions with adjustable relevance metrics. Generate word clouds for each topic with word size proportional to topic weight. Create topic similarity heatmaps showing which topics have overlapping vocabulary. Plot document embeddings in 2D space (t-SNE or UMAP) colored by dominant topic to visualize document clustering. Build topic distribution bar charts showing corpus-wide topic prevalence. Create stacked area charts for temporal topic trends. Design interactive dashboards allowing drill-down from topic overview to representative documents.

**8. Actionable Insights and Applications**

Transform topic analysis into practical value. Identify content themes by mapping discovered topics to business-relevant categories—what are customers talking about, what research themes dominate, what news topics trend? Use topic assignments for document organization, building category taxonomies from bottom-up topic discovery. Enable topic-based document retrieval by finding documents similar to a query based on topic profiles. Inform content strategy by identifying topic gaps (underrepresented themes) and saturated areas (overcrowded topics). Track topic trends for early detection of emerging issues or opportunities. Combine topic analysis with sentiment to understand not just what people discuss but how they feel about each theme.

Deliver your topic modeling analysis as:

1. **Model selection summary** explaining algorithm choice and parameter settings
2. **Evaluation metrics** including coherence scores, perplexity, and topic diversity
3. **Topic catalog** with ID, label, top keywords, and representative document excerpts
4. **Corpus statistics** showing topic distribution and document assignment patterns
5. **Temporal trends** if applicable, with emerging and declining topic identification
6. **Visualizations** including interactive topic explorer, word clouds, and distribution charts
7. **Quality assessment** noting coherent versus problematic topics
8. **Recommendations** for content strategy, organization, or further analysis based on findings

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{DOCUMENT_CORPUS}` | Collection size, source, and characteristics | "5,000 customer support tickets from Q3-Q4 2024" |
| `{ANALYSIS_OBJECTIVES}` | What you want to learn from topic discovery | "identify main support issue categories and track emerging problems" |
| `{BUSINESS_CONTEXT}` | How topic insights will be applied | "support workflow optimization and agent training curriculum design" |

---

## Usage Examples

### Example 1: Customer Feedback Theme Discovery
**Prompt:** "Conduct topic modeling analysis on {DOCUMENT_CORPUS: 20,000 product reviews across 50 product SKUs from e-commerce platform}, aiming to {ANALYSIS_OBJECTIVES: discover main feedback themes, identify product-specific issues, and understand category-level patterns}, in support of {BUSINESS_CONTEXT: product development roadmap prioritization and quality assurance focus areas}."

**Expected Output:** 12 coherent topics identified (shipping/delivery, product quality, value/pricing, customer service, packaging, ease of use, durability, appearance, sizing/fit, features, comparison to alternatives, gift experience) with coherence scores 0.42-0.58. Topic distribution showing quality (18%), shipping (15%), and value (14%) as dominant themes. Product-category cross-tabulation revealing electronics skewed toward features topics while apparel concentrated in sizing. Temporal analysis showing packaging complaints increased 40% post-holiday. Recommendations prioritizing shipping carrier review and size guide improvements.

### Example 2: Research Literature Mapping
**Prompt:** "Conduct topic modeling analysis on {DOCUMENT_CORPUS: 3,000 academic paper abstracts on machine learning applications in healthcare from 2020-2024}, aiming to {ANALYSIS_OBJECTIVES: map the research landscape, identify major research streams, and track emerging subfields}, in support of {BUSINESS_CONTEXT: systematic literature review and research grant proposal development}."

**Expected Output:** 15 topics covering diagnostic imaging, clinical NLP, drug discovery, patient outcome prediction, wearable sensors, genomics, mental health, radiology AI, EHR mining, federated learning, fairness/ethics, clinical trials, surgical robotics, telemedicine, and COVID-19 applications. Coherence scores averaging 0.51. Temporal analysis showing federated learning and fairness/ethics as fastest-growing topics (3x increase 2022-2024), COVID-19 declining from 2023. Citation network overlay identifying seminal papers per topic. Gap analysis revealing limited work on pediatric applications and long-term outcome prediction.

### Example 3: News Media Topic Tracking
**Prompt:** "Conduct topic modeling analysis on {DOCUMENT_CORPUS: 50,000 news articles from 10 major outlets covering technology sector over 12 months}, aiming to {ANALYSIS_OBJECTIVES: identify dominant narratives, track topic trends weekly, and detect emerging stories early}, in support of {BUSINESS_CONTEXT: competitive intelligence and PR strategy development}."

**Expected Output:** 20 topics including AI/LLM developments, big tech regulation, startup funding, cybersecurity incidents, semiconductor supply chain, social media platforms, streaming wars, electric vehicles, fintech, cryptocurrency, remote work, tech layoffs, privacy concerns, antitrust actions, M&A activity, product launches, earnings reports, executive changes, ESG initiatives, and international tech policy. Weekly trend dashboard showing topic velocity and acceleration. Early warning alerts for rapidly rising topics. Outlet comparison showing coverage emphasis differences. Narrative framing analysis for key topics.

---

## Cross-References

- [text-analytics-preprocessing.md](text-analytics-preprocessing.md) - Text preparation for topic modeling
- [text-analytics-sentiment-analysis.md](text-analytics-sentiment-analysis.md) - Combine topics with sentiment for richer insights
- [text-analytics-entity-recognition.md](text-analytics-entity-recognition.md) - Extract entities mentioned within topics
- [text-analytics-overview.md](text-analytics-overview.md) - Guide to text analytics technique selection
