class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()

        left = 0
        max_len = 0

        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            if max_len < len(seen):
                max_len = len(seen)
                
        return max_len
