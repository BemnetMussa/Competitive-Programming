t = int(input())

for _ in range(t):
    n = int(input())
    k = n // 2
    res = []

    for i in range(1, k + 1):
        res.append(k + i)
        res.append(i)

    if n % 2 != 0:
        res.append(n)

    print(*res)
