class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        # keeping the totals
        total = sum(nums)


        left = 0

        for i in range(len(nums)):
            if total - left - nums[i] == left:
                return i

            left += nums[i]

        return -1
