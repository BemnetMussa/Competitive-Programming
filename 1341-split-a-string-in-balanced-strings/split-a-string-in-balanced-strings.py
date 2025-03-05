class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        # taking unique indexed substrings
        # iterate until there is a balance if so go to the next ones


        subBalance = 0

        balance = 0
        left = 0
        for right in range(len(s)):
            balance += 1 if s[right] == "L" else -1

            if balance == 0:
                left = right + 1
                subBalance += 1

        
        return subBalance