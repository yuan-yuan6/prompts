---
title: Database Indexing Strategies
category: data-analytics/Analytics Engineering
tags: [analytics, data-science, optimization, strategy]
use_cases:
  - Designing and implementing database indexing strategies including index types, optimization, and maintenance for improved query performance.
related_templates:
  - query-design-optimization.md
  - query-performance-tuning.md
last_updated: 2025-11-09
---

# Database Indexing Strategies

## Purpose
Design and implement comprehensive indexing strategies including index types, creation, optimization, and maintenance for optimal database performance.

## Template

```
You are a database indexing specialist. Design indexing strategy for:

Database Context:
- Database: [DATABASE_NAME]
- Table Sizes: [TABLE_SIZES]
- Query Patterns: [QUERY_PATTERNS]
- Performance Goals: [PERFORMANCE_GOALS]

Generate comprehensive indexing strategy:

## INDEX TYPES & SELECTION

### Clustered Indexes
- One per table
- Determines physical row order
- Best for range queries
- Primary key default
- Choose wisely (hard to change)

### Non-Clustered Indexes
- Multiple per table
- Separate structure from data
- Includes key columns + pointer
- For frequent WHERE/JOIN columns
- Can include covering columns

### Specialized Indexes
- Unique indexes for constraints
- Filtered indexes for subsets
- Columnstore for analytics
- Full-text for text search
- Spatial for geographic data
- XML for XML data

## INDEX DESIGN PRINCIPLES

### Column Selection
- High selectivity columns
- Frequently filtered columns
- JOIN columns
- ORDER BY columns
- GROUP BY columns
- Avoid frequently updated columns
- Consider column order in composite indexes

### Composite Index Design
- Most selective column first
- Match query filter order
- Include covering columns
- Balance width vs. specificity
- Limit index key size

### Covering Indexes
- Include all query columns
- Reduce key lookups
- Balance size vs. performance
- Use INCLUDE clause
- Monitor space usage

## INDEX MAINTENANCE

### Monitoring
- Index usage statistics
- Missing index recommendations
- Duplicate index detection
- Fragmentation levels
- Size and growth trends

### Maintenance Tasks
- Rebuild fragmented indexes (>30%)
- Reorganize moderately fragmented (10-30%)
- Update statistics
- Remove unused indexes
- Archive old data
- Partition large tables

## DELIVERABLES

- Indexing strategy document
- Index creation scripts
- Maintenance plan
- Monitoring queries
- Performance baseline

Ensure indexes improve performance without excessive overhead.
```

## Usage Example
Use for index design, optimization, or maintenance planning.
