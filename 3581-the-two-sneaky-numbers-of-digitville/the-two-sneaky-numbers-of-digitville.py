class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        

        counter_nums = Counter(nums)

        ans = []
        for num in counter_nums:
            if counter_nums[num] > 1:
                ans.append(num)

        return ans