class MinStack:

    def __init__(self):
        self.stack = list()
    def push(self, val: int) -> None:
        
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            min_value = self.stack[-1][1]
            if val < min_value:
                self.stack.append((val, val))
            else:
                self.stack.append((val, min_value))

    def pop(self) -> None:
        last = self.stack[-1][0]
        self.stack = self.stack[:-1]
        return last

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
