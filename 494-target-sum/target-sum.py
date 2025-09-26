class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        nums[int] every combo to reach target: int

        approche
        nums[int] the combos are by + and - 


        - state: res
        - base case: idx == len(nums)-1
        - recrusive relation: 

        presude
        count = 0
        function dp(idx, res):
            if idx == len(nums) and res == target:
                count += 1
            if idx == len(nums):
                return 0
            
            dp(idx+1, -1 * nums[idx] + res) # minus
            dp(idx+1, nums[idx] + res) # plus

        return count

        memo = (idx, res)
                #to keep track the length
                    # to keep track the result
                
        """
      
        memo = {}

        def dp(idx, res):
            if (idx, res) in memo:
                return memo[(idx, res)]

            if idx == len(nums):
                if res == target: 
                    return 1
                else:
                    return 0
       
            
            memo[(idx, res)] = dp(idx+1, -1 * nums[idx] + res) + dp(idx+1, nums[idx] + res)

            return memo[(idx, res)]
        
   
        return dp(0, 0)