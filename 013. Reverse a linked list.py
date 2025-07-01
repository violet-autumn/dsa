# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem?isFullScreen=true

def reverse(head):
    if head is None or head.next is None:
        return head
    else:
        p = head
        c = p.next
        n = c.next
        head.next = None
        while n is not None:
            c.next = p
            p = c
            c = n
            n = n.next
        c.next = p
        head = c
        return head
