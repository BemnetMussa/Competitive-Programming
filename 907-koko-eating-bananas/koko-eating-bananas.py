class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        


        def hour(bananas):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / bananas)

            return hours



        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2  

            if hour(mid) <= h:
                right = mid - 1  
            else:
                left = mid + 1 

        return left  
