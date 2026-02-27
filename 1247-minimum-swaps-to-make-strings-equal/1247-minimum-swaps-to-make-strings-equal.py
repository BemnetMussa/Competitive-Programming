class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        n = len(s1)
        diffs = {"x": 0, "y": 0}
        for i in range(n):
            if s1[i] != s2[i]:
                diffs[s1[i]] += 1
        if diffs["x"]%2 != diffs["y"]%2:
            return -1
        cnt = diffs["x"]//2 + diffs["y"]//2
        if diffs["x"]%2 == 1:
            return cnt + 2
        
        return cnt