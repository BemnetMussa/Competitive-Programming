class Solution:
    def solveNQueens(self, n: int):
        cols = [False] * n
        posDiag = [False] * (2 * n - 1)   # r + c
        negDiag = [False] * (2 * n - 1)   # r - c + (n-1)

        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                pd = r + c
                nd = r - c

                if cols[c] or posDiag[pd] or negDiag[nd]:
                    continue

                cols[c] = posDiag[pd] = negDiag[nd] = True
                board[r][c] = "Q"

                backtrack(r + 1)

                board[r][c] = "."
                cols[c] = posDiag[pd] = negDiag[nd] = False

        backtrack(0)
        return res