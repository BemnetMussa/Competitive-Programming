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

    adj_list = defaultdict(list)
    parent = {}
    respect = {}
    root = -1

    for i in range(1, n + 1):
        p, r = numbers()
        parent[i] = p
        respect[i] = r
        if p != -1:
            adj_list[p].append(i)
        else:
            root = i

    queue = deque([root])
    ans = []

    while queue:
        node = queue.popleft()
        children = adj_list[node]
    
        disrespectful = 0
        total = 0

        for child in children:
            queue.append(child)
            total += 1
            if respect[child] == 1:
                disrespectful += 1
        # print(disrespectful, total, "dis, res")
        if total >= 0 and total == disrespectful and respect[node] == 1:
            ans.append(node)


    if not ans:
        print(-1)
    else:
        print(*sorted(ans))

if __name__ == "__main__":
    for _ in range(1):
        solve()
