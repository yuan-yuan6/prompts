#!/usr/bin/env python3
"""
AI/ML Tag Consolidation Script

Consolidates AI/ML related tags into standardized 'ai-ml' tag.

Tags to consolidate:
- data-science (86 occurrences)
- machine-learning (53 occurrences)
- nlp (1)
- sentiment-analysis (1)
- emotion-detection (1)
- causal-inference (1)

Total: ~143 tag instances → consolidated to 'ai-ml'
"""

import os
import re
from pathlib import Path
import yaml

# Tags to replace with 'ai-ml'
TAGS_TO_CONSOLIDATE = {
    'data-science',
    'machine-learning',
    'nlp',
    'sentiment-analysis',
    'emotion-detection',
    'causal-inference'
}

NEW_TAG = 'ai-ml'

def process_yaml_frontmatter(content: str) -> tuple[str, bool]:
    """Process YAML frontmatter and consolidate AI/ML tags."""
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

    # Check if any AI/ML tags present
    has_aiml_tags = any(tag in TAGS_TO_CONSOLIDATE for tag in tags)

    if not has_aiml_tags:
        return content, False

    # Replace AI/ML tags with consolidated tag
    new_tags = []
    aiml_found = False

    for tag in tags:
        if tag in TAGS_TO_CONSOLIDATE:
            if not aiml_found:
                new_tags.append(NEW_TAG)
                aiml_found = True
            # Skip duplicate AI/ML tags
        else:
            new_tags.append(tag)

    # Update data
    data['tags'] = new_tags

    # Reconstruct YAML
    new_yaml = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)

    return match.group(1) + new_yaml + match.group(3) + rest, True

def main():
    """Main consolidation function."""
    base_path = Path(__file__).parent.parent

    print("🔄 Consolidating AI/ML tags...\n")
    print(f"Tags to consolidate: {', '.join(sorted(TAGS_TO_CONSOLIDATE))}")
    print(f"New consolidated tag: {NEW_TAG}\n")

    files_processed = 0
    files_changed = 0
    tags_consolidated = 0

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

                # Count AI/ML tags before
                before_count = sum(content.count(f"- {tag}") for tag in TAGS_TO_CONSOLIDATE)

                new_content, changed = process_yaml_frontmatter(content)

                if changed:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                    rel_path = file_path.relative_to(base_path)
                    print(f"  ✅ {rel_path}")
                    files_changed += 1
                    tags_consolidated += before_count

            except Exception as e:
                print(f"  ❌ Error processing {file_path}: {e}")

    print("\n" + "=" * 80)
    print("CONSOLIDATION SUMMARY")
    print("=" * 80)
    print(f"Files processed: {files_processed}")
    print(f"Files changed: {files_changed}")
    print(f"Tags consolidated: {tags_consolidated}")
    print()
    print(f"✅ All AI/ML-related tags consolidated to '{NEW_TAG}'")
    print()
    print("Next step: Run consolidate_healthcare_tags.py for Phase 2")

if __name__ == "__main__":
    main()
