class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # sort in O(n) time
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                correct_pos = nums[i] - 1
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]

        
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)

        return res