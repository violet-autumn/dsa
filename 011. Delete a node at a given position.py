# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem?isFullScreen=true

def deleteNode(head, position):
    if head is None:
        return None
    elif position == 0:
        current_node = head
        head = head.next
        current_node.next = None
        return head
    else:
        current_node = head
        next_node = head.next
        while position > 1:
            current_node = current_node.next
            next_node = next_node.next
            position = position - 1
        current_node.next = next_node.next
        next_node.next = None
        return head
