class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0

def is_balanced(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        else:
            if char in closing_brackets:
                if stack.is_empty():
                    return False
                if stack.pop() != bracket_pairs[char]:
                    return False
    
    if stack.is_empty():
        return True
    else:
        return False

expression1 = "([]{})"
expression2 = "([)]"

print("Balanced?", is_balanced(expression1))  
print("Balanced?", is_balanced(expression2))  
