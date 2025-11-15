class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # a = first, b = second, c = thrid 
        # a + c == b True
        # 1 2 1 4 1 
        #     _ _ _

        valid_subarry = 0

        for right in range(2, len(nums)):
            a = nums[right - 2]
            b = nums[right - 1]
            c = nums[right]
            
            if a + c == b/ 2:
                valid_subarry += 1
            

        return valid_subarry