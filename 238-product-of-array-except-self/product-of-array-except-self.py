class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # answer default values 1
        ans = [1] * len(nums)


        # preforming the prefix product
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        
        # preforming the postfix product
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        
        # Time and space complexity with O(n) and O(1) respectively
        return ans