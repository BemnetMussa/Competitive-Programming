class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = [row[:] for row in matrix]  # copy matrix for DP
        
        for i in range(1, ROW):
            for j in range(COL):
                dp[i][j] += min(
                    dp[i-1][j], 
                    dp[i-1][j-1] if j-1 >= 0 else float('inf'), 
                    dp[i-1][j+1] if j+1 < COL else float('inf')
                )
        
        return min(dp[-1])