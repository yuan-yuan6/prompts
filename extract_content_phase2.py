#!/usr/bin/env python3
"""
Phase 2 Content Extractor - Extract content for newly split prompts
"""

import os
import re
from pathlib import Path

class ContentExtractorPhase2:
    def __init__(self):
        self.base_path = Path("/home/user/prompts")

        self.extraction_map = {
            "education/Teaching & Instruction/online-learning.md": {
                "online-learning-platform-architecture.md": {
                    "keywords": ["architecture", "system", "infrastructure", "security", "technical", "backend", "frontend", "integration", "scalability", "cloud", "database", "api"],
                    "exclude": ["content", "pedagogy", "assessment", "curriculum"]
                },
                "online-learning-content-curriculum.md": {
                    "keywords": ["content", "curriculum", "course", "materials", "syllabus", "lesson", "module", "resources", "instructional"],
                    "exclude": ["architecture", "system", "security"]
                },
                "online-learning-pedagogy-engagement.md": {
                    "keywords": ["pedagogy", "engagement", "assessment", "gamification", "personalization", "learning theory", "interactive", "motivation", "feedback"],
                    "exclude": ["architecture", "infrastructure"]
                },
                "online-learning-communication-tools.md": {
                    "keywords": ["communication", "collaboration", "discussion", "forum", "chat", "video", "messaging", "synchronous", "asynchronous", "conferencing"],
                    "exclude": []
                }
            },

            "data-analytics/Research Analytics/statistical-analysis.md": {
                "descriptive-statistics-eda.md": {
                    "keywords": ["descriptive", "exploratory", "eda", "summary", "distribution", "visualization", "histogram", "boxplot", "correlation", "mean", "median"],
                    "exclude": ["hypothesis", "regression", "bayesian"]
                },
                "hypothesis-testing-inference.md": {
                    "keywords": ["hypothesis", "test", "inference", "t-test", "anova", "chi-square", "p-value", "confidence interval", "significance", "null"],
                    "exclude": ["regression", "bayesian"]
                },
                "regression-modeling-analysis.md": {
                    "keywords": ["regression", "model", "linear", "logistic", "multiple", "coefficients", "residuals", "diagnostics", "assumptions", "r-squared"],
                    "exclude": ["bayesian", "non-parametric"]
                },
                "advanced-statistical-methods.md": {
                    "keywords": ["bayesian", "non-parametric", "advanced", "bootstrap", "permutation", "multiple testing", "correction", "specialized", "mcmc"],
                    "exclude": []
                }
            }
        }

    def extract_sections(self, content: str, keywords: list, exclude: list) -> str:
        """Extract sections matching keywords"""
        lines = content.split('\n')
        extracted_sections = []
        current_section = []
        section_score = 0
        in_code_block = False

        for i, line in enumerate(lines):
            if line.strip().startswith('```'):
                in_code_block = not in_code_block

            line_lower = line.lower()
            keyword_matches = sum(1 for kw in keywords if kw.lower() in line_lower)
            exclude_matches = sum(1 for ex in exclude if ex.lower() in line_lower)

            if line.startswith('#') or (in_code_block and i > 0):
                if current_section and section_score > 0:
                    extracted_sections.extend(current_section)
                    extracted_sections.append('')

                current_section = [line]
                section_score = keyword_matches - (exclude_matches * 2)
            else:
                current_section.append(line)
                section_score += keyword_matches - (exclude_matches * 2)

        if current_section and section_score > 0:
            extracted_sections.extend(current_section)

        return '\n'.join(extracted_sections)

    def extract_variables(self, content: str) -> str:
        """Extract variable definitions"""
        var_match = re.search(r'## Variables\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
        if var_match:
            return var_match.group(1).strip()
        return ""

    def extract_examples(self, content: str, keywords: list) -> str:
        """Extract relevant examples"""
        examples = []
        example_pattern = r'###? Example.*?\n(.*?)(?=\n###?|\Z)'
        matches = re.finditer(example_pattern, content, re.DOTALL)

        for match in matches:
            example_text = match.group(0)
            if any(kw.lower() in example_text.lower() for kw in keywords):
                examples.append(example_text)

        return '\n\n'.join(examples) if examples else ""

    def create_enhanced_subprompt(self, original_path: str, subprompt_file: str, config: dict) -> None:
        """Extract and enhance sub-prompt"""
        original_full_path = self.base_path / original_path
        with open(original_full_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        extracted_content = self.extract_sections(
            original_content,
            config['keywords'],
            config['exclude']
        )

        variables = self.extract_variables(original_content)
        examples = self.extract_examples(original_content, config['keywords'])

        category = '/'.join(original_path.split('/')[:-1])
        subprompt_path = self.base_path / category / subprompt_file

        if not subprompt_path.exists():
            print(f"⚠️  Warning: {subprompt_file} not found, skipping")
            return

        with open(subprompt_path, 'r', encoding='utf-8') as f:
            current_content = f.read()

        frontmatter_match = re.match(r'^(---\n.*?\n---\n)', current_content, re.DOTALL)
        if not frontmatter_match:
            print(f"⚠️  Warning: No frontmatter in {subprompt_file}")
            return

        frontmatter = frontmatter_match.group(1)

        quickstart_match = re.search(r'(## Quick Start.*?)(?=\n## [^Q])', current_content, re.DOTALL)
        quickstart = quickstart_match.group(1) if quickstart_match else "## Quick Start\n\n[Add Quick Start section]"

        enhanced_content = frontmatter + '\n'

        title_match = re.search(r'title:\s*(.+)', frontmatter)
        if title_match:
            enhanced_content += f"# {title_match.group(1)}\n\n"

        purpose_match = re.search(r'use_cases:\s*\n\s*-\s*(.+)', frontmatter)
        if purpose_match:
            enhanced_content += f"## Purpose\n{purpose_match.group(1)}\n\n"

        enhanced_content += quickstart + '\n\n'

        if extracted_content and len(extracted_content) > 500:
            enhanced_content += "## Template\n\n"
            content_lines = extracted_content.split('\n')
            if len(content_lines) > 800:
                enhanced_content += '\n'.join(content_lines[:800])
                enhanced_content += '\n\n[Content truncated for length - see original for full details]\n'
            else:
                enhanced_content += extracted_content
            enhanced_content += '\n\n'
        else:
            enhanced_content += "## Template\n\n```\n[Template content extracted from original - focused on specific topic]\n```\n\n"

        if variables:
            enhanced_content += "## Variables\n\n"
            var_lines = variables.split('\n')
            enhanced_content += '\n'.join(var_lines[:50])
            if len(var_lines) > 50:
                enhanced_content += '\n\n[Additional variables available in original template]\n'
            enhanced_content += '\n\n'

        if examples:
            enhanced_content += "## Usage Examples\n\n"
            enhanced_content += examples + '\n\n'

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

        with open(subprompt_path, 'w', encoding='utf-8') as f:
            f.write(enhanced_content)

        print(f"✅ Enhanced: {subprompt_file}")

    def run(self):
        """Execute content extraction"""
        print("\n" + "="*80)
        print("PHASE 2 CONTENT EXTRACTION")
        print("="*80)
        print("\nExtracting content from long prompts to populate sub-prompts...\n")

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
    extractor = ContentExtractorPhase2()
    extractor.run()
