class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col = len(matrix[0])
        row = len(matrix)

        self.prefix_matrix = [[0]* (col + 1) for _ in range(row+1)]

        for i in range(row):
            for j in range(col):

                self.prefix_matrix[i][j] = self.prefix_matrix[i-1][j] + self.prefix_matrix[i][j-1] - self.prefix_matrix[i-1][j-1] + matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_matrix[row2][col2] - self.prefix_matrix[row2][col1 -1] -self.prefix_matrix[row1-1][col2] + self.prefix_matrix[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)