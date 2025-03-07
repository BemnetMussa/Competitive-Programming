
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for c in tokens:
            if c in "+-*/":
                opr = stack.pop()
                ope = stack.pop()

                if c == "+":
                    result = ope + opr
                elif c == "-":
                    result = ope - opr
                elif c == "*":
                    result = ope * opr
                elif c == "/":
                    result = int(ope/opr) if ope/opr > 0 else math.ceil(ope/opr)
                
                stack.append(result)
       
            else:
                stack.append(int(c))
             
   

        return stack[0]

