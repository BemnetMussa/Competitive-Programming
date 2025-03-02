class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        


        trips.sort(key=lambda x: x[1])

        heap = []
        curr_capacity = 0


        for i in range(len(trips)):
            numPassangers, start, end = trips[i]
         
            while heap and heap[0][0] <= start:
                curr_capacity -= heap[0][1]
                heapq.heappop(heap)
            
            curr_capacity += numPassangers
   
            if curr_capacity > capacity:
                return False
         
            heapq.heappush(heap, [end, numPassangers])
            

        return True
     
            
