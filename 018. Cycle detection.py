# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true

def has_cycle(head):
    if head is None or head.next is None:
        # no cycle
        return 0
    else:
        slow_ptr = head
        fast_ptr = head.next
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            if slow_ptr == fast_ptr:
                #cycle detected
                return 1
            else:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
        # reached end, no cycle found
        return 0  
