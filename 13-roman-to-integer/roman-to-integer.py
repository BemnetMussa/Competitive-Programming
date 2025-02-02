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

        prev_num = 0
        ans = 0


        for i in range(len(s)-1, -1, -1):
            
            value = roman_dict[s[i]]

            if value >= prev_num:
                ans += value
            else:

                ans -= value

            prev_num = value 


        return ans


