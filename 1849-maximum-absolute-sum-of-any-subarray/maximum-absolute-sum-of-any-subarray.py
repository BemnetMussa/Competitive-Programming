class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = curr = 0
        res = 0

        for num in nums:
            curr += num
            res = max(res, abs(curr - max_sum), abs(curr - min_sum)) 

            max_sum = max(max_sum, curr)
            min_sum = min(min_sum, curr)

        return res

