class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [1, 2, 3] 
        # subarryes
        #   1, 1, 1
        #   1, 2, 1
        #   1 , 2, 2
        #   base case total == k
        # count --> dp approch (recursive approch)
        # time compelxity on each recursive call we have n options so recrusively it iwll be n^n which will fail
        
        # [1, 1, 1]
        #        | 
        #  0, 0, 0, 0 base case 1
        # why not just bottom up where we track the needed difference to make it valid so

        prefix = {}
        count = 0
        prefix[0] = 1 # base case

        curr_sum = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            count += prefix.get(diff, 0)

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

        return count