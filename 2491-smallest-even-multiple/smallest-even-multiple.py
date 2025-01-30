class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        smallest = n * 2

        if n == smallest / 2 and n % 2 == 0:
            smallest = n

        return smallest