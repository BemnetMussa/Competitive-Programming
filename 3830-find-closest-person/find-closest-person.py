class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        
        distance_x = abs(x - z)
        distance_y = abs(y - z)

        if distance_x == distance_y:
            return 0

        return 1 if distance_x < distance_y else 2