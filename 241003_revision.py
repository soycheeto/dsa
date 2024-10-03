numbers = [1, 3, 4, 6, 8, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
average_even = sum(even_numbers) / len(even_numbers)
print(average_even)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(8)
head.next.next.next.next = Node(9)

current = head
while current.next:
    current = current.next

last_element = current.value
is_multiple_of_3 = last_element % 3 == 0
print(last_element, is_multiple_of_3)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

stack = Stack()
for i in range(5):
    stack.push(i + 1)

if stack.stack and stack.stack[-1] % 2 == 0:
    stack.pop()
print(stack.stack)
