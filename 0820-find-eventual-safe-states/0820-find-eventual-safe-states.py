from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # check every path of a node and see if it leads to a terminal node
        '''
        terminal node = node with no outgoing edges
        safe node = every path from it leads to a terminal node or another safe node

        Approach:
        - find terminal nodes
        - use dfs to check each node
        - avoid cycles

        make it more efficient:
            if any path has a cycle => not safe
            else => safe
        '''

        safe = {}

        def dfs(node):
            if node in safe:  # already visited
                return safe[node]
            
            safe[node] = False  # mark as visiting
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False  # found a cycle
            
            safe[node] = True 
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res
