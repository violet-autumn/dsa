# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?isFullScreen=true

def reverse(head):
    if head is None or head.next is None:
        return head
    else:
        current_node = head
        while current_node is not None:
            # Swap current_node.next and current_node.prev
            next_node = current_node.next
            current_node.next = current_node.prev
            current_node.prev = next_node
            
            # Keep previous node saved for returning the head and increment current_node
            current_head = current_node
            current_node = next_node
        return current_head
