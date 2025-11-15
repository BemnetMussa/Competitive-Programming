class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 001
        # 100
        # ----
        # 101 -> using  bitwise or

        num = x ^ y
        return bin(num).count("1")