---
title: Advanced Network Visualization Template
category: data-analytics/Research Analytics
tags: ['data-analytics', 'visualization', 'network-analysis', 'graphs']
use_cases:
  - Create advanced network visualizations using force-directed layouts, hierarchical layouts, and interactive visualizations to communicate network insights effectively.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Advanced Network Visualization Template

## Purpose
Create advanced network visualizations using force-directed layouts, hierarchical layouts, and interactive visualizations to communicate network insights effectively.

## Quick Start

### For Data Scientists

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific create needs
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
- Create advanced network visualizations using force-directed layouts, hierarchical layouts, and interactive visualizations to communicate network insights effectively.
- Project-specific implementations
- Research and analysis workflows



## Template

- Network visualization showing communities with color coding

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

   - Hierarchical community structure

7. **Visualization Suite**

   - Multiple layout algorithms

   - Interactive network plots

   - Community and centrality visualizations

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

[Content truncated for length - see original for full details]


## Variables

[The template includes 400+ comprehensive variables covering all aspects of network analysis, organized by category...]

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
