class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)

        p = ''

        for i in range(len(y)-1, -1, -1):
            p += y[i]

        print(p)
        return True if x >= 0 and int(p) == x else False