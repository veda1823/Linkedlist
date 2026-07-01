class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteMiddle(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    while fast != None and fast.next != None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head

# Input
n = int(input())
arr = list(map(int, input().split()))

# Create linked list
head = Node(arr[0])
curr = head
for i in range(1, n):
    curr.next = Node(arr[i])
    curr = curr.next

# Delete middle node
head = deleteMiddle(head)

# Print linked list
curr = head
while curr:
    print(curr.val, end=" ")
    curr = curr.next