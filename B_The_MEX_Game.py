for _ in range(int(input())):

    n = int(input())
    a = list(map(int, input().split()))

    zeros = a.count(0)
    ones = a.count(1)

    if 2 * zeros <= n + 1:
        print(0)
        continue

    if zeros + ones < n or ones == 0:
        print(1)
        continue

    print(2)
