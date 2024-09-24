class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


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
        self.head=self.n1
        self.n1.prev=self.head

    def insert_beginning(self, value):
        new = Node(value)  
        new.next = self.head 
        if self.head is not None:
            self.head.prev = new 
        self.head = new  
    def insert_end(self, value):
        new = Node(value)  
        if self.head is None:
            self.head = new
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = new
            new.prev = tail

dll = Doubly_linkedList()
dll.insert_beginning(5)