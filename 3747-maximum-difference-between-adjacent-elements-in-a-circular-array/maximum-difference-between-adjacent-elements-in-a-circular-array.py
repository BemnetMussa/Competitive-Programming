class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        max_diff = float("-inf")

        for i in range(len(nums)):
            max_diff = max(max_diff, abs(nums[(i+1) % len(nums)] - nums[i]))


        return max_diff