# https://www.hackerrank.com/challenges/tree-top-view/problem?isFullScreen=true

def explore(root, nodes, hd, depth):
    if root is None:
        return
    else:
        # Explore the left subtree
        explore(root.left, nodes, hd - 1, depth + 1)
        # Check if the root belongs in nodes dict
        if hd not in nodes or (hd in nodes and depth < nodes[hd]):
            nodes[hd] = depth                     
        # Explore the right subtree
        explore(root.right, nodes, hd + 1, depth + 1)

def fetch_nodes(root, nodes, node_values, hd, depth):
    if root is None:
        return
    else:
        # Fetch from the left subtree
        fetch_nodes(root.left, nodes, node_values, hd - 1, depth + 1)
        # Check if root node is one of the selected ones
        if hd in nodes and depth == nodes[hd]:
            node_values[hd] = root.info
        # Fetch from the right subtree
        fetch_nodes(root.right, nodes, node_values, hd + 1, depth + 1)


def topView(root):
    # Define a dict that will store the (hd, depth) for each selected node 
    nodes = {} 
    
    # Recursively find the selected nodes - select one node for every new hd value (with the min depth) 
    explore (root, nodes, 0, 0)

    # Define a dict that will store the (hd, node value) for the selected nodes
    node_values = {}

    # Fetch the values of the selected nodes
    fetch_nodes (root, nodes, node_values, 0, 0)
    
    # Print the nodes as per top view (aka min_hd to max_hd)
    min_hd = min(node_values)
    max_hd = max(node_values)
    for i in range(min_hd, max_hd+1):
        print(node_values[i], end =" ")
