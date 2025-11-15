class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
            
        if xor != 0:
            return len(nums)
        elif any(num != 0 for num in nums):
            return len(nums) - 1
        else:
            return 0
