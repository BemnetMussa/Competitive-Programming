class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(x, y):
            res = 1
            while y:
                if y % 2:
                    res = (res * x) % MOD
                x = (x * x) % MOD
                y //= 2
            return res
        
        even = (n + 1) // 2
        odd = n // 2
        
        return (power(5, even) * power(4, odd)) % MOD
