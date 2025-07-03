# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem?isFullScreen=true

def postOrder(root):
    if root is None:
        return;
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=" ")
