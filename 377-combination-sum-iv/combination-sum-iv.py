class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Given distict nums[int] and target :int
        # requested to get possible combinations that adds up to target.
        # constraint 1 <= n <= 200 & 1 <= m <= 1000

        # approche: since every combination will be considered then recursive approche will be the way to go DP
        
        n = len(nums)
        # # Top-Down approch

        # @lru_cache(None)
        # def dp(curr_sum):
        #     if curr_sum == target:
        #         return 1
        #     if curr_sum > target:
        #         return 0

        #     comb = 0
        #     for i in range(n):
        #         comb += dp(curr_sum + nums[i])

        #     return comb

        # return dp(0) # O(2^m) time and space complexity

        # Bottom-Down approch
        dp = [0] * (target + 1)
        dp[0] = 1  # base case: one way to make sum 0

        for total in range(1, target + 1):
            for num in nums:
                if total - num >= 0:
                    dp[total] += dp[total - num]

        return dp[target] # O(m*n)

