class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # to hold the row and col of the zeros
        set_row = set()
        set_col = set()


        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):

                if matrix[i][j] == 0:
                    set_row.add(i)
                    set_col.add(j)

        
        for i in range(row):
            for j in range(col):
                
                if i in set_row or j in set_col:
                    matrix[i][j] = 0

        

        print(matrix)