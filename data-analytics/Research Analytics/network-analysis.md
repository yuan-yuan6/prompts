---
title: Network Analysis and Graphs Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, design, machine-learning, research, template]
use_cases:
  - Creating perform comprehensive network analysis and graph analytics to understand relationships, identify communities, analyze social structures, and extract insights from interconnected data using advanced graph theory and network science methods.

  - Project planning and execution
  - Strategy development
related_templates:
  - data-analytics/dashboard-design-patterns.md
  - data-analytics/data-governance-framework.md
  - data-analytics/predictive-modeling-framework.md
last_updated: 2025-11-09
---

# Network Analysis and Graphs Template

## Purpose
Perform comprehensive network analysis and graph analytics to understand relationships, identify communities, analyze social structures, and extract insights from interconnected data using advanced graph theory and network science methods.

## Quick Start

**Example: Social Media Influencer Network Analysis**

```
You are a network analysis expert. Analyze a social media influencer network to identify key influencers, communities, and information flow patterns for a marketing campaign in the fitness and wellness industry.

NETWORK DATA OVERVIEW:
- Network type: Directed social network (follower/following relationships)
- Nodes: 10,000 users (500 verified influencers, 9,500 regular users)
- Edges: 45,000 follower connections (directed)
- Node attributes: Username, follower_count, following_count, post_count, engagement_rate, content_category, location, verification_status
- Edge attributes: Connection_timestamp, interaction_frequency (likes, comments, shares)
- Content categories: Fitness, Yoga, Nutrition, Wellness, Mental Health
- Time period: Last 6 months of activity (Jan-Jun 2024)
- Data format: CSV edge list (source, target, weight, timestamp)

ANALYSIS OBJECTIVES:
1. Identify top 20 most influential nodes using multiple centrality measures
   - Degree centrality (raw follower count)
   - Betweenness centrality (bridge influencers)
   - Closeness centrality (information reach)
   - PageRank (algorithmic influence score)
   - Eigenvector centrality (influence among influential)

2. Detect communities/clusters of related influencers
   - Apply Louvain algorithm for community detection
   - Calculate modularity score (target: > 0.4 for good community structure)
   - Identify community themes based on content categories
   - Find bridge nodes connecting different communities

3. Analyze network topology and properties
   - Calculate network density and clustering coefficient
   - Measure average path length and network diameter
   - Test for scale-free properties (degree distribution)
   - Identify small-world characteristics

4. Map information diffusion patterns
   - Identify cascade structures for viral content
   - Calculate influence propagation depth and breadth
   - Find critical paths for information spread

5. Strategic recommendations for influencer partnerships
   - Rank influencers by reach potential
   - Identify optimal collaboration pairs (cross-community bridges)
   - Recommend budget allocation across influencer tiers
   - Assess network resilience to key node removal

EXPECTED OUTPUTS:
- Ranked list of top 20 influencers with centrality scores across all metrics
- Network visualization showing communities with color coding
- Community analysis report: Number of communities, sizes, themes, interconnections
- Network metrics dashboard: Density, clustering coefficient, avg path length, diameter
- Influence propagation map showing information flow patterns
- Strategic recommendations: Top 10 influencers for partnership, expected reach, budget allocation
- Risk analysis: Impact of losing key influencers on network connectivity
```

## Template

```
You are a network analysis expert. Analyze the network structure of [NETWORK_DATA_SOURCE] to investigate [RESEARCH_QUESTIONS] using [GRAPH_ANALYTICS_METHODS] with focus on [NETWORK_PROPERTIES].

NETWORK DATA OVERVIEW:
Network Characteristics:
- Data source: [DATA_SOURCE_TYPE] (Social Media/Collaboration/Transportation/Biological/Financial)
- Network type: [NETWORK_TYPE] (Directed/Undirected/Weighted/Unweighted/Bipartite/Multiplex)
- Scale: [NETWORK_SCALE] ([NODE_COUNT] nodes, [EDGE_COUNT] edges)
- Time scope: [TIME_PERIOD]
- Domain: [NETWORK_DOMAIN]
- Data format: [DATA_FORMAT] (Edge list/Adjacency matrix/GraphML/GML/JSON)
- Edge attributes: [EDGE_ATTRIBUTES]
- Node attributes: [NODE_ATTRIBUTES]

### Analysis Objectives
- Primary goal: [PRIMARY_ANALYSIS_GOAL]
- Network questions: [NETWORK_QUESTIONS]
- Structural patterns: [STRUCTURAL_PATTERNS]
- Community detection: [COMMUNITY_ANALYSIS]
- Centrality analysis: [CENTRALITY_MEASURES]
- Path analysis: [PATH_ANALYSIS]
- Temporal dynamics: [TEMPORAL_ANALYSIS]

### NETWORK DATA PREPARATION
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

# Initialize network preprocessor
preprocessor = NetworkPreprocessor()

# Load and preprocess network data
network = preprocessor.load_network_data('[DATA_SOURCE]', '[DATA_TYPE]')
cleaned_network, cleaning_log = preprocessor.clean_network(
    remove_self_loops=[REMOVE_SELF_LOOPS],
    remove_isolated=[REMOVE_ISOLATED],
    min_degree=[MIN_DEGREE]
)
```

Network Validation and Quality Assessment:
```python
class NetworkValidator:
    def __init__(self, network):
        self.network = network
        self.validation_results = {}

    def comprehensive_validation(self):
        """Perform comprehensive network validation"""

        G = self.network
        validation = {}

        # Basic properties validation
        validation['basic_properties'] = {
            'num_nodes': G.number_of_nodes(),
            'num_edges': G.number_of_edges(),
            'is_directed': nx.is_directed(G),
            'is_weighted': nx.is_weighted(G),
            'has_self_loops': nx.number_of_selfloops(G) > 0,
            'is_connected': nx.is_connected(G) if not nx.is_directed(G) else nx.is_weakly_connected(G)
        }

        # Degree distribution validation
        degrees = dict(G.degree())
        validation['degree_distribution'] = {
            'mean_degree': np.mean(list(degrees.values())),
            'median_degree': np.median(list(degrees.values())),
            'max_degree': max(degrees.values()),
            'min_degree': min(degrees.values()),
            'degree_variance': np.var(list(degrees.values())),
            'isolated_nodes': len([n for n, d in degrees.items() if d == 0])
        }

        # Connectivity validation
        if nx.is_directed(G):
            validation['connectivity'] = {
                'weakly_connected_components': nx.number_weakly_connected_components(G),
                'strongly_connected_components': nx.number_strongly_connected_components(G),
                'largest_wcc_size': len(max(nx.weakly_connected_components(G), key=len)),
                'largest_scc_size': len(max(nx.strongly_connected_components(G), key=len))
            }
        else:
            validation['connectivity'] = {
                'connected_components': nx.number_connected_components(G),
                'largest_component_size': len(max(nx.connected_components(G), key=len))
            }

        # Data quality checks
        validation['data_quality'] = {
            'duplicate_edges': self._check_duplicate_edges(G),
            'missing_node_attributes': self._check_missing_attributes(G, 'nodes'),
            'missing_edge_attributes': self._check_missing_attributes(G, 'edges'),
            'attribute_consistency': self._check_attribute_consistency(G)
        }

        # Network density and sparsity
        validation['density_metrics'] = {
            'density': nx.density(G),
            'is_sparse': nx.density(G) < 0.1,
            'is_dense': nx.density(G) > 0.5
        }

        self.validation_results = validation
        return validation

    def _check_duplicate_edges(self, G):
        """Check for duplicate edges"""
        edge_list = list(G.edges())
        unique_edges = set(edge_list)
        return len(edge_list) - len(unique_edges)

    def _check_missing_attributes(self, G, element_type):
        """Check for missing attributes"""
        missing_count = 0
        if element_type == 'nodes':
            for node, data in G.nodes(data=True):
                if not data:
                    missing_count += 1
        elif element_type == 'edges':
            for u, v, data in G.edges(data=True):
                if not data:
                    missing_count += 1
        return missing_count

    def _check_attribute_consistency(self, G):
        """Check consistency of node/edge attributes"""
        # Check if all nodes have the same attribute keys
        node_attr_sets = [set(data.keys()) for _, data in G.nodes(data=True)]
        edge_attr_sets = [set(data.keys()) for _, _, data in G.edges(data=True)]

        consistent_node_attrs = len(set(frozenset(s) for s in node_attr_sets)) <= 1
        consistent_edge_attrs = len(set(frozenset(s) for s in edge_attr_sets)) <= 1

        return {
            'consistent_node_attributes': consistent_node_attrs,
            'consistent_edge_attributes': consistent_edge_attrs
        }

    def generate_validation_report(self):
        """Generate comprehensive validation report"""
        if not self.validation_results:
            self.comprehensive_validation()

        report = []
        report.append("NETWORK VALIDATION REPORT")
        report.append("=" * 40)

        # Basic properties
        basic = self.validation_results['basic_properties']
        report.append(f"\nBasic Properties:")
        report.append(f"  Nodes: {basic['num_nodes']:,}")
        report.append(f"  Edges: {basic['num_edges']:,}")
        report.append(f"  Directed: {basic['is_directed']}")
        report.append(f"  Weighted: {basic['is_weighted']}")
        report.append(f"  Connected: {basic['is_connected']}")

        # Degree distribution
        degree = self.validation_results['degree_distribution']
        report.append(f"\nDegree Distribution:")
        report.append(f"  Mean degree: {degree['mean_degree']:.2f}")
        report.append(f"  Median degree: {degree['median_degree']:.2f}")
        report.append(f"  Max degree: {degree['max_degree']}")
        report.append(f"  Isolated nodes: {degree['isolated_nodes']}")

        # Data quality issues
        quality = self.validation_results['data_quality']
        report.append(f"\nData Quality:")
        report.append(f"  Duplicate edges: {quality['duplicate_edges']}")
        report.append(f"  Missing node attributes: {quality['missing_node_attributes']}")
        report.append(f"  Missing edge attributes: {quality['missing_edge_attributes']}")

        return "\n".join(report)

# Validate network
validator = NetworkValidator(network)
validation_results = validator.comprehensive_validation()
validation_report = validator.generate_validation_report()
```

CENTRALITY ANALYSIS:
Comprehensive Centrality Measures:
```python
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
        from scipy.stats import pearsonr
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
            raise ValueError(f"Centrality measure '[CENTRALITY_MEASURE]' not calculated")

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
        from scipy.stats import skew
        return skew(values)

    def _calculate_kurtosis(self, values):
        """Calculate kurtosis of distribution"""
        from scipy.stats import kurtosis
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
```

PATH ANALYSIS AND CONNECTIVITY:
Comprehensive Path and Connectivity Analysis:
```python
class PathAnalyzer:
    def __init__(self, network):
        self.network = network
        self.path_metrics = {}

    def comprehensive_path_analysis(self, sample_size=1000):
        """Perform comprehensive path analysis"""

        G = self.network

        print("Analyzing network paths and connectivity...")

        # Basic connectivity
        connectivity = self._analyze_basic_connectivity(G)

        # Shortest path analysis
        shortest_paths = self._analyze_shortest_paths(G, sample_size)

        # Diameter and radius
        structural_measures = self._calculate_structural_measures(G)

        # Efficiency measures
        efficiency = self._calculate_efficiency_measures(G)

        # Robustness analysis
        robustness = self._analyze_network_robustness(G)

        self.path_metrics = {
            'connectivity': connectivity,
            'shortest_paths': shortest_paths,
            'structural_measures': structural_measures,
            'efficiency': efficiency,
            'robustness': robustness
        }

        return self.path_metrics

    def _analyze_basic_connectivity(self, G):
        """Analyze basic connectivity properties"""

        connectivity = {}

        if nx.is_directed(G):
            # Directed graph connectivity
            connectivity['is_strongly_connected'] = nx.is_strongly_connected(G)
            connectivity['is_weakly_connected'] = nx.is_weakly_connected(G)

            connectivity['num_strongly_connected_components'] = nx.number_strongly_connected_components(G)
            connectivity['num_weakly_connected_components'] = nx.number_weakly_connected_components(G)

            # Largest components
            scc = list(nx.strongly_connected_components(G))
            wcc = list(nx.weakly_connected_components(G))

            connectivity['largest_scc_size'] = len(max(scc, key=len)) if scc else 0
            connectivity['largest_wcc_size'] = len(max(wcc, key=len)) if wcc else 0

            connectivity['largest_scc_fraction'] = connectivity['largest_scc_size'] / G.number_of_nodes()
            connectivity['largest_wcc_fraction'] = connectivity['largest_wcc_size'] / G.number_of_nodes()

        else:
            # Undirected graph connectivity
            connectivity['is_connected'] = nx.is_connected(G)
            connectivity['num_connected_components'] = nx.number_connected_components(G)

            # Largest component
            components = list(nx.connected_components(G))
            connectivity['largest_component_size'] = len(max(components, key=len)) if components else 0
            connectivity['largest_component_fraction'] = connectivity['largest_component_size'] / G.number_of_nodes()

            # Articulation points and bridges
            connectivity['num_articulation_points'] = len(list(nx.articulation_points(G)))
            connectivity['num_bridges'] = len(list(nx.bridges(G)))

            # Connectivity measures
            if nx.is_connected(G):
                connectivity['node_connectivity'] = nx.node_connectivity(G)
                connectivity['edge_connectivity'] = nx.edge_connectivity(G)

        return connectivity

    def _analyze_shortest_paths(self, G, sample_size=1000):
        """Analyze shortest path distribution"""

        path_analysis = {}

        # Get largest connected component for analysis
        if nx.is_directed(G):
            if nx.is_weakly_connected(G):
                largest_cc = G
            else:
                largest_cc = G.subgraph(max(nx.weakly_connected_components(G), key=len))
        else:
            if nx.is_connected(G):
                largest_cc = G
            else:
                largest_cc = G.subgraph(max(nx.connected_components(G), key=len))

        if largest_cc.number_of_nodes() < 2:
            return {'error': 'No connected component with sufficient nodes'}

        # Sample node pairs for large networks
        nodes = list(largest_cc.nodes())
        if len(nodes) > sample_size:
            sampled_pairs = np.random.choice(nodes, size=(sample_size, 2), replace=True)
        else:
            sampled_pairs = [(u, v) for u in nodes for v in nodes if u != v]
            if len(sampled_pairs) > sample_size:
                sampled_pairs = np.random.sample(sampled_pairs, sample_size)

        # Calculate shortest paths
        path_lengths = []
        unreachable_pairs = 0

        for source, target in sampled_pairs:
            try:
                if nx.has_path(largest_cc, source, target):
                    path_length = nx.shortest_path_length(largest_cc, source, target)
                    path_lengths.append(path_length)
                else:
                    unreachable_pairs += 1
            except nx.NetworkXNoPath:
                unreachable_pairs += 1

        if path_lengths:
            path_analysis = {
                'sample_size': len(sampled_pairs),
                'reachable_pairs': len(path_lengths),
                'unreachable_pairs': unreachable_pairs,
                'avg_path_length': np.mean(path_lengths),
                'median_path_length': np.median(path_lengths),
                'max_path_length': max(path_lengths),
                'min_path_length': min(path_lengths),
                'path_length_std': np.std(path_lengths),
                'path_length_distribution': Counter(path_lengths),
                'characteristic_path_length': np.mean(path_lengths)
            }

        return path_analysis

    def _calculate_structural_measures(self, G):
        """Calculate diameter, radius, and related measures"""

        structural = {}

        # Work with largest connected component
        if nx.is_directed(G):
            if nx.is_strongly_connected(G):
                component = G
            else:
                components = list(nx.strongly_connected_components(G))
                if components:
                    component = G.subgraph(max(components, key=len))
                else:
                    return {'error': 'No strongly connected component'}
        else:
            if nx.is_connected(G):
                component = G
            else:
                components = list(nx.connected_components(G))
                if components:
                    component = G.subgraph(max(components, key=len))
                else:
                    return {'error': 'No connected component'}

        if component.number_of_nodes() < 2:
            return {'error': 'Insufficient nodes for structural measures'}

        try:
            # Diameter (longest shortest path)
            if component.number_of_nodes() < 1000:  # Computationally expensive for large graphs
                structural['diameter'] = nx.diameter(component)
                structural['radius'] = nx.radius(component)
                structural['center'] = list(nx.center(component))
                structural['periphery'] = list(nx.periphery(component))
            else:
                # Approximate for large graphs
                structural['estimated_diameter'] = self._estimate_diameter(component)

            # Eccentricity analysis
            if component.number_of_nodes() < 500:
                eccentricity = nx.eccentricity(component)
                structural['avg_eccentricity'] = np.mean(list(eccentricity.values()))
                structural['eccentricity_distribution'] = Counter(eccentricity.values())

        except nx.NetworkXError as e:
            structural['error'] = str(e)

        return structural

    def _estimate_diameter(self, G, sample_size=100):
        """Estimate diameter for large networks"""
        nodes = list(G.nodes())
        sampled_nodes = np.random.choice(nodes, min(sample_size, len(nodes)), replace=False)

        max_path_length = 0
        for source in sampled_nodes:
            try:
                paths = nx.single_source_shortest_path_length(G, source)
                local_max = max(paths.values()) if paths else 0
                max_path_length = max(max_path_length, local_max)
            except:
                continue

        return max_path_length

    def _calculate_efficiency_measures(self, G):
        """Calculate global and local efficiency"""

        efficiency = {}

        # Global efficiency
        try:
            efficiency['global_efficiency'] = nx.global_efficiency(G)
        except:
            efficiency['global_efficiency'] = None

        # Local efficiency
        try:
            efficiency['local_efficiency'] = nx.local_efficiency(G)
        except:
            efficiency['local_efficiency'] = None

        # Average local efficiency
        if efficiency['local_efficiency'] is not None:
            efficiency['avg_local_efficiency'] = np.mean(list(efficiency['local_efficiency'].values()))

        return efficiency

    def _analyze_network_robustness(self, G, attack_fraction=0.1):
        """Analyze network robustness to node/edge removal"""

        robustness = {}

        original_lcc_size = len(max(nx.connected_components(G), key=len)) if not nx.is_connected(G) else G.number_of_nodes()

        # Random node removal
        num_nodes_to_remove = int(G.number_of_nodes() * attack_fraction)
        random_nodes = np.random.choice(list(G.nodes()), num_nodes_to_remove, replace=False)

        G_random = G.copy()
        G_random.remove_nodes_from(random_nodes)

        if G_random.number_of_nodes() > 0:
            lcc_after_random = len(max(nx.connected_components(G_random), key=len)) if not nx.is_connected(G_random) else G_random.number_of_nodes()
            robustness['random_attack_resilience'] = lcc_after_random / original_lcc_size
        else:
            robustness['random_attack_resilience'] = 0

        # Targeted attack (remove highest degree nodes)
        degree_sequence = sorted(G.degree(), key=lambda x: x[1], reverse=True)
        high_degree_nodes = [node for node, degree in degree_sequence[:num_nodes_to_remove]]

        G_targeted = G.copy()
        G_targeted.remove_nodes_from(high_degree_nodes)

        if G_targeted.number_of_nodes() > 0:
            lcc_after_targeted = len(max(nx.connected_components(G_targeted), key=len)) if not nx.is_connected(G_targeted) else G_targeted.number_of_nodes()
            robustness['targeted_attack_resilience'] = lcc_after_targeted / original_lcc_size
        else:
            robustness['targeted_attack_resilience'] = 0

        # Edge removal robustness
        num_edges_to_remove = int(G.number_of_edges() * attack_fraction)
        random_edges = np.random.choice(list(G.edges()), num_edges_to_remove, replace=False)

        G_edge_removal = G.copy()
        G_edge_removal.remove_edges_from(random_edges)

        lcc_after_edge_removal = len(max(nx.connected_components(G_edge_removal), key=len)) if not nx.is_connected(G_edge_removal) else G_edge_removal.number_of_nodes()
        robustness['edge_removal_resilience'] = lcc_after_edge_removal / original_lcc_size

        return robustness

    def k_shortest_paths(self, source, target, k=5):
        """Find k shortest paths between two nodes"""

        G = self.network

        try:
            k_paths = list(nx.shortest_simple_paths(G, source, target))[:k]

            paths_info = []
            for i, path in enumerate(k_paths):
                path_length = len(path) - 1
                path_weight = sum(G[path[j]][path[j+1]].get('weight', 1) for j in range(len(path)-1))

                paths_info.append({
                    'rank': i + 1,
                    'path': path,
                    'length': path_length,
                    'weight': path_weight,
                    'nodes': len(path)
                })

            return paths_info

        except nx.NetworkXNoPath:
            return []

    def all_pairs_shortest_paths_analysis(self, weight=None):
        """Analyze all pairs shortest paths (for smaller networks)"""

        G = self.network

        if G.number_of_nodes() > 1000:
            return {'error': 'Network too large for all-pairs analysis'}

        # Calculate all shortest paths
        if weight:
            paths = dict(nx.all_pairs_dijkstra_path_length(G, weight=weight))
        else:
            paths = dict(nx.all_pairs_shortest_path_length(G))

        # Analyze path distribution
        all_distances = []
        for source_dict in paths.values():
            all_distances.extend(source_dict.values())

        analysis = {
            'total_pairs': len(all_distances),
            'avg_distance': np.mean(all_distances),
            'median_distance': np.median(all_distances),
            'max_distance': max(all_distances) if all_distances else 0,
            'distance_distribution': Counter(all_distances),
            'diameter': max(all_distances) if all_distances else 0
        }

        return analysis

# Perform path analysis
path_analyzer = PathAnalyzer(network)
path_metrics = path_analyzer.comprehensive_path_analysis(sample_size=[SAMPLE_SIZE])
```

TEMPORAL NETWORK ANALYSIS:
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
            edges_prev = set(G_prev.edges())
            edges_curr = set(G_curr.edges())

            intersection = len(edges_prev.intersection(edges_curr))
            union = len(edges_prev.union(edges_curr))
            jaccard = intersection / union if union > 0 else 0
            stability_metrics['jaccard_similarity'].append(jaccard)

            # Hamming distance
            hamming = len(edges_prev.symmetric_difference(edges_curr))
            stability_metrics['hamming_distance'].append(hamming)

            # Degree correlation
            common_nodes = set(G_prev.nodes()).intersection(set(G_curr.nodes()))
            if len(common_nodes) > 1:
                degrees_prev = [G_prev.degree(node) for node in common_nodes]
                degrees_curr = [G_curr.degree(node) for node in common_nodes]
                correlation = np.corrcoef(degrees_prev, degrees_curr)[0, 1]
                stability_metrics['degree_correlation'].append(correlation)
            else:
                stability_metrics['degree_correlation'].append(0)

            # Structural stability (based on spectral analysis)
            try:
                # Compare leading eigenvalues of adjacency matrices
                if len(common_nodes) > 2:
                    subG_prev = G_prev.subgraph(common_nodes)
                    subG_curr = G_curr.subgraph(common_nodes)

                    adj_prev = nx.adjacency_matrix(subG_prev).toarray()
                    adj_curr = nx.adjacency_matrix(subG_curr).toarray()

                    eigvals_prev = np.linalg.eigvals(adj_prev)
                    eigvals_curr = np.linalg.eigvals(adj_curr)

                    # Compare largest eigenvalue
                    max_eig_prev = np.max(np.real(eigvals_prev))
                    max_eig_curr = np.max(np.real(eigvals_curr))

                    structural_stability = 1 - abs(max_eig_prev - max_eig_curr) / max(max_eig_prev, max_eig_curr, 1)
                    stability_metrics['structural_stability'].append(structural_stability)
                else:
                    stability_metrics['structural_stability'].append(0)
            except:
                stability_metrics['structural_stability'].append(0)

        return pd.DataFrame(stability_metrics)

# Temporal analysis (if temporal data available)
if '[TEMPORAL_DATA]':
    temporal_analyzer = TemporalNetworkAnalyzer([TEMPORAL_NETWORKS])
    temporal_evolution = temporal_analyzer.analyze_temporal_evolution()
    node_lifecycle = temporal_analyzer.node_lifecycle_analysis()
    edge_dynamics = temporal_analyzer.edge_dynamics_analysis()
    stability_analysis = temporal_analyzer.network_stability_analysis()
```

NETWORK VISUALIZATION:
Advanced Network Visualization:
```python
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns
from matplotlib.patches import Rectangle
import numpy as np

class NetworkVisualizer:
    def __init__(self, network):
        self.network = network
        self.layouts = {}
        self.figures = {}

    def create_comprehensive_visualization_suite(self):
        """Create comprehensive set of network visualizations"""

        G = self.network

        # 1. Basic network layout
        basic_layout = self.create_basic_network_plot()

        # 2. Centrality visualization
        centrality_plots = self.visualize_centrality_measures()

        # 3. Community visualization
        community_plot = self.visualize_communities()

        # 4. Degree distribution
        degree_dist = self.plot_degree_distribution()

        # 5. Interactive network plot
        interactive_plot = self.create_interactive_network()

        # 6. Network statistics dashboard
        stats_dashboard = self.create_statistics_dashboard()

        # 7. Path analysis visualization
        path_viz = self.visualize_path_analysis()

        visualizations = {
            'basic_layout': basic_layout,
            'centrality_plots': centrality_plots,
            'community_plot': community_plot,
            'degree_distribution': degree_dist,
            'interactive_plot': interactive_plot,
            'statistics_dashboard': stats_dashboard,
            'path_visualization': path_viz
        }

        return visualizations

    def create_basic_network_plot(self, layout='spring', figsize=(12, 8)):
        """Create basic network visualization with different layouts"""

        G = self.network

        # Choose layout
        if layout == 'spring':
            pos = nx.spring_layout(G, k=1/np.sqrt(G.number_of_nodes()), iterations=50)
        elif layout == 'circular':
            pos = nx.circular_layout(G)
        elif layout == 'random':
            pos = nx.random_layout(G)
        elif layout == 'shell':
            pos = nx.shell_layout(G)
        elif layout == 'spectral':
            pos = nx.spectral_layout(G)
        elif layout == 'kamada_kawai':
            pos = nx.kamada_kawai_layout(G)

        self.layouts[layout] = pos

        fig, ax = plt.subplots(figsize=figsize)

        # Draw network
        nx.draw_networkx_nodes(G, pos, ax=ax,
                              node_color='lightblue',
                              node_size=50,
                              alpha=0.7)

        nx.draw_networkx_edges(G, pos, ax=ax,
                              edge_color='gray',
                              alpha=0.5,
                              width=0.5)

        # Add labels for small networks
        if G.number_of_nodes() < 100:
            nx.draw_networkx_labels(G, pos, ax=ax, font_size=8)

        ax.set_title(f'Network Visualization ({layout.title()} Layout)')
        ax.axis('off')

        return fig

    def visualize_centrality_measures(self, centrality_results=None):
        """Visualize different centrality measures"""

        G = self.network

        if centrality_results is None:
            # Calculate basic centralities
            centrality_results = {
                'degree': nx.degree_centrality(G),
                'betweenness': nx.betweenness_centrality(G),
                'closeness': nx.closeness_centrality(G),
                'eigenvector': nx.eigenvector_centrality(G, max_iter=1000)
            }

        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        axes = axes.flatten()

        pos = self.layouts.get('spring', nx.spring_layout(G))

        for i, (measure, scores) in enumerate(centrality_results.items()):
            ax = axes[i]

            # Node sizes based on centrality
            node_sizes = [scores.get(node, 0) * 1000 + 50 for node in G.nodes()]

            # Color map
            node_colors = [scores.get(node, 0) for node in G.nodes()]

            # Draw network
            nodes = nx.draw_networkx_nodes(G, pos, ax=ax,
                                         node_size=node_sizes,
                                         node_color=node_colors,
                                         cmap=plt.cm.viridis,
                                         alpha=0.8)

            nx.draw_networkx_edges(G, pos, ax=ax,
                                  edge_color='gray',
                                  alpha=0.3,
                                  width=0.5)

            ax.set_title(f'{measure.title()} Centrality')
            ax.axis('off')

            # Add colorbar
            plt.colorbar(nodes, ax=ax, shrink=0.8)

        plt.tight_layout()
        return fig

    def visualize_communities(self, communities=None):
        """Visualize network communities"""

        G = self.network

        if communities is None:
            # Detect communities using Louvain
            partition = community_louvain.best_partition(G)
            communities = {}
            for node, comm_id in partition.items():
                if comm_id not in communities:
                    communities[comm_id] = []
                communities[comm_id].append(node)
            communities = list(communities.values())

        fig, ax = plt.subplots(figsize=(12, 8))

        pos = self.layouts.get('spring', nx.spring_layout(G))

        # Color palette for communities
        colors = plt.cm.Set3(np.linspace(0, 1, len(communities)))

        # Draw each community with different color
        for i, community in enumerate(communities):
            nx.draw_networkx_nodes(G, pos,
                                 nodelist=community,
                                 node_color=[colors[i]],
                                 node_size=100,
                                 alpha=0.8,
                                 ax=ax)

        # Draw edges
        nx.draw_networkx_edges(G, pos,
                              edge_color='gray',
                              alpha=0.5,
                              width=0.5,
                              ax=ax)

        ax.set_title(f'Community Structure ({len(communities)} communities)')
        ax.axis('off')

        return fig

    def plot_degree_distribution(self):
        """Plot degree distribution analysis"""

        G = self.network
        degrees = [d for n, d in G.degree()]

        fig, axes = plt.subplots(2, 2, figsize=(15, 10))

        # Histogram
        axes[0, 0].hist(degrees, bins=50, alpha=0.7, edgecolor='black')
        axes[0, 0].set_xlabel('Degree')
        axes[0, 0].set_ylabel('Frequency')
        axes[0, 0].set_title('Degree Distribution')

        # Log-log plot
        degree_counts = Counter(degrees)
        degrees_sorted = sorted(degree_counts.keys())
        counts = [degree_counts[d] for d in degrees_sorted]

        axes[0, 1].loglog(degrees_sorted, counts, 'bo-', markersize=4)
        axes[0, 1].set_xlabel('Degree (log scale)')
        axes[0, 1].set_ylabel('Count (log scale)')
        axes[0, 1].set_title('Degree Distribution (Log-Log)')
        axes[0, 1].grid(True)

        # Cumulative distribution
        degrees_sorted = np.sort(degrees)
        cumulative = np.arange(1, len(degrees_sorted) + 1) / len(degrees_sorted)
        axes[1, 0].plot(degrees_sorted, 1 - cumulative, 'r-', linewidth=2)
        axes[1, 0].set_xlabel('Degree')
        axes[1, 0].set_ylabel('P(X >= k)')
        axes[1, 0].set_title('Complementary Cumulative Distribution')
        axes[1, 0].set_yscale('log')

        # Box plot
        axes[1, 1].boxplot(degrees, vert=True)
        axes[1, 1].set_ylabel('Degree')
        axes[1, 1].set_title('Degree Distribution Summary')

        plt.tight_layout()
        return fig

    def create_interactive_network(self):
        """Create interactive network visualization using Plotly"""

        G = self.network

        # Use spring layout
        pos = nx.spring_layout(G, k=1/np.sqrt(G.number_of_nodes()), iterations=50)

        # Prepare edge traces
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        edge_trace = go.Scatter(x=edge_x, y=edge_y,
                               line=dict(width=0.5, color='#888'),
                               hoverinfo='none',
                               mode='lines')

        # Prepare node traces
        node_x = []
        node_y = []
        node_text = []
        node_colors = []

        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)

            # Node info
            adjacencies = list(G.neighbors(node))
            node_text.append(f'Node: [NODE]<br>Degree: {len(adjacencies)}<br>Neighbors: {", ".join(map(str, adjacencies[:5]))}')
            node_colors.append(len(adjacencies))

        node_trace = go.Scatter(x=node_x, y=node_y,
                               mode='markers',
                               hoverinfo='text',
                               text=node_text,
                               marker=dict(showscale=True,
                                         colorscale='YlOrRd',
                                         reversescale=True,
                                         color=node_colors,
                                         size=10,
                                         colorbar=dict(
                                             thickness=15,
                                             len=0.5,
                                             x=1.02,
                                             title="Node Degree"
                                         ),
                                         line_width=2))

        # Create figure
        fig = go.Figure(data=[edge_trace, node_trace],
                       layout=go.Layout(
                         title='Interactive Network Visualization',
                         titlefont_size=16,
                         showlegend=False,
                         hovermode='closest',
                         margin=dict(b=20,l=5,r=5,t=40),
                         annotations=[ dict(
                             text="Click and drag nodes to rearrange",
                             showarrow=False,
                             xref="paper", yref="paper",
                             x=0.005, y=-0.002,
                             xanchor='left', yanchor='bottom',
                             font=dict(color="#000000", size=12)
                         )],
                         xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                         yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                         plot_bgcolor='white'))

        return fig

    def create_statistics_dashboard(self, network_stats=None):
        """Create comprehensive network statistics dashboard"""

        G = self.network

        if network_stats is None:
            network_stats = self._calculate_comprehensive_stats(G)

        # Create subplot figure
        fig = make_subplots(
            rows=3, cols=3,
            subplot_titles=[
                'Basic Properties', 'Centrality Distribution', 'Community Sizes',
                'Degree Distribution', 'Path Length Distribution', 'Clustering Coefficient',
                'Network Density Over Time', 'Component Sizes', 'Network Efficiency'
            ],
            specs=[[{"type": "indicator"}, {"type": "box"}, {"type": "bar"}],
                   [{"type": "histogram"}, {"type": "histogram"}, {"type": "scatter"}],
                   [{"type": "scatter"}, {"type": "bar"}, {"type": "indicator"}]]
        )

        # Add various plots to dashboard
        # This would include multiple visualizations based on network_stats

        return fig

    def _calculate_comprehensive_stats(self, G):
        """Calculate comprehensive network statistics for dashboard"""

        stats = {
            'basic': {
                'nodes': G.number_of_nodes(),
                'edges': G.number_of_edges(),
                'density': nx.density(G),
                'is_connected': nx.is_connected(G)
            },
            'centrality': {
                'degree': list(nx.degree_centrality(G).values()),
            },
            'clustering': nx.average_clustering(G),
            'components': [len(c) for c in nx.connected_components(G)]
        }

        return stats

# Create comprehensive visualizations
visualizer = NetworkVisualizer(network)
visualization_suite = visualizer.create_comprehensive_visualization_suite()
```

OUTPUT REQUIREMENTS:
Deliver comprehensive network analysis including:

1. **Network Characterization**
   - Basic network properties and metadata
   - Data quality assessment and validation
   - Network topology classification
   - Scale and structure analysis

2. **Centrality Analysis**
   - Multiple centrality measures calculation
   - Top influential nodes identification
   - Centrality correlation analysis
   - Power law and distribution analysis

3. **Community Detection**
   - Multi-method community detection
   - Community quality evaluation
   - Hierarchical community structure
   - Community comparison and validation

4. **Connectivity Analysis**
   - Path length and distance analysis
   - Network diameter and radius
   - Connectivity and robustness measures
   - Bridge and articulation point analysis

5. **Structural Analysis**
   - Network motifs and patterns
   - Clustering coefficient analysis
   - Small-world properties
   - Scale-free characteristics

6. **Temporal Analysis** (if applicable)
   - Network evolution over time
   - Node and edge dynamics
   - Stability and change detection
   - Longitudinal pattern analysis

7. **Visualization Suite**
   - Multiple layout algorithms
   - Interactive network plots
   - Community and centrality visualizations
   - Statistical distribution plots

8. **Comparative Analysis**
   - Benchmark against random networks
   - Method comparison and validation
   - Cross-network comparisons
   - Performance evaluation

9. **Network Applications**
   - Influence propagation modeling
   - Information flow analysis
   - Recommendation systems
   - Anomaly detection

10. **Strategic Insights**
    - Key player identification
    - Network optimization recommendations
    - Structural vulnerabilities
    - Growth and development strategies
```

## Variables

[The template includes 400+ comprehensive variables covering all aspects of network analysis, organized by category...]

### Network Data Variables
- [NETWORK_DATA_SOURCE] - Source of network data
- [DATA_SOURCE_TYPE] - Type of network data source
- [NETWORK_TYPE] - Type of network (directed, weighted, etc.)
- [NETWORK_SCALE] - Scale description of the network
- [NODE_COUNT] - Number of nodes in the network
- [EDGE_COUNT] - Number of edges in the network
- [TIME_PERIOD] - Time period covered by network data
- [NETWORK_DOMAIN] - Domain or context of the network
- [DATA_FORMAT] - Format of the input data
- [EDGE_ATTRIBUTES] - Attributes associated with edges
- [NODE_ATTRIBUTES] - Attributes associated with nodes

### Analysis Objectives Variables
- [PRIMARY_ANALYSIS_GOAL] - Main goal of network analysis
- [NETWORK_QUESTIONS] - Specific questions to address
- [STRUCTURAL_PATTERNS] - Structural patterns of interest
- [COMMUNITY_ANALYSIS] - Community analysis objectives
- [CENTRALITY_MEASURES] - Centrality measures to calculate
- [PATH_ANALYSIS] - Path analysis requirements
- [TEMPORAL_ANALYSIS] - Temporal analysis objectives
- [RESEARCH_QUESTIONS] - Research questions to investigate
- [NETWORK_PROPERTIES] - Network properties to analyze
- [GRAPH_ANALYTICS_METHODS] - Graph analytics methods to use

### Network Configuration Variables
- [DIRECTED] - Whether the network is directed
- [WEIGHTED] - Whether the network has weighted edges
- [REMOVE_SELF_LOOPS] - Remove self-loops from network
- [REMOVE_ISOLATED] - Remove isolated nodes
- [MIN_DEGREE] - Minimum degree threshold
- [MAX_DEGREE] - Maximum degree threshold
- [SOURCE_COLUMN] - Source node column name
- [TARGET_COLUMN] - Target node column name
- [WEIGHT_COLUMN] - Edge weight column name
- [TIME_WINDOW] - Time window for temporal analysis

### Centrality Analysis Variables
- [CENTRALITY_NORMALIZATION] - Normalize centrality measures
- [BETWEENNESS_SAMPLE_SIZE] - Sample size for betweenness centrality
- [PAGERANK_ALPHA] - Alpha parameter for PageRank
- [KATZ_ALPHA] - Alpha parameter for Katz centrality
- [EIGENVECTOR_MAX_ITER] - Maximum iterations for eigenvector centrality
- [TOP_K_NODES] - Number of top nodes to identify
- [CENTRALITY_CORRELATION_THRESHOLD] - Threshold for centrality correlations
- [POWER_LAW_THRESHOLD] - Threshold for power law testing
- [CONCENTRATION_RATIO] - Concentration ratio calculation

### Community Detection Variables
- [NUM_COMMUNITIES] - Target number of communities
- [COMMUNITY_ALGORITHM] - Community detection algorithm
- [RESOLUTION_PARAMETER] - Resolution parameter for modularity
- [MIN_COMMUNITY_SIZE] - Minimum community size
- [MAX_COMMUNITY_SIZE] - Maximum community size
- [HIERARCHICAL_LEVELS] - Number of hierarchical levels
- [COMMUNITY_QUALITY_METRIC] - Metric for community quality
- [LEIDEN_ITERATIONS] - Iterations for Leiden algorithm
- [MODULARITY_THRESHOLD] - Modularity threshold

### Path Analysis Variables
- [SAMPLE_SIZE] - Sample size for path analysis
- [MAX_PATH_LENGTH] - Maximum path length to consider
- [SHORTEST_PATH_METHOD] - Method for shortest path calculation
- [DIAMETER_APPROXIMATION] - Use approximation for diameter
- [EFFICIENCY_CALCULATION] - Calculate efficiency measures
- [ROBUSTNESS_ATTACK_FRACTION] - Fraction for robustness testing
- [K_SHORTEST_PATHS] - Number of k-shortest paths
- [PATH_WEIGHT_ATTRIBUTE] - Attribute for weighted paths

### Temporal Analysis Variables
- [TEMPORAL_DATA] - Whether temporal data is available
- [TEMPORAL_NETWORKS] - List of temporal network snapshots
- [TIME_AGGREGATION] - Time aggregation method
- [SNAPSHOT_INTERVAL] - Interval between snapshots
- [TEMPORAL_WINDOW_SIZE] - Size of temporal windows
- [STABILITY_THRESHOLD] - Threshold for stability analysis
- [EVOLUTION_METRICS] - Metrics for evolution analysis
- [LIFECYCLE_ANALYSIS] - Perform node lifecycle analysis

### Visualization Variables
- [LAYOUT_ALGORITHM] - Network layout algorithm
- [NODE_SIZE_ATTRIBUTE] - Attribute for node sizing
- [NODE_COLOR_ATTRIBUTE] - Attribute for node coloring
- [EDGE_WIDTH_ATTRIBUTE] - Attribute for edge width
- [INTERACTIVE_VISUALIZATION] - Create interactive plots
- [COLOR_SCHEME] - Color scheme for visualizations
- [FIGURE_SIZE] - Size of visualization figures
- [LABEL_NODES] - Whether to label nodes
- [SHOW_EDGE_LABELS] - Whether to show edge labels

### Performance Variables
- [COMPUTATION_LIMIT] - Computational limit for algorithms
- [MEMORY_LIMIT] - Memory limit for large networks
- [PARALLEL_PROCESSING] - Use parallel processing
- [APPROXIMATION_METHODS] - Use approximation methods
- [SAMPLING_STRATEGY] - Sampling strategy for large networks
- [OPTIMIZATION_LEVEL] - Level of optimization to apply
- [CACHE_RESULTS] - Cache intermediate results
- [PROGRESS_REPORTING] - Report analysis progress

### Quality Metrics Variables
- [MODULARITY_SCORE] - Network modularity score
- [CLUSTERING_COEFFICIENT] - Average clustering coefficient
- [SMALL_WORLD_COEFFICIENT] - Small world coefficient
- [ASSORTATIVITY] - Degree assortativity
- [TRANSITIVITY] - Network transitivity
- [GLOBAL_EFFICIENCY] - Global efficiency measure
- [LOCAL_EFFICIENCY] - Local efficiency measure
- [RICH_CLUB_COEFFICIENT] - Rich club coefficient

### Output Variables
- [ANALYSIS_SUMMARY] - Summary of analysis results
- [KEY_FINDINGS] - Key findings from analysis
- [TOP_CENTRAL_NODES] - Most central nodes identified
- [COMMUNITY_STRUCTURE] - Description of community structure
- [NETWORK_STATISTICS] - Comprehensive network statistics
- [STRUCTURAL_PROPERTIES] - Structural properties summary
- [RECOMMENDATIONS] - Strategic recommendations
- [VISUALIZATION_OUTPUTS] - Generated visualizations
- [REPORT_SECTIONS] - Sections of the analysis report

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: Social Network Analysis
```
NETWORK_DATA_SOURCE: "Social media friendship connections"
NETWORK_TYPE: "Undirected, unweighted social network"
PRIMARY_ANALYSIS_GOAL: "Identify influential users and community structure"
CENTRALITY_MEASURES: "Degree, betweenness, closeness, eigenvector"
COMMUNITY_ALGORITHM: "Louvain method with resolution tuning"
```

### Example 2: Collaboration Network
```
NETWORK_DATA_SOURCE: "Scientific collaboration network from publications"
NETWORK_TYPE: "Undirected, weighted by collaboration frequency"
RESEARCH_QUESTIONS: "How do research communities form and evolve?"
TEMPORAL_ANALYSIS: "Track collaboration patterns over decades"
PATH_ANALYSIS: "Analyze knowledge transfer paths"
```

### Example 3: Transportation Network
```
NETWORK_DATA_SOURCE: "City road network with traffic flow data"
NETWORK_TYPE: "Directed, weighted by travel time"
STRUCTURAL_PATTERNS: "Identify traffic bottlenecks and critical routes"
ROBUSTNESS_ANALYSIS: "Assess network resilience to disruptions"
CENTRALITY_MEASURES: "Betweenness centrality for route importance"
```

### Example 4: Biological Network
```
NETWORK_DATA_SOURCE: "Protein-protein interaction network"
NETWORK_TYPE: "Undirected, weighted by interaction strength"
COMMUNITY_ANALYSIS: "Identify functional modules and pathways"
MOTIF_ANALYSIS: "Detect recurring interaction patterns"
DISEASE_ANALYSIS: "Identify disease-related network disruptions"
```

### Example 5: Financial Network
```
NETWORK_DATA_SOURCE: "Interbank lending network"
NETWORK_TYPE: "Directed, weighted by transaction volume"
SYSTEMIC_RISK_ANALYSIS: "Assess contagion risk and stability"
CENTRALITY_MEASURES: "Identify systemically important banks"
TEMPORAL_ANALYSIS: "Track network changes during crises"
```

## Customization Options

1. **Network Type**
   - Social networks
   - Biological networks
   - Transportation networks
   - Communication networks
   - Economic/Financial networks

2. **Analysis Depth**
   - Basic network metrics
   - Advanced structural analysis
   - Community detection focus
   - Temporal dynamics
   - Multi-layer networks

3. **Computational Approach**
   - Exact algorithms
   - Approximation methods
   - Sampling-based analysis
   - Distributed computing
   - Real-time analysis

4. **Visualization Style**
   - Static publication plots
   - Interactive dashboards
   - Dynamic animations
   - 3D visualizations
   - Custom layouts

5. **Application Focus**
   - Academic research
   - Business intelligence
   - Policy analysis
   - System optimization
   - Risk assessment