class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMiddle(head):
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

n = int(input())

head = None

if n > 0:
    a = list(map(int, input().split()))

    head = Node(a[0])
    cur = head

    for i in range(1, n):
        cur.next = Node(a[i])
        cur = cur.next

ans = findMiddle(head)
print(ans.data)