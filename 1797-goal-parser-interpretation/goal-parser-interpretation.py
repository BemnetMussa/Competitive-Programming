class Solution:
    def interpret(self, command: str) -> str:
        charList = list(command)

   
        ans = ''
        stack = []
    
        for char in charList:

            if char == 'G':
                ans += 'G'

            elif char == "a":
                ans += "al"

            elif char == ")" and stack[-1] == "(":
                ans += 'o'

            stack.append(char)


        return ans