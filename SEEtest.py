class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    def create_list(self,values):
        for value in values:
            self.append_node_end(value)
    def print_list(self):
        current = self.head
        while current:
            print(current)
            current = current.next
    def append_node_start(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def append_node_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def append_node_pos(self,value,pos):
        new_node = Node(value)
        if pos == 0:
            if self.head is None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        else:
            current = self.head
            for _ in range(pos-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
    def delete_value(self,value):
        current = self.head
        prev = None
        if current and current.value == value:
            self.head = current.next
            current = None
            return
        while current and current.value != value:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def delete_start(self):
        if not self.head:
            print("List is empty.\n")
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List empty.\n")
            return
        if not self.head.next:
            self.head=None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def delete_pos(self, pos):
        current = self.head
        if pos ==0:
            self.delete_start()
            return
        for _ in range(pos-1):
            current = current.next
        if current.next:
            current.next = current.next.next
            current = None
        else:
            raise IndexError("Position out of bounds.\n")
        
    def search_node(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False        
    

class stackNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def push(self, value):
        new = stackNode(value)
        if self.is_empty():
            self.head = new
        new.next = self.head
        self.head = new

    def pop(self):
        if self.is_empty():
            print("MT")
            return None
        popped_value = self.head
        self.head = self.head.next
        return popped_value

    def peek(self):
        if self.is_empty():
            print("MT")
            return None
        print(self.head)
        return

    def printStack(self,value):
        if self.is_empty():
            print("MT")
            return None
        current = self.head
        while current:
            print(current)
            current = current.next

    def postFix(exp):
        chars = exp.split()
        stack = Stack()

        for char in chars:
            if char.isdigit():
                stack.push(int(char))
            if char in '+-/*':
                operand2 = stack.pop()
                operand1 = stack.pop()

                if char == '+':
                    return operand1 + operand2
                elif char == '-':
                    return operand1 - operand2
                elif char == '/':
                    return operand1 / operand2
                elif char == '*':
                    return operand1 * operand2
                
class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value): #add a value to the rear
        new = QueueNode(value)
        if self.front is None:
            self.front = self.rear = new
        self.rear.next = new
        self.rear = new

    def dequeue(self): #remove a value from the front
        if self.is_empty():
            print("MT")
            return
        dequeued = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return dequeued

    def peek(self): #view the front element
        if self.is_empty():
            return "MT"
        print(self.front.value)

    def is_empty(self):
        return self.front is None

    def printQueue(self):
        current = self.front
        while current:
            print(current) 
            current = current.next
        
                
