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
        """
        Do not return anything, modify matrix in-place instead.
        """     
        ROWS, COLS = len(matrix), len(matrix[0])

        def helper(i, j): # helps to convert the rows and cols of the from the index
            for x in range(ROWS):
                if matrix[x][j] != "*":
                    matrix[x][j] = 0

            for y in range(COLS):
                if matrix[i][y] != "*":
                    matrix[i][y] = 0
            matrix[i][j] = 0

   
        # mark the zero's part
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    matrix[i][j] = "*"

        
        # change rows and cols of the stars *
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == "*":
                    helper(i, j)

        

