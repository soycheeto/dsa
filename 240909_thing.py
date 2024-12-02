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
            
    def delete_node(self, value):
        current = self.head
        prev = None
        if current and current.value == value:
            self.head = current.next
            current = None
            return
        while current and current.value != value:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def search_node(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False



ll = LinkedList()
ll.create_list([1, 2, 3, 4])
ll.append_node_end(5)
ll.append_node_begin(0)
ll.print_list()
print(ll.search_node(3))
print(ll.search_node(10))
ll.delete_node(3)
ll.print_list() 

