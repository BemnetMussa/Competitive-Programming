class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """
        given nums[int] 
        reqeusted to check if it is possible to get two subsets that there sum can be equal to each other 

        Approche: 
        since we are trying to get two subsets that are equal to each others.
        so by finding the sum(nums) // 2 if we can reach this target it is possile. 

        - we can track both the subsets and tracking them until there sum will be equal but it will complected
        - to optimize this we will use target which will be the half of the sums

        so how we can know if they can reach target or not
        by using recurssion. going through each subsets and taking if it taking or not taking the number so every single case will be handled
        
        Psudeocode will be: # by taking or not taking it every possiblity damm
            target = sum(nums)//2

            fucntion dp(curr_sum, idx):
                if curr_sum == target:
                    return true
                elif curr_sum > target or idx == len(nums):
                    return false

                        # don't take it                 # take it
                return dp(curr_sum, idx+1) or dp(curr_sum + nums[idx+1], idx+1)

        """

        target = sum(nums)
        
        # if odd
        if target % 2 != 0:
            return False

        target = target // 2

        @lru_cache(None)
        def dp(idx, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target or idx == len(nums):
                return False
            
            # take or skip
            return dp(idx+1, curr_sum) or dp(idx+1, curr_sum + nums[idx])
        
        
        return dp(0, 0)