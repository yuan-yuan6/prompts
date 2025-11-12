#!/usr/bin/env python3
"""
Consolidate and standardize tags across all templates.

This script:
1. Consolidates AI/ML tags (data-science, machine-learning, nlp, etc.) → ai-ml
2. Consolidates healthcare specialization tags → healthcare
3. Removes deprecated tags (business, industry, technology, navigation, etc.)
4. Removes single-use tags
5. Standardizes tag naming
6. Enforces maximum 7 tags per template
"""

import os
import re
import yaml
import shutil
from collections import Counter

class TagConsolidator:
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.changes = []

        # Tag consolidation mappings
        self.consolidation_map = {
            # AI/ML consolidation
            'data-science': 'ai-ml',
            'machine-learning': 'ai-ml',
            'nlp': 'ai-ml',
            'sentiment-analysis': 'ai-ml',
            'emotion-detection': 'ai-ml',
            'causal-inference': 'ai-ml',
            'deep-learning': 'ai-ml',
            'neural-networks': 'ai-ml',

            # Healthcare - keep healthcare, remove specializations
            'telemedicine': None,  # Remove, redundant
            'clinical-practice': None,
            'public-health': None,
            'health-policy': None,
            'health-education': None,
            'acute-care': None,
            'critical-care': None,
            'chronic-care': None,
            'behavioral-health': None,
            'mental-health': None,

            # Deprecated - redundant with category structure
            'business': None,
            'industry': None,
            'technology': None,
            'navigation': None,
            'reference': None,
            'comprehensive': None,
            'overview': None,

            # Content type - use sparingly
            'template': None,  # Redundant, everything is a template

            # Function consolidations
            'professional-services': 'management',  # Consolidate
        }

        # Standard tags to keep
        self.standard_tags = {
            # Core functions
            'strategy', 'management', 'optimization', 'development', 'operations',
            'communication', 'marketing', 'automation', 'security', 'testing',
            'analysis', 'planning', 'creative', 'evaluation', 'implementation',

            # Technology domains
            'ai-ml', 'data-analytics', 'infrastructure', 'devops', 'cloud',
            'database', 'web', 'mobile', 'api',

            # Industries
            'healthcare', 'finance', 'education', 'government', 'nonprofit',
            'retail', 'manufacturing', 'automotive', 'transportation',

            # Content types (selective)
            'framework', 'research', 'documentation', 'design',

            # Use cases
            'personal', 'enterprise', 'startup', 'remote-work',

            # Specialized
            'compliance', 'risk-management', 'quality-assurance', 'hr',
            'legal', 'sales', 'customer-experience', 'data-quality',
        }

    def consolidate_tags(self, tags):
        """Consolidate tags according to mapping"""
        if not isinstance(tags, list):
            return tags

        new_tags = []
        for tag in tags:
            # Apply consolidation mapping
            if tag in self.consolidation_map:
                mapped = self.consolidation_map[tag]
                if mapped and mapped not in new_tags:
                    new_tags.append(mapped)
            elif tag in self.standard_tags:
                if tag not in new_tags:
                    new_tags.append(tag)
            # Skip tags not in standard list and not mapped

        # Limit to 7 tags
        return new_tags[:7]

    def process_file(self, filepath):
        """Process a single file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return False

        # Extract YAML frontmatter
        match = re.match(r'^(---\s*\n)(.*?\n)(---\s*\n)', content, re.DOTALL)
        if not match:
            return False

        yaml_header = match.group(1)
        yaml_content = match.group(2)
        yaml_footer = match.group(3)
        rest_content = content[len(match.group(0)):]

        try:
            metadata = yaml.safe_load(yaml_content)
        except:
            return False

        if not metadata or 'tags' not in metadata:
            return False

        original_tags = metadata['tags']
        new_tags = self.consolidate_tags(original_tags)

        if original_tags != new_tags:
            # Update metadata
            metadata['tags'] = new_tags

            # Reconstruct YAML
            new_yaml = yaml.dump(metadata, default_flow_style=False, allow_unicode=True, sort_keys=False)
            new_content = yaml_header + new_yaml + yaml_footer + rest_content

            if not self.dry_run:
                # Backup
                shutil.copy2(filepath, filepath + '.backup')

                # Write
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

            self.changes.append({
                'file': filepath,
                'old_tags': original_tags,
                'new_tags': new_tags,
                'removed': len(original_tags) - len(new_tags)
            })

            return True

        return False

    def run(self):
        """Run consolidation"""
        print("=" * 70)
        print("TAG CONSOLIDATION")
        print("=" * 70)
        print(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE'}")
        print()

        # Find all templates
        templates = []
        for root, dirs, files in os.walk('.'):
            if '.git' in root or 'scripts' in root:
                continue

            for file in files:
                if file.endswith('.md') and 'README' not in file and 'INDEX' not in file:
                    templates.append(os.path.join(root, file))

        print(f"Processing {len(templates)} templates...")

        # Process each
        for filepath in templates:
            self.process_file(filepath)

        # Report
        print("\n" + "=" * 70)
        print("RESULTS")
        print("=" * 70)
        print(f"\nFiles processed: {len(templates)}")
        print(f"Files changed: {len(self.changes)}")
        print(f"Total tags removed: {sum(c['removed'] for c in self.changes)}")

        if self.changes:
            print("\n" + "=" * 70)
            print("SAMPLE CHANGES (First 15)")
            print("=" * 70)

            for i, change in enumerate(self.changes[:15]):
                print(f"\n{i+1}. {change['file']}")
                print(f"   Old ({len(change['old_tags'])} tags): {', '.join(change['old_tags'][:10])}")
                if len(change['old_tags']) > 10:
                    print(f"                      ... and {len(change['old_tags']) - 10} more")
                print(f"   New ({len(change['new_tags'])} tags): {', '.join(change['new_tags'])}")
                print(f"   Removed: {change['removed']} tags")

        # Tag statistics
        all_new_tags = []
        for change in self.changes:
            all_new_tags.extend(change['new_tags'])

        tag_counts = Counter(all_new_tags)

        print("\n" + "=" * 70)
        print("NEW TAG DISTRIBUTION (Top 30)")
        print("=" * 70)
        for tag, count in tag_counts.most_common(30):
            print(f"{tag:30} {count:>4}")

        if self.dry_run:
            print("\n" + "=" * 70)
            print("DRY RUN COMPLETE - No changes made")
            print("=" * 70)
            print("Run with --live to apply changes")
        else:
            print("\n" + "=" * 70)
            print("CHANGES APPLIED")
            print("=" * 70)

if __name__ == "__main__":
    import sys
    dry_run = '--live' not in sys.argv

    consolidator = TagConsolidator(dry_run=dry_run)
    consolidator.run()
