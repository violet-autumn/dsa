# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem?isFullScreen=true

def getNode(head, positionFromTail):
    a = []
    current_node = head
    while current_node is not None:
        a.append(current_node.data)
        current_node = current_node.next
    
    size = len(a)
    answer = a[size-positionFromTail-1]
    
    return answer
