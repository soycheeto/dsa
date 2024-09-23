class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    
    def is_empty(self):
        return self.front is None and self.rear is None

    
    def insert(self, value):
        new_node = Node(value) 
        if self.is_empty(): 
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node 
    def print_queue(self):
        if self.is_empty():
            print
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

