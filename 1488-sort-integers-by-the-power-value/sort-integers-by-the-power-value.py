class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}

        def helper(x):
            if x == 1:
                return 0
            if x not in memo:
                if x % 2 == 0:
                    memo[x] = 1 + helper(x//2)
                    return memo[x]
                memo[x] = 1 + helper(x * 3 + 1)
            return memo[x]
        
        num_pows = sorted([(helper(num), num) for num in range(lo, hi+1)])
        

        return num_pows[k-1][1]
  