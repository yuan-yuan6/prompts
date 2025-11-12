#!/usr/bin/env python3
"""
Fix YAML syntax errors in template files.
Specifically fixes unquoted titles containing colons.
"""

import os
import re
from pathlib import Path

def fix_yaml_title(content):
    """
    Fix YAML frontmatter titles with unquoted colons.
    Converts: title: Text - Part 1: Section
    To: title: "Text - Part 1: Section"
    """
    lines = content.split('\n')
    fixed_lines = []
    in_frontmatter = False
    frontmatter_count = 0

    for line in lines:
        if line.strip() == '---':
            frontmatter_count += 1
            in_frontmatter = frontmatter_count == 1
            fixed_lines.append(line)
            continue

        if in_frontmatter and line.strip().startswith('title:'):
            # Extract the title value
            match = re.match(r'^(\s*title:\s*)(.+)$', line)
            if match:
                prefix = match.group(1)
                title_value = match.group(2).strip()

                # Check if title contains colon and is not already quoted
                if ':' in title_value and not (title_value.startswith('"') and title_value.endswith('"')):
                    # Remove any existing quotes
                    title_value = title_value.strip('"').strip("'")
                    # Add double quotes
                    fixed_line = f'{prefix}"{title_value}"'
                    fixed_lines.append(fixed_line)
                    continue

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)

def find_yaml_syntax_errors(base_dir):
    """Find all markdown files with potential YAML syntax errors."""
    issues = []

    for root, dirs, files in os.walk(base_dir):
        # Skip hidden directories and scripts
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'scripts']

        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Check for unquoted titles with colons
                    lines = content.split('\n')
                    in_frontmatter = False
                    frontmatter_count = 0

                    for i, line in enumerate(lines):
                        if line.strip() == '---':
                            frontmatter_count += 1
                            in_frontmatter = frontmatter_count == 1
                            continue

                        if in_frontmatter and line.strip().startswith('title:'):
                            match = re.match(r'^(\s*title:\s*)(.+)$', line)
                            if match:
                                title_value = match.group(2).strip()
                                if ':' in title_value and not (title_value.startswith('"') and title_value.endswith('"')):
                                    issues.append({
                                        'file': filepath,
                                        'line': i + 1,
                                        'content': line,
                                        'title': title_value
                                    })

                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

    return issues

def fix_files(base_dir, dry_run=False):
    """Fix YAML syntax errors in all markdown files."""
    issues = find_yaml_syntax_errors(base_dir)

    print(f"\n🔍 Found {len(issues)} files with YAML syntax issues\n")

    if not issues:
        print("✅ No YAML syntax errors found!")
        return 0

    fixed_count = 0

    for issue in issues:
        filepath = issue['file']
        rel_path = os.path.relpath(filepath, base_dir)

        print(f"📝 {rel_path}")
        print(f"   Line {issue['line']}: {issue['content']}")

        if not dry_run:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                fixed_content = fix_yaml_title(content)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)

                print(f"   ✅ Fixed")
                fixed_count += 1
            except Exception as e:
                print(f"   ❌ Error: {e}")
        else:
            print(f"   Would fix (dry run)")

    print(f"\n{'=' * 80}")
    if dry_run:
        print(f"🔍 DRY RUN: Would fix {len(issues)} files")
    else:
        print(f"✅ Fixed {fixed_count} files")

    return fixed_count

if __name__ == '__main__':
    import sys

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("🔍 Running in DRY RUN mode (no changes will be made)\n")

    fixed_count = fix_files(base_dir, dry_run)

    sys.exit(0 if fixed_count >= 0 else 1)
