class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y = str(x)
        return True if x >= 0 and x == int(y[::-1]) else False

