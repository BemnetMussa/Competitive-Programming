class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        given: nums array and K integer
        req: find number of subarry where there score is less than k, subarry is contigious
        soln: sliding thorugh the nums and counting the subarries along the way with O(N)
        
        to handle the middle count i will count the lngth on the subarries 
        
        """
        subarries_count = 0
        curr_sum = 0

        left = 0
        for right in range(len(nums)):
          
            curr_sum += nums[right]

            while curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
                
            subarries_count += (right - left + 1)

            

        return subarries_count