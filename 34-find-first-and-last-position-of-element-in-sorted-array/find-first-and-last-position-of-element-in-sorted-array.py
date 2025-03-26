# class Solution:
#     def leftSearch(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         best = -1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 best = mid
#                 right = mid - 1  # Move left to find the first occurrence
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return best

#     def rightSearch(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         best = -1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 best = mid
#                 left = mid + 1  # Move right to find the last occurrence
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return best

#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         return [self.leftSearch(nums, target), self.rightSearch(nums, target)]


import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the leftmost occurrence using bisect_left
        left = bisect.bisect_left(nums, target)
        
        # Check if target exists in the list
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        # Find the rightmost occurrence using bisect_right
        right = bisect.bisect_right(nums, target) - 1
        
        return [left, right]

