class Solution:
    def tribonacci(self, n: int) -> int:
        """
        n = 4
        0, 1, 1, 2, 4 = 4


        """

        memo = defaultdict(int)
        def dp(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1

            if memo[n]: return memo[n]

            memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
            return memo[n]

        return dp(n)