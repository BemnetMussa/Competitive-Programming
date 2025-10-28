'''
Given two positive integers left and right. find two integers nums1 and nums2 such that:
    - left <= num1 < num2 <= right .
    - Both num1 and num2 are prime numbers.
    - num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return ans = [nums1, nums2]  if multiple exists return the smallest one. (nums1)


Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

solution: 
- find the list of prime nubmers -> [11, 13, 17, 19] -> using prime factorization 
    - shoudl i itearte through it to find the it
- find the smallest closest gap which will be the first two ( by sorting based ont there difference from adjucent values)
            - nums.sort(lambda x: x[1] - x[0]) --> there was a method to do this but i forgot shittt hmmm somethign liek this or function creating one i forgot it. well it doesn't matter i will create it. let me just know how does this works.
            - [1, 2, 3]
            - [[1, 2], [2, 3]] grouping it and then sorting it base don the difference which will give nlogn which i gues will pass
- reutrn the first two values [nums[0], nums[1]]

-----------------------------------------------------------------------------------------------------------------------------------

forgot about the code and so on shitttt. 
'''

class Solution:
    def __init__(self):
        # self.sieve up to  right -- gives us primes that are valid upto right
        max_right = 10**6
        self.sieve = [True] * (10**6 + 1)
        self.sieve[0:2] = [False, False]
        
        for i in range(2, max_right + 1):
            if self.sieve[i]:
                for j in range(i*i, (max_right)+1, i):
                    self.sieve[j] = False

    def closestPrimes(self, left: int, right: int) -> list[int]:
        # collect prime numbers
        primes = [x for x in range(left, right+1) if self.sieve[x]]
        if len(primes) < 2:
            return [-1, -1]
        
        #find the minimum one
        min_gap = float('inf')
        ans = [-1, -1]

        for i in range(len(primes) -1):
            gap = primes[i+1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                ans = [primes[i], primes[i+1]]

        return ans

        

