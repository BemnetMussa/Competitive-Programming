class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
         # Step 1: Initialize difference matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Step 2: Apply difference updates for each query
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        
        # Step 3: Build final matrix using prefix sums
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                val = diff[i][j]
                if i > 0:
                    val += mat[i - 1][j]
                if j > 0:
                    val += mat[i][j - 1]
                if i > 0 and j > 0:
                    val -= mat[i - 1][j - 1]
                mat[i][j] = val
        
        return mat