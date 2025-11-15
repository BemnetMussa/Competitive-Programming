'''
given m by n grid which represents a map of '1' land and '0' water. return the number of islands.
requested: to get the number of islands that are surrounded by water. 
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]


'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def backTracking(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return

            if grid[i][j] == "0" or visited[i][j]:
                return
            
            visited[i][j] = True
            for dx, dy in directions:
                nx, ny = dx + i, dy + j
                backTracking(nx, ny)

        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and not visited[i][j]:
                    backTracking(i, j)
                    res += 1

        return res


        