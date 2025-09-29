class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Given nums[int],
        Requested to get the longest strictly increasing subsequence. *len

        soltion
            -  nums = [10,9,2,5,3,7,101,18]

        for each index finding the longest strictely increasing subsequence 

        state = idx
        base_case = reaching the end of length
        recursive relation = dp(idx+1) iteraton 
        psudocode

        memo = {}
        function dp(idx):
            for idx >= len(nums):
                return 1
            if idx in memo:
                return memo[idx]

            length = 0
            for i in range(idx+1, len(nums)):
                
                if nums[i] > nums[idx]:
                    length += dp(i)

            memo[idx] = length
            return length

        """
        memo = {}
        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            length = 1 # at least it self
            for i in range(idx+1, len(nums)):
                if nums[i] > nums[idx]:
                    length = max(length, dp(i)+1)
            
            memo[idx] = length
            return length

        return max([dp(i) for i in range(len(nums))])
