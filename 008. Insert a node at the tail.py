def insertNodeAtTail(head, data):
    current_node = head
    
    if current_node is None:
        new_node = SinglyLinkedListNode(data)
        return new_node 
    else:
        while current_node.next is not None:
            current_node = current_node.next
        new_node = SinglyLinkedListNode(data)
        current_node.next = new_node
        return head
