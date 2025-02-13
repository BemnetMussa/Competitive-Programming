class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       

        max_len  = 0

        left = 0

        for right in range(len(nums)):
            
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

       
        

        return max_len 
            
            
