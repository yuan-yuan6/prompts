#!/usr/bin/env python3
"""
Interactive Navigation Tool for Prompt Templates
Search, filter, and discover templates with ease
"""
import os
import re
import yaml
import sys
from pathlib import Path

class PromptNavigator:
    def __init__(self, base_dir='/home/user/prompts'):
        self.base_dir = base_dir
        self.templates = []
        self.load_templates()

    def load_templates(self):
        """Load all prompt templates with metadata"""
        exclude_patterns = [
            'README', 'INDEX', 'LICENSE', 'IMPLEMENTATION', 'FEASIBILITY',
            'PROGRESS', 'SUMMARY', 'GUIDE', 'ANALYSIS', 'REFACTORING',
            'TEMPLATE', 'PLAN', 'ASSESSMENT', '.templates', 'VERSION'
        ]

        for root, dirs, files in os.walk(self.base_dir):
            dirs[:] = [d for d in dirs if not d.startswith('.')]

            for file in files:
                if file.endswith('.md'):
                    if any(pattern in file.upper() or pattern in root.upper()
                           for pattern in exclude_patterns):
                        continue

                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.base_dir)

                    try:
                        metadata = self.extract_metadata(file_path)
                        if metadata:
                            metadata['file_path'] = file_path
                            metadata['rel_path'] = rel_path
                            self.templates.append(metadata)
                    except Exception:
                        pass

        print(f"Loaded {len(self.templates)} templates\n")

    def extract_metadata(self, file_path):
        """Extract frontmatter metadata from markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if match:
            try:
                return yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                return None
        return None

    def search_templates(self, query):
        """Search templates by keyword"""
        query_lower = query.lower()
        results = []

        for template in self.templates:
            # Search in title, category, tags, use_cases
            title = template.get('title', '').lower()
            category = template.get('category', '').lower()
            tags = ' '.join(template.get('tags', [])).lower()
            use_cases = ' '.join(str(uc) for uc in template.get('use_cases', [])).lower()

            if (query_lower in title or query_lower in category or
                query_lower in tags or query_lower in use_cases):
                results.append(template)

        return results

    def filter_by_category(self, category):
        """Filter templates by category"""
        return [t for t in self.templates if category.lower() in t.get('category', '').lower()]

    def filter_by_tag(self, tag):
        """Filter templates by tag"""
        return [t for t in self.templates
                if tag.lower() in [t_tag.lower() for t_tag in t.get('tags', [])]]

    def list_categories(self):
        """List all unique categories"""
        categories = set()
        for template in self.templates:
            category = template.get('category', '')
            if category:
                # Extract main category (first part before /)
                main_cat = category.split('/')[0]
                categories.add(main_cat)
        return sorted(categories)

    def list_tags(self):
        """List all unique tags"""
        tags = set()
        for template in self.templates:
            tags.update(template.get('tags', []))
        return sorted(tags)

    def display_results(self, results, limit=20):
        """Display search results"""
        if not results:
            print("No templates found matching your criteria.\n")
            return

        print(f"\nFound {len(results)} template(s):\n")
        print(f"{'#':<4} {'Title':<50} {'Category':<30}")
        print("-" * 85)

        for i, template in enumerate(results[:limit], 1):
            title = template.get('title', 'Untitled')[:48]
            category = template.get('category', 'N/A')[:28]
            print(f"{i:<4} {title:<50} {category:<30}")

        if len(results) > limit:
            print(f"\n... and {len(results) - limit} more. Refine your search to see more results.")

    def display_template_details(self, template):
        """Display detailed information about a template"""
        print("\n" + "="*80)
        print(f"TEMPLATE: {template.get('title', 'Untitled')}")
        print("="*80)
        print(f"\n📁 Category: {template.get('category', 'N/A')}")
        print(f"📂 File: {template.get('rel_path', 'N/A')}")

        tags = template.get('tags', [])
        if tags:
            print(f"🏷️  Tags: {', '.join(tags[:10])}")

        use_cases = template.get('use_cases', [])
        if use_cases:
            print(f"\n💡 Use Cases:")
            for i, uc in enumerate(use_cases[:3], 1):
                uc_text = str(uc)[:120]
                print(f"   {i}. {uc_text}")
                if len(uc_text) == 120:
                    print("      ...")

        related = template.get('related_templates', [])
        if related:
            print(f"\n🔗 Related Templates:")
            for rel in related[:5]:
                print(f"   - {rel}")

        last_updated = template.get('last_updated', 'N/A')
        print(f"\n📅 Last Updated: {last_updated}")
        print("\n" + "="*80)

    def interactive_mode(self):
        """Interactive navigation interface"""
        print("\n" + "="*80)
        print("  🧭 PROMPT TEMPLATE NAVIGATOR")
        print("="*80)
        print("\n  Interactive tool for discovering and navigating 375+ prompt templates")
        print("  Type 'help' to see available commands\n")

        while True:
            try:
                command = input("Navigator> ").strip()

                if not command:
                    continue

                if command.lower() in ['exit', 'quit', 'q']:
                    print("\nGoodbye! 👋\n")
                    break

                elif command.lower() == 'help':
                    self.show_help()

                elif command.lower().startswith('search '):
                    query = command[7:].strip()
                    results = self.search_templates(query)
                    self.display_results(results)

                elif command.lower() == 'categories':
                    categories = self.list_categories()
                    print(f"\nAvailable Categories ({len(categories)}):\n")
                    for i, cat in enumerate(categories, 1):
                        count = len(self.filter_by_category(cat))
                        print(f"  {i:2}. {cat:<30} ({count} templates)")
                    print()

                elif command.lower().startswith('category '):
                    category = command[9:].strip()
                    results = self.filter_by_category(category)
                    self.display_results(results)

                elif command.lower() == 'tags':
                    tags = self.list_tags()
                    print(f"\nAvailable Tags ({len(tags)}):\n")
                    for i, tag in enumerate(tags[:50], 1):  # Show first 50
                        count = len(self.filter_by_tag(tag))
                        print(f"  {i:2}. {tag:<25} ({count})")
                    if len(tags) > 50:
                        print(f"\n  ... and {len(tags) - 50} more tags")
                    print()

                elif command.lower().startswith('tag '):
                    tag = command[4:].strip()
                    results = self.filter_by_tag(tag)
                    self.display_results(results)

                elif command.lower().startswith('show '):
                    try:
                        index = int(command[5:].strip()) - 1
                        # Get last search results (simplified - in production, would store)
                        print("\nPlease use 'details <path>' to show template details")
                    except (ValueError, IndexError):
                        print("Invalid template number")

                elif command.lower().startswith('details '):
                    path = command[8:].strip()
                    matching = [t for t in self.templates if path in t.get('rel_path', '')]
                    if matching:
                        self.display_template_details(matching[0])
                    else:
                        print("Template not found")

                elif command.lower() == 'stats':
                    self.show_stats()

                elif command.lower() == 'random':
                    import random
                    template = random.choice(self.templates)
                    self.display_template_details(template)

                else:
                    print(f"Unknown command: '{command}'. Type 'help' for available commands.")

            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋\n")
                break
            except Exception as e:
                print(f"Error: {e}")

    def show_help(self):
        """Display help menu"""
        help_text = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                           AVAILABLE COMMANDS                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

SEARCH & DISCOVERY:
  search <keyword>        Search templates by keyword (title, tags, use cases)
                          Example: search "marketing", search "machine learning"

  category <name>         Filter templates by category
                          Example: category "business", category "healthcare"

  tag <name>              Filter templates by tag
                          Example: tag "optimization", tag "strategy"

BROWSING:
  categories              List all available categories with template counts
  tags                    List all available tags
  random                  Show a random template (discover something new!)

DETAILS:
  details <path>          Show detailed information about a template
                          Example: details "business/Sales & Marketing/lead-scoring.md"

INFORMATION:
  stats                   Show repository statistics
  help                    Show this help menu

NAVIGATION:
  exit, quit, q           Exit the navigator

╔══════════════════════════════════════════════════════════════════════════════╗
║                              SEARCH TIPS                                      ║
╚══════════════════════════════════════════════════════════════════════════════╝

• Searches are case-insensitive
• Search terms match across titles, categories, tags, and use cases
• Use specific keywords for better results: "machine learning", "financial analysis"
• Browse categories first to understand repository structure
• Use 'random' to discover templates you didn't know existed!

Examples:
  > search analytics          # Find all analytics-related templates
  > category technology       # Browse all technology templates
  > tag machine-learning      # Find ML-specific templates
  > details business/...      # View details of specific template
"""
        print(help_text)

    def show_stats(self):
        """Display repository statistics"""
        print("\n" + "="*80)
        print("  📊 REPOSITORY STATISTICS")
        print("="*80)

        print(f"\n  Total Templates: {len(self.templates)}")

        categories = self.list_categories()
        print(f"  Total Categories: {len(categories)}")

        tags = self.list_tags()
        print(f"  Total Tags: {len(tags)}")

        # Category distribution
        print("\n  Top 10 Categories by Template Count:")
        cat_counts = {}
        for template in self.templates:
            cat = template.get('category', '').split('/')[0]
            cat_counts[cat] = cat_counts.get(cat, 0) + 1

        sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
        for i, (cat, count) in enumerate(sorted_cats[:10], 1):
            print(f"    {i:2}. {cat:<30} {count:>3} templates")

        # Tag distribution
        print("\n  Top 10 Most Common Tags:")
        tag_counts = {}
        for template in self.templates:
            for tag in template.get('tags', []):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
        for i, (tag, count) in enumerate(sorted_tags[:10], 1):
            print(f"    {i:2}. {tag:<30} {count:>3} templates")

        print("\n" + "="*80 + "\n")

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("""
Prompt Template Navigator - Interactive CLI Tool

Usage:
  python navigate.py              # Start interactive mode
  python navigate.py --help       # Show this help message

Description:
  Navigate through 375+ prompt templates with ease. Search by keyword,
  filter by category or tag, and discover templates for your use case.

Interactive Mode Commands:
  Type 'help' once in interactive mode for full command list.

Examples:
  > search machine learning       # Find ML templates
  > category business             # Browse business templates
  > tag optimization              # Filter by tag
  > random                        # Discover something new!
""")
        return

    navigator = PromptNavigator()
    navigator.interactive_mode()

if __name__ == '__main__':
    main()
