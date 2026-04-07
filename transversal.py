class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def transverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("none")

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        
    def delete_first(self):
        if self.head is None:
            print("list is empty")
            return
        
        self.head = self.head.next

    def delete_first(self):
        if self.head is None:
            print("list is empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

ll = linkedlist()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print("original list:")
ll.transverse()

ll.insert_begin(5)
print("after insert at beginning:")
ll.transverse()

ll.insert_end(40)
print("after insert at end:")
ll.transverse()

ll.delete_first()
print("after delete first:")
ll.transverse()

ll.delete_first()
print("after delete last:")
ll.transverse()