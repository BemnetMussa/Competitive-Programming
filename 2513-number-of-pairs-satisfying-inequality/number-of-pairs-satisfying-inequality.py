from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # Build array of differences and start modified merge sort
        arr = [a - b for a, b in zip(nums1, nums2)]
        return self.merge_sort(arr, 0, len(arr) - 1, diff)

    def merge_sort(self, arr: List[int], l: int, r: int, diff: int) -> int:
        # Sort arr[l:r] and count valid pairs
        if l >= r:
            return 0
        m = (l + r) // 2
        count = self.merge_sort(arr, l, m, diff) + self.merge_sort(arr, m + 1, r, diff)
        count += self.count_pairs(arr, l, m, r, diff)  # count cross pairs
        self.merge(arr, l, m, r)  # merge sorted halves
        return count

    def count_pairs(self, arr: List[int], l: int, m: int, r: int, diff: int) -> int:
        # Count pairs (i, j) with i in left half, j in right half, satisfying arr[i] <= arr[j] + diff
        count, j = 0, m + 1
        for i in range(l, m + 1):
            while j <= r and arr[i] > arr[j] + diff:
                j += 1
            count += (r - j + 1)
        return count

    def merge(self, arr: List[int], l: int, m: int, r: int) -> None:
        # Merge two sorted halves arr[l:m] and arr[m+1:r]
        temp = []
        i, j = l, m + 1
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i]); i += 1
            else:
                temp.append(arr[j]); j += 1
        temp.extend(arr[i:m+1])
        temp.extend(arr[j:r+1])
        arr[l:r+1] = temp
