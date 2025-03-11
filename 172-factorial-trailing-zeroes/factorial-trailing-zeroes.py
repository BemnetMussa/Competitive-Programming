class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0  
        
        count = 0
        while n >= 5:
            count += n // 5  
            n //= 5  
        
        return count
