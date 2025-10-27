class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        checking if it is an anagrem or not true or false
        Input: s = "anagram", t = "nagaram"
                    |||             |          -> values, frequences 
        
        s.count("a") == t.count("a")


        convert to lists => sort them lexgrpghically then check the equality *easy soltion but. 

        '''

        return Counter(s) == Counter(t)