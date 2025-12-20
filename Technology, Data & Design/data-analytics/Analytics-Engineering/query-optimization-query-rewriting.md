---
category: data-analytics
description: Optimize SQL query performance through strategic rewriting, execution plan improvements, and advanced patterns including subquery elimination, JOIN optimization, and window functions
title: Query Optimization - Query Rewriting & SQL Optimization
tags:
- query-optimization
- sql-rewriting
- execution-plans
- database-performance
use_cases:
- Rewriting inefficient SQL queries for improved performance
- Optimizing execution plans through query restructuring
- Implementing query hints and advanced SQL patterns
related_templates:
- data-analytics/Analytics-Engineering/query-optimization-baseline-analysis.md
- data-analytics/Analytics-Engineering/query-optimization-indexing-strategies.md
- data-analytics/Analytics-Engineering/query-optimization-overview.md
industries:
- finance
- healthcare
- retail
- technology
- manufacturing
type: framework
difficulty: intermediate
slug: query-optimization-query-rewriting
---

# Query Optimization - Query Rewriting & SQL Optimization

## Purpose
Optimize SQL query performance through strategic rewriting techniques that transform inefficient patterns into performant alternatives. This framework covers subquery elimination, JOIN optimization, window function usage, CTE patterns, and judicious query hint application while preserving query semantics.

## Template

Optimize SQL queries for {DATABASE_CONTEXT}, addressing {QUERY_CHALLENGES} to achieve {PERFORMANCE_OBJECTIVES}.

**1. Subquery Pattern Analysis**

Begin by identifying subquery patterns that cause performance problems. IN clauses with subqueries force the optimizer to evaluate the subquery for each row in the outer query—convert these to JOINs or EXISTS which allow more efficient execution strategies. Correlated subqueries that reference outer query columns execute once per outer row, creating multiplicative performance impact—replace with JOINs or window functions that process data in a single pass. Scalar subqueries in SELECT lists execute for every row returned—move these to JOINs or pre-aggregate in CTEs. NOT IN with nullable columns produces unexpected results and poor performance—use NOT EXISTS or LEFT JOIN with NULL check instead. Nested subqueries multiple levels deep confuse optimizers—flatten into JOINs or break into CTEs with clear dependencies. Identify subqueries that return large result sets used only for existence checks—EXISTS returns immediately upon finding a match while IN must materialize the entire set.

**2. JOIN Optimization Strategies**

Optimize JOIN operations that often dominate query execution time. Order tables in JOINs to start with the most selective—the table that filters to the fewest rows should drive the join to minimize intermediate result sizes. Choose appropriate join types based on data characteristics: INNER JOIN when both sides must match, LEFT JOIN when preserving all rows from one side, and avoid CROSS JOIN unless specifically needed for cartesian products. Convert implicit joins (comma-separated tables in FROM with WHERE conditions) to explicit JOIN syntax for clarity and optimizer efficiency. Eliminate unnecessary JOINs when the joined table contributes no columns to the result and doesn't filter rows—these add overhead without value. Use semi-joins (EXISTS or IN) when you need to filter based on related table existence without returning columns from that table. Consider join hints only when optimizer consistently chooses suboptimal join algorithms despite accurate statistics.

**3. Set Operation Refinement**

Refine set operations that often contain hidden performance costs. Replace UNION with UNION ALL when duplicate elimination is unnecessary—UNION implies DISTINCT which requires sorting or hashing the entire result set. Apply DISTINCT at the appropriate level—on source queries before UNION ALL if each source is unique internally, or once at the end if deduplication across sources is needed. Convert multiple UNIONs of the same table with different filters into a single query with OR conditions or CASE expressions when possible. Use INTERSECT and EXCEPT judiciously—these set operations may be less efficient than equivalent EXISTS or NOT EXISTS patterns depending on the optimizer. Avoid DISTINCT as a fix for incorrect JOINs that produce duplicates—fix the JOIN logic instead of masking the problem with expensive deduplication.

**4. Window Function Application**

Apply window functions to replace inefficient self-joins and correlated subqueries. Running totals and cumulative aggregates previously requiring self-joins or correlated subqueries execute efficiently with SUM OVER with appropriate frame specification. Ranking and row numbering using ROW_NUMBER, RANK, and DENSE_RANK eliminate the need for self-joins that match rows to count predecessors. Lag and lead analysis accessing previous or next row values replaces correlated subqueries that find adjacent records. Moving averages and sliding window calculations using frame specifications (ROWS BETWEEN or RANGE BETWEEN) replace complex self-join patterns. First and last value within groups using FIRST_VALUE and LAST_VALUE with partitioning replaces subqueries that find boundary records. Partition carefully to match business logic—incorrect partitioning produces wrong results that may not be obvious in testing.

**5. CTE and Query Structure**

Structure complex queries using Common Table Expressions for readability and potential performance benefits. Break complex logic into named CTEs with clear purposes—data filtering, aggregation, transformation, and final assembly—making queries self-documenting and easier to optimize. Apply filters as early as possible in CTEs to reduce data volumes flowing through subsequent operations. Avoid materializing CTEs multiple times by referencing each CTE only once when possible, or use temporary tables for results needed multiple times. Use recursive CTEs for hierarchical data traversal replacing cursor-based or iterative approaches—but set recursion limits to prevent runaway queries. Consider whether CTEs or derived tables (inline subqueries) perform better on your platform—some optimizers inline CTEs while others materialize them. Structure CTEs to enable optimizer predicate pushdown—filters in the final SELECT should push into CTEs when possible.

**6. Predicate Optimization**

Optimize WHERE clause predicates that determine how much data the query processes. Make predicates sargable (Search ARGument ABLE) so indexes can be used—avoid functions on indexed columns, use range comparisons instead of BETWEEN when beneficial, and avoid implicit type conversions. Order predicates by selectivity when the optimizer doesn't reorder them automatically—most selective predicates first reduce rows for subsequent predicates. Convert OR conditions to UNION ALL when each condition can use different indexes—OR often prevents index usage while UNION ALL allows optimal access for each branch. Use IN lists instead of multiple OR conditions for the same column—optimizers handle IN lists more efficiently up to platform-specific limits. Avoid negative conditions (NOT IN, NOT LIKE, <>) when positive conditions achieve the same result—positive conditions often enable better index utilization. Parameterize queries appropriately—literal values enable better statistics-based optimization while parameters enable plan reuse.

**7. Query Hint Guidelines**

Apply query hints strategically when optimizer choices are consistently suboptimal. Use hints as a last resort after verifying statistics are current, indexes are appropriate, and query structure is optimal—hints override optimizer intelligence and may cause problems as data changes. Document every hint with justification explaining why the optimizer fails and what the hint corrects. Common scenarios for hints include forcing index usage when optimizer incorrectly estimates selectivity, controlling parallelism for queries that perform better single-threaded, and addressing parameter sniffing issues with RECOMPILE or OPTIMIZE FOR hints. Test hints with varying data volumes and distributions—a hint that helps today may hurt tomorrow as data evolves. Review hinted queries during regular maintenance to verify hints remain beneficial. Consider query plan guides or plan forcing as alternatives that don't require query modification.

**8. Validation and Deployment**

Validate optimized queries thoroughly before production deployment. Verify semantic equivalence by comparing results between original and optimized queries on representative data—row counts, aggregates, and sample records should match exactly. Measure performance improvement capturing execution time, logical reads, physical reads, CPU time, and memory grants before and after optimization. Test with production-like data volumes—queries that perform well on small datasets may behave differently at scale. Validate across parameter ranges if queries are parameterized—optimization that helps one parameter value may hurt others. Create rollback procedures preserving original queries for quick reversion if problems emerge. Monitor optimized queries after deployment tracking execution metrics over time to ensure sustained improvement. Document optimization rationale and decisions for future reference and knowledge sharing.

Deliver your query optimization as:

1. **Subquery analysis** identifying patterns and conversion opportunities
2. **JOIN optimization** with reordering, type selection, and elimination recommendations
3. **Set operation refinement** converting UNION to UNION ALL and optimizing DISTINCT
4. **Window function rewrites** replacing self-joins and correlated subqueries
5. **CTE structure** organizing complex queries for clarity and performance
6. **Predicate optimization** ensuring sargability and selectivity ordering
7. **Query hints** applied judiciously with documented justification
8. **Validation results** confirming semantic equivalence and performance improvement

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{DATABASE_CONTEXT}` | Platform, version, and workload type | "SQL Server 2022 OLTP system with mixed read-write workload" |
| `{QUERY_CHALLENGES}` | Specific issues to address | "correlated subqueries in reporting queries, expensive ORDER BY operations, parameter sniffing" |
| `{PERFORMANCE_OBJECTIVES}` | Target improvements | "reduce P95 query latency from 5 seconds to under 500ms, eliminate table scans on Orders table" |

---

## Usage Examples

### Example 1: E-Commerce Reporting Query Optimization
**Prompt:** "Optimize SQL queries for {DATABASE_CONTEXT: PostgreSQL 15 supporting e-commerce analytics with 500GB order history}, addressing {QUERY_CHALLENGES: customer lifetime value calculation using correlated subqueries, product ranking queries with self-joins, sales trend reports with multiple UNIONs}, to achieve {PERFORMANCE_OBJECTIVES: dashboard queries under 3 seconds, nightly batch reports completing within 2-hour window}."

**Expected Output:** Subquery analysis converting customer LTV correlated subqueries to window functions with SUM OVER partitioned by customer_id. JOIN optimization eliminating self-join for product ranking using ROW_NUMBER window function. Set operation refinement replacing UNION with UNION ALL for sales trend queries after confirming no cross-source duplicates. CTE structure for batch reports with filtered base CTE, aggregation CTE, and final formatting. Predicate optimization ensuring date range filters are sargable using >= and < instead of BETWEEN with timestamps. Validation showing 85% reduction in logical reads for LTV query, 10x improvement in product ranking.

### Example 2: Financial Transaction Query Tuning
**Prompt:** "Optimize SQL queries for {DATABASE_CONTEXT: SQL Server 2022 processing 10 million daily transactions with strict latency requirements}, addressing {QUERY_CHALLENGES: account balance calculations with scalar subqueries, transaction lookup queries with OR conditions preventing index usage, audit queries with NOT IN patterns}, to achieve {PERFORMANCE_OBJECTIVES: balance inquiry under 50ms, transaction search under 200ms, audit queries under 30 seconds}."

**Expected Output:** Subquery analysis replacing scalar balance subqueries with indexed view or pre-computed column. JOIN optimization converting OR-based transaction lookups to UNION ALL enabling separate index seeks per condition. NOT IN audit patterns converted to NOT EXISTS with explicit NULL handling. Window function application for running balance calculation replacing iterative cursor-based approach. Query hint recommendation for OPTION (RECOMPILE) on transaction search due to parameter sniffing with highly variable date ranges. Validation confirming semantic equivalence with test cases covering edge conditions and performance metrics showing targets achieved.

### Example 3: Healthcare Analytics Query Restructuring
**Prompt:** "Optimize SQL queries for {DATABASE_CONTEXT: Snowflake data warehouse with 2TB clinical data supporting population health analytics}, addressing {QUERY_CHALLENGES: patient cohort queries with deeply nested subqueries, outcome analysis with multiple self-joins for temporal patterns, quality measure calculations with complex CASE logic}, to achieve {PERFORMANCE_OBJECTIVES: cohort identification under 60 seconds, outcome analysis under 5 minutes, quality dashboard refresh under 10 minutes}."

**Expected Output:** Subquery analysis flattening nested cohort criteria into CTEs with explicit join conditions. Self-join elimination for temporal pattern matching using LAG/LEAD window functions to compare visit sequences. CTE structure with layered approach: base population, inclusion criteria, exclusion criteria, measure calculation, final aggregation. Set operation refinement consolidating multiple measure queries into single pass with conditional aggregation. QUALIFY clause usage for Snowflake-specific row filtering after window functions. Cluster key recommendations aligning with common filter patterns. Validation with warehouse utilization metrics showing reduced scan volume and compute time.

---

## Cross-References

- [query-optimization-baseline-analysis.md](query-optimization-baseline-analysis.md) - Identify queries needing optimization
- [query-optimization-indexing-strategies.md](query-optimization-indexing-strategies.md) - Index design supporting rewritten queries
- [query-optimization-overview.md](query-optimization-overview.md) - Query optimization module navigation
