from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # If k is enough to go straight without worrying about obstacles
        if k >= rows + cols - 2:
            return rows + cols - 2
        
        queue = deque([(0, 0, k, 0)])  # (row, col, remaining_k, steps)
        visited = {(0, 0, k)}
        
        while queue:
            i, j, rem, steps = queue.popleft()
            
            # reached destination
            if (i, j) == (rows - 1, cols - 1):
                return steps
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols:
                    new_k = rem - grid[x][y]
                    if new_k >= 0 and (x, y, new_k) not in visited:
                        visited.add((x, y, new_k))
                        queue.append((x, y, new_k, steps + 1))
        
        return -1  # no path
