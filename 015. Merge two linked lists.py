# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem?isFullScreen=true

def mergeLists(head1, head2):
    
    # Assign c1 and c2 of the basis that c1.data is <= c2.data. 
    # Assign head to smaller one to return in the end
    if head1.data <= head2.data:
        c1 = head1
        c2 = head2
        head = head1
    else:
        c1 = head2
        c2 = head1
        head = head2
    
    # Merge the lists until one of the current pointers (c1, c2) become None
    # p is the pointer to the node just before c1 and c2 branch off 
    while c1 is not None and c2 is not None:
        if c1.data <= c2.data:
            p = c1
            c1 = c1.next
        else:
            p.next = c2
            c2 = c2.next
            p = p.next
            p.next = c1
    
    # Based on which current pointer reached null, attach the rest of the remaining link list
    if c1 is None:
        p.next = c2
    else:
        p.next = c1

    return head
