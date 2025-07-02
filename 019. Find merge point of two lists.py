# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?isFullScreen=true

def findMergeNode(head1, head2):
    a = []
    c1 = head1
    c2 = head2
    
    # Store the addresses of all nodes for list1
    while c1 is not None:
        a.append(c1)
        c1 = c1.next
    
    # Iterate through list 2 and find the first occurance of common node
    while c2 is not None:
        if c2 in a:
            return c2.data
        else:
            c2 = c2.next
    
    # Lists didn't merge
    return None
