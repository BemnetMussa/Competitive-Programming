
n, m = map(int, input().strip().split())

compress = []
current_size = 0
for _ in range(n):
    a, b = map(int, input().strip().split())
    current_size += a
    compress.append( a - b )

compress.sort(reverse=True)
count = 0
for c in compress:
    if current_size <= m:
        break
    current_size -= c
    count += 1

if current_size <= m:
    print(count)
else:
    print(-1) # Time complexity: O(nlogn), Space complexity: O(n)
