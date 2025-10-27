class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        checking if it is an anagrem or not true or false
        Input: s = "anagram", t = "nagaram"
                    |||             |          -> values, frequences 
        
        s.count("a") == t.count("a")


        convert to lists => sort them lexgrpghically then check the equality *easy soltion but. 

        '''

        temp = set(s + t)
        for char in temp:
            if s.count(char) != t.count(char):
                return False
      
        return True