class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        def findPath(node, visited):
            if node == destination:
                return True

            visited.add(node)

            for neigh in graph[node]:
             
                if neigh not in visited:
                    found = findPath(neigh, visited)
                    if found:
                        return True

            return False

        return findPath(source, set())
        
        