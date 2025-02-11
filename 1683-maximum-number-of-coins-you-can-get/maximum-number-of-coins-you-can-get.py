class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        turn = len(piles)

        me = 0
        i = len(piles) - 2
        while turn > 0:
            me += piles[i]
            i -= 2
            turn -= 3


        return me
