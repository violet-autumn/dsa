# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?isFullScreen=true

# Given
class BinarySearchTree:
    def __init__(self): 
        self.root = None
         
#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

# Code below

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return self.root
        else:
            current_node = self.root
            while current_node is not None:
                if current_node.info < val:
                    if current_node.right is not None:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        return self.root
                else:
                    if current_node.left is not None:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        return self.root
