# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem?isFullScreen=true

def printLinkedList(head):
    current_node = head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next
