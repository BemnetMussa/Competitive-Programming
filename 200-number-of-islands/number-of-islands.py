class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def scan(row, col):
            if not inbound(row, col) or grid[row][col] == "0" or (row, col) in visited:
                return

            visited.add((row, col))

            for dx, dy in directions:
                scan(row + dx, col + dy)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    scan(i, j)
                    islands += 1

        return islands
