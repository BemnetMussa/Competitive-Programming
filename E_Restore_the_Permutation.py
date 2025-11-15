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
    b = numbers()

    ranges = [[] for _ in range(n + 2)]  # index by left endpoint
    for i in range(n):
        l = (i + 1) // (b[i] + 1) + 1
        r = (i + 1) // b[i] if b[i] != 0 else n
        ranges[l].append((r, i))

    res = [0] * n
    pq = []

    for val in range(1, n + 1):
        for r, i in ranges[val]:
            heap.heappush(pq, (r, i))
        while pq:
            r, i = heap.heappop(pq)
            if r >= val:
                res[i] = val
                break

    print(*res)

if __name__ == "__main__":
    for _ in range(test_cases()):
        solve()
