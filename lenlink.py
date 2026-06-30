class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findLength(head):
    cur = head
    length = 0

    while cur is not None:
        length += 1
        cur = cur.next

    return length

n = int(input())

head = None

if n > 0:
    a = list(map(int, input().split()))

    head = Node(a[0])
    cur = head

    for i in range(1, n):
        cur.next = Node(a[i])
        cur = cur.next

print(findLength(head))