class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Array to track trust counts
        trust_counts = [0] * (n + 1)
        
        for a, b in trust:
            trust_counts[a] -= 1 
            trust_counts[b] += 1  
        
    
        for person in range(1, n + 1):
            if trust_counts[person] == n - 1:  # Judge is trusted by everyone except themselves
                return person
        
        return -1  # No judge found
