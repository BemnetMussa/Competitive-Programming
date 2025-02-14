class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        op = 0 
        nums.sort()

        heapq.heapify(nums)


        while nums[0] < k:

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            heapq.heappush(nums, (min(x,y) * 2 + max(x, y)))

            
            op += 1

        return op


