"""Create a class node with the following attributes : value, next

Create a class Stack and the class Stack should have the following methods:
init()
is_empty(): that checks whether the stack is empty or not
pop(): pop the topmost element into the stack
print():print the stack"""

class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next  


class Stack:
    def __init__(self):
        self.head = None  
        
    def is_empty(self):
        return self.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node      

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        else:
            popped_value = self.head.value
            self.head = self.head.next
            return popped_value

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.head
            print("Stack elements:")
            while current:
                print(current.value)
                current = current.next

s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.print_stack() 
print("Popped element:", s.pop()) 
s.print_stack()
print("Is the stack empty?", s.is_empty())
