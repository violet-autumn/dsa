def insertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = head
    head = new_node
    return head
