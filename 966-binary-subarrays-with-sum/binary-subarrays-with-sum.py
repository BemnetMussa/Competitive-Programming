class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        

        # prefix map
        prefix = { 0: 1 }

        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - goal
            res += prefix.get(diff, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

  


        return res
