class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        s_count = Counter(s)

        num = s_count[s[0]]
     
        for char in s_count:
            if s_count[char] != num:
                return False


        return True