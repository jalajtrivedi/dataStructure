class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
    
    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            raise OverflowError("Overflow: Stack is full")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Underflow: Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0

def evaluate_postfix(expression):
    stack = Stack(len(expression))
    
    for ch in expression:
        if ch.isdigit():
            stack.push(int(ch))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if ch == '+':
                stack.push(operand1 + operand2)
            elif ch == '-':
                stack.push(operand1 - operand2)
            elif ch == '*':
                stack.push(operand1 * operand2)
            elif ch == '/':
                stack.push(int(operand1 / operand2))  

    return stack.pop()

expression = "512+4*+3-"
result = evaluate_postfix(expression)
print("Result of the postfix expression:", result)