from math import floor

def count_divisible(n, x):
    return n // x

def count_good(l, r):
    total = r - l + 1

    def count_range(x):
        return count_divisible(r, x) - count_divisible(l-1, x)

    primes = [2, 3, 5, 7]
    from itertools import combinations

    # Inclusion-exclusion
    bad_count = 0
    for i in range(1, len(primes)+1):
        for combo in combinations(primes, i):
            lcm = 1
            for p in combo:
                lcm *= p
            c = count_range(lcm)
            if i % 2 == 1:
                bad_count += c
            else:
                bad_count -= c

    return total - bad_count

# Input reading and output:
t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(count_good(l, r))
