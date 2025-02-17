class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curr_sum = 0
        prefix_sum = {0: 1}
        res = 0

        for nums in nums:
            curr_sum += nums
            diff = curr_sum - k

            res += prefix_sum.get(diff, 0)

            prefix_sum[curr_sum] =  1 + prefix_sum.get(curr_sum, 0)

        return res