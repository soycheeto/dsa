class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) is None

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return f"pop from empty stack"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return"peek from empty stack"

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
