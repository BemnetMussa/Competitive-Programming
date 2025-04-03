class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums) # for fast look ups
        index = 0

        for i in range(len(nums)+1):
            if not(i in nums):
                index = i

        return index