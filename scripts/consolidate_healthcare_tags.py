#!/usr/bin/env python3
"""
Healthcare Tag Consolidation Script

Consolidates low-frequency healthcare specialization tags into primary 'healthcare' tag.

Tags to remove (keep only 'healthcare'):
- telemedicine (3)
- public-health (2)
- clinical-practice (1)
- acute-care (1)
- critical-care (1)
- chronic-care (1)
- behavioral-health (1)
- mental-health (1)
- health-policy (1)
- health-education (1)
- epidemiology (1)
- community-health (1)
"""

import os
import re
from pathlib import Path
import yaml

# Tags to remove (keep only 'healthcare' as primary)
TAGS_TO_REMOVE = {
    'telemedicine',
    'public-health',
    'clinical-practice',
    'acute-care',
    'critical-care',
    'chronic-care',
    'behavioral-health',
    'mental-health',
    'health-policy',
    'health-education',
    'epidemiology',
    'community-health',
    'health-systems',
    'health-informatics',
    'population-health'
}

PRIMARY_TAG = 'healthcare'

def process_yaml_frontmatter(content: str) -> tuple[str, bool]:
    """Process YAML frontmatter and consolidate healthcare tags."""
    pattern = r'^(---\s*\n)(.*?)(\n---\s*\n)'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return content, False

    yaml_content = match.group(2)
    rest = content[match.end():]

    try:
        data = yaml.safe_load(yaml_content)
    except yaml.YAMLError:
        return content, False

    if 'tags' not in data or not data['tags']:
        return content, False

    tags = data['tags']
    if not isinstance(tags, list):
        return content, False

    # Check if any healthcare specialization tags present
    has_healthcare_tags = any(tag in TAGS_TO_REMOVE for tag in tags)

    if not has_healthcare_tags:
        return content, False

    # Remove healthcare specialization tags, ensure primary healthcare tag exists
    new_tags = []
    has_primary = False

    for tag in tags:
        if tag == PRIMARY_TAG:
            has_primary = True
            new_tags.append(tag)
        elif tag in TAGS_TO_REMOVE:
            # Skip specialization tags
            continue
        else:
            new_tags.append(tag)

    # Add primary healthcare tag if not present and we removed specialization tags
    if has_healthcare_tags and not has_primary:
        new_tags.insert(0, PRIMARY_TAG)

    # Update data
    data['tags'] = new_tags

    # Reconstruct YAML
    new_yaml = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return match.group(1) + new_yaml + match.group(3) + rest, True

def main():
    """Main consolidation function."""
    base_path = Path(__file__).parent.parent

    print("🔄 Consolidating Healthcare tags...\n")
    print(f"Tags to remove: {', '.join(sorted(TAGS_TO_REMOVE))}")
    print(f"Primary tag to keep: {PRIMARY_TAG}\n")

    files_processed = 0
    files_changed = 0
    tags_removed = 0

    for root, dirs, files in os.walk(base_path):
        # Skip hidden directories and scripts
        if '/.git' in root or '/.github' in root or '/scripts' in root:
            continue

        for file in files:
            if not file.endswith('.md'):
                continue

            file_path = Path(root) / file
            files_processed += 1

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Count healthcare tags before
                before_count = sum(content.count(f"- {tag}") for tag in TAGS_TO_REMOVE)

                new_content, changed = process_yaml_frontmatter(content)

                if changed:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                    rel_path = file_path.relative_to(base_path)
                    print(f"  ✅ {rel_path}")
                    files_changed += 1
                    tags_removed += before_count

            except Exception as e:
                print(f"  ❌ Error processing {file_path}: {e}")

    print("\n" + "=" * 80)
    print("CONSOLIDATION SUMMARY")
    print("=" * 80)
    print(f"Files processed: {files_processed}")
    print(f"Files changed: {files_changed}")
    print(f"Tags removed: {tags_removed}")
    print()
    print(f"✅ Healthcare specialization tags consolidated to '{PRIMARY_TAG}'")
    print()
    print("Next step: Run content type tag cleanup")

if __name__ == "__main__":
    main()
