class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(a):
            piles = 0
            for c in candies:
                piles += c // a
                if piles >= k:
                    return True
            return False
        
        l,r = 1,sum(candies) // k
        while l<=r:
            mid = (l+r) // 2
            if possible(mid):
                l = mid+1
            else:
                r = mid-1
        return r
        