class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front = None
        self.read=None

    def enqueue(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
            
    def is_empty(self):
        return self.front is None
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        dequeued_value = self.front.value
        self.front = self.front.next 

        if self.front is None:
            self.rear = None
        return dequeued_value
    
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:\n", q.front())

print("Is the queue empty?\n", q.is_empty())
