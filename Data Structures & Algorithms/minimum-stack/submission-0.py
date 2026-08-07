class MinStack:
    # not store the val itself but their difference
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack: # if is empty stack
            self.stack.append(0) 
            # append the difference between val(new min) and preious val(current min)(0 for 1st min)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
        
    def pop(self) -> None:
        if not self.stack:
            return
        p = self.stack.pop()
        if p < 0:
            self.min = self.min - p

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min # top one is not min
        else:
            return self.min # top one is min

    def getMin(self) -> int:
        return self.min
        
