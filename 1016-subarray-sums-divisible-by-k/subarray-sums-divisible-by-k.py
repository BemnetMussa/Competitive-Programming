class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        

        prefix = {0:1}

        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            rem = curr_sum % k

            res += prefix.get(rem, 0)

            prefix[rem] = prefix.get(rem, 0) + 1


        return res

            
            