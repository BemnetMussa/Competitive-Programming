class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        memo = {}
        def dp(curr_poss, unit):
            if curr_poss == stones[-1]:
                return True

            if (curr_poss, unit) in memo:
                return memo[(curr_poss, unit)]

            for jump in [unit, unit+1, unit-1]:
                if jump > 0 and curr_poss + jump in stones and dp(curr_poss + jump, jump):
                    memo[(curr_poss, jump)] =  True
                    return memo[(curr_poss, jump)]

            memo[(curr_poss, unit)] =  False
            return memo[(curr_poss, unit)]

        return dp(1, 1)



        









                


        