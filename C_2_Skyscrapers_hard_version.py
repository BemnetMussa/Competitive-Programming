import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

L = [0]*n
R = [0]*n
stack = []

# left sums
for i in range(n):
    while stack and m[stack[-1]] > m[i]:
        stack.pop()

    if stack:
        j = stack[-1]
        L[i] = L[j] + m[i]*(i-j)
    else:
        L[i] = m[i]*(i+1)

    stack.append(i)

stack.clear()

# right sums
for i in range(n-1,-1,-1):
    while stack and m[stack[-1]] > m[i]:
        stack.pop()

    if stack:
        j = stack[-1]
        R[i] = R[j] + m[i]*(j-i)
    else:
        R[i] = m[i]*(n-i)

    stack.append(i)

peak = max(range(n), key=lambda i: L[i]+R[i]-m[i])

a = [0]*n
a[peak] = m[peak]

for i in range(peak-1,-1,-1):
    a[i] = min(m[i], a[i+1])

for i in range(peak+1,n):
    a[i] = min(m[i], a[i-1])

print(*a)