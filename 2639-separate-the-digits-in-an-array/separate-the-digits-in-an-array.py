class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        str_num = ""
        for num in nums:
            str_num += str(num)

        ans = [int(x) for x in str_num]


        return ans
