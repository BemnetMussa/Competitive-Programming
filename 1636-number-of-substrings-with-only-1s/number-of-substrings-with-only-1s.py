class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        cur = 0
        for num in s:
            if num == "1":
                cur += 1
                total += cur % MOD
            else:
                cur = 0
        return total % MOD       
            