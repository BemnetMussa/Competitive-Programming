class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        row = len(mat)
        col = len(mat[0])



        for i in range(0, 4):
            if mat == target:
                return True

            mat = self.rotate90(mat, row, col)

        return False


    

    def rotate90(self, mat, row, col):

        new_mat = [[0] * row for _ in range(col)]

        for c in range(col):
            if len(mat) != 0:

                mat_list = mat.pop()
                for r in range(row):
                    new_mat[r][c] = mat_list[r]
      

        return new_mat