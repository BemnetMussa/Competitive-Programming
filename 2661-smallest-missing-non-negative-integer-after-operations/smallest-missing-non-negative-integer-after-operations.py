class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainder_count = [0] * value
        for num in nums:
            remainder_count[num % value] += 1
        
        min_count = min(remainder_count)
        min_index = remainder_count.index(min_count)
        
        return value * min_count + min_index