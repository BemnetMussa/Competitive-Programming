class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # ptr1, ptr2 = 0, 0
        # while ptr2 < len(t) and ptr1 < len(s):
        #     if s[ptr1] == t[ptr2]:
        #         ptr1 += 1
        #         ptr2 += 1
        #     else:
        #         ptr2 += 1

        # return True if ptr1 == len(s) else False 
        # time O(n) where n = len(t) and space of O(1) 


        # DP - Approche
        # top down approche  
        # def dp(i, j):
        #     if i == len(s):
        #         return True
        #     if j == len(t):
        #         return False

        #     if s[i] == t[j]:
        #         return dp(i+1, j+1)
        #     else:
        #         return dp(i, j+1)
        # return dp(0, 0)

        
        # Bottom down approche
        m, n = len(s), len(t)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty s is always a subsequence
        for j in range(n + 1):
            dp[m][j] = True

        # Fill table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]

        return dp[0][0]





        