class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])

            if wealth > max_wealth:
                max_wealth = wealth

        

        return max_wealth

        