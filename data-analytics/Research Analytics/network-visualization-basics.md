---
title: Network Visualization and Graph Theory Basics
category: data-analytics/Research Analytics
tags: [data-analytics, network-analysis, visualization, graph-theory, network-metrics]
use_cases:
  - Understanding fundamental graph theory concepts
  - Loading and preprocessing network data
  - Creating basic network visualizations
  - Analyzing degree distributions and network topology
related_templates:
  - network-analysis-overview.md
  - network-centrality-measures.md
  - network-community-detection.md
last_updated: 2025-11-09
---

# Network Visualization and Graph Theory Basics

## Purpose
Master fundamental graph theory concepts, learn to load and preprocess network data, create effective visualizations using multiple layout algorithms, and analyze basic network properties and topology.

## Template

```
You are a network visualization expert. Analyze [NETWORK_DATA_SOURCE] to create comprehensive visualizations and understand basic network structure using [LAYOUT_ALGORITHMS] with focus on [VISUALIZATION_GOALS].

NETWORK DATA:
- Data source: [DATA_SOURCE_TYPE] (Social/Biological/Transportation/Communication)
- Network type: [NETWORK_TYPE] (Directed/Undirected/Weighted/Bipartite)
- Scale: [NODE_COUNT] nodes, [EDGE_COUNT] edges
- Data format: [DATA_FORMAT] (Edge list/Adjacency matrix/GraphML/JSON)

ANALYSIS OBJECTIVES:
- Visualization goal: [PRIMARY_VISUALIZATION_GOAL]
- Layout preferences: [LAYOUT_ALGORITHM]
- Network properties: [BASIC_PROPERTIES_TO_ANALYZE]
- Degree analysis: [DEGREE_DISTRIBUTION_ANALYSIS]

### NETWORK DATA LOADING AND PREPROCESSING

```python
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict, Counter
import plotly.graph_objects as go

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
                edge_attr='[EDGE_ATTRIBUTES]' if '[EDGE_ATTRIBUTES]' else None,
                create_using=nx.DiGraph() if '[DIRECTED]' else nx.Graph()
            )

        elif data_type == 'adjacency_matrix':
            # Load adjacency matrix
            adj_matrix = pd.read_csv(data_source, index_col=0)
            G = nx.from_pandas_adjacency(
                adj_matrix,
                create_using=nx.DiGraph() if '[DIRECTED]' else nx.Graph()
            )

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
            cleaning_log.append(f"Removed {num_self_loops} self loops")

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
                    subnetworks[f'component_{i}'] = subG

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
                    subnetworks[f'ego_{node}'] = ego_G

        elif method == 'attribute_based':
            # Extract subnetworks based on node attributes
            attribute = kwargs.get('attribute')
            values = kwargs.get('values')

            if attribute and values:
                for value in values:
                    nodes = [n for n, d in G.nodes(data=True) if d.get(attribute) == value]
                    if len(nodes) >= kwargs.get('min_size', 3):
                        subG = G.subgraph(nodes).copy()
                        subnetworks[f'{attribute}_{value}'] = subG

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

# Initialize and load network
preprocessor = NetworkPreprocessor()
network = preprocessor.load_network_data('[DATA_SOURCE]', '[DATA_TYPE]')
cleaned_network, cleaning_log = preprocessor.clean_network(
    remove_self_loops=[REMOVE_SELF_LOOPS],
    remove_isolated=[REMOVE_ISOLATED],
    min_degree=[MIN_DEGREE]
)
```

### NETWORK VALIDATION AND BASIC PROPERTIES

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

        # Network density and sparsity
        validation['density_metrics'] = {
            'density': nx.density(G),
            'is_sparse': nx.density(G) < 0.1,
            'is_dense': nx.density(G) > 0.5
        }

        self.validation_results = validation
        return validation

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

        return "\n".join(report)

# Validate network
validator = NetworkValidator(network)
validation_results = validator.comprehensive_validation()
validation_report = validator.generate_validation_report()
print(validation_report)
```

### NETWORK VISUALIZATION

```python
class NetworkVisualizer:
    def __init__(self, network):
        self.network = network
        self.layouts = {}
        self.figures = {}

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

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )

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
            node_text.append(
                f'Node: {node}<br>Degree: {len(adjacencies)}<br>' +
                f'Neighbors: {", ".join(map(str, adjacencies[:5]))}'
            )
            node_colors.append(len(adjacencies))

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            text=node_text,
            marker=dict(
                showscale=True,
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
                line_width=2
            )
        )

        # Create figure
        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title='Interactive Network Visualization',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                plot_bgcolor='white'
            )
        )

        return fig

# Create visualizations
visualizer = NetworkVisualizer(network)

# Basic network plots with different layouts
spring_plot = visualizer.create_basic_network_plot(layout='spring')
circular_plot = visualizer.create_basic_network_plot(layout='circular')
kamada_plot = visualizer.create_basic_network_plot(layout='kamada_kawai')

# Degree distribution analysis
degree_dist_plot = visualizer.plot_degree_distribution()

# Interactive visualization
interactive_plot = visualizer.create_interactive_network()
interactive_plot.show()
```

OUTPUT REQUIREMENTS:
Deliver comprehensive network visualization including:

1. **Network Data Loading**
   - Successfully loaded network from [DATA_FORMAT]
   - Network size: [NODE_COUNT] nodes, [EDGE_COUNT] edges
   - Network type: [NETWORK_TYPE]
   - Data quality assessment

2. **Basic Network Properties**
   - Density: [NETWORK_DENSITY]
   - Connectivity: [CONNECTIVITY_STATUS]
   - Degree statistics: mean, median, max, min
   - Component analysis

3. **Visualizations Created**
   - Multiple layout comparisons (spring, circular, spectral)
   - Degree distribution plots (histogram, log-log, cumulative)
   - Interactive network visualization
   - Node and edge attribute visualizations

4. **Key Findings**
   - Network topology type (scale-free, small-world, random, etc.)
   - Degree distribution characteristics
   - Connectivity patterns
   - Structural insights
```

## Variables

### Data Source Variables
- [NETWORK_DATA_SOURCE] - Source of network data
- [DATA_SOURCE_TYPE] - Type of network data source
- [DATA_FORMAT] - Format of input data (Edge list/Adjacency matrix/GraphML/JSON)
- [SOURCE_COLUMN] - Source node column name in edge list
- [TARGET_COLUMN] - Target node column name in edge list
- [DATA_TYPE] - Type of data format to load

### Network Type Variables
- [NETWORK_TYPE] - Type of network (Directed/Undirected/Weighted/Bipartite)
- [DIRECTED] - Whether the network is directed (True/False)
- [WEIGHTED] - Whether edges have weights (True/False)
- [NODE_COUNT] - Number of nodes in network
- [EDGE_COUNT] - Number of edges in network

### Preprocessing Variables
- [REMOVE_SELF_LOOPS] - Remove self-loops (True/False)
- [REMOVE_ISOLATED] - Remove isolated nodes (True/False)
- [MIN_DEGREE] - Minimum degree threshold for filtering
- [MAX_DEGREE] - Maximum degree threshold for filtering
- [EDGE_ATTRIBUTES] - Edge attributes to include
- [NODE_ATTRIBUTES] - Node attributes to include

### Visualization Variables
- [LAYOUT_ALGORITHM] - Layout algorithm to use (spring/circular/kamada_kawai/spectral)
- [LAYOUT_ALGORITHMS] - Multiple layouts to compare
- [VISUALIZATION_GOALS] - Primary visualization objectives
- [PRIMARY_VISUALIZATION_GOAL] - Main visualization goal
- [FIGURE_SIZE] - Size of figures (default: (12, 8))
- [NODE_SIZE_ATTRIBUTE] - Attribute for sizing nodes
- [NODE_COLOR_ATTRIBUTE] - Attribute for coloring nodes

### Analysis Variables
- [BASIC_PROPERTIES_TO_ANALYZE] - Which basic properties to focus on
- [DEGREE_DISTRIBUTION_ANALYSIS] - Degree distribution analysis requirements
- [NETWORK_DENSITY] - Calculated network density
- [CONNECTIVITY_STATUS] - Network connectivity status

## Best Practices

1. **Data Loading**
   - Always validate data format before loading
   - Check for duplicate edges and self-loops
   - Verify node IDs are consistent

2. **Preprocessing**
   - Document all cleaning steps
   - Keep original data unchanged
   - Record filtering decisions and rationale

3. **Visualization**
   - Use appropriate layout for network size and structure
   - Spring layout: Good for most networks
   - Circular layout: Highlights symmetry
   - Hierarchical layout: For tree structures
   - Spectral layout: For community structure

4. **Degree Distribution**
   - Always check log-log plot for power-law behavior
   - Compare with theoretical distributions
   - Report both in-degree and out-degree for directed networks

5. **Interactive Plots**
   - Essential for large networks (> 100 nodes)
   - Enable zooming and panning
   - Include informative hover text
   - Limit to reasonable size for performance

## Usage Example

```
NETWORK_DATA_SOURCE: "social_media_connections.csv"
DATA_FORMAT: "Edge list"
NETWORK_TYPE: "Undirected, unweighted"
LAYOUT_ALGORITHM: "spring"
PRIMARY_VISUALIZATION_GOAL: "Understand overall network structure and identify hubs"
BASIC_PROPERTIES_TO_ANALYZE: "Density, connectivity, degree distribution"
```
