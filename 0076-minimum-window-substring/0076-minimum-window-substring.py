from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        required = len(need)

        res_len = float("inf")
        res = ""

        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                # update answer
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]

                # shrink
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        return res