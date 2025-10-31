class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        repeat = []
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                repeat.append(nums[i-1])

        return repeat