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

def accumulate(arr):
    return list(itertools.accumulate(arr))

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    total = sum(a)  
    need = (total)//3

    # prefix sums
    prefix_a = accumulate(a)
    prefix_b = accumulate(b)
    prefix_c = accumulate(c)



    # suffix sums
    suffix_a = accumulate(a[::-1])[::-1]
    suffix_b = accumulate(b[::-1])[::-1]
    suffix_c = accumulate(c[::-1])[::-1]


    print("-----------------------------")
    need_a_index = bisect_left(prefix_a, need)
    need_b_index = bisect_left(prefix_b, need)
    need_c_index = bisect_left(prefix_c, need)

    options = [
    (need_a_index, 'a'),
    (need_b_index, 'b'),
    (need_c_index, 'c')
]

    min_index, who = min(options)

    print(f"Minimum index: {min_index}, Who: {who}")

    # suffix also
    option_suffix = []
    if who == "a":
        need_b_index_suffix = bisect_left(suffix_b[::-1], need)
        need_c_index_suffix = bisect_left(suffix_c[::-1], need)
        option_suffix = [
            (need_b_index_suffix+n-2, 'b'),
            (need_c_index_suffix+n-2, 'c')
        ]
    elif who == "b":
        need_a_index_suffix = bisect_left(suffix_a[::-1], need)
        need_c_index_suffix = bisect_left(suffix_c[::-1], need)
        option_suffix = [
            (need_a_index_suffix+n-2, 'a'),
            (need_c_index_suffix+n-2, 'c')
        ]
    else:  # who == "c"
        need_a_index_suffix = bisect_left(suffix_a[::-1], need)
        need_b_index_suffix = bisect_left(suffix_b[::-1], need)
        option_suffix = [
            (need_a_index_suffix+n-2, 'a'),
            (need_b_index_suffix+n-2, 'b')
        ]

    if not option_suffix:
        print(-1)
        return 

    min_index_suffix, who_suffix = min(option_suffix)

    print(f"Minimum index (suffix): {min_index_suffix}, Who: {who_suffix}")

    if who == "a" and who_suffix == "b":
        zsum = prefix_a[need_b_index] 

    print(suffix_a)

    

if __name__ == "__main__":
    for _ in range(test_cases()):
        solve()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   