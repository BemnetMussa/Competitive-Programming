class MyQueue:

    def __init__(self):
        self.stack1 = [] #adding
        self.stack2 = [] #removing 
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2 = self.stack1[::-1]
      

    def pop(self) -> int:
        if not self.empty():
            poped = self.stack2.pop()
            self.stack1 = self.stack2[::-1]
            return poped
        

    def peek(self) -> int:
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()