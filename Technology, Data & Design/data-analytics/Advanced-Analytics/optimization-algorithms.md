---
category: data-analytics
title: Optimization Algorithms & Operations Research Framework
tags:
- optimization
- operations-research
- linear-programming
- algorithms
use_cases:
- Solving resource allocation and scheduling problems
- Optimizing supply chain and logistics decisions
- Portfolio optimization and financial planning
- Production planning and inventory management
related_templates:
- data-analytics/Advanced-Analytics/predictive-modeling-framework.md
- data-analytics/Advanced-Analytics/time-series-analysis.md
- data-analytics/dashboard-design-patterns.md
industries:
- manufacturing
- finance
- logistics
- retail
- energy
type: framework
difficulty: intermediate
slug: optimization-algorithms
---

# Optimization Algorithms & Operations Research Framework

## Purpose
Solve optimization problems systematically using operations research techniques. This framework covers problem formulation, algorithm selection, solver configuration, solution validation, and production deployment for linear programming, integer programming, constraint optimization, and heuristic methods.

## Template

Develop an optimization solution for {PROBLEM_NAME} to {OBJECTIVE} with {SCALE_CONSTRAINTS}.

**1. PROBLEM UNDERSTANDING**

Define what you're optimizing:

Business context: What decision are you trying to optimize? What's the business objective—minimize cost, maximize profit, minimize time, maximize utilization? Who makes these decisions today and how? What's the value of improvement?

Problem classification: What type of optimization problem is this? Linear programming (LP) has continuous variables and linear constraints. Mixed-integer programming (MIP) adds discrete decisions. Quadratic programming (QP) has quadratic objectives. Nonlinear programming (NLP) has nonlinear functions. Stochastic optimization handles uncertainty. Classification determines algorithm choice.

Scale assessment: How many decision variables? How many constraints? What's the required solution time? Problems with thousands of variables and constraints are routine for modern solvers. Millions may require decomposition or heuristics. Real-time optimization needs sub-second solutions.

**2. MATHEMATICAL FORMULATION**

Translate the business problem to mathematics:

Decision variables: What are you deciding? Variables can be continuous (production quantities, allocation percentages), binary (yes/no decisions, facility open/closed), or integer (number of trucks, shifts). Define bounds—physical limits, capacity constraints, non-negativity.

Objective function: What are you optimizing? Express as a mathematical function of decision variables. Minimize total cost, maximize total profit, minimize makespan, maximize coverage. Include all relevant cost or value components. Ensure linearity if using LP/MIP.

Constraints: What rules must be satisfied? Capacity constraints limit resource usage. Demand constraints ensure requirements are met. Balance constraints enforce flow conservation. Logical constraints link binary variables. Express each constraint mathematically. Distinguish hard constraints (must satisfy) from soft constraints (prefer to satisfy).

Problem structure: Does your problem have special structure that enables efficient algorithms? Network flows (transportation, assignment), knapsack problems, set covering, scheduling problems all have specialized algorithms faster than general MIP. Recognize and exploit structure.

**3. ALGORITHM SELECTION**

Choose the right solution method:

Exact methods for optimal solutions: Simplex algorithm solves LP efficiently—millions of variables in seconds. Interior point methods handle large sparse LP well. Branch-and-bound solves MIP by systematic enumeration. Branch-and-cut adds cutting planes to tighten bounds. These methods prove optimality but may be slow for hard combinatorial problems.

Heuristics for good solutions fast: When exact methods are too slow, heuristics find good (not provably optimal) solutions quickly. Genetic algorithms evolve populations of solutions. Simulated annealing escapes local optima through random moves. Tabu search maintains memory to avoid cycling. These scale to massive problems but don't guarantee optimality.

Hybrid approaches: Matheuristics combine exact and heuristic methods. Use heuristics to find good feasible solutions, then exact methods to prove bounds or improve locally. Large neighborhood search destroys and repairs solutions. These often outperform pure approaches.

Selection criteria: Choose exact methods when optimality matters, problem is tractable, and time allows. Choose heuristics when problems are huge, solutions needed fast, or near-optimal is sufficient. Consider hybrid when you need quality guarantees but pure exact is too slow.

**4. SOLVER CONFIGURATION**

Set up the optimization engine:

Solver selection: Commercial solvers (Gurobi, CPLEX) are 10-100x faster than open-source for MIP. HiGHS and SCIP are excellent free options. Google OR-Tools provides good interfaces. For heuristics, custom implementation or frameworks like Optuna work well. Match solver to problem type and budget.

Key parameters: MIP gap controls when to stop—1-5% gap is often acceptable and much faster than proving optimality. Time limits prevent runaway computation. Preprocessing simplifies the problem automatically. Parallelization uses multiple cores. Warm starts seed with previous solutions for faster convergence.

Tuning for performance: Enable presolve to tighten bounds and reduce problem size. Adjust branching priority to focus on important variables. Add cutting planes for specific problem structures. Configure node selection strategy. For large problems, use decomposition to break into subproblems.

**5. SOLUTION VALIDATION**

Verify the solution works:

Feasibility verification: Does the solution satisfy all constraints? Check constraint violations explicitly. Use solver's built-in feasibility checks. Test with original business rules, not just mathematical constraints.

Optimality verification: For exact methods, verify the optimality gap is within tolerance. For heuristics, compare against bounds if available, or against baseline solutions. Run multiple times with different starting points to check consistency.

Sensitivity analysis: How stable is the solution? Test objective coefficient ranges—how much can costs change before the solution changes? Test constraint right-hand sides—how does solution change with capacity or demand? Identify binding constraints that drive the solution.

Business validation: Does the solution make business sense? Review with domain experts. Check for artifacts of the formulation that don't match reality. Validate against historical decisions and outcomes.

**6. APPLICATION DOMAINS**

Apply optimization to common problems:

Supply chain optimization: Network design determines facility locations and flows. Inventory optimization balances holding costs and service levels. Transportation optimization routes vehicles and loads. Production planning schedules what to make when. These problems often have network structure enabling efficient algorithms.

Resource allocation: Workforce scheduling assigns people to shifts and tasks. Machine scheduling sequences jobs on equipment. Budget allocation distributes limited funds across projects. Capacity planning sizes resources for future demand. These often involve assignment or scheduling structures.

Financial optimization: Portfolio optimization balances risk and return—typically quadratic programming. Capital allocation distributes investment across opportunities. Pricing optimization sets prices to maximize revenue. Risk management optimizes hedging strategies.

Scheduling: Job shop scheduling sequences operations across machines. Timetabling assigns events to time slots and rooms. Crew scheduling assigns personnel to trips or shifts. Project scheduling sequences activities with resource constraints. These are often computationally hard, benefiting from heuristics.

**7. ROBUSTNESS AND UNCERTAINTY**

Handle real-world variability:

Scenario analysis: Test solutions across multiple scenarios—optimistic, expected, pessimistic. Identify solutions that perform well across scenarios. Quantify regret (gap from best possible in each scenario).

Robust optimization: Optimize for worst-case performance over uncertainty set. Produces conservative solutions that work even if parameters are adversarial. Trade off expected performance for guaranteed worst-case.

Stochastic optimization: Model uncertainty probabilistically with scenarios or distributions. Two-stage models make decisions now, then recourse decisions after uncertainty resolves. Chance constraints ensure feasibility with high probability.

Sensitivity-based hedging: Identify parameters with high sensitivity. Build slack or flexibility for those parameters. Focus data quality efforts on high-impact inputs.

**8. PRODUCTION DEPLOYMENT**

Put optimization into operations:

Integration architecture: Connect to data sources for inputs (demand forecasts, costs, capacities). Interface with execution systems for outputs (orders, schedules, allocations). Handle data validation and error recovery. Schedule runs (batch) or trigger on events (real-time).

Performance monitoring: Track solve time, optimality gap, and solution quality over time. Alert on infeasibility or degraded solutions. Monitor business outcomes to validate optimization impact.

Maintenance: Update parameters as business changes. Refine formulation as edge cases emerge. Re-tune solver as problem characteristics evolve. Plan for version upgrades.

Continuous improvement: Use solution data to improve forecasts and parameters. A/B test optimization vs baseline. Track value delivered. Identify opportunities to expand scope.

Deliver your optimization solution as:

1. **PROBLEM DEFINITION** - Business objective, decision type, scale, constraints

2. **MATHEMATICAL FORMULATION** - Objective function, variables, constraints in mathematical notation

3. **ALGORITHM CHOICE** - Selected method with rationale, expected performance

4. **SOLVER CONFIGURATION** - Solver, parameters, time limits, gap tolerance

5. **VALIDATION PLAN** - Feasibility checks, sensitivity analysis, business validation

6. **DEPLOYMENT APPROACH** - Integration points, monitoring, maintenance plan

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{PROBLEM_NAME}` | Optimization problem being solved | "Supply Chain Network Design", "Production Scheduling", "Portfolio Allocation" |
| `{OBJECTIVE}` | What to optimize | "Minimize total logistics cost", "Maximize production throughput", "Maximize risk-adjusted return" |
| `{SCALE_CONSTRAINTS}` | Problem size and requirements | "500 SKUs across 20 warehouses, solve in under 10 minutes", "1000 jobs on 50 machines" |

## Usage Examples

### Example 1: Supply Chain Network Optimization

```
Develop an optimization solution for Distribution Network Design to 
minimize total logistics cost with 10,000 SKUs across 50 potential 
warehouse locations solving weekly.
```

**Expected Output:**
- Problem: Facility location + transportation, MIP with binary location variables
- Formulation: Min transport + fixed costs, subject to demand coverage, capacity limits
- Algorithm: Branch-and-cut with Gurobi, warm start from previous week
- Configuration: 2% MIP gap, 30-minute time limit, enable presolve
- Validation: Check all demand served, sensitivity on facility costs, compare vs current network
- Result: 15% cost reduction, $5M annual savings

### Example 2: Production Scheduling

```
Develop an optimization solution for Manufacturing Job Shop Scheduling 
to minimize makespan with 500 jobs across 20 machines solving in 
real-time for daily planning.
```

**Expected Output:**
- Problem: Job shop scheduling, NP-hard combinatorial optimization
- Formulation: Sequence variables, disjunctive constraints, makespan objective
- Algorithm: Hybrid—constraint programming for feasibility, genetic algorithm for optimization
- Configuration: 5% gap tolerance, 5-minute time limit, restart from current schedule
- Validation: Verify precedence constraints, simulate on historical data
- Result: 20% makespan reduction, 15% throughput increase

### Example 3: Portfolio Optimization

```
Develop an optimization solution for Investment Portfolio Optimization 
to maximize risk-adjusted return with 1000 securities subject to 
risk limits and sector constraints.
```

**Expected Output:**
- Problem: Mean-variance optimization, quadratic programming
- Formulation: Max return - λ×variance, subject to budget, risk limits, sector bounds
- Algorithm: Interior point method for QP, solved in seconds
- Configuration: Gurobi or MOSEK, barrier algorithm, tight tolerance
- Validation: Check portfolio weights sum to 1, verify risk within limits, backtest
- Result: Sharpe ratio 1.8, 12% expected return, 8% volatility

## Cross-References

- **Predictive Modeling:** predictive-modeling-framework.md - ML for demand forecasting inputs
- **Time Series:** time-series-analysis.md - Forecasting for optimization parameters
- **Dashboard Design:** dashboard-design-patterns.md - Visualizing optimization results
- **AI Strategy:** ai-strategy-roadmap.md - AI/ML enhancement of optimization
