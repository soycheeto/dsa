"""Create a class Node with attributes
value, next
Create five nodes and link them.
Perform the following operations:
Print the list
Insert a new node at the end of the list
Insert a new node at the beginning of the list
Insert a new node at a specific position in the list(the position has to be given by the user)"""

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
def printNode(start):
    current = start
    while current:
        print(current.value)
        current = current.next

def insertEnd(head, new_val):
    new_node = Node(new_val) #create new node
    if not head: #if head = None
        return new_node 
    
    temp = head 
    while temp.next: #traverse till last node
        temp = temp.next #add new pointer 
    temp.next = new_node #assign pointer to new node
    return head

def insertStart(head, new_val):
    new_node = Node(new_val)
    new_node.next = head
    return new_node

def insertPos(head, new_val, pos):
    new_node = Node(new_val)
    
    if pos == 0:
        # Insert at the head
        new_node.next = head
        return new_node
    
    node = head
    for _ in range(pos - 1):
        node = node.next
    
    next = node.next
    node.next = new_node
    new_node.next = next
    
    return head

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


printNode(n1)

head = insertEnd(n1, 6)
printNode(head)

head = insertStart(head, 0)
printNode(head)

head = insertPos(head, 100, 3)
printNode(head)

