class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Given nums[int] and target: int
        Requested minimum subarry Result where sum(Result) >= target
        len(subarry) minimial 

        Approche 
        target = 7, nums = [2,3,1,2,4,3]
                            _______     -> 5 
                              _______   
                                ______   -> 3
                                    ____  -> 2

        sliding window approche by trackign the window and the sum

        pseudocode
        left = 0

        min_subarray = 0
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_subarray = min(min_subarray, right-left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_subarray
        """

        left = 0

        min_subarray = float("inf")
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_subarray = min(min_subarray, right-left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_subarray if min_subarray != float("inf") else 0