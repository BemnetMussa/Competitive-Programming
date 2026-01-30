from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)
        
        # If total sum is odd, no partition can have even difference
        if total_sum % 2 != 0:
            return 0
        
        # Otherwise, every partition (n-1 of them) is valid
        return n - 1
