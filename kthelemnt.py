class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getKthFromEnd(head, k):
    slow = head
    fast = head

    for i in range(k):
        if fast is None:
            return -1
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.data

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

print(getKthFromEnd(head, k))