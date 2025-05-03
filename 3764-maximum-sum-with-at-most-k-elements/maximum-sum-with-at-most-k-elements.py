class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # max heap
        max_heap = []

        for i in range(len(grid)):
            max_heap_row = self.to_max_heap(grid[i])
            for _ in range(limits[i]):
                val = -heappop(max_heap_row)
                heappush(max_heap, -val)
     
        ans = []
        for _ in range(k):
            ans.append(-heappop(max_heap))

        return sum(ans)
        


    def to_max_heap(self, arr):
        heapify(arr := [-x for x in arr])
        return arr