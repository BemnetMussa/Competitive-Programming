class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []


        # [ 1, 2, 3, 3, 5]
        #   
        for i in range(len(nums)):
            
            while nums[i] != nums[nums[i] - 1]: # curr value correct index are not the same
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums):
            if num != i + 1:
                res.append(num)
        
        return res
