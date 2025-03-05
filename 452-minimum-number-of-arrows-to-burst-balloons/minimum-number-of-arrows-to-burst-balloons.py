class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # [[1,2],[2,3],[3,4],[4,5]]
        #                 | 
        #                     |   
        arrows = 1
        points.sort(key=lambda x: x[0])

        x = points[0][1]
        print(points)
        for i in range(1, len(points)):

            if x < points[i][0]:
                arrows += 1
                x = points[i][1]

            else:
                x = min(x, points[i][1])
        
        return arrows 