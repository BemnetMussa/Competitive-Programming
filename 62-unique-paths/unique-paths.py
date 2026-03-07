class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''

        '''

        # Step 1: state space
        bottom_up = [[0] * (n) for _ in range(m)]

        # Step 2: Intialize the state space
        for i in range(m):
            for j in range(n):
                bottom_up[i][j] = 1
        

        # Step 3: tranation of states
        # Step 4: fill in proper strcutre
        for i in range(1, m):
            for j in range(1, n):
                bottom_up[i][j] = bottom_up[i-1][j] + bottom_up[i][j-1] # top + left

        print(bottom_up)
        return bottom_up[m-1][n-1]

        
        # memo = {}
        # def dp(i, j):
        #     if i > m-1 or j > n-1:
        #         return 0
        #     if (i, j) == (m-1, n-1):
        #         return 1
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     memo[(i, j)] =  dp(i+1, j) + dp(i, j+1)
        #     return memo[(i, j)]
        
        # return dp(0, 0)