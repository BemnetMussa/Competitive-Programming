class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 
        
        # Step 1: place nums on correct pos
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i] 

        # Step 2: the first not correct pos is the missing one
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1  

        # Step 3: if all correct pos
        return n + 1
