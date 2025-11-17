class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # at least k steps away
        left = 0
        for right, value in enumerate(nums):
            if nums[left] == 1 and value == 1 and left != right:
                difference = right - (left + 1)
                print(left, right, difference)
                if difference < k:
                    return False
            # print(right, left, value)
            if value == 1:
                left = right

        return True