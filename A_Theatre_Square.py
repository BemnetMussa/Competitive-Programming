from math import ceil
n, m, k = map(int, input().split())

res = ceil(n/k) * ceil(m/k)

print(res)