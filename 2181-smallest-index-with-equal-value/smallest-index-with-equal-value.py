class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        min_index = float("inf")

        for i in range(len(nums)):
            if i % 10 == nums[i]:
                min_index = min(min_index, i)

        
        return min_index if min_index != float("inf") else -1