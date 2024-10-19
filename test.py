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
    def enqueue(self, value):
        new = Node(value)
        if self.is_empty():
            self.front = self.rear = new
        self.rear.next = new
        self.rear = new
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        dequeue =self.front.value
        self.front = self.front.next
        
        if self.front is None:
            self.rear is None
        return dequeue
    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        current = self.front.value
        while current:
            print(current.value)
            current = current.next