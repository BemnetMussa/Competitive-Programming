class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        rows = len(grid)
        cols = len(grid[0])

        maxLocal = [[0]* (cols - 2) for _ in range((rows) -2)]

        for i in range(len(maxLocal)):
            for j in range(len(maxLocal)):

                maxLocal[i][j] = self.max_in_submatrix(grid, (i+ 1, j + 1))

        return maxLocal

    def max_in_submatrix(self, matrix, center):

        row, col = len(matrix), len(matrix[0])
        center_i, center_j = center

        max_value = float('-inf')  

        # Iterate over the 3x3 sub-matrix
        for i in range(center_i - 1, center_i + 2):
            for j in range(center_j - 1, center_j + 2):
                # Check bounds to avoid index errors
                if 0 <= i < row and 0 <= j < col:
                    max_value = max(max_value, matrix[i][j])

        return max_value
