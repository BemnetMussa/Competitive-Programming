class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]

        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i - 1][j - 1]
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):

                if row - k < 0:
                    row1 = 0
                else:
                    row1 = row - k
                

                if row + k >= len(mat):
                    row2 = len(mat) - 1
                else:
                    row2 = row + k
                
                if col - k < 0:
                    col1 = 0
                else:
                    col1 = col - k
                
                if col + k >= len(mat[0]):
                    col2 = len(mat[0]) - 1
                else:
                    col2 = col + k
                

                mat[row][col] = prefix[row2 + 1][col2 + 1] - prefix[row2 + 1][col1] - prefix[row1][col2 + 1] + prefix[row1][col1]

            
        return mat
