#!/usr/bin/env python3
"""
Update INDEX.md to replace mega-prompt references with new sub-prompts
"""

import re
from pathlib import Path

def update_index():
    index_path = Path("/home/user/prompts/INDEX.md")

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define replacements - map old references to new sub-prompt lists
    replacements = {
        # Research Design (education)
        r'- \[Research Design\]\(education/Academic Research/research-design\.md\) - `education`': '''- [Research Design Overview](education/Academic Research/research-design-overview.md) - `education`
- [Quantitative Research Design](education/Academic Research/quantitative-research-design.md) - `education`
- [Qualitative Research Design](education/Academic Research/qualitative-research-design.md) - `education`
- [Mixed-Methods Research Design](education/Academic Research/mixed-methods-research-design.md) - `education`
- [Research Sampling Strategies](education/Academic Research/research-sampling-strategies.md) - `education`
- [Research Data Collection](education/Academic Research/research-data-collection.md) - `education`
- [Research Ethics & Compliance](education/Academic Research/research-ethics-compliance.md) - `education`''',

        # Literature Reviews (education)
        r'- \[Literature Reviews\]\(education/Academic Research/literature-reviews\.md\) - `education`': '''- [Literature Reviews Overview](education/Academic Research/literature-reviews-overview.md) - `education`
- [Systematic Literature Review](education/Academic Research/systematic-literature-review.md) - `education`
- [Meta-Analysis Research](education/Academic Research/meta-analysis-research.md) - `education`
- [Narrative Literature Review](education/Academic Research/narrative-literature-review.md) - `education`''',

        # Network Analysis (data-analytics)
        r'- \[Network Analysis\]\(data-analytics/Research Analytics/network-analysis\.md\) - `data-analytics`': '''- [Network Analysis Overview](data-analytics/Research Analytics/network-analysis-overview.md) - `data-analytics`
- [Network Centrality Analysis](data-analytics/Research Analytics/network-centrality-analysis.md) - `data-analytics`
- [Network Community Detection](data-analytics/Research Analytics/network-community-detection.md) - `data-analytics`
- [Network Path Analysis](data-analytics/Research Analytics/network-path-analysis.md) - `data-analytics`
- [Network Temporal Analysis](data-analytics/Research Analytics/network-temporal-analysis.md) - `data-analytics`
- [Network Visualization Advanced](data-analytics/Research Analytics/network-visualization-advanced.md) - `data-analytics`''',

        # Text Analytics (data-analytics)
        r'- \[Text Analytics\]\(data-analytics/Research Analytics/text-analytics\.md\) - `data-analytics`': '''- [Text Analytics Overview](data-analytics/Research Analytics/text-analytics-overview.md) - `data-analytics`
- [Text Preprocessing & NLP](data-analytics/Research Analytics/text-preprocessing-nlp.md) - `data-analytics`
- [Sentiment Analysis](data-analytics/Research Analytics/sentiment-analysis-nlp.md) - `data-analytics`
- [Topic Modeling](data-analytics/Research Analytics/topic-modeling-nlp.md) - `data-analytics`
- [Named Entity Recognition](data-analytics/Research Analytics/named-entity-recognition.md) - `data-analytics`
- [Text Classification](data-analytics/Research Analytics/text-classification-nlp.md) - `data-analytics`''',

        # Experimental Design (data-analytics)
        r'- \[Experimental Design\]\(data-analytics/Research Analytics/experimental-design\.md\) - `data-analytics`': '''- [Experimental Design Overview](data-analytics/Research Analytics/experimental-design-overview.md) - `data-analytics`
- [A/B Testing Experiments](data-analytics/Research Analytics/ab-testing-experiments.md) - `data-analytics`
- [Randomized Controlled Trials](data-analytics/Research Analytics/randomized-controlled-trials.md) - `data-analytics`
- [Quasi-Experimental Design](data-analytics/Research Analytics/quasi-experimental-design.md) - `data-analytics`
- [Causal Inference Analysis](data-analytics/Research Analytics/causal-inference-analysis.md) - `data-analytics`''',

        # Pipeline Development (data-analytics)
        r'- \[Pipeline Development\]\(data-analytics/Analytics Engineering/pipeline-development\.md\) - `data-analytics`': '''- [Pipeline Development Overview](data-analytics/Analytics Engineering/pipeline-development-overview.md) - `data-analytics`
- [Data Ingestion Pipelines](data-analytics/Analytics Engineering/data-ingestion-pipelines.md) - `data-analytics`
- [Data Transformation Pipelines](data-analytics/Analytics Engineering/data-transformation-pipelines.md) - `data-analytics`
- [Pipeline Orchestration](data-analytics/Analytics Engineering/pipeline-orchestration.md) - `data-analytics`
- [Pipeline Monitoring & Quality](data-analytics/Analytics Engineering/pipeline-monitoring-quality.md) - `data-analytics`''',

        # Query Optimization (data-analytics)
        r'- \[Query Optimization\]\(data-analytics/Analytics Engineering/query-optimization\.md\) - `data-analytics`': '''- [Query Optimization Overview](data-analytics/Analytics Engineering/query-optimization-overview.md) - `data-analytics`
- [Query Analysis & Profiling](data-analytics/Analytics Engineering/query-analysis-profiling.md) - `data-analytics`
- [Query Optimization Strategies](data-analytics/Analytics Engineering/query-optimization-strategies.md) - `data-analytics`
- [Database Indexing Strategies](data-analytics/Analytics Engineering/database-indexing-strategies.md) - `data-analytics`
- [Query Performance Monitoring](data-analytics/Analytics Engineering/query-performance-monitoring.md) - `data-analytics`''',
    }

    # Additional replacements for different contexts (without category tag)
    replacements_no_category = {
        r'- \[Research Design\]\(education/Academic Research/research-design\.md\)': '''- [Research Design Overview](education/Academic Research/research-design-overview.md)
- [Quantitative Research Design](education/Academic Research/quantitative-research-design.md)
- [Qualitative Research Design](education/Academic Research/qualitative-research-design.md)
- [Mixed-Methods Research Design](education/Academic Research/mixed-methods-research-design.md)
- [Research Sampling Strategies](education/Academic Research/research-sampling-strategies.md)
- [Research Data Collection](education/Academic Research/research-data-collection.md)
- [Research Ethics & Compliance](education/Academic Research/research-ethics-compliance.md)''',

        r'- \[Literature Reviews\]\(education/Academic Research/literature-reviews\.md\)': '''- [Literature Reviews Overview](education/Academic Research/literature-reviews-overview.md)
- [Systematic Literature Review](education/Academic Research/systematic-literature-review.md)
- [Meta-Analysis Research](education/Academic Research/meta-analysis-research.md)
- [Narrative Literature Review](education/Academic Research/narrative-literature-review.md)''',

        r'- \[Network Analysis\]\(data-analytics/Research Analytics/network-analysis\.md\)': '''- [Network Analysis Overview](data-analytics/Research Analytics/network-analysis-overview.md)
- [Network Centrality Analysis](data-analytics/Research Analytics/network-centrality-analysis.md)
- [Network Community Detection](data-analytics/Research Analytics/network-community-detection.md)
- [Network Path Analysis](data-analytics/Research Analytics/network-path-analysis.md)
- [Network Temporal Analysis](data-analytics/Research Analytics/network-temporal-analysis.md)
- [Network Visualization Advanced](data-analytics/Research Analytics/network-visualization-advanced.md)''',

        r'- \[Text Analytics\]\(data-analytics/Research Analytics/text-analytics\.md\)': '''- [Text Analytics Overview](data-analytics/Research Analytics/text-analytics-overview.md)
- [Text Preprocessing & NLP](data-analytics/Research Analytics/text-preprocessing-nlp.md)
- [Sentiment Analysis](data-analytics/Research Analytics/sentiment-analysis-nlp.md)
- [Topic Modeling](data-analytics/Research Analytics/topic-modeling-nlp.md)
- [Named Entity Recognition](data-analytics/Research Analytics/named-entity-recognition.md)
- [Text Classification](data-analytics/Research Analytics/text-classification-nlp.md)''',

        r'- \[Experimental Design\]\(data-analytics/Research Analytics/experimental-design\.md\)': '''- [Experimental Design Overview](data-analytics/Research Analytics/experimental-design-overview.md)
- [A/B Testing Experiments](data-analytics/Research Analytics/ab-testing-experiments.md)
- [Randomized Controlled Trials](data-analytics/Research Analytics/randomized-controlled-trials.md)
- [Quasi-Experimental Design](data-analytics/Research Analytics/quasi-experimental-design.md)
- [Causal Inference Analysis](data-analytics/Research Analytics/causal-inference-analysis.md)''',

        r'- \[Pipeline Development\]\(data-analytics/Analytics Engineering/pipeline-development\.md\)': '''- [Pipeline Development Overview](data-analytics/Analytics Engineering/pipeline-development-overview.md)
- [Data Ingestion Pipelines](data-analytics/Analytics Engineering/data-ingestion-pipelines.md)
- [Data Transformation Pipelines](data-analytics/Analytics Engineering/data-transformation-pipelines.md)
- [Pipeline Orchestration](data-analytics/Analytics Engineering/pipeline-orchestration.md)
- [Pipeline Monitoring & Quality](data-analytics/Analytics Engineering/pipeline-monitoring-quality.md)''',

        r'- \[Query Optimization\]\(data-analytics/Analytics Engineering/query-optimization\.md\)': '''- [Query Optimization Overview](data-analytics/Analytics Engineering/query-optimization-overview.md)
- [Query Analysis & Profiling](data-analytics/Analytics Engineering/query-analysis-profiling.md)
- [Query Optimization Strategies](data-analytics/Analytics Engineering/query-optimization-strategies.md)
- [Database Indexing Strategies](data-analytics/Analytics Engineering/database-indexing-strategies.md)
- [Query Performance Monitoring](data-analytics/Analytics Engineering/query-performance-monitoring.md)''',
    }

    # Apply replacements with category tags first
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    # Apply replacements without category tags (for alphabetical sections)
    for pattern, replacement in replacements_no_category.items():
        content = re.sub(pattern, replacement, content)

    # Update template counts in section headers
    # Analytics & Business Intelligence: was 17, now 17 - 7 + 31 = 41
    content = re.sub(
        r'### Analytics & Business Intelligence\n\*\*17 templates\*\*',
        '### Analytics & Business Intelligence\n**41 templates**',
        content
    )

    # Education & Learning: was 29, now 29 - 2 + 10 = 37
    content = re.sub(
        r'### Education & Learning\n\*\*29 templates\*\*',
        '### Education & Learning\n**37 templates**',
        content
    )

    # Update the main index description
    content = re.sub(
        r'A comprehensive, searchable index of all 375\+ templates',
        'A comprehensive, searchable index of all 400+ templates',
        content
    )

    # Write updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ INDEX.md updated successfully!")
    print("\nChanges made:")
    print("  - Replaced 7 mega-prompts with 38 new sub-prompts and overviews")
    print("  - Updated Analytics & Business Intelligence: 17 → 41 templates")
    print("  - Updated Education & Learning: 29 → 37 templates")
    print("  - Updated total count: 375+ → 400+ templates")

if __name__ == "__main__":
    update_index()
