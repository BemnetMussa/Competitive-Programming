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

from functools import lru_cache

def solve():
    s = input().strip()
    n = len(s)

    # Count "vv" pairs from the left
    left_vv = [0] * n
    count = 0
    for i in range(1, n):
        if s[i-1] == 'v' and s[i] == 'v':
            count += 1
        left_vv[i] = count

    # Count "vv" pairs from the right
    right_vv = [0] * n
    count = 0
    for i in range(n-2, -1, -1):
        if s[i] == 'v' and s[i+1] == 'v':
            count += 1
        right_vv[i] = count

    # For each 'o', multiply left and right "vv" counts
    result = 0
    for i in range(n):
        if s[i] == 'o':
            result += left_vv[i] * right_vv[i]

    print(result)


if __name__ == "__main__":
    for _ in range(1):
        solve()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   