class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # so rather than using hashmap what if i just did
        # xor all of the element and the xor of the same element ibelive it is 0

        # print(3 ^ 3) # indeeed  0

        missing = 0

        for num in nums:
            missing ^= num

        return missing