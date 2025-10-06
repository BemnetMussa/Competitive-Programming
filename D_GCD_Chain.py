
from math import gcd

def solve():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    n = data[0]
    nums = data[1:]

    dp = [1] * n  # at least 

    for i in range(n):
        for j in range(i):

            if nums[j] < nums[i] and gcd(nums[j], nums[i]) > 1:
                dp[i] = max(dp[i], dp[j] + 1)
                

    print(max(dp))



if __name__ == "__main__":
    for _ in range(1):
        solve()

