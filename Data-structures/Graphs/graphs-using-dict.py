# IMPLEMENTING GRAPH DATA STRUCTURE USING DICTIONARIES

from collections import defaultdict 

# Note that the keys in the dict are the nodes in the graph while the
# values represent are just a list of the nodes connected with the edge
graphOne = defaultdict(list) 

# Function for generating edges on the graph
def generate_edges(graph): 
    edges = [] 
    for node in graph: 
        for neighbor in graph[node]: 
            edges.append((node, neighbor))
    return edges


# Function for adding the edges of the graph

def addEdge(graph,a,b): 
    graph[a].append(b)

# Call the functions 
addEdge(graphOne,'a','b')
addEdge(graphOne,'b','c')
addEdge(graphOne,'c','d')
addEdge(graphOne,'d','e')
addEdge(graphOne,'e','f')
addEdge(graphOne,'f','g')

print(generate_edges(graphOne))

# CODE FOR GENERATING SHORTEST AND LONGEST PATH OF THE EDGE NOT IMPLEMENTED