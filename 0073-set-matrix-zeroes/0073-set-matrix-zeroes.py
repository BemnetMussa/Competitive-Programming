'''
Given: m by n integer matrix. if an element is 0 set it's entire row and column to 0
in place.

approch: 
[   [1,0,1],
    [0,0,0],
    [1,0,1]
]

# idetnified the indexs of the 0 and store it on an array[(i, j)]
# going through it and change it's row and column to zero 

O(n) and time of O(n*m)
 optimize: 
 assing the index that we got assign unique character that is *$
 going throug the dollar sign and update it.

O(1) and time of O(n*m)

[   [*,1,2,*],
    [3,4,5,2],
    [1,3,1,5]
]

[   [0,0,0,0],
    [0,4,5,2],
    [0,3,1,5]
]
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # mark zeros in first row/col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # set cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # handle first row/col
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        

