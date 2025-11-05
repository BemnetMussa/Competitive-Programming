class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7

        '''
        2 -> 3 -> 4 -> 5 // takes 3 steps given k = 10 stpes 
        '''

        MOD = 10**9 + 7
        diff = abs(endPos - startPos)

        # impossible if distance > k or parity mismatch
        if diff > k or (k - diff) % 2 != 0:
            return 0

        r = (k + diff) // 2
        return comb(k, r) % MOD