# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem?isFullScreen=true

def preOrder(root):
    if root is None:
        return;
    else:
        print(root.info, end=" ")
        preOrder(root.left)
        preOrder(root.right)
