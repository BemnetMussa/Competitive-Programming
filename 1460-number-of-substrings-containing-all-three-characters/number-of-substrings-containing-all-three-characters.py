'''
                    s = "abcabc"
                         ___    -> valid len(s) - right  = 4
                          ___   -> valid len(s) - right = 4 + 3 = 7
                           ___  -> valid len(s) - right = 9
                            ___ -> valid len(s) - right = 10

1 + 1 = 2
[3, 4, 2]

'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        last_pos = [-1] * 3 # track the last valid pos
        total = 0

        for pos in range(len(s)):
            last_pos[ord(s[pos]) - ord("a")] = pos

            # update the total from the left
            total += 1 + min(last_pos)

        return total
            

            

