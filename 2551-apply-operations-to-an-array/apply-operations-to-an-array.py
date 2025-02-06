class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        

        # if nums[i] == nums[i + 1]  then nums[i] = nums[i] * 2 and nums[i+1] = 0
        # moving the zeros to the last


        for i in range(1, len(nums)):

            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0

        

        # moving zeros to the last 
        holder = 0
        seeker = 0

        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]

                holder += 1
            seeker += 1

        return nums
