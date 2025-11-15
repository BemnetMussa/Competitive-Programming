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
        k = number()
        a = numbers()

     
        classPerWeek = sum(a)

   
        zmin_days = {} 
        aDouble = a + a

    
        for start_day in range(7):
        
            if a[start_day] == 0:
                continue
            
            attend = 0
       
            for days_passed in range(1, 8):
                idx = start_day + days_passed - 1
                if aDouble[idx] == 1:
                    attend += 1
                    
                    if attend not in zmin_days or days_passed < zmin_days[attend]:
                        zmin_days[attend] = days_passed

        # print(zmin_days)

        if k == 0 or not classPerWeek:
            print(0)
            return
            

        full_weeks = (k - 1) // classPerWeek
        remaining_classes = (k - 1) % classPerWeek + 1
        

        min_days_rem = zmin_days[remaining_classes]
        total_days = full_weeks * 7 + min_days_rem

        # print(full_weeks, remaining_classes, min_days_rem)
        
        print(total_days)


if __name__ == "__main__":
    for _ in range(test_cases()):
        solve()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   