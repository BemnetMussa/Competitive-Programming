class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        WHITE = -1
        BLUE = 0
        RED = 1

        # Initially mark all nodes as unvisited
        colors = [WHITE for _ in range(len(graph))]

        def dfs(node, color):
            for neighbor in graph[node]:
                if colors[neighbor] == WHITE:
                    # Assign the opposite color to neighbor
                    colors[neighbor] = RED if color == BLUE else BLUE

                    if not dfs(neighbor, colors[neighbor]):
                        return 
                        
                elif colors[neighbor] == color:
                    # Not bipartite
                    return False
                    
            return True

        for node in range(len(graph)):
            if colors[node] == WHITE:
                colors[node] = BLUE
                if not dfs(node, BLUE):
                    return False

        return True
