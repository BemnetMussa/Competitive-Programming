import sys
from collections import defaultdict, deque



def solve():
    n, a, b = map(int, sys.stdin.readline().split())
    
    graph = defaultdict(list)
    for _ in range(n):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    if a == b:
        print("NO")
        return

    # --- Step 1: Find all nodes on the cycle ---
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    cycle_nodes = set()

    stack = [(1, -1)]
    while stack:
        u, p = stack.pop()

        if visited[u]:
            # Found a cycle; backtrack to get cycle nodes
            temp = p
            cycle_nodes.add(u)
            while temp != -1 and temp != u:
                cycle_nodes.add(temp)
                temp = parent[temp]
            break

        visited[u] = True
        parent[u] = p
        for v in graph[u]:
            if v != p:
                stack.append((v, u))

    # --- Step 2: BFS distances ---
    def bfs(start_node):
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        q = deque([start_node])
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    q.append(neighbor)
        return distances

    dist_from_a = bfs(a)
    dist_from_b = bfs(b)

    # --- Step 3: Check if Valeriu can win ---
    valeriu_can_win = any(dist_from_b[node] < dist_from_a[node] for node in cycle_nodes)

    print("YES" if valeriu_can_win else "NO")


# --- Main execution loop ---
try:
    num_test_cases = int(sys.stdin.readline())
    for _ in range(num_test_cases):
        solve()
except (IOError, ValueError):
    pass
