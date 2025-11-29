class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        total_sum = sum(nums)
        return total_sum % k # returns the reminder