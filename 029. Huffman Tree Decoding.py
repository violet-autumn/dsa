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


#------------------------------------------------------------------------------------------------------------#

# The following approach traverses the entire tree once and builds a decoder dict, thereby saving the comute to go through the tree for every letter

def assign(root, decoder, string):
    # If the node is a leaf node, assign the character in decoder dict
    if root.left is None: 
        decoder[string] = root.data
    else:
        assign(root.left, decoder, string + '0')
        assign(root.right, decoder, string + '1')

def decodeHuff(root, s):
    
    # Define a dictionary that will store the decoded characters
    decoder = {}
    
    # Decode the characters from the tree
    assign(root, decoder, '')
    
    # Parse the input string and return the answer
    answer = ""
    temp = ""
    it = 0
    for it in range (0, len(s)):
        temp += s[it]
        if temp in decoder:
            answer += decoder[temp]
            temp = ""
    
    print(answer)
