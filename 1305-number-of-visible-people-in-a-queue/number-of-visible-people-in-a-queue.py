class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []

        sees = []

        for i in range(len(heights)-1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
           
                stack.pop()
                count += 1
                

            if stack:
                count += 1
            
            stack.append(heights[i])

            sees.append(count)

        return sees[::-1]
