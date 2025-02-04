class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        

        for i in range(len(nums)):

            for j in range(i, len(nums)):
                
                index = abs(i-j)
                value = abs(nums[i] - nums[j])

                if index >= indexDifference and value >= valueDifference:
                    return [i, j]


        return [-1, -1]
