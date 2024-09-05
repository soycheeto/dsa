#Create a class Node with two parameters - value, next
#Create three instances and link them

class Node:
    def _init_(self, value, next):
        self.value=value
        self.next=next
        
node1=Node(10,None)  
node2=Node(20,node1) 
node3=Node(30,node2) 


l1reverse=[]
current_node=node3
while current_node:
    l1reverse.append(current_node.value)
    current_node=current_node.next

l1reverse