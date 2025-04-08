class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white, gray, black = 0, 1, 2

        # build graph
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        color = {i: white for i in range(numCourses)}

        def dfs(course):
            if color[course] == gray:
                return False  # cycle found
            if color[course] == black:
                return True  # already processed

            color[course] = gray
            for child in graph[course]:
                if not dfs(child):
                    return False
            color[course] = black
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
