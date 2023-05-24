import networkx as nx
import matplotlib.pyplot as plt

def find_minimum_weight_edge(graph, subgraph1, subgraph2):
    # Get the edges connecting the two subgraphs
    boundary_edges = [
        (u, v, data['weight'])
        for u, v, data in graph.edges(data=True)
        if (u in subgraph1.nodes and v in subgraph2.nodes) or (v in subgraph1.nodes and u in subgraph2.nodes)
    ]
    # Sort the boundary edges by weight
    sorted_edges = sorted(boundary_edges, key=lambda x: x[2])
    # Return the minimum weight edge and its weight
    if sorted_edges:
        return sorted_edges[0][:3][2]
    else:
        return None

def largest_weight_in_minimum_spanning_tree(subgraph):
    # Compute the minimum spanning tree of the subgraph
    mst = nx.minimum_spanning_tree(subgraph)

    # Get the weights of the edges in the minimum spanning tree
    weights = [data['weight'] for _, _, data in mst.edges(data=True)]

    # Return the largest weight
    if weights:
        return max(weights)
    else:
        return 0

# funcion MInt(C1 , C2)
def mint(c1, c2, cnst):
    return round(min(largest_weight_in_minimum_spanning_tree(c1) + taf(c1, cnst), largest_weight_in_minimum_spanning_tree(c2) + taf(c2, cnst)), 4)

def taf(c, cnst):
    return round(cnst/len(c), 4)





