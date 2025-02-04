class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = Counter(nums)

        for val in s:
            if s[val] > 1:
                return True


        return False