"""
Create a class Node with arguments: value, next
Create 5 nodes and link them
And do the following operations - 1) Traverse through the list and print the value of each node, 2)Search for a particular node, the value of the node to be searched is to be given by the user"""

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

def traverse(start):
    current = start
    while current:
        print(current.value)
        current = current.next

def search(start, searchval):
    current = start
    while current:
        if current.value == searchval:
            return f"Node with value {searchval} found.\n"
        current = current.next
    return f"Node with value {searchval} not found.\n"

head = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

head.next=n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("Node values: \n")
traverse(head)

value = int(input("Enter a value: \n"))
result = search(head, value)
print(result)
