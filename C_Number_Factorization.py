import sys
from collections import Counter


# def trial_division_simple(n: int) -> list[int]:
#    factorization: list[int] = []
#    d = 2
    #  while d * d <= n:
    #  while n % d == 0:
    #            factorization.append(d)
    #  n //= d
    #  d += 1
    #  if n > 1:
    #        factorization.append(n)
    #  return factorization


def get_prime_factorization(num):
  
    factors = Counter() # group the reptative ones
    d = 2
    temp = num
    while d * d <= temp:
        while temp % d == 0:
            factors[d] += 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] += 1
    return factors



for _ in range(int(input())):
    # approche get the prime factorization and dicitionary to track duplicates then key = primes and valu = power
    n = int(input())
    
    # get prime factorization as a dictionary
    factors = get_prime_factorization(n)
    total_sum = 0
    


    while factors:
        # current primes
        current_primes = list(factors.keys())
        # minimum power among them
        min_power = min(factors.values())
        
        # at one
        a = 1
        for p in current_primes:
            a *= p
            
     
        total_sum += a * min_power
        
        primes_to_remove = []
        for p in current_primes:
            factors[p] -= min_power

            if factors[p] == 0:
                del factors[p]
            
    print(total_sum)


