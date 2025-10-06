class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        given a non-negative grid 
        requested to move from top-left to bottom-right corner 
            - choose best path that have minimum cost
            - allowed moves down or right only **

        approch:
        - since we  can't know which is the best path unless if we go through that pass. 
        talking: because sorthing will cause inordering it form it's original order. as a result we need to go through each path and choose the best path.

        --> recursive approche: starting from top-left and going through each node by taking the options of righ tand bottom paths

        state: node
        base_case: reach the bottom-right corner 
        recurive relation: dp(node.right) + dp(node.bottom)


        *since it is a grid m * n
        psudocode;

        M, N = len(grid), len(grid[0])
        function dp(i, j):
            if i > M-1 or j > N-1: # if out of bound
                return flaot("inf")
                
            if (i, j) == (M-1, N-1): # reached the bottom right corner
                return grid[i][j]
            
            if (i, j) in memo: # if it is already computed
                reutrn memo[(i, j)]

            right = dp(i+1, j)
            bottom = dp(i, j+1)

            memo[(i, j)] = grid[i][j] + min(right, bottom)  # memorization on (i, j) no need to go again
            
            return memo[(i, j)]

        """

        M, N = len(grid), len(grid[0])

        memo = {}
        def dp(i, j):
            if i > M-1 or j > N-1:
                return float("inf")
                
            if (i, j) == (M-1, N-1):
                return grid[i][j]
            
            if (i, j) in memo:
                return memo[(i, j)]

            right = dp(i+1, j)
            bottom = dp(i, j+1)

            memo[(i, j)] = grid[i][j] + min(right, bottom) 
            
            return memo[(i, j)]

        return dp(0, 0)