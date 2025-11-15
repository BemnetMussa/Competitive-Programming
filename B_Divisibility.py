from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

g = 1

#lcm(2, 3, 4, 5, ...) 
for num in range(2, 11):
    g = lcm(g, num)


n = int(input())


print(n // g)

