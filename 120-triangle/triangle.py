class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # given array[list][int], 
        # allowed to move to adjucent row belove can move to the next row

        #constraints t <= triangle.length <= 200
        n = len(triangle)

        # @lru_cache(None)
        # def dfs(row, col):
        #     # base case
        #     if row == (n-1):
        #         return triangle[row][col]

        #     # decision
        #     down = dfs(row+1, col)
        #     right = dfs(row+1, col+1)

        #     return triangle[row][col] + min(down, right)

        # return dfs(0, 0)

        # bottom up approch        
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):

                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]