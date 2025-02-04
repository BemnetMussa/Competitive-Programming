class Solution:
    def firstUniqChar(self, s: str) -> int:
      
        li = Counter(s)
     

        for i in range(len(s)):
            char = li[s[i]]
        
            if char == 1:
                return i

        return -1

