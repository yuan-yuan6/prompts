---
title: Network Community Detection Algorithms
category: data-analytics/Research Analytics
tags: [data-analytics, network-analysis, community-detection, clustering, modularity]
use_cases:
  - Discovering groups and clusters in networks
  - Identifying densely connected communities
  - Analyzing modular network structure
  - Comparing different community detection algorithms
related_templates:
  - network-analysis-overview.md
  - network-visualization-basics.md
  - network-centrality-measures.md
  - applied-network-analytics.md
last_updated: 2025-11-09
---

# Network Community Detection Algorithms

## Purpose
Discover and analyze community structure in networks using multiple detection algorithms. Identify densely connected groups, evaluate community quality, detect hierarchical structures, and understand the modular organization of complex networks.

## Template

```
You are a community detection expert. Analyze the community structure of [NETWORK_DATA_SOURCE] using [COMMUNITY_ALGORITHMS] to identify [COMMUNITY_GOALS].

NETWORK CONTEXT:
- Network type: [NETWORK_TYPE]
- Scale: [NODE_COUNT] nodes, [EDGE_COUNT] edges
- Expected communities: [EXPECTED_NUM_COMMUNITIES] (if known)
- Domain: [NETWORK_DOMAIN]

COMMUNITY DETECTION OBJECTIVES:
- Detection methods: [COMMUNITY_ALGORITHMS]
- Quality metrics: [QUALITY_METRICS]
- Hierarchical analysis: [HIERARCHICAL_DETECTION]
- Comparison strategy: [COMPARISON_APPROACH]

### COMPREHENSIVE COMMUNITY DETECTION

```python
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict, Counter
import community as community_louvain
from networkx.algorithms import community
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

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
            leiden_partition = leidenalg.find_partition(
                ig_graph,
                leidenalg.ModularityVertexPartition
            )
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
            from sklearn.cluster import SpectralClustering
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
        ig_graph = ig.Graph(
            n=len(node_list),
            edges=edge_list,
            directed=G.is_directed()
        )

        return ig_graph

    def _spectral_clustering(self, G, n_clusters=8):
        """Apply spectral clustering"""
        from sklearn.cluster import SpectralClustering

        # Get adjacency matrix
        adj_matrix = nx.adjacency_matrix(G).toarray()

        # Apply spectral clustering
        spectral = SpectralClustering(
            n_clusters=n_clusters,
            affinity='precomputed',
            random_state=42
        )
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
        node_to_idx = {node: idx for idx, node in enumerate(G.nodes())}
        for u, v in G.edges():
            im.addLink(node_to_idx[u], node_to_idx[v])

        # Run algorithm
        im.run()

        # Extract communities
        idx_to_node = {idx: node for node, idx in node_to_idx.items()}
        communities = defaultdict(list)
        for node in im.tree:
            if node.isLeaf():
                communities[node.moduleIndex()].append(idx_to_node[node.physicalId])

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
                    external_edges = sum(
                        1 for node in comm
                        for neighbor in G.neighbors(node)
                        if neighbor not in comm
                    )
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

    def visualize_communities(self, method='best', figsize=(12, 8)):
        """Visualize network communities"""

        if method == 'best':
            comparison = self.compare_community_methods()
            method = comparison.index[0]

        G = self.network
        communities = self.communities[method]

        fig, ax = plt.subplots(figsize=figsize)

        pos = nx.spring_layout(G, k=1/np.sqrt(G.number_of_nodes()), iterations=50)

        # Color palette for communities
        colors = plt.cm.Set3(np.linspace(0, 1, len(communities)))

        # Draw each community with different color
        for i, comm in enumerate(communities):
            nx.draw_networkx_nodes(
                G, pos,
                nodelist=comm,
                node_color=[colors[i]],
                node_size=100,
                alpha=0.8,
                ax=ax,
                label=f'Community {i+1} (n={len(comm)})'
            )

        # Draw edges
        nx.draw_networkx_edges(
            G, pos,
            edge_color='gray',
            alpha=0.5,
            width=0.5,
            ax=ax
        )

        ax.set_title(f'Community Structure - {method.title()} Method\n' +
                    f'{len(communities)} communities detected')
        ax.axis('off')

        # Add legend if not too many communities
        if len(communities) <= 10:
            ax.legend(loc='upper left', fontsize=8)

        return fig

# Perform community detection
community_detector = CommunityDetector(network)

# Detect communities using multiple methods
detected_communities = community_detector.detect_communities_multiple_methods()

# Evaluate community quality
community_quality = community_detector.evaluate_community_quality()

# Compare methods
method_comparison = community_detector.compare_community_methods()
print("\n=== COMMUNITY DETECTION METHOD COMPARISON ===")
print(method_comparison[['modularity', 'num_communities', 'avg_community_size', 'overall_rank']])

# Analyze best method
community_structure = community_detector.analyze_community_structure(method='best')

# Hierarchical community detection
hierarchical_communities = community_detector.hierarchical_community_detection(max_levels=[MAX_HIERARCHY_LEVELS])

# Visualize communities
community_viz = community_detector.visualize_communities(method='best')
plt.show()
```

OUTPUT REQUIREMENTS:
Deliver comprehensive community detection analysis including:

1. **Community Detection Results**
   - Communities detected by each method
   - Number of communities found
   - Community size distributions
   - Method-specific parameters used

2. **Quality Evaluation**
   - Modularity scores (higher is better, range: -0.5 to 1.0)
   - Coverage (fraction of intra-community edges)
   - Performance (classification accuracy)
   - Conductance (community boundary strength)

3. **Method Comparison**
   - Ranking of methods by quality metrics
   - Agreement between different methods
   - Recommended method for this network
   - Justification for recommendation

4. **Community Structure Analysis**
   - Intra vs. inter-community edge distribution
   - Individual community characteristics
   - Central nodes within communities
   - External connectivity patterns

5. **Hierarchical Structure** (if applicable)
   - Multi-level community organization
   - Number of levels detected
   - Community nesting patterns
   - Hierarchical visualization

6. **Key Findings**
   - Main community characteristics
   - Network modularity interpretation
   - Domain-specific insights
   - Actionable recommendations
```

## Variables

### Network Context Variables
- [NETWORK_DATA_SOURCE] - Source of network data
- [NETWORK_TYPE] - Type of network (Directed/Undirected/Weighted)
- [NODE_COUNT] - Number of nodes
- [EDGE_COUNT] - Number of edges
- [NETWORK_DOMAIN] - Domain of the network
- [EXPECTED_NUM_COMMUNITIES] - Expected number of communities (if known)

### Algorithm Selection Variables
- [COMMUNITY_ALGORITHMS] - Which algorithms to use
- [COMMUNITY_GOALS] - Goals for community detection
- [NUM_COMMUNITIES] - Target number of communities (for spectral clustering)
- [HIERARCHICAL_DETECTION] - Perform hierarchical detection (True/False)
- [MAX_HIERARCHY_LEVELS] - Maximum hierarchy levels (default: 5)

### Quality Metrics Variables
- [QUALITY_METRICS] - Which quality metrics to calculate
- [COMPARISON_APPROACH] - How to compare methods
- [MODULARITY_THRESHOLD] - Minimum acceptable modularity
- [MIN_COMMUNITY_SIZE] - Minimum community size
- [MAX_COMMUNITY_SIZE] - Maximum community size

## Understanding Community Detection Algorithms

### 1. Louvain Algorithm
**Approach:** Greedy modularity optimization
**Speed:** Fast (suitable for large networks)
**Advantages:** Good quality, widely used, deterministic
**Disadvantages:** Resolution limit, may miss small communities
**Best for:** General-purpose community detection

### 2. Leiden Algorithm
**Approach:** Improved Louvain with guaranteed well-connected communities
**Speed:** Fast
**Advantages:** Better quality than Louvain, no resolution limit issues
**Disadvantages:** Requires additional library (leidenalg)
**Best for:** High-quality community detection

### 3. Girvan-Newman
**Approach:** Progressive edge removal based on betweenness
**Speed:** Slow (O(m²n) or O(n³))
**Advantages:** Hierarchical structure, interpretable
**Disadvantages:** Computationally expensive
**Best for:** Small networks, hierarchical analysis

### 4. Label Propagation
**Approach:** Iterative label spreading
**Speed:** Very fast
**Advantages:** Simple, scalable, no parameters
**Disadvantages:** Non-deterministic, quality varies
**Best for:** Large networks, quick exploration

### 5. Greedy Modularity
**Approach:** Bottom-up agglomerative clustering
**Speed:** Fast
**Advantages:** Good for large networks
**Disadvantages:** Greedy approach may not find global optimum
**Best for:** Large-scale networks

### 6. Spectral Clustering
**Approach:** Eigenvalue decomposition of graph Laplacian
**Speed:** Moderate
**Advantages:** Well-founded mathematically
**Disadvantages:** Requires specifying number of clusters
**Best for:** When number of communities is known

### 7. Infomap
**Approach:** Information-theoretic compression
**Speed:** Fast
**Advantages:** Hierarchical, handles directed networks well
**Disadvantages:** Requires additional library
**Best for:** Flow-based networks, directed graphs

## Quality Metrics Explained

### Modularity
- **Range:** -0.5 to 1.0
- **Interpretation:**
  - > 0.3: Significant community structure
  - 0.3-0.7: Strong communities
  - > 0.7: Very strong (rare in real networks)
- **Formula:** Q = (fraction of edges within communities) - (expected fraction in random network)

### Coverage
- **Range:** 0 to 1
- **Interpretation:** Fraction of edges that fall within communities
- **Higher is better:** More intra-community connections

### Performance
- **Range:** 0 to 1
- **Interpretation:** Fraction of correctly classified node pairs
- **Higher is better:** More accurate community assignment

### Conductance
- **Range:** 0 to 1
- **Interpretation:** Ratio of edges leaving community to total edges
- **Lower is better:** Strong community boundaries

## Best Practices

1. **Use Multiple Methods**
   - Different algorithms capture different aspects
   - Consensus across methods = robust communities
   - Compare results systematically

2. **Validate Results**
   - Check if communities make sense in domain context
   - Examine community size distribution
   - Verify modularity is significant (> 0.3)

3. **Consider Network Characteristics**
   - Large networks: Use Louvain, Leiden, or Label Propagation
   - Small networks: Can use Girvan-Newman
   - Directed networks: Consider Infomap
   - Weighted networks: Most methods support weights

4. **Hierarchical Analysis**
   - Real networks often have nested structure
   - Multi-level analysis reveals organization at different scales
   - Compare hierarchical levels

5. **Interpretation**
   - Communities should align with domain knowledge
   - Examine inter-community connections
   - Identify bridge nodes between communities

## Usage Example

```
NETWORK_DATA_SOURCE: "protein_interaction_network.csv"
NETWORK_TYPE: "Undirected, weighted by interaction confidence"
COMMUNITY_ALGORITHMS: "Louvain, Leiden, Label Propagation, Infomap"
COMMUNITY_GOALS: "Identify functional modules and protein complexes"
QUALITY_METRICS: "Modularity, coverage, conductance"
HIERARCHICAL_DETECTION: True
MAX_HIERARCHY_LEVELS: 3
COMPARISON_APPROACH: "Rank by modularity and biological relevance"
```
