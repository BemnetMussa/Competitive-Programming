class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        res = 0
        curr = 0
        l = 0

        for r in range(len(nums)):
            # when it overlaps
            while curr & nums[r]:
                # unmask the the removed num[l]
                curr = curr ^ nums[l]
                l += 1
            # not overlaps
            res = max(res, r - l + 1)
            curr = curr ^ nums[r]
    

        return res