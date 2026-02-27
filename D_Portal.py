import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    x = int(data[index + 1])
    y = int(data[index + 2])
    index += 3
    p = [int(data[index + i]) for i in range(n)]
    index += n

    L = p[:x]
    M = p[x:y]
    R = p[y:]
    S = L + R
    ls = len(S)

    if ls == 0:
        minm = min(M)
        pos = M.index(minm)
        res = M[pos:] + M[:pos]
    else:
        s0 = S[0]
        minm = min(M)
        if minm < s0:
            pos = M.index(minm)
            res = M[pos:] + M[:pos] + S
        else:
            pos = M.index(minm)
            B = M[pos:] + M[:pos]
            best_k = ls
            for kk in range(1, ls):
                if minm < S[kk]:
                    best_k = kk
                    break
            res = S[:best_k] + B + S[best_k:]

    print(' '.join(map(str, res)))