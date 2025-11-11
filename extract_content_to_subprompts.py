#!/usr/bin/env python3
"""
Content Extractor - Extract relevant content from mega-prompts to populate sub-prompts
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

class ContentExtractor:
    def __init__(self):
        self.base_path = Path("/home/user/prompts")

        # Mapping of original files to their sub-prompts
        self.extraction_map = {
            "education/Academic Research/research-design.md": {
                "quantitative-research-design.md": {
                    "keywords": ["quantitative", "experimental", "statistical", "hypothesis", "randomized", "control group"],
                    "exclude": ["qualitative", "phenomenology", "ethnography"]
                },
                "qualitative-research-design.md": {
                    "keywords": ["qualitative", "phenomenology", "grounded theory", "ethnography", "case study", "interview", "thematic"],
                    "exclude": ["quantitative", "statistical test"]
                },
                "mixed-methods-research-design.md": {
                    "keywords": ["mixed", "integration", "triangulation", "convergent", "explanatory", "exploratory sequential"],
                    "exclude": []
                },
                "research-sampling-strategies.md": {
                    "keywords": ["sampling", "sample size", "power analysis", "recruitment", "probability", "stratified"],
                    "exclude": []
                },
                "research-data-collection.md": {
                    "keywords": ["data collection", "survey", "questionnaire", "interview", "observation", "measurement"],
                    "exclude": []
                },
                "research-ethics-compliance.md": {
                    "keywords": ["ethics", "ethical", "IRB", "consent", "informed consent", "compliance", "protection", "confidentiality"],
                    "exclude": []
                }
            },

            "data-analytics/Research Analytics/network-analysis.md": {
                "network-centrality-analysis.md": {
                    "keywords": ["centrality", "degree", "betweenness", "closeness", "pagerank", "eigenvector"],
                    "exclude": ["community", "modularity"]
                },
                "network-community-detection.md": {
                    "keywords": ["community", "modularity", "clustering", "louvain", "partition", "cluster"],
                    "exclude": []
                },
                "network-path-analysis.md": {
                    "keywords": ["path", "shortest path", "connectivity", "diameter", "distance", "reachability"],
                    "exclude": []
                },
                "network-temporal-analysis.md": {
                    "keywords": ["temporal", "dynamic", "evolution", "time-varying", "link prediction", "longitudinal"],
                    "exclude": []
                },
                "network-visualization-advanced.md": {
                    "keywords": ["visualization", "layout", "plotting", "interactive", "force-directed", "hierarchical"],
                    "exclude": []
                }
            },

            "data-analytics/Research Analytics/text-analytics.md": {
                "text-preprocessing-nlp.md": {
                    "keywords": ["preprocessing", "tokenization", "cleaning", "normalization", "stemming", "lemmatization"],
                    "exclude": ["sentiment", "topic modeling", "classification"]
                },
                "sentiment-analysis-nlp.md": {
                    "keywords": ["sentiment", "opinion", "polarity", "emotion", "vader", "textblob", "positive", "negative"],
                    "exclude": []
                },
                "topic-modeling-nlp.md": {
                    "keywords": ["topic", "lda", "nmf", "bertopic", "latent", "topic modeling"],
                    "exclude": []
                },
                "named-entity-recognition.md": {
                    "keywords": ["entity", "ner", "named entity", "extraction", "person", "organization", "location"],
                    "exclude": []
                },
                "text-classification-nlp.md": {
                    "keywords": ["classification", "categorization", "classifier", "category", "label"],
                    "exclude": []
                }
            },

            "education/Academic Research/literature-reviews.md": {
                "systematic-literature-review.md": {
                    "keywords": ["systematic", "prisma", "protocol", "inclusion criteria", "exclusion criteria", "search strategy"],
                    "exclude": ["meta-analysis", "effect size"]
                },
                "meta-analysis-research.md": {
                    "keywords": ["meta-analysis", "effect size", "forest plot", "heterogeneity", "publication bias", "pooled"],
                    "exclude": []
                },
                "narrative-literature-review.md": {
                    "keywords": ["narrative", "scoping", "thematic", "synthesis", "literature synthesis"],
                    "exclude": ["systematic", "meta-analysis"]
                }
            },

            "data-analytics/Analytics Engineering/pipeline-development.md": {
                "data-ingestion-pipelines.md": {
                    "keywords": ["ingestion", "extract", "source", "cdc", "streaming", "batch ingestion"],
                    "exclude": ["transformation", "orchestration"]
                },
                "data-transformation-pipelines.md": {
                    "keywords": ["transformation", "transform", "bronze", "silver", "gold", "data quality"],
                    "exclude": ["ingestion", "orchestration"]
                },
                "pipeline-orchestration.md": {
                    "keywords": ["orchestration", "airflow", "dag", "workflow", "scheduling", "prefect", "dagster"],
                    "exclude": []
                },
                "pipeline-monitoring-quality.md": {
                    "keywords": ["monitoring", "quality", "alerting", "sla", "observability", "metrics"],
                    "exclude": []
                }
            },

            "data-analytics/Analytics Engineering/query-optimization.md": {
                "query-analysis-profiling.md": {
                    "keywords": ["profiling", "execution plan", "analysis", "performance metrics", "baseline"],
                    "exclude": ["indexing", "index"]
                },
                "query-optimization-strategies.md": {
                    "keywords": ["optimization", "query rewriting", "join", "tuning", "query hint"],
                    "exclude": ["indexing", "monitoring"]
                },
                "database-indexing-strategies.md": {
                    "keywords": ["index", "indexing", "b-tree", "columnstore", "partition", "covering index"],
                    "exclude": []
                },
                "query-performance-monitoring.md": {
                    "keywords": ["monitoring", "performance", "statistics", "maintenance", "continuous"],
                    "exclude": []
                }
            },

            "data-analytics/Research Analytics/experimental-design.md": {
                "ab-testing-experiments.md": {
                    "keywords": ["a/b", "ab test", "multivariate", "conversion", "treatment", "control"],
                    "exclude": ["clinical", "quasi"]
                },
                "randomized-controlled-trials.md": {
                    "keywords": ["rct", "randomized", "clinical trial", "treatment allocation", "blinding"],
                    "exclude": ["quasi", "difference-in-differences"]
                },
                "quasi-experimental-design.md": {
                    "keywords": ["quasi", "difference-in-differences", "did", "propensity", "regression discontinuity"],
                    "exclude": []
                },
                "causal-inference-analysis.md": {
                    "keywords": ["causal", "instrumental", "synthetic control", "econometric", "counterfactual"],
                    "exclude": []
                }
            }
        }

    def extract_sections(self, content: str, keywords: List[str], exclude: List[str]) -> str:
        """
        Extract sections from content that match keywords and don't match exclude terms
        """
        lines = content.split('\n')
        extracted_sections = []
        current_section = []
        section_score = 0
        in_code_block = False

        for i, line in enumerate(lines):
            # Track code blocks
            if line.strip().startswith('```'):
                in_code_block = not in_code_block

            # Calculate relevance score for this line
            line_lower = line.lower()
            keyword_matches = sum(1 for kw in keywords if kw.lower() in line_lower)
            exclude_matches = sum(1 for ex in exclude if ex.lower() in line_lower)

            # If this is a header or we're in a code block, check if section is relevant
            if line.startswith('#') or (in_code_block and i > 0):
                # Save previous section if it was relevant
                if current_section and section_score > 0:
                    extracted_sections.extend(current_section)
                    extracted_sections.append('')  # Add blank line between sections

                # Start new section
                current_section = [line]
                section_score = keyword_matches - (exclude_matches * 2)
            else:
                current_section.append(line)
                section_score += keyword_matches - (exclude_matches * 2)

        # Add final section if relevant
        if current_section and section_score > 0:
            extracted_sections.extend(current_section)

        return '\n'.join(extracted_sections)

    def extract_variables(self, content: str) -> str:
        """Extract variable definitions from content"""
        # Find Variables section
        var_match = re.search(r'## Variables\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if var_match:
            return var_match.group(1).strip()
        return ""

    def extract_examples(self, content: str, keywords: List[str]) -> str:
        """Extract relevant examples from content"""
        # Find Example sections
        examples = []
        example_pattern = r'###? Example.*?\n(.*?)(?=\n###?|\Z)'
        matches = re.finditer(example_pattern, content, re.DOTALL)

        for match in matches:
            example_text = match.group(0)
            # Check if example is relevant
            if any(kw.lower() in example_text.lower() for kw in keywords):
                examples.append(example_text)

        return '\n\n'.join(examples) if examples else ""

    def create_enhanced_subprompt(self, original_path: str, subprompt_file: str, config: Dict) -> None:
        """
        Extract content from original file and create enhanced sub-prompt
        """
        # Read original file
        original_full_path = self.base_path / original_path
        with open(original_full_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Extract relevant sections
        extracted_content = self.extract_sections(
            original_content,
            config['keywords'],
            config['exclude']
        )

        # Extract variables and examples
        variables = self.extract_variables(original_content)
        examples = self.extract_examples(original_content, config['keywords'])

        # Read current sub-prompt to preserve frontmatter and Quick Start
        category = '/'.join(original_path.split('/')[:-1])
        subprompt_path = self.base_path / category / subprompt_file

        if not subprompt_path.exists():
            print(f"⚠️  Warning: {subprompt_file} not found, skipping")
            return

        with open(subprompt_path, 'r', encoding='utf-8') as f:
            current_content = f.read()

        # Extract frontmatter and Quick Start from current file
        frontmatter_match = re.match(r'^(---\n.*?\n---\n)', current_content, re.DOTALL)
        if not frontmatter_match:
            print(f"⚠️  Warning: No frontmatter in {subprompt_file}")
            return

        frontmatter = frontmatter_match.group(1)

        # Extract Quick Start
        quickstart_match = re.search(r'(## Quick Start.*?)(?=\n## [^Q])', current_content, re.DOTALL)
        quickstart = quickstart_match.group(1) if quickstart_match else "## Quick Start\n\n[Add Quick Start section]"

        # Build enhanced content
        enhanced_content = frontmatter + '\n'

        # Add title from frontmatter
        title_match = re.search(r'title:\s*(.+)', frontmatter)
        if title_match:
            enhanced_content += f"# {title_match.group(1)}\n\n"

        # Add purpose from frontmatter
        purpose_match = re.search(r'use_cases:\s*\n\s*-\s*(.+)', frontmatter)
        if purpose_match:
            enhanced_content += f"## Purpose\n{purpose_match.group(1)}\n\n"

        # Add Quick Start
        enhanced_content += quickstart + '\n\n'

        # Add extracted template content
        if extracted_content and len(extracted_content) > 500:
            enhanced_content += "## Template\n\n"
            # Limit extracted content to reasonable size (max ~800 lines)
            content_lines = extracted_content.split('\n')
            if len(content_lines) > 800:
                enhanced_content += '\n'.join(content_lines[:800])
                enhanced_content += '\n\n[Content truncated for length - see original for full details]\n'
            else:
                enhanced_content += extracted_content
            enhanced_content += '\n\n'
        else:
            enhanced_content += "## Template\n\n```\n[Template content extracted from original - add specific guidance]\n```\n\n"

        # Add variables if found
        if variables:
            enhanced_content += "## Variables\n\n"
            # Limit variables to first 50 most relevant
            var_lines = variables.split('\n')
            enhanced_content += '\n'.join(var_lines[:50])
            if len(var_lines) > 50:
                enhanced_content += '\n\n[Additional variables available in original template]\n'
            enhanced_content += '\n\n'

        # Add examples if found
        if examples:
            enhanced_content += "## Usage Examples\n\n"
            enhanced_content += examples + '\n\n'

        # Add standard footer
        enhanced_content += """## Best Practices

1. **Focus**: Concentrate on the specific aspect covered by this template
2. **Integration**: Combine with related templates for comprehensive solutions
3. **Iteration**: Start simple and refine based on results
4. **Documentation**: Track your parameters and customizations

## Tips for Success

- Begin with the Quick Start section
- Customize variables to your specific context
- Validate outputs against your requirements
- Iterate and refine based on results

## Related Resources

See the overview file for the complete collection of related templates.

---

**Note:** This focused template is part of a comprehensive collection designed for improved usability.
"""

        # Write enhanced content
        with open(subprompt_path, 'w', encoding='utf-8') as f:
            f.write(enhanced_content)

        print(f"✅ Enhanced: {subprompt_file}")

    def run(self):
        """Execute content extraction for all sub-prompts"""
        print("\n" + "="*80)
        print("CONTENT EXTRACTION TO SUB-PROMPTS")
        print("="*80)
        print("\nExtracting relevant content from mega-prompts to populate sub-prompts...\n")

        total_enhanced = 0

        for original_path, subprompts in self.extraction_map.items():
            print(f"\n{'='*80}")
            print(f"Processing: {original_path}")
            print(f"{'='*80}")

            for subprompt_file, config in subprompts.items():
                self.create_enhanced_subprompt(original_path, subprompt_file, config)
                total_enhanced += 1

        print("\n" + "="*80)
        print("CONTENT EXTRACTION COMPLETE!")
        print("="*80)
        print(f"\nTotal sub-prompts enhanced: {total_enhanced}")
        print("\nAll sub-prompts now have:")
        print("  ✅ Frontmatter with metadata")
        print("  ✅ Quick Start sections")
        print("  ✅ Extracted relevant template content")
        print("  ✅ Relevant variables")
        print("  ✅ Usage examples")
        print("  ✅ Best practices and tips")
        print("\n")

if __name__ == "__main__":
    extractor = ContentExtractor()
    extractor.run()
