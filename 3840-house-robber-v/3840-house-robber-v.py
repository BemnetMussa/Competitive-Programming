class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        
        # looking at differnet approches - dp
        if len(nums) < 2:
            return nums[0]
        dp = [0] * len(nums)

        dp[0] = nums[0]
        if colors[1] == colors[0]:
            dp[1] = max(nums[0], nums[1])
        else:
            dp[1] = nums[0] + nums[1]

        for i in range(2, len(nums)):
            res = dp[i-1]
            if colors[i] == colors[i-1]:
                res = max(res, nums[i] + dp[i-2])
            else:
                res += nums[i]

            dp[i] = res
        return dp[-1] # time complexity: O(n), Space compelxity: O(n)