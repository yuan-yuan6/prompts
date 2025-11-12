#!/usr/bin/env python3
"""
Update healthcare category to clinical-healthcare in all templates.
"""

import os
import re

def update_category_references():
    """Update all healthcare category references to clinical-healthcare."""

    fixed_count = 0

    # Walk through all markdown files
    for root, dirs, files in os.walk('/home/user/prompts'):
        # Skip hidden directories and scripts
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'scripts']

        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    original_content = content

                    # Update category fields
                    content = re.sub(
                        r'category:\s*healthcare/',
                        'category: clinical-healthcare/',
                        content
                    )

                    # Update related_templates references
                    content = re.sub(
                        r'healthcare/',
                        'clinical-healthcare/',
                        content
                    )

                    # Write back if changed
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed_count += 1
                        rel_path = os.path.relpath(filepath, '/home/user/prompts')
                        print(f"✅ Updated: {rel_path}")

                except Exception as e:
                    print(f"❌ Error processing {filepath}: {e}")

    print(f"\n{'='*80}")
    print(f"✅ Updated {fixed_count} files")
    return fixed_count

if __name__ == '__main__':
    update_category_references()
