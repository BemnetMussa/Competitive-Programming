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

import sys

def solve():
    n = number()
    a = numbers()
   
    results = []
    for i in range(n):
       
        if i == n - 1:
            results.append(0)
            continue
        midpoints = []
        for j in range(i + 1, n):
            if a[j] != a[i]:
                direction = 1 if a[j] > a[i] else -1
                midpoints.append((a[i] + a[j], direction))
        
        if not midpoints:
            results.append(0)
            continue

        current_count = sum(1 for mid, dir in midpoints if dir == -1)
        max_count = current_count
        midpoints.sort()
        
        for m_val, m_dir in midpoints:
            if m_dir == -1:
                current_count -= 1
            else:
                current_count += 1
            
            if current_count > max_count:
                max_count = current_count
        
        results.append(max_count)
    
    print(*results)

if __name__ == "__main__":
    for _ in range(test_cases()):
        solve()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   