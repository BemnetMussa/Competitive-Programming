class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        partner = {}
        for a, b in pairs:
            partner[a] = b
            partner[b] = a

        rank = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n-1):
                friend = preferences[i][j]
                rank[i][friend] = j

        unhappy = 0

        for x in range(n):
            y = partner[x]

            for u in preferences[x]:
                if u == y:
                    break

                v = partner[u]

                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break

        return unhappy
