class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1
tail = n5

temp = head
while temp:
    print(temp.data)
    temp = temp.next

count = 0
temp = head
while temp:
    count +=1
    temp = temp.next

print("Length:", count)

print("Head:", head.data)
print("Tail:", tail.data)