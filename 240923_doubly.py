class Node():
    def __init__(self, value, next, prev):
        self.value=value
        self.next=next
        self.prev=prev

class Doubly_linkedList():
    def __init__(self):
        self.head=None
        self.n1 = Node(10, None,None)
        self.n2 = Node(20, None,None)
        self.n3 = Node(30, None,None)
        self.n1.next=self.n2
        self.n2.prev=self.n1
        self.n2.next=self.n3
        self.n3.prev=self.n2
        self.head.next=self.n1
        self.n1.prev=self.head

    def traverse_forward(self):
        temp=self.head
        while(temp!=None):
            print(temp.value)
            temp = temp.next

    def traverse_backward(self):
        temp=self.n3
        while(temp!=None):
            print(temp.value)
            temp = temp.prev

dll = Doubly_linkedList()
dll.traverse_forward()
dll.traverse_backward()

