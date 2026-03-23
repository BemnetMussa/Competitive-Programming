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

def z_algorithm(s):
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z

def solve():
    n, q = numbers()
    s = word()

    for _ in range(q):
        li, ri = numbers()
        li -= 1
        ri -= 1
        Len = ri - li + 1
        S = s[li:ri + 1]
        z = z_algorithm(S)

        max_at_reach = [-1] * (Len + 1)
        max_at_reach[Len] = 0
        current_max = 0
        max_r = Len
        total = 0

        for pos in range(1, Len + 1):
            dp_val = 1 + current_max
            total += dp_val
            if pos < Len:
                zz = z[pos]
                r = min(Len, pos + zz)
                val = dp_val
                if val > max_at_reach[r]:
                    max_at_reach[r] = val
                    if val > current_max:
                        current_max = val
                        max_r = r
                        
            if pos < Len and max_r < pos + 1:
                new_max = -1
                new_r = -1
                for k in range(pos + 1, Len + 1):
                    if max_at_reach[k] > new_max:
                        new_max = max_at_reach[k]
                        new_r = k
                current_max = new_max
                max_r = new_r

        print(total)

if __name__ == "__main__":
    for _ in range(test_cases()):
        solve()