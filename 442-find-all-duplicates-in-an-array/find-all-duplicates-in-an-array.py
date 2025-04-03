class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = set()

        i = 0
        while i < len(nums):
            curr_val = nums[i]

            if curr_val != i + 1:
                if curr_val in res:
                    i += 1
                   
                elif curr_val == nums[curr_val - 1]:
                    res.add(curr_val)
                    i += 1

                else:
                    nums[i], nums[curr_val - 1] = nums[curr_val - 1], nums[i]

            else:
                i += 1

        return list(res)






                