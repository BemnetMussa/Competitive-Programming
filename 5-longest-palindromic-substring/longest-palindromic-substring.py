class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n) time

        # s_reverse = s[::-1]
        # res = ""

        # left = 0
        # for right in range(len(s)):
        #     if s_reverse[right] != s[right]:
        #         left = right + 1
        #     else:
        #         curr_ans = s[left: right + 1] # O(N^2)
        #         print(curr_ans)
        #         if len(curr_ans) > len(res):
        #             res = curr_ans

        # return res if len(res) != 0 else s[0]
        # # fails on babcde, reversed-> edcbab  where bab is a palnidrom 

        start, end = 0, 0

        def expand(i, j):
            while i >= 0  and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i+1, j-1 # expanded left and right

        for i in range(len(s)):
            left1, right1 = expand(i, i) # odd-length
            left2, right2 = expand(i, i+1) # even-length

            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2
            
        return s[start: end + 1]
        