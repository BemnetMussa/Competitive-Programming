from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # DFS function must be defined before usage
        def dfs(i, j):
            if (i, j) in visited or board[i][j] == "X":
                return

            visited.add((i, j))
            board[i][j] = "T"

            for x, y in directions:
                ni = x + i
                nj = y + j
                if 0 <= ni < n and 0 <= nj < m:  # Fixed boundary check
                    dfs(ni, nj)

        # Step 1: Mark unsourdounded edges
        visited = set()
        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m-1] == "O":
                dfs(i, m-1)

        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j)
            if board[n-1][j] == "O":
                dfs(n-1, j)
        
        # Step 2: Mark all remaining 'O' as 'X'
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
