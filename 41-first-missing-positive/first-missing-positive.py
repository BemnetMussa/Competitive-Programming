class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(max(nums)+1):
            if i + 1 not in nums:
                return i + 1

        return 1