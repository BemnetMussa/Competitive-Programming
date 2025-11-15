class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        # Step 1: find pivot
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: binary search on descending suffix
            left, right = i + 1, n - 1
            target = nums[i]
            while left < right:
                mid = (left + right + 1) // 2  # bias right for descending
                if nums[mid] > target:
                    left = mid
                else:
                    right = mid - 1
            # left now points to smallest number > nums[i]
            nums[i], nums[left] = nums[left], nums[i]

        # Step 3: reverse suffix in-place
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
