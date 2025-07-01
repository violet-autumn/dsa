# www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list?isFullScreen=true

def insertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = head
    head = new_node
    return head
