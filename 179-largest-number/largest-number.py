from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):

        arr = [str(x) for x in nums]
        arr.sort(key=lambda x:x*10, reverse = True)

        if arr[0] == "0":
            return "0"

        res = "".join(arr)
        return res