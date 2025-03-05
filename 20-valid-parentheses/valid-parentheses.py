class Solution:
    def isValid(self, s: str) -> bool:
        zmap = {
            "(": ")",
            "[": "]",
            "{": "}"
        }


        stack =[]

        for char in s:
            if char in zmap.keys():
                stack.append(char)
            elif stack and zmap[stack[-1]] == char:
                stack.pop()
            else:
                return False

        return stack == []