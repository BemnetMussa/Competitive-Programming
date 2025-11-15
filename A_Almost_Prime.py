def trial_division_distinct(n):
    factors = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.add(d)
            while n % d == 0:
                n //= d
        d += 1

    if n > 1:
        factors.add(n)

    return factors




n = int(input())
count = 0

for i in range(2, n + 1):
    if len(trial_division_distinct(i)) == 2:
        count += 1

print(count)
