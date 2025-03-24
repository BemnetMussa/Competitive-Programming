class Solution:
    def leftSearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        best = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                best = mid
                right = mid - 1  # Move left to find the first occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return best

    def rightSearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        best = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                best = mid
                left = mid + 1  # Move right to find the last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return best

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.leftSearch(nums, target), self.rightSearch(nums, target)]
