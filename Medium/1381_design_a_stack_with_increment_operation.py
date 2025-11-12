class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        def isFull():
            return len(self.stack) == self.capacity
        
        if not isFull():
            self.stack.append(x)

    def pop(self) -> int:
        def isEmpty():
            return len(self.stack) == 0

        if isEmpty():
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
