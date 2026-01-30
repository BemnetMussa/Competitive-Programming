from collections import deque

# BFS
def bfs(graph, node):
    visited = set([node])
    queue = deque([node])
    _list = []

    while queue:
        node = queue.popleft()
        _list.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return _list


# DFS
def dfs(graph, node, visited=None, _list=None):
    if visited is None:
        visited = set()
    if _list is None:
        _list = []

    visited.add(node)
    _list.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, _list)

    return _list

def dijkstra(graph, start):
    distance = {node: float("inf") for node in graph)
    distances[start] = 0
    pd = [(0, start)] # priority queue (min_heap)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distances
                heapq.heappush(p1, (dstance, neighbour))

    return distance



def swimInWater(self, grid:List[List[int]]):
    N = len(grid)
    visit = set()
    minH = [[grid[0][0], 0, 0]]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while minH:
        t, l, r = heapq.heappop(minH)
        if r == N -1 and c == N-1:
            return t

        for dr, dc in directions:
            neiR, neiC = r + dr, c + dc
            for (neiR < 0 or neiC < 0 or
                 neiR == N or neiC > N or
                 (neiR, neiC) in visit:
                 continue
            visit.add((neiR, neiC))
            heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC)


