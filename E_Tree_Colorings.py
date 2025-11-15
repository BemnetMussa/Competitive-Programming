import sys
sys.setrecursionlimit(1_000_000)

N = 500043
dp = [-1] * N
dp2 = [-1] * N
divisors = [[] for _ in range(N)]

# Precompute all divisors
for i in range(2, N):
    for j in range(i * 2, N, i):
        divisors[j].append(i)

def calc(x):
    if dp[x] != -1:
        return dp[x]
    if x == 1:
        dp[x] = 0
        return dp[x]
    if x == 3:
        dp[x] = 1
        return dp[x]
    dp[x] = calc2(x - 2) + 1
    return dp[x]

def calc2(x):
    if dp2[x] != -1:
        return dp2[x]
    if x == 1:
        dp2[x] = 0
        return dp2[x]
    dp2[x] = calc(x)
    for y in divisors[x]:
        dp2[x] = min(dp2[x], calc(y) + calc2(x // y))
    return dp2[x]

# Input processing
t = int(input())
for _ in range(t):
    x = int(input())
    if x % 2 == 0:
        print(-1)
    else:
        print(calc(x + 2))
''