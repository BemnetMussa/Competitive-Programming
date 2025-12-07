class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 0 upto 10*9
        # 7 - 3
        # 3 , 7
        # 3, 5, 7
        # 3 * 3
        # 1 , 10
        # 1, 3, 5, 7, 9, 10

        # low .... high
        # half 

        return (high + 1) // 2 - low // 2