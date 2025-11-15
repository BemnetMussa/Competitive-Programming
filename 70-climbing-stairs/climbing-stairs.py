<<<<<<< HEAD
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Given n which is n steps requred to climb a starcase
        Requested in how many ways can we climb the starcases 
            - allowed either climb 1 or 2 stpes
        
        Approche
        1, 2, 1, 2, 1, 2, 1, 2, 1, 2
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1  
        1, 1, 1, 1, 1, 1, 2 ,1 ,1, 1 
        .........

        *keep track of every combo of steps until i reach n steps
        *keep track of  and generating the stpes eveyr step by using recursion
            - dp(i) + dp(i+1) -> which will allow us to keep track of all the steps 
        - we can go fruther by memroization such in that to keep track of the node ouptut for by using memo

        memo = hashmap/array

        function dp(k):
            # base case
            if k == 1:
                return 1 # it will not be less than this one because of constraints
            
            if k in memo:
                return memo[k]
            memo[n] =  dp(k) + dp(k+2)
            return memo[n]

        
        """

        memo = defaultdict(int)

        def dp(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            if memo[n]:
                return memo[n]
            
            memo[n] = dp(n-1) + dp(n-2)

            return memo[n]
        
        return dp(n)

            

            
=======
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
>>>>>>> 8e4622e2a8d09a8df92b1d80f3bb5bf1f1acf34a
