class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                
                return s[left:right] == s[left:right][::-1] or  s[1+left:right+1] == s[1+left:right+1][::-1]
            left += 1
            right -= 1
        
        return True
