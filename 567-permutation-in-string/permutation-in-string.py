class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        count_s1 = Counter(s1)
        window = Counter(s2[:n])

        if window == count_s1:
            return True

        for i in range(n, m):
            window[s2[i]] += 1
            window[s2[i - n]] -= 1
            if window[s2[i - n]] == 0:
                del window[s2[i - n]]

            if window == count_s1:
                return True

        return False
