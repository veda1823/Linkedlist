class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def findMin(head):
    if head is None:
        return -1
    mn = head.data
    cur = head.next
    while cur is not None:
        if cur.data < mn:
            mn = cur.data
        cur = cur.next
    return mn
n = int(input())
head = None
if n > 0:
    a = list(map(int, input().split()))
    head = Node(a[0])
    cur = head
    for i in range(1, n):
        cur.next = Node(a[i])
        cur = cur.next

print(findMin(head))