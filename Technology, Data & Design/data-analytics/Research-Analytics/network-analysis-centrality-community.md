---
title: Network Analysis - Centrality and Community Detection
category: data-analytics
tags:
- data-analytics
- ai-ml
use_cases:
- Identifying influential nodes using multiple centrality measures
- Detecting communities and clusters in networks
- Analyzing community structure and quality
- Comparing different community detection algorithms
related_templates:
- data-analytics/Research-Analytics/network-analysis-data-preparation.md
- data-analytics/Research-Analytics/network-analysis-paths-temporal.md
- data-analytics/Research-Analytics/network-analysis-visualization.md
- data-analytics/Research-Analytics/network-analysis-overview.md
last_updated: 2025-11-10
industries:
- technology
type: template
difficulty: intermediate
slug: network-analysis-centrality-community
---

# Network Analysis - Centrality and Community Detection

## Purpose
Identify important nodes and detect community structures in networks using multiple centrality measures and community detection algorithms. This module provides comprehensive tools for centrality analysis, community detection, and structural pattern recognition.

## Quick Centrality Prompt
Analyze [network name] with [X nodes, Y edges]. Calculate centrality measures (degree, betweenness, closeness, PageRank, eigenvector), identify top 20 influential nodes, detect communities using Louvain algorithm, evaluate community quality (modularity), and characterize each community by size and key members. Visualize network colored by community with node size by centrality.

## Quick Start

**Example: Identify Influencers and Communities in Social Network**

```
You are a network analysis expert. Analyze a social media network to identify key influencers and detect community structure.

NETWORK OVERVIEW:
- Network: Social media follower network
- Nodes: 10,000 users
- Edges: 45,000 connections
- Type: Directed, weighted by interaction frequency

CENTRALITY ANALYSIS OBJECTIVES:
1. Calculate multiple centrality measures:
   - Degree centrality (raw influence)
   - Betweenness centrality (bridge influencers)
   - Closeness centrality (information reach)
   - PageRank (algorithmic influence)
   - Eigenvector centrality (influence among influential)

2. Identify top 20 most influential nodes across all measures
3. Analyze correlation between different centrality measures
4. Test for power-law distribution in centrality scores

COMMUNITY DETECTION OBJECTIVES:
1. Apply multiple community detection algorithms:
   - Louvain (modularity optimization)
   - Label propagation (fast detection)
   - Greedy modularity (hierarchical)

2. Evaluate community quality:
   - Calculate modularity scores (target: > 0.4)
   - Measure coverage and performance
   - Analyze community size distribution

3. Identify bridge nodes connecting communities
4. Analyze internal community structure

EXPECTED OUTPUT:
- Top 20 influencers with centrality scores for all measures
- Centrality correlation matrix with statistical significance
- Community assignments with quality metrics
- Community structure analysis with size distribution
- Bridge nodes connecting different communities
```

## Template

```
You are a network analysis expert. Analyze the centrality and community structure of [NETWORK_DATA_SOURCE].

CENTRALITY ANALYSIS REQUIREMENTS:
Centrality Measures to Calculate:
- Degree centrality: [CALCULATE_DEGREE]
- Betweenness centrality: [CALCULATE_BETWEENNESS]
- Closeness centrality: [CALCULATE_CLOSENESS]
- Eigenvector centrality: [CALCULATE_EIGENVECTOR]
- PageRank: [CALCULATE_PAGERANK]
- Katz centrality: [CALCULATE_KATZ]
- Harmonic centrality: [CALCULATE_HARMONIC]

Analysis Parameters:
- Normalization: [CENTRALITY_NORMALIZATION]
- Top K nodes: [TOP_K_NODES]
- Correlation threshold: [CENTRALITY_CORRELATION_THRESHOLD]
- Power law testing: [TEST_POWER_LAW]

COMMUNITY DETECTION REQUIREMENTS:
Algorithms to Apply:
- Louvain: [USE_LOUVAIN]
- Leiden: [USE_LEIDEN]
- Girvan-Newman: [USE_GIRVAN_NEWMAN]
- Label propagation: [USE_LABEL_PROPAGATION]
- Greedy modularity: [USE_GREEDY_MODULARITY]
- Spectral clustering: [USE_SPECTRAL]

Detection Parameters:
- Target communities: [NUM_COMMUNITIES]
- Resolution parameter: [RESOLUTION_PARAMETER]
- Min community size: [MIN_COMMUNITY_SIZE]
- Quality metric: [COMMUNITY_QUALITY_METRIC]

EVALUATION REQUIREMENTS:
- Compare centrality measures
- Evaluate community quality
- Identify structural patterns
- Analyze community hierarchy
```

## Centrality Analysis

### CentralityAnalyzer Class

```python
import networkx as nx
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, skew, kurtosis

class CentralityAnalyzer:
    def __init__(self, network):
        self.network = network
        self.centrality_scores = {}

    def calculate_all_centralities(self, normalized=True):
        """Calculate all major centrality measures"""

        G = self.network
        centralities = {}

        print("Calculating centrality measures...")

        # Degree Centrality
        print("  - Degree centrality")
        centralities['degree'] = nx.degree_centrality(G)

        # Betweenness Centrality
        print("  - Betweenness centrality")
        centralities['betweenness'] = nx.betweenness_centrality(
            G, normalized=normalized, k=min(100, G.number_of_nodes())
        )

        # Closeness Centrality
        print("  - Closeness centrality")
        if nx.is_connected(G) or nx.is_directed(G):
            centralities['closeness'] = nx.closeness_centrality(G, distance=None)
        else:
            centralities['closeness'] = {}
            for component in nx.connected_components(G):
                subG = G.subgraph(component)
                closeness_sub = nx.closeness_centrality(subG)
                centralities['closeness'].update(closeness_sub)

        # Eigenvector Centrality
        print("  - Eigenvector centrality")
        try:
            centralities['eigenvector'] = nx.eigenvector_centrality(G, max_iter=1000)
        except nx.NetworkXError:
            print("    Warning: Eigenvector centrality failed, using PageRank instead")
            centralities['eigenvector'] = nx.pagerank(G)

        # PageRank
        print("  - PageRank")
        centralities['pagerank'] = nx.pagerank(G, alpha=0.85, max_iter=1000)

        # Katz Centrality
        print("  - Katz centrality")
        try:
            alpha = 1 / (max(dict(G.degree()).values()) + 1)
            centralities['katz'] = nx.katz_centrality(G, alpha=alpha, max_iter=1000)
        except (nx.NetworkXError, ZeroDivisionError):
            print("    Warning: Katz centrality calculation failed")
            centralities['katz'] = {node: 0 for node in G.nodes()}

        # Harmonic Centrality
        print("  - Harmonic centrality")
        centralities['harmonic'] = nx.harmonic_centrality(G, distance=None)

        # Load Centrality (for weighted networks)
        if nx.is_weighted(G):
            print("  - Load centrality")
            centralities['load'] = nx.load_centrality(G, weight='weight')

        # Current Flow Betweenness Centrality (for connected networks)
        if nx.is_connected(G) and G.number_of_nodes() < 500:  # Computationally expensive
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
        p_values = pd.DataFrame(index=correlation_matrix.index, columns=correlation_matrix.columns)

        for i in correlation_matrix.index:
            for j in correlation_matrix.columns:
                if i != j:
                    corr, p_val = pearsonr(centrality_df[i], centrality_df[j])
                    p_values.loc[i, j] = p_val
                else:
                    p_values.loc[i, j] = 0.0

        return {
            'correlation_matrix': correlation_matrix,
            'p_values': p_values,
            'significant_correlations': correlation_matrix[(correlation_matrix.abs() > 0.5) & (p_values < 0.05)]
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
                'skewness': self._calculate_skewness(values),
                'kurtosis': self._calculate_kurtosis(values)
            }

            # Distribution shape analysis
            stats['is_power_law'] = self._test_power_law_distribution(values)
            stats['concentration_ratio'] = self._calculate_concentration_ratio(values)

            analysis[measure] = stats

        return analysis

    def _calculate_skewness(self, values):
        """Calculate skewness of distribution"""
        return skew(values)

    def _calculate_kurtosis(self, values):
        """Calculate kurtosis of distribution"""
        return kurtosis(values)

    def _test_power_law_distribution(self, values):
        """Test if distribution follows power law"""
        # Simple test - more sophisticated methods exist
        log_values = np.log([v + 1e-10 for v in values if v > 0])
        if len(log_values) < 10:
            return False

        # Linear regression on log-log scale
        ranks = np.log(np.arange(1, len(log_values) + 1))
        sorted_log_values = np.sort(log_values)[::-1]

        correlation = np.corrcoef(ranks, sorted_log_values)[0, 1]
        return correlation < -0.8  # Strong negative correlation indicates power law

    def _calculate_concentration_ratio(self, values):
        """Calculate concentration ratio (e.g., top 10% vs. rest)"""
        sorted_values = sorted(values, reverse=True)
        top_10_percent = int(len(sorted_values) * 0.1)
        top_10_sum = sum(sorted_values[:top_10_percent])
        total_sum = sum(sorted_values)
        return top_10_sum / total_sum if total_sum > 0 else 0

# Perform centrality analysis
centrality_analyzer = CentralityAnalyzer(network)
centrality_results = centrality_analyzer.calculate_all_centralities()
centrality_correlations = centrality_analyzer.analyze_centrality_correlations()
top_nodes_degree = centrality_analyzer.identify_top_nodes('degree', [TOP_K_NODES])
centrality_distributions = centrality_analyzer.centrality_distribution_analysis()
```

## Community Detection

### CommunityDetector Class

```python
import community as community_louvain
from networkx.algorithms import community
from sklearn.cluster import SpectralClustering
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from collections import defaultdict

class CommunityDetector:
    def __init__(self, network):
        self.network = network
        self.communities = {}
        self.community_metrics = {}

    def detect_communities_multiple_methods(self):
        """Apply multiple community detection algorithms"""

        G = self.network
        methods = {}

        print("Detecting communities using multiple methods...")

        # 1. Louvain Algorithm
        print("  - Louvain algorithm")
        try:
            louvain_communities = community_louvain.best_partition(G)
            methods['louvain'] = self._partition_to_communities(louvain_communities)
        except Exception as e:
            print(f"    Error in Louvain: {e}")
            methods['louvain'] = []

        # 2. Leiden Algorithm (if available)
        try:
            import leidenalg
            import igraph as ig

            print("  - Leiden algorithm")
            # Convert to igraph
            ig_graph = self._networkx_to_igraph(G)
            leiden_partition = leidenalg.find_partition(ig_graph, leidenalg.ModularityVertexPartition)
            methods['leiden'] = [list(community) for community in leiden_partition]
        except ImportError:
            print("    Leiden algorithm not available (install leidenalg)")
        except Exception as e:
            print(f"    Error in Leiden: {e}")

        # 3. Girvan-Newman Algorithm
        print("  - Girvan-Newman algorithm")
        if G.number_of_nodes() < 1000:  # Computationally expensive
            try:
                gn_communities = community.girvan_newman(G)
                # Take the partition with highest modularity
                best_partition = None
                best_modularity = -1

                for i, partition in enumerate(gn_communities):
                    if i > 10:  # Limit iterations
                        break
                    mod = community.modularity(G, partition)
                    if mod > best_modularity:
                        best_modularity = mod
                        best_partition = partition

                methods['girvan_newman'] = list(best_partition) if best_partition else []
            except Exception as e:
                print(f"    Error in Girvan-Newman: {e}")
        else:
            print("    Skipping Girvan-Newman (too many nodes)")

        # 4. Label Propagation
        print("  - Label propagation")
        try:
            lp_communities = community.label_propagation_communities(G)
            methods['label_propagation'] = [list(comm) for comm in lp_communities]
        except Exception as e:
            print(f"    Error in Label Propagation: {e}")

        # 5. Greedy Modularity Maximization
        print("  - Greedy modularity maximization")
        try:
            greedy_communities = community.greedy_modularity_communities(G)
            methods['greedy_modularity'] = [list(comm) for comm in greedy_communities]
        except Exception as e:
            print(f"    Error in Greedy Modularity: {e}")

        # 6. Spectral Clustering
        print("  - Spectral clustering")
        try:
            methods['spectral'] = self._spectral_clustering(G, n_clusters=[NUM_COMMUNITIES])
        except Exception as e:
            print(f"    Error in Spectral Clustering: {e}")

        # 7. Infomap (if available)
        try:
            import infomap
            print("  - Infomap")
            methods['infomap'] = self._infomap_communities(G)
        except ImportError:
            print("    Infomap not available")
        except Exception as e:
            print(f"    Error in Infomap: {e}")

        self.communities = methods
        return methods

    def _partition_to_communities(self, partition):
        """Convert node-community partition to list of communities"""
        communities = defaultdict(list)
        for node, comm_id in partition.items():
            communities[comm_id].append(node)
        return list(communities.values())

    def _networkx_to_igraph(self, G):
        """Convert NetworkX graph to igraph"""
        import igraph as ig

        # Create vertex mapping
        node_list = list(G.nodes())
        node_to_idx = {node: i for i, node in enumerate(node_list)}

        # Create edge list with indices
        edge_list = [(node_to_idx[u], node_to_idx[v]) for u, v in G.edges()]

        # Create igraph
        ig_graph = ig.Graph(n=len(node_list), edges=edge_list, directed=G.is_directed())

        return ig_graph

    def _spectral_clustering(self, G, n_clusters=8):
        """Apply spectral clustering"""
        # Get adjacency matrix
        adj_matrix = nx.adjacency_matrix(G).toarray()

        # Apply spectral clustering
        spectral = SpectralClustering(n_clusters=n_clusters, affinity='precomputed', random_state=42)
        cluster_labels = spectral.fit_predict(adj_matrix)

        # Convert to communities
        communities = defaultdict(list)
        for node, label in zip(G.nodes(), cluster_labels):
            communities[label].append(node)

        return list(communities.values())

    def _infomap_communities(self, G):
        """Apply Infomap algorithm"""
        import infomap

        # Create Infomap instance
        im = infomap.Infomap()

        # Add links
        for u, v in G.edges():
            im.addLink(u, v)

        # Run algorithm
        im.run()

        # Extract communities
        communities = defaultdict(list)
        for node in im.tree:
            if node.isLeaf():
                communities[node.moduleIndex()].append(node.physicalId)

        return list(communities.values())

    def evaluate_community_quality(self):
        """Evaluate quality of detected communities"""

        G = self.network
        evaluation_results = {}

        for method, communities in self.communities.items():
            if not communities:
                continue

            print(f"Evaluating {method} communities...")

            # Modularity
            modularity = community.modularity(G, communities)

            # Coverage (fraction of edges within communities)
            coverage = community.coverage(G, communities)

            # Performance (fraction of correctly classified node pairs)
            performance = community.performance(G, communities)

            # Number of communities
            num_communities = len(communities)

            # Community sizes
            community_sizes = [len(comm) for comm in communities]

            # Conductance (for each community)
            conductances = []
            for comm in communities:
                if len(comm) > 1:
                    subG = G.subgraph(comm)
                    internal_edges = subG.number_of_edges()
                    external_edges = sum(1 for node in comm for neighbor in G.neighbors(node)
                                       if neighbor not in comm)
                    total_edges = internal_edges + external_edges
                    conductance = external_edges / total_edges if total_edges > 0 else 0
                    conductances.append(conductance)

            evaluation_results[method] = {
                'modularity': modularity,
                'coverage': coverage,
                'performance': performance,
                'num_communities': num_communities,
                'avg_community_size': np.mean(community_sizes),
                'median_community_size': np.median(community_sizes),
                'largest_community_size': max(community_sizes),
                'smallest_community_size': min(community_sizes),
                'avg_conductance': np.mean(conductances) if conductances else None,
                'community_size_distribution': community_sizes
            }

        self.community_metrics = evaluation_results
        return evaluation_results

    def compare_community_methods(self):
        """Compare different community detection methods"""

        if not self.community_metrics:
            self.evaluate_community_quality()

        comparison = pd.DataFrame(self.community_metrics).T

        # Rank methods by modularity
        comparison['modularity_rank'] = comparison['modularity'].rank(ascending=False)

        # Rank methods by performance
        comparison['performance_rank'] = comparison['performance'].rank(ascending=False)

        # Combined score (you can adjust weights)
        comparison['combined_score'] = (
            0.4 * comparison['modularity_rank'] +
            0.3 * comparison['performance_rank'] +
            0.3 * comparison['coverage'].rank(ascending=False)
        )

        comparison['overall_rank'] = comparison['combined_score'].rank(ascending=True)

        return comparison.sort_values('overall_rank')

    def analyze_community_structure(self, method='best'):
        """Analyze structure of detected communities"""

        if method == 'best':
            # Select best method based on evaluation
            comparison = self.compare_community_methods()
            method = comparison.index[0]

        if method not in self.communities:
            raise ValueError(f"Method {method} not found in detected communities")

        G = self.network
        communities = self.communities[method]

        structure_analysis = {}

        # Inter-community connections
        inter_community_edges = 0
        intra_community_edges = 0

        community_map = {}
        for i, comm in enumerate(communities):
            for node in comm:
                community_map[node] = i

        for u, v in G.edges():
            if community_map.get(u) == community_map.get(v):
                intra_community_edges += 1
            else:
                inter_community_edges += 1

        structure_analysis['edge_distribution'] = {
            'intra_community_edges': intra_community_edges,
            'inter_community_edges': inter_community_edges,
            'intra_community_ratio': intra_community_edges / G.number_of_edges()
        }

        # Community-specific analysis
        community_details = []
        for i, comm in enumerate(communities):
            subG = G.subgraph(comm)

            # Internal structure
            internal_density = nx.density(subG)

            # Centrality within community
            if len(comm) > 1:
                internal_centrality = nx.degree_centrality(subG)
                central_node = max(internal_centrality.items(), key=lambda x: x[1])
            else:
                central_node = (list(comm)[0], 1.0)

            # External connections
            external_connections = 0
            for node in comm:
                external_connections += len([n for n in G.neighbors(node) if n not in comm])

            community_details.append({
                'community_id': i,
                'size': len(comm),
                'internal_density': internal_density,
                'external_connections': external_connections,
                'central_node': central_node[0],
                'central_node_centrality': central_node[1],
                'avg_external_degree': external_connections / len(comm) if len(comm) > 0 else 0
            })

        structure_analysis['community_details'] = pd.DataFrame(community_details)
        structure_analysis['method_used'] = method

        return structure_analysis

    def hierarchical_community_detection(self, max_levels=5):
        """Detect hierarchical community structure"""

        G = self.network
        hierarchical_communities = []

        # Start with the full network
        current_level_graphs = [G]
        level = 0

        while current_level_graphs and level < max_levels:
            print(f"Detecting communities at level {level}")

            next_level_graphs = []
            level_communities = []

            for graph in current_level_graphs:
                if graph.number_of_nodes() < 10:  # Stop if too small
                    continue

                # Detect communities in current graph
                partition = community_louvain.best_partition(graph)
                communities = self._partition_to_communities(partition)

                level_communities.extend(communities)

                # Create subgraphs for next level
                for comm in communities:
                    if len(comm) > 5:  # Only proceed if community is large enough
                        subG = graph.subgraph(comm).copy()
                        next_level_graphs.append(subG)

            hierarchical_communities.append(level_communities)
            current_level_graphs = next_level_graphs
            level += 1

        return hierarchical_communities

# Perform community detection
community_detector = CommunityDetector(network)
detected_communities = community_detector.detect_communities_multiple_methods()
community_quality = community_detector.evaluate_community_quality()
method_comparison = community_detector.compare_community_methods()
community_structure = community_detector.analyze_community_structure()
hierarchical_communities = community_detector.hierarchical_community_detection()
```

## Variables

### Centrality Variables
- [CALCULATE_DEGREE] - Calculate degree centrality
- [CALCULATE_BETWEENNESS] - Calculate betweenness centrality
- [CALCULATE_CLOSENESS] - Calculate closeness centrality
- [CALCULATE_EIGENVECTOR] - Calculate eigenvector centrality
- [CALCULATE_PAGERANK] - Calculate PageRank
- [CALCULATE_KATZ] - Calculate Katz centrality
- [CALCULATE_HARMONIC] - Calculate harmonic centrality
- [CENTRALITY_NORMALIZATION] - Normalize centrality scores
- [TOP_K_NODES] - Number of top nodes to identify
- [CENTRALITY_CORRELATION_THRESHOLD] - Threshold for significant correlations
- [TEST_POWER_LAW] - Test for power-law distribution
- [PAGERANK_ALPHA] - Alpha parameter for PageRank (default: 0.85)
- [KATZ_ALPHA] - Alpha parameter for Katz centrality
- [CONCENTRATION_RATIO_PERCENT] - Percentage for concentration ratio (default: 10%)

### Community Detection Variables
- [USE_LOUVAIN] - Use Louvain algorithm
- [USE_LEIDEN] - Use Leiden algorithm
- [USE_GIRVAN_NEWMAN] - Use Girvan-Newman algorithm
- [USE_LABEL_PROPAGATION] - Use label propagation
- [USE_GREEDY_MODULARITY] - Use greedy modularity
- [USE_SPECTRAL] - Use spectral clustering
- [USE_INFOMAP] - Use Infomap algorithm
- [NUM_COMMUNITIES] - Target number of communities
- [RESOLUTION_PARAMETER] - Resolution parameter for modularity
- [MIN_COMMUNITY_SIZE] - Minimum community size threshold
- [MAX_COMMUNITY_SIZE] - Maximum community size threshold
- [COMMUNITY_QUALITY_METRIC] - Metric for evaluating quality
- [MODULARITY_THRESHOLD] - Threshold for acceptable modularity
- [HIERARCHICAL_LEVELS] - Number of hierarchical levels to detect

## Usage Examples

### Example 1: Comprehensive Centrality Analysis
```
CALCULATE_DEGREE: True
CALCULATE_BETWEENNESS: True
CALCULATE_CLOSENESS: True
CALCULATE_EIGENVECTOR: True
CALCULATE_PAGERANK: True
CENTRALITY_NORMALIZATION: True
TOP_K_NODES: 20
CENTRALITY_CORRELATION_THRESHOLD: 0.5
TEST_POWER_LAW: True
```

### Example 2: Multi-Method Community Detection
```
USE_LOUVAIN: True
USE_LABEL_PROPAGATION: True
USE_GREEDY_MODULARITY: True
MIN_COMMUNITY_SIZE: 5
MODULARITY_THRESHOLD: 0.4
COMMUNITY_QUALITY_METRIC: "modularity"
```

### Example 3: Hierarchical Community Structure
```
USE_LOUVAIN: True
HIERARCHICAL_LEVELS: 3
MIN_COMMUNITY_SIZE: 10
RESOLUTION_PARAMETER: 1.0
```

## Best Practices

1. **Use Multiple Centrality Measures** - Different measures capture different aspects of importance
2. **Normalize Scores** - Normalize centrality scores for fair comparison across networks
3. **Test Statistical Significance** - Use correlation testing to validate relationships
4. **Apply Multiple Algorithms** - Compare results from different community detection methods
5. **Evaluate Quality** - Always assess community quality using modularity and other metrics
6. **Consider Network Type** - Choose appropriate algorithms for directed vs. undirected networks
7. **Handle Disconnected Networks** - Process each component separately for some centrality measures
8. **Computational Awareness** - Use sampling for expensive algorithms on large networks
9. **Validate Results** - Cross-validate community assignments using multiple methods
10. **Interpret Contextually** - Consider domain knowledge when interpreting centrality and communities
