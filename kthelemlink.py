class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findKth(head, k):
    cur = head

    for i in range(1, k):
        if cur is None:
            return -1
        cur = cur.next

    if cur is None:
        return -1

    return cur.data

n = int(input())

head = None

if n > 0:
    a = list(map(int, input().split()))

    head = Node(a[0])
    cur = head

    for i in range(1, n):
        cur.next = Node(a[i])
        cur = cur.next

k = int(input())

print(findKth(head, k))