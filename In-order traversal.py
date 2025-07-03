# https://www.hackerrank.com/challenges/tree-inorder-traversal/problem?isFullScreen=true

def inOrder(root):
    if root is None:
        return;
    else:
        inOrder(root.left)
        print(root.info, end=" ")
        inOrder(root.right)
