class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        Given len(s) == len(t), and an integer maxCost
        Request making s the same as t and the cost is s[i] - t[i]
        Return the max length to change to be the same as s == t
        otherwise return 0

         s = "abcd", t = "bcdf", maxCost = 3
              ||| -> 3
         s = "abcd", t = "cdef", maxCost = 3
              |||| -> SO WE CAN JUST CHANGE 1 LENGTH 
         s = "addvsabc", t = "zxyzsbcd", maxCost = 3
                   ___

        keep track of window, min_len

        pseudocode
        left = 0 # keep track for shift
        min_len = flaot("inf") # track smaller
        cost = 0

        for right in range(len(s)):
          
            cost += char(t[right]) - char(s[right])
            while cost > maxCost:
                cost -= char(t[left]) - char[s[left]]
                left += 1

            min_len = min(min_len, right - left + 1)

        return min_len
        """

        left = 0 # keep track for shift
        min_len = 0 # track smaller
        cost = 0

        for right in range(len(s)):
          
            cost += abs(ord(t[right]) - ord(s[right]))
            while cost > maxCost:
                cost -= abs(ord(t[left]) - ord(s[left]))
                left += 1

          
            min_len = max( min_len, right - left + 1 )

        return min_len