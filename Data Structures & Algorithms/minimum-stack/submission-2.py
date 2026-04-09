class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.size > 0:
            curr_min = self.stack[self.size - 1][1]
            self.stack.append((val, min(val, curr_min)))
        else:
            self.stack.append((val, val))
        
        self.size += 1

    def pop(self) -> None:
        if self.size > 0:
            curr_min = self.stack[self.size - 1][1]
            pop_ele = self.stack.pop()
            self.size -= 1

    def top(self) -> int:
        if self.size > 0:
            return self.stack[self.size-1][0]

    def getMin(self) -> int:
        if self.size > 0:
            return self.stack[self.size - 1][1]
