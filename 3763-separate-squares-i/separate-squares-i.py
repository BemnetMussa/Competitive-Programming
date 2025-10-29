'''
Given: 2D integer array where Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Requested to get the minimum y-coordinate value of a horizontal line such that the total area of the square above the line equals to the total aready of the squrea below the line. 

'''


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares)
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        def area_below(y_line):
            area = 0.0
            for _, y, l in squares:
                bottom, top = y, y + l
                if y_line <= bottom:
                    continue
                elif y_line >= top:
                    area += l * l
                else:
                    area += l * (y_line - bottom)
            return area

        # binary search with fixed iterations
        for _ in range(60):  # enough for 1e-6 precision
            mid = (low + high) / 2
            below = area_below(mid)
            if below * 2 < total_area:  # area below too small → move line up
                low = mid
            else:  # area below too large → move line down
                high = mid

        return (low + high) / 2
