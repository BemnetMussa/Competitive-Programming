class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count frequencies
        count = Counter(words)

        # Step 2: Min-heap of size k with (-freq, word)
        heap = []
        for word, freq in count.items():
            heappush(heap, (-freq, word))  # negative frequency for max-heap behavior

        # Step 3: Extract top k from heap
        result = [heappop(heap)[1] for _ in range(k)]

        return result
