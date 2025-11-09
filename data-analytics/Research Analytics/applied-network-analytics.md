---
title: Applied Network Analytics and Use Cases
category: data-analytics/Research Analytics
tags: [data-analytics, network-analysis, applications, use-cases, domain-specific]
use_cases:
  - Applying network analysis to specific domains
  - Social network analysis and influence mapping
  - Biological network analysis
  - Infrastructure and transportation networks
  - Financial and economic network analysis
related_templates:
  - network-analysis-overview.md
  - network-centrality-measures.md
  - network-community-detection.md
  - temporal-network-analysis.md
last_updated: 2025-11-09
---

# Applied Network Analytics and Use Cases

## Purpose
Apply network analysis techniques to real-world problems across different domains. Understand domain-specific network characteristics, select appropriate methods for each application, and derive actionable insights from network data.

## Domain-Specific Applications

### 1. SOCIAL NETWORK ANALYSIS

#### Use Case: Identifying Influencers and Information Flow

```python
import networkx as nx
import pandas as pd
import numpy as np
from collections import Counter

class SocialNetworkAnalyzer:
    def __init__(self, network):
        self.network = network

    def identify_influencers(self, top_k=20):
        """Identify key influencers using multiple centrality measures"""

        G = self.network

        # Calculate multiple centrality measures
        centralities = {
            'degree': nx.degree_centrality(G),
            'betweenness': nx.betweenness_centrality(G),
            'eigenvector': nx.eigenvector_centrality(G, max_iter=1000),
            'pagerank': nx.pagerank(G)
        }

        # Create combined influence score
        influence_scores = {}
        for node in G.nodes():
            score = (
                0.3 * centralities['degree'].get(node, 0) +
                0.3 * centralities['betweenness'].get(node, 0) +
                0.2 * centralities['eigenvector'].get(node, 0) +
                0.2 * centralities['pagerank'].get(node, 0)
            )
            influence_scores[node] = score

        # Identify top influencers
        top_influencers = sorted(
            influence_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )[:top_k]

        return {
            'influencers': top_influencers,
            'centrality_scores': centralities,
            'combined_scores': influence_scores
        }

    def detect_echo_chambers(self):
        """Detect echo chambers and filter bubbles"""

        G = self.network

        # Detect communities
        import community as community_louvain
        partition = community_louvain.best_partition(G)

        # Analyze homophily within communities
        communities = {}
        for node, comm_id in partition.items():
            if comm_id not in communities:
                communities[comm_id] = []
            communities[comm_id].append(node)

        # Calculate echo chamber metrics
        echo_chamber_metrics = []
        for comm_id, members in communities.items():
            subG = G.subgraph(members)

            # Internal vs external edges
            internal_edges = subG.number_of_edges()
            external_edges = sum(
                1 for node in members
                for neighbor in G.neighbors(node)
                if neighbor not in members
            )

            # Echo chamber score (higher = more isolated)
            total_edges = internal_edges + external_edges
            echo_score = internal_edges / total_edges if total_edges > 0 else 0

            echo_chamber_metrics.append({
                'community_id': comm_id,
                'size': len(members),
                'internal_edges': internal_edges,
                'external_edges': external_edges,
                'echo_chamber_score': echo_score
            })

        return pd.DataFrame(echo_chamber_metrics)

    def analyze_information_cascade(self, seed_nodes, steps=5):
        """Simulate information cascade from seed nodes"""

        G = self.network
        activated = set(seed_nodes)
        cascade_data = {0: list(seed_nodes)}

        for step in range(1, steps + 1):
            new_activated = set()

            for node in activated:
                neighbors = set(G.neighbors(node))
                new_activated.update(neighbors - activated)

            activated.update(new_activated)
            cascade_data[step] = list(new_activated)

            if not new_activated:
                break

        # Calculate reach metrics
        total_reach = len(activated)
        reach_percentage = (total_reach / G.number_of_nodes()) * 100

        return {
            'cascade_by_step': cascade_data,
            'total_reach': total_reach,
            'reach_percentage': reach_percentage,
            'steps_to_saturate': step
        }

# Example: Social Network Analysis
social_network = nx.read_edgelist('[SOCIAL_NETWORK_DATA]')
social_analyzer = SocialNetworkAnalyzer(social_network)

# Identify influencers
influencers = social_analyzer.identify_influencers(top_k=20)

# Detect echo chambers
echo_chambers = social_analyzer.detect_echo_chambers()

# Simulate information cascade
cascade = social_analyzer.analyze_information_cascade(
    seed_nodes=['influential_user_1', 'influential_user_2'],
    steps=5
)
```

### 2. BIOLOGICAL NETWORK ANALYSIS

#### Use Case: Protein-Protein Interaction Networks

```python
class BiologicalNetworkAnalyzer:
    def __init__(self, network, node_attributes=None):
        self.network = network
        self.node_attributes = node_attributes

    def identify_protein_complexes(self):
        """Identify protein complexes using community detection"""

        G = self.network

        # Use multiple community detection methods
        import community as community_louvain

        # Louvain for modularity
        partition = community_louvain.best_partition(G)

        # Convert to protein complexes
        complexes = {}
        for protein, complex_id in partition.items():
            if complex_id not in complexes:
                complexes[complex_id] = []
            complexes[complex_id].append(protein)

        # Filter small complexes
        significant_complexes = {
            k: v for k, v in complexes.items()
            if len(v) >= 3  # Minimum size for protein complex
        }

        return significant_complexes

    def find_disease_genes(self, known_disease_genes):
        """Find candidate disease genes based on network proximity"""

        G = self.network

        # Calculate centrality for known disease genes
        disease_subgraph = G.subgraph(known_disease_genes)

        # Find genes closely connected to disease genes
        candidate_genes = {}

        for gene in G.nodes():
            if gene not in known_disease_genes:
                # Calculate proximity to disease genes
                proximity_score = 0
                for disease_gene in known_disease_genes:
                    if nx.has_path(G, gene, disease_gene):
                        distance = nx.shortest_path_length(G, gene, disease_gene)
                        proximity_score += 1 / (distance + 1)

                candidate_genes[gene] = proximity_score

        # Rank candidates
        ranked_candidates = sorted(
            candidate_genes.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked_candidates[:50]  # Top 50 candidates

    def analyze_functional_modules(self):
        """Identify functional modules and pathways"""

        G = self.network

        # Detect modules using community detection
        from networkx.algorithms import community

        communities = community.greedy_modularity_communities(G)

        # Analyze each module
        modules_analysis = []

        for i, module in enumerate(communities):
            subG = G.subgraph(module)

            # Module properties
            module_info = {
                'module_id': i,
                'size': len(module),
                'density': nx.density(subG),
                'avg_clustering': nx.average_clustering(subG),
                'members': list(module)
            }

            modules_analysis.append(module_info)

        return modules_analysis

# Example: Protein Interaction Network
ppi_network = nx.read_edgelist('[PPI_NETWORK_DATA]')
bio_analyzer = BiologicalNetworkAnalyzer(ppi_network)

# Identify protein complexes
complexes = bio_analyzer.identify_protein_complexes()

# Find disease gene candidates
known_disease_genes = ['BRCA1', 'TP53', 'EGFR']
candidates = bio_analyzer.find_disease_genes(known_disease_genes)

# Analyze functional modules
modules = bio_analyzer.analyze_functional_modules()
```

### 3. TRANSPORTATION NETWORK ANALYSIS

#### Use Case: Traffic Flow and Route Optimization

```python
class TransportationNetworkAnalyzer:
    def __init__(self, network):
        self.network = network

    def identify_bottlenecks(self):
        """Identify traffic bottlenecks using betweenness centrality"""

        G = self.network

        # Edge betweenness centrality (identifies critical roads)
        edge_betweenness = nx.edge_betweenness_centrality(G, weight='travel_time')

        # Identify top bottlenecks
        bottlenecks = sorted(
            edge_betweenness.items(),
            key=lambda x: x[1],
            reverse=True
        )[:20]

        return bottlenecks

    def optimize_routes(self, source, target, k_paths=5):
        """Find k-shortest paths between locations"""

        G = self.network

        try:
            # Find k-shortest paths
            paths = list(nx.shortest_simple_paths(
                G, source, target, weight='travel_time'
            ))[:k_paths]

            # Calculate metrics for each path
            path_analysis = []
            for i, path in enumerate(paths):
                path_length = len(path) - 1
                travel_time = sum(
                    G[path[j]][path[j+1]]['travel_time']
                    for j in range(len(path)-1)
                )

                path_analysis.append({
                    'rank': i + 1,
                    'path': path,
                    'num_segments': path_length,
                    'total_travel_time': travel_time
                })

            return path_analysis

        except nx.NetworkXNoPath:
            return []

    def assess_network_resilience(self, attack_type='random', fraction=0.1):
        """Assess network resilience to disruptions"""

        G = self.network

        # Original connectivity
        original_components = nx.number_connected_components(G)
        original_lcc = len(max(nx.connected_components(G), key=len))

        # Simulate disruption
        num_nodes_remove = int(G.number_of_nodes() * fraction)

        if attack_type == 'random':
            nodes_to_remove = np.random.choice(
                list(G.nodes()),
                num_nodes_remove,
                replace=False
            )
        elif attack_type == 'targeted':
            # Remove highest betweenness nodes
            betweenness = nx.betweenness_centrality(G)
            nodes_to_remove = sorted(
                betweenness.items(),
                key=lambda x: x[1],
                reverse=True
            )[:num_nodes_remove]
            nodes_to_remove = [n for n, _ in nodes_to_remove]

        # Create disrupted network
        G_disrupted = G.copy()
        G_disrupted.remove_nodes_from(nodes_to_remove)

        # Assess impact
        disrupted_components = nx.number_connected_components(G_disrupted)
        disrupted_lcc = len(max(nx.connected_components(G_disrupted), key=len))

        resilience_score = disrupted_lcc / original_lcc

        return {
            'attack_type': attack_type,
            'nodes_removed': num_nodes_remove,
            'original_lcc': original_lcc,
            'disrupted_lcc': disrupted_lcc,
            'resilience_score': resilience_score,
            'connectivity_maintained': resilience_score > 0.8
        }

# Example: Transportation Network
traffic_network = nx.read_edgelist('[TRAFFIC_NETWORK_DATA]')
transport_analyzer = TransportationNetworkAnalyzer(traffic_network)

# Identify bottlenecks
bottlenecks = transport_analyzer.identify_bottlenecks()

# Find alternative routes
routes = transport_analyzer.optimize_routes(
    source='LocationA',
    target='LocationB',
    k_paths=5
)

# Assess resilience
resilience = transport_analyzer.assess_network_resilience(
    attack_type='targeted',
    fraction=0.1
)
```

### 4. FINANCIAL NETWORK ANALYSIS

#### Use Case: Systemic Risk and Contagion

```python
class FinancialNetworkAnalyzer:
    def __init__(self, network):
        self.network = network

    def identify_systemically_important_institutions(self):
        """Identify systemically important financial institutions"""

        G = self.network

        # Calculate multiple risk indicators
        centralities = {
            'degree': nx.degree_centrality(G),
            'betweenness': nx.betweenness_centrality(G),
            'eigenvector': nx.eigenvector_centrality(G, max_iter=1000),
            'closeness': nx.closeness_centrality(G)
        }

        # Combined systemic importance score
        systemic_scores = {}
        for node in G.nodes():
            score = (
                0.25 * centralities['degree'].get(node, 0) +
                0.35 * centralities['betweenness'].get(node, 0) +
                0.25 * centralities['eigenvector'].get(node, 0) +
                0.15 * centralities['closeness'].get(node, 0)
            )
            systemic_scores[node] = score

        # Rank institutions
        ranked_institutions = sorted(
            systemic_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked_institutions

    def simulate_contagion(self, failed_institution, threshold=0.3):
        """Simulate financial contagion from institution failure"""

        G = self.network
        failed = {failed_institution}
        contagion_steps = {0: [failed_institution]}

        # Get edge weights (exposure amounts)
        exposures = nx.get_edge_attributes(G, 'exposure')

        step = 0
        while True:
            step += 1
            new_failures = set()

            # Check each institution's exposure to failed institutions
            for node in G.nodes():
                if node not in failed:
                    # Calculate total exposure to failed institutions
                    total_exposure = 0
                    total_assets = G.nodes[node].get('assets', 1)

                    for failed_node in failed:
                        if G.has_edge(node, failed_node):
                            exposure = exposures.get((node, failed_node), 0)
                            total_exposure += exposure

                    # Check if exposure exceeds threshold
                    exposure_ratio = total_exposure / total_assets
                    if exposure_ratio > threshold:
                        new_failures.add(node)

            if not new_failures:
                break

            failed.update(new_failures)
            contagion_steps[step] = list(new_failures)

        return {
            'total_failures': len(failed),
            'failure_rate': len(failed) / G.number_of_nodes(),
            'contagion_steps': contagion_steps,
            'failed_institutions': list(failed)
        }

    def assess_network_stability(self):
        """Assess overall financial network stability"""

        G = self.network

        # Network structure metrics
        density = nx.density(G)
        clustering = nx.average_clustering(G)
        components = nx.number_connected_components(G)

        # Degree distribution (concentration risk)
        degrees = [d for n, d in G.degree()]
        degree_concentration = np.std(degrees) / (np.mean(degrees) + 1e-10)

        # Assortativity (do high-degree nodes connect to each other?)
        assortativity = nx.degree_assortativity_coefficient(G)

        return {
            'density': density,
            'clustering': clustering,
            'num_components': components,
            'degree_concentration': degree_concentration,
            'assortativity': assortativity,
            'stability_score': self._calculate_stability_score(
                density, clustering, degree_concentration, assortativity
            )
        }

    def _calculate_stability_score(self, density, clustering, concentration, assortativity):
        """Calculate overall stability score (0-1, higher is more stable)"""

        # Low density = less interconnected = more stable
        density_score = 1 - density

        # Moderate clustering is good
        clustering_score = 1 - abs(clustering - 0.3)

        # Low concentration = more diversified = more stable
        concentration_score = 1 / (1 + concentration)

        # Negative assortativity = less core-periphery = more stable
        assortativity_score = 1 - (assortativity + 1) / 2

        stability = (
            0.3 * density_score +
            0.2 * clustering_score +
            0.3 * concentration_score +
            0.2 * assortativity_score
        )

        return stability

# Example: Financial Network
financial_network = nx.read_edgelist('[FINANCIAL_NETWORK_DATA]')
financial_analyzer = FinancialNetworkAnalyzer(financial_network)

# Identify systemically important institutions
sifi = financial_analyzer.identify_systemically_important_institutions()

# Simulate contagion
contagion = financial_analyzer.simulate_contagion(
    failed_institution='Bank_A',
    threshold=0.3
)

# Assess stability
stability = financial_analyzer.assess_network_stability()
```

## Best Practices by Domain

### Social Networks
1. **Privacy and Ethics**
   - Anonymize sensitive data
   - Follow platform terms of service
   - Consider ethical implications

2. **Data Collection**
   - Account for sampling bias
   - Verify data authenticity
   - Handle missing connections

3. **Analysis Considerations**
   - Temporal dynamics are critical
   - Context matters for interpretation
   - Combine with content analysis

### Biological Networks
1. **Data Quality**
   - Validate experimental data
   - Account for false positives/negatives
   - Use confidence scores

2. **Integration**
   - Combine multiple data sources
   - Use functional annotations
   - Incorporate domain knowledge

3. **Validation**
   - Cross-reference with literature
   - Experimental validation
   - Statistical significance testing

### Transportation Networks
1. **Spatial Considerations**
   - Include geographic constraints
   - Account for real-world distances
   - Consider temporal patterns

2. **Dynamic Analysis**
   - Model time-varying traffic
   - Peak vs. off-peak analysis
   - Seasonal variations

3. **Optimization**
   - Multi-objective optimization
   - Trade-offs (time vs. distance)
   - Constraint satisfaction

### Financial Networks
1. **Risk Management**
   - Stress testing scenarios
   - Regulatory compliance
   - Real-time monitoring

2. **Data Handling**
   - High-frequency updates
   - Confidentiality requirements
   - Data validation

3. **Modeling**
   - Account for feedback loops
   - Non-linear dynamics
   - Tail risk assessment

## Common Pitfalls and Solutions

### Pitfall 1: Ignoring Network Boundaries
**Problem:** Incomplete network data
**Solution:**
- Acknowledge boundary effects
- Use boundary specification methods
- Consider sampling strategies

### Pitfall 2: Static Analysis of Dynamic Systems
**Problem:** Analyzing time-varying networks as static
**Solution:**
- Use temporal network methods
- Consider time windows
- Track evolution

### Pitfall 3: Over-interpreting Centrality
**Problem:** Assuming high centrality = importance
**Solution:**
- Use multiple centrality measures
- Validate with domain knowledge
- Consider context

### Pitfall 4: Ignoring Network Null Models
**Problem:** Not testing against random baselines
**Solution:**
- Generate appropriate null models
- Calculate statistical significance
- Report p-values

### Pitfall 5: Scalability Issues
**Problem:** Algorithms too slow for large networks
**Solution:**
- Use sampling methods
- Implement approximation algorithms
- Parallel computing

## Success Metrics by Domain

### Social Networks
- User engagement increase
- Information spread efficiency
- Community health metrics

### Biological Networks
- Novel pathway discovery
- Disease gene prediction accuracy
- Drug target identification

### Transportation Networks
- Reduced travel time
- Improved network resilience
- Bottleneck mitigation

### Financial Networks
- Risk reduction
- Contagion prevention
- Systemic stability improvement

## Variables

### Application-Specific Variables
- [SOCIAL_NETWORK_DATA] - Social network data source
- [PPI_NETWORK_DATA] - Protein interaction network data
- [TRAFFIC_NETWORK_DATA] - Transportation network data
- [FINANCIAL_NETWORK_DATA] - Financial network data
- [DOMAIN] - Application domain
- [USE_CASE] - Specific use case
- [ANALYSIS_GOALS] - Domain-specific goals
- [METRICS] - Domain-appropriate metrics
- [VALIDATION_APPROACH] - How to validate results

## Usage Examples

### Example 1: Social Network Influence Campaign
```
DOMAIN: "Social Media Marketing"
USE_CASE: "Identify influencers for product launch campaign"
ANALYSIS_GOALS: "Find 20 key influencers with high reach and engagement"
METRICS: "PageRank, betweenness centrality, community centrality"
VALIDATION_APPROACH: "Cross-reference with engagement metrics"
```

### Example 2: Disease Gene Discovery
```
DOMAIN: "Computational Biology"
USE_CASE: "Identify candidate genes for Alzheimer's disease"
ANALYSIS_GOALS: "Find proteins closely connected to known disease genes"
METRICS: "Network proximity, functional similarity"
VALIDATION_APPROACH: "Literature review, experimental validation"
```

### Example 3: Smart City Traffic Optimization
```
DOMAIN: "Urban Transportation"
USE_CASE: "Reduce traffic congestion in downtown area"
ANALYSIS_GOALS: "Identify bottlenecks and optimize traffic flow"
METRICS: "Betweenness centrality, flow efficiency, resilience"
VALIDATION_APPROACH: "Traffic simulation, pilot implementation"
```

### Example 4: Financial Systemic Risk
```
DOMAIN: "Financial Regulation"
USE_CASE: "Assess systemic risk in banking network"
ANALYSIS_GOALS: "Identify systemically important banks and contagion paths"
METRICS: "Systemic importance, contagion impact, network stability"
VALIDATION_APPROACH: "Stress testing, historical crisis analysis"
```
