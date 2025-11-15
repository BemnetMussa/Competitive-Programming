'''
task: desing a object class MinStack that have funcionalites of:
- MinStack() --> intializing the stack object
- Void push(int val)--> adding an elemetn to the stack
- Void pop() --> poping an element form a stack
- int top() --> return the top elemtn form the stack
- int getMin() --> getMin()?? getting the smallest elemtn from the stack.

need Additional data strcutre?
 - heap() since O(logn) --> X
 - two stacks that holds stack and minStack at each level

["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]


should have used montinonic two stacks
stack
minStack -> which holds minimum value at each stack level

'''


class MinStack:
    def __init__(self):
        self.stack = [] # -2, 0, -1
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop() # 1
        self.minStack.pop()
        
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your Minstack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()