from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        count = 0

        def backtrack(i, curr_or):
            nonlocal max_or, count
            if i == len(nums):
                if curr_or == max_or:
                    count += 1
                elif curr_or > max_or:
                    max_or = curr_or
                    count = 1
                return

            backtrack(i + 1, curr_or | nums[i])  # include nums[i]
            backtrack(i + 1, curr_or)           # exclude nums[i]

        backtrack(0, 0)
        return count
