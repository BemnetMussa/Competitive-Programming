import math

def solve():
    n, m = map(int, input().split())

    gcd = math.gcd(n, m)
    m_simplified = m // gcd

    temp = m_simplified
    while temp % 2 == 0:
        temp //= 2

    if temp > 1:
        print(-1)
        return
    
    # print(m_simplified, temp)

    operations = 0
    while n % m != 0:
        remainder = n % m
        operations += remainder
        n += remainder

    print(operations)

t = int(input())
for _ in range(t):
    solve()
