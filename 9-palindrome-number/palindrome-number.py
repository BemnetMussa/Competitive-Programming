class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 12221
        # 12221 - reverse
        # 

        # 12345
        # |   | - log(n)

        # 123 - 12
        # 12 45 --> 21
         # 45 != 21 false
         # 120202020

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        while reverse < x: # upto the half of x
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x //= 10 
        
        return x == reverse or x == reverse // 10