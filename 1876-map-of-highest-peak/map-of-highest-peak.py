class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        '''
            isWater[i][j] == 0 -> is land
            isWater[i][j] == 1 -> is water

            convert the matrix into -> the hight of water cell is 0 
                                    -> any two cells have an absolute difference at most 1
                                    -> 4 directions

            approch:
                - since we convert everytthing and also there will be one water everytime, 
                - create new matrix to track the heights 
                - check and convert
        
        '''
        m, n = len(isWater), len(isWater[0])
        res = [[-1]*n for _ in range(m)]
        q = deque()


        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    q.append((i, j))

        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # iterating and marking 
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and res[nx][ny] == -1:
                    res[nx][ny] = res[x][y] + 1
                    q.append((nx, ny))

        return res
       


