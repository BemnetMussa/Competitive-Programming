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