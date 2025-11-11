#!/usr/bin/env python3
"""
Remove all time estimates from prompt files
Preserves all other content and structure
"""

import re
import os
from pathlib import Path

def remove_time_estimates(content):
    """Remove various time estimate patterns from content"""

    # Pattern 1: Remove time from step headers like "**Step 1: Do Something (10 minutes)**"
    # Captures: "**Step 1: Do Something**" without the time
    content = re.sub(
        r'(\*\*Step \d+:.*?)\s*\([0-9]+-?[0-9]*\s*(?:minutes?|hours?|days?|weeks?|months?)\)\s*(\*\*)',
        r'\1\2',
        content
    )

    # Pattern 2: Remove entire "Time Estimate:" or "### Time Estimate" sections
    # This removes the line with "Time Estimate:" and the content after it (usually one line)
    content = re.sub(
        r'^\*\*Time Estimate:\*\*.*$\n^-.*$',
        '',
        content,
        flags=re.MULTILINE
    )

    # Pattern 3: Also handle simple "**Time Estimate:**" followed by content on same line
    content = re.sub(
        r'^\*\*Time Estimate:\*\*.*$',
        '',
        content,
        flags=re.MULTILINE
    )

    # Pattern 4: Remove "### Time Estimate" headers and their content
    # Remove until next ### or ## section
    content = re.sub(
        r'^###\s*Time Estimate[s]?\s*$\n(?:^(?!#+\s).*$\n?)*',
        '',
        content,
        flags=re.MULTILINE
    )

    # Pattern 5: Remove timeline estimates from descriptive text
    # Like "Framework design: 4-8 hours to complete template"
    # But be careful not to remove legitimate content
    lines = content.split('\n')
    filtered_lines = []

    for line in lines:
        # Skip lines that are purely about time estimates in workflows
        if re.search(r'^-\s*(Framework design|Implementation):\s*.*?([0-9]+-?[0-9]*\s*(?:hours?|days?|weeks?|months?))', line):
            # Check if this is ONLY about time, not other info
            if re.search(r'^\s*-\s*\w+:\s*[0-9]+-?[0-9]*\s*(?:hours?|days?|weeks?|months?)\s*(?:to|for|over)?\s*', line):
                continue  # Skip this line

        filtered_lines.append(line)

    content = '\n'.join(filtered_lines)

    # Pattern 6: Remove standalone time references in parentheses from any line
    # But preserve other parenthetical content
    content = re.sub(
        r'\s*\([0-9]+-?[0-9]*\s*(?:minutes?|hours?|days?|weeks?|months?)\s*(?:for|to|over)?\s*[^)]*\)',
        '',
        content
    )

    # Clean up any double blank lines created by removals
    content = re.sub(r'\n\n\n+', '\n\n', content)

    # Clean up trailing whitespace
    lines = content.split('\n')
    lines = [line.rstrip() for line in lines]
    content = '\n'.join(lines)

    return content

def process_file(filepath):
    """Process a single file to remove time estimates"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()

        modified_content = remove_time_estimates(original_content)

        # Only write if content changed
        if modified_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function to process all prompt files"""

    # Categories to process
    categories = [
        'business', 'creative', 'data-analytics', 'education', 'finance',
        'government', 'healthcare', 'industry', 'nonprofit', 'personal',
        'professional-services', 'security', 'technology'
    ]

    base_path = Path('/home/user/prompts')
    files_processed = 0
    files_modified = 0

    for category in categories:
        category_path = base_path / category
        if not category_path.exists():
            continue

        # Find all .md files recursively
        for md_file in category_path.rglob('*.md'):
            # Skip README files
            if md_file.name == 'README.md':
                continue

            files_processed += 1
            if process_file(md_file):
                files_modified += 1
                print(f"✓ Modified: {md_file.relative_to(base_path)}")

    print(f"\n{'='*60}")
    print(f"Processing complete!")
    print(f"Files processed: {files_processed}")
    print(f"Files modified: {files_modified}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
