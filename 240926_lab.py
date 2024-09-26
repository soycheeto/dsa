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

    def delete_node_by_value(self, value):
        current = self.head
        
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:  # Node is the head
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                print(f"Node with value {value} deleted.")
                return
            current = current.next
        
        print(f"Node with value {value} not found.")


    def traverse_backward(self):
        temp=self.n3
        while(temp!=None):
            print(temp.value)
            temp = temp.prev

dll = Doubly_linkedList()
dll.delete_node_by_value(30)
dll.traverse_backward() 
