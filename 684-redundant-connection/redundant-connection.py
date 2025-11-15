class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [i for i in range(N + 1)] # 1, 2, 3
        Rank = [1] * (N+1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if Rank[p1] > Rank[p2]:
                parent[p2] = p1
                Rank[p1] += Rank[p2]

            else:
                parent[p1] = p2
                Rank[p2] += Rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        