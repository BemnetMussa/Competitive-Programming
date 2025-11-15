'''
Given: array nums[int] in ascending order & distinct values
Requested: to get the index of the target: int value inside the nums otherwise **return -1
constrinats: time (O(logn))
approch: to use O(logn) approch using binary search

psudcode: 
left = 0

'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
