class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def calculatePerimeter(row, col):
            visited[row][col] = True
            ans = 0
            for x, y in directions:
                new_row = row + x
                new_col = col + y
                
                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    ans += 1

                elif not visited[new_row][new_col]:
                    ans += calculatePerimeter(new_row, new_col)

            return ans

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return calculatePerimeter(i, j)
