t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    pos = [0] * (n + 1)
    for i in range(n):
        pos[p[i]] = i

    segments = 1
    for i in range(2, n + 1):
        if pos[i] < pos[i - 1]:
            segments += 1

    print(segments - 1)
