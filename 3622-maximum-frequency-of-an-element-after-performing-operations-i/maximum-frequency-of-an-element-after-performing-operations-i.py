class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        mx = max(nums)
        n = mx + k + 2
        f = [0] * n
        for x in nums:
            f[x] += 1

        pre = [0] * n
        pre[0] = f[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + f[i]

        ans = 0
        for t in range(n):
            if f[t] == 0 and numOperations == 0:
                continue
            l, r = max(0, t - k), min(n - 1, t + k)
            tot = pre[r] - (pre[l - 1] if l > 0 else 0)
            adj = tot - f[t]
            val = f[t] + min(numOperations, adj)
            ans = max(ans, val)
        return ans