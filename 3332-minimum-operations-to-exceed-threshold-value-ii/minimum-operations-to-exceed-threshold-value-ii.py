class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:  
            return 0

        operations = 0
        heapq.heapify(nums)  

        while len(nums) > 1 and nums[0] < k: 
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_val = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_val)
            operations += 1

        if nums[0] < k: # if not satisified
            return -1  

        return operations
