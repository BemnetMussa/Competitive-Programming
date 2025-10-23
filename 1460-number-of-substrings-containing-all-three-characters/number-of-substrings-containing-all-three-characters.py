'''
                    s = "abcabc"
                         ___    -> valid len(s) - right  = 4
                          ___   -> valid len(s) - right = 4 + 3 = 7
                           ___  -> valid len(s) - right = 9
                            ___ -> valid len(s) - right = 10

'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        res = 0
        left = 0

        count = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):
            count[s[right]] += 1

            while all(count[c] > 0 for c in "abc"):
                res += len(s) - right
                count[s[left]] -= 1
                left += 1

        return res
         
            

            

