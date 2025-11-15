class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # 1514. Path with Maximum Probabilyt
        '''
        Given: an undirected weighted graph of n nodes ( 0-indexed ). represented by an edge list where edges[i] = [a, b], succProb[i] is the prbabily of success

        n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2

        REquested: max prbabily of success to go from start to end and return it's success probabily 
        Approch: bfs approch on all nodes. keeping track of nodes
        itearte through it. keep track of the probabilty hold on!
        since there will be *start and *end what i created as a tree rather than keepign it graph
        '''

        # build graph with probabilties 
        adj_list = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            adj_list[u].append((v, prob))
            adj_list[v].append((u, prob))

        # Max-heap: (-probabilitey, node)
        heap = [(-1.0, start_node)]
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob # convert to positive
            if prob < max_prob[node]:
                continue

            if node == end_node:
                return prob
            
            for neigh, neigh_prob in adj_list[node]:
                new_prob = prob * neigh_prob
                if new_prob > max_prob[neigh]:
                    max_prob[neigh] = new_prob
                    heapq.heappush(heap, (-new_prob, neigh))

        return 0.0
