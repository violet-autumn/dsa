# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem?isFullScreen=true

def reversePrint(head):
    current_node = head
    a = []
    while current_node is not None:
        a.append(current_node.data)
        current_node = current_node.next
    while a != []:
        print(a.pop())
