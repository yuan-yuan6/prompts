---
title: Network Analysis - Paths and Temporal Dynamics
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, network-analysis, path-analysis, temporal-networks]
use_cases:
  - Analyzing network connectivity and shortest paths
  - Measuring network diameter, radius, and efficiency
  - Assessing network robustness and resilience
  - Tracking temporal evolution of network structure
related_templates:
  - data-analytics/Research Analytics/network-analysis-data-preparation.md
  - data-analytics/Research Analytics/network-analysis-centrality-community.md
  - data-analytics/Research Analytics/network-analysis-visualization.md
  - data-analytics/Research Analytics/network-analysis-overview.md
last_updated: 2025-11-10
---

# Network Analysis - Paths and Temporal Dynamics

## Purpose
Analyze network connectivity, path structures, robustness, and temporal evolution. This module provides comprehensive tools for path analysis, connectivity measurement, robustness testing, and tracking how networks change over time.

## Quick Start

**Example: Analyze Network Connectivity and Robustness**

```
You are a network analysis expert. Analyze the connectivity structure and robustness of a transportation network.

NETWORK OVERVIEW:
- Network: City road network
- Nodes: 500 intersections
- Edges: 1,200 road segments
- Type: Undirected, weighted by travel time

PATH ANALYSIS OBJECTIVES:
1. Calculate shortest path metrics:
   - Average path length across all node pairs
   - Network diameter (longest shortest path)
   - Network radius and center nodes
   - Path length distribution

2. Measure connectivity:
   - Number of connected components
   - Size of largest connected component
   - Articulation points (critical intersections)
   - Bridge edges (critical road segments)

3. Calculate efficiency measures:
   - Global efficiency (overall connectivity)
   - Local efficiency (neighborhood connectivity)
   - Average node efficiency

ROBUSTNESS ANALYSIS:
1. Test resilience to failures:
   - Random node removal (10% of nodes)
   - Targeted attack (remove highest degree nodes)
   - Random edge removal (10% of edges)

2. Measure impact:
   - Change in largest component size
   - Change in average path length
   - Network fragmentation

3. Identify critical nodes:
   - Nodes whose removal most impacts connectivity
   - Bottleneck identification

EXPECTED OUTPUT:
- Comprehensive path metrics report
- Connectivity analysis with critical nodes
- Robustness resilience scores
- Vulnerability assessment
- Recommendations for network strengthening
```

## Template

```
You are a network analysis expert. Analyze paths, connectivity, and temporal dynamics of [NETWORK_DATA_SOURCE].

PATH ANALYSIS REQUIREMENTS:
Metrics to Calculate:
- Average path length: [CALCULATE_AVG_PATH_LENGTH]
- Network diameter: [CALCULATE_DIAMETER]
- Network radius: [CALCULATE_RADIUS]
- Eccentricity distribution: [CALCULATE_ECCENTRICITY]
- K-shortest paths: [K_SHORTEST_PATHS]

Analysis Parameters:
- Sample size: [SAMPLE_SIZE]
- Maximum path length: [MAX_PATH_LENGTH]
- Use approximation: [DIAMETER_APPROXIMATION]
- Weight attribute: [PATH_WEIGHT_ATTRIBUTE]

CONNECTIVITY REQUIREMENTS:
Components Analysis:
- Connected components: [ANALYZE_COMPONENTS]
- Articulation points: [FIND_ARTICULATION_POINTS]
- Bridge edges: [FIND_BRIDGES]
- Node/edge connectivity: [CALCULATE_CONNECTIVITY]

Efficiency Metrics:
- Global efficiency: [CALCULATE_GLOBAL_EFFICIENCY]
- Local efficiency: [CALCULATE_LOCAL_EFFICIENCY]

ROBUSTNESS TESTING:
Attack Simulations:
- Random attack fraction: [ROBUSTNESS_ATTACK_FRACTION]
- Targeted attack strategy: [TARGETED_ATTACK_STRATEGY]
- Edge removal testing: [TEST_EDGE_REMOVAL]

Impact Metrics:
- Component size changes: [TRACK_COMPONENT_CHANGES]
- Path length changes: [TRACK_PATH_CHANGES]
- Fragmentation measures: [MEASURE_FRAGMENTATION]

TEMPORAL ANALYSIS (if applicable):
Evolution Tracking:
- Temporal data available: [TEMPORAL_DATA]
- Number of snapshots: [NUM_TEMPORAL_SNAPSHOTS]
- Time aggregation: [TIME_AGGREGATION]
- Stability threshold: [STABILITY_THRESHOLD]

Metrics to Track:
- Network growth/shrinkage
- Structural stability
- Node/edge lifecycle
- Community evolution
```

## Path Analysis and Connectivity

### PathAnalyzer Class

```python
import networkx as nx
import pandas as pd
import numpy as np
from collections import Counter

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
            sampled_pairs = [(np.random.choice(nodes), np.random.choice(nodes)) for _ in range(sample_size)]
        else:
            sampled_pairs = [(u, v) for u in nodes for v in nodes if u != v]
            if len(sampled_pairs) > sample_size:
                sampled_pairs = np.random.choice(len(sampled_pairs), sample_size, replace=False)
                sampled_pairs = [sampled_pairs[i] for i in range(len(sampled_pairs))]

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
            local_eff = nx.local_efficiency(G)
            efficiency['local_efficiency'] = local_eff
            efficiency['avg_local_efficiency'] = np.mean(list(local_eff.values())) if local_eff else None
        except:
            efficiency['local_efficiency'] = None
            efficiency['avg_local_efficiency'] = None

        return efficiency

    def _analyze_network_robustness(self, G, attack_fraction=0.1):
        """Analyze network robustness to node/edge removal"""

        robustness = {}

        # Get original largest component size
        if nx.is_directed(G):
            original_lcc_size = len(max(nx.weakly_connected_components(G), key=len)) if not nx.is_weakly_connected(G) else G.number_of_nodes()
        else:
            original_lcc_size = len(max(nx.connected_components(G), key=len)) if not nx.is_connected(G) else G.number_of_nodes()

        # Random node removal
        num_nodes_to_remove = int(G.number_of_nodes() * attack_fraction)
        random_nodes = np.random.choice(list(G.nodes()), min(num_nodes_to_remove, G.number_of_nodes()), replace=False)

        G_random = G.copy()
        G_random.remove_nodes_from(random_nodes)

        if G_random.number_of_nodes() > 0:
            if nx.is_directed(G_random):
                lcc_after_random = len(max(nx.weakly_connected_components(G_random), key=len)) if not nx.is_weakly_connected(G_random) else G_random.number_of_nodes()
            else:
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
            if nx.is_directed(G_targeted):
                lcc_after_targeted = len(max(nx.weakly_connected_components(G_targeted), key=len)) if not nx.is_weakly_connected(G_targeted) else G_targeted.number_of_nodes()
            else:
                lcc_after_targeted = len(max(nx.connected_components(G_targeted), key=len)) if not nx.is_connected(G_targeted) else G_targeted.number_of_nodes()
            robustness['targeted_attack_resilience'] = lcc_after_targeted / original_lcc_size
        else:
            robustness['targeted_attack_resilience'] = 0

        # Edge removal robustness
        if G.number_of_edges() > 0:
            num_edges_to_remove = int(G.number_of_edges() * attack_fraction)
            edges_list = list(G.edges())
            random_edges = [edges_list[i] for i in np.random.choice(len(edges_list), min(num_edges_to_remove, len(edges_list)), replace=False)]

            G_edge_removal = G.copy()
            G_edge_removal.remove_edges_from(random_edges)

            if nx.is_directed(G_edge_removal):
                lcc_after_edge_removal = len(max(nx.weakly_connected_components(G_edge_removal), key=len)) if not nx.is_weakly_connected(G_edge_removal) else G_edge_removal.number_of_nodes()
            else:
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

## Temporal Network Analysis

### TemporalNetworkAnalyzer Class

```python
import community as community_louvain
from networkx.algorithms import community

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
            print(f"Analyzing time point {t+1}/{time_points}")

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

## Variables

### Path Analysis Variables
- [SAMPLE_SIZE] - Sample size for path length calculations
- [CALCULATE_AVG_PATH_LENGTH] - Calculate average path length
- [CALCULATE_DIAMETER] - Calculate network diameter
- [CALCULATE_RADIUS] - Calculate network radius
- [CALCULATE_ECCENTRICITY] - Calculate eccentricity distribution
- [K_SHORTEST_PATHS] - Number of k-shortest paths to find
- [MAX_PATH_LENGTH] - Maximum path length to consider
- [DIAMETER_APPROXIMATION] - Use approximation for diameter
- [PATH_WEIGHT_ATTRIBUTE] - Attribute for weighted path calculations

### Connectivity Variables
- [ANALYZE_COMPONENTS] - Analyze connected components
- [FIND_ARTICULATION_POINTS] - Identify articulation points
- [FIND_BRIDGES] - Identify bridge edges
- [CALCULATE_CONNECTIVITY] - Calculate node/edge connectivity
- [CALCULATE_GLOBAL_EFFICIENCY] - Calculate global efficiency
- [CALCULATE_LOCAL_EFFICIENCY] - Calculate local efficiency

### Robustness Variables
- [ROBUSTNESS_ATTACK_FRACTION] - Fraction of nodes/edges to remove (default: 0.1)
- [TARGETED_ATTACK_STRATEGY] - Strategy for targeted attacks
- [TEST_EDGE_REMOVAL] - Test edge removal robustness
- [TRACK_COMPONENT_CHANGES] - Track component size changes
- [TRACK_PATH_CHANGES] - Track path length changes
- [MEASURE_FRAGMENTATION] - Measure network fragmentation

### Temporal Variables
- [TEMPORAL_DATA] - Whether temporal data is available
- [TEMPORAL_NETWORKS] - List of temporal network snapshots
- [NUM_TEMPORAL_SNAPSHOTS] - Number of temporal snapshots
- [TIME_AGGREGATION] - Method for aggregating temporal data
- [STABILITY_THRESHOLD] - Threshold for stability metrics
- [SNAPSHOT_INTERVAL] - Time interval between snapshots

## Usage Examples

### Example 1: Comprehensive Path Analysis
```
SAMPLE_SIZE: 1000
CALCULATE_AVG_PATH_LENGTH: True
CALCULATE_DIAMETER: True
CALCULATE_RADIUS: True
CALCULATE_ECCENTRICITY: True
```

### Example 2: Robustness Testing
```
ROBUSTNESS_ATTACK_FRACTION: 0.1
TARGETED_ATTACK_STRATEGY: "Remove highest degree nodes"
TEST_EDGE_REMOVAL: True
TRACK_COMPONENT_CHANGES: True
```

### Example 3: Temporal Evolution Analysis
```
TEMPORAL_DATA: True
NUM_TEMPORAL_SNAPSHOTS: 12
TIME_AGGREGATION: "monthly"
STABILITY_THRESHOLD: 0.7
```

## Best Practices

1. **Sample for Large Networks** - Use sampling for expensive path calculations on large networks
2. **Consider Disconnected Components** - Analyze largest component separately for meaningful metrics
3. **Test Multiple Attack Strategies** - Assess robustness under different failure scenarios
4. **Track Temporal Changes** - Monitor key metrics over time to detect significant changes
5. **Validate Efficiency Measures** - Ensure efficiency calculations are appropriate for network type
6. **Identify Critical Infrastructure** - Focus on articulation points and bridges for vulnerability
7. **Use Approximations Wisely** - Balance accuracy and computation time for diameter estimates
8. **Document Temporal Snapshots** - Clearly define time windows and aggregation methods
9. **Compare Stability Metrics** - Use multiple metrics to assess temporal stability
10. **Contextualize Results** - Interpret path and robustness metrics in domain context
