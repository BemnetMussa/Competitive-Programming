class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumlator = 0

        for i in range(len(nums)):
            accumlator += nums[i]
            nums[i] = accumlator

        
        return nums