import numpy as np
import cv2
import matplotlib.pyplot as plt
import networkx as nx

# functions visualize_graph and visualize_weighted_graph are used foe debugging must called only with small images up to 10x10 pixels
def visualize_graph(graph):
    plt.figure(figsize=(8, 8))
    pos = {k: k for k in graph.nodes()}
    nx.draw_networkx(graph, pos=pos, node_size=10, node_color='b')
    plt.axis('off')
    plt.show()

def visualize_weighted_graph(graph):
    plt.figure(figsize=(50, 50))
    pos = {k: k for k in graph.nodes()}
    nx.draw_networkx(graph, pos=pos, node_size=10, node_color='b')
    
    # Print the weights of the edges
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels)
    
    plt.axis('off')
    plt.show()

def visualize_segments(pixel_lists):
    # Determine the number of pixel lists
    num_lists = len(pixel_lists)
    
    # Define the size of the image
    width = 200
    height = 400

    # Create a new blank image with white background
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Assign a unique color for each pixel list
    colors = [tuple(np.random.randint(0, 256, size=3, dtype=np.uint8)) for _ in range(num_lists)]

    # Draw the pixels on the image using their respective colors
    for i, pixel_list in enumerate(pixel_lists):
        color = colors[i]
        for pixel in pixel_list:
            x, y = pixel
            #image[y, x] = color
            image[x, y] = color

    # Display the composed image
    cv2.imshow('Composed Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return image
