class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def issafe(r,c):
            n = len(board)
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
                if r - i >= 0 and c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                if r - i >= 0 and c + i < n and board[r-i][c+i] == 'Q':
                    return False
            return True
                
        def solve(r):
            n = len(board)
            if r == n:
                print(board)
                ans.append(["".join(i) for i in board])
                return 
            for c in range(0,n):
                if issafe(r,c):
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.'

                    
        board = [['.']*n for i in range(n)]
        ans =[]
        solve(0) 
        return ans
