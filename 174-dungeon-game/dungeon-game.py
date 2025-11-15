'''
Given *bottom-right corner. given m x n grid. night positioned at top-left corner
- given intial health start from the top-left corner and rescue the princess. along the way demons represented by negative numbers & health point as postivie it increase and decresase altneratevely based on the numbers

return the minimum health point to start with


approche: 
bottom up approch 

create a matrix.copy
already intialized

starting from the queen go each possiblity
choose the maxmmum one and add it.
'''

                
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (COLS + 1) for _ in range(ROWS + 1)]

        # Minimum health needed at the princess's cell
        dp[ROWS][COLS - 1] = dp[ROWS - 1][COLS] = 1

        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
        print(dp)
        return dp[0][0]








