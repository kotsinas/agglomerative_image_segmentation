from rgb_vectors import *
from diff_mst import *
from visualization import *
import time


class Cluster:
    def __init__(self, id):
        self.id = id
        self.nodes = []
        self.edges = []

    def add_node_to_cluster(self, node):
        self.nodes.append(node)

    def merge(self, cluster):
        self.nodes = list(set(self.nodes + cluster.nodes))

start_time = time.time()

# neighbor parameter        
neighbor_hops = 1
# standard deviation
s = 5
# parameter k of the function τ(C)
k = 200

# graph creation
graph = image_to_graph('church.jpg')
graph = add_edges(graph, neighbor_hops)
graph = calculate_edge_weights(graph, s)
#visualize_weighted_graph(graph)

clusters = []
count = 1
# initial clusters (one per pixel)
for node in graph:
    cluster = Cluster(count)
    count = count+1
    cluster.add_node_to_cluster(node)
    clusters.append(cluster)
    #print(cluster.id, cluster.nodes)



sorted_edges = sort_edges_by_weight(graph)
for edge in sorted_edges:
    flag = 1

    # if edge lies inside cluster do nothing
    for cluster in clusters:
        if edge[0] in cluster.nodes and edge[1] in cluster.nodes:
            flag = 0
    if flag == 0:
        pass
    # else merge
    else:        
        # Find the instances of the two clusters
        cluster1 = next((cluster for cluster in clusters if edge[0] in cluster.nodes), None)
        cluster2 = next((cluster for cluster in clusters if edge[1] in cluster.nodes), None)
        #print("cluster1 =",cluster1.id,"cluster2 =",cluster2.id)
        
        # Check if both clusters exist
        if cluster1 and cluster2:

            subgraph1 = graph.subgraph(cluster1.nodes)
            subgraph2 = graph.subgraph(cluster2.nodes)

            if find_minimum_weight_edge(graph, subgraph1, subgraph2)<= mint(subgraph1, subgraph2, k):
                # Merge the clusters
                cluster1.merge(cluster2)
                # Remove the second cluster from the list
                clusters.remove(cluster2)


segments = []
for cl in clusters:
    segments.append(cl.nodes)
    #print(cl.id, cl.nodes)
    #print("+++++++++++++++++++")


outcome_img = visualize_segments(segments)
cv2.imwrite('seg_church_s5_n1_k200.jpg', outcome_img)

end_time = time.time()
execution_time = end_time - start_time

print("Execution time:", round(execution_time, 4), "seconds")