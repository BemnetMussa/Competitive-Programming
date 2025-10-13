class Solution:
    def countPrimes(self, n: int) -> int:
        
        # given n: Int, 
        # requested to get the number prime numbers less than n

        # approch:
            # factorize the primes from n upto 2 and return the number of prime numbers
            # or iterate from 2 upto sqrt(n) and track the number of prime numbers since it will be valid anytime but more than sqrt(n) also it is less than n so we should go upt to n
            # it will take Time complexity of O(n) and space of O(n)


        if n < 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)
