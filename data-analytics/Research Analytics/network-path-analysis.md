---
title: Network Path & Connectivity Analysis Template
category: data-analytics/Research Analytics
tags: ['data-analytics', 'network-analysis', 'path-analysis', 'topology']
use_cases:
  - Analyze network paths, connectivity, and information flow using shortest path algorithms, network diameter, and reachability analysis to understand network topology.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Network Path & Connectivity Analysis Template

## Purpose
Analyze network paths, connectivity, and information flow using shortest path algorithms, network diameter, and reachability analysis to understand network topology.

## Quick Start

### For Data Scientists

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific analyze needs
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
- Analyze network paths, connectivity, and information flow using shortest path algorithms, network diameter, and reachability analysis to understand network topology.
- Project-specific implementations
- Research and analysis workflows



## Template

   - Measure average path length and network diameter

   - Find critical paths for information spread

- Network metrics dashboard: Density, clustering coefficient, avg path length, diameter

- Risk analysis: Impact of losing key influencers on network connectivity
```


- Path analysis: [PATH_ANALYSIS]

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

[Content truncated for length - see original for full details]


## Variables

[The template includes 400+ comprehensive variables covering all aspects of network analysis, organized by category...]

## Usage Examples

### Example 2: Collaboration Network
```
NETWORK_DATA_SOURCE: "Scientific collaboration network from publications"
NETWORK_TYPE: "Undirected, weighted by collaboration frequency"
RESEARCH_QUESTIONS: "How do research communities form and evolve?"
TEMPORAL_ANALYSIS: "Track collaboration patterns over decades"
PATH_ANALYSIS: "Analyze knowledge transfer paths"
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
