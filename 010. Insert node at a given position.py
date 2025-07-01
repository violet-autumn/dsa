def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        head = new_node
    elif position == 0:
        new_node.next = head
        head = new_node
    else:
        current_node = head
        next_node = head.next
        while position > 1:
            current_node = current_node.next
            next_node = next_node.next
            position = position - 1
        current_node.next = new_node
        new_node.next = next_node 
    
    return head
