---
title: Network Modeling and Simulation
category: data-analytics/Research Analytics
tags: [data-analytics, network-analysis, modeling, simulation, random-graphs, network-generation]
use_cases:
  - Generating synthetic networks for testing and benchmarking
  - Understanding network formation mechanisms
  - Creating null models for statistical comparison
  - Simulating network growth and dynamics
related_templates:
  - network-analysis-overview.md
  - network-visualization-basics.md
  - temporal-network-analysis.md
  - applied-network-analytics.md
last_updated: 2025-11-09
---

# Network Modeling and Simulation

## Purpose
Generate synthetic networks, understand network formation mechanisms, create null models for statistical testing, simulate network growth processes, and benchmark analysis algorithms using theoretically grounded network models.

## Template

```
You are a network modeling expert. Generate and analyze synthetic networks using [NETWORK_MODELS] to understand [MODELING_OBJECTIVES] and compare with [REAL_NETWORK_DATA].

MODELING CONTEXT:
- Target network size: [TARGET_SIZE] nodes
- Network characteristics: [DESIRED_PROPERTIES]
- Model types: [MODEL_TYPES]
- Comparison network: [COMPARISON_NETWORK]

MODELING OBJECTIVES:
- Primary goal: [MODELING_GOAL]
- Null hypothesis testing: [NULL_HYPOTHESIS]
- Growth simulation: [GROWTH_DYNAMICS]
- Parameter estimation: [PARAMETER_FITTING]

### RANDOM GRAPH MODELS

```python
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from collections import Counter

class NetworkModelGenerator:
    def __init__(self):
        self.generated_networks = {}
        self.model_parameters = {}

    def generate_erdos_renyi(self, n, p=None, m=None, model='GNP'):
        """
        Generate Erdős-Rényi random graph

        Parameters:
        - n: Number of nodes
        - p: Probability of edge creation (for G(n,p) model)
        - m: Number of edges (for G(n,m) model)
        - model: 'GNP' for G(n,p), 'GNM' for G(n,m)
        """

        if model == 'GNP' and p is not None:
            # G(n,p) model: Each edge exists with probability p
            G = nx.erdos_renyi_graph(n, p)
            params = {'n': n, 'p': p, 'model': 'GNP'}
        elif model == 'GNM' and m is not None:
            # G(n,m) model: Exactly m edges
            G = nx.gnm_random_graph(n, m)
            params = {'n': n, 'm': m, 'model': 'GNM'}
        else:
            raise ValueError("Specify either p (for GNP) or m (for GNM)")

        self.generated_networks['erdos_renyi'] = G
        self.model_parameters['erdos_renyi'] = params

        return G

    def generate_barabasi_albert(self, n, m, seed=None):
        """
        Generate Barabási-Albert scale-free network

        Parameters:
        - n: Number of nodes
        - m: Number of edges to attach from new node
        - seed: Random seed for reproducibility
        """

        # Preferential attachment model
        G = nx.barabasi_albert_graph(n, m, seed=seed)

        params = {'n': n, 'm': m, 'model': 'Barabasi-Albert'}

        self.generated_networks['barabasi_albert'] = G
        self.model_parameters['barabasi_albert'] = params

        return G

    def generate_watts_strogatz(self, n, k, p, seed=None):
        """
        Generate Watts-Strogatz small-world network

        Parameters:
        - n: Number of nodes
        - k: Each node connected to k nearest neighbors in ring
        - p: Probability of rewiring each edge
        - seed: Random seed for reproducibility
        """

        G = nx.watts_strogatz_graph(n, k, p, seed=seed)

        params = {'n': n, 'k': k, 'p': p, 'model': 'Watts-Strogatz'}

        self.generated_networks['watts_strogatz'] = G
        self.model_parameters['watts_strogatz'] = params

        return G

    def generate_configuration_model(self, degree_sequence):
        """
        Generate network with specified degree sequence

        Parameters:
        - degree_sequence: List of node degrees
        """

        # Ensure degree sequence is graphical
        if sum(degree_sequence) % 2 != 0:
            degree_sequence = list(degree_sequence)
            degree_sequence[0] += 1

        G = nx.configuration_model(degree_sequence)

        # Remove self-loops and parallel edges
        G = nx.Graph(G)
        G.remove_edges_from(nx.selfloop_edges(G))

        params = {'degree_sequence': degree_sequence, 'model': 'Configuration'}

        self.generated_networks['configuration'] = G
        self.model_parameters['configuration'] = params

        return G

    def generate_stochastic_block_model(self, sizes, p_matrix, seed=None):
        """
        Generate stochastic block model (community structure)

        Parameters:
        - sizes: List of community sizes
        - p_matrix: Probability matrix for edges between/within communities
        - seed: Random seed
        """

        G = nx.stochastic_block_model(sizes, p_matrix, seed=seed)

        params = {
            'sizes': sizes,
            'p_matrix': p_matrix,
            'model': 'Stochastic Block Model'
        }

        self.generated_networks['stochastic_block'] = G
        self.model_parameters['stochastic_block'] = params

        return G

    def generate_powerlaw_cluster_graph(self, n, m, p, seed=None):
        """
        Generate Holme-Kim power-law cluster graph

        Parameters:
        - n: Number of nodes
        - m: Number of random edges to add for each new node
        - p: Probability of adding a triangle after adding a random edge
        - seed: Random seed
        """

        G = nx.powerlaw_cluster_graph(n, m, p, seed=seed)

        params = {'n': n, 'm': m, 'p': p, 'model': 'Powerlaw Cluster'}

        self.generated_networks['powerlaw_cluster'] = G
        self.model_parameters['powerlaw_cluster'] = params

        return G

    def generate_random_geometric_graph(self, n, radius, dim=2, seed=None):
        """
        Generate random geometric graph (spatial network)

        Parameters:
        - n: Number of nodes
        - radius: Distance threshold for edge creation
        - dim: Dimension of space (default: 2)
        - seed: Random seed
        """

        G = nx.random_geometric_graph(n, radius, dim=dim, seed=seed)

        params = {'n': n, 'radius': radius, 'dim': dim, 'model': 'Random Geometric'}

        self.generated_networks['random_geometric'] = G
        self.model_parameters['random_geometric'] = params

        return G

# Generate various network models
model_generator = NetworkModelGenerator()

# Erdős-Rényi random graph
er_network = model_generator.generate_erdos_renyi(
    n=[NUM_NODES],
    p=[EDGE_PROBABILITY]
)

# Barabási-Albert scale-free network
ba_network = model_generator.generate_barabasi_albert(
    n=[NUM_NODES],
    m=[ATTACHMENT_EDGES]
)

# Watts-Strogatz small-world network
ws_network = model_generator.generate_watts_strogatz(
    n=[NUM_NODES],
    k=[NEAREST_NEIGHBORS],
    p=[REWIRING_PROBABILITY]
)

# Stochastic block model (communities)
sbm_network = model_generator.generate_stochastic_block_model(
    sizes=[COMMUNITY_SIZES],
    p_matrix=[PROBABILITY_MATRIX]
)
```

### NETWORK MODEL ANALYSIS AND COMPARISON

```python
class NetworkModelAnalyzer:
    def __init__(self, networks_dict):
        self.networks = networks_dict
        self.comparison_metrics = {}

    def calculate_network_properties(self, G):
        """Calculate comprehensive network properties"""

        properties = {}

        # Basic properties
        properties['num_nodes'] = G.number_of_nodes()
        properties['num_edges'] = G.number_of_edges()
        properties['density'] = nx.density(G)

        # Degree distribution
        degrees = [d for n, d in G.degree()]
        properties['avg_degree'] = np.mean(degrees)
        properties['degree_variance'] = np.var(degrees)

        # Clustering
        properties['avg_clustering'] = nx.average_clustering(G)
        properties['transitivity'] = nx.transitivity(G)

        # Connected components
        if nx.is_connected(G):
            properties['is_connected'] = True
            properties['num_components'] = 1
            properties['largest_component_size'] = G.number_of_nodes()

            # Path metrics (only for connected graphs)
            if G.number_of_nodes() < 1000:
                properties['avg_path_length'] = nx.average_shortest_path_length(G)
                properties['diameter'] = nx.diameter(G)
        else:
            properties['is_connected'] = False
            components = list(nx.connected_components(G))
            properties['num_components'] = len(components)
            properties['largest_component_size'] = len(max(components, key=len))

            # Calculate for largest component
            largest_cc = G.subgraph(max(components, key=len))
            if largest_cc.number_of_nodes() < 1000:
                properties['avg_path_length'] = nx.average_shortest_path_length(largest_cc)
                properties['diameter'] = nx.diameter(largest_cc)

        # Degree distribution fitting
        properties['degree_distribution'] = degrees
        properties['power_law_alpha'] = self._estimate_power_law_exponent(degrees)

        # Assortativity
        properties['degree_assortativity'] = nx.degree_assortativity_coefficient(G)

        return properties

    def _estimate_power_law_exponent(self, degrees):
        """Estimate power-law exponent using MLE"""
        degrees_filtered = [d for d in degrees if d > 0]
        if len(degrees_filtered) < 2:
            return None

        # Simple MLE estimator: alpha = 1 + n / sum(ln(x_i / x_min))
        x_min = min(degrees_filtered)
        n = len(degrees_filtered)
        sum_log = sum(np.log(d / x_min) for d in degrees_filtered)

        if sum_log > 0:
            alpha = 1 + n / sum_log
            return alpha
        return None

    def compare_with_real_network(self, real_network, model_name):
        """Compare generated model with real network"""

        real_props = self.calculate_network_properties(real_network)
        model_props = self.calculate_network_properties(self.networks[model_name])

        comparison = pd.DataFrame({
            'Real Network': real_props,
            f'{model_name.title()} Model': model_props
        })

        # Calculate relative differences
        comparison['Relative Difference'] = abs(
            comparison['Real Network'] - comparison[f'{model_name.title()} Model']
        ) / (comparison['Real Network'] + 1e-10)

        return comparison

    def test_small_world_properties(self, G):
        """Test for small-world network properties"""

        n = G.number_of_nodes()
        m = G.number_of_edges()

        # Calculate actual properties
        C_actual = nx.average_clustering(G)

        if nx.is_connected(G):
            L_actual = nx.average_shortest_path_length(G)
        else:
            # Use largest component
            largest_cc = max(nx.connected_components(G), key=len)
            L_actual = nx.average_shortest_path_length(G.subgraph(largest_cc))

        # Compare with random graph
        p = 2 * m / (n * (n - 1))
        C_random = p
        L_random = np.log(n) / np.log(n * p) if p > 0 else float('inf')

        # Small-world coefficient
        sigma = (C_actual / C_random) / (L_actual / L_random) if L_random > 0 and C_random > 0 else None

        return {
            'clustering_actual': C_actual,
            'clustering_random': C_random,
            'path_length_actual': L_actual,
            'path_length_random': L_random,
            'small_world_coefficient': sigma,
            'is_small_world': sigma > 1 if sigma else False
        }

    def test_scale_free_properties(self, G):
        """Test for scale-free network properties"""

        degrees = [d for n, d in G.degree()]

        # Fit power law
        alpha = self._estimate_power_law_exponent(degrees)

        # Kolmogorov-Smirnov test
        # Compare empirical distribution with power law
        degree_counts = Counter(degrees)
        unique_degrees = sorted(degree_counts.keys())
        empirical_ccdf = []
        for k in unique_degrees:
            empirical_ccdf.append(sum(degree_counts[d] for d in unique_degrees if d >= k) / len(degrees))

        # Test on log-log scale
        log_degrees = np.log(unique_degrees)
        log_ccdf = np.log(empirical_ccdf)

        # Linear regression
        slope, intercept, r_value, p_value, std_err = stats.linregress(log_degrees, log_ccdf)

        return {
            'power_law_alpha': alpha,
            'log_log_slope': slope,
            'r_squared': r_value**2,
            'p_value': p_value,
            'is_scale_free': r_value**2 > 0.8  # High R² suggests power law
        }

    def visualize_model_comparison(self, real_network=None):
        """Create comprehensive visualization comparing models"""

        fig, axes = plt.subplots(2, 3, figsize=(18, 12))

        models = list(self.networks.keys())
        if real_network:
            models = ['Real Network'] + models
            all_networks = {'Real Network': real_network, **self.networks}
        else:
            all_networks = self.networks

        # Degree distribution comparison
        ax = axes[0, 0]
        for name, G in all_networks.items():
            degrees = [d for n, d in G.degree()]
            degree_counts = Counter(degrees)
            degrees_sorted = sorted(degree_counts.keys())
            counts = [degree_counts[d] for d in degrees_sorted]
            ax.loglog(degrees_sorted, counts, 'o-', label=name, alpha=0.7, markersize=4)
        ax.set_xlabel('Degree (log scale)')
        ax.set_ylabel('Count (log scale)')
        ax.set_title('Degree Distribution Comparison')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # Clustering coefficient comparison
        ax = axes[0, 1]
        clustering_values = [nx.average_clustering(G) for G in all_networks.values()]
        ax.bar(range(len(all_networks)), clustering_values, color='skyblue', edgecolor='black')
        ax.set_xticks(range(len(all_networks)))
        ax.set_xticklabels(all_networks.keys(), rotation=45, ha='right')
        ax.set_ylabel('Average Clustering Coefficient')
        ax.set_title('Clustering Coefficient Comparison')

        # Density comparison
        ax = axes[0, 2]
        density_values = [nx.density(G) for G in all_networks.values()]
        ax.bar(range(len(all_networks)), density_values, color='lightcoral', edgecolor='black')
        ax.set_xticks(range(len(all_networks)))
        ax.set_xticklabels(all_networks.keys(), rotation=45, ha='right')
        ax.set_ylabel('Network Density')
        ax.set_title('Density Comparison')

        # Component size comparison
        ax = axes[1, 0]
        component_sizes = []
        for G in all_networks.values():
            if nx.is_connected(G):
                component_sizes.append(G.number_of_nodes())
            else:
                component_sizes.append(len(max(nx.connected_components(G), key=len)))
        ax.bar(range(len(all_networks)), component_sizes, color='lightgreen', edgecolor='black')
        ax.set_xticks(range(len(all_networks)))
        ax.set_xticklabels(all_networks.keys(), rotation=45, ha='right')
        ax.set_ylabel('Largest Component Size')
        ax.set_title('Connectivity Comparison')

        # Path length comparison (for connected networks)
        ax = axes[1, 1]
        path_lengths = []
        model_names = []
        for name, G in all_networks.items():
            if nx.is_connected(G) and G.number_of_nodes() < 1000:
                path_lengths.append(nx.average_shortest_path_length(G))
                model_names.append(name)
        if path_lengths:
            ax.bar(range(len(model_names)), path_lengths, color='plum', edgecolor='black')
            ax.set_xticks(range(len(model_names)))
            ax.set_xticklabels(model_names, rotation=45, ha='right')
            ax.set_ylabel('Average Path Length')
            ax.set_title('Path Length Comparison')

        # Degree assortativity comparison
        ax = axes[1, 2]
        assortativity_values = [nx.degree_assortativity_coefficient(G) for G in all_networks.values()]
        ax.bar(range(len(all_networks)), assortativity_values, color='gold', edgecolor='black')
        ax.axhline(y=0, color='r', linestyle='--', alpha=0.5)
        ax.set_xticks(range(len(all_networks)))
        ax.set_xticklabels(all_networks.keys(), rotation=45, ha='right')
        ax.set_ylabel('Degree Assortativity')
        ax.set_title('Assortativity Comparison')

        plt.tight_layout()
        return fig

# Analyze generated models
analyzer = NetworkModelAnalyzer(model_generator.generated_networks)

# Calculate properties for each model
for model_name, network in model_generator.generated_networks.items():
    print(f"\n=== {model_name.upper()} MODEL ===")
    props = analyzer.calculate_network_properties(network)
    for key, value in props.items():
        if key != 'degree_distribution':
            print(f"  {key}: {value}")

# Test for small-world properties
print("\n=== SMALL-WORLD PROPERTIES ===")
ws_properties = analyzer.test_small_world_properties(ws_network)
for key, value in ws_properties.items():
    print(f"  {key}: {value}")

# Test for scale-free properties
print("\n=== SCALE-FREE PROPERTIES ===")
ba_properties = analyzer.test_scale_free_properties(ba_network)
for key, value in ba_properties.items():
    print(f"  {key}: {value}")

# Compare with real network (if available)
if '[REAL_NETWORK_AVAILABLE]':
    real_network = nx.read_edgelist('[REAL_NETWORK_PATH]')
    comparison = analyzer.compare_with_real_network(real_network, 'barabasi_albert')
    print("\n=== MODEL vs REAL NETWORK COMPARISON ===")
    print(comparison)

# Visualization
viz = analyzer.visualize_model_comparison()
plt.show()
```

OUTPUT REQUIREMENTS:
Deliver comprehensive network modeling analysis including:

1. **Generated Network Models**
   - Erdős-Rényi random graphs
   - Barabási-Albert scale-free networks
   - Watts-Strogatz small-world networks
   - Configuration models
   - Stochastic block models

2. **Model Properties**
   - Basic statistics for each model
   - Degree distributions
   - Clustering coefficients
   - Path length distributions

3. **Model Validation**
   - Small-world coefficient testing
   - Scale-free properties verification
   - Statistical goodness-of-fit tests
   - Parameter estimation

4. **Comparative Analysis**
   - Model vs. model comparison
   - Model vs. real network comparison
   - Strengths and limitations of each model
   - Best-fit model recommendation

5. **Visualizations**
   - Degree distribution comparisons
   - Property comparisons across models
   - Network layout visualizations
   - Statistical test results
```

## Variables

### Model Generation Variables
- [NUM_NODES] - Number of nodes to generate
- [EDGE_PROBABILITY] - Edge probability for Erdős-Rényi
- [ATTACHMENT_EDGES] - Edges to attach in Barabási-Albert
- [NEAREST_NEIGHBORS] - k value for Watts-Strogatz
- [REWIRING_PROBABILITY] - Rewiring probability for Watts-Strogatz
- [COMMUNITY_SIZES] - Sizes of communities in SBM
- [PROBABILITY_MATRIX] - Edge probability matrix for SBM

### Analysis Variables
- [MODELING_OBJECTIVES] - Goals of network modeling
- [MODELING_GOAL] - Primary modeling goal
- [MODEL_TYPES] - Types of models to generate
- [TARGET_SIZE] - Target network size
- [DESIRED_PROPERTIES] - Desired network characteristics

### Comparison Variables
- [REAL_NETWORK_DATA] - Real network for comparison
- [COMPARISON_NETWORK] - Network to compare against
- [REAL_NETWORK_AVAILABLE] - Whether real network is available
- [REAL_NETWORK_PATH] - Path to real network data
- [NULL_HYPOTHESIS] - Null hypothesis for testing
- [PARAMETER_FITTING] - Parameter fitting objectives
- [GROWTH_DYNAMICS] - Growth dynamics to simulate

## Understanding Network Models

### 1. Erdős-Rényi (ER) Random Graph
**Formation:** Each edge exists independently with probability p
**Properties:**
- Poisson degree distribution
- Low clustering
- Short average path length
- No community structure
**Use Cases:** Null model, baseline comparison

### 2. Barabási-Albert (BA) Scale-Free
**Formation:** Preferential attachment (rich get richer)
**Properties:**
- Power-law degree distribution
- Presence of hubs
- Robust to random failures
- Vulnerable to targeted attacks
**Use Cases:** Social networks, citation networks, internet

### 3. Watts-Strogatz (WS) Small-World
**Formation:** Start with ring, rewire edges with probability p
**Properties:**
- High clustering
- Short path length
- Regular + random = small-world
**Use Cases:** Social networks, neural networks, power grids

### 4. Configuration Model
**Formation:** Generate network with exact degree sequence
**Properties:**
- Arbitrary degree distribution
- Preserves degree sequence
- Random otherwise
**Use Cases:** Null model preserving degree distribution

### 5. Stochastic Block Model (SBM)
**Formation:** Community-based edge probabilities
**Properties:**
- Built-in community structure
- Controllable modularity
- Within/between group densities
**Use Cases:** Testing community detection algorithms

## Best Practices

1. **Model Selection**
   - Match model to research question
   - Consider computational constraints
   - Validate model assumptions

2. **Parameter Tuning**
   - Fit parameters to real network properties
   - Use multiple metrics for fitting
   - Validate parameter estimates

3. **Null Model Testing**
   - Generate multiple realizations
   - Calculate statistical significance
   - Report confidence intervals

4. **Model Validation**
   - Test against multiple properties
   - Use out-of-sample validation
   - Check for overfitting

5. **Comparative Analysis**
   - Compare multiple models
   - Use diverse metrics
   - Consider model complexity

## Usage Example

```
NUM_NODES: 1000
EDGE_PROBABILITY: 0.01
ATTACHMENT_EDGES: 3
NEAREST_NEIGHBORS: 6
REWIRING_PROBABILITY: 0.1
MODELING_GOAL: "Create null models for statistical testing and understand network formation"
REAL_NETWORK_DATA: "empirical_network.csv"
NULL_HYPOTHESIS: "Observed clustering is not significantly different from random"
```
