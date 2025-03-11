class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def trailing(n):
            if n == 1 or n == 0 :
                return 1

            return n * trailing(n-1)

        val = trailing(n)

        count = 0

        while val % 10 == 0:

            count += 1

            val //= 10

        return count