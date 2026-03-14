class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        1. states:
                    dp[m][n]
        2. transitions: 
                    dp[m][n] = dp[m-1][n] + dp[m][n-1] # top + left
        3. baseCase:
                    when we reach the (m-1, n-1). 
        '''
        # memo = {}
        # def dp(i, j):
        #     # basecase
        #     if not(0 <= i < m) or not(0 <= j < n):
        #         return 0
        #     if (i, j) == (m-1, n-1): # final postioin 
        #         return 1

        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     # Transitoin
        #     answer = dp(i+1, j) + dp(i, j+1)
        #     memo[(i, j)] = answer
        #     return answer
        # return dp(0, 0)

        # 1. state space
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # 2. intializing the base case
        for i in range(m):
            for j in range(n):
                dp[i][j] = 1

        # 3. transition
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # 4. result
        return dp[m-1][n-1]

        