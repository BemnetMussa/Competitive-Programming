'''
Given: number of stairs n: int 
    - we can either climb 1 or 2 stpes, in how many distinct climb to the top 

REquested: to get in houw many distinc clibm that i can climb 

constratins: 1 <= n <= 45

approch: 
 n = 2
1 + 1 = 2
1 + 2 = 2  --> so tow ways 

we should consider all of the posibilites
on that case we will use dp to solve this problem 

n = 3

            3
           / \
          2   1
         / \
        1   0

'''

class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def waysClimb(n):
            if n == 0:
                return 1
            if n < 0:
                return 0

            if n in memo:
                return memo[n]

            oneStep = waysClimb(n-1)
            twoStep = waysClimb(n-2)

            memo[n] = oneStep + twoStep

            return memo[n]

        return waysClimb(n) # time compelxity = O(n) and space compelixty O(n)