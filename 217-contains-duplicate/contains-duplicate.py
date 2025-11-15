class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        # True if any value > 1
        return any(value > 1 for value in count.values())