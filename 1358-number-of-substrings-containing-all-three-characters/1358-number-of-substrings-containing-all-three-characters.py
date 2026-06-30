
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Given: s :string , s elements of a, b , c
        # Requested: numbers of substrings containing at least all a, b, c characters
        # Solution: 
        #   s = "aabdacabadg bbbbcabc"
        #        ___      -> count = 1
        #         ___     -> count = 1 + 1, abc + bca +  ? ,  ? = abca

        count = 0
        charFreqency = defaultdict(int)
        l = 0

        for r in range(len(s)):
            charFreqency[s[r]] += 1

            while len(charFreqency) == 3:
                count += len(s) - r

                charFreqency[s[l]] -= 1
                if charFreqency[s[l]] == 0:
                    del charFreqency[s[l]]

                l += 1

        return count
