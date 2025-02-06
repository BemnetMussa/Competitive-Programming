class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        w = 0
        # itrating through each friends 
        for i in range(1, n + 1):

            w = (k + w) % i
            
        return w + 1