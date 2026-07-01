class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

n = int(input())
a = list(map(int, input().split()))
pos = int(input())

head = Node(a[0])
curr = head
nodes = [head]

for i in range(1, n):
    curr.next = Node(a[i])
    curr = curr.next
    nodes.append(curr)

deleteNode(nodes[pos])

curr = head
while curr:
    print(curr.val, end=" ")
    curr = curr.next