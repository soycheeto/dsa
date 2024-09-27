class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Circular_linkedList():
    def __init__(self):
        self.head=None
        self.n1=Node(10, None)
        self.n2=Node(20, None)
        self.n3=Node(30, None)
        self.n1.next=self.n2
        self.n2.next=self.n3

    def traversal(self):
        temp = self.head
        if temp is None:
            return
        while True:
            print(temp.value, end=" ")
            temp = temp.next
            if temp == self.head:
                break
