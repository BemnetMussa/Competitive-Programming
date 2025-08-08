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
        l1, b1, l2, b2, l3, b3 = numbers()

        # since l3 <= l2 <= l1 and b3 <= b2 <= b1
        # rearranging 3 rectangles to form a square

        # 2 cases horizontally and vertically 
        # 1 case
        if l2 == l3:
        
            nb = b2 + b3

            if nb == b1 and l1 + l2 == nb:
                return print("YES")
            
        if b2 == b3:
            nl = l2 + l3

            if nl == l1 and b1 + b2 == nl:
                return print("YES")
            
        if b2 == b3 and l2 == l3:
            if b1 + b2 + b3 == l2:
                return print("YES")
               
        return print("NO")



        



    if __name__ == "__main__":
        for _ in range(test_cases()):
            solve()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    