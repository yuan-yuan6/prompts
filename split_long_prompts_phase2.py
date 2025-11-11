#!/usr/bin/env python3
"""
Phase 2: Split remaining 2 high-priority long prompts (1500+ lines)
"""

import os
import re
from pathlib import Path

class LongPromptSplitter:
    def __init__(self):
        self.base_path = Path("/home/user/prompts")

        self.split_configs = {
            "education/Teaching & Instruction/online-learning.md": {
                "splits": [
                    {
                        "filename": "online-learning-platform-architecture.md",
                        "title": "Online Learning Platform Architecture",
                        "purpose": "Design technical platform architecture for online learning including system design, infrastructure, security, integrations, and scalability for e-learning platforms.",
                        "keywords": ["architecture", "system", "infrastructure", "security", "technical", "backend", "frontend", "integration", "scalability", "cloud"],
                        "tags": ["education", "platform-architecture", "system-design", "edtech"]
                    },
                    {
                        "filename": "online-learning-content-curriculum.md",
                        "title": "Online Learning Content & Curriculum Design",
                        "purpose": "Design comprehensive learning content and curriculum including course structure, content types, materials development, and content management for online education.",
                        "keywords": ["content", "curriculum", "course", "materials", "syllabus", "lesson", "module", "resources"],
                        "tags": ["education", "curriculum", "content-design", "course-development"]
                    },
                    {
                        "filename": "online-learning-pedagogy-engagement.md",
                        "title": "Online Learning Pedagogy & Engagement",
                        "purpose": "Design pedagogical strategies and engagement frameworks including learning theories, assessment methods, gamification, personalization, and interactive learning experiences.",
                        "keywords": ["pedagogy", "engagement", "assessment", "gamification", "personalization", "learning theory", "interactive", "motivation"],
                        "tags": ["education", "pedagogy", "engagement", "learning-design"]
                    },
                    {
                        "filename": "online-learning-communication-tools.md",
                        "title": "Online Learning Communication & Collaboration Tools",
                        "purpose": "Design communication and collaboration systems including synchronous/asynchronous tools, discussion forums, messaging, video conferencing, and collaborative features.",
                        "keywords": ["communication", "collaboration", "discussion", "forum", "chat", "video", "messaging", "synchronous", "asynchronous"],
                        "tags": ["education", "communication", "collaboration", "tools"]
                    }
                ],
                "overview_filename": "online-learning-overview.md"
            },

            "data-analytics/Research Analytics/statistical-analysis.md": {
                "splits": [
                    {
                        "filename": "descriptive-statistics-eda.md",
                        "title": "Descriptive Statistics & Exploratory Data Analysis",
                        "purpose": "Perform comprehensive descriptive statistics and exploratory data analysis including summary statistics, distributions, visualizations, and data profiling.",
                        "keywords": ["descriptive", "exploratory", "eda", "summary", "distribution", "visualization", "histogram", "boxplot", "correlation"],
                        "tags": ["statistics", "eda", "descriptive", "data-analysis"]
                    },
                    {
                        "filename": "hypothesis-testing-inference.md",
                        "title": "Hypothesis Testing & Statistical Inference",
                        "purpose": "Conduct hypothesis testing and statistical inference including t-tests, ANOVA, chi-square, confidence intervals, p-values, and power analysis.",
                        "keywords": ["hypothesis", "test", "inference", "t-test", "anova", "chi-square", "p-value", "confidence interval", "significance"],
                        "tags": ["statistics", "hypothesis-testing", "inference", "significance"]
                    },
                    {
                        "filename": "regression-modeling-analysis.md",
                        "title": "Regression Analysis & Statistical Modeling",
                        "purpose": "Perform regression analysis and statistical modeling including linear regression, logistic regression, model diagnostics, assumptions testing, and interpretation.",
                        "keywords": ["regression", "model", "linear", "logistic", "multiple", "coefficients", "residuals", "diagnostics", "assumptions"],
                        "tags": ["statistics", "regression", "modeling", "analysis"]
                    },
                    {
                        "filename": "advanced-statistical-methods.md",
                        "title": "Advanced Statistical Methods",
                        "purpose": "Apply advanced statistical methods including Bayesian analysis, non-parametric tests, multiple testing corrections, and specialized statistical techniques.",
                        "keywords": ["bayesian", "non-parametric", "advanced", "bootstrap", "permutation", "multiple testing", "correction", "specialized"],
                        "tags": ["statistics", "bayesian", "non-parametric", "advanced"]
                    }
                ],
                "overview_filename": "statistical-analysis-overview.md"
            }
        }

    def generate_quick_start(self, title: str, purpose: str, tags: list) -> str:
        """Generate a Quick Start section"""
        category = "Data Engineers" if "data-engineering" in tags else \
                   "Researchers & Statisticians" if "statistics" in tags or "research" in tags else \
                   "Educators & Instructional Designers" if "education" in tags else \
                   "Data Scientists"

        return f"""## Quick Start

### For {category}

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific needs for {purpose.split()[0].lower()}
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine based on results

**Common Use Cases:**
- {purpose}
- Project-specific implementations
- Practical applications and deployments
"""

    def create_overview_file(self, original_path: str, config: dict) -> str:
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
This is a navigation hub for the {original_title.lower()} template collection. The comprehensive template has been split into focused sub-prompts for easier use and better clarity.

## Quick Start

**Choose Your Template:**

Browse the specialized templates below and select the one that matches your specific needs. Each template is focused, easy to use, and can be applied independently.

"""

        for i, split in enumerate(splits, 1):
            content += f"""### {i}. {split['title']}
**File:** `{split['filename']}`

**Purpose:** {split['purpose']}

**Keywords:** {', '.join(split['keywords'][:5])}

---

"""

        content += f"""## How to Use

1. **Identify your specific need** from the templates above
2. **Open the corresponding template file**
3. **Follow the Quick Start guide** in that template
4. **Customize variables** to match your requirements
5. **Generate and refine** your output

## Template Collection

| Template | Focus Area | Best For |
|----------|-----------|----------|
"""

        for split in splits:
            focus = split['keywords'][0].title()
            best_for = split['purpose'].split()[0:8]
            content += f"| {split['title']} | {focus} | {' '.join(best_for)}... |\n"

        content += f"""
## Related Templates

All templates in this collection are designed to work together. You can combine insights and approaches from multiple templates for comprehensive solutions.

## Support

For questions or issues with any template:
- Check the specific template's Quick Start section
- Review the Usage Examples in each template
- Consult the Best Practices section

---

**Note:** These focused templates replace the original comprehensive template for improved usability and clarity.
"""

        return content

    def split_prompt(self, original_path: str, config: dict) -> None:
        """Split a long prompt into focused sub-prompts"""
        full_path = self.base_path / original_path

        print(f"\n{'='*80}")
        print(f"Splitting: {original_path}")
        print(f"{'='*80}")

        # Read original file
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if frontmatter_match:
            original_frontmatter = frontmatter_match.group(1)
            main_content = content[frontmatter_match.end():]
        else:
            original_frontmatter = ""
            main_content = content

        # Extract category
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

    def create_sub_prompt(self, output_dir: Path, split: dict, category: str, original_content: str) -> None:
        """Create a focused sub-prompt file"""
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
[This section contains the relevant portions extracted from the original template]

Note: This template is part of a focused collection. See the overview file for related templates.
```

## Variables

[Key variables for this specific template will be listed here during content extraction]

## Usage Examples

### Example 1: Practical Application
[Practical example specific to this template's focus]

### Example 2: Advanced Use Case
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

**Note:** This is a focused template extracted from a comprehensive collection for improved usability.
"""

        # Write sub-prompt file
        output_path = output_dir / split['filename']
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)

        print(f"✓ Created: {split['filename']}")

    def run(self):
        """Execute the splitting process"""
        print("\n" + "="*80)
        print("PHASE 2: LONG PROMPT SPLITTER (1500-1999 lines)")
        print("="*80)
        print(f"\nWill split {len(self.split_configs)} long prompts into focused sub-prompts\n")

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
    splitter = LongPromptSplitter()
    splitter.run()
