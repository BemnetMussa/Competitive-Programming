class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        from collections import Counter
        count = Counter()
        global_min = float('inf')

        for a, b in zip(basket1, basket2):
            count[a] += 1
            count[b] -= 1
            global_min = min(global_min, a, b)

        excess = []

        for key, val in count.items():
            if val % 2 != 0:
                return -1
            excess += [key] * (abs(val) // 2)

        excess.sort()
        return sum(min(x, 2 * global_min) for x in excess[:len(excess)//2])