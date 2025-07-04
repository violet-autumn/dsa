# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?isFullScreen=true

def decodeHuff(root, s):
    answer = ""
    it = 0
    
    # Number of characters in the answer = freq at root
    for i in range(0, root.freq):
        current_node = root
        
        # Traverse the tree until you reach a leaf node (whose left and right are None)
        while current_node.left is not None:            
            if s[it] == '0': 
                if current_node.left.left is None:
                    answer += current_node.left.data 
                current_node = current_node.left
            else:
                if current_node.right.left is None:
                    answer += current_node.right.data
                current_node = current_node.right
            it = it + 1
    
    # Print the result
    print(answer)
