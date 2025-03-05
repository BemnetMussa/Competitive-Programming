class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)

        stack = []
        for i in range(len(temperatures)):
            while (stack and temperatures[stack[-1]] < temperatures[i]):
          
                res[stack[-1]] = i - stack[-1]
                stack.pop()
          
            stack.append(i)
        


        return res