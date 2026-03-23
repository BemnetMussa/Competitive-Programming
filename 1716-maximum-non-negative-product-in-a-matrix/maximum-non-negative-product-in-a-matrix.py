class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) ,len(grid[0])
        MOD = 10**9 + 7

        @lru_cache(None)
        def backtracing(i, j):
            if i == rows -1 and j == cols -1:
                return (grid[i][j], grid[i][j])
            
            res_max = float("-inf")
            res_min = float("inf")

            val = grid[i][j]
            if i + 1 < rows:
                mx, mn = backtracing(i+1, j)
                candiates = [val * mx, val * mn]
                res_max = max(res_max, max(candiates))
                res_min = min(res_min, min(candiates))

            if j + 1 < cols:
                mx, mn = backtracing(i, j+1)
                candiates = [val * mx, val * mn]
                res_max = max(res_max, max(candiates))
                res_min = min(res_min, min(candiates))

            return (res_max, res_min)

        zmax, _ = backtracing(0, 0)
        return zmax % MOD if zmax >= 0 else -1

                
                
                