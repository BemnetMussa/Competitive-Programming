'''
- Given m x n integer array grid. robot located at top left conrer tryies to move two bottom right corner. but there is an obstaclae he can take it if it is

return the possible unique paths

function dp(i, j):
    # base cases
    reaching the obstacle
    reaching the destination

    # recrusive relation
    take down or right and check every path
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        # top down approche
        # memo = {}
        # def dp(i, j):
        #     if i >= ROWS or j >= COLS: return 0
        #     if obstacleGrid[i][j] == 1:
        #         return 0
        #     if (i, j) == (ROWS - 1, COLS - 1):
        #         return 1

        #     # memoization
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     # paths
        #     down = dp(i+1, j)
        #     right = dp(i, j+1)

        #     memo[(i, j)] = down + right
        #     return memo[(i, j)]

        # return dp(0, 0) # TIME, SPACE = O(N * M), O(N * M)


        # Bottom-up approch 
        dp = [[0] * (COLS+1) for _ in range(ROWS+1)]

        # Initilaize 
        dp[ROWS-1][COLS-1] = 1

        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        

        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if obstacleGrid[i][j] != 1:
                    if i + 1 < ROWS:
                        dp[i][j] += dp[i+1][j]
                    if j + 1 < COLS:
                        dp[i][j] += dp[i][j+1]

        return dp[0][0]

                





            