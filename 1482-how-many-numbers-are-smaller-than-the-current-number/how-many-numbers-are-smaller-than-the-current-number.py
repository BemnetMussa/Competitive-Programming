class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        

        dict_num = Counter(nums)

        ans = []
        for num in nums:
            count = 0
            for key in dict_num:
                if num > key:
                    count += dict_num[key]


            ans.append(count)


        return ans