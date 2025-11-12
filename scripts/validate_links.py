#!/usr/bin/env python3
"""
Link Validation Script for Prompts Database

Validates related_templates references in YAML frontmatter
and detects broken links.

Usage: python3 validate_links.py
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple
import yaml

def extract_yaml_frontmatter(content: str) -> Dict:
    """Extract YAML frontmatter from markdown file."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return {}
    return {}

def find_template_file(template_ref: str, base_path: Path) -> bool:
    """Check if a template file exists."""
    # Try exact path first
    if (base_path / template_ref).exists():
        return True

    # Try with .md extension if missing
    if not template_ref.endswith('.md'):
        if (base_path / f"{template_ref}.md").exists():
            return True

    # Try relative paths from root
    for root, dirs, files in os.walk(base_path):
        # Skip hidden directories
        if '/.git' in root or '/.github' in root:
            continue

        # Check if filename matches
        template_name = Path(template_ref).name
        if template_name in files:
            return True

    return False

def validate_file_links(file_path: Path, base_path: Path) -> List[str]:
    """Validate all related_templates in a file."""
    broken_links = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter = extract_yaml_frontmatter(content)

        if 'related_templates' in frontmatter:
            related = frontmatter['related_templates']

            # Handle both list and single string
            if isinstance(related, str):
                related = [related]
            elif not isinstance(related, list):
                return broken_links

            for template_ref in related:
                if not template_ref or template_ref == 'null':
                    continue

                if not find_template_file(template_ref, base_path):
                    broken_links.append(template_ref)

    except Exception as e:
        print(f"  Error reading {file_path}: {e}")

    return broken_links

def main():
    """Main validation function."""
    base_path = Path(__file__).parent.parent

    print("🔍 Validating related_templates links across all markdown files...\n")

    all_files = []
    for root, dirs, files in os.walk(base_path):
        # Skip hidden directories and scripts
        if '/.git' in root or '/.github' in root or '/scripts' in root:
            continue

        for file in files:
            if file.endswith('.md'):
                all_files.append(Path(root) / file)

    print(f"📊 Found {len(all_files)} markdown files to check\n")

    files_with_issues = []
    total_broken_links = 0

    for file_path in sorted(all_files):
        broken_links = validate_file_links(file_path, base_path)

        if broken_links:
            rel_path = file_path.relative_to(base_path)
            files_with_issues.append((rel_path, broken_links))
            total_broken_links += len(broken_links)

    # Report results
    print("=" * 80)
    print("VALIDATION RESULTS")
    print("=" * 80)
    print()

    if files_with_issues:
        print(f"❌ Found {total_broken_links} broken links in {len(files_with_issues)} files:\n")

        for rel_path, broken_links in files_with_issues:
            print(f"📄 {rel_path}")
            for link in broken_links:
                print(f"   ❌ {link}")
            print()
    else:
        print("✅ All related_templates links are valid!\n")

    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total files checked: {len(all_files)}")
    print(f"Files with broken links: {len(files_with_issues)}")
    print(f"Total broken links: {total_broken_links}")
    print()

    if files_with_issues:
        print("💡 Recommendation: Run update_links.py to fix these broken references")
        return 1
    else:
        print("✅ Database integrity check passed!")
        return 0

if __name__ == "__main__":
    exit(main())
