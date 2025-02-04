class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums) // 2

        dict_nums = Counter(nums)
      
        for num in dict_nums:
            if dict_nums[num] > n:
                return num

        return 0