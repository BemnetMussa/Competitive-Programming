class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # mark with "$" zeros positon
        rows = len(matrix)
        cols = len(matrix[0])

        sets = set()
            

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    sets.add((i, j))

        for x, y in sets:
            for i in range(rows):
                matrix[i][y] = 0
            for j in range(cols):
                matrix[x][j] = 0
            
           
                
        # O(n^3) -> O(n^2)