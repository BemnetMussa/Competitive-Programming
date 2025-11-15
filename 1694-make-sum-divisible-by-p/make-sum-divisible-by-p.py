class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # we need to keep track of two things
                # - the number that makes it invalid
                # - number that makes it valid ( iterating thrugh it )
        # it shouldn't be this much hard -- trying to find the smallest legnth to remove possibley nohting 
        # nums= [3, 1, 4, 2],  sum(nums) = 10 % 9 = 1
        #           |          found so return 1 element only
        # nums = [6,3,5,2], p = 9, sum(nums) = 16 % 9 = 7
        #                    _. 7 not in our array
        #   sort -> [2, 3, 5, 6]
        #            |  |  |        10 > 7,
        #               |  |        8 > 7,  store two elements
        #                  |        5 < 7, return the prevsious smallest one
        # in general
        # the sum
        # check if rem in nums if there is return 1
        # otherwise sliding window approch after the sort

        target = sum(nums) % p
        if target == 0:
            return 0

        prefix_mod = {0: -1}  # prefix sum modulo -> index
        curr = 0
        res = float('inf')

        for i, num in enumerate(nums):
            curr = (curr + num) % p
            needed = (curr - target) % p
            if needed in prefix_mod:
                res = min(res, i - prefix_mod[needed])
            prefix_mod[curr] = i

        return res if res < len(nums) else -1