from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Convert 0s to -1s
        for i in range(len(nums)):
            nums[i] = -1 if nums[i] == 0 else 1

        # Compute prefix sum array
        prefix_sum = [0] * (len(nums) + 1)  
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]  
        

        # Dictionary to store the first occurrence of a prefix sum
        index_map = {}
        max_length = 0
        
        # Iterate over prefix_sum array
        for i in range(len(prefix_sum)):
            if prefix_sum[i] in index_map:
                # If prefix sum is seen before, update max_length
                max_length = max(max_length, i - index_map[prefix_sum[i]])
            else:
                # Store the first occurrence of this prefix sum
                index_map[prefix_sum[i]] = i

        return max_length
