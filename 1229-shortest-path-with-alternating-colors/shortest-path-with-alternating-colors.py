from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        blue_graph = defaultdict(list)
        red_graph = defaultdict(list)

        for a, b in blueEdges:
            blue_graph[a].append(b)

        for a, b in redEdges:
            red_graph[a].append(b)

        """
        queue
        0 --> Red
        1 --> Blue
        """

        # initializing the queue with both colors from node 0
        queue = deque([(0, 0), (0, 1)])
        visited = set([(0, 0), (0, 1)]) # marking it as visited
        dist = 0

        nodes = [-1] * n

        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()

                if nodes[node] == -1:
                    nodes[node] = dist

                if color == 0:  # Last was RED, so next must be BLUE
                    for neighbor in blue_graph[node]:
                        if (neighbor, 1) not in visited:
                            visited.add((neighbor, 1))
                            queue.append((neighbor, 1))

                else:  # Last was BLUE, so next must be RED
                    for neighbor in red_graph[node]:
                        if (neighbor, 0) not in visited:
                            visited.add((neighbor, 0))
                            queue.append((neighbor, 0))

            dist += 1

        return nodes
