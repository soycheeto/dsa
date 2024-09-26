"""Create a class node that has the following attributes:
value, next, prev

Create a class doubly_linkedlist and include the following operations:
Creation of a doubly linked list with five nodes
Write a method to make a doubly linked list circular
Write a method to find the middle element in a doubly linked list"""
class Node: 
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Doubly_linkedList():
    def __init__(self):
        self.head = None
        self.n1 = Node(10)
        self.n2 = Node(20)
        self.n3 = Node(30)
        self.n4 = Node(40)
        self.n5 = Node(50)
        self.n1.next = self.n2
        self.n2.prev = self.n1
        self.n2.next = self.n3
        self.n3.prev = self.n2
        self.n3.next = self.n4
        self.n4.prev = self.n3
        self.n4.next = self.n5
        self.n5.prev = self.n4
        self.head = self.n1
    
    def circular(self):
        self.n5.next = self.head
        self.head.prev = self.n5

    def find_middle(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        
        middle_position = count // 2
        
        current = self.head
        for i in range(middle_position):
            current = current.next
        
        return current.value