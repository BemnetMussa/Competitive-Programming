class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # Constracting a minHeap
        heap = []
        for i in range(n):
            for j in range(n):
                heappush(heap, matrix[i][j])

  
        while k > 1:
            heappop(heap)
            k -= 1 # decrement 
     

        return heap[0] if len(heap) > 0 else 0 # gives the kth largest element