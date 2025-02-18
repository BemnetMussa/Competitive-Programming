from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            # Find the intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:  # Valid intersection
                ans.append([start, end])

            # Move the pointer that has the smaller end time
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans
