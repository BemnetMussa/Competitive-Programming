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


# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         N = len(nums)

#         target = sum(nums) // k
   
#         # track the used elements
#         used = [False] * N
# \
#         def divideArrayToKsubsets(idx, k, curr_sum):
#             if k == 0:
#                 return True
#             if curr_sum == target:
#                 return divideArrayToKsubsets(0, k-1, 0)

#             for i in range(idx, N):
#                 if not used[i] and curr_sum + nums[i] <= target:
#                     used[i] = True
#                     if divideArrayToKsubsets(i + 1, k, curr_sum + nums[i]):
#                         return True
#                     used[i] = False

#             return False

#         return divideArrayToKsubsets(0, k, 0)



class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)  # optimization
        used = [False] * len(nums)
        memo = {}

        def backtrack(k, subsetSum, start):
            state = tuple(used)
            if state in memo:
                return memo[state]
            if k == 1:
                return True
            if subsetSum == target:
                res = backtrack(k - 1, 0, 0)
                memo[state] = res
                return res

            for i in range(start, len(nums)):
                if used[i] or subsetSum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(k, subsetSum + nums[i], i + 1):
                    memo[state] = True
                    return True
                used[i] = False

            memo[state] = False
            return False

        return backtrack(k, 0, 0)



        



