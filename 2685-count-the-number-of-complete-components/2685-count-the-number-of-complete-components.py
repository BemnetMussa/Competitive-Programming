
class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = set()
        ans = 0

        def dfs(node, res):
            if node in vis:
                return
            vis.add(node)
            res.append(node)
            for neigh in adj[node]:
                dfs(neigh, res)

        for i in range(n):
            if i in vis:
                continue
            comp = []
            dfs(i, comp)
            if all(len(adj[node]) == len(comp) - 1 for node in comp):
                ans += 1

        return ans
