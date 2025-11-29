class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # a
        # aa
        # aab --> check
        # aac --> check
        # aaa --> count += 1
        # a
        # ab
        # aba --> count += 1
        # aca --> count += 1

        # top down dp -- will fail
        # down top dp --> n^2
        # hmmm how many duplicates are there can that detmerine the subsecuqnce that we can mak ewhy not
        # if there is 3 with 3 length string 1
        # if there is 3 duplicates with 4 then we can make easely 2+ 1
        # if there is 3 duplicates with 5 teams then we can geneate upto 3 
        # ....


        res  = 0
        for char in set(s):
            left = s.find(char)
            right = s.rfind(char)

            # print(left, right)
            if left < right:
                middle_chars = set(s[left+1:right])
                res += len(middle_chars)

        return res

        