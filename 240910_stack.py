class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def is_empty(self):
        if(self.head==None):
            print("is empty")
        print("not empty")

    def push(self,value):
        new_node=Node(value,None)
        if(self.head==None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def print_stack(self):
        if(self.head==None):
            print("Stack is empty")
            return
        else:
            current = self.head
            print("Stack is empty")
            while current:
                print(current.data)
                current=current.next


stack = Stack()
stack.is_empty()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()
stack.is_empty()