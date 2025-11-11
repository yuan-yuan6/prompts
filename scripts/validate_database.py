#!/usr/bin/env python3
"""
Automated validation script for prompts database
Checks:
- YAML frontmatter completeness
- Category validity
- Related_templates link integrity
- File naming conventions
- Directory structure compliance
"""
import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

class DatabaseValidator:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.errors = []
        self.warnings = []
        self.stats = {
            'total_files': 0,
            'valid_files': 0,
            'errors': 0,
            'warnings': 0
        }

        # Valid top-level categories
        self.valid_categories = {
            'communication', 'content-creation', 'data-analytics', 'design',
            'education', 'finance', 'government', 'healthcare', 'human-resources',
            'legal-compliance', 'media-journalism', 'nonprofit', 'operations',
            'personal', 'sales-marketing', 'security', 'strategy', 'technology'
        }

        # Required frontmatter fields
        self.required_fields = ['category', 'title', 'tags', 'use_cases', 'last_updated']

    def validate_yaml_frontmatter(self, filepath, content):
        """Validate YAML frontmatter structure and required fields"""
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)

        if not frontmatter_match:
            self.errors.append(f"{filepath}: Missing YAML frontmatter")
            return None

        try:
            frontmatter = yaml.safe_load(frontmatter_match.group(1))
        except yaml.YAMLError as e:
            self.errors.append(f"{filepath}: Invalid YAML - {e}")
            return None

        # Check required fields
        for field in self.required_fields:
            if field not in frontmatter:
                self.errors.append(f"{filepath}: Missing required field '{field}'")

        return frontmatter

    def validate_category(self, filepath, category):
        """Validate category field matches directory structure"""
        if not category:
            return

        # Get top-level category
        top_cat = category.split('/')[0] if '/' in category else category

        if top_cat not in self.valid_categories:
            self.errors.append(f"{filepath}: Invalid category '{category}'. Top-level must be one of: {', '.join(sorted(self.valid_categories))}")

        # Check if category matches file location
        rel_path = filepath.relative_to(self.base_dir)
        file_cat = str(rel_path.parent).replace(os.sep, '/')

        if file_cat != category and file_cat != '.':
            self.warnings.append(f"{filepath}: Category '{category}' doesn't match file location '{file_cat}'")

    def validate_related_templates(self, filepath, related_templates):
        """Validate that related_templates references exist"""
        if not related_templates:
            return

        current_dir = filepath.parent

        for ref in related_templates:
            # Try relative to current file
            ref_path = current_dir / ref
            if not ref_path.exists():
                # Try relative to base dir
                ref_path = self.base_dir / ref
                if not ref_path.exists():
                    self.warnings.append(f"{filepath}: related_templates reference not found: '{ref}'")

    def validate_file_naming(self, filepath):
        """Validate file naming conventions"""
        filename = filepath.name

        # Should be kebab-case
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*\.md$', filename):
            self.warnings.append(f"{filepath}: Filename should be kebab-case (lowercase with hyphens)")

    def validate_tags(self, filepath, tags):
        """Validate tags structure"""
        if not tags:
            self.warnings.append(f"{filepath}: No tags defined")
            return

        if not isinstance(tags, list):
            self.errors.append(f"{filepath}: Tags should be a list")
            return

        if len(tags) == 0:
            self.warnings.append(f"{filepath}: Empty tags list")

        if len(tags) > 15:
            self.warnings.append(f"{filepath}: Excessive tags ({len(tags)}). Recommended: 5-10")

    def validate_use_cases(self, filepath, use_cases):
        """Validate use_cases structure"""
        if not use_cases:
            self.warnings.append(f"{filepath}: No use_cases defined")
            return

        if not isinstance(use_cases, list):
            self.errors.append(f"{filepath}: use_cases should be a list")
            return

        if len(use_cases) == 0:
            self.warnings.append(f"{filepath}: Empty use_cases list")

    def validate_last_updated(self, filepath, last_updated):
        """Validate last_updated date format"""
        if not last_updated:
            return

        # Should be YYYY-MM-DD format
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(last_updated)):
            self.errors.append(f"{filepath}: last_updated should be YYYY-MM-DD format, got '{last_updated}'")

    def validate_file(self, filepath):
        """Validate a single markdown file"""
        self.stats['total_files'] += 1

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Validate frontmatter
            frontmatter = self.validate_yaml_frontmatter(filepath, content)

            if frontmatter:
                # Validate individual fields
                self.validate_category(filepath, frontmatter.get('category'))
                self.validate_related_templates(filepath, frontmatter.get('related_templates'))
                self.validate_file_naming(filepath)
                self.validate_tags(filepath, frontmatter.get('tags'))
                self.validate_use_cases(filepath, frontmatter.get('use_cases'))
                self.validate_last_updated(filepath, frontmatter.get('last_updated'))

                self.stats['valid_files'] += 1

        except Exception as e:
            self.errors.append(f"{filepath}: Unexpected error - {e}")

    def run(self):
        """Run validation on entire database"""
        print("🔍 Validating prompts database...")
        print(f"Base directory: {self.base_dir}")
        print()

        # Find all markdown files
        exclude_files = {'README.md', 'INDEX.md', 'CLASSIFICATION_GUIDE.md',
                        'TAG_TAXONOMY.md', 'INDUSTRY_VIEW.md', 'TECHNOLOGY_VIEW.md',
                        'USE_CASE_VIEW.md', 'CHANGELOG.md'}

        for md_file in self.base_dir.rglob('*.md'):
            # Skip excluded files and directories
            if md_file.name in exclude_files:
                continue
            if '.git' in str(md_file) or '.templates' in str(md_file):
                continue

            self.validate_file(md_file)

        # Update stats
        self.stats['errors'] = len(self.errors)
        self.stats['warnings'] = len(self.warnings)

        # Print results
        self.print_report()

        # Return exit code (0 = success, 1 = errors found)
        return 0 if self.stats['errors'] == 0 else 1

    def print_report(self):
        """Print validation report"""
        print("\n" + "="*80)
        print("📊 VALIDATION REPORT")
        print("="*80)
        print()

        print(f"✓ Total files validated: {self.stats['total_files']}")
        print(f"✓ Valid files: {self.stats['valid_files']}")
        print(f"❌ Errors: {self.stats['errors']}")
        print(f"⚠️  Warnings: {self.stats['warnings']}")
        print()

        if self.errors:
            print("="*80)
            print("❌ ERRORS")
            print("="*80)
            for error in self.errors[:50]:  # Show first 50 errors
                print(f"  • {error}")
            if len(self.errors) > 50:
                print(f"  ... and {len(self.errors) - 50} more errors")
            print()

        if self.warnings:
            print("="*80)
            print("⚠️  WARNINGS")
            print("="*80)
            for warning in self.warnings[:50]:  # Show first 50 warnings
                print(f"  • {warning}")
            if len(self.warnings) > 50:
                print(f"  ... and {len(self.warnings) - 50} more warnings")
            print()

        if self.stats['errors'] == 0 and self.stats['warnings'] == 0:
            print("✅ All checks passed! Database is valid.")
        elif self.stats['errors'] == 0:
            print("✅ No errors found. Please review warnings.")
        else:
            print("❌ Validation failed. Please fix errors above.")

        print()


def main():
    base_dir = Path(__file__).parent.parent
    validator = DatabaseValidator(base_dir)
    exit_code = validator.run()

    # Write report to file for CI/CD
    report_file = base_dir / 'validation_report.txt'
    with open(report_file, 'w') as f:
        f.write(f"Validation Report\n")
        f.write(f"=================\n\n")
        f.write(f"Total files: {validator.stats['total_files']}\n")
        f.write(f"Valid files: {validator.stats['valid_files']}\n")
        f.write(f"Errors: {validator.stats['errors']}\n")
        f.write(f"Warnings: {validator.stats['warnings']}\n")

    exit(exit_code)


if __name__ == '__main__':
    main()
