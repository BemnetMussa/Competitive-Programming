class Solution:
    def tribonacci(self, n: int) -> int:
        """
        n = 4
        0, 1, 1, 2, 4 = 4


        """

        # memo = defaultdict(int)
        # def dp(n):
        #     if n <= 0:
        #         return 0
        #     if n == 1:
        #         return 1

        #     if memo[n]: return memo[n]

        #     memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
        #     return memo[n]

        # bottom up approche
        # initialize the memoization
        dp = [0 for _ in range(n+1)]
        
        if n == 0:
            return 0
        if n < 3:
            return 1
        # base cases
        dp[1], dp[2] = 1, 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[-1]