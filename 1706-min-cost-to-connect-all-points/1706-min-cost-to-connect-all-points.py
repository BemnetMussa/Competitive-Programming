class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Cycle detected

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        # Create a complete graph and compute edge weights (Manhattan distance)
        for i in range(n):
            for j in range(i + 1, n):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((weight, i, j))

        # Sort edges by weight (ascending order)
        edges.sort()

        dsu = DSU(n)
        total_cost = 0
        count = 0  # Number of edges in the MST

        # Apply Kruskal’s algorithm
        for weight, u, v in edges:
            if dsu.union(u, v):  # Connect if no cycle
                total_cost += weight
                count += 1
                if count == n - 1:  # Stop when we have n-1 edges
                    break

        return total_cost
