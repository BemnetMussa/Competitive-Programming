n = int(input())
nums = list(map(int, input().split()))

dp = [0] * (n)

for i in range(1, n):
    one = dp[i-1] + abs(nums[i] - nums[i-1])
    two = dp[i-2] + abs(nums[i] - nums[i-2]) if i > 1 else float("inf")

    dp[i] = int(min(one, two))

# print(dp)
print(dp[-1])