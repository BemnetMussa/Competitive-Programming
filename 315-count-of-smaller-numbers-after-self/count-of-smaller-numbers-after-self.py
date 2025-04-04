from typing import List, Tuple

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        nums_with_indices = list(enumerate(nums))
        
        self.mergeSort(nums_with_indices, 0, n - 1, result)
        return result

    def mergeSort(self, nums: List[Tuple[int, int]], start: int, end: int, result: List[int]):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid, result)
        self.mergeSort(nums, mid + 1, end, result)
        self.merge(nums, start, mid, end, result)

    def merge(self, nums: List[Tuple[int, int]], start: int, mid: int, end: int, result: List[int]):
        left_pos, right_pos = start, mid + 1
        merged = []
        right_count = 0

        while left_pos <= mid and right_pos <= end:
            if nums[left_pos][1] > nums[right_pos][1]:
                right_count += 1
                merged.append(nums[right_pos])
                right_pos += 1
            else:
                result[nums[left_pos][0]] += right_count
                merged.append(nums[left_pos])
                left_pos += 1

        while left_pos <= mid:
            result[nums[left_pos][0]] += right_count
            merged.append(nums[left_pos])
            left_pos += 1

        while right_pos <= end:
            merged.append(nums[right_pos])
            right_pos += 1

        nums[start:end + 1] = merged
