class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        

        # 474. Ones and Zeroes
        '''
        # Given an array of binary strings *strs and two integer *m and *n.
        Requested: to rutnr the largest subset x in y with at most m an -> 0's and n -> 1's

        strs = ["10","0001","111001","1","0"], m = 5, n = 3
                
        '''
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for word in strs:
            zero = word.count('0')
            one = word.count('1')

            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)

        return dp[m][n]
