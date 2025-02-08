class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])

        ans = []

        i, j = 0, 0
        upward = True  

        while len(ans) < row * col:
            ans.append(mat[i][j])

            if upward:  # Moving upward-right
                if j == col - 1:
                    i += 1  
                    upward = False
                elif i == 0:  
                    j += 1  
                    upward = False
                else:
                    i -= 1 
                    j += 1 

                    
            else:  # Moving downward-left
                if i == row - 1: 
                    j += 1  
                    upward = True
                elif j == 0:  
                    i += 1  
                    upward = True
                else:
                    i += 1  
                    j -= 1 

        return ans
