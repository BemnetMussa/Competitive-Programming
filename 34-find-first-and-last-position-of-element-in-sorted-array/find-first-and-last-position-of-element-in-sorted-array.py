class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1


        while (left <= right ):
            
            if nums[left] == target and nums[right] == target:
                return [left, right]

            if nums[left] < target:
                left += 1

            if nums[right] > target:
                right -= 1

        return [-1, -1]