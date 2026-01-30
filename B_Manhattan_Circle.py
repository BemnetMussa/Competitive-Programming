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
    n, m = numbers()
    matrix = [word() for _ in range(n)]
    
    # find the top "#"
    found = False
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "#":
                found = True
                break

        if found:
            break


    fixed_col = j
    while i+1 < n and j-1 >= 0 and matrix[i+1][j-1] != ".":
        i += 1
        j -= 1

    print(i+1, fixed_col+1)

if __name__ == "__main__":
    for _ in range(test_cases()):
        solve()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   