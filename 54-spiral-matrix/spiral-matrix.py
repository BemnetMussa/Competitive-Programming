from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        while matrix:  # Keep going until matrix is empty

            # Step 1: pop the fisrt one
            ans.extend(matrix.pop(0))
            
            # Step 2: Pop the last element of each remaining row 
            if matrix:
                for row in matrix:
                    if row: 
                        ans.append(row.pop())
            
            # Step 3: Pop the last row in reverse order 
            if matrix:
                ans.extend(matrix.pop()[::-1])
            
            # Step 4: Pop the first element of each remaining row from bottom to top 
            if matrix:
                for i in range(len(matrix) - 1, -1, -1):
                    if matrix[i]: 
                        ans.append(matrix[i].pop(0))
        
        return ans
33