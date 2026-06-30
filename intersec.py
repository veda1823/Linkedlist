class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build(arr):
    if not arr:
        return None, None

    head = Node(arr[0])
    cur = head

    for x in arr[1:]:
        cur.next = Node(x)
        cur = cur.next

    return head, cur


def getIntersectionNode(headA, headB):
    p1 = headA
    p2 = headB

    while p1 != p2:
        if p1:
            p1 = p1.next
        else:
            p1 = headB

        if p2:
            p2 = p2.next
        else:
            p2 = headA

    return p1


# Input
n, m, c = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
common = list(map(int, input().split()))

headA, tailA = build(a)
headB, tailB = build(b)
commonHead, commonTail = build(common)

if tailA:
    tailA.next = commonHead
else:
    headA = commonHead

if tailB:
    tailB.next = commonHead
else:
    headB = commonHead

ans = getIntersectionNode(headA, headB)

if ans:
    print(ans.data)
else:
    print("NULL")