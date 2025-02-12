class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        a = 0
        b = int(math.sqrt(c))

        while(a <= b):
            value = a**2 + b**2
            if (value == c):
                return True
            elif value < c:
                a += 1

            else:
                b -= 1

        return False