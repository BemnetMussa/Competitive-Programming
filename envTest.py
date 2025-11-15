

# Knapsack-2
# constrant W <= 10**9

n, W = map(int, input().split())
query = [tuple(map(int, input().split())) for _ in range(n)]

# values as the nodes, weight as the value of the ndoes
Vmax = sum([v for w, v in query])

dp = [float("inf")] * (Vmax+1) # since v upto 100
for vi, wi in query:
    for v in range(vmax, vi-1, -1):
        dp[v] = min(dp[v], dp[v - vi] + wi) # min since we are trying to acheive the max profit by less weight

for i in range(Vmax, -1, -1):
    if dp[i] <= w:
        print(v)
        break



