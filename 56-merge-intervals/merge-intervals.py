'''
Given: an array of intervals[i] = [starti, endi], merge all overlapping intervals .
requested: to return the non overnalpping intervals 
solution:      



intervals = [[1,3],[2,6],[8,10],[15,18]]
     array =[[1, 6], [8, 10],  [15, 18]] -> return this non overalpping array

psudocode:
intervals.sort()
answer = [internvals[0]] # [1, 3]

for i in range(1, len(intervals)):
    start, end = intervals[i] # [2, 6]
    if answer[-1][1] >= start: # 3 >= 2
        answer[-1][1] = end # [1, 6]

return answer
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = [intervals[0]] # [1, 3]

        for i in range(1, len(intervals)):
            start, end = intervals[i] # [2, 6]
            if answer[-1][1] >= start: # 3 >= 2
                answer[-1][1] = max(end, answer[-1][1]) # [1, 6]
            else:
                answer.append([start, end])

        return answer # time compelxity O(nlogn) and space of O(n)