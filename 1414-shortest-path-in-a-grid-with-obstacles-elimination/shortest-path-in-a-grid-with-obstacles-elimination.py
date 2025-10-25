'''
Given: m x n integer matrix grid. each cell is either 0 ( empthy ) or 1 ( obstacle ). up, down, rig, left, 
from top (0, 0) reach (row-1, col-1) 

Requested: Return the minimum number of steps that are needed. can remove k obstacles
constratins: 1 <= m, n <= 40
            1 <= k <= m * n
approche: 
-> [0,0,0],
   [1,1,0],
   [0,0,0],
   [0,1,1],
   [0,0,0] 
what we need: 
    Take all the paths, 
    keep track of how many steps it takes us.
    track of visited 

approch --> dp approch -> breadth first search using queue will be enough i think

'''

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # (i, j, k, steps)
        nodes = deque([(0, 0, k, 0)]) # start node
        visited = {(0, 0, k, 0)}

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while nodes: 
            x, y, rem_k, steps = nodes.popleft()
            
            if (x, y) == (ROWS-1, COLS-1):
                return steps

            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                # if in bound
                if 0 <= nx < ROWS and 0 <= ny < COLS:
                    new_k = rem_k - grid[nx][ny]
                
                    if new_k >= 0 and (nx, ny, new_k) not in visited:
                        visited.add((nx, ny, new_k))
                        nodes.append((nx, ny, new_k, steps + 1))
                    

        return -1

