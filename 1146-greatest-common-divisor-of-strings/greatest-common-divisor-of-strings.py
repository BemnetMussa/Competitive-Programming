class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        #  ABABAB
        #  A * 6 = AAAAAAA  != ABABAB
        #  AB * 3 = ABABABA == ABABAB   True

        # ABCABC
        # A * 6 = AAAAAA != ABCABc
        # AB * 3 = ABABAB != ABCABC
        # ABC * 2  = ABCABC == ABCABc  True
        

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        return str1[:gcd(len(str1), len(str2))]
