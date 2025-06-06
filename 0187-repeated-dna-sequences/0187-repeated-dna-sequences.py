from collections import defaultdict
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        hashmap = defaultdict(int)
        
        for i in range(len(s) - 9):  
            window = s[i:i+10]      
            hashmap[window] += 1     

        # only return substrings that appear more than once
        return [key for key, val in hashmap.items() if val > 1]
