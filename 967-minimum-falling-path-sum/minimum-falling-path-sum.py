'''
Given:
- Given an n x n array of integers matrix,

Requested:
# - Return the minimum sum of any falling path through matrix.
  - 

'''





class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        
        memo = {}  # for memoization
        
        def dp(i, j):
            if j < 0 or j >= COL:  # out of bounds
                return float('inf')
            if i == ROW - 1:  # last row
                return matrix[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = matrix[i][j] + min(
                dp(i+1, j-1),
                dp(i+1, j),
                dp(i+1, j+1)
            )
            return memo[(i, j)]
        
        return min(dp(0, j) for j in range(COL))  # start from any column in first row


        
