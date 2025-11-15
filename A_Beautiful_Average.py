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

    n = int(input())
    s = input()


    for i in range(1 << n):
        p_indices = []
        p_chars = []
        x_chars = []

 
        for j in range(n):
            if (i >> j) & 1:

                p_indices.append(j + 1)
                p_chars.append(s[j])
            else:
                x_chars.append(s[j])

        # --- Condition Checks ---

      
        p_string = "".join(p_chars)
        is_p_valid = (p_string == "".join(sorted(p_string)))


        x_string = "".join(x_chars)
        is_x_valid = (x_string == x_string[::-1])

        if is_p_valid and is_x_valid:
            print(len(p_indices))
            # The *p_indices unpacks the list for printing, e.g., [2, 3] becomes 2 3
            print(*p_indices)
            return

    # If the loop finishes without returning, no solution was found.
    print(-1)


if __name__ == "__main__":
    for _ in range(test_cases()):
        solve()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   