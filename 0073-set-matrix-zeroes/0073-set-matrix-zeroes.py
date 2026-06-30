class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # mark with "$" zeros positon
        rows = len(matrix)
        cols = len(matrix[0])

        def flip(x, y):
            for i in range(rows):
                if matrix[i][y] != "$":
                    matrix[i][y] = 0

            for j in range(cols):
                if matrix[x][j] != "$":
                    matrix[x][j] = 0

            matrix[x][y] = 0
            

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][j] = "$"

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "$":
                    flip(i,j)
                
        
        
        
