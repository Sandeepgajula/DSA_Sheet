class MinStack:

    def __init__(self):
        self.a = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.a.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.a.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.a[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
