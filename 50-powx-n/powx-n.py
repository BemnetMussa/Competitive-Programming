class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1 
        if n < 0:
            return 1 / self.myPow(x, -n)  # Flip the sign of n and invert x
        
        
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half  # For even exponents
        else:
            return x * self.myPow(x, n - 1)  # For odd exponents
