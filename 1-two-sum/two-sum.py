class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [2,7,11,15]
        #  7,
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i


