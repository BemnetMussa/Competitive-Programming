"""
Given two strings s and t. 
Request Number of distinct subsequences of s which equals t.

Return
- trying out each combinatoins and validating if they equal to t from s
- counting how many we can make

function dp(i, j):
    if j == len(t)-1:
        return 1
    if i == len(s)-1:
        return 0

    # take it
    take, skip = 0, 0
    if s[i] == t[j]:
        take = dp(i+1, j+1)
    
    # skip it
    skip = dp(i, j+1)

    return take + skip # top-down approch with O(n * m) and space of the same


"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}
        def dp(i, j):
            if j == len(t): return 1
            if i == len(s): return 0

            if (i, j) in memo:
                return memo[(i, j)]

            take = 0
            if s[i] == t[j]:
                take = dp(i+1, j+1)
            
            skip = dp(i + 1, j)
            memo[(i, j)] = skip + take

            return memo[(i, j)]

        return dp(0, 0)