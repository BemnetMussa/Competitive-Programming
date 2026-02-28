n = int(input())
a = list(input().strip())

k = a.count('H')
a = a + a

current = 0
for i in range(k):
    if a[i] == 'T':
        current += 1

min_swaps = current

# sliding window - hhththh,hhththh
for i in range(1, n):
    if a[i - 1] == 'T':
        current -= 1
    if a[i + k - 1] == 'T':
        current += 1

    min_swaps = min(min_swaps, current)

print(min_swaps)