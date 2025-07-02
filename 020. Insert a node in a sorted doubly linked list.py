# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?isFullScreen=true

def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    
    if head is None:     
        # Linked list was empty           
        head = new_node
        return head

    elif new_node.data < head.data: 
        # New element is to be inserted at head position
        head.prev = new_node
        new_node.next = head
        head = new_node
        return head
        
    else:
        # New element to be inserted at ith/tail positon                           
        current_node = head
        while current_node.next is not None:
            if new_node.data < current_node.next.data:
                # Insert the element after current node
                new_node.next = current_node.next
                new_node.prev = current_node
                current_node.next.prev = new_node
                current_node.next = new_node
                return head
            else:
                current_node = current_node.next 
        
        # Insert the element at tail
        current_node.next  = new_node
        new_node.prev = current_node
        return head
