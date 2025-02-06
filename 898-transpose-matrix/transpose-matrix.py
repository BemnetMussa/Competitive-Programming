class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        cols = len(matrix[0])

        new_matrix = [[0] * rows for _ in range(cols)]



        for r in range(rows):
            for c in range(cols):

                new_matrix[c][r] = matrix[r][c]

        
        return new_matrix