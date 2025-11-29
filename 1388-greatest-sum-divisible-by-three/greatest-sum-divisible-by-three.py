from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        
        # Separate numbers by remainder mod 3
        rem1 = sorted([x for x in nums if x % 3 == 1])
        rem2 = sorted([x for x in nums if x % 3 == 2])
        
        if total % 3 == 0:
            return total
        
        ans = 0
        if total % 3 == 1:
            option1 = total - (rem1[0] if rem1 else float('inf'))
            option2 = total - (sum(rem2[:2]) if len(rem2) >= 2 else float('inf'))
            ans = max(option1, option2)
        else:  # total % 3 == 2
            option1 = total - (rem2[0] if rem2 else float('inf'))
            option2 = total - (sum(rem1[:2]) if len(rem1) >= 2 else float('inf'))
            ans = max(option1, option2)
        
        return ans if ans != float('inf') else 0
