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

from collections import Counter

from collections import Counter


def solve():
    n, m = map(int, input().split())
    packages = list(map(int, input().split()))
    freq = Counter(packages)


    left, right = 1, m // n
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        particiants = sum(count // mid for count in freq.values()) if mid > 0 else 0

        if particiants >= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

if __name__ == "__main__":
    for _ in range(1):
        solve()
