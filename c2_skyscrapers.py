
n = int(input())
m = list(map(int, input().split()))

L = [0] * n
R = [0] * n

stack = []

# From the left to the right -> increase  - peak - decrease
for i in range(n):
    while stack and stack[-1] > m[i]:
        stack.pop()
    if stack:
        j = stack[-1]
        L[i] = L[i] + (i-j) * m[i] # increasing order fro all i -> j indexis 
    else:
        L[i] = (i+1) * m[i]

    stack.append(i)

stack = []

# From the left to the right -> Decrease - peak - increase
for i in range(n-1, -1, -1):
    while stack and stack[-1] > m[i]:
        stack.pop()
    if stack:
        j = stack[-1]
        R[i] = R[i] + (j-i) * m[i]
    else:
        R[i] = (n-1)*m[i]

    stack.append(i)

# find best peak
best = 0 
peak = 0

for i in range(n):
    val = L[i]+ R[i] - m[i]
    if val > best:
        best = val
        peak = i

# reconstrcut answer
a = [0] * n
a[peak] = best

for i in range(peak-1, -1, -1):
    a[i] = min(m[i], a[i+1])

for i in range(peak+1, n):
    a[i] = min(m[i], a[i-1])

print(*a)
