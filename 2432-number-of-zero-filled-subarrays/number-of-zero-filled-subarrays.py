class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        count = 0
        left = 0

        for right in range(len(nums)):
            curr_num = nums[right]

            if curr_num != 0:
                left = right + 1
                continue

            count += right - left + 1

        return count