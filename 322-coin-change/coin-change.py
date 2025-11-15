<<<<<<< HEAD
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dp(rem):
            #basecases 
            if rem == 0:
                return 0
            if rem < 0:
                return float("inf") # sum(combunations) > amount

            if rem in memo:
                return memo[rem]
                
            mini = float("inf")
            for coin in coins: # unique coins
                length = dp(rem - coin)
                mini = min(mini, length + 1)

            memo[rem] = mini
            return mini

        return dp(amount) if dp(amount) != float("inf") else -1
=======
'''
Given: array coins[int] representing coins of different denominations and infinite amount of each denominations.
        amount: Int, total amount of money

Requested: return the fewest number of coins that are needed to make the amount.

constraints: 1 <= coins.length <= 12

IF THIS SOUNDS GOOD WE CAN CONTINUE

Approch: 
CAN YOU GIVE ME JUST 3 MINUTE TO THINK ABOUT THE APPROCH OR LET ME JUST SHOW YOU HOW I THINK! I THINK IT WILL BE BETTER.

coins = [1,2,5, 11], amount = 11

11 == amount -> 1 coin
1 + 1 + 1 + 1 + 1 == amount -> 5 coins
2 + 2 + 1 == amount -> 3 coins
5 + 5 (let just say there is no 1 only 2 ) = -1 != amount
....

How to choose the least number of coins. 
we can choose and start from the largest ones but will not gurantee

So the option that i think will be better based on the coins availabe using DP. WHICH WILL TAKE EVERY SINGLE POSSIBLITY AND ALONG THE WAY WE CAN KEEP TRACK HOW MUCH COINS THAT WE HAVE USED

lET ME RIGH THE PSUDOCODE:
THE BASE CASE: WHEN THE CURRENT AMOUNT => AMOUNT.
THE RECURSIVE RELATION: dp(i, curr_sum)
THE STATE: i, curr_sum

1 2, inf ==> 2
 \
  2  1 , inf ==> 1
   \
    3  # reach this 6 == amount(6) return 1


coins_size = len(coins)

def  leastNumCoinsMakesAmount(i, curr_sum):
    if curr_sum == amount:
        return 1 
    if curr_sum > amount:
        return float("inf") # excceds the amount

    min_coins = float("inf")
    for j in range(i, len(coins)):
        min_coins = min(min_coins, 1 + leastNumCoinsMakesAmount(j, curr_sum + coins[j]))

    return min_coins 


res = leastNumCoinsMakesAmount(0, 0) 

return res - 1 if res != float("inf") else -1

'''


        

class Solution:
    def coinChange(self, coins, amount):

        memo = {}
        def  leastNumCoinsMakesAmount(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float("inf") # excceds the amount

            # memoization
            if rem in memo:
                return memo[rem]

            min_coins = float("inf")
            for coin in coins:
                min_coins = min(min_coins, 1 + leastNumCoinsMakesAmount(rem - coin))
            
            memo[rem] = min_coins

            return min_coins 

        
        res = leastNumCoinsMakesAmount(amount) 

        return res if res != float("inf") else -1
>>>>>>> 8e4622e2a8d09a8df92b1d80f3bb5bf1f1acf34a
