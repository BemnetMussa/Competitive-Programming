from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Sort edges by weight
        edgeList.sort(key=lambda x: x[2])
        
        # Keep original index of queries
        queries = sorted([(u, v, limit, i) for i, (u, v, limit) in enumerate(queries)], key=lambda x: x[2])
        
        uf = UnionFind(n)
        res = [False] * len(queries)
        i = 0  # Pointer for edges
        
        for u, v, limit, idx in queries:
            # Union all edges with weight < limit
            while i < len(edgeList) and edgeList[i][2] < limit:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1
            # Check if u and v are connected
            res[idx] = uf.find(u) == uf.find(v)
        
        return res
