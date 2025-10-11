'''
Given a arr[int] and difference, 
Requested to return the longest subsequence in arr which is in sequence where the difference of adjacent elements in the subsequence quals differenece. 

constratins: 1 <= n <= 10^5


approch: 
    - arr = [1,2,3,4, 6, 3], difference = 1 
             _______    __ -> [1, 2, 3, 4, 3]
             # for each one of them we should find the longest valid answer

    - arr = [1,5,7,8,5,3,4,2,1], difference = -2
             _       _ _    

            check every single subsets and comput it along the way uisng DP

                                                1
                                        ()    (7, -6)

psuedococde:
  memo = {}
- funciton dp(i, mask):
    if (i, mask) == n:
        return 1
    
    if (i, mask) in memo:
        return memo[i]

    max_leng = 0
    for j in range(n):
        if not (mask & (1 << j)) and difference == (nums[i] - nums[j]):
            new_mask = mask | ( 1 << j )
            max_leng = max(max_leng, max_leng + dp(j, new_mask)
    
    memo[(i, mask)] = max_leng

    return max_leng
Time complexity will be at 2^n won't pass 10^5

# for the bottom up approch which will be more efficent than this one 
to track the length using dictionary
a-b = d so a-d = b
dp = {} # to track 
max_leng = 0

for num in arr:
    dp[num] = dp.get(num-difference, 0) +1
    max_leng = max(max_leng, dp[num])

return max_leng # time O(n)
'''



class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = {}  # dp[num] = length of longest subsequence ending with num
        max_len = 0

        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            max_len = max(max_len, dp[num])

        return max_len