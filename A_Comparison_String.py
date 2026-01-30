t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    zmax = 1
    current = 1

    for i in range(1, n):
        if s[i] == s[i - 1]:
            current += 1
            zmax = max(zmax, current)
        else:
            current = 1

    print(zmax + 1)
