class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        # Check rows and columns for duplicates
        for i in range(row):
            if not self.isValid(board[i]):  
                return False
            if not self.isValid([board[j][i] for j in range(col)]):  
                return False

        # Check 3x3 sub-grids
        for i in range(0, row, 3):
            for j in range(0, col, 3):
                if not self.checkSubGrid(board, i, j):
                    return False

        return True

    def isValid(self, unit: List[str]) -> bool:
        seen = set()
        for char in unit:
            if char != ".":
                if char in seen:
                    return False
                seen.add(char)
        return True




    def checkSubGrid(self, board, r, c):
    
        seen = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                char = board[i][j]
                if char != ".":
                    if char in seen:
                        return False
                    seen.add(char)
        return True
