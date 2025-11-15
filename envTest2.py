# problm description
#   use A, gain ai happenies
#   use B, gain bi happenies
#   use C, gain ci happenies
# get bored if he use the same thing 2 or more times. *consecutively 
# Requested: -Get the maximum possible total points of happiness to get.

'''
a, b, c 
a, b, c
a, b, c
...
maybe the best approch is baa,
hwo do i know on the first row that to not take a

yon each iteration
having 3 choices, a, b, c 
keepign track of the similirites also along the w

Top-down approch

import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

n = int(input())
q = [tuple(map(int, input().split())) for _ in range(n)]

@lru_cache(None)
def dp(i, prev):
    # base-case
    if i == n:
        return 0
    
    res = 0
    for choice, val in zip(['a','b','c'], q[i]):
        if choice != prev:
            res = max(res, val + dp(i+1, choice))

    return res

print(dp(0, ''))
'''

# bottom up approch 

n = int(input())
q = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
dp[0][0] = dp[0][0]
dp[0][1] = dp[0][1]
dp[0][2] = dp[0][2]

for i in range(1, n):
    dp[i][0] = q[i][0] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = q[i][1] + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = q[i][2] + max(dp[i-1][0], dp[i-1][1])

print(max(dp[n-1]))
