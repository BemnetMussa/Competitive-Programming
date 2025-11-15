from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        counter_t = Counter(t)
        window = Counter()
        
        have, need = 0, len(counter_t)
        left = 0
        ans = float("inf")
        result = ""

        for right in range(len(s)):
            window[s[right]] += 1
            
            if s[right] in counter_t and window[s[right]] == counter_t[s[right]]:
                have += 1

            while have == need:  # valid window
                if (right - left + 1) < ans:
                    ans = right - left + 1
                    result = s[left:right+1]

                window[s[left]] -= 1
                if s[left] in counter_t and window[s[left]] < counter_t[s[left]]:
                    have -= 1
                
                left += 1
        
        return result
