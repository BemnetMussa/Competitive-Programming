'''

Given:
- array coins representing coins of different denominations and an integer amount representing a total amount of money.
- return the number of combinations that make up the amount. 

'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N_coins = len(coins)
        # Top-down approche
        # memo = {}
        # def numCombinations_thatMakesUpTheAmount(idx, total):
        #     if total == amount:
        #         return 1

        #     if total > amount or idx == N_coins:
        #         return 0
            
        #     if (idx, total) in memo:
        #         return memo[(idx,total)]

        #     res = numCombinations_thatMakesUpTheAmount(idx, total + coins[idx]) + numCombinations_thatMakesUpTheAmount(idx + 1, total)
        #     memo[(idx, total)] = res
        #     return memo[(idx, total)]

        # return numCombinations_thatMakesUpTheAmount(0, 0)
        

        # Bottom-up approche
        dp = [0] * ( amount + 1 )
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

