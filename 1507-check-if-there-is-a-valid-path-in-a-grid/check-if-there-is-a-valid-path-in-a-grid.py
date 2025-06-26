class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx != fy:
            self.parent[fy] = fx

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        street_dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }

        reverse_dir = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0),
        }

        for i in range(m):
            for j in range(n):
                for dx, dy in street_dirs[grid[i][j]]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        rev = reverse_dir[(dx, dy)]
                        if rev in street_dirs[grid[ni][nj]]:
                            u = i * n + j
                            v = ni * n + nj
                            uf.union(u, v)

        return uf.find(0) == uf.find(m * n - 1)
