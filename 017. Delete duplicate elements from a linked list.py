# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem?isFullScreen=true

def removeDuplicates(head):
    if head is None or head.next is None:
        return head
    else:
        previous_node = head
        current_node = head.next
        while current_node is not None:
            if previous_node.data == current_node.data: 
                #Delete dupicate node
                previous_node.next = current_node.next
                current_node.next = None
                current_node = previous_node.next
            else:
                #Increment both 
                current_node = current_node.next
                previous_node = previous_node.next
        return head
