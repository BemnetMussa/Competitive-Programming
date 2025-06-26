class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # a subarry that satisfies
            # nums[i] % modulo == k 
            # [3, 2, 4]
            #  _          count = 1
            #  _  _       count = 2   > know that 2 so invalid so will be one with 3
            #  _  _  _    count = 3   > 

            # keeping track of > good integers , bad integers such that i will gone substract form the subarray
            # keeping track of the number of subarries that we can create


            # USING PREFIX SUM DAMM

            n = len(nums)
            cnt = Counter([0])
            res = 0
            prefix = 0
            for i in range(n):
                prefix += 1 if nums[i] % modulo == k else 0
                res += cnt[(prefix - k + modulo) % modulo]
                cnt[prefix % modulo] += 1
            return res