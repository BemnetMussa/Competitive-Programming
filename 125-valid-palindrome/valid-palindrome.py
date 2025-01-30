class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
            s.lower()

            remove spaces and commas and so on 
            d = "abcdefghijklmnopqrstuvwxyz"
            char_list = list(d)
            
        
        """


        # filtering steps
        s = s.lower()

        li = list(s)

        char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        ans = ""
   
        for char in s:

            if char in char_list:
                ans += char

        # palandriom checking steps
        s = ans

        return True if ans[::-1] == s else False
      
