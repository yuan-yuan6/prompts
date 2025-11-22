# Contributing

Thanks for contributing to the Prompts Library! Follow this guidance to ensure your changes pass validation.

## Local setup
1. Create or activate the repo venv and install dependencies:

```bash
chmod +x scripts/setup_env.sh
./scripts/setup_env.sh
```

2. Run lint to verify metadata:

```bash
./.venv/bin/python3 scripts/lint_metadata.py
```

3. Generate the INDEX and JSON:

```bash
./.venv/bin/python3 scripts/generate_index.py
```

## Metadata requirements
- Add YAML front-matter at the top of each Markdown template with at least:
  - `title`, `category`, `last_updated`.
- Recommended fields to include (linter issues will be warnings if missing):
  - `type` (one of `template`, `framework`, `generator`, `comprehensive`)
  - `difficulty` (one of `quick`, `intermediate`, `comprehensive`)
  - `tags` (list; recommended to use canonical tags in `scripts/taxonomy.json`)
  - `slug` if you want a small identifier for the template.

## Taxonomy
- Canonical categories and tags are maintained in `scripts/taxonomy.json` and summarized in `TAXONOMY.md`.
- To add a new category or tag, update those files and submit a PR explaining why the addition is necessary.

## CI
- A CI job validates metadata on PRs. If the linter reports `issues` (errors), your PR will fail validation.
- Warnings are visible in `metadata_lint_report.json` and are suggested changes, but they do not fail CI.

## Best practices
- Keep `category` as a root canonical category (e.g., `communication`) and optionally include subcategory `communication/meetings` in the `category` field.
- Avoid special characters in `title` — quote them in YAML if present (e.g., `title: "Foundation & Governance"`).
- Use `tags` from canonical tags list.
- Keep front-matter consistent and complete to help in indexing and documentation.

## Using category migration scripts


```bash
./.venv/bin/python3 scripts/apply_category_mapping.py --report
```


```bash
./.venv/bin/python3 scripts/apply_category_mapping.py --apply
```


```bash
./.venv/bin/python3 scripts/apply_category_mapping.py --report --taxonomy
```

- If you're cleaning up multi-word subcategories or fixing capitalization, consider running the script with `--normalize` during the review step to standardize subcategories into kebab-case:

```bash
./.venv/bin/python3 scripts/apply_category_mapping.py --report --normalize
```

Normalization should be reviewed in the PR because it changes `category` strings' text.
