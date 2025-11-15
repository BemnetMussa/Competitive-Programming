class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        result = 0

        for a, b in dominoes:
            key = tuple(sorted([a, b]))  # Ensure order doesn't matter (e.g., [1,2] and [2,1] are equivalent)
            result += counts[key]  # If we've seen this key before, we can form a pair
            counts[key] += 1  # Increment the count for this domino type
        
        return result
