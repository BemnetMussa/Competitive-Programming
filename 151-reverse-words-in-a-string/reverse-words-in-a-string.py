class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = list(map(str, s.split()))
        s.reverse()
        return str(' '.join(s))