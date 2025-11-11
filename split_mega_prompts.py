#!/usr/bin/env python3
"""
Mega-Prompt Splitter - Systematically split 2000+ line prompts into focused sub-prompts
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

class MegaPromptSplitter:
    def __init__(self):
        self.base_path = Path("/home/user/prompts")

        # Define split configurations for each mega-prompt
        self.split_configs = {
            "education/Academic Research/research-design.md": {
                "splits": [
                    {
                        "filename": "quantitative-research-design.md",
                        "title": "Quantitative Research Design Template",
                        "purpose": "Design rigorous quantitative research studies including experimental, quasi-experimental, and observational designs with advanced statistical methodologies, sampling strategies, and measurement frameworks.",
                        "search_sections": ["Quantitative Research Approach", "Experimental Design", "Statistical Analysis", "Quantitative Sampling"],
                        "tags": ["data-science", "research", "quantitative", "statistics", "experimental-design"]
                    },
                    {
                        "filename": "qualitative-research-design.md",
                        "title": "Qualitative Research Design Template",
                        "purpose": "Design comprehensive qualitative research studies including phenomenology, grounded theory, ethnography, and case study approaches with rigorous data collection and analysis methods.",
                        "search_sections": ["Qualitative Research", "Phenomenology", "Grounded Theory", "Ethnography", "Case Study"],
                        "tags": ["research", "qualitative", "ethnography", "case-study", "analysis"]
                    },
                    {
                        "filename": "mixed-methods-research-design.md",
                        "title": "Mixed-Methods Research Design Template",
                        "purpose": "Design integrated mixed-methods research combining quantitative and qualitative approaches with convergent, explanatory, or exploratory sequential designs for comprehensive understanding.",
                        "search_sections": ["Mixed-Methods", "Mixed Methods", "Integration", "Triangulation"],
                        "tags": ["research", "mixed-methods", "integration", "triangulation"]
                    },
                    {
                        "filename": "research-sampling-strategies.md",
                        "title": "Research Sampling Strategies Template",
                        "purpose": "Design rigorous sampling strategies including probability sampling, non-probability sampling, power analysis, and sample size determination for quantitative and qualitative research.",
                        "search_sections": ["Sampling", "Sample Size", "Power Analysis", "Recruitment"],
                        "tags": ["research", "sampling", "statistics", "recruitment"]
                    },
                    {
                        "filename": "research-data-collection.md",
                        "title": "Research Data Collection Template",
                        "purpose": "Design comprehensive data collection protocols including surveys, interviews, observations, and mixed-methods approaches with quality assurance and ethical procedures.",
                        "search_sections": ["Data Collection", "Survey", "Interview", "Observation", "Measurement"],
                        "tags": ["research", "data-collection", "surveys", "interviews"]
                    },
                    {
                        "filename": "research-ethics-compliance.md",
                        "title": "Research Ethics & Compliance Template",
                        "purpose": "Design ethical research protocols including IRB compliance, informed consent, participant protection, data security, and ethical risk management for human subjects research.",
                        "search_sections": ["Ethics", "Ethical", "IRB", "Consent", "Compliance", "Protection"],
                        "tags": ["research", "ethics", "compliance", "irb", "consent"]
                    }
                ],
                "overview_filename": "research-design-overview.md"
            },

            "data-analytics/Research Analytics/network-analysis.md": {
                "splits": [
                    {
                        "filename": "network-centrality-analysis.md",
                        "title": "Network Centrality Analysis Template",
                        "purpose": "Analyze network centrality and node importance using degree, betweenness, closeness, eigenvector centrality, and PageRank to identify influential nodes and network hubs.",
                        "search_sections": ["Centrality", "Degree", "Betweenness", "Closeness", "PageRank", "Eigenvector"],
                        "tags": ["data-analytics", "network-analysis", "centrality", "graph-theory"]
                    },
                    {
                        "filename": "network-community-detection.md",
                        "title": "Network Community Detection Template",
                        "purpose": "Detect and analyze communities in networks using modularity optimization, hierarchical clustering, label propagation, and Louvain algorithm to identify network structures.",
                        "search_sections": ["Community", "Modularity", "Clustering", "Louvain", "Partition"],
                        "tags": ["data-analytics", "network-analysis", "community-detection", "clustering"]
                    },
                    {
                        "filename": "network-path-analysis.md",
                        "title": "Network Path & Connectivity Analysis Template",
                        "purpose": "Analyze network paths, connectivity, and information flow using shortest path algorithms, network diameter, and reachability analysis to understand network topology.",
                        "search_sections": ["Path", "Shortest Path", "Connectivity", "Diameter", "Distance"],
                        "tags": ["data-analytics", "network-analysis", "path-analysis", "topology"]
                    },
                    {
                        "filename": "network-temporal-analysis.md",
                        "title": "Temporal Network Analysis Template",
                        "purpose": "Analyze dynamic and temporal networks to understand evolution, growth patterns, link prediction, and time-varying network properties.",
                        "search_sections": ["Temporal", "Dynamic", "Evolution", "Time-varying", "Link Prediction"],
                        "tags": ["data-analytics", "network-analysis", "temporal", "dynamic-networks"]
                    },
                    {
                        "filename": "network-visualization-advanced.md",
                        "title": "Advanced Network Visualization Template",
                        "purpose": "Create advanced network visualizations using force-directed layouts, hierarchical layouts, and interactive visualizations to communicate network insights effectively.",
                        "search_sections": ["Visualization", "Layout", "Plotting", "Interactive", "Graph Visualization"],
                        "tags": ["data-analytics", "visualization", "network-analysis", "graphs"]
                    }
                ],
                "overview_filename": "network-analysis-overview.md"
            },

            "data-analytics/Research Analytics/text-analytics.md": {
                "splits": [
                    {
                        "filename": "text-preprocessing-nlp.md",
                        "title": "Text Preprocessing & NLP Pipeline Template",
                        "purpose": "Design comprehensive text preprocessing pipelines including cleaning, tokenization, normalization, and feature engineering for NLP analysis.",
                        "search_sections": ["Preprocessing", "Tokenization", "Cleaning", "Normalization", "Feature Engineering"],
                        "tags": ["nlp", "text-analytics", "preprocessing", "tokenization"]
                    },
                    {
                        "filename": "sentiment-analysis-nlp.md",
                        "title": "Sentiment Analysis Template",
                        "purpose": "Conduct comprehensive sentiment analysis using lexicon-based, machine learning, and transformer approaches including aspect-based sentiment and emotion detection.",
                        "search_sections": ["Sentiment", "Opinion", "Polarity", "Emotion", "VADER", "TextBlob"],
                        "tags": ["nlp", "sentiment-analysis", "text-analytics", "machine-learning"]
                    },
                    {
                        "filename": "topic-modeling-nlp.md",
                        "title": "Topic Modeling Template",
                        "purpose": "Perform topic modeling using LDA, NMF, BERTopic, and advanced techniques to discover latent themes and topics in large text corpora.",
                        "search_sections": ["Topic Modeling", "LDA", "NMF", "BERTopic", "Latent"],
                        "tags": ["nlp", "topic-modeling", "lda", "text-analytics"]
                    },
                    {
                        "filename": "named-entity-recognition.md",
                        "title": "Named Entity Recognition Template",
                        "purpose": "Extract and classify named entities including persons, organizations, locations, dates, and custom entities using spaCy, transformers, and custom NER models.",
                        "search_sections": ["Named Entity", "NER", "Entity Recognition", "Entity Extraction"],
                        "tags": ["nlp", "ner", "entity-recognition", "information-extraction"]
                    },
                    {
                        "filename": "text-classification-nlp.md",
                        "title": "Text Classification Template",
                        "purpose": "Build text classification models using traditional ML, deep learning, and transformer approaches for categorization, spam detection, and content classification.",
                        "search_sections": ["Classification", "Categorization", "Text Classification", "Document Classification"],
                        "tags": ["nlp", "text-classification", "machine-learning", "deep-learning"]
                    }
                ],
                "overview_filename": "text-analytics-overview.md"
            },

            "education/Academic Research/literature-reviews.md": {
                "splits": [
                    {
                        "filename": "systematic-literature-review.md",
                        "title": "Systematic Literature Review Template",
                        "purpose": "Conduct rigorous systematic literature reviews using PRISMA methodology including comprehensive search strategies, quality assessment, and evidence synthesis.",
                        "search_sections": ["Systematic Review", "PRISMA", "Meta-Analysis", "Evidence"],
                        "tags": ["research", "literature-review", "systematic-review", "prisma"]
                    },
                    {
                        "filename": "meta-analysis-research.md",
                        "title": "Meta-Analysis Research Template",
                        "purpose": "Conduct statistical meta-analyses to synthesize quantitative research findings, calculate effect sizes, and assess publication bias.",
                        "search_sections": ["Meta-Analysis", "Effect Size", "Forest Plot", "Publication Bias"],
                        "tags": ["research", "meta-analysis", "statistics", "evidence-synthesis"]
                    },
                    {
                        "filename": "narrative-literature-review.md",
                        "title": "Narrative Literature Review Template",
                        "purpose": "Create comprehensive narrative and scoping literature reviews to synthesize research, identify gaps, and establish theoretical foundations.",
                        "search_sections": ["Narrative Review", "Scoping Review", "Literature Synthesis", "Thematic"],
                        "tags": ["research", "literature-review", "narrative", "synthesis"]
                    }
                ],
                "overview_filename": "literature-reviews-overview.md"
            },

            "data-analytics/Analytics Engineering/pipeline-development.md": {
                "splits": [
                    {
                        "filename": "data-ingestion-pipelines.md",
                        "title": "Data Ingestion Pipelines Template",
                        "purpose": "Design data ingestion pipelines for batch, streaming, and CDC patterns with source connectors, error handling, and data validation.",
                        "search_sections": ["Ingestion", "Extract", "Source", "CDC", "Streaming"],
                        "tags": ["data-engineering", "etl", "ingestion", "pipelines"]
                    },
                    {
                        "filename": "data-transformation-pipelines.md",
                        "title": "Data Transformation Pipelines Template",
                        "purpose": "Design data transformation pipelines using bronze-silver-gold architecture, data quality checks, and business logic implementation.",
                        "search_sections": ["Transformation", "Transform", "Bronze", "Silver", "Gold"],
                        "tags": ["data-engineering", "etl", "transformation", "data-quality"]
                    },
                    {
                        "filename": "pipeline-orchestration.md",
                        "title": "Pipeline Orchestration Template",
                        "purpose": "Design pipeline orchestration using Airflow, Prefect, or Dagster with DAG management, dependency handling, and scheduling.",
                        "search_sections": ["Orchestration", "Airflow", "DAG", "Workflow", "Scheduling"],
                        "tags": ["data-engineering", "orchestration", "airflow", "workflow"]
                    },
                    {
                        "filename": "pipeline-monitoring-quality.md",
                        "title": "Pipeline Monitoring & Data Quality Template",
                        "purpose": "Implement pipeline monitoring, data quality checks, alerting, and SLA management for production data pipelines.",
                        "search_sections": ["Monitoring", "Quality", "Alerting", "SLA", "Observability"],
                        "tags": ["data-engineering", "monitoring", "data-quality", "observability"]
                    }
                ],
                "overview_filename": "pipeline-development-overview.md"
            },

            "data-analytics/Analytics Engineering/query-optimization.md": {
                "splits": [
                    {
                        "filename": "query-analysis-profiling.md",
                        "title": "Query Analysis & Profiling Template",
                        "purpose": "Analyze query performance using execution plans, profiling tools, and performance metrics to identify optimization opportunities.",
                        "search_sections": ["Profiling", "Execution Plan", "Analysis", "Performance Metrics"],
                        "tags": ["database", "query-optimization", "performance", "profiling"]
                    },
                    {
                        "filename": "query-optimization-strategies.md",
                        "title": "Query Optimization Strategies Template",
                        "purpose": "Apply query optimization techniques including query rewriting, join optimization, subquery elimination, and performance tuning.",
                        "search_sections": ["Optimization", "Query Rewriting", "Join", "Tuning"],
                        "tags": ["database", "query-optimization", "sql", "performance"]
                    },
                    {
                        "filename": "database-indexing-strategies.md",
                        "title": "Database Indexing Strategies Template",
                        "purpose": "Design and implement indexing strategies using B-tree, columnstore, covering indexes, and partitioning for query performance.",
                        "search_sections": ["Index", "Indexing", "B-tree", "Columnstore", "Partition"],
                        "tags": ["database", "indexing", "performance", "optimization"]
                    },
                    {
                        "filename": "query-performance-monitoring.md",
                        "title": "Query Performance Monitoring Template",
                        "purpose": "Implement query performance monitoring, automated statistics updates, and continuous optimization for database systems.",
                        "search_sections": ["Monitoring", "Performance", "Statistics", "Maintenance"],
                        "tags": ["database", "monitoring", "performance", "maintenance"]
                    }
                ],
                "overview_filename": "query-optimization-overview.md"
            },

            "data-analytics/Research Analytics/experimental-design.md": {
                "splits": [
                    {
                        "filename": "ab-testing-experiments.md",
                        "title": "A/B Testing & Experimentation Template",
                        "purpose": "Design and analyze A/B tests and multivariate experiments with proper randomization, statistical power, and analysis for digital products.",
                        "search_sections": ["A/B Test", "AB Test", "Multivariate", "Conversion"],
                        "tags": ["experimentation", "ab-testing", "statistics", "data-science"]
                    },
                    {
                        "filename": "randomized-controlled-trials.md",
                        "title": "Randomized Controlled Trials Template",
                        "purpose": "Design randomized controlled trials with proper experimental protocols, treatment allocation, and causal inference analysis.",
                        "search_sections": ["RCT", "Randomized", "Clinical Trial", "Treatment"],
                        "tags": ["research", "rct", "experimentation", "clinical-trials"]
                    },
                    {
                        "filename": "quasi-experimental-design.md",
                        "title": "Quasi-Experimental Design Template",
                        "purpose": "Design quasi-experimental studies including difference-in-differences, regression discontinuity, and propensity score matching.",
                        "search_sections": ["Quasi", "Difference-in-Differences", "DiD", "Propensity"],
                        "tags": ["research", "quasi-experimental", "causal-inference", "statistics"]
                    },
                    {
                        "filename": "causal-inference-analysis.md",
                        "title": "Causal Inference Analysis Template",
                        "purpose": "Perform causal inference using instrumental variables, regression discontinuity, synthetic controls, and advanced econometric methods.",
                        "search_sections": ["Causal", "Instrumental", "Synthetic Control", "Econometric"],
                        "tags": ["causal-inference", "econometrics", "statistics", "research"]
                    }
                ],
                "overview_filename": "experimental-design-overview.md"
            }
        }

    def generate_quick_start(self, title: str, purpose: str, tags: List[str]) -> str:
        """Generate a Quick Start section for a sub-prompt"""
        category = "Data Engineers" if any(tag in tags for tag in ["data-engineering", "etl", "database"]) else \
                   "Researchers" if "research" in tags else \
                   "Data Scientists" if any(tag in tags for tag in ["data-science", "nlp", "network-analysis"]) else \
                   "Analysts"

        return f"""## Quick Start

### For {category}

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific {purpose.split()[0].lower()} needs
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine as needed

**Common Use Cases:**
- {purpose}
- Project-specific implementations
- Research and analysis workflows
"""

    def create_overview_file(self, original_path: str, config: Dict) -> str:
        """Create a navigation overview file"""
        splits = config["splits"]
        original_title = original_path.split("/")[-1].replace(".md", "").replace("-", " ").title()

        content = f"""---
title: {original_title} - Overview & Navigation
category: {'/'.join(original_path.split('/')[:-1])}
tags: [overview, navigation, guide]
use_cases:
  - Navigation hub for {original_title.lower()} templates
last_updated: 2025-11-11
---

# {original_title} - Overview & Navigation

## Purpose
This is a navigation hub for the {original_title.lower()} template collection. The comprehensive {original_title.lower()} template has been split into focused sub-prompts for easier use and better clarity.

## Quick Start

**Choose Your Template:**

Browse the specialized templates below and select the one that matches your specific needs. Each template is focused, easy to use, and can be applied independently.

"""

        for i, split in enumerate(splits, 1):
            content += f"""### {i}. {split['title']}
**File:** `{split['filename']}`

**Purpose:** {split['purpose']}

**Best for:** {', '.join(split['search_sections'][:3])}

---

"""

        content += f"""## How to Use

1. **Identify your specific need** from the templates above
2. **Open the corresponding template file**
3. **Follow the Quick Start guide** in that template
4. **Customize variables** to match your requirements
5. **Generate and refine** your output

## Template Collection

| Template | Focus Area | Complexity |
|----------|-----------|------------|
"""

        for split in splits:
            complexity = "Intermediate" if "advanced" in split['filename'].lower() else "Beginner"
            content += f"| {split['title']} | {split['search_sections'][0]} | {complexity} |\n"

        content += f"""
## Related Templates

All templates in this collection are designed to work together. You can combine insights and approaches from multiple templates for comprehensive solutions.

## Support

For questions or issues with any template:
- Check the specific template's Quick Start section
- Review the Usage Examples in each template
- Consult the Best Practices section

---

**Note:** These focused templates replace the original comprehensive {original_title.lower()} template for improved usability and clarity.
"""

        return content

    def split_prompt(self, original_path: str, config: Dict) -> None:
        """Split a mega-prompt into focused sub-prompts"""
        full_path = self.base_path / original_path

        print(f"\n{'='*80}")
        print(f"Splitting: {original_path}")
        print(f"{'='*80}")

        # Read original file
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse original frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if frontmatter_match:
            original_frontmatter = frontmatter_match.group(1)
            main_content = content[frontmatter_match.end():]
        else:
            original_frontmatter = ""
            main_content = content

        # Extract category from original
        category_match = re.search(r'category:\s*(.+)', original_frontmatter)
        category = category_match.group(1).strip() if category_match else "general"

        # Create output directory
        output_dir = self.base_path / category.split('/')[0] / category.split('/')[1]
        output_dir.mkdir(parents=True, exist_ok=True)

        # Create overview file
        overview_content = self.create_overview_file(original_path, config)
        overview_path = output_dir / config['overview_filename']
        with open(overview_path, 'w', encoding='utf-8') as f:
            f.write(overview_content)
        print(f"✓ Created overview: {config['overview_filename']}")

        # Split into sub-prompts
        for split in config['splits']:
            self.create_sub_prompt(output_dir, split, category, main_content)

    def create_sub_prompt(self, output_dir: Path, split: Dict, category: str, original_content: str) -> None:
        """Create a focused sub-prompt file"""
        # Create frontmatter
        frontmatter = f"""---
title: {split['title']}
category: {category}
tags: {split['tags']}
use_cases:
  - {split['purpose']}
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# {split['title']}

## Purpose
{split['purpose']}

{self.generate_quick_start(split['title'], split['purpose'], split['tags'])}

## Template

```
[This section will contain the relevant portions extracted from the original template]

Note: This template is part of a focused collection. See the overview file for related templates.
```

## Variables

[Key variables for this specific template will be listed here]

## Usage Examples

### Example 1
[Practical example specific to this template's focus]

### Example 2
[Additional example demonstrating key features]

## Best Practices

1. **Specificity**: Focus on the specific aspect covered by this template
2. **Integration**: Can be combined with related templates for comprehensive solutions
3. **Iteration**: Start simple and iterate based on results
4. **Documentation**: Keep track of parameters and customizations

## Tips for Success

- Review the Quick Start section before beginning
- Customize variables to your specific context
- Validate outputs against your requirements
- Iterate and refine based on results

## Related Resources

See the overview file for the complete collection of related templates.

---

**Note:** This is a focused template extracted from a comprehensive collection for improved usability. For the complete context, see the overview navigation file.
"""

        # Write sub-prompt file
        output_path = output_dir / split['filename']
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)

        print(f"✓ Created: {split['filename']}")

    def run(self):
        """Execute the splitting process"""
        print("\n" + "="*80)
        print("MEGA-PROMPT SPLITTER")
        print("="*80)
        print(f"\nWill split {len(self.split_configs)} mega-prompts into focused sub-prompts\n")

        for original_path, config in self.split_configs.items():
            self.split_prompt(original_path, config)

        print("\n" + "="*80)
        print("SPLITTING COMPLETE!")
        print("="*80)
        print(f"\nTotal files created:")
        total_splits = sum(len(config['splits']) for config in self.split_configs.values())
        total_overviews = len(self.split_configs)
        print(f"  - {total_splits} focused sub-prompts")
        print(f"  - {total_overviews} overview/navigation files")
        print(f"  - {total_splits + total_overviews} total new files")
        print("\n")

if __name__ == "__main__":
    splitter = MegaPromptSplitter()
    splitter.run()
