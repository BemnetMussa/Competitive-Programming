class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000
        }

        # stack = [V]       5
        # V > I            5 - I = 4
        # stack = [C]
        # C > X            C - x = 94
        # stack = []



        stack = []
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if stack and roman_dict[stack[-1]] > roman_dict[s[i]]:
                ans -= roman_dict[s[i]]
            
            else:
             
                stack.append(s[i])


        if stack:
            for char in stack:
                ans += roman_dict[char]


        return ans


