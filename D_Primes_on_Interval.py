
a, b, k = map(int, input().split())

# which is prime
def is_prime(a):
    if a < 2:
        return False
    
    i = 2

    while i * i <= a:
        if a % i == 0:
            return False
        i += 1

    return True


# # count primes in range
# def count_primes_in_range(x, y):
#     counter = 0
#     for num in range(x, y+1):
#         if is_prime(num):
#             counter += 1

#     return counter

def valid(l):
    for x in range(a, b - l + 2):
        y = x + l - 1
        if count_primes_in_range(x, y) < k:
            return False 
    return True


# a prefix sum array for prime count 
prime_count_prefix = [0] * (b + 1)
for i in range(1, b + 1):
    prime_count_prefix[i] = prime_count_prefix[i-1] + (1 if is_prime(i) else 0)

# how many primes in the range x upto y
def count_primes_in_range(x, y):
    if x > y:
        return 0

    if x <= 0:
        x = 1
    return prime_count_prefix[y] - prime_count_prefix[x-1]

# the range of l 
low = 1
high = b-a + 1
ans = float("inf")
while low <= high:
    l = low + (high - low) // 2
    if valid(l): 
        ans = l
        high = l-1
    else:
        low = l + 1
# O(logn * n * n) > 10^6
# updated O(long*n)
print(ans if ans != float("inf") else -1)