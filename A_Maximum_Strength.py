def solve():
    l, r = input().split()


    # make equal length
    if len(l) < len(r):
        l = l.rjust(len(r), '0')
    elif len(r) < len(l):
        r = r.rjust(len(l), '0')


    n = len(l)
    ans = 0
    for i in range(n):
        if l[i] != r[i]:
            ans = (int(r[i]) - int(l[i])) + 9 * (n - i - 1) # after diff rest can be 0 and 9 alternatively
            break
    print(ans)

t = int(input())
for _ in range(t):
    solve()
