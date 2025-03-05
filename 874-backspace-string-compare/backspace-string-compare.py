class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:


        return self.build(s) == self.build(t)
            
    def build(self, str):
        stack = []

        for char in str:
            if char == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
        
        

