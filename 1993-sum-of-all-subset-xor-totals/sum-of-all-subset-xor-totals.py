class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # 5, 1, 6
        # 5
        # 5, 1
        # 5, 1, 6
        # 1, 
        # 1, 6
        # backtracking by iterating through the element 
        # basecase reaching the end of the nums
        res = 0
        def backTracking(i, total):
            nonlocal res
            if i >= len(nums):
                res += total
                return

            backTracking(i+1, total ^ nums[i]) # take
            backTracking(i+1, total) # skip


        backTracking(0, 0)
        return res
