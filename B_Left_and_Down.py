from math import gcd

def solve():
    a, b, k = map(int, input().split())
    
    # If already at (0,0), no cost needed
    if a == 0 and b == 0:
        print(0)
        return
    
    g = gcd(a, b)
    
    # minimal step is (a/g, b/g)
    if (a // g) <= k and (b // g) <= k:
        print(1)
    else:
        print(2)

for _ in range(int(input())):
    solve()
