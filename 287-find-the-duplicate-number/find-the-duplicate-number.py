class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)

        for n, f in count.items():
            if f > 1:
                return n