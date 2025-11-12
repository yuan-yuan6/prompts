#!/usr/bin/env python3
"""
Remove Redundant Tags Script

Removes redundant content type tags and generic/meta tags.

Content Type Tags to Remove (redundant with file naming):
- comprehensive (9)
- overview (5)

Generic/Meta Tags to Remove (too vague):
- business (11)
- industry (27)
- technology (when used as generic tag, not in technology/ category context)
- navigation (if present)
- professional (too vague)

Keep these content type tags:
- template
- framework
- guide
- research
- documentation
"""

import os
import re
from pathlib import Path
import yaml

# Tags to remove
CONTENT_TYPE_TAGS_TO_REMOVE = {
    'comprehensive',
    'overview',
}

GENERIC_META_TAGS_TO_REMOVE = {
    'business',
    'industry',
    'navigation',
    'professional',
}

ALL_TAGS_TO_REMOVE = CONTENT_TYPE_TAGS_TO_REMOVE | GENERIC_META_TAGS_TO_REMOVE

def process_yaml_frontmatter(content: str, file_path: str) -> tuple[str, bool]:
    """Process YAML frontmatter and remove redundant tags."""
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

    # Check if any tags to remove are present
    has_tags_to_remove = any(tag in ALL_TAGS_TO_REMOVE for tag in tags)

    if not has_tags_to_remove:
        return content, False

    # Remove redundant tags
    new_tags = [tag for tag in tags if tag not in ALL_TAGS_TO_REMOVE]

    # Special case: keep 'technology' tag only in technology/ category files
    for tag in tags:
        if tag == 'technology':
            if not file_path.startswith('technology/'):
                # Remove technology tag from non-technology category files
                continue
            else:
                # Keep it for technology category files
                if tag not in new_tags:
                    new_tags.append(tag)

    # Update data
    data['tags'] = new_tags

    # Reconstruct YAML
    new_yaml = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return match.group(1) + new_yaml + match.group(3) + rest, True

def main():
    """Main function."""
    base_path = Path(__file__).parent.parent

    print("🔄 Removing redundant tags...\n")
    print(f"Content type tags to remove: {', '.join(sorted(CONTENT_TYPE_TAGS_TO_REMOVE))}")
    print(f"Generic/meta tags to remove: {', '.join(sorted(GENERIC_META_TAGS_TO_REMOVE))}\n")

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

                # Get relative path for category checking
                rel_path = str(file_path.relative_to(base_path))

                # Count tags before
                before_count = sum(content.count(f"- {tag}") for tag in ALL_TAGS_TO_REMOVE)

                new_content, changed = process_yaml_frontmatter(content, rel_path)

                if changed:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

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
    print("✅ Redundant tags removed")
    print()
    print("Next step: Update TAG_TAXONOMY.md with new standardized tags")

if __name__ == "__main__":
    main()
