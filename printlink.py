class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    cur = head

    while cur is not None:
        print(cur.data, end=" -> ")
        cur = cur.next

    print("X")

n = int(input())

if n == 0:
    head = None
else:
    a = list(map(int, input().split()))

    head = Node(a[0])
    cur = head

    for i in range(1, n):
        cur.next = Node(a[i])
        cur = cur.next

printList(head)