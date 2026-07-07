class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        x = 0
        sum = 0
        while n > 0:
            last = n % 10

            if last != 0:
                x = x * 10 + last

            sum += last
            n //= 10

        invers = 0
        while x > 0:
            digit = x % 10
            invers = invers *  10 + digit
            x //= 10
        
        return invers * sum