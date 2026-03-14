# 1415. The K-th Lexicographical String of All Happy Strings of Length n
'''
Given: 
    - n: int, k: int
    - where consider list of all happy string of length n that is *sorted in Lexicographical order* ( increasing sequence ) 
        > happy string is a string that:
            > consist only of letters of the set ['a', 'b', 'c']
            > s[i] != s[i+1], for all 0 < i < s.length - 1
                

Requested:
    - Return the kth string of this list or return empthy string if there are less than k, 
    happy stirngs of length n. 


Approch:
> Testcases
    n = 1, k = 3
    ["a", "b", "c"], since the length (n) is one
    return "c"

    n = 1, k = 4
    ['a', 'b', 'c'], since we can make 3 length list for n = 1 string size

'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = ""
        def backtracking(s):
            nonlocal k, res
            # baseCases

            if len(s) == n: 
                k -= 1
                if k == 0:
                    res = s
                return 
    
            for char in ['a', 'b', 'c']:
                if not s or s[-1] != char: # happy condition
                    backtracking(s + char)
                if res:
                    return 

        backtracking("")
        return res