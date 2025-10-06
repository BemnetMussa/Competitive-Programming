class Solution:
    def rob(self, nums: List[int]) -> int:
        """

        Given a list of houses[int] 
        Requested to rob the gold (houses[i]) but can't rob two houses that are adjuscent at the same time
        
        Approche: 
        since we can rob two houses that are adjucent to each other at the *same time.
        so the way will be even or odd ways to rob the houses. compare them and return the max
        That it.
        no becase [2, 1, 3, 9] max is 10 but [2 ,9] = 11 sooo

        just by using DB can i do it! let's see
        nums = [1, 2, 3, 1]
        going through each index (knowing the alternatives ) then if the altenrative of th eothe is greater than the alternative of the prvious then we can hold that even or odd alternative as the soltuoin
        
        pseudocode
        funciton zmax(idx):
            if idx <= 0: return 0

            return max(zmax(idx-1), zmax(idx-2) + nums[idx])
        """

        @lru_cache(None)
        def zmax(idx):
            if idx < 0: 
                return 0

            return max(zmax(idx-1), zmax(idx-2) + nums[idx])

        return zmax(len(nums)-1)














        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]

    
        # prev1, prev2 = 0, 0


        # for num in nums:
        #     # For each house, determine if you should rob it or not
        #     temp = prev1
        #     prev1 = max(prev1, prev2 + num)
        #     prev2 = temp

        # # The maximum amount we can rob is stored in prev1
        # return prev1
