class Node:
    def __init__(self, data):
        self.data =data
        self.next = None
    
class Circular_linkedList():
    def __init__(self):
        self.head=None
        self.n1=Node(10,None)
        self.n2=Node(20,None)
        self.n3=Node(30,None)
        self.n1.next=self.n2
        self.n2.next=self.n3
        self.head=self.n1
        self.n3.next=self.head
    def traversal(self):
        temp=self.head
        while True:
            print(temp.value)
            temp=temp.next
            if(temp==self.head):
                break
    def insertion_beginning(self,value):
        new_node = Node(value)
        if not self.head: 
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insertion_after_node(self, target_value, value):
        temp = self.head
        if not temp:
            return
        while True:
            if temp.data == target_value:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                break 
            temp = temp.next
            if temp == self.head:
                print(f"Node with value {target_value} not found.")
                break


