# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?isFullScreen=true

def address_along_path(root, path, val):
    current_node = root
    while current_node.info != val:
        path.append(current_node.info)
        if current_node.info > val:
            current_node = current_node.left
        else:
            current_node = current_node.right
    path.append(current_node.info)

def return_ptr_from_value(root, val):
    current_node = root
    while current_node is not None:
        if current_node.info == val:
            return current_node
        elif current_node.info > val:
            current_node = current_node.left
        else:
            current_node = current_node.right

def lca(root, v1, v2):
    # Iterate through the tree for v1 and store the val of each node along the path in an array
    path1 = []
    address_along_path(root, path1, v1)
    
    # Iterate through the tree for v2 and store the val of each node along the path in an array
    path2 = []
    address_along_path(root, path2, v2)
    
    # Iterate through array2 until the same val is found in array1
    for i in range (len(path2)-1, 0-1, -1):
        if path2[i] in path1:
            return return_ptr_from_value(root, path2[i])    


#-----------------------------------------------------------------------------------------------------------------# 

# The following approach can also be done using the value of the node instead of the address of the node

def lca(root, v1, v2):
    # Iterate through the tree for v1 and store the mem_addr of each node along the path in an array
    path1 = []
    current_node = root
    while current_node.info != v1:
        path1.append(current_node)
        if current_node.info > v1:
            current_node = current_node.left
        else:
            current_node = current_node.right
    path1.append(current_node)
    
    # Iterate through the tree for v2 and return pointer to the last node after which the paths deviate
    current_node = root
    while current_node in path1:
        previous_node = current_node
        if current_node.info > v2:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return previous_node
