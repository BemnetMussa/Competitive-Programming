class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        op = 0

        left = 0
        right = len(nums) -1 

        nums.sort()
        
        while (left < right):
            zsum = nums[left] + nums[right]

            if zsum == k:
                left += 1
                right -= 1
                op += 1

            elif zsum > k:
                right -= 1

            else:
                left += 1

        return op
        