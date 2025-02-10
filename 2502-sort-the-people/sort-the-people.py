class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        for i in range(len(heights)-1):

            if heights[i] < heights[i+1]:
                for i in range(i, -1, -1):
                    if heights[i] < heights[i+1]:
                        heights[i], heights[i+1], = heights[i+1], heights[i]
                        names[i], names[i+1] = names[i+1], names[i]
                    
            

        
        print(heights)


        return names