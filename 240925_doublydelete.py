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
        self.n1.next = self.n2
        self.n2.prev = self.n1
        self.n2.next = self.n3
        self.n3.prev = self.n2
        self.head = self.n1

    def delete_at_start(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head

        while current.next:
            current = current.next

        if current == self.head:
            self.head = None
            return
        
        current.prev.next = None

    def delete_at_middle(self, value):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while current and current.value != value:
            current = current.next
        if not current:
            print(f"Node with value {value} not found")
            return
        if current == self.head and not current.next:
            self.head = None
            return
        if current == self.head:
            self.head = current.next
            self.head.prev = None
            return
        if not current.next:
            current.prev.next = None
            return
        current.prev.next = current.next
        current.next.prev = current.prev
