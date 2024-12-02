def find_largest_and_smallest(arr):
    if len(arr) == 0:
        return "Array is empty!"

    largest = max(arr)
    smallest = min(arr)
    
    return largest, smallest

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)
class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node

class SinglyLinkedList:
    """Class to represent a singly linked list."""
    def __init__(self):
        self.head = None  # Head of the list

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, data):
        """Delete the first node with the given data."""
        temp = self.head

        # If the head itself holds the data to be deleted
        if temp is not None and temp.data == data:
            self.head = temp.next
            temp = None
            return

        # Search for the node to be deleted
        prev = None
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next

        # If the data was not found in the list
        if temp is None:
            print(f"Data {data} not found in the list.")
            return

        # Unlink the node from the list
        prev.next = temp.next
        temp = None

    def traverse(self):
        """Traverse and print the linked list."""
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node


class Stack:
    """Class to represent a stack using a singly linked list."""
    def __init__(self):
        self.top = None  # Pointer to the top of the stack

    def push(self, data):
        """Push an element onto the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Pop the top element from the stack."""
        if self.is_empty():
            print("Stack underflow! Cannot pop from an empty stack.")
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        """Return the top element of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None


class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node


class Queue:
    """Class to represent a queue using a singly linked list."""
    def __init__(self):
        self.front_node = None  # Pointer to the front of the queue
        self.rear_node = None   # Pointer to the rear of the queue

    def enqueue(self, data):
        """Add an element to the end of the queue."""
        new_node = Node(data)
        if self.rear_node is None:  # If the queue is empty
            self.front_node = self.rear_node = new_node
            return
        self.rear_node.next = new_node
        self.rear_node = new_node

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            print("Queue underflow! Cannot dequeue from an empty queue.")
            return None
        dequeued_node = self.front_node
        self.front_node = self.front_node.next
        if self.front_node is None:  # If the queue becomes empty
            self.rear_node = None
        return dequeued_node.data

    def front(self):
        """Return the front element of the queue without removing it."""
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        return self.front_node.data

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front_node is None


class DoublyNode:
    """Class to represent a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    """Class to represent a doubly linked list."""
    def __init__(self):
        self.head = None  # Pointer to the head of the list

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = DoublyNode(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, data):
        """Delete the first node with the given data."""
        temp = self.head

        # Search for the node to be deleted
        while temp is not None and temp.data != data:
            temp = temp.next

        # If the node was not found
        if temp is None:
            print(f"Data {data} not found in the list.")
            return

        # Update the pointers to delete the node
        if temp.prev is not None:
            temp.prev.next = temp.next
        else:
            self.head = temp.next  # Node to delete is the head

        if temp.next is not None:
            temp.next.prev = temp.prev

        temp = None

    def traverse_forward(self):
        """Traverse and print the list forward."""
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Traverse and print the list backward."""
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        # Go to the end of the list
        while current.next:
            current = current.next
        # Traverse backward
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

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


from collections import deque

class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}  # Dictionary to store the adjacency list

    def add_edge(self, v, w):
        """Add an edge between vertices v and w (undirected graph)."""
        if v not in self.graph:
            self.graph[v] = []
        if w not in self.graph:
            self.graph[w] = []
        
        self.graph[v].append(w)
        self.graph[w].append(v)

    def bfs(self, start_vertex):
        """Perform BFS starting from the start_vertex."""
        visited = set()  # Set to track visited vertices
        queue = deque([start_vertex])  # Queue for BFS
        visited.add(start_vertex)  # Mark the start vertex as visited
        
        while queue:
            vertex = queue.popleft()  # Dequeue a vertex from the queue
            print(vertex, end=" ")  # Print the vertex (or process it)

            # Enqueue all unvisited adjacent vertices of the current vertex
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


