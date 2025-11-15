class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Attach index to each task
        for i in range(len(tasks)):
            tasks[i].append(i)

        # Sort tasks by enqueue time
        tasks.sort()

        result = []
        heap = []
        time = 0
        i = 0  # index in sorted task list

        while i < len(tasks) or heap:
            # Push all tasks that have arrived by 'time'
            while i < len(tasks) and tasks[i][0] <= time:
                enqueueTime, processingTime, index = tasks[i]
                heappush(heap, (processingTime, index))
                i += 1

            if heap:
                procTime, index = heappop(heap)
                time += procTime
                result.append(index)
            else:
                # No tasks available, jump time forward
                time = tasks[i][0]

        return result
