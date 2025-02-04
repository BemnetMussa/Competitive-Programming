class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        reach = len(nums) // 3
        dict_nums = Counter(nums)

        ans = []
     
        for num in dict_nums:
            if dict_nums[num] > reach:
                ans.append(num)

        return ans
        


        