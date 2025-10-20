class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def backtrack(i, j, idx):
            if idx == len(word):
                return True
            if (i < 0 or i >= ROWS or
                j < 0 or j >= COLS or
                word[idx] != board[i][j] or
                (i, j) in path):
                return False

            path.add((i, j))
            res = (backtrack(i + 1, j, idx + 1) or
                   backtrack(i - 1, j, idx + 1) or
                   backtrack(i, j + 1, idx + 1) or
                   backtrack(i, j - 1, idx + 1))
            path.remove((i, j))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        return False
