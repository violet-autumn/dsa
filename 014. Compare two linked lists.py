# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?isFullScreen=true

def compare_lists(head1, head2):
    c1 = head1
    c2 = head2
    
    # Return 0 incase of data mismatch
    while c1 is not None and c2 is not None:
        if c1.data != c2.data:
            return 0
        c1 = c1.next
        c2 = c2.next
    
    # If both the lists ended together, return 1, else 0 
    if c1 is None and c2 is None:
        return 1
    else:
        return 0
