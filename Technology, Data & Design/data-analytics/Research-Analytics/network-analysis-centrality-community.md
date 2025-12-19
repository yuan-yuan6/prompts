---
category: data-analytics
title: Network Analysis - Centrality & Community Detection
tags:
- research-analytics
- network-analysis
- centrality
- community-detection
use_cases:
- Identifying influential nodes in social networks
- Detecting communities and clusters in networks
- Finding bridge nodes connecting different groups
- Analyzing organizational or market structures
related_templates:
- data-analytics/Research-Analytics/network-analysis-data-preparation.md
- data-analytics/Research-Analytics/network-analysis-visualization.md
- data-analytics/Research-Analytics/network-analysis-overview.md
industries:
- technology
- finance
- healthcare
- social-media
- research
type: framework
difficulty: intermediate
slug: network-analysis-centrality-community
---

# Network Analysis - Centrality & Community Detection

## Purpose
Identify important nodes and discover community structures in networks. This framework covers centrality measures to find influential actors, community detection algorithms to reveal group structures, and quality metrics to validate findings.

## Quick Start Prompt

> Analyze **[NETWORK TYPE]** with **[N nodes, M edges]**. Help me: (1) **Centrality**—which nodes are most influential? Calculate degree, betweenness, closeness, and PageRank. Who are the top 10? (2) **Communities**—what groups exist? Apply Louvain algorithm, evaluate modularity. How many communities? What characterizes each? (3) **Bridge nodes**—who connects different communities? (4) **Interpretation**—what do these patterns mean for the domain? Provide: ranked influencer list, community summary, and actionable insights.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid network analysis.

---

## Template

Analyze centrality and community structure for {NETWORK_DESCRIPTION} containing {NETWORK_SIZE} to support {ANALYSIS_OBJECTIVE}.

Conduct analysis across six dimensions:

**1. CENTRALITY ANALYSIS**

Identify important nodes using multiple measures:

Degree centrality: Count direct connections. High degree nodes are hubs with many relationships. In social networks, these are popular individuals. In citation networks, highly cited papers. Simple but foundational—reveals who has the most direct influence or visibility.

Betweenness centrality: Measure how often a node lies on shortest paths between others. High betweenness nodes are brokers or bridges—they control information flow. Remove them and the network fragments. Critical for identifying gatekeepers, bottlenecks, or key intermediaries.

Closeness centrality: Calculate average distance to all other nodes. High closeness means quick access to everyone—efficient spreaders of information. In communication networks, these nodes can reach the whole network fastest. Important for diffusion and reach analysis.

Eigenvector centrality: Weight connections by importance of neighbors. Being connected to important nodes makes you important. Captures influence that propagates—a node connected to five highly central nodes outranks one connected to five peripheral nodes.

PageRank: Google's algorithm adapted for general networks. Similar to eigenvector centrality but handles directed networks and damping. Robust measure of overall importance considering both quantity and quality of incoming links.

Correlation analysis: Compare centrality measures. Strong correlations suggest redundancy—one measure captures what others do. Weak correlations reveal different types of importance. A node high on betweenness but low on degree is a critical bridge despite few connections.

**2. CENTRALITY DISTRIBUTION**

Analyze how centrality is distributed across nodes:

Power law testing: Many real networks show highly skewed centrality distributions—few nodes have high centrality, most have low. Test for power law distribution. If present, the network has clear hubs and a long tail of peripheral nodes.

Concentration ratio: Calculate what fraction of total centrality the top 10% of nodes hold. High concentration (above 50%) indicates a hierarchical network with dominant players. Low concentration suggests more egalitarian structure.

Outlier identification: Find nodes with unusually high or low centrality. Extremely high centrality nodes are critical—their removal significantly impacts network structure. Unusually low centrality in otherwise connected networks may indicate isolation or measurement issues.

Stability assessment: For dynamic networks, track how centrality rankings change over time. Stable rankings indicate persistent influence structures. High volatility suggests a competitive or evolving landscape.

**3. COMMUNITY DETECTION**

Discover group structures within the network:

Louvain algorithm: Optimize modularity through iterative node reassignment. Fast, scalable, and produces good results on most networks. Start here for initial community structure. Works well on networks up to millions of nodes.

Label propagation: Nodes adopt the most common label among neighbors. Very fast but less deterministic—run multiple times and check consistency. Good for quick exploration or very large networks where Louvain is slow.

Girvan-Newman: Remove edges with highest betweenness iteratively, creating a dendrogram of splits. Computationally expensive but reveals hierarchical structure. Best for smaller networks where you want to understand the splitting process.

Spectral clustering: Use eigenvectors of the graph Laplacian to embed nodes in space, then cluster. Good when you have a target number of communities. Handles various community shapes that modularity optimization might miss.

Algorithm comparison: Different algorithms find different communities. Run multiple methods and compare results. High agreement suggests robust community structure. Disagreement may indicate overlapping communities, fuzzy boundaries, or noise.

**4. COMMUNITY QUALITY**

Evaluate the quality of detected communities:

Modularity score: Measures how much more densely connected communities are internally versus random expectation. Scores above 0.3 indicate meaningful community structure. Above 0.7 is very strong structure. Below 0.3 suggests weak or no natural communities.

Coverage: Fraction of edges that fall within communities. High coverage means most connections are within-group. Low coverage with high modularity indicates sparse but distinct communities.

Conductance: For each community, ratio of external to total edges. Low conductance means well-separated communities. High conductance indicates porous boundaries with many cross-community connections.

Internal density: Edge density within each community. Compare to overall network density. Communities should be denser than the network average. Much higher density confirms tight-knit groups.

Size distribution: Examine community sizes. Highly unequal sizes (one giant community, many tiny ones) may indicate resolution issues. Very uniform sizes might be artificial. Natural networks often show log-normal size distributions.

**5. STRUCTURAL PATTERNS**

Identify key structural roles and patterns:

Bridge identification: Find nodes with high betweenness that connect different communities. These bridges enable cross-community communication. Their removal would isolate groups. Critical for understanding information flow and network resilience.

Community hubs: Identify the most central node within each community. These are local leaders or representatives. Compare their global centrality to understand which communities are more influential network-wide.

Boundary spanners: Find nodes with connections to multiple communities. Different from bridges—they maintain membership in one community while reaching others. Important for innovation and knowledge transfer.

Core-periphery structure: Within each community, identify core members (densely connected to each other) versus periphery (connected to core but not each other). Reveals internal hierarchy and engagement levels.

Isolated components: Check for disconnected parts of the network. Small isolates may be measurement artifacts or genuinely separate groups. Large components warrant separate analysis.

**6. INTERPRETATION AND IMPLICATIONS**

Translate findings into actionable insights:

Influence strategy: Based on centrality analysis, who should be targeted for maximum network impact? For information diffusion, target high closeness. For brokerage, engage high betweenness nodes. For prestige association, connect to high eigenvector nodes.

Community characterization: Profile each community by member attributes, internal structure, and external connections. What makes each community distinct? Are they geographic, topical, demographic, or functional groupings?

Vulnerability assessment: Where is the network fragile? Removal of high betweenness bridges could fragment the network. Communities connected by single bridges are at risk. Identify redundancy and resilience.

Intervention design: For network interventions (marketing, public health, organizational change), how should communities be approached? Seed different communities simultaneously? Target community hubs first? Use bridges to spread across boundaries?

Deliver your analysis as:

1. **TOP INFLUENCERS** - Ranked list with centrality scores, role characterization (hub, bridge, authority)

2. **CENTRALITY SUMMARY** - Distribution statistics, correlation matrix, power law assessment

3. **COMMUNITY MAP** - Number of communities, sizes, modularity score, key characteristics

4. **QUALITY METRICS** - Modularity, coverage, conductance by community, algorithm agreement

5. **STRUCTURAL ROLES** - Bridges, community hubs, boundary spanners, core-periphery patterns

6. **ACTIONABLE INSIGHTS** - Implications for influence, vulnerability, intervention strategy

Use this quality scale for community structure:
- Modularity < 0.3: Weak or no community structure
- Modularity 0.3-0.5: Moderate community structure
- Modularity 0.5-0.7: Strong community structure
- Modularity > 0.7: Very strong, distinct communities

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{NETWORK_DESCRIPTION}` | Type and context of network | "Twitter retweet network during election", "company email communication network", "protein interaction network" |
| `{NETWORK_SIZE}` | Scale of the network | "10,000 users and 45,000 connections", "500 employees with 3,200 email exchanges", "2,000 proteins with 8,500 interactions" |
| `{ANALYSIS_OBJECTIVE}` | What decisions or understanding you seek | "identify key influencers for marketing campaign", "understand organizational silos", "find functional protein modules" |

## Usage Examples

### Example 1: Social Media Influencer Analysis

```
Analyze centrality and community structure for Twitter follower network 
during product launch containing 50,000 users and 180,000 follow relationships 
to identify key influencers for seeding viral marketing campaign.
```

**Expected Output:**
- Top 10 influencers: Mix of celebrities (high degree), industry experts (high eigenvector), and connectors (high betweenness)
- Centrality: Power law distribution, top 1% holds 40% of total degree centrality
- Communities: 12 communities detected (modularity=0.62)—tech enthusiasts, lifestyle bloggers, news amplifiers, brand advocates, etc.
- Key bridges: 15 accounts connect 3+ communities, critical for cross-community spread
- Recommendation: Seed campaign with 2 hubs per community plus 5 key bridges for maximum reach

### Example 2: Organizational Network Analysis

```
Analyze centrality and community structure for corporate email network 
containing 800 employees and 12,000 monthly email exchanges to understand 
informal influence structures and departmental silos.
```

**Expected Output:**
- Top influencers: Several non-managers rank highly on betweenness (informal connectors)
- Communities: 8 communities—roughly align with departments but 2 cross-functional groups emerge
- Silos: Engineering and Legal show low inter-community connectivity (conductance=0.08)
- Bridges: 12 employees connect multiple departments, mostly in product management
- Recommendation: Strengthen cross-departmental connections through bridge employees; address Legal isolation

### Example 3: Research Collaboration Network

```
Analyze centrality and community structure for academic co-authorship network 
containing 2,500 researchers and 6,000 collaboration links to identify 
research clusters and interdisciplinary bridge researchers.
```

**Expected Output:**
- Top influencers: Senior researchers dominate degree centrality; mid-career researchers high on betweenness
- Communities: 18 communities mapping to research subfields (modularity=0.71)
- Interdisciplinary bridges: 23 researchers connect 3+ subfields—candidates for collaboration grants
- Emerging clusters: 2 communities show high internal growth rate—emerging research areas
- Recommendation: Support bridge researchers with interdisciplinary funding; monitor emerging clusters

## Cross-References

- **Data Preparation:** network-analysis-data-preparation.md - Preparing network data for analysis
- **Visualization:** network-analysis-visualization.md - Visualizing centrality and communities
- **Overview:** network-analysis-overview.md - Network analysis fundamentals
- **Paths & Temporal:** network-analysis-paths-temporal.md - Path analysis and temporal dynamics
