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

def kthFromEnd(head, k):
    length = findLength(head)

    pos = length - k + 1

    cur = head
    count = 1

    while count < pos:
        cur = cur.next
        count += 1

    return cur

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

ans = kthFromEnd(head, k)
print(ans.data)