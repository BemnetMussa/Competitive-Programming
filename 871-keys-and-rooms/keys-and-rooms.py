class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms) - 1
        # using hashmap for index : lists
        hashmap = defaultdict(list)

        for i , li in enumerate(rooms):
            hashmap[i] = li

        visited = set()

        def dfs(curr):

            visited.add(curr)

            for key in hashmap[curr]:
                if key not in visited:
                    dfs(key)

        dfs(0) # starting index 0
        total_sum = sum(visited)
        actual_sum = n * (n + 1) // 2
    
        return total_sum == actual_sum
        


