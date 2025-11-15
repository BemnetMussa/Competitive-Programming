class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count = Counter(nums)

        # Step 2: Create a min-heap of size k
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))  # push (frequency, number)
            if len(heap) > k:
                heapq.heappop(heap)  # remove smallest frequency

        # Step 3: Extract just the numbers from the heap
        return [num for freq, num in heap]
