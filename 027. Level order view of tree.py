# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?isFullScreen=true

def height_of_tree(root):
    if root is None:
        return -1
    else:
        return 1 + max(height_of_tree(root.left), height_of_tree(root.right))

def depth_traversal(root, arr, depth):
    if root is None:
        return
    else:
        depth_traversal(root.left, arr, depth + 1)
        arr[depth].append(root.info)
        depth_traversal(root.right, arr, depth + 1)

def levelOrder(root):
    # Find the height of the tree
    height = height_of_tree(root)
    
    #Define a 2D array to store node values as per depth [[Nodes at depth 0], [Nodes at depth 1], [Nodes at depth 2],...]
    arr = [[] for _ in range(height+1)]
    
    # Traverse the tree inOrder and fill the array
    depth_traversal(root, arr, 0)
    
    # Print the nodes as per depth
    for i in range (0, height+1):
        for j in range(0, len(arr[i])):
            print(arr[i][j], end=" ")
