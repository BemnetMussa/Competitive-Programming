import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
     
        op = 0
        heapq.heapify(nums)
        print(nums)
   
        while nums[0] < k:
       
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            new_value = x * 2 + y
            
            heapq.heappush(nums, new_value)
         
            op += 1
        
        return op
