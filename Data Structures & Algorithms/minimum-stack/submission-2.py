class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> int:
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        
        self.stack.append(val)

    def pop(self) -> int:
        if self.isEmpty():
            return "Stack is empty"
            
        self.stack.pop()
        self.min_stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0

    def top(self) -> int:
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def getMin(self) -> int:
        if self.isEmpty():
            return "Stack is empty"
        return self.min_stack[-1]
