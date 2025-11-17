class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainderCount = defaultdict(int)

        # Count normalized remainders
        for num in arr:
            rem = (num % k + k) % k
            remainderCount[rem] += 1

        for r in remainderCount:
            if r == 0:
                if remainderCount[r] % 2 != 0:
                    return False
            elif r * 2 == k:  # Special case when r == k/2
                if remainderCount[r] % 2 != 0:
                    return False
            else:
                if remainderCount[r] != remainderCount[k - r]:
                    return False

        return True
