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
        new_node = Node(value) 
        if self.is_empty(): 
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node 
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        dequeued_value = self.front.value
        self.front = self.front.next 

        if self.front is None:
            self.rear = None
        return dequeued_value
    
    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current:
                print(current)
                current = current.next


q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

