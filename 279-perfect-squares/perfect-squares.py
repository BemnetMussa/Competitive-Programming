class Solution:
    def numSquares(self, n: int) -> int:
        # given n: integer 
        # requested to return least number of perfect square numbers that sum up to n

        # approche: dp approche since to consider every possiblity 
        # Top-down approch 
        squares = [i*i for i in range(1, isqrt(n)+1)]

        # @lru_cache(None)
        # def dp(remaining):
        #     if remaining == 0:
        #         return 0

        #     min_count = float('inf')
        #     for sq in squares:
        #         if sq <= remaining:
        #             min_count = min(min_count, 1 + dp(remaining - sq))

        #     return min_count

        # return dp(n)

        # Bottom up approch:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for num in range(1, n+1):
            for sq in squares:
                if sq <= num:
                    dp[num] = min(dp[num], 1 + dp[num - sq])

        return dp[n]
        

