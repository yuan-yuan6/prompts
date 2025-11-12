#!/usr/bin/env python3
"""
Add industry tags to all templates based on their applicability.

This script:
1. Analyzes each template's category, title, and content
2. Adds relevant industry tags based on applicability
3. Creates industry-specific discovery capability
"""

import os
import re
import yaml
import shutil

class IndustryTagger:
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.changes = []

        # Define industry categories and their indicators
        self.industries = {
            'healthcare': {
                'keywords': ['health', 'medical', 'patient', 'clinical', 'hospital', 'hipaa', 'phi', 'telehealth', 'wellness'],
                'categories': ['healthcare']
            },
            'finance': {
                'keywords': ['financial', 'banking', 'payment', 'trading', 'investment', 'pci-dss', 'pci', 'wealth', 'fintech'],
                'categories': ['finance']
            },
            'technology': {
                'keywords': ['software', 'saas', 'cloud', 'api', 'devops', 'infrastructure', 'cybersecurity'],
                'categories': ['technology', 'security', 'data-analytics']
            },
            'retail': {
                'keywords': ['retail', 'ecommerce', 'e-commerce', 'storefront', 'catalog', 'inventory', 'customer-experience'],
                'categories': ['sales-marketing']
            },
            'manufacturing': {
                'keywords': ['manufacturing', 'production', 'factory', 'supply-chain', 'lean', 'six-sigma', 'quality'],
                'categories': ['operations']
            },
            'education': {
                'keywords': ['education', 'learning', 'course', 'curriculum', 'teaching', 'student', 'academic'],
                'categories': ['education']
            },
            'government': {
                'keywords': ['government', 'policy', 'public', 'federal', 'regulatory', 'compliance', 'fedramp'],
                'categories': ['government']
            },
            'nonprofit': {
                'keywords': ['nonprofit', 'fundraising', 'donor', 'volunteer', 'grant', 'charitable'],
                'categories': ['nonprofit']
            }
        }

        # Universal applicability - these templates apply to all industries
        self.universal_categories = {
            'communication', 'human-resources', 'strategy', 'legal-compliance',
            'personal', 'operations'
        }

    def get_industry_tags(self, filepath, metadata):
        """Determine which industry tags apply to this template"""
        industries = set()

        # Get category
        category = metadata.get('category', '')
        main_category = category.split('/')[0] if category else ''

        # Read file content for keyword analysis
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().lower()
        except:
            content = ''

        # Check each industry
        for industry, config in self.industries.items():
            # Direct category match
            if main_category in config['categories']:
                industries.add(industry)
                continue

            # Keyword matching
            keyword_matches = sum(1 for keyword in config['keywords'] if keyword in content)
            if keyword_matches >= 2:  # Require at least 2 keyword matches
                industries.add(industry)

        # Universal templates get multiple industry tags
        if main_category in self.universal_categories:
            # Add common industries for universal templates
            industries.update(['technology', 'finance', 'healthcare', 'retail', 'manufacturing'])

        return sorted(list(industries))

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

        if not metadata:
            return False

        # Determine applicable industries
        industry_tags = self.get_industry_tags(filepath, metadata)

        # Skip if no industries or already has industries field
        if not industry_tags or 'industries' in metadata:
            return False

        # Add industries field
        metadata['industries'] = industry_tags

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
            'industries': industry_tags
        })

        return True

    def run(self):
        """Run the tagger"""
        print("=" * 70)
        print("INDUSTRY TAGGING SYSTEM")
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
        print(f"Files tagged: {len(self.changes)}")

        if self.changes:
            # Count industries
            from collections import Counter
            industry_counts = Counter()
            for change in self.changes:
                for industry in change['industries']:
                    industry_counts[industry] += 1

            print("\n" + "=" * 70)
            print("INDUSTRY DISTRIBUTION")
            print("=" * 70)
            for industry, count in industry_counts.most_common():
                print(f"{industry:20} {count:>4} templates")

            print("\n" + "=" * 70)
            print("SAMPLE CHANGES (First 20)")
            print("=" * 70)
            for i, change in enumerate(self.changes[:20]):
                print(f"\n{i+1}. {change['file']}")
                print(f"   Industries: {', '.join(change['industries'])}")

        if self.dry_run:
            print("\n" + "=" * 70)
            print("DRY RUN COMPLETE")
            print("=" * 70)
            print("Run with --live to apply changes")
        else:
            print("\n" + "=" * 70)
            print("CHANGES APPLIED")
            print("=" * 70)

if __name__ == "__main__":
    import sys
    dry_run = '--live' not in sys.argv

    tagger = IndustryTagger(dry_run=dry_run)
    tagger.run()
