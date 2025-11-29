def count(n):
    if n <= 0:
        return 0
    s = str(n)
    L = len(s)
    if L == 1:
        return n  # 1..n all valid
    
    # count all numbers with length < L
    res = 0
    res += 9  # all 1-digit (1..9)
    for length in range(2, L):
        res += 9 * (10 ** (length - 2))
    
    # handle length == L
    first = int(s[0])
    # numbers of length L with first digit < first(s)
    res += (first - 1) * (10 ** (L - 2))
    
    # numbers with same first digit and length L
    if L == 2:
        # candidate = dd
        candidate = int(s[0] + s[0])
        if candidate <= n:
            res += 1
    else:
        middle = s[1:-1]  # may be like '234' or ''
        res += int(middle) if middle != '' else 0
        candidate = int(s[0] + middle + s[0])
        if candidate <= n:
            res += 1

    return res

l, r = map(int, input().split())
print(count(r) - count(l - 1))
