'''
Given nums[int] and k: int

requested: return True if it is possible to divide the array into k non-empthy subsets whose sums are all equal.

constratins: 1 <= k <= len(nums) <= 16
approch:
- nums = [4,3,2,3,5,2,1], k = 4
ok, since we need to divide exactly to k subsets. The target value will be target = sum(nums)/k
since we need to consider every possiblity. 
rather than taking k options every single time which will give us k^N. taking two options 2^N
taking 4, not taking 0
taking 3 = 7 not procesddeing and so on 

psudocode soltuion:
- function dp(idx, total):
    if total == target:
        return 1
    
    if idx == len(N) or total > target:
        return 0

    return dp(idx, total + nums[idx]) + dp(idx+1, total)

'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        
        nums.sort(reverse=True)  # sake for optimizaiton
       
        memo = {}

        def backtrack(k, subsetSum, start, mask):
            
            if mask in memo:
                return memo[mask]
            if k == 1:
                return True

            if subsetSum == target:
                res = backtrack(k - 1, 0, 0, mask)
                memo[mask] = res
                return res

            for i in range(start, len(nums)):
                if mask & (1 << i) or subsetSum + nums[i] > target:
                    continue

                new_mask = mask | (1 << i)
                if backtrack(k, subsetSum + nums[i], i + 1, new_mask):
                    memo[mask] = True
                    return True
                

            memo[mask] = False
            return False

        return backtrack(k, 0, 0, 0)



        



