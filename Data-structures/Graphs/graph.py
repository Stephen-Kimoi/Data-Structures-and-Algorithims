# GRAPH IMPLEMENTATION IN PYTHON 

# Create a Node class
class Node:
    # Initialize it with stored data (values) and list of neighbors 
    def __init__(self, value, neighbors=None): 
        self.value = value 
        if neighbors == None: 
            self.neighbors = [] 
        else:
            self.neighbors = neighbors
        
    # Check whether the node is connected to any neighbors 
    def node_has_neighbors(self): 
        if len(self.neighbors) == 0: 
            return False 
        return True 

    # Returns number of vertices which have a neighbor
    def number_of_neighbors(self): 
        return len(self.neighbors)
    
    # Add a new connection 
    def add_neighbor(self, neighbor): 
        self.neighbors.append(neighbor)
    

# Now that we've created a node, we can create a Graph class that will 
# represent the graph data structure 

class Graph: 
    # It contains an attribute that has all nodes of the graph 
    def __init__(self, nodes=None): 
        if nodes is None: 
            self.nodes = [] 
        else:
            self.nodes = nodes 
    
    # Adding new nodes to the graph 
    def add_new_node(self, value, neighbors=None):
        self.nodes.append(Node(value, neighbors))
    
    # Check whether a node of a given value exists 
    def node_exists(self,value): 
        for node in self.nodes: 
            if node.value == value: 
                return node
        return node

    # Add a new edge between nodes 
    def add_new_edge(self, value1, value2, weight=1):
        node1 = self.node_exists(value1)
        node2 = self.node_exists(value2)

        if (node1 is not None) and (node2 is not None): 
            node1.add_neighbor((node1, weight))
            node2.add_neighbor((node2, weight))
        else: 
            print("Error: One or more nodes are not found")
        
    # Return the number of nodes in the graph 
    def number_of_nodes(self): 
        return f"The graph has {len(self.nodes)} nodes" 

    # Return true if given nodes are connected otherwise return false 
    def are_connected(self, node_one, node_two): 
        node_one = self.node_exists(node_one) 
        node_two = self.node_exists(node_two)

        for neighbor in node_one.neighbors: 
            if neighbor[0].value == node_two.value: 
                return True 
            return False