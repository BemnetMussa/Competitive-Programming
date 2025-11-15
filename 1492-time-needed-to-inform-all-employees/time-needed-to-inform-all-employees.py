class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        '''
            finding the time requried to reach all employess *recurssiverly

            approche:
                starting from the headId then deciding through it by chocing on each level the max time
                bfs

                (time, node)
        '''

        # Step 1: Build the adjacency list 
        adj_list = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:  # Ignore the head (no manager)
                adj_list[manager[i]].append(i)

        # Step 2: BFS traversal to calculate max time
        queue = deque([(headID, 0)])  # (node, accumulated time)
        max_time = 0

        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)

            for subordinate in adj_list[node]:
                queue.append((subordinate, time + informTime[node]))

        return max_time

