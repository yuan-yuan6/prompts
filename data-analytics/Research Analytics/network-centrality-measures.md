---
title: Network Centrality Measures and Node Analysis
category: data-analytics/Research Analytics
tags: [data-analytics, network-analysis, centrality, influence, node-importance]
use_cases:
  - Identifying influential nodes and key players in networks
  - Analyzing node importance from multiple perspectives
  - Comparing different centrality measures
  - Finding network hubs and bottlenecks
related_templates:
  - network-analysis-overview.md
  - network-visualization-basics.md
  - network-community-detection.md
  - applied-network-analytics.md
last_updated: 2025-11-09
---

# Network Centrality Measures and Node Analysis

## Purpose
Identify and analyze the most important nodes in a network using comprehensive centrality measures. Understand node importance from multiple perspectives including connectivity, information flow control, proximity, and influence propagation.

## Template

```
You are a network centrality expert. Analyze the importance of nodes in [NETWORK_DATA_SOURCE] using [CENTRALITY_MEASURES] to identify [NODE_IMPORTANCE_GOALS].

NETWORK CONTEXT:
- Network type: [NETWORK_TYPE]
- Analysis focus: [CENTRALITY_FOCUS] (Influence/Information Flow/Connectivity/Proximity)
- Scale: [NODE_COUNT] nodes, [EDGE_COUNT] edges
- Domain: [NETWORK_DOMAIN]

CENTRALITY OBJECTIVES:
- Primary measures: [PRIMARY_CENTRALITY_MEASURES]
- Top nodes to identify: [TOP_K_NODES]
- Correlation analysis: [ANALYZE_CORRELATIONS]
- Distribution analysis: [ANALYZE_DISTRIBUTIONS]

### COMPREHENSIVE CENTRALITY ANALYSIS

```python
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, skew, kurtosis
from collections import Counter

class CentralityAnalyzer:
    def __init__(self, network):
        self.network = network
        self.centrality_scores = {}

    def calculate_all_centralities(self, normalized=True):
        """Calculate all major centrality measures"""

        G = self.network
        centralities = {}

        print("Calculating centrality measures...")

        # 1. Degree Centrality
        print("  - Degree centrality")
        centralities['degree'] = nx.degree_centrality(G)

        # 2. Betweenness Centrality
        print("  - Betweenness centrality")
        centralities['betweenness'] = nx.betweenness_centrality(
            G,
            normalized=normalized,
            k=min(100, G.number_of_nodes())  # Sample for large networks
        )

        # 3. Closeness Centrality
        print("  - Closeness centrality")
        if nx.is_connected(G) or nx.is_directed(G):
            centralities['closeness'] = nx.closeness_centrality(G, distance=None)
        else:
            # Calculate for each component separately
            centralities['closeness'] = {}
            for component in nx.connected_components(G):
                subG = G.subgraph(component)
                closeness_sub = nx.closeness_centrality(subG)
                centralities['closeness'].update(closeness_sub)

        # 4. Eigenvector Centrality
        print("  - Eigenvector centrality")
        try:
            centralities['eigenvector'] = nx.eigenvector_centrality(G, max_iter=1000)
        except nx.NetworkXError:
            print("    Warning: Eigenvector centrality failed, using PageRank instead")
            centralities['eigenvector'] = nx.pagerank(G)

        # 5. PageRank
        print("  - PageRank")
        centralities['pagerank'] = nx.pagerank(G, alpha=0.85, max_iter=1000)

        # 6. Katz Centrality
        print("  - Katz centrality")
        try:
            alpha = 1 / (max(dict(G.degree()).values()) + 1)
            centralities['katz'] = nx.katz_centrality(G, alpha=alpha, max_iter=1000)
        except (nx.NetworkXError, ZeroDivisionError):
            print("    Warning: Katz centrality calculation failed")
            centralities['katz'] = {node: 0 for node in G.nodes()}

        # 7. Harmonic Centrality
        print("  - Harmonic centrality")
        centralities['harmonic'] = nx.harmonic_centrality(G, distance=None)

        # 8. Load Centrality (for weighted networks)
        if nx.is_weighted(G):
            print("  - Load centrality")
            centralities['load'] = nx.load_centrality(G, weight='weight')

        # 9. Current Flow Betweenness Centrality (for connected networks)
        if nx.is_connected(G) and G.number_of_nodes() < 500:
            print("  - Current flow betweenness centrality")
            try:
                centralities['current_flow_betweenness'] = nx.current_flow_betweenness_centrality(G)
            except:
                print("    Warning: Current flow betweenness calculation failed")

        # Store results
        self.centrality_scores = centralities
        return centralities

    def analyze_centrality_correlations(self):
        """Analyze correlations between centrality measures"""

        if not self.centrality_scores:
            self.calculate_all_centralities()

        # Create DataFrame with centrality scores
        centrality_df = pd.DataFrame(self.centrality_scores)
        centrality_df = centrality_df.fillna(0)

        # Calculate correlations
        correlation_matrix = centrality_df.corr()

        # Statistical significance testing
        p_values = pd.DataFrame(
            index=correlation_matrix.index,
            columns=correlation_matrix.columns
        )

        for i in correlation_matrix.index:
            for j in correlation_matrix.columns:
                if i != j:
                    corr, p_val = pearsonr(centrality_df[i], centrality_df[j])
                    p_values.loc[i, j] = p_val
                else:
                    p_values.loc[i, j] = 0.0

        # Find significant correlations
        significant_mask = (correlation_matrix.abs() > 0.5) & (p_values.astype(float) < 0.05)
        significant_correlations = correlation_matrix[significant_mask]

        return {
            'correlation_matrix': correlation_matrix,
            'p_values': p_values,
            'significant_correlations': significant_correlations,
            'centrality_dataframe': centrality_df
        }

    def identify_top_nodes(self, centrality_measure, top_k=10):
        """Identify top nodes by centrality measure"""

        if centrality_measure not in self.centrality_scores:
            raise ValueError(f"Centrality measure '{centrality_measure}' not calculated")

        scores = self.centrality_scores[centrality_measure]
        top_nodes = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]

        return {
            'centrality_measure': centrality_measure,
            'top_nodes': top_nodes,
            'scores_distribution': {
                'mean': np.mean(list(scores.values())),
                'median': np.median(list(scores.values())),
                'std': np.std(list(scores.values())),
                'max': max(scores.values()),
                'min': min(scores.values())
            }
        }

    def centrality_distribution_analysis(self):
        """Analyze the distribution of centrality measures"""

        analysis = {}

        for measure, scores in self.centrality_scores.items():
            values = list(scores.values())

            # Basic statistics
            stats = {
                'count': len(values),
                'mean': np.mean(values),
                'median': np.median(values),
                'std': np.std(values),
                'min': min(values),
                'max': max(values),
                'range': max(values) - min(values),
                'q25': np.percentile(values, 25),
                'q75': np.percentile(values, 75),
                'iqr': np.percentile(values, 75) - np.percentile(values, 25),
                'skewness': skew(values),
                'kurtosis': kurtosis(values)
            }

            # Distribution shape analysis
            stats['is_power_law'] = self._test_power_law_distribution(values)
            stats['concentration_ratio'] = self._calculate_concentration_ratio(values)

            analysis[measure] = stats

        return analysis

    def _test_power_law_distribution(self, values):
        """Test if distribution follows power law"""
        log_values = np.log([v + 1e-10 for v in values if v > 0])
        if len(log_values) < 10:
            return False

        # Linear regression on log-log scale
        ranks = np.log(np.arange(1, len(log_values) + 1))
        sorted_log_values = np.sort(log_values)[::-1]

        correlation = np.corrcoef(ranks, sorted_log_values)[0, 1]
        return correlation < -0.8  # Strong negative correlation indicates power law

    def _calculate_concentration_ratio(self, values):
        """Calculate concentration ratio (top 10% vs. rest)"""
        sorted_values = sorted(values, reverse=True)
        top_10_percent = int(len(sorted_values) * 0.1)
        top_10_sum = sum(sorted_values[:top_10_percent])
        total_sum = sum(sorted_values)
        return top_10_sum / total_sum if total_sum > 0 else 0

    def compare_centrality_rankings(self, measures=None, top_k=20):
        """Compare node rankings across different centrality measures"""

        if measures is None:
            measures = list(self.centrality_scores.keys())

        rankings = {}
        for measure in measures:
            if measure in self.centrality_scores:
                scores = self.centrality_scores[measure]
                ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
                rankings[measure] = [node for node, score in ranked[:top_k]]

        # Calculate rank agreement
        from scipy.stats import kendalltau

        agreement_matrix = pd.DataFrame(index=measures, columns=measures)

        for m1 in measures:
            for m2 in measures:
                if m1 in self.centrality_scores and m2 in self.centrality_scores:
                    # Get common nodes
                    common_nodes = set(self.centrality_scores[m1].keys()) & \
                                  set(self.centrality_scores[m2].keys())

                    if len(common_nodes) > 1:
                        scores1 = [self.centrality_scores[m1][n] for n in common_nodes]
                        scores2 = [self.centrality_scores[m2][n] for n in common_nodes]

                        tau, p_value = kendalltau(scores1, scores2)
                        agreement_matrix.loc[m1, m2] = tau

        return {
            'rankings': rankings,
            'agreement_matrix': agreement_matrix
        }

    def visualize_centrality_measures(self, centrality_results=None):
        """Visualize different centrality measures"""

        G = self.network

        if centrality_results is None:
            centrality_results = {
                'degree': self.centrality_scores.get('degree', nx.degree_centrality(G)),
                'betweenness': self.centrality_scores.get('betweenness', nx.betweenness_centrality(G)),
                'closeness': self.centrality_scores.get('closeness', nx.closeness_centrality(G)),
                'pagerank': self.centrality_scores.get('pagerank', nx.pagerank(G))
            }

        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.flatten()

        pos = nx.spring_layout(G, k=1/np.sqrt(G.number_of_nodes()), iterations=50)

        for i, (measure, scores) in enumerate(centrality_results.items()):
            ax = axes[i]

            # Node sizes based on centrality
            node_sizes = [scores.get(node, 0) * 1000 + 50 for node in G.nodes()]

            # Color map
            node_colors = [scores.get(node, 0) for node in G.nodes()]

            # Draw network
            nodes = nx.draw_networkx_nodes(
                G, pos, ax=ax,
                node_size=node_sizes,
                node_color=node_colors,
                cmap=plt.cm.viridis,
                alpha=0.8
            )

            nx.draw_networkx_edges(
                G, pos, ax=ax,
                edge_color='gray',
                alpha=0.3,
                width=0.5
            )

            ax.set_title(f'{measure.title()} Centrality')
            ax.axis('off')

            # Add colorbar
            plt.colorbar(nodes, ax=ax, shrink=0.8)

        plt.tight_layout()
        return fig

    def plot_centrality_distributions(self):
        """Plot distribution of centrality measures"""

        n_measures = len(self.centrality_scores)
        fig, axes = plt.subplots(
            (n_measures + 1) // 2, 2,
            figsize=(14, 4 * ((n_measures + 1) // 2))
        )
        axes = axes.flatten() if n_measures > 1 else [axes]

        for idx, (measure, scores) in enumerate(self.centrality_scores.items()):
            ax = axes[idx]
            values = list(scores.values())

            # Histogram
            ax.hist(values, bins=50, alpha=0.7, edgecolor='black')
            ax.set_xlabel(f'{measure.title()} Score')
            ax.set_ylabel('Frequency')
            ax.set_title(f'{measure.title()} Centrality Distribution')

            # Add mean and median lines
            mean_val = np.mean(values)
            median_val = np.median(values)
            ax.axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.4f}')
            ax.axvline(median_val, color='blue', linestyle='--', label=f'Median: {median_val:.4f}')
            ax.legend()

        # Hide extra subplots
        for idx in range(n_measures, len(axes)):
            axes[idx].axis('off')

        plt.tight_layout()
        return fig

# Perform centrality analysis
centrality_analyzer = CentralityAnalyzer(network)

# Calculate all centrality measures
centrality_results = centrality_analyzer.calculate_all_centralities(normalized=[NORMALIZE])

# Analyze correlations between measures
centrality_correlations = centrality_analyzer.analyze_centrality_correlations()

# Identify top nodes for each measure
top_nodes_degree = centrality_analyzer.identify_top_nodes('degree', top_k=[TOP_K_NODES])
top_nodes_betweenness = centrality_analyzer.identify_top_nodes('betweenness', top_k=[TOP_K_NODES])
top_nodes_pagerank = centrality_analyzer.identify_top_nodes('pagerank', top_k=[TOP_K_NODES])

# Distribution analysis
centrality_distributions = centrality_analyzer.centrality_distribution_analysis()

# Compare rankings across measures
ranking_comparison = centrality_analyzer.compare_centrality_rankings(top_k=[TOP_K_NODES])

# Create visualizations
centrality_vis = centrality_analyzer.visualize_centrality_measures()
distribution_plots = centrality_analyzer.plot_centrality_distributions()

# Display correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    centrality_correlations['correlation_matrix'],
    annot=True,
    fmt='.3f',
    cmap='coolwarm',
    center=0,
    square=True
)
plt.title('Centrality Measures Correlation Matrix')
plt.tight_layout()
plt.show()

# Print top nodes for each measure
print("\n=== TOP NODES BY CENTRALITY MEASURE ===\n")
for measure in centrality_results.keys():
    top_analysis = centrality_analyzer.identify_top_nodes(measure, top_k=10)
    print(f"\n{measure.upper()} CENTRALITY:")
    print("-" * 50)
    for rank, (node, score) in enumerate(top_analysis['top_nodes'], 1):
        print(f"{rank:2d}. Node {node}: {score:.6f}")
```

OUTPUT REQUIREMENTS:
Deliver comprehensive centrality analysis including:

1. **Centrality Scores**
   - All calculated centrality measures
   - Node rankings for each measure
   - Score distributions and statistics
   - Power-law analysis

2. **Top Influential Nodes**
   - Top [TOP_K_NODES] nodes by each measure
   - Multi-measure consensus ranking
   - Nodes appearing in multiple top-k lists
   - Node-specific centrality profiles

3. **Correlation Analysis**
   - Correlation matrix between measures
   - Statistical significance (p-values)
   - Strong vs. weak measure relationships
   - Measure redundancy assessment

4. **Distribution Analysis**
   - Mean, median, std for each measure
   - Skewness and kurtosis
   - Concentration ratios
   - Power-law characteristics

5. **Comparative Insights**
   - Ranking agreement between measures
   - Measure-specific vs. universal hubs
   - Domain-appropriate measure recommendations
   - Key findings and interpretations
```

## Variables

### Network Context Variables
- [NETWORK_DATA_SOURCE] - Source of network data
- [NETWORK_TYPE] - Type of network (Directed/Undirected/Weighted)
- [NODE_COUNT] - Number of nodes
- [EDGE_COUNT] - Number of edges
- [NETWORK_DOMAIN] - Domain of the network (Social/Biological/Transportation)

### Centrality Configuration Variables
- [CENTRALITY_MEASURES] - Which centrality measures to calculate
- [PRIMARY_CENTRALITY_MEASURES] - Most important measures to focus on
- [NODE_IMPORTANCE_GOALS] - Goals for identifying important nodes
- [CENTRALITY_FOCUS] - Focus area (Influence/Information Flow/Connectivity)
- [TOP_K_NODES] - Number of top nodes to identify (default: 10)
- [NORMALIZE] - Whether to normalize centrality scores (True/False)

### Analysis Options Variables
- [ANALYZE_CORRELATIONS] - Perform correlation analysis (True/False)
- [ANALYZE_DISTRIBUTIONS] - Analyze centrality distributions (True/False)
- [COMPARE_RANKINGS] - Compare rankings across measures (True/False)
- [CONCENTRATION_THRESHOLD] - Threshold for concentration analysis
- [POWER_LAW_TEST] - Test for power-law distribution (True/False)

## Understanding Centrality Measures

### 1. Degree Centrality
**What it measures:** Number of direct connections
**Interpretation:** Social connectivity, immediate reach
**Best for:** Identifying well-connected hubs
**Formula:** Number of neighbors / (Total nodes - 1)

### 2. Betweenness Centrality
**What it measures:** Number of shortest paths passing through node
**Interpretation:** Control over information flow, brokerage
**Best for:** Finding bottlenecks and bridges
**Computational note:** Expensive for large networks (use sampling)

### 3. Closeness Centrality
**What it measures:** Average distance to all other nodes
**Interpretation:** How quickly information spreads from this node
**Best for:** Identifying efficient broadcasters
**Note:** Only meaningful in connected graphs

### 4. Eigenvector Centrality
**What it measures:** Connection to other important nodes
**Interpretation:** Influence through well-connected neighbors
**Best for:** Prestige and status analysis
**Related:** Basis for PageRank algorithm

### 5. PageRank
**What it measures:** Importance via random walk probability
**Interpretation:** Long-term influence, quality of connections
**Best for:** Web graphs, citation networks
**Advantage:** Works on directed graphs

### 6. Katz Centrality
**What it measures:** Weighted sum of all walks from node
**Interpretation:** Global reach with distance decay
**Best for:** Networks with distance-based influence
**Parameter:** Alpha controls distance decay rate

### 7. Harmonic Centrality
**What it measures:** Sum of inverse distances to all nodes
**Interpretation:** Similar to closeness but handles disconnected graphs
**Best for:** Disconnected or large networks
**Advantage:** More robust than closeness

## Best Practices

1. **Multiple Measures**
   - Always calculate multiple centrality measures
   - No single measure captures all aspects of importance
   - Compare and contrast different perspectives

2. **Normalization**
   - Use normalized scores for cross-network comparison
   - Understand normalization impact on interpretation
   - Report both normalized and raw scores when relevant

3. **Correlation Analysis**
   - Check correlations between measures
   - High correlation suggests redundancy
   - Low correlation reveals different aspects of importance

4. **Computational Efficiency**
   - For large networks (>10,000 nodes):
     - Use sampling for betweenness centrality
     - Skip expensive measures like current flow betweenness
     - Consider approximation algorithms

5. **Interpretation Guidelines**
   - Consider network context and domain
   - Degree centrality ≠ importance in all contexts
   - Combine quantitative scores with qualitative understanding

6. **Validation**
   - Verify top nodes make sense in domain context
   - Check for computational errors (negative values, NaN)
   - Compare with known important nodes if available

## Usage Example

```
NETWORK_DATA_SOURCE: "collaboration_network.csv"
NETWORK_TYPE: "Undirected, weighted by collaboration count"
CENTRALITY_MEASURES: "Degree, betweenness, closeness, eigenvector, PageRank"
PRIMARY_CENTRALITY_MEASURES: "Betweenness and eigenvector"
NODE_IMPORTANCE_GOALS: "Identify key researchers who bridge different research communities"
CENTRALITY_FOCUS: "Information Flow and Influence"
TOP_K_NODES: 20
ANALYZE_CORRELATIONS: True
ANALYZE_DISTRIBUTIONS: True
```
