"""
-basic mathematical recursion
-nodes
    -creation"""

class Node:
    def _init_(self, value):
        self.value=value
        self.next=None

"""-linked lists
    -insert a node at start/end/position
    -delete node at start/end/position  
    -traversal and print
    -search for value"""

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self, values):
        for value in values:
            self.append_node_end(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

    def append_node_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append_node_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_node_at(self, value, position):
        new_node = Node(value)
        if position == 0:  # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node    
            
    def delete_node(self, value):
        current = self.head # Initialize `current` to the head of the linked list and `prev` to None.
        prev = None
        if current and current.value == value: # Check if the head node itself contains the target value to delete.
            self.head = current.next # If so, update the head to point to the next node, effectively removing the current head.
            current = None # Free the memory by dereferencing the `current` node.
            return  # Exit the function as the node has been deleted.
        while current and current.value != value: # Traverse the list to find the node with the target value.
            prev = current # Update `prev` to point to the current node before moving to the next node.
            current = current.next # Move `current` to the next node in the list.
        if current is None: # If `current` is None, it means the target value is not present in the list.
            return  # Exit the function without making any changes.
        prev.next = current.next # Adjust the `next` pointer of the `prev` node to bypass the node to be deleted.
        current = None # Free the memory of the node to be deleted by dereferencing it.


    def delete_node_at_start(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_node_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:  # Only one node in the list
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None 

    def delete_node_at(self, position):
        if position == 0:  # Delete the first node
            self.delete_node_at_start()
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            raise IndexError("Position out of bounds")

    def search_node(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    """

-stack
    -check if empty
    -push
    -pop
    -peek   
    -print
    -traverse
    -postfix formulas IMPORTANT"""
    
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next  


class Stack:
    def __init__(self):
        self.head = None  
        
    def is_empty(self):
        return self.head is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node      

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        else:
            popped_value = self.head.value
            self.head = self.head.next
            return popped_value
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        else:
            return self.head.value

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.head
            print("Stack elements:")
            while current:
                print(current.value)
                current = current.next

    def postfix(exp):
        stack = Stack()

        chars = exp.split()

        for char in chars:
            if char.isdigit(): 
                stack.push(int(char))
            else: 
                operand2 = stack.pop()
                operand1 = stack.pop()
            
            
                if char == '+':
                    result = operand1 + operand2
                elif char == '-':
                    result = operand1 - operand2
                elif char == '*':
                    result = operand1 * operand2
                elif char == '/':
                    result = operand1 / operand2  
                else:
                    return f"Unknown operator: {char}"
            
   
                stack.push(result)
    
   
        return stack.pop()
    exp = "5 6 2 + * 12 4 / -"
    result = postfix(exp)
    print(f"The result of the exp '{exp}' is: {result}")
    
    """
-queue
    -is_empty
    -enqueue
    -dequeue
    -peek
    -print

"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.front = None
        self.rear=None

    def enqueue(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        dequeued_value = self.front.value
        self.front = self.front.next 

        if self.front is None:
            self.rear = None
        return dequeued_value
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty. No front element.")
            return None
        return self.front.value
            
    def is_empty(self):
        return self.front is None

"""
-doubly linked lists
    -insert at beginning/end/position
    -delete at start/end/middle/value/position 
    -traverse forward/backward x
    -make list circular x
    -find middle node x

    """
class Node: 
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Doubly_linkedList():
    def __init__(self):
        self.head=None
        self.n1 = Node(10, None,None)
        self.n2 = Node(20, None,None)
        self.n3 = Node(30, None,None)
        self.n1.next=self.n2
        self.n2.prev=self.n1
        self.n2.next=self.n3
        self.n3.prev=self.n2
        self.head.next=self.n1
        self.n1.prev=self.head

    def traverse_forward(self):
        temp=self.head
        while(temp!=None):
            print(temp.value)
            temp = temp.next

    def traverse_backward(self):
        temp=self.n3
        while(temp!=None):
            print(temp.value)
            temp = temp.prev

    def insert_beginning(self, value):
        new = Node(value)  
        new.next = self.head 
        if self.head is not None:
            self.head.prev = new 
        self.head = new  

    def insert_end(self, value):
        new = Node(value)  
        if self.head is None:
            self.head = new
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = new
            new.prev = tail

    def insert_at_position(self, value, position):
        new_node = Node(value)
        if position == 0:  # Insert at the beginning
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node

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

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty")
            return

        if position == 0:  # Delete at the beginning
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return

        current = self.head
        for _ in range(position):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next

        if current is None:
            raise IndexError("Position out of bounds")

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def circular(self):
        self.n3.next = self.head
        self.head.prev = self.n3

    def find_middle(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        
        middle_position = count // 2
        
        current = self.head
        for i in range(middle_position):
            current = current.next
        
        return current.value

"""
-circular linked lists
    -traversal
    -insert at beginning
    -insert after node

    """
class CircularNode:
    """Class to represent a node in a circular linked list."""
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node


class CircularLinkedList:
    """Class to represent a circular linked list."""
    def __init__(self):
        self.head = None  # Pointer to the head of the list

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = CircularNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself for circularity
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            self.head = new_node
            last.next = self.head

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = CircularNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself for circularity
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head

    def delete_node(self, data):
        """Delete the first node with the given data."""
        if self.head is None:
            print("The list is empty. Nothing to delete.")
            return

        # Special case: Deleting the head node
        current = self.head
        prev = None
        while current.data != data:
            if current.next == self.head:
                print(f"Data {data} not found in the list.")
                return
            prev = current
            current = current.next

        if current == self.head:  # Head node to be deleted
            if self.head.next == self.head:  # Single node case
                self.head = None
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = self.head.next
                last.next = self.head
        else:  # Deleting other nodes
            prev.next = current.next
        current = None

    def traverse(self):
        """Traverse and print the circular linked list."""
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")




"""
-binary search trees
    -dfs
    -bfs
    -pre/in/post order recursive
    -lca
    -grandchildren

    """

class TreeNode:
    """Class to represent a node in a binary tree."""
    def __init__(self, data):
        self.data = data  # Data of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child


class BinaryTree:
    """Class to represent a binary tree."""
    def __init__(self):
        self.root = None  # Pointer to the root of the tree

    def insert(self, data):
        """Insert a new node with the given data into the tree."""
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                # Insert in the left child if empty
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    queue.append(current.left)

                # Insert in the right child if empty
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    queue.append(current.right)

    def pre_order_traversal(self, node):
        """Traverse the tree in pre-order (root, left, right)."""
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        """Traverse the tree in in-order (left, root, right)."""
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        """Traverse the tree in post-order (left, right, root)."""
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

    def find_lca(self, node1, node2):
        """Find the Lowest Common Ancestor of two nodes."""
        return self._find_lca_helper(self.root, node1, node2)

    def _find_lca_helper(self, node, node1, node2):
        """Helper function to find LCA."""
        # Base case: if the node is None or matches either node1 or node2
        if node is None or node.data == node1 or node.data == node2:
            return node

        # Recursively search in the left and right subtrees
        left_lca = self._find_lca_helper(node.left, node1, node2)
        right_lca = self._find_lca_helper(node.right, node1, node2)

        # If both left and right subtrees return non-null values, current node is the LCA
        if left_lca and right_lca:
            return node

        # Otherwise, return the non-null value from the left or right subtree
        return left_lca if left_lca else right_lca

    def find_grandchildren(self, node_val):
        """Find and return a list of all grandchildren of the given node."""
        # Find the node first
        node = self._find_node(self.root, node_val)
        if node is None:
            return []

        grandchildren = []
        # Check the children of the given node
        if node.left:
            if node.left.left:
                grandchildren.append(node.left.left.data)
            if node.left.right:
                grandchildren.append(node.left.right.data)
        if node.right:
            if node.right.left:
                grandchildren.append(node.right.left.data)
            if node.right.right:
                grandchildren.append(node.right.right.data)

        return grandchildren

    def _find_node(self, node, node_val):
        """Helper function to find a node with a given value."""
        if node is None or node.data == node_val:
            return node

        left_result = self._find_node(node.left, node_val)
        if left_result:
            return left_result

        return self._find_node(node.right, node_val)
            
    def bfs(self):
        """Perform a breadth-first search (level-order traversal) on the tree."""
        if not self.root:
            print("Tree is empty")
            return
        
        queue = [self.root]  # Initialize a queue with the root node
        
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")  # Process the current node
            
            if current.left:
                queue.append(current.left)  # Enqueue the left child
            
            if current.right:
                queue.append(current.right)  # Enqueue the right child

    def dfs(self):
        """Perform a depth-first search (pre-order traversal) on the tree."""
        if not self.root:
            print("Tree is empty")
            return
        
        stack = [self.root]  # Initialize a stack with the root node
        
        while stack:
            current = stack.pop()
            print(current.data, end=" ")  # Process the current node
            
            # Push the right child first so the left child is processed first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

"""
-adjacency list

    """

# Functions for unweighted directed graph
def add_edge_unweighted_directed(adj, u, v):
    adj[u].append(v)

# Functions for unweighted undirected graph
def add_edge_unweighted_undirected(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# Functions for weighted directed graph
def add_edge_weighted_directed(adj, u, v, w):
    adj[u].append((v, w))

# Functions for weighted undirected graph
def add_edge_weighted_undirected(adj, u, v, w):
    adj[u].append((v, w))
    adj[v].append((u, w))

# Display function for unweighted graphs
def display_adj_list_unweighted(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(f"{j} ", end="")
        print()

# Display function for weighted graphs
def display_adj_list_weighted(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(f"{{{j[0]}, {j[1]}}} ", end="")
        print()

V = 5  # Number of vertices

# Unweighted Directed Graph
print("Unweighted Directed Graph:")
adj_unweighted_directed = [[] for _ in range(V)]
add_edge_unweighted_directed(adj_unweighted_directed, 0, 1)
add_edge_unweighted_directed(adj_unweighted_directed, 1, 2)
add_edge_unweighted_directed(adj_unweighted_directed, 2, 3)
add_edge_unweighted_directed(adj_unweighted_directed, 3, 4)
display_adj_list_unweighted(adj_unweighted_directed)

# Unweighted Undirected Graph
print("\nUnweighted Undirected Graph:")
adj_unweighted_undirected = [[] for _ in range(V)]
add_edge_unweighted_undirected(adj_unweighted_undirected, 0, 1)
add_edge_unweighted_undirected(adj_unweighted_undirected, 1, 2)
add_edge_unweighted_undirected(adj_unweighted_undirected, 2, 3)
add_edge_unweighted_undirected(adj_unweighted_undirected, 3, 4)
display_adj_list_unweighted(adj_unweighted_undirected)

# Weighted Directed Graph
print("\nWeighted Directed Graph:")
adj_weighted_directed = [[] for _ in range(V)]
add_edge_weighted_directed(adj_weighted_directed, 0, 1, 5)
add_edge_weighted_directed(adj_weighted_directed, 1, 2, 3)
add_edge_weighted_directed(adj_weighted_directed, 2, 3, 1)
add_edge_weighted_directed(adj_weighted_directed, 3, 4, 2)
display_adj_list_weighted(adj_weighted_directed)

# Weighted Undirected Graph
print("\nWeighted Undirected Graph:")
adj_weighted_undirected = [[] for _ in range(V)]
add_edge_weighted_undirected(adj_weighted_undirected, 0, 1, 5)
add_edge_weighted_undirected(adj_weighted_undirected, 1, 2, 3)
add_edge_weighted_undirected(adj_weighted_undirected, 2, 3, 1)
add_edge_weighted_undirected(adj_weighted_undirected, 3, 4, 2)
display_adj_list_weighted(adj_weighted_undirected)



"""
-graph

    """

