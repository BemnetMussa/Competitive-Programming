    # -----------------------------
    # Language: Python 3
    # Author: Bemnet
    # -----------------------------

    import sys
    from math import ceil, floor, sqrt, gcd, inf, log2, isqrt, lcm
    import itertools
    import heapq as heap
    from collections import defaultdict, Counter, deque
    from bisect import bisect_left, bisect_right
    from random import randint

    input = sys.stdin.readline

    number = lambda: int(input().strip())
    numbers = lambda: list(map(int, input().strip().split()))
    so = lambda: sorted(map(int, input().strip().split()))
    word = lambda: input().strip()
    words = lambda: input().strip().split()
    yn = lambda cond: "YES" if cond else "NO"
    prefix_sum = lambda arr: list(itertools.accumulate(arr))
    rand = randint(1, 10**9)
    xor = lambda x: x ^ rand

    def test_cases(custom_cases=0):
        return number() if not custom_cases else custom_cases

    def to_min_heap(arr):
        heap.heapify(arr)
        return arr

    def to_max_heap(arr):
        heap.heapify(arr := [-x for x in arr])
        return arr

    def solve():
        n = number()
        a = numbers()

        if n == 0:
            print(0)
            return
        
        total = 0
        for i in range(n-1):
            total += abs(a[i] - a[i+1])

        ans = total

        # Case 1: Remove the first 
        ans = min(ans, total - abs(a[0] - a[1]))

        # Case 2: Remove the last 
        ans = min(ans, total - abs(a[n-2] - a[n-1]))

        # Case 3: Remove an element from the middle 
        for i in range(1, n-1):
            current_removal = (total 
                            - abs(a[i-1] - a[i]) 
                            - abs(a[i] - a[i+1]) 
                            + abs(a[i-1] - a[i+1]))
            if current_removal < ans:
                ans = current_removal
        
        print(ans)


    if __name__ == "__main__":
        for _ in range(test_cases()):
            solve()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    