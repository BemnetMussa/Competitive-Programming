'''
Given directed acyclic graph -- with no cycle. 
Requested to get all unique paths from the node 0. 

approch: 
    traversing the nodes starting from node 0
    keep track of the unique paths 
    return the unqiue paths
'''


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []

        def dfs(node, path):
            
            path.append(node)
            
            if node == len(graph)-1:
                res.append(path[:])
            else:
                for neigh in graph[node]:
                    dfs(neigh, path)

            path.pop()

        dfs(0, [])
        return res