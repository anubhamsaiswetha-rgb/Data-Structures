class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("middle:", find_middle(n1))