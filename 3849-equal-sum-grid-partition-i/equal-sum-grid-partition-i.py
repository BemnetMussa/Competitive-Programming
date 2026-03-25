class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        if total % 2 != 0:
            return False
        
        # Horizontal cut
        curr = 0
        for i in range(rows - 1):
            curr += sum(grid[i])
            if curr == total - curr:
                return True
        
        # Column sums
        col_sums = [0] * cols
        for i in range(rows):
            for j in range(cols):
                col_sums[j] += grid[i][j]
        
        # Vertical cut
        curr = 0
        for j in range(cols - 1):
            curr += col_sums[j]
            if curr == total - curr:
                return True
        
        return False