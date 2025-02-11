class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            zmin = i

            for j in range(i+1, len(nums)):
                if nums[zmin] >= nums[j]:
                    nums[zmin], nums[j] = nums[j], nums[zmin]


        
        print(nums)