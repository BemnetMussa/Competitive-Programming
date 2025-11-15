class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        heap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff <= 0:
                continue
            
            bricks -= diff # using the bricks
            heappush(heap, -diff) # max heap
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heappop(heap)



        
        return len(heights) - 1  # Reached the last building

