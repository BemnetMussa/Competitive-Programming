import sys
from math import isqrt

input = sys.stdin.readline

def build_permutation(n):
    p = [-1] * n
    i = n - 1
    while i >= 0:
        s = isqrt(i) 
        while s * s < i:
            s += 1
        square = s * s
        j = square - i  
        if j < 0 or j > i:
            return [-1]
        for k in range(i, j - 1, -1):
            p[k] = square - k
        i = j - 1
    return p

t = int(input())
for _ in range(t):
    n = int(input())
    res = build_permutation(n)
    print(*res)
