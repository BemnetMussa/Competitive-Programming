class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        Symbol   Value
        I        1
        V        5
        X        10
        L        50
        C        100
        D        500
        M        1000

        '''
        roman_map = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        roman_keys = list(roman_map.keys())
        ans = ""
        i = len(roman_keys) - 1 

        
        while num > 0:
            if num >= roman_keys[i]:
                
                ans += roman_map[roman_keys[i]]  
                num -= roman_keys[i] 
            else:
                i -= 1 
                
        return ans
