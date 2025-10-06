'''
Given 
    s: string and p string
Requested 
    to get the first index of all the palandrom of p on s
    return [fidx] 

Approche
    s = "cbaebabacd", p = "abc"
          |||

        ba 
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)

        k = len(p) - 1
        res = []
       
        subs = Counter(s[:k])
        for i in range(k, len(s)):

            subs[s[i]] += 1
            
            if subs == target:
                res.append(i-k)
            
            subs[s[i-k]] -= 1
            if subs[s[i-k]] == 0:
                del subs[s[i-k]]

        return res
            
