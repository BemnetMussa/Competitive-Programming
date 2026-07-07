class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        window = defaultdict(int)
        req = len(need)

        have = 0
 
        ans = ""
        ans_leng = float("inf")
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == req:

                if (r - l + 1) < ans_leng:
                    ans = s[l: r + 1]
                    ans_leng = r - l + 1

                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1


        return ans





