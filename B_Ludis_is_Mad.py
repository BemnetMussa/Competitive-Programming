import math

t = int(input())
for _ in range(t):

    n = int(input())
    a = []
    b = []

    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    tm = list(map(int, input().split()))

    curr_time = 0
    for i in range(n):
        travel = (a[i] - (b[i-1] if i > 0 else 0)) + tm[i]
        
        curr_time += travel
        if i == n - 1:
            break
        min_stay = math.ceil((b[i] - a[i]) / 2)
        curr_time = max(curr_time + min_stay, b[i])

    print(curr_time)
