class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given: text1: string and text2: string 
        Requested to get the longest commen subsequence of both

        Approche
        - holding one string as a base text1: string and checking if it is equal to the text2
        
         text1 = "abcde", text2 = "ace" 
                  |                | 
                  __               __   # since b not in text2 we will pop char b
                  _ __             ___  # same since D not in text2
                  _ _ _            ____ # the longest is 3
                

            *tracking: the length & 
        
        either taking the value or not taking it  
        hmmm
        approchre:
        text1 = "abcde", text2 = "ace" 
                 |                |    -> same taking it ans = "a"
                  |                |   -> not same we have two options either ignore b or c so we take both  *boom that it.

        state = dp(i, j)
        basecase = reach the end either i or j
        recursive relation = if i and j are equal: dp(i+1, j+1) if not dp(i+1, j) or dp(i+1, j)
        """
        len_1, len_2 = len(text1), len(text2)

        memo = {}
        def dp(i, j):
            if not 0 <= i < len_1 or not 0 <= j < len_2:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
         
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dp(i+1, j+1)
            else:
                memo[(i, j)] = max(dp(i+1, j), dp(i, j+1))

            return memo[(i, j)]

        return dp(0, 0)
