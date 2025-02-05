class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        

        num_counter = Counter(nums)
        ans = []

        for num in num_counter:
            if num_counter[num] == 2:
                ans.append(num)


        return ans





                