#!/usr/bin/env python3
"""
Generate comprehensive INDEX.md file from all templates in repository.

This script:
1. Scans all template files
2. Extracts metadata from YAML frontmatter
3. Generates INDEX.md with:
   - Statistics
   - By Category view
   - Alphabetical view
   - Category statistics
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime

class IndexGenerator:
    def __init__(self):
        self.templates = []
        self.categories = defaultdict(list)
        self.subcategories = defaultdict(list)

    def extract_metadata(self, filepath):
        """Extract YAML frontmatter from markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Look for YAML frontmatter
            match = re.match(r'^---\s*\n(.*?\n)---\s*\n', content, re.DOTALL)
            if match:
                yaml_content = match.group(1)
                try:
                    metadata = yaml.safe_load(yaml_content)
                    if metadata:
                        metadata['filepath'] = filepath.lstrip('./')
                        return metadata
                except:
                    pass
        except:
            pass

        # If no metadata, create minimal entry
        return {
            'filepath': filepath.lstrip('./'),
            'title': os.path.basename(filepath).replace('.md', '').replace('-', ' ').title(),
            'category': self._guess_category(filepath),
            'tags': [],
            'use_cases': []
        }

    def _guess_category(self, filepath):
        """Guess category from filepath"""
        parts = filepath.split('/')
        if len(parts) > 1:
            category = parts[1]
            if len(parts) > 2 and parts[2] not in ['README.md']:
                return f"{parts[1]}/{parts[2]}"
            return category
        return "uncategorized"

    def scan_repository(self):
        """Scan repository for all template files"""
        exclude_patterns = [
            'README.md', 'INDEX.md', 'CHANGELOG.md', 'LICENSE',
            '_VIEW.md', 'GUIDE.md', 'SUMMARY.md', 'PLAN.md',
            'STATUS.md', 'COMPLETE.md', 'ANALYSIS.md', 'TRACKER.md',
            'RECOMMENDATIONS.md', 'TAXONOMY.md', 'FEASIBILITY.md',
            'REFACTORING.md', 'IMPROVEMENTS.md', 'PROMPT_', '.backup'
        ]

        for root, dirs, files in os.walk('.'):
            if '.git' in root or 'scripts' in root:
                continue

            for file in files:
                if not file.endswith('.md'):
                    continue

                # Skip documentation files
                if any(p in file for p in exclude_patterns):
                    continue

                filepath = os.path.join(root, file)
                metadata = self.extract_metadata(filepath)

                if metadata:
                    self.templates.append(metadata)

                    # Categorize
                    category = metadata.get('category', 'uncategorized')
                    main_category = category.split('/')[0] if '/' in category else category
                    self.categories[main_category].append(metadata)

                    if '/' in category:
                        self.subcategories[category].append(metadata)

        print(f"Scanned {len(self.templates)} templates")
        print(f"Found {len(self.categories)} main categories")
        print(f"Found {len(self.subcategories)} subcategories")

    def generate_index(self):
        """Generate INDEX.md content"""
        lines = []

        # Header
        lines.append("# Prompts Database Index")
        lines.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        lines.append("")

        # Statistics
        lines.append("## Statistics")
        lines.append("")
        lines.append(f"- **Total Templates:** {len(self.templates)}")
        lines.append(f"- **Main Categories:** {len(self.categories)}")
        lines.append(f"- **Subcategories:** {len(self.subcategories)}")
        lines.append("")

        # Table of Contents
        lines.append("## Table of Contents")
        lines.append("")
        lines.append("1. [By Category](#by-category)")
        lines.append("2. [Alphabetical Index](#alphabetical-index)")
        lines.append("3. [Category Statistics](#category-statistics)")
        lines.append("")

        # By Category
        lines.append("## By Category")
        lines.append("")

        for category in sorted(self.categories.keys()):
            templates = self.categories[category]
            category_name = category.replace('-', ' ').title()
            lines.append(f"### {category_name} ({len(templates)})")
            lines.append("")

            # Sort templates alphabetically
            sorted_templates = sorted(templates, key=lambda t: t.get('title', ''))

            for template in sorted_templates:
                title = template.get('title', 'Untitled')
                filepath = template.get('filepath', '')
                category = template.get('category', '')

                lines.append(f"- [{title}]({filepath}) - `{category}`")

            lines.append("")

        # Alphabetical Index
        lines.append("## Alphabetical Index")
        lines.append("")

        sorted_all = sorted(self.templates, key=lambda t: t.get('title', '').lower())

        current_letter = None
        for template in sorted_all:
            title = template.get('title', 'Untitled')
            first_letter = title[0].upper() if title else 'Z'

            if first_letter != current_letter:
                current_letter = first_letter
                lines.append(f"### {current_letter}")
                lines.append("")

            filepath = template.get('filepath', '')
            category = template.get('category', '')

            lines.append(f"- [{title}]({filepath}) - `{category}`")

        lines.append("")

        # Category Statistics
        lines.append("## Category Statistics")
        lines.append("")
        lines.append("| Category | Template Count | Percentage |")
        lines.append("|----------|----------------|------------|")

        total = len(self.templates)
        sorted_categories = sorted(self.categories.items(), key=lambda x: len(x[1]), reverse=True)

        for category, templates in sorted_categories:
            count = len(templates)
            percentage = (count / total * 100) if total > 0 else 0
            category_name = category.replace('-', ' ').title()
            lines.append(f"| {category_name} | {count} | {percentage:.1f}% |")

        lines.append("")

        # Footer
        lines.append("---")
        lines.append("")
        lines.append("*Generated automatically by generate_index.py*")
        lines.append("")

        return '\n'.join(lines)

    def write_index(self, output_path='INDEX.md'):
        """Write INDEX.md file"""
        content = self.generate_index()

        # Backup existing INDEX if it exists
        if os.path.exists(output_path):
            backup_path = output_path + '.backup'
            import shutil
            shutil.copy2(output_path, backup_path)
            print(f"Backed up existing INDEX to {backup_path}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Generated {output_path}")
        print(f"Total templates indexed: {len(self.templates)}")

    def run(self):
        """Run the generator"""
        print("=" * 70)
        print("INDEX.MD GENERATOR")
        print("=" * 70)
        print()

        self.scan_repository()
        self.write_index()

        print("\n" + "=" * 70)
        print("GENERATION COMPLETE")
        print("=" * 70)

if __name__ == "__main__":
    generator = IndexGenerator()
    generator.run()
