class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            correct_pos = nums[i] - 1
           
            if nums[correct_pos] != i + 1:
                if nums[correct_pos] == nums[i]:
                    return nums[i]

                nums[correct_pos], nums[i] = nums[i], nums[correct_pos]

            else:
                i += 1
         