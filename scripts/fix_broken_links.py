#!/usr/bin/env python3
"""
Fix Broken Links Script

Automatically fixes broken related_templates references.
"""

import os
import re
from pathlib import Path
from typing import Dict, List
import yaml

# Mapping of broken links to correct paths or None (to remove)
LINK_FIXES = {
    # Design files
    "design/user-experience-audit.md": None,  # Doesn't exist, remove

    # Finance files
    "financial-analysis.md": "finance/Corporate-Finance/financial-analysis-overview.md",

    # Operations files
    "operations/business-continuity-planning.md": None,  # Doesn't exist, remove
    "operations/program-management.md": None,  # Doesn't exist, remove
    "operations/business-model-design.md": None,  # Doesn't exist, remove
    "operations/supply-chain-optimization.md": None,  # Doesn't exist, remove
    "operations/operational-efficiency.md": None,  # Doesn't exist, remove
    "operations/process-improvement.md": None,  # Doesn't exist, remove
    "operations/organizational-development.md": None,  # Doesn't exist, remove

    # Legal-compliance files
    "legal-compliance/contract-management.md": None,  # Doesn't exist, remove
    "legal-compliance/regulatory-compliance.md": None,  # Doesn't exist, remove
    "legal-compliance/ethics-compliance.md": None,  # Doesn't exist, remove
    "legal-compliance/corporate-governance.md": None,  # Doesn't exist, remove

    # Strategy files - use business-planning as closest match
    "strategy/strategic-planning.md": "strategy/business-planning.md",
    "strategic-planning.md": "strategy/business-planning.md",

    # Sales-marketing files
    "sales-marketing/partnership-development.md": None,  # Doesn't exist, remove
    "sales-marketing/brand-strategy.md": "sales-marketing/Marketing-Creative/brand-storytelling-comprehensive.md",

    # Human resources files
    "human-resources/recruitment.md": "human-resources/recruitment-overview.md",
    "human-resources/talent-acquisition.md": "human-resources/talent-acquisition-strategy.md",
    "human-resources/performance-management.md": "human-resources/hr-performance-management.md",

    # Security files
    "security/Application-Security/owasp-security-testing.md": None,  # Doesn't exist, remove
    "security/Compliance-Governance/compliance-management.md": None,  # Doesn't exist, remove

    # Technology files
    "api-design.md": None,  # Need to check what exists
    "testing-strategy.md": None,  # Need to check what exists
}

def find_file_in_tree(filename: str, base_path: Path) -> str:
    """Search for a file in the directory tree."""
    for root, dirs, files in os.walk(base_path):
        if '/.git' in root or '/.github' in root:
            continue
        if filename in files:
            full_path = Path(root) / filename
            return str(full_path.relative_to(base_path))
    return None

def extract_and_fix_yaml(content: str, fixes: Dict[str, str]) -> str:
    """Extract YAML frontmatter, fix links, and reconstruct content."""
    pattern = r'^(---\s*\n)(.*?)(\n---\s*\n)'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return content

    yaml_content = match.group(2)
    rest_of_content = content[match.end():]

    try:
        data = yaml.safe_load(yaml_content)
    except yaml.YAMLError:
        return content

    if 'related_templates' not in data:
        return content

    related = data['related_templates']

    # Handle both list and single string
    if isinstance(related, str):
        related = [related]
    elif not isinstance(related, list):
        return content

    # Fix or remove broken links
    fixed_related = []
    changed = False

    for template_ref in related:
        if not template_ref or template_ref == 'null':
            continue

        if template_ref in fixes:
            changed = True
            if fixes[template_ref] is not None:
                fixed_related.append(fixes[template_ref])
            # If None, we skip (remove) the link
        else:
            fixed_related.append(template_ref)

    if not changed:
        return content

    # Update the data
    if fixed_related:
        data['related_templates'] = fixed_related
    else:
        del data['related_templates']

    # Reconstruct YAML
    new_yaml = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return match.group(1) + new_yaml + match.group(3) + rest_of_content

def main():
    """Main fix function."""
    base_path = Path(__file__).parent.parent

    print("🔧 Fixing broken related_templates links...\n")

    # First, let's check which files from LINK_FIXES actually exist
    print("📊 Checking which referenced files exist...\n")

    for broken_link, suggested_fix in LINK_FIXES.items():
        if suggested_fix and suggested_fix != broken_link:
            file_path = base_path / suggested_fix
            if file_path.exists():
                print(f"  ✅ {broken_link} → {suggested_fix}")
            else:
                print(f"  ❌ {suggested_fix} doesn't exist (suggested fix for {broken_link})")

    print("\n🔍 Scanning for files with broken links...\n")

    files_fixed = 0
    links_fixed = 0

    for root, dirs, files in os.walk(base_path):
        if '/.git' in root or '/.github' in root or '/scripts' in root:
            continue

        for file in files:
            if not file.endswith('.md'):
                continue

            file_path = Path(root) / file

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = extract_and_fix_yaml(content, LINK_FIXES)

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                    rel_path = file_path.relative_to(base_path)
                    print(f"  ✅ Fixed: {rel_path}")
                    files_fixed += 1

                    # Count how many links were fixed
                    original_matches = set(re.findall(r'related_templates:.*?\n(?:  - .*?\n)*', content, re.DOTALL))
                    new_matches = set(re.findall(r'related_templates:.*?\n(?:  - .*?\n)*', new_content, re.DOTALL))

                    if original_matches and new_matches:
                        orig_count = content.count('- ')
                        new_count = new_content.count('- ')
                        links_fixed += abs(orig_count - new_count)

            except Exception as e:
                print(f"  ❌ Error processing {file_path}: {e}")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Files fixed: {files_fixed}")
    print(f"Links fixed/removed: {links_fixed}")
    print()
    print("✅ Run validate_links.py to verify fixes")

if __name__ == "__main__":
    main()
