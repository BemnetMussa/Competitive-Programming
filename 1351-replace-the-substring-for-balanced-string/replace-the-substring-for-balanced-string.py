from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        window = Counter()
        left = 0
        k = len(s) // 4  
        count = Counter(s)  
        length = float("inf")

    
        if all(count[ch] == k for ch in "QWER"):
            return 0

        for right in range(len(s)):
            window[s[right]] += 1  # Expand window

            # Shrink window when valid
            while all(count[ch] - window[ch] <= k for ch in "QWER"):
                length = min(length, right - left + 1)
                window[s[left]] -= 1  # Remove leftmost character
                left += 1  # Move left pointer

        return length if length != float("inf") else 0
