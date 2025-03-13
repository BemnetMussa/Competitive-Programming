class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def triangle(idx, prevArr):
            if idx == rowIndex:
                return prevArr
            
            # Build the next row
            nums = [0] * (len(prevArr) + 1)
            for i in range(len(prevArr)):
                nums[i] += prevArr[i]
                nums[i + 1] += prevArr[i]
            
            # Move to the next row recursively
            return triangle(idx + 1, nums)
        
        return triangle(0, [1])
