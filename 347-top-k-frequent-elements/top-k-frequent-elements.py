class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []
        for n, count in counts.items():
            heapq.heappush(heap, (count, n))

            if len(heap) > k:
                heapq.heappop(heap)

        return [n for count, n in heap]