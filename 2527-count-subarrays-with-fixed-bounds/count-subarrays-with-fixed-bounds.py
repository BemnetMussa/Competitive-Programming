class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        def oper(nums):
            last_min_index = None
            last_max_index = None
            total = 0
   
            for idx, val in enumerate(nums):
                if val == minK:
                    last_min_index = idx
                if val == maxK:
                    last_max_index = idx

                if last_min_index is not None and last_max_index is not None:
                    total += min(last_min_index, last_max_index) + 1

            return total

        res = 0

        for bo, group in groupby(nums, lambda x: minK <= x <= maxK):
            group_list = list(group)
            print(bo, group_list) 

            if bo: 
                res += oper(group_list)

        return res