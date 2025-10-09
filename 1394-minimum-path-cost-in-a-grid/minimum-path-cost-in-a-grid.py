class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
      
        # Given matrix[][] m x n, contains distinct integers. 
        # can move to any other cell. each move has a cost moveCost[i][j] from i to j.
        # requested to get the minimum path that cost minimum. from the first row one of the cell to the end of any cell last row.

        # approch will be dp
        # start with top - down approch 
        ROWS, COLS = len(grid), len(grid[0])

        @lru_cache(None)
        def dp(i, j):
            if i == ROWS - 1:
                return grid[i][j]

            val = grid[i][j]
            min_cost = float("inf")
            for next_col in range(COLS):
                move = moveCost[val][next_col]
                min_cost = min(min_cost, val + move + dp(i + 1, next_col))


            return min_cost

        return min(dp(0, j) for j in range(COLS))

