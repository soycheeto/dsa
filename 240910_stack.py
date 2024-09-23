class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack():
    def __init__(self):
        self.head = None  

    def is_empty(self):
        return self.head is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node      
    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.print_stack()

print("Is the stack empty?", s1.is_empty()) 
