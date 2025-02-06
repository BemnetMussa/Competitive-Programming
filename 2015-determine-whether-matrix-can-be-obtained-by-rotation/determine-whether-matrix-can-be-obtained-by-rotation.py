class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        row = len(mat)
        col = len(mat[0])

        if mat == target:
            return True

        if len(mat) == 0:
            return False

        rotated_mat = self.rotate90(mat, row, col)

        for i in range(1, 4):
            print(rotated_mat)
            if rotated_mat == target:
                return True
            rotated_mat = self.rotate90(rotated_mat, row, col)

        return False


    

    def rotate90(self, mat, row, col):

        new_mat = [[0] * row for _ in range(col)]
        # [[1, 2, 3, 4], [1, 2, 3, 4]]

        for c in range(col):

            # curr  [1, 2, 3, 4]
            if len(mat) != 0:

                mat_list = mat.pop()
                print(mat_list)

                for r in range(row):
                    new_mat[r][c] = mat_list[r]
            print(new_mat)
        print('done')

        return new_mat