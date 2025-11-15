# D. Flowers

MOD = 10**9 + 7
max_flowers = 10**5

t, k = map(int, input().split())
        
dp = [0] * (max_flowers + 1)
dp[0] = 1 # base case

for i in range(1, max_flowers + 1):
    dp[i] = dp[i-1]
    
    # last k flowers are white
    if i >= k:
        dp[i] = (dp[i] + dp[i-k]) % MOD


prefix_sum = [0] * (max_flowers+1)
prefix_sum[0] = dp[0]
for i in range(1, max_flowers+1):
    prefix_sum[i] = (prefix_sum[i-1] + dp[i]) % MOD

for _ in range(t):
    a, b = map(int, input().split())
    result = (prefix_sum[b] - prefix_sum[a-1] + MOD ) % MOD
    print(result)

