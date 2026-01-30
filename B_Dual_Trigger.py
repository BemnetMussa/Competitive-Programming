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
        s = input().strip()

        ones_indices = []
        for i in range(n):
            if s[i] == '1':
                ones_indices.append(i)
        
        k = len(ones_indices)
        
        if k % 2 != 0:
            print("NO")
        elif k == 2:
            if ones_indices[1] == ones_indices[0] + 1:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")

if __name__ == "__main__":
    for _ in range(test_cases()):
        solve()
