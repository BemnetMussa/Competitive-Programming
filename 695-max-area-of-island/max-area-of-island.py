class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        max_area = 0
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def scan(row, col):
            if not inbound(row, col) or grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row, col))
            count = 0

            for dx, dy in directions:
                count += scan(row + dx, col + dy)
            
            return count + 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count = scan(i, j)
                    print((i, j), count)
                    max_area = max(max_area, count)
                    

        return max_area