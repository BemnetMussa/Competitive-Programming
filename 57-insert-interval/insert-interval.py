class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
       
        intervals.extend([newInterval])
        intervals.sort()
        answer = [intervals[0]] # [1, 3]

        for i in range(1, len(intervals)):
            start, end = intervals[i] # [2, 6]
            if answer[-1][1] >= start: # 3 >= 2
                answer[-1][1] = max(end, answer[-1][1]) # [1, 6]
            else:
                answer.append([start, end])

        return answer # time compelxity O(nlogn) and space of O(n)

        