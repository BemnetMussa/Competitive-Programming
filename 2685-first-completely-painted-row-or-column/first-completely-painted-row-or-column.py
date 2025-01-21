class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        pos = {}
        
        for i in range(row):
            for j in range(col):
                pos[mat[i][j]] = (i, j)
        
        rCnt = [0] * row
        cCnt = [0] * col
        
        for i, val in enumerate(arr):
            r, c = pos[val]
            rCnt[r] += 1
            cCnt[c] += 1
            if rCnt[r] == col or cCnt[c] == row:
                return i
        return len(arr) - 1