---
title: Network Community Detection Template
category: data-analytics/Research Analytics
tags: ['data-analytics', 'network-analysis', 'community-detection', 'clustering']
use_cases:
  - Detect and analyze communities in networks using modularity optimization, hierarchical clustering, label propagation, and Louvain algorithm to identify network structures.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Network Community Detection Template

## Purpose
Detect and analyze communities in networks using modularity optimization, hierarchical clustering, label propagation, and Louvain algorithm to identify network structures.

## Quick Start

### For Data Scientists

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific detect needs
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine as needed

**Common Use Cases:**
- Detect and analyze communities in networks using modularity optimization, hierarchical clustering, label propagation, and Louvain algorithm to identify network structures.
- Project-specific implementations
- Research and analysis workflows



## Template

2. Detect communities/clusters of related influencers

   - Apply Louvain algorithm for community detection

   - Calculate modularity score (target: > 0.4 for good community structure)

   - Identify community themes based on content categories

   - Calculate network density and clustering coefficient

   - Identify optimal collaboration pairs (cross-community bridges)

- Community analysis report: Number of communities, sizes, themes, interconnections

- Network metrics dashboard: Density, clustering coefficient, avg path length, diameter

- Community detection: [COMMUNITY_ANALYSIS]

### Data Loading and Preprocessing
```python
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict, Counter
import community as community_louvain
from networkx.algorithms import community
import plotly.graph_objects as go
import plotly.express as px
from scipy import sparse
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

class NetworkPreprocessor:
    def __init__(self):
        self.networks = {}
        self.node_attributes = {}
        self.edge_attributes = {}
        self.metadata = {}

    def load_network_data(self, data_source, data_type='edge_list'):
        """Load network data from various formats"""

        if data_type == 'edge_list':
            # Load from edge list (CSV, TSV, etc.)
            edges_df = pd.read_csv(data_source)

            # Create network
            G = nx.from_pandas_edgelist(
                edges_df,
                source='[SOURCE_COLUMN]',
                target='[TARGET_COLUMN]',
                edge_attr=[EDGE_ATTRIBUTES] if '[EDGE_ATTRIBUTES]' else None,
                create_using=nx.DiGraph() if '[DIRECTED]' else nx.Graph()
            )

        elif data_type == 'adjacency_matrix':
            # Load adjacency matrix
            adj_matrix = pd.read_csv(data_source, index_col=0)
            G = nx.from_pandas_adjacency(adj_matrix, create_using=nx.DiGraph() if '[DIRECTED]' else nx.Graph())

        elif data_type == 'graphml':
            # Load GraphML format
            G = nx.read_graphml(data_source)

        elif data_type == 'gml':
            # Load GML format
            G = nx.read_gml(data_source)

        elif data_type == 'json':
            # Load from JSON
            import json
            with open(data_source, 'r') as f:
                data = json.load(f)
            G = nx.node_link_graph(data)

        # Store network
        self.networks['main'] = G

        # Extract metadata
        self.metadata['main'] = {
            'num_nodes': G.number_of_nodes(),
            'num_edges': G.number_of_edges(),
            'is_directed': nx.is_directed(G),
            'is_weighted': nx.is_weighted(G),
            'is_connected': nx.is_connected(G) if not nx.is_directed(G) else nx.is_weakly_connected(G),
            'node_attributes': list(G.nodes(data=True)[0][1].keys()) if G.nodes() else [],
            'edge_attributes': list(G.edges(data=True)[0][2].keys()) if G.edges() else []
        }

        return G

    def clean_network(self, remove_self_loops=True, remove_isolated=False,
                     min_degree=None, max_degree=None):
        """Clean and preprocess network"""

        G = self.networks['main'].copy()
        cleaning_log = []

        # Remove self loops
        if remove_self_loops:
            num_self_loops = nx.number_of_selfloops(G)
            G.remove_edges_from(nx.selfloop_edges(G))
            cleaning_log.append(f"Removed [NUM_SELF_LOOPS] self loops")

        # Remove isolated nodes
        if remove_isolated:
            isolated_nodes = list(nx.isolates(G))
            G.remove_nodes_from(isolated_nodes)
            cleaning_log.append(f"Removed {len(isolated_nodes)} isolated nodes")

        # Filter by degree
        if min_degree is not None or max_degree is not None:
            nodes_to_remove = []
            for node, degree in dict(G.degree()).items():
                if min_degree is not None and degree < min_degree:
                    nodes_to_remove.append(node)
                elif max_degree is not None and degree > max_degree:
                    nodes_to_remove.append(node)

            G.remove_nodes_from(nodes_to_remove)
            cleaning_log.append(f"Removed {len(nodes_to_remove)} nodes based on degree filter")

        # Store cleaned network
        self.networks['cleaned'] = G

        return G, cleaning_log

    def create_subnetworks(self, method='connected_components', **kwargs):
        """Extract subnetworks based on various criteria"""

        G = self.networks.get('cleaned', self.networks['main'])
        subnetworks = {}

        if method == 'connected_components':
            # Extract connected components
            if nx.is_directed(G):
                components = list(nx.weakly_connected_components(G))
            else:
                components = list(nx.connected_components(G))

            for i, component in enumerate(components):
                if len(component) >= kwargs.get('min_size', 3):
                    subG = G.subgraph(component).copy()
                    subnetworks[f'component_[I]'] = subG

        elif method == 'k_core':
            # Extract k-core
            k = kwargs.get('k', 2)
            k_core = nx.k_core(G, k=k)
            subnetworks['k_core'] = k_core

        elif method == 'ego_networks':
            # Extract ego networks for specified nodes
            nodes = kwargs.get('nodes', list(G.nodes())[:10])
            radius = kwargs.get('radius', 1)

            for node in nodes:
                if node in G:
                    ego_G = nx.ego_graph(G, node, radius=radius)
                    subnetworks[f'ego_[NODE]'] = ego_G

        elif method == 'attribute_based':
            # Extract subnetworks based on node attributes
            attribute = kwargs.get('attribute')
            values = kwargs.get('values')

            if attribute and values:
                for value in values:
                    nodes = [n for n, d in G.nodes(data=True) if d.get(attribute) == value]
                    if len(nodes) >= kwargs.get('min_size', 3):
                        subG = G.subgraph(nodes).copy()
                        subnetworks[f'[ATTRIBUTE]_[VALUE]'] = subG

        self.networks.update(subnetworks)
        return subnetworks

    def add_node_attributes(self, attribute_data, attribute_name):
        """Add attributes to network nodes"""

        G = self.networks.get('cleaned', self.networks['main'])

        # Add attributes from dictionary or dataframe
        if isinstance(attribute_data, dict):
            nx.set_node_attributes(G, attribute_data, attribute_name)
        elif isinstance(attribute_data, pd.DataFrame):
            attr_dict = attribute_data.set_index(attribute_data.columns[0])[attribute_name].to_dict()
            nx.set_node_attributes(G, attr_dict, attribute_name)

        # Update metadata
        if attribute_name not in self.metadata['main']['node_attributes']:
            self.metadata['main']['node_attributes'].append(attribute_name)

    def temporal_network_preprocessing(self, timestamp_column):
        """Preprocess temporal/dynamic networks"""

        G = self.networks['main']

        # Extract temporal information
        edge_times = {}
        for u, v, data in G.edges(data=True):
            if timestamp_column in data:
                edge_times[(u, v)] = data[timestamp_column]

        # Sort edges by timestamp
        sorted_edges = sorted(edge_times.items(), key=lambda x: x[1])

        # Create temporal snapshots
        time_windows = self._create_time_windows(sorted_edges, window_size='[TIME_WINDOW]')

        temporal_networks = {}
        for i, (start_time, end_time, edges) in enumerate(time_windows):
            temp_G = nx.Graph() if not nx.is_directed(G) else nx.DiGraph()
            temp_G.add_edges_from([edge[0] for edge in edges])
            temporal_networks[f'time_[I]'] = temp_G

        self.networks.update(temporal_networks)
        return temporal_networks

    def _create_time_windows(self, sorted_edges, window_size):
        """Create time windows for temporal analysis"""
        # Implementation for creating time windows
        # This would depend on the specific temporal analysis requirements
        pass


COMMUNITY DETECTION:

Advanced Community Detection Methods:
```python
import community as community_louvain
from networkx.algorithms import community
from sklearn.cluster import SpectralClustering, KMeans
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, modularity_score

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
            print(f"    Error in Louvain: [E]")
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
            print(f"    Error in Leiden: [E]")

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
                print(f"    Error in Girvan-Newman: [E]")
        else:
            print("    Skipping Girvan-Newman (too many nodes)")

        # 4. Label Propagation
        print("  - Label propagation")
        try:
            lp_communities = community.label_propagation_communities(G)
            methods['label_propagation'] = [list(comm) for comm in lp_communities]
        except Exception as e:
            print(f"    Error in Label Propagation: [E]")

        # 5. Greedy Modularity Maximization
        print("  - Greedy modularity maximization")
        try:
            greedy_communities = community.greedy_modularity_communities(G)
            methods['greedy_modularity'] = [list(comm) for comm in greedy_communities]
        except Exception as e:
            print(f"    Error in Greedy Modularity: [E]")

        # 6. Spectral Clustering
        print("  - Spectral clustering")
        try:
            methods['spectral'] = self._spectral_clustering(G, n_clusters=[NUM_COMMUNITIES])
        except Exception as e:
            print(f"    Error in Spectral Clustering: [E]")

        # 7. Infomap (if available)
        try:
            import infomap
            print("  - Infomap")
            methods['infomap'] = self._infomap_communities(G)
        except ImportError:
            print("    Infomap not available")
        except Exception as e:
            print(f"    Error in Infomap: [E]")

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

            print(f"Evaluating [METHOD] communities...")

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
            raise ValueError(f"Method [METHOD] not found in detected communities")

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
            print(f"Detecting communities at level [LEVEL]")

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

Dynamic Network Analysis:
```python
class TemporalNetworkAnalyzer:
    def __init__(self, networks_sequence):
        self.networks_sequence = networks_sequence
        self.temporal_metrics = {}

    def analyze_temporal_evolution(self):
        """Analyze how network properties evolve over time"""

        evolution_metrics = {}
        time_points = len(self.networks_sequence)

        # Initialize metric tracking
        metrics = {
            'num_nodes': [],
            'num_edges': [],
            'density': [],
            'clustering_coefficient': [],
            'avg_path_length': [],
            'diameter': [],
            'modularity': [],
            'num_communities': [],
            'largest_component_size': []
        }

        for t, G in enumerate(self.networks_sequence):
            print(f"Analyzing time point {t+1}/[TIME_POINTS]")

            # Basic metrics
            metrics['num_nodes'].append(G.number_of_nodes())
            metrics['num_edges'].append(G.number_of_edges())
            metrics['density'].append(nx.density(G))

            # Clustering coefficient
            if G.number_of_nodes() > 0:
                metrics['clustering_coefficient'].append(nx.average_clustering(G))
            else:
                metrics['clustering_coefficient'].append(0)

            # Path length and diameter (for connected component)
            if nx.is_connected(G):
                if G.number_of_nodes() > 1:
                    metrics['avg_path_length'].append(nx.average_shortest_path_length(G))
                    if G.number_of_nodes() < 500:  # Diameter is expensive
                        metrics['diameter'].append(nx.diameter(G))
                    else:
                        metrics['diameter'].append(None)
                else:
                    metrics['avg_path_length'].append(0)
                    metrics['diameter'].append(0)
            else:
                # Use largest component
                largest_cc = max(nx.connected_components(G), key=len) if G.number_of_nodes() > 0 else set()
                if len(largest_cc) > 1:
                    subG = G.subgraph(largest_cc)
                    metrics['avg_path_length'].append(nx.average_shortest_path_length(subG))
                    if len(largest_cc) < 500:
                        metrics['diameter'].append(nx.diameter(subG))
                    else:
                        metrics['diameter'].append(None)
                else:
                    metrics['avg_path_length'].append(0)
                    metrics['diameter'].append(0)

            # Community detection
            try:
                communities = community_louvain.best_partition(G)
                num_communities = len(set(communities.values()))
                modularity = community.modularity(G, [
                    [node for node, comm in communities.items() if comm == c]
                    for c in set(communities.values())
                ])

                metrics['num_communities'].append(num_communities)
                metrics['modularity'].append(modularity)
            except:
                metrics['num_communities'].append(0)
                metrics['modularity'].append(0)

            # Largest component size
            if G.number_of_nodes() > 0:
                largest_component = max(nx.connected_components(G), key=len)
                metrics['largest_component_size'].append(len(largest_component))
            else:
                metrics['largest_component_size'].append(0)

        evolution_metrics = pd.DataFrame(metrics)
        evolution_metrics['time'] = range(len(self.networks_sequence))

        self.temporal_metrics['evolution'] = evolution_metrics
        return evolution_metrics

    def node_lifecycle_analysis(self):
        """Analyze lifecycle of nodes across time"""

        # Track all nodes across time
        all_nodes = set()
        for G in self.networks_sequence:
            all_nodes.update(G.nodes())

        node_lifecycle = {}

        for node in all_nodes:
            lifecycle = {
                'first_appearance': None,
                'last_appearance': None,
                'total_appearances': 0,
                'continuous_periods': [],
                'intermittent': False
            }

            appearances = []
            for t, G in enumerate(self.networks_sequence):
                if node in G:
                    appearances.append(t)
                    lifecycle['total_appearances'] += 1

            if appearances:
                lifecycle['first_appearance'] = min(appearances)
                lifecycle['last_appearance'] = max(appearances)

                # Find continuous periods
                continuous_periods = []
                if appearances:
                    start = appearances[0]
                    end = appearances[0]

                    for i in range(1, len(appearances)):
                        if appearances[i] == end + 1:
                            end = appearances[i]
                        else:
                            continuous_periods.append((start, end))
                            start = appearances[i]
                            end = appearances[i]
                    continuous_periods.append((start, end))

                lifecycle['continuous_periods'] = continuous_periods
                lifecycle['intermittent'] = len(continuous_periods) > 1

            node_lifecycle[node] = lifecycle

        return node_lifecycle

    def edge_dynamics_analysis(self):
        """Analyze edge formation and dissolution"""

        edge_dynamics = {
            'persistent_edges': set(),
            'forming_edges': {},
            'dissolving_edges': {},
            'edge_lifetime': {},
            'temporal_edge_list': []
        }

        # Track all edges across time
        all_edges = set()
        for G in self.networks_sequence:
            all_edges.update(G.edges())

        for edge in all_edges:
            edge_presence = []
            for t, G in enumerate(self.networks_sequence):
                edge_presence.append(edge in G.edges() or (edge[1], edge[0]) in G.edges())

            # Calculate lifetime
            lifetime = sum(edge_presence)
            edge_dynamics['edge_lifetime'][edge] = {
                'lifetime': lifetime,
                'lifetime_fraction': lifetime / len(self.networks_sequence),
                'first_appearance': edge_presence.index(True) if True in edge_presence else None,
                'last_appearance': len(edge_presence) - 1 - edge_presence[::-1].index(True) if True in edge_presence else None
            }

            # Persistent edges (present in all time points)
            if all(edge_presence):
                edge_dynamics['persistent_edges'].add(edge)

        # Track edge formation and dissolution
        for t in range(1, len(self.networks_sequence)):
            prev_edges = set(self.networks_sequence[t-1].edges())
            curr_edges = set(self.networks_sequence[t].edges())

            # New edges
            forming = curr_edges - prev_edges
            edge_dynamics['forming_edges'][t] = forming

            # Dissolved edges
            dissolving = prev_edges - curr_edges
            edge_dynamics['dissolving_edges'][t] = dissolving

        return edge_dynamics

    def network_stability_analysis(self):
        """Analyze stability of network structure"""

        stability_metrics = {
            'jaccard_similarity': [],
            'hamming_distance': [],
            'degree_correlation': [],
            'structural_stability': []
        }

        for t in range(1, len(self.networks_sequence)):
            G_prev = self.networks_sequence[t-1]
            G_curr = self.networks_sequence[t]

            # Jaccard similarity of edge sets

[Content truncated for length - see original for full details]


## Variables

[The template includes 400+ comprehensive variables covering all aspects of network analysis, organized by category...]

## Usage Examples

### Example 1: Social Network Analysis
```
NETWORK_DATA_SOURCE: "Social media friendship connections"
NETWORK_TYPE: "Undirected, unweighted social network"
PRIMARY_ANALYSIS_GOAL: "Identify influential users and community structure"
CENTRALITY_MEASURES: "Degree, betweenness, closeness, eigenvector"
COMMUNITY_ALGORITHM: "Louvain method with resolution tuning"
```


### Example 4: Biological Network
```
NETWORK_DATA_SOURCE: "Protein-protein interaction network"
NETWORK_TYPE: "Undirected, weighted by interaction strength"
COMMUNITY_ANALYSIS: "Identify functional modules and pathways"
MOTIF_ANALYSIS: "Detect recurring interaction patterns"
DISEASE_ANALYSIS: "Identify disease-related network disruptions"
```


## Best Practices

1. **Focus**: Concentrate on the specific aspect covered by this template
2. **Integration**: Combine with related templates for comprehensive solutions
3. **Iteration**: Start simple and refine based on results
4. **Documentation**: Track your parameters and customizations

## Tips for Success

- Begin with the Quick Start section
- Customize variables to your specific context
- Validate outputs against your requirements
- Iterate and refine based on results

## Related Resources

See the overview file for the complete collection of related templates.

---

**Note:** This focused template is part of a comprehensive collection designed for improved usability.
