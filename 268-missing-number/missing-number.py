class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2 # sum of the first n numbers
        actual_sum = sum(nums) # actual sum

        return total_sum - actual_sum # the missing one
