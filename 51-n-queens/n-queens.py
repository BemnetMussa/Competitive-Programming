class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        postivDiag = set()
        negativeDiag = set()

        board = [["."] * n for _ in range(n)]

        res= []
        def backtrack(r):
            #base case
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n): # for each row
                if c in cols or (r + c) in postivDiag or (r - c) in negativeDiag:
                    continue
                
                cols.add(c)
                postivDiag.add(r+c)
                negativeDiag.add(r-c)
                board[r][c] = "Q"

                backtrack( r + 1 ) # going to the next row

                cols.remove(c)
                postivDiag.remove(r + c)
                negativeDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res
    