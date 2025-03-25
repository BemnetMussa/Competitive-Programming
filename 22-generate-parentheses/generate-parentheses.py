class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []


        def generate(open, close):
            if open == close == n:
                res.append(''.join(stack))
                return

            if open < n:
                stack.append('(')
                generate(open + 1, close)

                stack.pop()
            if close < open:
                stack.append(')')
                generate(open, close + 1)
                stack.pop()

        generate(0, 0)

        return res