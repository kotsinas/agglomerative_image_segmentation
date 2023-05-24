import cv2
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math

def convert_uint8_to_int64(array):
    return array.astype(np.int64)

def image_to_graph(image_path):
    # Read the image 
    image = cv2.imread(image_path)

    # Get the image shape
    rows, cols, _ = image.shape

    # Create a graph with a node for each pixel in the image
    graph = nx.grid_2d_graph(rows, cols)

    # Set the value of each node to the RGB value of the corresponding pixel
    for i in range(rows):
        for j in range(cols):
            node_id = (i, j)
            node_value = tuple(image[i, j])
            graph.nodes[node_id]['value'] = node_value

    # Add the 'rows' and 'cols' attributes to the graph
    graph.graph['rows'] = rows
    graph.graph['cols'] = cols

    return graph

def add_edges(graph, k):
    # Get the rows and cols from the graph attributes
    rows = graph.graph['rows']
    cols = graph.graph['cols']

    # Iterate over the nodes
    for node_id in graph.nodes():
        # Get the coordinates of the current node
        i, j = node_id

        # Iterate over the neighbors
        for ni in range(i-k, i+k+1):
            for nj in range(j-k, j+k+1):
                # Check if the neighbor is within the image bounds
                if 0 <= ni < rows and 0 <= nj < cols:
                    # Don't add edges from a node to itself
                    if node_id != (ni, nj):
                        # Check if the nodes are already connected
                        if not graph.has_edge(node_id, (ni, nj)):
                            # Add an edge between the nodes
                            graph.add_edge(node_id, (ni, nj))

    return graph

def calculate_edge_weights(graph, s):
    # Iterate over all edges in the graph
    for u, v in graph.edges():
        # Get the RGB vectors of the connected nodes
        rgb_u = np.array(graph.nodes[u].get('value'))
        rgb_v = np.array(graph.nodes[v].get('value'))
        rgb_u = convert_uint8_to_int64(rgb_u)
        rgb_v = convert_uint8_to_int64(rgb_v)
 
        if rgb_u is not None and rgb_v is not None:
            distance = np.linalg.norm(rgb_u - rgb_v)
            weight = 1/(2*s**2)
            weight = distance*weight
            weight = math.exp(weight)
            weight = round(weight, 4)
            graph[u][v]['weight'] = weight
            #print(f"Distance between nodes {u} and {v}: {weight}")
                
        # Assign 'cluster' attribute
        #graph[u][v]['cluster'] = None

    return graph

def sort_edges_by_weight(graph):
    edges = graph.edges(data=True)  # Get the list of edges with their weights
    sorted_edges = sorted(edges, key=lambda x: x[2]['weight'])  # Sort the edges by weight
    return sorted_edges





