class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()

        def good(k):

            balls = 1
            left = position[0]

            for p in position:
                if p - left >= k:
                    balls += 1
                    left = p

            return balls >= m

        
        left = 1
        right = position[-1] - position[0]  

        while left <= right:
            mid = left + (right - left) // 2
     
            # choicing the force rather than where to put the balls
            if good(mid):
                left = mid + 1
            else:
                right = mid - 1


        return right
