class Solution:
    def maxArea(self, height: List[int]) -> int:
        


        length = len(height)-1

        left = 0
        right = len(height)-1

        max_area = 0



        while left < right:

            if height[left] > height[right]:
                min_height = height[right]
                right -= 1
              
            else:
                min_height = height[left]
                left += 1
       

            area = length * min_height
            
            max_area = area if max_area < area else max_area


            length -= 1

        return max_area